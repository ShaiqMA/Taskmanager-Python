#BRONNEN:
#https://www.youtube.com/watch?v=d6X00jiGmOE
#https://dev.to/lawaniej/a-simple-command-line-task-manager-in-python-4pba
# https://www.geeksforgeeks.org/python/python-classes-and-objects/
# python intro 4B Loops
# Python intro 2A Input, if else statements
# Python 9A Virtual environments
#  https://www.youtube.com/watch?v=wfcWRAxRVBA

#hierbij importeer ik functies om data te laden, opslaan,
#De rich library om een mooie console look, en tabbellen te krijgen 
from tasks.data_manager import load_tasks, save_tasks
from rich.console import Console
from rich.table import Table

console = Console()

#class aangemaakt om de taken te laden
class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

#hier zie je een tabel voor de taken met kolommen 
    def list_tasks(self):
        table = Table(title="Jouw Taken")
        table.add_column("ID", justify="right")
        table.add_column("Titel")
        table.add_column("Categorie")
        table.add_column("Prioriteit")
        table.add_column("Afgerond")

        #deze for loop zorgt ervoor dat alle taken die je hebt worden doorlopen,
        #deze taken worden als een rij toegevoeg in een tabel in de console
        for index, task in enumerate(self.tasks):
            # hierbij heb ik 2 variabelen gemaakt voor de prioriteitnummer, de bovenste heeft de kleuren voor de prioriteit
            # de onderste zorgt ervoor dat python de array juist telt, want python telft vanaf 0
            prioriteitKleuren = ["green", "bright_green", "yellow", "orange1", "red"]
            prioriteitKleur = prioriteitKleuren[task["Prioriteit"]-1]
            table.add_row(
                str(index + 1),
                task["Titel"],
                task["Categorie"],
                # deze f string haalt de kleur uit de array op basis van de nummer en zorgt ervoor dat het in Rich wordt toegepast
                f"[{prioriteitKleuren[task['Prioriteit'] - 1]}]{task['Prioriteit']}[/{prioriteitKleuren[task['Prioriteit'] - 1]}]",
                str(task["Afgerond"])
            )
        #print de tabel in de console
        console.print(table)

    #functie waarbij de gebruiker om details vraagt van de taak
    def add_task(self):
        #je zal een prompt krijgen waarbij je de titel cat en prioriteit moet invullen
        titel = input("Titel: ")
        
        # een array met allerlei categorieën
        Categorieën = [
            "1. Studie", 
            "2. Huishoudelijk", 
            "3. Werk", 
            "4. Hobby",
            "5. Persoonlijke Verzorging", 
            "6. Overig"
            ]
        
        # doorloopt alle categorieen doormiddel van een for in loop
        console.print("Categorieën")
        for cat in Categorieën:
            console.print (cat)

        # metr deze variabele maakt de gebruiker een keuze uit de categorieen, daarbij komt er een
        # if statement die kijkt of de nummer lager dan 1 is of hoger dan het aantal categorieën
        catkeuze = int(input("Kies een categorie voor je taak (vul de nummertje achter de categorie in!):"))
        if catkeuze < 1 or catkeuze > len(Categorieën):
            console.print("[red]ERROR[/red] Categoriekeuze ongeldig! [red]ERROR[/red]")
            return

        # zorgt ervoor dat de nummertje achter de categorie verwijnt
        categorie = Categorieën[catkeuze - 1].split(". ", 1)[1]

        prioriteit = int(input("Prioriteit (1-5): "))
        if prioriteit < 1 or prioriteit > 5: 
            console.print("[red]ERROR[/red] Prioriteit moet tussen 1 en 5 liggen! [red]ERROR[/red]")
            return

        #wordt toegevoegd aan de tabel
        self.tasks.append({
            "Titel": titel,
            "Categorie": categorie,
            "Prioriteit": prioriteit,
            "Afgerond": False
        })
        self.save_tasks()
        #print een bevestiging in groene kleur dat je taak is toegevoegd
        console.print(f"[green]'{titel}' toegevoegd![/green]")
        
    # hier definieer ik een complete task functie waarmee je de taak kan afronden
    def complete_task(self):
        # dit laat weer alle taken zien zodat je kan bekijken welke taak je wilt afronden
        self.list_tasks()
        # hier vraagt het de gebruiken om de taakid, -1 erachter gezet omdat python vanaf 0 begint tellen
        taakId = int(input("Welke taak wil je afronden? (voer de taak id in): ")) - 1

        #hier een if else statement, deze kijkt of de cijfer niet negatief is en of het kleiner is dan de aantal taken
        # zo ja, dan wordt de afgerond vakje veranderd naar true en krijg je een berichtje van goedkeuring
        # anders een foutmelding
        if 0 <= taakId < len(self.tasks):
            self.tasks[taakId]["Afgerond"] = True
            self.save_tasks()
            console.print(f"[green]Taak afgerond![/green]")
        else:
            console.print("[red]Taak ID is onjuist[/red]")
    
    # taken verwijderen functie gedifinieerd
    def delete_task(self):
        #laat een lijst van taken zien
        self.list_tasks()
        #vraagt jou een taakid in te vullen die je wilt verwijderen
        idTask = int(input("Welke taak wil je verwijderen? (geef het id nummer op): ")) - 1

        #checkt of de id die je invoert niet lager dan 0 of hoger dan de lengte is van de taken
        if 0 <= idTask < len(self.tasks):
            removeTask = self.tasks.pop(idTask)
            self.save_tasks()
            console.print(f"[red] '{removeTask['Titel']}'  verwijdered  [/red]")
        else:
            #zo niet krijg je een foutmelding
            console.print("[red] de ID is ongeldig[/red]")

    def show_statistics(self):
        # laat de lengte zien van een taak
        totaal = len(self.tasks)
        # door een for in loop dtelt het de aantal taken dei compleet zijn
        afgerond = sum(t["Afgerond"] for t in self.tasks)
        # laat de statistieken zien in de console
        console.print(f"Totaal: {totaal}, Afgerond: {afgerond}")

    def save_tasks(self):
        # roept de save task functie aan
        save_tasks(self.tasks)
        # belangrijk: bij alle functies zoals add remove en complete roep ik de functie aan zodat het opslaat