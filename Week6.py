import numpy as np
import itertools
import pandas as pd


states=['sleeping','eating','walking']
hidden=['healthy','sick']
pi=[0.5,0.5]

state=pd.Series(pi,index=hidden,name='states')
print("Initial probability:\n",state, "\n")


a_df=pd.DataFrame(columns=hidden,index=hidden)
a_df.loc['healthy']=[0.7,0.3]
a_df.loc['sick']=[0.4,0.6]
print("Transition probabilities:\n",a_df,"\n")


b_df=pd.DataFrame(columns=states,index=hidden)
b_df.loc['healthy']=[0.2,0.6,0.2]
b_df.loc['sick']=[0.4,0.8,0.6]
print("Emission probabilities:\n",b_df,"\n")

def forward(obs,a_df,b_df,pi,hidden):
    total=0
    all_state_paths=list(itertools.product(hidden,repeat=len(obs)))


    for path in all_state_paths:
        prob=pi[hidden.index(path[0])]*b_df.loc[path[0],obs[0]]

        for t in range(1,len(obs)):
            prev=path[t-1]
            curr=path[t]
            prob*=a_df.loc[prev,curr]*b_df.loc[curr,obs[t]]
            total+=prob
    return total

obsq=['sleeping','eating','walking']
print("Forward (total probability):",forward(obsq,a_df,b_df,pi,hidden))

"""
#output:

Initial probability:
 healthy    0.5
sick       0.5
Name: states, dtype: float64 

Transition probabilities:
         healthy sick
healthy     0.7  0.3
sick        0.4  0.6 

Emission probabilities:
         sleeping eating walking
healthy      0.2    0.6     0.2
sick         0.4    0.8     0.6 

Forward (total probability): 0.5016"""

            
