#BRONNERN: 
# https://www.youtube.com/watch?v=nqx2kMgKRVo
# https://www.youtube.com/watch?v=d6X00jiGmOE


# import van de taskmanager klasse vanuit de task_manager file.
# import van risch library zodat de console een mooie look krijgt.
from tasks.task_manager import TaskManager
from rich.console import Console

console = Console()
manager = TaskManager()

# de hoofdmenu functie, via hier kan de gebruiker acties uitvoeren 
def main_menu():
    while True: 
        #dit print de opties in de console
        console.print("\n[bold blue]Efficiente TaskManager[/bold blue]")
        console.print("1. Bekijk taken")
        console.print("2. Voeg taak toe")
        console.print("3. Rond taak af")
        console.print("4. Verwijder taak")
        console.print("5. Statistieken")
        console.print("6. Afsluiten")

        keuze = input("Maak een keuze: ")

        # if else die zorgen voor functionaliteit wanneer de gebruiker 1 keuze maakt 
        if keuze == "1":
            manager.list_tasks()
        elif keuze == "2":
            manager.add_task()
        elif keuze == "3":
            manager.complete_task()
        elif keuze == "4":
            manager.delete_task()
        elif keuze == "5":
            manager.show_statistics()
        elif keuze == "6":
            console.print("Tot ziens!")
            break
        else:
            console.print("[red]Ongeldige keuze[/red]")

# zorgt ervoor dat de main_menu functie wordt uitgevoerd wanneer het script wordt gestart
if __name__ == "__main__":
    main_menu()