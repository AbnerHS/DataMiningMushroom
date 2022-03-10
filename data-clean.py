import pandas as pd
import numpy as np

def main():
  input_file = 'dataset/agaricus-lepiota.data'
  output_file = 'dataset/agaricus-lepiota-clear.data'
  names = ['class','cap-shape','cap-surface','cap-color','bruises','odor','gill-attachment','gill-spacing','gill-size','gill-color','stalk-shape','stalk-root','stalk-surface-above-ring','stalk-surface-below-ring','stalk-color-above-ring','stalk-color-below-ring','veil-type','veil-color','ring-number','ring-type','spore-print-color','population','habitat']
  df = pd.read_csv(input_file, names=names, na_values='?')
  df_original = df.copy()

  print("Primeiras 15 linhas")
  print(df.head(15))
  print("\n")

  print("Informações gerais")
  print(df.info())
  print("\n")

  print("Descrição")
  print(df.describe())
  print("\n")

  print("Dados Faltantes")
  print(df.isnull().sum())
  print("\n")

  columns_missing_values = df.columns[df.isnull().any()]
  print(columns_missing_values)

  for c in columns_missing_values:
    updateMissingValues(df, c)

  print(df.describe())
  print("\n")
  print(df.head(15))
  print(df_original.head(15))
  print("\n")
  df.to_csv(output_file, header=False, index=False)

def updateMissingValues(df, column, method="mode", number=0):
  if method == 'number':
    # Substituindo valores ausentes por um número
    df[column].fillna(number, inplace=True)
  elif method == 'median':
    # Substituindo valores ausentes pela mediana 
    median = df['Density'].median()
    df[column].fillna(median, inplace=True)
  elif method == 'mean':
    # Substituindo valores ausentes pela média
    mean = df[column].mean()
    df[column].fillna(mean, inplace=True)
  elif method == 'mode':
    # Substituindo valores ausentes pela moda
    mode = df[column].mode()[0]
    df[column].fillna(mode, inplace=True)

if __name__ == '__main__':
  main()

