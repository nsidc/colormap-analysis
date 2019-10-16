import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from viscm import viscm

cm_data = [[0.07451, 0.47843, 0.89020],
           [0.96863, 0.98824, 1.00000]]
test_cm = LinearSegmentedColormap.from_list(__file__, cm_data)

if __name__ == "__main__":
    viscm(test_cm)
    plt.show()
