import numpy as np

from DecisionHelper import DecisionHelper

if __name__ == '__main__':
    m = np.array([[8, 7, 6, 7, 8, 9],
                  [9, 8, 7, 8, 9, 8],
                  [7, 6, 8, 6, 7, 7]])
    wei = [0.1, 0.3, 0.1, 0.2, 0.2, 0.1]
    map_of_the_table = ['GCC', 'Clang', 'MSVC']
    dh = DecisionHelper(m, wei)
    print(dh.saw())
    print(dh.topsis())
    print(dh.electre())
