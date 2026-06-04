import psycopg
import ui
 
class Connection:
        def __init__(self):
                self.conn = psycopg.connect(
                        host="192.168.135.10",
                        port=5432,
                        dbname="obce",
                        user="student",
                        password="bluemonkey3"
                )
                self.cursor = self.conn.cursor()
        def kill(self):
                self.cursor.close()
                self.conn.close()
        def getCursor(self):
                return self.cursor
        def execute(self, command):
                self.cursor.execute(command)
                rows = self.cursor.fetchall()
                for r in rows:
                        print(r)
 
def main():
        c = Connection()
        result = ui.menu()
        c.execute(result)
        c.kill()
 
if __name__ == "__main__":
        main()
