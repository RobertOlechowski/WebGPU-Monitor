
class DataSnapshot:
    def __init__(self, gpu_data):
        self.gpu_data = gpu_data

    def dump(self):
        for item in self.gpu_data:
            print(item)
