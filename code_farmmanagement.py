# -*- coding: utf-8 -*-
"""Code_FarmManagement.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FspvdxCCtGJ39aaAO0G1secemXCbEDWP
"""

import random

class FarmManagementGame:
    def __init__(self):
        self.stats = {
            'Farm Productivity': 50,
            'Community Reputation': 50,
            'Financial Stability': 50,
            'Sustainability': 50,
            'Energy': 100,
            'Happiness': 100
        }
        self.animals = {'chickens': 10, 'cows': 5}
        self.researchers = 0
        self.competitors = {'competitor1': 50, 'competitor2': 45}
        self.year = 1
        self.max_years = 5
        self.events = ['typhoon', 'festival', 'drought', 'community feast', 'research breakthrough']

    def run_game(self):
        self.setup_farm()
        while self.year <= self.max_years:
            self.simulate_year()
        self.evaluate_performance()

    def setup_farm(self):
        print("🌾 Welcome to your vibrant farm in the Philippine countryside! 🌾")
        print("Manage your farm, interact with the community, face competitors, and work with researchers to thrive.")
        self.introduce_researchers()

    def introduce_researchers(self):
        self.researchers = random.randint(1, 3)
        print(f"\n🔬 You have {self.researchers} researchers working on improving your crop yields and animal health.")

    def simulate_year(self):
        print(f"\n🌞 Year {self.year} Start 🌞")
        for _ in range(4):  # Simulate each quarter as a season
            self.run_season()
        self.year += 1

    def run_season(self):
        self.perform_daily_tasks()
        self.handle_random_event()
        self.competitor_actions()
        self.energy_and_happiness_check()

    def perform_daily_tasks(self):
        morning_action = input("\n🌱 Morning: Choose your action (1: Tend to livestock, 2: Plant crops): ")
        if morning_action == '1':
            self.manage_livestock()
        else:
            self.plant_crops()

        afternoon_action = input("\n🌽 Afternoon: Market (1: Sell produce, 2: Buy supplies): ")
        if afternoon_action == '1':
            self.sell_produce()
        else:
            self.buy_supplies()

    def manage_livestock(self):
        print("Tending to livestock...")
        for animal, count in self.animals.items():
            productivity_gain = random.randint(1, 3) * count
            self.stats['Farm Productivity'] += productivity_gain

    def plant_crops(self):
        productivity_gain = random.randint(5, 15)
        self.stats['Farm Productivity'] += productivity_gain
        print("Planting crops increased productivity by", productivity_gain)

    def sell_produce(self):
        market_success = random.randint(5, 15)
        self.stats['Financial Stability'] += market_success
        print("Selling produce at the market increased financial stability by", market_success)

    def buy_supplies(self):
        market_expense = random.randint(3, 8)
        self.stats['Financial Stability'] -= market_expense
        print("Buying supplies decreased financial stability by", market_expense)

    def handle_random_event(self):
        event = random.choice(self.events)
        print(f"\n⚡ Random Event: {event} ⚡")
        if event == 'typhoon':
            damage = random.randint(10, 20)
            self.stats['Farm Productivity'] -= damage
            print(f"Typhoon caused {damage} damage to productivity.")
        elif event == 'research breakthrough':
            self.stats['Sustainability'] += 15
            print("Researchers made a breakthrough! Sustainability increased.")

    def competitor_actions(self):
        response = input("\n👥 Competitors are spreading rumors. Will you respond? (1: Yes, 2: No): ")
        if response == '1':
            self.stats['Community Reputation'] += 5
            print("You addressed the rumors positively, improving your reputation.")
        else:
            self.stats['Community Reputation'] -= 10
            print("Ignoring the rumors hurt your reputation.")

    def energy_and_happiness_check(self):
        self.stats['Energy'] -= random.randint(20, 30)
        if self.stats['Energy'] < 20:
            print("Energy too low! Consider resting tomorrow.")
        self.stats['Happiness'] -= random.randint(5, 10)
        if self.stats['Happiness'] < 20:
            print("Happiness is low. Consider family activities or community engagement.")

    def evaluate_performance(self):
        print("\n🏆 End of Game Evaluation 🏆")
        for stat, value in self.stats.items():
            print(f"{stat}: {value}")
        if self.stats['Farm Productivity'] > 200:
            print("🌟 You've become a Master Farmer with a thriving farm! 🌟")
        else:
            print("👏 Year ends with modest success. More to improve next year! 👏")

game = FarmManagementGame()
game.run_game()