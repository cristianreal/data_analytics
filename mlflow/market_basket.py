import mlflow
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

class MarketBasketModel:
    def __init__(self, min_support=0.01, min_threshold=1):
        self.min_support = min_support
        self.min_threshold = min_threshold
        self.frequent_itemsets = None
        self.rules = None

    def fit(self, X):
        self.frequent_itemsets = apriori(X, min_support=self.min_support, use_colnames=True)
        self.rules = association_rules(self.frequent_itemsets, metric="lift", min_threshold=self.min_threshold)
        return self

    def predict(self, X):
        # This is a placeholder prediction function
        # In reality, you might use the rules to make recommendations
        return np.array(['placeholder' for _ in range(len(X))])

# Set the experiment name
mlflow.set_experiment("market_basket_analysis")

# Sample data (replace with your actual data loading)
data = {
    'Transaction': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
    'Item': ['Apple', 'Bread', 'Bread', 'Milk', 'Apple', 'Milk', 'Bread', 'Milk', 'Apple', 'Bread']
}
df = pd.DataFrame(data)
basket = pd.crosstab(df['Transaction'], df['Item'])

# Start an MLflow run
with mlflow.start_run():
    # Log parameters
    mlflow.log_param("min_support", 0.2)
    mlflow.log_param("min_threshold", 1)

    # Create and fit the model
    model = MarketBasketModel(min_support=0.001, min_threshold=1)
    model.fit(basket)

    # Log metrics
    mlflow.log_metric("num_rules", len(model.rules))
    mlflow.log_metric("max_lift", model.rules['lift'].max())

    # Log the rules as an artifact
    model.rules.to_csv("association_rules.csv", index=False)
    mlflow.log_artifact("association_rules.csv")

    # Create an input example
    input_example = basket.iloc[:5]

    # Log the model with input example
    mlflow.pyfunc.log_model(
        "market_basket_model",
        python_model=model,
        input_example=input_example,
        signature=mlflow.models.infer_signature(input_example, model.predict(input_example))
    )

print("Market Basket Analysis completed. Check MLflow UI for results.")