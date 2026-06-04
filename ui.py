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
        command = None
        item = options[a]
 
        if item.name == Items.END.name: return
        elif item.name == Items.LIST_OKRES.name:
                command = "SELECT * FROM okresy LIMIT 5;"
        elif item.name == Items.LIST_OBEC.name:
                command = "SELECT * FROM obce_pob LIMIT 5;"
        elif item.name == Items.FIND_OBEC.name:
                pass
        elif item.name == Items.STATS_OKRES.name:
                pass
 
        return command
 
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
