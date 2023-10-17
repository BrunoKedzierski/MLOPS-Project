##TODO Make the pipeline here
import  download_data
import data_preprocesing
import data_learning

## TODO add steps
data = download_data.get_data()
data = data_preprocesing.drop_missing_data(['stalk-root'],data)
data = data_preprocesing.encode_data(data)
X_train, y_train, X_test, y_test, X_val, y_val = data_learning.train_test_val_split(data)
model = data_learning.train(X_train, y_train, X_test, y_test)
data_learning.save_model(model)