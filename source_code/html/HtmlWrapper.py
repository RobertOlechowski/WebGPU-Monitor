from fasthtml.common import *


def _render_footer():
    links = [("GitHub", "https://github.com/RobertOlechowski/WebGPU-Monitor"),
             ("Author", "https://robertolechowski.com/")
             ]

    links = tuple([Li(A(text, href=href)) for text, href, in links])
    ver = os.getenv('RR_BUILD_VERSION', None)
    if ver is None:
        return Footer(P("GPUWeb Monitor"), Ul(links))
    else:
        return Footer(P("GPUWeb Monitor"), P(ver, cls="ver"), Ul(links))

class HtmlWrapper:
    def __init__(self, app, config_ds):
        self._footer = _render_footer()
        self.config_ds = config_ds
        self.app = app

    def render_table(self, gpu_data):
        _config = self.config_ds.get_last_data()

        _cols = ["", *[a.name for a in gpu_data]]
        _head = Thead(Tr(*[Th(a) for a in _cols]))

        rows = []
        for item in _config.outputs:
            _row_data = [item.get_value(gpu_info) for gpu_info in gpu_data]
            _row_cells = [Td(a) for a in _row_data]
            rows.append(Tr(Th(item.title), *_row_cells))

        return Table(_head, Tbody(*rows))

    def render_main_page(self, data_snapshot):
        title = "GPUWeb Monitor"
        _header = Header(H1(title))
        table = self.render_table(data_snapshot.gpu_data)
        return Title(title), _header, Main(table, cls='container', hx_push_url='true', hx_swap_oob='true', id='main'), self._footer

    def render_to_text(self, url):
        from starlette.testclient import TestClient
        client = TestClient(self.app)
        print(client.get(url).text)






