from enum import Enum
 
class Items(Enum):
        END = "Konec"
        LIST_OKRES = "Seznam okresu"
        LIST_OBEC = "Obce v okrese"
        FIND_OBEC = "Hledat obec"
        STATS_OKRES = "Statistiky okresu"
 
options = [
        Items.END,
        Items.LIST_OKRES,
        Items.LIST_OBEC,
        Items.FIND_OBEC,
        Items.STATS_OKRES
]

def choose_new_menu(a):
        query = None
        command = None
        item = options[a]
 
        if item.name == Items.END.name: return
        elif item.name == Items.LIST_OKRES.name:
                command = "SELECT * FROM okresy;"
        elif item.name == Items.LIST_OBEC.name:
                query = input("Zadej kod okresu: ")
                command = "SELECT obce_pob.nazev, SUM(obce_pob.pocet_obyvatel) AS pocet_obyvatel, AVG(obce_pob.prumerny_vek) AS prumerny_vek FROM obce_pob JOIN okresy ON obce_pob.id_okres = okresy.id_okres WHERE obce_pob.id_okres ILIKE (%s) GROUP BY obce_pob.nazev;"
        elif item.name == Items.FIND_OBEC.name:
                query = input("Zadej nazev obce: ")
                command = "SELECT nazev FROM obce_pob WHERE nazev ILIKE (%s);"
        elif item.name == Items.STATS_OKRES.name:
                query = input("Zadej kod okresu: ")
                command = "SELECT obce_pob.nazev, SUM(obce_pob.pocet_obyvatel) AS pocet_obyvatel, AVG(obce_pob.prumerny_vek) AS prumerny_vek FROM obce_pob JOIN okresy ON obce_pob.id_okres = okresy.id_okres WHERE obce_pob.id_okres ILIKE (%s) GROUP BY obce_pob.nazev;"
 
        if query is not None:
                query = query.split(", ")
                for i in range(len(query)): query[i] = f"%{query[i]}%"
                query = tuple(query)

        return (command, query)
 
def menu():
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
                        print(f"Please input a number between 0 and {len(options)-1}\n")
                        continue
                break
        return choose_new_menu(a)
