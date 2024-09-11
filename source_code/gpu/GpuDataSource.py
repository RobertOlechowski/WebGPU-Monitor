import subprocess
import sys

from source_code.gpu.DataSnapshot import DataSnapshot
from source_code.gpu.GpuInfo import GpuInfo

class GpuDataSource:
    def __init__(self, config_ds):
        self.config_ds = config_ds

    @staticmethod
    def _call_smi_1(_config):
        _query = f"--query-gpu={','.join([a.query for a in _config.nvidia_smi])}"
        _cmd = ['nvidia-smi', _query, "--format=csv,noheader"]
        try:
            result = subprocess.run(_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error nvidia-smi: {e.output}", file=sys.stderr)
            raise

    @staticmethod
    def _call_smi_2(_config):
        _cmd = ['nvidia-smi']
        try:
            result = subprocess.run(_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error nvidia-smi: {e.output}", file=sys.stderr)
            raise

    def get_data(self):
        _config = self.config_ds.get_last_data()
        _output_csv = self._call_smi_1(_config).split("\n")
        _output_csv = [a for a in _output_csv if len(a)>0]
        _data_1 = [GpuInfo(_config.nvidia_smi, a) for a in _output_csv]

        _output_2 = self._call_smi_2(_config)
        for item in _data_1:
            item.add_data(_output_2)


        return DataSnapshot(_data_1)
