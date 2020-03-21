import context
import pandas as pd 


from context import data_dir






df = pd.read_csv(str(data_dir) + '/kestrel_2020.csv')



# new = df[['Date', 'Time', 'TempOut', "OutHum", 'DewPt', 'Bar']].copy()



# new = df[['Time', 'Temp', "WindSpeed"]].copy()
# new2 = new{}


# new.to_csv(str(data_dir) + '/kestral.csv')




