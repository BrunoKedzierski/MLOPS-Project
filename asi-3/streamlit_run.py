from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project

import yaml
import streamlit as st
import os

bootstrap_project(os.getcwd())
session = KedroSession.create()
st.title("Bank and Marketing")

st.header("Data_Science parameters")
random_state = st.slider("Select random_state", min_value=1, max_value=10, value=3)
kernel = st.select_slider("Select kernel", ["poly", "microkernel", "exokernel", "hybrid", "nano"], value="poly")
rebalance = st.selectbox("Select rebalance:", ["undersampled", "oversampled"])
model_type = st.selectbox("Select model_type:", ["logistic", "OTHER CHOICES"])
n_estimators = st.slider("Select n_estimators", min_value=50, max_value=500, value=150)

with open("./conf/base/parameters_data_science.yml", "w") as f:
    yaml.dump({"model_options": {"random_state": random_state, "features": "all", "kernel": kernel, "rebalance": rebalance, "model_type": model_type, "n_estimators": n_estimators}}, f)

st.header("Train_Test_Split Parameters")
test_size = st.slider("Choose test_size:", min_value=0.1, max_value=1.0, value=0.2)
val_size = st.slider("Choose val_size:", min_value=0.1, max_value=1.0, value=0.2)
random_state_split = st.slider("Select_random_state", min_value=1, max_value=10, value=3)
rebalance_split = st.selectbox("Select_rebalance:", ["undersampled", "oversampled"])


with open("./conf/base/parameters_train_test_split.yml", "w") as f:
    yaml.dump({"dataset_choice": {"rebalance": rebalance_split, "target_var_name": "y", "test_size": 0.2, "val_size": 0.2, "random_state": random_state_split}}, f)

pipeline = st.select_slider("Select pipeline", ["__default__", "dp", "ds"], value="__default__")
if st.button("Get Answer!"):
    answer = session.run(pipeline)
