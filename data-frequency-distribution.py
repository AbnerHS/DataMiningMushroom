import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
  input_file = 'dataset/agaricus-lepiota-clear.data'
  names = ['class','cap-shape','cap-surface','cap-color','bruises','odor','gill-attachment','gill-spacing','gill-size','gill-color','stalk-shape','stalk-root','stalk-surface-above-ring','stalk-surface-below-ring','stalk-color-above-ring','stalk-color-below-ring','veil-type','veil-color','ring-number','ring-type','spore-print-color','population','habitat']
  df = pd.read_csv(input_file, names=names, na_values='?')
  df = df.apply(lambda x: pd.factorize(x, sort=True)[0])
  
  # Distribuição de frequência de cap-shape
  cap_shape = df['cap-shape']
  labels = ['bell','conical','flat','sunken','knobbed','convex']
  sizes, x = np.histogram(cap_shape, bins=np.arange(7))
  plt.pie(sizes, labels=labels)
  plt.show()

  # Distribuição de frequência de odor
  odor = df['odor']
  labels =  ['almond','creosote','foul','anise','musty','none','pungent','spicy','fishy']
  sizes, x = np.histogram(odor, bins=np.arange(10))
  plt.bar(np.arange(9), height=sizes, tick_label=labels)
  plt.show()

if __name__ == "__main__":
  main()