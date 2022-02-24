import pandas as pd
import numpy as np

def main():
  input_file = 'dataset/agaricus-lepiota.data'
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

if __name__ == '__main__':
  main()

