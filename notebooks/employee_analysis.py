#!/usr/bin/env python
# coding: utf-8

# # Employee Data Analysis
# 
# ## 1. Introduction
# This project analyses employee data using Python, Pandas and NumPy.
# 
# ## 2. Data Loading
# Load employee information from a CSV file.
# 
# ## 3. Data Analysis
# Analyse employee counts and average salaries by department.
# 
# ## 4. Performance Testing
# Measure execution time using %timeit.
# 
# ## 5. Findings
# Summarise the important observations from the dataset.

# In[ ]:


import pandas as pd
import numpy as np

# Load employee dataset
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
df = pd.read_csv(BASE_DIR / "data" / "employees.csv")

# Display first five records
df.head()

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)
print(df.head())
# In[ ]:




