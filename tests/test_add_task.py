#BRONNEN: https://www.youtube.com/watch?v=3OmfTIf-SOU
# https://docs.python.org/3/library/unittest.html


# import van data manager en unittest
import unittest
from tasks.data_manager import save_tasks, load_tasks

# testclass voor mijn test
class TestAddTask(unittest.TestCase):

    def test_saveload(self):
        # een test taak die we gaan testen dus
        test_task = [{
            "Titel": "Test",
            "Categorie": "School",
            "Prioriteit": 3,
            "Afgerond": False
        }]
        # slaat op in json bestand
        save_tasks(test_task)
        # haalt op uit json bestand
        loadTask = load_tasks()
        # controoleert of titel gelijk is aan test
        self.assertEqual(loadTask[0]["Titel"], "Test")


    def test_returnlist(self):
        # deze test checkt namelijk of load_tasks niet gaat crashen en altijd een lijst retourneerd
        tasks = load_tasks()
        self.assertIsInstance(tasks, list)


if __name__ == "__main__":
    unittest.main("Test_Add_Task")