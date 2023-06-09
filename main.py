import geopandas
import matplotlib.pyplot as plt
import numpy as np

image_path = "images/"
data_path = "data/"

data_rg = data_path + "NUTS_RG_10M_2021_3035.geojson"
data_lb = data_path + "NUTS_LB_2021_3035.geojson"
data_bn = data_path + "NUTS_BN_10M_2021_3035.geojson"

gp_rg = geopandas.read_file(data_rg)
gp_lb = geopandas.read_file(data_lb)
gp_bn = geopandas.read_file(data_bn)

rg_figure = gp_rg.plot(figsize=(20,15), color="gray").figure
rg_figure.savefig(image_path + "geodata_ax.png")

lb_figure = gp_lb.plot(figsize=(20,15), color="red").figure
lb_figure.savefig(image_path + "geodata_lb.png")

bn_figure = gp_bn.plot(figsize=(20,15), color="blue").figure
bn_figure.savefig(image_path + "geodata_bn.png")

#ax = gp_rg.plot(figsize=(20,15), color="gray")
#gp_lb.plot(figsize=(20,15), ax=ax, color="yellow")
#gp_bn.plot(figsize=(20,15), ax=ax, color="red")
