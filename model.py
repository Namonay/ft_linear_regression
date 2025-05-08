import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

from confidence import Confidence

data_path="datasets/data.csv"

class Model:
    def __init__(self, data_name=data_path, learning_rate=0.01, epochs=2000):
        with open(data_name, 'r') as file:
            self.data = pd.read_csv(file)
            self.km = [self.data["km"][i] for i in range(len(self.data))]
            self.price = [self.data["price"][i] for i in range(len(self.data))]
            self.learning_rate = learning_rate
            self.epochs = epochs
            self.theta0 = 0
            self.theta1 = 0
            self.km_min = 0
            self.km_max = 0
            self.cost_history = []
            self.m = len(self.data)
            self.normalize_values()

    def __estimate_price(self, mileage):
        return self.theta0 + (self.theta1 * mileage)

    def estimate_price(self, mileage):
        return self.__estimate_price((mileage - self.km_min) / (self.km_max - self.km_min))

    def normalize_values(self):
        self.km_min = np.min(self.km)
        self.km_max = np.max(self.km)
        for i in range(len(self.km)):
            self.km[i] = (self.km[i] - self.km_min) / (self.km_max - self.km_min)
    
    def calculate_thetas(self):
        tmp_t0 = 0
        tmp_t1 = 0
        cost = 0
        for i in range(self.m):
            pred = self.__estimate_price(self.km[i])
            tmp_t0 += pred - self.price[i]
            tmp_t1 += (pred - self.price[i]) * self.km[i]
            cost += (pred - self.price[i]) ** 2
        self.cost_history.append(cost / (2 * self.m))
        return (tmp_t0, tmp_t1)

    def train(self):
        for epoch in range(self.epochs):
            tmp_t0, tmp_t1 = self.calculate_thetas()
            self.theta0 -= self.learning_rate * tmp_t0
            self.theta1 -= self.learning_rate * tmp_t1

    def export(self):
        theta1_raw = self.theta1 / (self.km_max - self.km_min)
        theta0_raw = self.theta0 - self.theta1 * self.km_min / (self.km_max - self.km_min)
        data = [
            ["theta0", "theta1"],
            [theta0_raw, theta1_raw]
        ]
        with open("thetas.csv", mode="w", newline="") as file:
            writer = csv.writer(file)

            writer.writerows(data)
    def visualize(self):
        confidence = Confidence(data_path=data_path)

        km_range = np.linspace(min(self.data["km"]), max(self.data["km"]), 100)
        predicted_prices = self.theta0 + (self.theta1 * (km_range - self.km_min) / (self.km_max - self.km_min))
        fig, (regression, cost) = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

        regression.scatter(self.data["km"], self.data["price"], color='blue', label='Données')
        regression.plot(km_range, predicted_prices, color='red', label='Regression line')

        regression.set_xlabel("Kilometers (km)")
        regression.set_ylabel("Price (Euros)")
        regression.set_title("Linear Regression")
        regression.legend()
        regression.grid(True)
        regression.text(0.05, 0.95, f"Confidence: {confidence.get_confidence()}", transform=regression.transAxes, fontsize=8, verticalalignment='top', horizontalalignment='left', color="black")
        cost.plot(range(1, len(self.cost_history) + 1), self.cost_history, color='green')
        cost.set_title("Cost vs Epochs")
        cost.set_xlabel("Epochs")
        cost.set_ylabel("Cost")
        cost.grid(True)
        plt.show()

first_model = Model()
first_model.train()
first_model.export()
first_model.visualize()
