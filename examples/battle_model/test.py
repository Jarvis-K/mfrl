from  senario_battle import generate_map
import magent
env = magent.GridWorld('battle', map_size=40)
env.reset()
handles=env.get_handles()
generate_map(env, 40, handles)
state= list(env.get_observation(handles[0]))

# n_action = [env.get_action_space(handles[0])[0], env.get_action_space(handles[1])[0]]
# print(n_action)
print(state.len())


# import matplotlib.pyplot as plt
# plt.imshow(state) #Needs to be in row,col order