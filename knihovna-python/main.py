import csv
import json
from tabulate import tabulate

class KnihovniSystem:
    def __init__(self, nazev_souboru):
        self.soubor = nazev_souboru
        self.knihy = self.nacti_knihy()
        
    def nacti_knihy(self):
        try:
            with open(self.soubor, 'r', encoding='UTF-8') as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            print('Nefacha ti soubor ')
            #return []
        except:
            print('Cosi sa nepovedlo mister')
        finally:
            pass
        
        
    def uloz_knihy(self):
        if self.knihy:
            fieldnames = self.knihy[0].keys()
            try:
                with open(self.soubor, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(self.knihy)
            except FileNotFoundError:
                print(f"Soubor {self.soubor} nrbyl nalezen")
            
    def import_json(self, json_soubor):
        try:
            with open(json_soubor, 'r', encoding='utf-8') as f:
                knihy = json.load(f)
            self.knihy = knihy
            self.uloz_knihy
            print("Knihy byly upsesne importovany")
        except FileNotFoundError:
            print(f"Soubor {json_soubor} nebyl nalezen.")
            
    def export_json(self, json_soubor):
        try:
            with open(json_soubor, 'x', encoding='UTF-8') as f:
                f.write(json.dumps(self.knihy, indent=4))
        except FileNotFoundError:
            print('Nefacha ti soubor ')
            #return []
        except:
            print('Nekde se neco nepocedlo')
                
            
    def zobraz_knihy(self):
        if not self.knihy:
            print("Zadne knihy nejsou dispozici")
            return
        header = {
            'isbn': 'ISBN',
            'nazev_knihy' : 'NÁZEV KNIHY',
            'autor' : 'AUTOR',
            'rok_vydani' : 'ROK VYDANÍ',
            'nakladatelstvi' : 'NAKLADATELSTVÍ',
            'zanr' : 'ŽÁNR',
            'pocet_stran' : 'POČET STRAN',
            'cena' : 'CENA'
        }
        
        table_data = [[kniha[key] for key in header.keys()] for kniha in self.knihy]
        print(tabulate(table_data, headers=header.values(), tablefmt='grid'))
        return
            
system = KnihovniSystem('knihy.csv')
system.uloz_knihy()
print(system.knihy[0]['nazev_knihy'])
system.zobraz_knihy()