import pandas as pd

class Estimate:
    def __init__(self, thetas_path="thetas.csv"):
        self.path = thetas_path
        self.theta0 = 0
        self.theta1 = 0
        self.get_thetas()
    def get_thetas(self):
        try:
            with open(self.path, 'r') as file:
                self.data = pd.read_csv(file)
                self.theta0 = self.data["theta0"].iloc[0]
                self.theta1 = self.data["theta1"].iloc[0]
        except:
            print("! Warning, no data has been found")
    def estimate_price(self, mileage):
        return self.theta0 + (self.theta1 * mileage)

estimate = Estimate()
try:
    input =  int(input("Please enter the mileage of your car: "))
except:
    print("! Wrongs args format")
else:
    print("The estimated price for a", input, "kilometers car is :", estimate.estimate_price(input))
