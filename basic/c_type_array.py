import ctypes


class Array:
    def __init__(self, size):
        array_data_type = ctypes.py_object * size
        self.size = size
        self.memory = array_data_type()
        for i in range(size):
            self.memory[i] = None

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.memory[idx]

    def __setitem__(self, idx, value):
        self.memory[idx] = value


if __name__ == "main":
    array = Array(6)

    for i in range(len(array)):
        array[i] = i + 1

    for i in range(len(array)):
        print(array[i], end=', ')
