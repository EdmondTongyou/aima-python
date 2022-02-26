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
        
        if (state == ({"F", "W", "G", "C"}, {"", "", "", ""})):
            possible_actions.remove({"F", "W"},
                                    {"F", "C"})

        elif (state == ({"", "W", "", "C"}, {"F", "", "G", ""}) or ({"F", "", "G", ""}, {"", "W", "", "C"})):
            possible_actions.remove({"F", "W"},
                                    {"F", "C"})

        elif (state == ({"F" , "W" , "", "C" }, {"", "", "G", ""}) or ({"" , "" , "G", "" }, {"F", "W", "", "C"})):
            possible_actions.remove({"F" , "G" })

        elif (state == ({"F", "W", "G", "" }, {"", "", "","C"}) or ({"" , "" , "", "C" }, {"F", "W", "G", ""})):
            possible_actions.remove({"F" , "C" },
                                    {"F"})

        elif (state == ({"F" , "" , "G", "C" }, {"", "W", "", ""}) or ({"" , "W" , "", "" }, {"F", "", "G", "C"})):
            possible_actions.remove({"F", "W"},
                                    {"F"})

        else:
            return

        return possible_actions

    def result(self, state, action):
        new_state = set(state)

        illegal_states = (
                            # All Illegal States
                            ({"", "", "G" , "C"}  , {"F", "W", "", ""}) ,
                            ({"F", "W", "" , ""}  , {"", "", "G", "C"}) ,
                            ({"", "W", "G" , "C"} , {"F", "", "", ""})  ,
                            ({"F", "", "" , ""}   , {"", "W", "G", "C"}),
                            ({"", "W", "G" , ""}  , {"F", "", "", "C"}) ,
                            ({"F", "", "" , "C"}  , {"", "W", "G", ""}) ,
        )

        if (state in illegal_states):
            return

        new_state = new_state.actions(state)
        return frozenset(new_state)

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)