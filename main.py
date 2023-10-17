
import  download_data
import data_preprocesing
import data_learning

data = download_data.get_data()
data = data_preprocesing.preprocess_data(data,['stalk-root'])

model = data_learning.train_model(data, 'poisonous')
