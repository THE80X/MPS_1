import numpy as np

from DecisionHelper import DecisionHelper

if __name__ == '__main__':
    m = np.array([[3, 3, 3, 5, 3, 2],
                  [3, 3, 3, 4, 3, 2],
                  [3, 2, 3, 3, 3, 2]])
    wei = [0.1, 0.3, 0.1, 0.2, 0.2, 0.1]

    dh = DecisionHelper(m, wei)
    print(dh.saw())
    print(dh.topsis())
    print(dh.electre())
