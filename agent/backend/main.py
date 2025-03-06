from fastapi import FastAPI
from pydantic import BaseModel
from ai_agent import geo_agent
import requests

app = FastAPI()

GEO_URL = "http://localhost:8080/geoserver"
USERNAME = "admin"
PASSWORD = "geoserver"

class QueryRequest(BaseModel):
    workspace: str
    query: str

@app.post("/query")
async def query_geoserver(request: QueryRequest):
    """AI-powered GeoServer query"""
    result = geo_agent.invoke({"query": request.query, "workspace": request.workspace})
    
    if not result.get("exists"):
        return {"error": result.get("message")}
    
    layer_name = result["layer"]
    layer_type = result["layer_type"]
    bounds = result["bounds"]

    if layer_type == "vector":
        wfs_url = f"{GEO_URL}/ows?service=WFS&version=1.0.0&request=GetFeature&typeName={request.workspace}:{layer_name}&outputFormat=application/json"
        response = requests.get(wfs_url, auth=(USERNAME, PASSWORD))
        geojson_data = response.json() if response.status_code == 200 else {"error": "Failed to fetch vector data"}
        return {"layer": layer_name, "type": layer_type, "bounds": bounds, "data": geojson_data}

    elif layer_type == "raster":
        return {"layer": layer_name, "type": layer_type, "bounds": bounds, "wms_url": f"{GEO_URL}/{request.workspace}/wms?"}
    
    return {"error": "Invalid layer type"}
