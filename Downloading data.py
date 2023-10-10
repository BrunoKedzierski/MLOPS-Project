import subprocess
import pandas as pd

#subprocess.run(["pip","install", "--upgrade","ucimlrepo"])



from ucimlrepo import fetch_ucirepo


mushroom = fetch_ucirepo(id=73)
data = mushroom.data.original

print(type(data))
data.to_csv("mushroom.csv")