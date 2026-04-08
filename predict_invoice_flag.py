import joblib
import pandas as pd

MODEL_PATH = r"D:\Machine Learning Project (Data Science)\invoice_flagging\models\predict_flag_model.pkl"


def load_model():
    with open(MODEL_PATH, "rb") as f:
        return joblib.load(f)


def predict_invoice_flag(input_data):
    model = load_model()

    input_df = pd.DataFrame(input_data)

    prediction = model.predict(input_df)

    input_df["Predicted_Flag"] = prediction

    return input_df