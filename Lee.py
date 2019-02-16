import Queue

def read_from_file(filename):
    """
    :param filename: Map location and dimensions
    :return: Integer dimensions and map matrix
    """

    readfile = open(filename, "r")
    line = readfile.readline()
    arr = line.split()

    aux = []
    result = []
    m = int(arr[0])
    n = int(arr[1])
    aux.append(m)
    aux.append(n)
    result.append(aux)

    for i in range(m):
        line = readfile.readline()
        arr = line.split()
        aux = []
        for j in range(n):
            aux.append(int(arr[j]))
        result.append(aux)

    readfile.close()
    return result


def write_to_file(filename, result):
    """
    :param filename: Write result to filename
    :param result: Minimum number of steps and the path
    :return:
    """

    _writefile_ = open(filename, "w")
    for arr in result:
        for elem in arr:
            _writefile_.write("%d " % elem)
        _writefile_.write("\n")

    _writefile_.close()


def _get_path_(mat, i, j, result, dl, dcl, m, n):
    """
    Get path
    :param mat:
    :param i:
    :param j:
    :param result:
    :param dl:
    :param dcl:
    :return:
    """
    if mat[i][j] == 1:
        result.append([i, j])
    else:
        aux = []
        for k in range(4):
            ln = i + dl[k]
            cn = j + dcl[k]
            if 0 <= ln and ln <= m-1 and 0 <= cn and cn <= n-1 and mat[ln][cn] == mat[i][j] - 1:
                _get_path_(mat, ln, cn, result, dl, dcl, m, n)
                result.append([i, j])
                break


def _lee_(data):
    """
    :param data: Map details
    :return: Minimum number of steps and the path
    """
    m = data[0][0]
    n = data[0][1]
    mat = []
    for i in range(m):
        aux = []
        for j in range(n):
            aux.append(0)
        mat.append(aux)

    dl = [-1, 0, 1, 0]
    dcl = [0, 1, 0, -1]

    mat[0][0] = 1
    cx = 0
    cy = 0
    q = Queue.Queue()
    q.put([cx, cy, 1])
    while not q.empty():
        aux = q.get()
        cx = aux[0]
        cy = aux[1]
        dc = aux[2]
        for k in range(4):
            nx = cx + dl[k]
            ny = cy + dcl[k]
            if 0 <= nx and nx <= m-1 and 0 <= ny and ny <= n-1 and data[nx+1][ny] == 0 and mat[nx][ny] == 0:
                q.put([nx, ny, dc+1])
                mat[nx][ny] = dc+1

    aux = []
    aux.append(mat[m-1][n-1]-1)
    result = []
    result.append(aux)
    _get_path_(mat, m-1, n-1, result, dl, dcl, m, n)
    return result


def main():
    """
    Main function
    :return:
    """
    matrix = read_from_file("lee.in")
    result = _lee_(matrix)
    write_to_file("lee.out", result)


if __name__ == "__main__":
    main()