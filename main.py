from search import *
class WolfGoatCabbage(Problem):
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal
    pass

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)