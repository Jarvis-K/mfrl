from  senario_battle import generate_map
import magent
env = magent.GridWorld('battle', map_size=40)
env.reset()
handles=env.get_handles()
generate_map(env, 40, handles)
state= env.get_observation(handles[0])
print(env.get_feature_space(handles[0]))
print(len(state))

# import matplotlib.pyplot as plt
# plt.imshow(state) #Needs to be in row,col order