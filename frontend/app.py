import streamlit as st
import requests
import json
from streamlit_folium import st_folium
import folium
from langchain.agents import initialize_agent, AgentType
from langchain_core.runnables import RunnableConfig
from langchain.tools import Tool
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
import math
import Geoserver as gs
from langgraph.prebuilt import create_react_agent

gsObject = gs.Geoserver()


def latlon_to_tile(lat, lon, zoom):
    """Converts latitude and longitude to tile row and column numbers."""
    n = 2.0**zoom
    tile_x = int((lon + 180.0) / 360.0 * n)
    tile_y = int(
        (
            1.0
            - math.log(math.tan(math.radians(lat)) + (1 / math.cos(math.radians(lat))))
            / math.pi
        )
        / 2.0
        * n
    )
    return tile_x, tile_y


def query_geoserver(workspace, layer_name, layer_type, lat, lon, zoom=11):
    """Queries GeoServer for WMS (raster) or WMTS (vector) data."""
    base_url = "http://geoserver.bluehawk.ai:8080/geoserver"
    if layer_type == "raster":
        return f"{base_url}/wms?service=WMS&version=1.1.1&request=GetMap&layers={workspace}:{layer_name}&styles=&format=image/png&transparent=true"
    elif layer_type == "vector":
        tile_x, tile_y = latlon_to_tile(lat, lon, zoom)

        return f"http://13.202.93.120:8080/geoserver/{workspace}/gwc/service/wmts?layer={workspace}%3A{layer_name}&style=&tilematrixset=EPSG%3A4326&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image%2Fpng&TileMatrix=EPSG%3A4326%3A{zoom}&TileCol={tile_x}&TileRow={tile_y}"

    return "Invalid layer type"


def visualize_geoserver_data(url):
    """Displays GeoServer data on a Leaflet map in a new page."""
    st.page_link("/map", label="Click to open map", icon="map")

    if st.session_state.get("show_map", False):
        m = folium.Map(location=[20, 78], zoom_start=5)
        folium.raster_layers.WmsTileLayer(url=url, transparent=True).add_to(m)
        st_folium(m, width=700, height=500)


parser = StrOutputParser()

# Define LangChain agent tools
tools = [
    Tool(
        name="GeoServer Query",
        func=lambda params: query_geoserver(**json.loads(params)),
        description='Queries GeoServer for geospatial data. Input should be a JSON object with "workspace", "layer_name" and "layer_type" keys.',
    ),
    Tool(
        name="GeoServer Layer Check",
        func=lambda params: gsObject.check_layer_exists(**json.loads(params)),
        description='Checks if a layer exists on GeoServer and returns its type. Input should be a JSON object with "workspace" and "layer_name" keys.',
    ),
    Tool(
        name="GeoServer Workspace Layers list",
        func=lambda params: gsObject.get_layers(**json.loads(params)),
        description='Lists all the layers published inside a geoserver workspace. Input should be a JSON object with "workspace" key',
    ),
    Tool(
        name="GeoServer Workspace list",
        func=lambda: gsObject.get_workspaces(),
        description="Lists all the workspaces present on the geoserver instance. Requires no inputs.",
    ),
]

# Initialize LangChain agent
llm = Ollama(model="llama3.1:8b")
prompt = """You are an AI assistant integrated with GeoServer tools. Use the tools only when needed and return the final answer as soon as you have it. Do not keep asking follow-up questions unless explicitly requested. If you have retrieved the necessary information, present it clearly and stop."""

# agent = initialize_agent(
#     tools,
#     llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     verbose=True,

#     #stop_sequence=["Final Answer"],
#     max_iterations=5,

#     output_parser=parser,
#       agent_kwargs={
#         "system_message": (
#             "You are an AI assistant integrated with GeoServer tools. "
#             "Use the tools only when needed and return the final answer as soon as you have it. "
#             "Do not keep asking follow-up questions unless explicitly requested. "
#             "If you have retrieved the necessary information, present it clearly and stop."
#         )
#     }
# )

agent_executor = create_react_agent(llm, tools, prompt=prompt)

# Streamlit UI
st.title("Chat with Ollama Llama3.1 and GeoServer Integration")

# User input
user_query = st.text_area("Enter your query:")
if st.button("Submit") and user_query:
    with st.spinner("Generating response..."):
        response = agent_executor.invoke({"messages": [("user", user_query)]})
        st.text_area("Response:", response, height=400)

        # if (
        #     isinstance(response, dict) and "url" in response
        # ):  # If a GeoServer URL is detected
        #     visualize_geoserver_data(response["url"])

# Run the app with: `streamlit run script.py`
