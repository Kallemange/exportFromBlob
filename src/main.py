import SQLExporter as sqlEx

class Config:
    def __init__(self):
        with open('../config.txt','r') as file:
            content = file.readlines()
            self.server = content[0].strip()
            self.database = content[1].strip()
            self.tables = content[2].split()
    def tostr(self):
        return 'Driver={SQL Server};Server='+self.server +';Database='+self.database +';Trusted_Connection=yes;'


def main():
    config = Config()
    exporter = sqlEx.SQLExporter(config)
    exporter.execSQL()
    print('klar')


if __name__ == "__main__":
    main()
