class TableField:
    def __init__(self, name, data_type, input_type=""):
        self.name = name
        self.data_type = data_type
        self.input_type = input_type

    def getName(self):
        return self.name

    def getDataType(self):
        return self.data_type

    def getInputType(self):
        return self.input_type
