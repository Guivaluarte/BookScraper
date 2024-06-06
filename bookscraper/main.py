import pandas as pd


def create_dataframe():
  df = pd.read_json('data.json').set_index('name')
  df['price'] = df['price'].astype(float)



if __name__ == '__main__':
  data = create_dataframe()