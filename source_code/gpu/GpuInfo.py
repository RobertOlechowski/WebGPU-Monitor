import re

from source_code.helpers.helpers import setattr_ex, getattr_ex


class GpuInfo:
    def __init__(self, parsers, data):
        self.smi_version = None
        self.cuda_version = None

        data = data.split(",")
        self._parsers = parsers

        if len(data) != len(parsers):
            raise Exception("Problem output parse problem")

        for index, parser in enumerate(parsers):
            data_item = data[index]
            if isinstance(data_item, str):
                data_item = data_item.strip()
            setattr_ex(self, parser.target, data_item)

    def add_data(self, data):
        text = data.split("\n")[2]
        pattern = r"NVIDIA-SMI (\d+\.\d+).*?CUDA Version: (\d+\.\d+)"
        match = re.search(pattern, text)

        if match:
            self.smi_version  = match.group(1)
            self.cuda_version = match.group(2)

    def __str__(self):
        _results = ["[GpuInfoParser]"]
        for item in self._parsers:
            value = getattr_ex(self, item.target)
            _results.append(f"{item.query:>24} : {value}")

        return "\n".join(_results)
