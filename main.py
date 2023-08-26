from Board import Board
from Find import Find

if __name__ == '__main__':
    m, n = map(int, input().split(' '))
    b = []
    for i in range(m):
        b.append(input().split(' '))
    bb = Board(m, n, b)
    F = Find(bb)
    #F.bfs_search()
    #F.ids_search()
    #F.bds_search()
    F.a_star_search()
    #F.ida_star_search()

