import os
from django.contrib.gis.utils import LayerMapping
from geodjango.map.models import GeoData

# Modelとファイルのカラムのマッピング
mapping = {
    'id': 'id',
    'geom': 'POLYGON',
}
# ファイルパス
geojson_file = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', '01-01101.geojson'))


# 実行
def run(verbose=True):
    lm = LayerMapping(GeoData, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)


if __name__ == '__main__':
    run()
