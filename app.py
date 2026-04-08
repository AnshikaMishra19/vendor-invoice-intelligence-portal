import streamlit as st
from inference.predict_freight import predict_freight_cost
from inference.predict_invoice_flag import predict_invoice_flag

#==========================================================
# Page Configuration
#==========================================================
st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    layout="wide"
)

#==========================
# Header Section
#==========================
st.markdown("""
# Vendor Invoice Intelligence Portal
### AI-Driven Freight Cost Prediction & Invoice Risk Flagging
""")

st.divider()

#=============
# Sidebar
#=============
st.sidebar.title("Model Selection")

selected_model = st.sidebar.radio(
    "Choose Prediction Model",
    [
        "Freight Cost Prediction",
        "Invoice Manual Approval Flag"
    ]
)

#=======================
# Freight Cost Prediction 
#=======================
if selected_model == "Freight Cost Prediction":

    st.subheader("Freight Cost Prediction")

    with st.form("freight_form"):
        quantity = st.number_input("Quantity", min_value=1, value=1200)
        dollars = st.number_input("Invoice Dollars", min_value=1.0, value=18500.0)

        submit_freight = st.form_submit_button("Predict Freight Cost")

    if submit_freight:

        # ✅ MATCH WITH TRAINING FEATURES (IMPORTANT)
        input_data = {
            "Quantity": [quantity],
            "Dollars": [dollars]
        }

        result = predict_freight_cost(input_data)

        st.write(result)  # debug (optional)

        prediction = result["Predicted_Freight"]

        st.success("Prediction completed successfully")

        st.metric(
            "Estimated Freight Cost",
            f"${prediction[0]:,.2f}"
        )

#=================================
# Invoice Flag Prediction
#=================================
else:

    st.subheader("Invoice Manual Approval Prediction")

    with st.form("invoice_flag_form"):

        invoice_quantity = st.number_input("Invoice Quantity", min_value=1, value=50)
        freight = st.number_input("Freight Cost", min_value=0.0, value=1.73)
        invoice_dollars = st.number_input("Invoice Dollars", min_value=1.0, value=352.95)
        total_item_quantity = st.number_input("Total Item Quantity", min_value=1, value=162)
        total_item_dollars = st.number_input("Total Item Dollars", min_value=1.0, value=2476.0)

        submit_flag = st.form_submit_button("Evaluate Invoice Risk")

    if submit_flag:

        input_data = {
            "invoice_quantity": [invoice_quantity],
            "invoice_dollars": [invoice_dollars],
            "Freight": [freight],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars]
        }

        result = predict_invoice_flag(input_data)

        st.write(result)  # debug (optional)

        flag = result["Predicted_Flag"][0]

        if flag == 1:
            st.error("Invoice requires MANUAL APPROVAL")
        else:
            st.success("Invoice is SAFE for Auto-Approval")