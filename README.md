# Matkalla Italiaan

## Description

A city finder on world map built on Django and Leaflet.

<img
    src='./map_interface.png'
    style='max-width: 300px'>

## Installation

Step 1:

Clone the project. Python and pip are required. Also virtual environment is recommended. You can create and activate one using commands

```
python3 -m venv .venv
source .venv/bin/activate
```

Step 2: Install necessary python packages

```
pip install -r requirements.txt
```

Step 3: Run inside folder __djangoleaflet__

```
python manage.py runserver
```

## Troubleshooting

In case there is trouble with installing or running the packages concerning GDAL. Try these to fix the issue:

Step 1: Install development files for GDAL

```
sudo apt-get install libgdal-dev
```

Step 2: Check the version of libgdal-dev and be sure to install GDAL with same version

```
pip install gdal==”VERSION”
```

Step 3: GDAL uses use_2to3, so you need either disable it or install older setuptools version (58.0.0 or older) that still support it

```
pip install setuptools==58.0.0
```