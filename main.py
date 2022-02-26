from search import *
class WolfGoatCabbage(Problem):
    # 0 denotes that the object is on the west bank
    # 1 denotes that the object is on the east bank
    # Farmer must always move per action
    def __init__(self, initial=({"F", "G", "W", "C"}, {"", "", "", ""}), goal=({"", "", "", ""}, {"F", "G", "W", "C"})):
        super().__init__(initial, goal)

    def actions(self, state):
        possible_actions = [{"F", "G"},
                            {"F", "W"},
                            {"F", "C"},
                            {"F"}
        ]
        
        return possible_actions

    def result(self, state, action):
        current_state = state
        legal_states = (
                            # All Legal States
                            ({"F", "W", "G", "C"}, {"", "", "", ""})    ,
                            (["", "W", "","C"]   , {"F", "", "G", ""})  ,
                            ({"F", "W", "", "C"} , {"", "", "G", ""})   ,
                            ({"", "", "", "C"}   , {"F", "W", "G", ""}) ,
                            ({"", "", "", ""}    , {"F", "W", "G", "C"}),
        )

        illegal_states = (
                            # All Illegal States
                            ({"", "W", "G", ""}  , {"F", "", "", "C"})  ,
                            ({"", "", "G", "C"}  , {"F", "W", "", ""})  ,
                            ({"", "W", "G", "C"} , {"F", "", "", ""})   ,
        )

        if (current_state in illegal_states):
            return False

        legal_states.remove(current_state)
        new_state = current_state.actions(state)

        return tuple(new_state)

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    #solution = depth_first_graph_search(wgc).solution()
    #print(solution)
    #solution = breadth_first_graph_search(wgc).solution()
    #print(solution)