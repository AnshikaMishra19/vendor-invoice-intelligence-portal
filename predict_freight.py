import pandas as pd

def predict_freight_cost(input_data):
    df = pd.DataFrame(input_data)

    # Simple logic (5% of invoice dollars)
    prediction = df["Dollars"] * 0.05  

    return pd.DataFrame({
        "Predicted_Freight": prediction
    })