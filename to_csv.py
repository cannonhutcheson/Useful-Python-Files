import pandas as pd
data = pd.io.stata.read_stata("C:/Users/19126/Desktop/ECON4750/HW_1/tonga_data.dta")
data.to_csv('tonga_data.csv')

