import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from lab6 import find_unreachable_cities

class TestGasPipelines(unittest.TestCase):
    def test_all_reachable(self):
        cities = ["Львів", "Стрий", "Долина"]
        storages = ["Сховище_1"]
        pipelines = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
            ["Стрий", "Долина"],
        ]
        self.assertEqual(find_unreachable_cities(cities, storages, pipelines), [])

    def test_partial_reachability(self):
        cities = ["Львів", "Стрий", "Долина"]
        storages = ["Сховище_1", "Сховище_2"]
        pipelines = [
            ["Сховище_1", "Львів"],
            ["Сховище_2", "Долина"],

        ]
        expected = [
            ["Сховище_1", ["Стрий", "Долина"]],
            ["Сховище_2", ["Львів", "Стрий"]],
        ]
        self.assertEqual(find_unreachable_cities(cities, storages, pipelines), expected)

    def test_disconnected_graph(self):
        cities = ["Місто_А", "Місто_Б"]
        storages = ["Сховище_А"]
        pipelines = []
        expected = [
            ["Сховище_А", ["Місто_А", "Місто_Б"]],
        ]
        self.assertEqual(find_unreachable_cities(cities, storages, pipelines), expected)

    def test_multiple_paths(self):
        cities = ["А", "Б", "В", "Г"]
        storages = ["СХ_1", "СХ_2"]
        pipelines = [
            ["СХ_1", "А"],
            ["А", "Б"],
            ["СХ_2", "В"],
            ["В", "Г"],
            ["Г", "А"],
        ]
        expected = [
            ["СХ_1", ["В", "Г"]],
        ]
        self.assertEqual(find_unreachable_cities(cities, storages, pipelines), expected)


if __name__ == "__main__":
    unittest.main()