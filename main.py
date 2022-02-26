from search import *
class WolfGoatCabbage(Problem):
    # 0 denotes that the object is on the west bank
    # 1 denotes that the object is on the east bank
    # Farmer must always move per action
    def __init__(self, initial=({"F": 0, "G": 0, "W": 0, "C": 0}), goal=({"F": 1, "G": 1, "W": 1, "C":1})):
        super().__init__(initial, goal)

    def actions(self, state):
        possible_actions = [{"F", "G"},
                            {"F", "W"},
                            {"F", "C"},
                            {"F"}
        ]
        
        if (state == ({"F": 0, "W": 0, "G": 0, "C": 0})):
            possible_actions.remove({"F", "W"},
                                    {"F", "C"})
            possible_actions.append({"F": 1}, {"G": 1})
        elif (state == ({"F": 1, "W": 0, "G": 1,"C": 0})):
            possible_actions.remove({"F", "W"},
                                    {"F", "C"})

        elif (state == ({"F": 0, "W": 0, "G": 1, "C": 0})):
            possible_actions.remove({"F", "G"})

        elif (state == ({"F": 1, "W": 1, "G": 1, "C": 0})):
            possible_actions.remove({"F", "C"},
                                    {"F"})

        else:
            return

        return possible_actions

    def result(self, state, action):
        new_state = list(state)
        legal_states = (
                            # All Legal States, Goal State is omitted.
                            ({"F": 0, "W": 0, "G": 0, "C": 0}),
                            ({"F": 1, "W": 0, "G": 1, "C": 0}),
                            ({"F": 0, "W": 0, "G": 1, "C": 0}),
                            ({"F": 1, "W": 1, "G": 1, "C": 0})
        )

        illegal_states = (
                            # All Illegal States
                            ({"F": 1, "W": 0, "G": 0, "C": 1}),
                            ({"F": 1, "W": 1, "G": 0, "C": 0}),
                            ({"F": 1, "W": 0, "G": 0, "C": 0})
        )

        if (state in illegal_states):
            return

        legal_states.remove(state)
        new_state = frozenset(state.actions(state))
        return new_state

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    #solution = breadth_first_graph_search(wgc).solution()
    #print(solution)