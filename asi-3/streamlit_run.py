from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project

import yaml
import streamlit as st
import os
import wandb
import bank_client

bootstrap_project(os.getcwd())
session = KedroSession.create()
st.title("Bank and Marketing")

st.header("Kedro parameters and running pipeline")
with st.expander("kedro"):
    st.header("Data_Science parameters")
    random_state = st.slider("Select random_state", min_value=1, max_value=10, value=3)
    kernel = st.select_slider("Select kernel", ["linear", "poly", "rbf", "sigmoid"], value="poly")
    rebalance = st.selectbox("Select rebalance:", ["undersampled", "oversampled"])
    model_type = st.selectbox("Select model_type:", ["logistic", "OTHER CHOICES"])
    n_estimators = st.slider("Select n_estimators", min_value=100, max_value=500, value=150)

    with open("./conf/base/parameters_data_science.yml", "w") as f:
        yaml.dump({"model_options": {"random_state": random_state, "features": "all", "kernel": kernel,
                                     "rebalance": rebalance, "model_type": model_type, "n_estimators": n_estimators}}, f)

    st.header("Train_Test_Split Parameters")
    test_size = st.slider("Choose test_size:", min_value=0.1, max_value=1.0, value=0.2)
    val_size = st.slider("Choose val_size:", min_value=0.1, max_value=1.0, value=0.2)
    random_state_split = st.slider("Select_random_state", min_value=1, max_value=10, value=3)
    rebalance_split = st.selectbox("Select_rebalance:", ["undersampled", "oversampled"])

    st.header("Wandblogin")
    input_text = st.text_area("Paste wandb API KEY:", value="", height=200)

    with open("./conf/base/parameters_train_test_split.yml", "w") as f:
        yaml.dump({"dataset_choice": {"rebalance": rebalance_split, "target_var_name": "y", "test_size": 0.2,
                                      "val_size": 0.2, "random_state": random_state_split}}, f)

    pipeline = st.select_slider("Select pipeline", ["__default__", "dp", "ds"], value="__default__")
    if st.button("Get Answer!"):
        answer = session.run(pipeline)
        session.load_context()

st.header("Results Filter")
with st.expander("Filter results by:"):
    clientFilter = bank_client
    clientFilter.age = st.slider("Choose age:", min_value=0, max_value=100, value=(0, 100))
    clientFilter.job = st.multiselect("Choose job:", ['management', 'technician', 'entrepreneur', 'blue-collar', 'retired', 'admin.',
                                              'services', 'self-employed', 'unemployed', 'housemaid', 'student'], default=['management', 'technician', 'entrepreneur', 'blue-collar', 'retired', 'admin.',
                                              'services', 'self-employed', 'unemployed', 'housemaid', 'student'])
    clientFilter.marital = st.multiselect("Choose marital:", ['married', 'single', 'divorced'], default=['married', 'single', 'divorced'])
    clientFilter.education = st.multiselect("Choose education:", ['tertiary', 'secondary', 'primary'],default=['tertiary', 'secondary', 'primary'])
    clientFilter.default = st.multiselect("Choose default:", ["yes", "no"], default=["yes", "no"])
    clientFilter.balance = st.slider("Choose balance:", min_value=-8019, max_value=102127, value=(-8019, 102127))
    clientFilter.housing = st.multiselect("Choose housing:", ["yes", "no"], default=["yes", "no"])
    clientFilter.loan = st.multiselect("Choose loan:", ["yes", "no"], default=["yes", "no"])
    clientFilter.day_of_week = st.slider("Choose day:", min_value=1, max_value=31, value=(1, 31))
    clientFilter.month = st.multiselect("Choose month:", ["January", "February", "March", "April", "May", "June", "July",
                                                     "August", "September", "October", "November", "December"], default=["January", "February", "March", "April", "May", "June", "July",
                                                     "August", "September", "October", "November", "December"])
    clientFilter.duration = st.slider("Choose duration:", min_value=0, max_value=4918, value=(0, 4918))
    clientFilter.campaign = st.slider("Choose campaign:", min_value=1, max_value=63, value=(1, 63))
    clientFilter.pdays = st.slider("Choose pdays:", min_value=-1, max_value=873, value=(1, 873))
    clientFilter.previous = st.slider("Choose previous:", min_value=0, max_value=275, value=(0, 275))

st.header("Specific result for single entry")
with st.expander("Test Specific Results"):
    clientTest = bank_client
    clientTest.age = st.slider("Choose age:", min_value=0, max_value=100)
    clientTest.job = st.selectbox("Choose job:",
                                  ['management', 'technician', 'entrepreneur', 'blue-collar', 'retired', 'admin.',
                                   'services', 'self-employed', 'unemployed', 'housemaid', 'student'])
    clientTest.marital = st.selectbox("Choose marital:", ['married', 'single', 'divorced'])
    clientTest.education = st.selectbox("Choose education:", ['tertiary', 'secondary', 'primary'])
    clientTest.default = st.selectbox("Choose default:", ["yes", "no"])
    clientTest.balance = st.slider("Choose balance:", min_value=-8019, max_value=102127)
    clientTest.housing = st.selectbox("Choose housing:", ["yes", "no"])
    clientTest.loan = st.selectbox("Choose loan:", ["yes", "no"])
    clientTest.day_of_week = st.slider("Choose day:", min_value=1, max_value=31)
    clientTest.month = st.select_slider("Choose month:",
                                        ["January", "February", "March", "April", "May", "June", "July",
                                         "August", "September", "October", "November", "December"]).lower()[:3]
    clientTest.duration = st.slider("Choose duration:", min_value=0, max_value=4918)
    clientTest.campaign = st.slider("Choose campaign:", min_value=1, max_value=63)
    clientTest.pdays = st.slider("Choose pdays:", min_value=-1, max_value=873)
    clientTest.previous = st.slider("Choose previous:", min_value=0, max_value=275)

#run = wandb.init(project="bank_dataset")




