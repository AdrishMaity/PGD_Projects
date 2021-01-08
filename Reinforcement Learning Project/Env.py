# Import routines

import numpy as np
import math
import random

# Defining hyperparameters
m = 5 # number of cities, ranges from 1 ..... m
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger


class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        self.action_space = [(p,q) for p in range(m+1) for q in range(m+1) if ((p>0 and q>0 and p!=q) or (p==0 and q==0))]
        self.state_space = [(X,T,D) for X in range(1,m+1) for T in range(t) for D in range(d)]
        # self.state_init = random.choice(self.state_space)
        self.state_init = random.choice([(1,3,2), (2,5,1), (3,2,6), (4,4,2), (5,10,5)])

        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input

    def state_encod_arch1(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        state_encod = (m+t+d)*[0]
        # encode location
        state_encod[state[0]-1] = 1 # for nth location the encoded index is n-1
        # encode time
        state_encod[state[1]+m] = 1
        # encode day of the week
        state_encod[state[2]+m+t] = 1

        return state_encod


    # Use this function if you are using architecture-2 
    # def state_encod_arch2(self, state, action):
    #     """convert the (state-action) into a vector so that it can be fed to the NN. This method converts a given state-action pair into a vector format. Hint: The vector is of size m + t + d + m + m."""

        
    #     return state_encod


    ## Getting number of requests

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        
        # use poisson distribution for generating random # of requests based on average
        
        location = state[0]
        if location == 1:
            requests = np.random.poisson(2)
        elif location == 2:
            requests = np.random.poisson(12)
        elif location == 3:
            requests = np.random.poisson(4)
        elif location == 4:
            requests = np.random.poisson(7)
        elif location == 5:
            requests = np.random.poisson(8)

        if requests >15:
            requests =15

        possible_actions_index = random.sample(range(1, (m-1)*m +1), requests) # (0,0) is not considered as customer request
        actions = [self.action_space[i] for i in possible_actions_index]

        

        if (0, 0) not in actions:
            actions.append((0,0))
            possible_actions_index.append(self.action_space.index((0,0))) # find index of (0,0) action

        return possible_actions_index,actions  


    def calculate_new_time(self, time_of_day, day_of_week, time_taken):
        time_of_day = time_of_day + math.ceil(time_taken)
        if time_of_day > (t-1):
            time_of_day = time_of_day % t
            day_of_week += 1
            day_of_week = day_of_week % d
        return time_of_day, day_of_week
                                          

    def reward_func(self, state, action, Time_matrix):
        """
        Takes in state, action and Time-matrix and returns the reward
        
        reward = (revenue earned from pickup point p to drop point q) - 
                (Cost of battery used in moving from pickup point p to drop point q) - 
                (Cost of battery used in moving from current point i to pick-up point p)
        
        """
        
        # initialize variables
        reward = 0
        cab_pos = state[0] # current cab location
        pickup_pos = action[0] # customer pickup location
        drop_pos = action[1] # customer drop location
        time_of_day = state[1] # current time of the day
        day_of_week = state[2] # current day of the week
        
        # Calculate the new "time of day" and "day of the week" when cab reaches pickup position
        if cab_pos!=pickup_pos: 
            # using Time Matrix calculate total time to reach pick up location
            time_taken = Time_matrix[cab_pos-1][pickup_pos-1][time_of_day][day_of_week]
            
            # calculate new "time of day" and "day of the week"
            time_of_day,day_of_week = self.calculate_new_time(time_of_day,day_of_week,time_taken) 
        
        if (pickup_pos == 0) and (drop_pos==0):
            reward = -C # Per hour fuel and other costs for no-ride action
        else:
            # calculate total reward
            reward = R*Time_matrix[pickup_pos-1][drop_pos-1][time_of_day][day_of_week] - C*(Time_matrix[pickup_pos-1][drop_pos-1][time_of_day][day_of_week] + Time_matrix[cab_pos-1][pickup_pos-1][time_of_day][day_of_week])
        return reward




    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""

        # initialize variables
        cab_pos = state[0] # current cab location
        pickup_pos = action[0] # customer pickup location
        drop_pos = action[1] # customer drop location
        time_of_day = state[1] # current time of the day
        day_of_week = state[2] # current day of the week


        if (pickup_pos == 0) and (drop_pos==0):
            new_cab_pos = cab_pos
            total_time_spent = 1
        else:
            # Time to move from current point to pick-up point
            time_to_reach_pickup_pos = 0
            if cab_pos!=pickup_pos:
                time_to_reach_pickup_pos = Time_matrix[cab_pos-1][pickup_pos-1][time_of_day][day_of_week]
            time_to_complete_ride = Time_matrix[pickup_pos-1][drop_pos-1][time_of_day][day_of_week]

            total_time_spent = time_to_reach_pickup_pos + time_to_complete_ride

            # calculate total travel time
            new_cab_pos = drop_pos
        
        # calculate new "time of day" and "day of the week"
        new_time_of_day, new_day_of_week = self.calculate_new_time(time_of_day,day_of_week,total_time_spent)

        next_state = (new_cab_pos, new_time_of_day, new_day_of_week)

        return next_state


    def reset(self):
        # self.state_init = random.choice(self.state_space)
        self.state_init = random.choice([(1,3,2), (2,5,1), (3,2,6), (4,4,2), (5,10,5)])
        return self.action_space, self.state_space, self.state_init


