# MyFirstGeoDjango

A GeoDjango project with PostGIS backend for storing and visualizing geographic polygon data (Japanese municipal boundaries).

## Tech Stack

- Python 3.7
- Django (GeoDjango)
- PostgreSQL / PostGIS
- GDAL

## Project Structure

```
geodjango/
├── geodjango/       # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── map/             # Map application
│   ├── models.py    # GeoData model with PolygonField
│   ├── admin.py     # OSMGeoAdmin registration
│   ├── bulk_insert.py # LayerMapping for GeoJSON import
│   └── data/        # GeoJSON data files
└── manage.py
```

## Features

- `GeoData` model with Django's `PolygonField` for geographic data
- Bulk import of GeoJSON data using `LayerMapping`
- OpenStreetMap-based admin interface via `OSMGeoAdmin`

## Prerequisites

- PostgreSQL with PostGIS extension
- GDAL library

## Setup

```bash
cd geodjango
pip install django psycopg2-binary
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Data Import

```bash
python manage.py shell
>>> from map.bulk_insert import run
>>> run()
```
