import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():
  input_file = 'dataset/agaricus-lepiota-clear.data'
  output_file = 'dataset/agaricus-lepiota-normalized.data'
  names = ['class','cap-shape','cap-surface','cap-color','bruises','odor','gill-attachment','gill-spacing','gill-size','gill-color','stalk-shape','stalk-root','stalk-surface-above-ring','stalk-surface-below-ring','stalk-color-above-ring','stalk-color-below-ring','veil-type','veil-color','ring-number','ring-type','spore-print-color','population','habitat']
  target = names[0]
  features = names[1:]
  
  df = pd.read_csv(input_file, names=names, na_values='?')

  #Discretização -> simbolos numéricos para números
  df = df.apply(lambda x: pd.factorize(x, sort=True)[0])
  
  #Normalização Min-Max
  x = df.loc[:, features].values
  x_minmax = MinMaxScaler().fit_transform(x)
  normalizedDf = pd.DataFrame(data=x_minmax, columns=features)
  normalizedDf = pd.concat([normalizedDf, df[[target]]], axis=1)
  print(normalizedDf.info())
  print(normalizedDf.describe())
  print(normalizedDf.head(15))

  normalizedDf.to_csv(output_file, header=False, index=False)

if __name__ == "__main__":
  main()