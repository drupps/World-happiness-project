import pandas as pd
from sqlalchemy import create_engine

wh20 = pd.read_csv("../data/tidy_data/WHR20_columns_fixed.csv")
engine = create_engine("sqlite:///wh20.sqlite")
wh20.to_sql(name='wh20', con=engine, if_exists='replace', index=False)