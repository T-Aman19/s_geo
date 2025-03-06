import streamlit as st
import folium
from streamlit_folium import folium_static
import requests

# 🔗 API Endpoint
FASTAPI_URL = "http://localhost:8000/query"

st.title("🌍 AI-Powered GeoServer Query Agent (LLaMA 3.1)")

# User Inputs
workspace_name = st.text_input("Enter Workspace Name")
user_query = st.text_input("Enter a geospatial query (e.g., 'show all roads in New York')")

if st.button("Search"):
    if user_query and workspace_name:
        response = requests.post(FASTAPI_URL, json={"query": user_query, "workspace": workspace_name})
        result = response.json()
        
        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"Layer '{result['layer']}' found! Type: {result['type']}")

            # Extract Auto-Center & Auto-Zoom
            bounds = result["bounds"]
            minx, miny, maxx, maxy = bounds
            center_lat, center_lon = (miny + maxy) / 2, (minx + maxx) / 2
            zoom_bounds = [[miny, minx], [maxy, maxx]]

            # 🗺️ Create Map
            m = folium.Map(location=[center_lat, center_lon], zoom_start=5)

            if result["type"] == "vector":
                folium.GeoJson(result["data"]).add_to(m)
            elif result["type"] == "raster":
                folium.raster_layers.WmsTileLayer(
                    url=result["wms_url"],
                    layers=result["layer"],
                    transparent=True,
                    fmt="image/png"
                ).add_to(m)

            m.fit_bounds(zoom_bounds)
            folium_static(m)
    else:
        st.warning("Please enter both workspace name and query.")
