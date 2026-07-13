
from .TableField import TableField
class TableFieldCollection:
    def __init__(self):
        self.fields = []

    def addField(self, name, data_type, input_type=""):
        field = TableField(name, data_type, input_type)
        self.fields.append(field)

    def getFields(self):
        return self.fields

    def findDataType(self, name):
        for field in self.fields:
            if field.getName() == name:
                return field.getDataType()
        return None
