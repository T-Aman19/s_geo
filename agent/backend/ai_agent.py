from langchain_community.llms import Ollama
import langgraph
import requests
from Geoserver import Geoserver

gsObject = Geoserver()

# 🌍 GeoServer API
GEO_URL = "http://localhost:8080/geoserver"
WORKSPACE_API_URL = "http://localhost:5000/api/get_workspace_layers"

# 🔥 Use Ollama (LLaMA 3.1)
llm = Ollama(model="llama3.1:8b")

def get_workspace_layers(workspace_name):
    """Fetch all layers in a workspace with their type and bounding box."""
    response =gsObject.get_layers(workspace_name)
    return response

def check_layer_existence(state):
    workspace_name = state["workspace"]
    user_query = state["query"]
    
    layers_info = get_workspace_layers(workspace_name)
    if not layers_info:
        return {"exists": False, "message": "Workspace not found or API error."}
    
    available_layers = {layer["name"]: layer for layer in layers_info["layers"]}

    # 🧠 Use LLaMA 3.1 to determine the relevant layer
    response = llm.invoke(f"Which GeoServer layer best matches this query: '{user_query}'? Available layers: {list(available_layers.keys())}")
    suggested_layer = response.strip()

    if suggested_layer in available_layers:
        layer_info = available_layers[suggested_layer]
        return {
            "exists": True,
            "layer": suggested_layer,
            "layer_type": layer_info["type"],
            "bounds": layer_info["extent"]
        }
    
    return {"exists": False, "message": "No relevant layer found for this query."}

# 🔗 LangGraph Pipeline
graph = langgraph.Graph()
graph.add_node("check_layer", check_layer_existence)
graph.set_entry_point("check_layer")
geo_agent = graph.compile()
