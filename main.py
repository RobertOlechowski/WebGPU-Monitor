from fasthtml.common import *
from starlette.testclient import TestClient

from source_code.config.ConfigLoader import ConfigLoader
from source_code.gpu.GpuDataSource import GpuDataSource
from source_code.helpers.DataRefresher import DataRefresher
from source_code.helpers.helpers import is_running_in_pycharm
from source_code.html.HtmlWrapper import HtmlWrapper

config_ds = DataRefresher(ds = ConfigLoader(), time_period=5)
_config = config_ds.get_last_data()



_links = [Link(rel='stylesheet', href='assets/styles.css', type='text/css'),
          Link(rel='stylesheet', href='assets/custom.css', type='text/css'),
          Link(rel='icon', href='assets/favicon.ico', type='image/x-icon'),
        ]

app, rt = fast_app(hdrs=tuple(_links), live=True)

data_source = DataRefresher(ds = GpuDataSource(config_ds), time_period=_config.app.refresh_period)
app_wrap = HtmlWrapper(app, config_ds)

@app.get("/", methods='get')
def home():
    data_snapshot = data_source.get_last_data()
    return app_wrap.render_main_page(data_snapshot)

print("Start App")

if is_running_in_pycharm():
    client = TestClient(app)
    print(client.get("/").text)
else:
    serve()





