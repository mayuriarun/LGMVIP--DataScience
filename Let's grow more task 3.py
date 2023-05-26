#!/usr/bin/env python
# coding: utf-8

# ![Capture2.JPG](attachment:Capture2.JPG)

# ### Task 3 : Music Recommendations
# - Objective : To create music recommender system that can suggest songs to listener based on their listening patterns.
# - Auther: Mayuri Arun Pathak Data Science Intern
# - Dataset : https://www.kaggle.com/c/kkbox-music-recommendation-challenge/data

# - Setting Working Directories

# In[3]:


import os
os.chdir("H:\\Data Science\\Internship\\Spark")


# - Import Required Libraries

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


# - Understanding the Dataset

# In[ ]:




