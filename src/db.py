import sqlite3

class Databaseconnect:
    def __init__(self):
        pass
    
    ## Setting up the database
    def init_db(self):
        conn=sqlite3.connect("feedback.db")
        cursor=conn.cursor()
        cursor.execute("""
                     CREATE TABLE IF NOT EXISTs feedback (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT NOT NULL,
                         email TEXT NOT NULL,
                         feedback TEXT NOT NULL,
                         sentiment TEXT
                     );
                     """)
        conn.commit()
        conn.close()    
    def check_db_content(self):    
        conn=sqlite3.connect("feedback.db")
        c=conn.cursor()
        c.execute("DELETE  FROM feedback")
        res=c.fetchall()
        conn.close()
        return res
   
'''
if __name__=="__main__":
    try:
        db=Databaseconnect()
        db.init_db()
        print(db.check_db_content())
        print("Database created successfully")
    except Exception as e :
        print(e)
       
        
'''


        