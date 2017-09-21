from sklearn.decomposition import PCA as sklearnPCA
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

df1 = pd.read_csv("~/Documents/coip_data/PCA_analysis/ctrl_denovo.csv", usecols = ["Unique", "Total", "Avg. Precursor Intensity", "AVG"])
df2 = pd.read_csv("~/Documents/coip_data/PCA_analysis/IP_denovo.csv", usecols = ["Unique", "Total", "Avg. Precursor Intensity", "AVG"])
#print df_temp
#normalize data
df1 = df1 / df1.ix[0]
df2 = df2 / df2.ix[0]
#print df1.shape
#print df2.shape
df1 = df1.T.values
df2 = df2.T.values

#concatenate two dataframe
df = np.concatenate((df1, df2), axis=1)
#print df
#print df.shape

#calculate PCA
sklearn_pca = sklearnPCA(n_components=2)
sklearn_transf = sklearn_pca.fit_transform(df.T)
ratio = sklearn_pca.explained_variance_ratio_


#plotting the results
plt.plot(sklearn_transf[0:399,0],sklearn_transf[0:399,1], 'o', markersize=7, color='blue', alpha=0.5, label='control')
plt.plot(sklearn_transf[400:1003,0], sklearn_transf[400:1003,1], '^', markersize=7, color='red', alpha=0.5, label='IP')

plt.xlabel(str(ratio[0]*100) + "%")
plt.ylabel(str(ratio[1]*100) + "%")
#plt.xlim([-4,4])
#plt.ylim([-4,4])
plt.legend()
plt.title('Both ctrl and  IP hits from micromere')

plt.show()
