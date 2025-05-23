import sqlite3

class Handler():
    def __init__(self, dbName):
        self.dbName = dbName
        self.conn = sqlite3.connect(f'{self.dbName}')
        self.cursor = self.conn.cursor()
    
    def GetTable(self, tableName):
        self.cursor.execute(f'''SELECT * FROM {tableName}''')
        data = self.cursor.fetchall()
        return data

if __name__ == "__main__":
    dbName = "C:\API\API\ApiDb.db"
    db = Handler(dbName)
    data = db.GetTable("Endpoints")
    print(data)