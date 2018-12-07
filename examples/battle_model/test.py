from  senario_battle import generate_map
import magent
import numpy as np
env = magent.GridWorld('battle', map_size=40)
env.reset()
handles=env.get_handles()
generate_map(env, 40, handles)
state= list(env.get_observation(handles[0]))
handle=handles[0]
nei_len=10
poss=env.get_pos(handle)
nei_space=nei_len**2
act_prob=[]
for i in range(poss.shape[0]):
    sum_cnt=0
    act_p=np.zeros(env.get_action_space(handle)[0])
    for j in range(poss.shape[0]):
        if i != j:
            if np.sum(np.square(poss[i]-poss[j]))<nei_space:
                # act_p+=acts_onehot[j]
                sum_cnt+=1
    print(sum_cnt)
# n_action = [env.get_action_space(handles[0])[0], env.get_action_space(handles[1])[0]]
# print(n_action)
# print(state.len())


# import matplotlib.pyplot as plt
# plt.imshow(state) #Needs to be in row,col order