#########################################################################
#        >    File Name: test.py
#        >       Author: jezeehu
#        >         Mail: jezeehu@tencent.com
#        > Created Time: 2023-07-07 16:54:34
#########################################################################
#!/usr/bin/python
# -*- coding:utf-8 -*-
import gym
env = gym.make('CartPole-v1')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()
