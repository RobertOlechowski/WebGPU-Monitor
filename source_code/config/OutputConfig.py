from source_code.helpers.helpers import getattr_ex


class OutputConfig:
    def __init__(self, format_str=None, ref=None, title=None, path=None, smi_dict = None):
        self.ref = ref
        self.format_str = format_str
        self.path = path
        self.parser = smi_dict.get(self.ref, None)
        self.title = title or self.ref

    def get_value(self, gpu_info):
        if self.ref is not None and self.parser is not None:
            return getattr_ex(gpu_info, self.parser.target)

        if self.path is not None:
            return getattr_ex(gpu_info, self.path)

        if self.format_str is not None and isinstance(self.format_str, str):
            return self.format_str.format(gpu_info)

        if self.format_str is not None and isinstance(self.format_str, list):
            return "\n".join([a.format(gpu_info) for a in self.format_str])

        raise Exception(f"Can't generate value for [{self.ref}] [{self.title}]")