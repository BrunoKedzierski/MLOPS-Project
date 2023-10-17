import subprocess
import pandas as pd
from ucimlrepo import fetch_ucirepo

def get_data():
    mushroom = fetch_ucirepo(id=73)
    data = mushroom.data.original
    return data