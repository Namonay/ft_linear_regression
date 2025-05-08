import pandas as pd
'''
Class Confidence:
    Calculate the confidence using the R-Square score
    https://en.wikipedia.org/wiki/Coefficient_of_determination
'''

class Confidence:
    def __init__(self, thetas_path="thetas.csv", data_path="datasets/data.csv"):
        self.theta_path = thetas_path
        self.data_path = data_path
        self.data = []
        self.theta0 = 0
        self.theta1 = 0
        self.get_thetas()
        self.get_data()
    def get_thetas(self):
        try:
            with open(self.theta_path, 'r') as file:
                data = pd.read_csv(file)
                self.theta0 = data["theta0"].iloc[0]
                self.theta1 = data["theta1"].iloc[0]
        except:
            print("! Warning, no trained model has been found")

    def get_data(self):
        try:
            with open(self.data_path, 'r') as file:
                self.data = pd.read_csv(file)
        except:
            print("! Warning, no data has been found")

    def estimate_price(self, mileage):
        return self.theta0 + (self.theta1 * mileage)

    def get_confidence(self):
        predicted_price = []
        for data in self.data["km"]:
            predicted_price.append(self.estimate_price(data))
        avg_price = sum(self.data["price"]) / len(self.data["price"])
        ss_tot = sum((y - avg_price) ** 2 for y in self.data["price"])
        ss_res = sum((y - y_hat) ** 2 for y, y_hat in zip(self.data["price"], predicted_price))
        r2 = 1 - (ss_res / ss_tot)
        return r2