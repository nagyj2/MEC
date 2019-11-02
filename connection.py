import mysql.connector

class Connection():
    cnx = None
    cursor = None
    
    def __init__(self,user='root',passwd='rootroot',database='mec'):
        
        self._cred = [user,passwd,database]
        
    def opencnx(self):

        try:
            self.cnx = mysql.connector.connect(user=self._cred[0],
                                  password=self._cred[1],
                                  database=self._cred[2])
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Incorrect credentials")
            elif err.errno == errorcode.ER_BAD_DV_ERROR:
                print("Database not available")
            else:
                print(err)
                
    def closecnx(self):
        self.cnx.close()
        self.cnx = None
        
    def opencursor(self):
        self.cursor = self.cnx.cursor()
        
    def closecursor(self):
        self.cursor.close()
        self.cursor = None
                
    def query(self,query):
        if (not self.cnx.is_connected()):
            print("Not connected to database")
            return
        
        if (not self.cursor):
            print("Cursor not connected")
            return
            
        self.cursor.execute(query)
        try:
            return self.cursor.fetchall()
        except:
            return None
        
        
if __name__ == "__main__":
    db = Connection()
    db.opencnx()
    db.opencursor()

    result = db.query("show tables")
    print(result)
    result = db.query("insert into testtable values(34)")
    print(result)
    result = db.query("select * from testtable")
    print(result)

    db.closecursor()
    db.closecnx()
            
