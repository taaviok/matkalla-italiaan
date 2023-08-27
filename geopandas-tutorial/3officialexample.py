#plots four cities on top of S America
# (9condageo_venv) C:\Users\aditya.kelekar\6conda_geopanda>python 3officialexample.py

#phase1 : display four cities of S America
#step1: make a geodatframe of given long and lat data

# writing in ship from Pihlajansaari back , 23.6.23
#phase2 : show the city names
#phase3 : web appln 
#phase4 : web appln - user enters a city name 

import pandas as pd
import geopandas
import matplotlib.pyplot as plt
from geodatasets import get_path  ### used for getting the background earth

df = pd.DataFrame(
    {
        "City": ["Buenos Aires", "Brasilia", "Santiago", "Bogota", "Caracas"],
        "Country": ["Argentina", "Brazil", "Chile", "Colombia", "Venezuela"],
        "Latitude": [-34.58, -15.78, -33.45, 4.60, 10.48],
        "Longitude": [-58.66, -47.91, -70.66, -74.08, -66.86],
    }
)


gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326"
)

print(gdf.head())

### -- for getting the background earth:
world = geopandas.read_file(get_path("naturalearth.land"))

# We restrict to South America.
ax = world.clip([-90, -55, -25, 15]).plot(color="blue", edgecolor="black")
### end -- for getting the background earth

# We can now plot our ``GeoDataFrame``.
gdf.plot(ax=ax, color="red")

plt.show()