import yaml

from source_code.config.AppConfig import AppConfig
from source_code.config.Config import Config
from source_code.config.OutputConfig import OutputConfig
from source_code.config.SmiConfig import SmiConfig


def _config_constructor(loader, node):
    fields = loader.construct_mapping(node, deep=True)

    smi_data = [SmiConfig(**record) for record in fields['nvidia_smi']]

    smi_dict = {a.query: a for a in smi_data}

    outputs = [OutputConfig(**record, smi_dict=smi_dict) for record in fields['output']]

    app = AppConfig(**fields['app'])
    result = Config(app=app, nvidia_smi=smi_data, outputs=outputs)

    return result

yaml.add_constructor('!Config', _config_constructor)


class ConfigLoader:
    def __init__(self):
        pass

    def get_data(self):
        with open('config/config.yaml', 'r') as file:
            content = file.read()

        config = yaml.load(content, Loader=yaml.FullLoader)
        return config