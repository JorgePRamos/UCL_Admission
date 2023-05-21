
import numpy
def adMatrixToAdList(adj_mat):
    adList = []
    matrix = numpy.array(adj_mat)
    for row in matrix:
        rowList = []
        for  pos in range(len(row)):
            if not row[pos] == 0:
                rowList.append(pos)
        adList.append(rowList)
    return adList



if __name__ == "__main__":
    adj_mat =   [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]
    print(adMatrixToAdList(adj_mat))