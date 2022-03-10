import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def main():
  input_file = 'dataset/agaricus-lepiota-normalized.data'
  names = ['class','cap-shape','cap-surface','cap-color','bruises','odor','gill-attachment','gill-spacing','gill-size','gill-color','stalk-shape','stalk-root','stalk-surface-above-ring','stalk-surface-below-ring','stalk-color-above-ring','stalk-color-below-ring','veil-type','veil-color','ring-number','ring-type','spore-print-color','population','habitat']
  target = names[0]
  features = names[1:]

  df = pd.read_csv(input_file, names=names, na_values='?')

  x = df.loc[:, features].values

  #PCA projection
  pca = PCA()
  principalComponents = pca.fit_transform(x)
  print(pca.explained_variance_ratio_.tolist())
  # print(principalComponents[:, 0:2])

  principalDf = pd.DataFrame(data=principalComponents[:,0:2], 
                            columns=['principal component 1','principal component 2'])
  finalDf = pd.concat([principalDf, df[target]], axis=1)

  print(finalDf.info())
  print(finalDf.describe())
  print(finalDf.head(15))

  VisualizePcaProjection(finalDf, target)

def VisualizePcaProjection(finalDf, targetColumn):
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('2 component PCA', fontsize = 20)
    targets = [0, 1, ]
    colors = ['r', 'g']
    for target, color in zip(targets,colors):
        indicesToKeep = finalDf[targetColumn] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                   finalDf.loc[indicesToKeep, 'principal component 2'],
                   c = color, s = 50)
    ax.legend(targets)
    ax.grid()
    plt.show()

if __name__ == '__main__':
  main()