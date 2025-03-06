GEOSERVER_SERVICE_URL = "http://localhost:8080/geoserver"
WORKSPACE_REST_URL = f"{GEOSERVER_SERVICE_URL}/rest/workspaces"
GWC_REST_LAYER_URL=   "{GEOSERVER_SERVICE_URL}/gwc/rest/layers/{layer_name}.xml"
PERSISTENT_STORAGE_DIR = "uploads"

GLOBAL_SETTTINGS_URL = "{GEOSERVER_SERVICE_URL}/rest/services/{SERVICE}/workspaces/{WORKSPACE}/settings"

WMTS_GLOBAL_XML = "<wmts> <enabled>true</enabled> <name>WMTS</name> <title>GeoServer Web Map Tile Service</title> <maintainer>http://geoserver.org/com</maintainer> <abstrct>A compliant implementation of WMTS service.</abstrct> <accessConstraints>NONE</accessConstraints> <fees>NONE</fees> <versions> <org.geotools.util.Version> <version>1.0.0</version> </org.geotools.util.Version> </versions> <keywords> <string>WMTS</string> </keywords> <citeCompliant>false</citeCompliant> <onlineResource>http://geoserver.org</onlineResource> <schemaBaseURL>http://schemas.opengis.net</schemaBaseURL> <verbose>false</verbose> </wmts>"
WFS_GLOBAL_XML = """<wfs>
  <enabled>true</enabled>
  <name>WFS</name>
  <title>GeoServer Web Feature Service</title>
  <maintainer>http://geoserver.org/comm</maintainer>
  <abstrct>This is the reference implementation of WFS 1.0.0 and WFS 1.1.0, supports all WFS operations including Transaction.</abstrct>
  <accessConstraints>NONE</accessConstraints>
  <fees>NONE</fees>
  <versions>
    <org.geotools.util.Version>
      <version>1.0.0</version>
    </org.geotools.util.Version>
    <org.geotools.util.Version>
      <version>1.1.0</version>
    </org.geotools.util.Version>
    <org.geotools.util.Version>
      <version>2.0.0</version>
    </org.geotools.util.Version>
  </versions>
  <keywords>
    <string>WFS</string>
    <string>GEOSERVER</string>
  </keywords>
  <metadataLink/>
  <citeCompliant>false</citeCompliant>
  <onlineResource>http://geoserver.org</onlineResource>
  <schemaBaseURL>http://schemas.opengis.net</schemaBaseURL>
  <verbose>false</verbose>
  <metadata>
    <entry key="SHAPE-ZIP_DEFAULT_PRJ_IS_ESRI">false</entry>
  </metadata>
  <gml>
    <entry>
      <version>V_11</version>
      <gml>
        <srsNameStyle>URN</srsNameStyle>
        <overrideGMLAttributes>false</overrideGMLAttributes>
      </gml>
    </entry>
    <entry>
      <version>V_20</version>
      <gml>
        <srsNameStyle>URN2</srsNameStyle>
        <overrideGMLAttributes>false</overrideGMLAttributes>
      </gml>
    </entry>
    <entry>
      <version>V_10</version>
      <gml>
        <srsNameStyle>XML</srsNameStyle>
        <overrideGMLAttributes>true</overrideGMLAttributes>
      </gml>
    </entry>
  </gml>
  <serviceLevel>COMPLETE</serviceLevel>
  <maxFeatures>1000000</maxFeatures>
  <featureBounding>false</featureBounding>
  <canonicalSchemaLocation>false</canonicalSchemaLocation>
  <encodeFeatureMember>false</encodeFeatureMember>
  <hitsIgnoreMaxFeatures>false</hitsIgnoreMaxFeatures>
  <includeWFSRequestDumpFile>false</includeWFSRequestDumpFile>
  <getFeatureOutputTypeCheckingEnabled>false</getFeatureOutputTypeCheckingEnabled>
</wfs>"""
WMS_GLOBAL_XML = """<wms>
  <enabled>true</enabled>
  <name>WMS</name>
  <title>GeoServer Web Map Service</title>
  <maintainer>http://geoserver.org/comm</maintainer>
  <abstrct>A compliant implementation of WMS plus most of the SLD extension (dynamic styling). Can also generate PDF, SVG, KML, GeoRSS</abstrct>
  <accessConstraints>NONE</accessConstraints>
  <fees>NONE</fees>
  <versions>
    <org.geotools.util.Version>
      <version>1.1.1</version>
    </org.geotools.util.Version>
    <org.geotools.util.Version>
      <version>1.3.0</version>
    </org.geotools.util.Version>
  </versions>
  <keywords>
    <string>WMS</string>
    <string>GEOSERVER</string>
  </keywords>
  <metadataLink/>
  <citeCompliant>false</citeCompliant>
  <onlineResource>http://geoserver.org</onlineResource>
  <schemaBaseURL>http://schemas.opengis.net</schemaBaseURL>
  <verbose>false</verbose>
  <metadata>
    <entry key="disableDatelineWrappingHeuristic">false</entry>
    <entry key="kmlSuperoverlayMode">auto</entry>
    <entry key="kmlReflectorMode">refresh</entry>
    <entry key="svgAntiAlias">true</entry>
    <entry key="rootLayerInCapabilities">true</entry>
    <entry key="kmlPlacemark">false</entry>
    <entry key="kmlKmscore">40</entry>
    <entry key="mapWrapping">true</entry>
    <entry key="pngCompression">25</entry>
    <entry key="jpegCompression">25</entry>
    <entry key="advancedProjectionDensification">false</entry>
    <entry key="advancedProjectionHandling">true</entry>
    <entry key="kmlAttr">true</entry>
    <entry key="svgRenderer">Batik</entry>
    <entry key="MarkFactoryList"></entry>
    <entry key="scalehintMapunitsPixel">false</entry>
  </metadata>
  <watermark>
    <enabled>false</enabled>
    <position>BOT_RIGHT</position>
    <transparency>0</transparency>
  </watermark>
  <interpolation>Nearest</interpolation>
  <getFeatureInfoMimeTypeCheckingEnabled>false</getFeatureInfoMimeTypeCheckingEnabled>
  <getMapMimeTypeCheckingEnabled>false</getMapMimeTypeCheckingEnabled>
  <dynamicStylingDisabled>false</dynamicStylingDisabled>
  <featuresReprojectionDisabled>false</featuresReprojectionDisabled>
  <maxBuffer>25</maxBuffer>
  <maxRequestMemory>65536</maxRequestMemory>
  <maxRenderingTime>60</maxRenderingTime>
  <maxRenderingErrors>1000</maxRenderingErrors>
  <cacheConfiguration>
    <enabled>false</enabled>
    <maxEntries>1000</maxEntries>
    <maxEntrySize>51200</maxEntrySize>
  </cacheConfiguration>
  <transformFeatureInfoDisabled>false</transformFeatureInfoDisabled>
  <autoEscapeTemplateValues>false</autoEscapeTemplateValues>
</wms>"""

TILE_CACHING_XML = """
 <GeoServerLayer>
<enabled>true</enabled>
<inMemoryCached>true</inMemoryCached>
<name>{layer_name}</name> 
<blobStoreId>{blobStoreId}</blobStoreId>
<mimeFormats>
<string>application/vnd.mapbox-vector-tile</string>
<string>image/png</string>
<string>image/jpeg</string>
<string>application/json;type=geojson</string>
<string>application/json;type=topojson</string>
</mimeFormats>
<gridSubsets>
<gridSubset>
<gridSetName>EPSG:4326</gridSetName>
</gridSubset>
<gridSubset>
<gridSetName>EPSG:900913</gridSetName>
</gridSubset>
</gridSubsets>
<metaWidthHeight>
<int>4</int>
<int>4</int>
</metaWidthHeight>
<expireCache>0</expireCache>
<expireClients>0</expireClients>
<parameterFilters>
<styleParameterFilter>
<key>STYLES</key>
<defaultValue/>
</styleParameterFilter>
</parameterFilters>
<gutter>0</gutter>
<cacheWarningSkips/>
</GeoServerLayer>
    """



AWS_ACCESS_KEY='AKIAY74WNG3KQBN5T6OI'
AWS_SECRET_KEY='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'
S3_BUCKET='testimagesuat'