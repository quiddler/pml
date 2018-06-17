from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import numpy as np 
import sys

sys.path.append('..')
from plotdecisionregions import plot_decision_regions
import matplotlib.pyplot as plt 
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

print(np.unique(y))  # [0, 1, 2] instead of ['Setosa', 'Versicolor', 'Virginica']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print(X_train)
print(X_test)
print(y_train)
print(y_test)

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

print('training data\n', X_train_std)
print('testing data\n', X_test_std)

ppn = Perceptron(n_iter=40, eta0=0.1, random_state=0)
ppn.fit(X_train_std, y_train)

y_pred = ppn.predict(X_test_std)
print('Misclassified samples: %d' % (y_test != y_pred).sum())

print('Accuracy -> %.2f' % accuracy_score(y_test, y_pred))

X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

plot_decision_regions(X=X_combined_std, y=y_combined, classifier=ppn, test_idx=range(105, 150))
plt.xlabel('petal length standardized')
plt.ylabel('petal width standardized')
plt.legend(loc='upper left')
plt.show()


