from searchMethods import searching
from complexity import executionTime
import matplotlib.pyplot as mlt

if __name__ == '__main__':
    table = executionTime.take_execution_time(10000, 1000000, 50000, 5)
    xpoints = []
    ypoints = []
    for row in table:
        print(row)
        xpoints += [row[3]]
        ypoints += [row[0]]

    mlt.plot(xpoints, ypoints)
    mlt.show()

