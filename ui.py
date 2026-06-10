from enum import Enum
 
class Items(Enum):
	END = "Konec"
	LIST_OKRES = "Seznam okresu"
	LIST_OBEC = "Obce v okrese"
	FIND_OBEC = "Hledat obec"
	STATS_OKRES = "Statistiky okresu"
	TOP_OBEC = "Top 10 nejvetsich obci"
 
options = [
	Items.END,
	Items.LIST_OKRES,
	Items.LIST_OBEC,
	Items.FIND_OBEC,
	Items.STATS_OKRES,
	Items.TOP_OBEC
]

def submit(data, format):
	for chunk in data:
		output=format
		for i in chunk:
			output = output.replace("$", str(i), 1)
		if output.count('\n') > 0: output += '\n'
		print(output)

def getCommand(a):
	query = None
	command = None
	format = None
	item = options[a]
 
	if item.name == Items.END.name: return None
	elif item.name == Items.LIST_OKRES.name:
		command = "SELECT id_okres, nazev FROM okresy;"
		format = "$ $"
	elif item.name == Items.LIST_OBEC.name:
		query = input("Zadej kod okresu: ")
		command = "SELECT obce_pob.nazev, SUM(obce_pob.pocet_obyvatel) AS pocet_obyvatel, AVG(obce_pob.prumerny_vek) AS prumerny_vek FROM obce_pob JOIN okresy ON obce_pob.id_okres = okresy.id_okres WHERE obce_pob.id_okres ILIKE (%s) GROUP BY obce_pob.nazev;"
		format = "$\nPocet obyvatel: $\nPrumerny vek: $"
	elif item.name == Items.FIND_OBEC.name:
		query = input("Zadej nazev obce: ")
		command = "SELECT id_okres, nazev FROM obce_pob WHERE nazev ILIKE (%s);"
		format = "$ $"
	elif item.name == Items.STATS_OKRES.name:
		query = input("Zadej kod okresu: ")
		command = "SELECT obce_pob.nazev, SUM(obce_pob.pocet_obyvatel) AS pocet_obyvatel, AVG(obce_pob.prumerny_vek) AS prumerny_vek, AVG(obce_pob.prumerny_vek_muzi)/AVG(obce_pob.prumerny_vek_zeny) AS pomer FROM obce_pob JOIN okresy ON obce_pob.id_okres = okresy.id_okres WHERE obce_pob.id_okres ILIKE (%s) GROUP BY obce_pob.nazev;" 
		format = "$\nPocet obyvatel: $\nPrumerny vek: $\nPomer muzi zeny: $"
	elif item.name == Items.TOP_OBEC.name:
		command = "SELECT id_okres, nazev, pocet_obyvatel AS pocet_obyvatel FROM obce_pob ORDER BY pocet_obyvatel DESC LIMIT 10"
		format = "$ $ - $ obyvatel"

	if query is not None:
		query = query.split(", ")
		for i in range(len(query)): query[i] = f"%{query[i]}%"
		query = tuple(query)

	output = {
		"command":command,
		"query":query,
		"format":format
	}

	return output
 
def request():
	print("""
=========================
 DEMOGRAFIE ČR
=========================
	""")
	a = None
	while True:
		for i,v in enumerate(options):
			print(f"{i} - {v.value}")
		a = input("\nVyber: ")
		try:
			a = int(a)
			if a < 0 or a > len(options)-1:
				raise Exception()
		except Exception:
			print(f"Zadej cislo mezi 0 a {len(options)-1}\n")
			continue
		break
	print()
	return getCommand(a)
