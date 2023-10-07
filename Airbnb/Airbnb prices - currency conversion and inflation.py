#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_cell_magic('capture', '', '!pip install numpy pandas streamlit gdown currencyconverter\nimport numpy as np\n\n# For readability purposes, we will disable scientific notation for numbers\nnp.set_printoptions(suppress=True)\nimport os\nimport shutil\n\nimport gdown # gdown helps us download dataset from google drive\nfrom numpy import genfromtxt')


# In[3]:


# Downloading file from Google Drive
# This file is based on data from: http://insideairbnb.com/get-the-data/
file_id_1 = "13fyESiH1ZEnMV6eabAyhe20t4W6peEWK"
downloaded_file_1 = "WK1_Airbnb_Amsterdam_listings_proj.csv"

# Downloading the file from Google Drive
gdown.download(id=file_id_1, output=downloaded_file_1)


# In[4]:


from numpy import genfromtxt

my_data = genfromtxt(downloaded_file_1, delimiter="|", dtype = "unicode")
my_data


# In[5]:


# Remove the first column and row
matrix = my_data[1: , 1:]

# Print out the first four columns
matrix [:, :4]


# In[6]:


# Transposing the dataset
matrix_T = matrix [:, :4].T
matrix_T


# In[7]:


# Remove the dollar sign
matrix_T = np.char.replace(matrix_T, "$", "")


# In[8]:


# Remove the comma
matrix_T = np.char.replace(matrix_T, ",", "")


# In[9]:


# We check if the records contaning dollars and comma signs are replaced
matrix_T[(np.char.find(matrix_T, "$") > -1) | (np.char.find(matrix_T, ",") > -1)] 

# the is nothing in output, whihc means that symbols were removed


# In[10]:


# To enable numerical operations we must convert the string/unicode to float32
matrix_T = matrix_T.astype(np.float32)

# Printing out the first fours rows 
matrix_T[:5, :]


# In[11]:


from currency_converter import CurrencyConverter

cc = CurrencyConverter()

# column = price_usd
matrix_T[:, 1]


# In[34]:


# We can check the number of currencies available 
cc.currencies


# In[37]:


# Let's convert the rate from the US dollar to British Pound
gbp_rate = cc.convert(1, "USD","GBP")

# Multiply the dollar column by your currency of choice
matrix_T[:, 1] = matrix_T[:, 1]*gbp_rate
matrix_T[:, 1]


# #### Airbnb's  inflation prices (we can use 7% as our inflation rate)

# In[12]:


# Multiply the British Pound column by the inflation percentage (1.00 + inflation)
matrix_T[:,1] = matrix_T[:,1] * 1.07
matrix_T[:, 1]


# In[13]:


# Rounding off the prices down to the nearest two decimals
matrix_T[:, 1] = np.around(matrix_T[:, 1], 2)
matrix_T[:, 1]

