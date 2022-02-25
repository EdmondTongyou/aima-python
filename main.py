from search import *
class WolfGoatCabbage(Problem):
    # 0 denotes that the object is on the west bank
    # 1 denotes that the object is on the east bank
    def __init__(self, initial=(["F", "G", "W", "C"], [0, 0, 0, 0]), goal=(["F", "G", "W", "C"], [1, 1, 1, 1])):
        super().__init__(initial, goal)

    def actions(self, state):
        raise NotImplementedError

    def eaten(self, state1, state2):
        if (state1 == "G" and state2 == "W"):
            return True
        elif (state1 == "G" and state2 == "C"):
            return True
        else:
            return False

    def is_safe(self, state1, state2):
        if (self.eaten(state1, state2) or self.eaten(state1, state2)):
            return False
        else:
            return True

    def result(self, state, action):
        current_state = state
        state = current_state
        return(current_state)

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self, state):
        raise NotImplementedError

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    #solution = depth_first_graph_search(wgc).solution()
    #print(solution)
    #solution = breadth_first_graph_search(wgc).solution()
    #print(solution)