# ASI_Grupa3
## Dataset bank

1. Install conda fromhttps://docs.conda.io/projects/miniconda/en/latest/

2. Open cmd and go to the catalog with this project inside.
conda env create -f environment.yml

3. run python launcher.py script from command line

4. Streamlit app will be open in browser and you will be able to manage software from this web panel.

// Dopisać URL !!!!


Technologies:
- Python : all informations are in environment.yml file for conda. Below are also some of the most important python packages.
	- fastapi - exchanging informations with server
	- kedro - way of managing machine learning model. https://kedro.org/
	- kedro-viz -
	- sdv - for synthetic data
	- streamlit for web panel to change learning parameters and to test results.
	- pandas - managing dataframes

- Wandb : website for creating and managing machine learning models. We use it also as database.
 // gdzie znaleźć - url