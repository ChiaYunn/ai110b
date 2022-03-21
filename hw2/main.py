import pandas as pd
import numpy as np

initial_state = [0, 0, 0, 0]
final_state = pd.Series([1, 1, 1, 1])

final_state.index = ['wolf', 'sheep', 'veg', 'human']
state = pd.DataFrame(columns=["wolf", "sheep", "veg", "human"])
state = state.append({'wolf': 0, 'sheep': 0, 'veg': 0,
                      'human': 0}, ignore_index=True)
state_col = state.columns


def human(state, num):
    current = state.loc[len(state)-1][state_col]

    if (current == final_state).all():
        return state

    elif (current['human'] == 1 and current['wolf'] == 1 and current['veg'] == 1 and current['sheep'] == 0):
        current['human'] = 0
        state = state.append(current, ignore_index=True)
        current['human'] = 1
        current['sheep'] = 1
        state = state.append(current, ignore_index=True)
        state = human(state, 0)
        return state

    else:
        row = current[current == current['human']]

        for id in range(num, len(row)-1):
            current = state.loc[len(state)-1][state_col]
            current['human'] = 1-current['human']
            current[row.index[id]] = 1-current[row.index[id]]

            if not(((current['wolf'] == current['sheep']) and (current['sheep'] != current['human'])) or
                   ((current['sheep'] == current['veg']) and (current['sheep'] != current['human']))):
                state = state.append(current, ignore_index=True)
                if len(state) == len(state.drop_duplicates()):
                    state = human(state, 0)
                    return state
                else:
                    state = state.drop_duplicates()
                    if (id != len(row)-1-1):
                        state = human(state, id+1)
                        return state
                    else:
                        current = state.loc[len(state)-1][state_col]
                        current['human'] = 1-current['human']
                        state = state.append(current, ignore_index=True)
                        state = human(state, 0)
                        return state


output = human(state, 0)
print(output)
