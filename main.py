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
        def execute(self, result):
                if result is None: return
                self.cursor.execute(result[0], result[1])
                return self.cursor.fetchall()
 
def main():
        #c = Connection()
        feedback = True
        while feedback:
                request = ui.menu()
                #result = c.execute(request)
                #feedback = ui.finish(result)
        #c.kill()
 
if __name__ == "__main__":
        main()
