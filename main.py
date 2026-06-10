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
	def execute(self, req):
		if req is None: return None
		self.cursor.execute(req.command, req.query)
		return self.cursor.fetchall()
 
def main():
	#c = Connection()
	res = 1
	while res is not None:
		req = ui.request()
		#res = c.execute(req)
		#if res is not None: ui.submit(res, req.format)
	#c.kill()
 
if __name__ == "__main__":
	main()
