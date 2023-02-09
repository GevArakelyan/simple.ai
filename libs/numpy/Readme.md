### Numpy

* Docs: https://docs.scipy.org/doc/numpy/reference/routines.math.html
* Matrixes: https://docs.scipy.org/doc/numpy/reference/routines.Linalg.html

---
### [Introduction to Numerical Computing with NumPy | SciPy 2019 Tutorial | Alex Chabot-Leclerc](https://www.youtube.com/watch?v=ZB7BZMhfPgk)

https://github.com/enthought/Numpy-Tutorial-SciPyConf-2019
Alexandre Chabot-Leclerc





---















### Python Numpy Tutorial: 
https://cs231n.github.io/python-numpy-tutorial

CS231n Convolutional Neural Networks for Visual Recognition
CS231n Winter 2016: Lecture 2: Data-driven approach, kNN, Linear Classification 1
https://www.youtube.com/watch?v=8inugqHkfvE&list=PLkt2uSq6rBVctENoVBg1TpCC7OQi31AlC&index=3

```python
import numpy as np
distance = np.sum(np.abs(self.Xtr - X[i,:]), axis=1)
min_index = np.argmin(distances) # get the index with smallest distance
Ypred[i] = self.ytr[min_index] # predict the label of the nearest example
```