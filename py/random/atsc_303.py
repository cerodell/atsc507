import context
import pandas as pd 


from context import data_dir






df = pd.read_csv(str(data_dir) + '/davis_sation_data.txt', sep = '\s+', skiprows = 3)



new = df[['Date', 'Time', 'TempOut', "OutHum", 'DewPt', 'Bar']].copy()

new.to_csv(str(data_dir) + '/davis_wxsation.csv')
