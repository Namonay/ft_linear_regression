# ft_linear_regression

A simple linear regression project in Python for educational purposes. The goal is to predict the price of a car based on its mileage using linear regression, and to visualize the results and the model's confidence.

## Features

- Reads car mileage and price data from CSV datasets.
- Learns optimal parameters (`theta0`, `theta1`) using gradient descent.
- Normalizes input data for effective training.
- Exports learned parameters to a CSV file.
- Predicts car prices for any given mileage.
- Calculates R² (coefficient of determination) to indicate model confidence.
- Visualizes the regression line, cost function evolution, and confidence score.

## Project Structure

```
ft_linear_regression/
│
├── datasets/
│   ├── data.csv                # Default dataset
│   ├── big_data.csv
│   ├── negative_data.csv
│   ├── nonlinear_data.csv
│   ├── perfectpositive_data.csv
│   ├── small_data.csv
│   └── variance_data.csv
│
├── model.py                    # Main file: trains, saves, and visualizes the model
├── estimate.py                 # Script to estimate a price given a mileage
├── confidence.py               # Calculates R² confidence score
└── thetas.csv                  # Saved learned parameters after running model.py
```

## Usage

### 1. Train the Model

Simply run:

```bash
python model.py
```

- Trains the linear regression model on `datasets/data.csv`.
- Saves the learned parameters (`thetas.csv`).
- Displays a plot with the data, regression line, confidence score (R²), and cost vs epochs.

### 2. Estimate Car Price

After training, estimate a car price by mileage:

```bash
python estimate.py
```

- Enter the mileage when prompted.
- Outputs the predicted price.

### 3. Confidence Score

The R² (confidence) score is printed on the regression plot, indicating how well the model fits the data.

## Custom Datasets

You can swap out the dataset by changing the `data_path` variable in `model.py` or by providing your own CSV file in the `datasets/` folder. The CSV must have columns: `km,price`.

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib

Install dependencies with:

```bash
pip install pandas numpy matplotlib
```

## Notes

- The model uses simple linear regression (1 feature: km).
- Data is normalized for stable and faster learning.
