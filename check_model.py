import joblib

model = joblib.load(r"D:\Machine Learning Project (Data Science)\invoice_flagging\models\freight_model.pkl")

print("Number of features:", model.n_features_in_)