import subprocess
import pandas as pd
from ucimlrepo import fetch_ucirepo

mushroom = fetch_ucirepo(id=73)
data = mushroom.data.original
data.to_csv("mushroom.csv")