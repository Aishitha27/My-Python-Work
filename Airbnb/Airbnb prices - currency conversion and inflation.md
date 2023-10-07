```python
%%capture
!pip install numpy pandas streamlit gdown currencyconverter
import numpy as np

# For readability purposes, we will disable scientific notation for numbers
np.set_printoptions(suppress=True)
import os
import shutil

import gdown # gdown helps us download dataset from google drive
from numpy import genfromtxt
```


```python
# Downloading file from Google Drive
# This file is based on data from: http://insideairbnb.com/get-the-data/
file_id_1 = "13fyESiH1ZEnMV6eabAyhe20t4W6peEWK"
downloaded_file_1 = "WK1_Airbnb_Amsterdam_listings_proj.csv"

# Downloading the file from Google Drive
gdown.download(id=file_id_1, output=downloaded_file_1)
```

    Downloading...
    From: https://drive.google.com/uc?id=13fyESiH1ZEnMV6eabAyhe20t4W6peEWK
    To: C:\Users\Cashapona\WK1_Airbnb_Amsterdam_listings_proj.csv
    100%|███████████████████████████████████████████████████████████████████████████████| 246k/246k [00:00<00:00, 1.41MB/s]
    




    'WK1_Airbnb_Amsterdam_listings_proj.csv'




```python
from numpy import genfromtxt

my_data = genfromtxt(downloaded_file_1, delimiter="|", dtype = "unicode")
my_data
```




    array([['', '0', '1', ..., '6170', '6171', '6172'],
           ['id', '23726706', '35815036', ..., '35760705', '36900951',
            '40575103'],
           ['price', '$88.00', '$105.00', ..., '$180.00', '$174.00',
            '$65.00'],
           ['latitude', '52.34916', '52.42419', ..., '52.42624', '52.31983',
            '52.33946'],
           ['longitude', '4.97879', '4.95689', ..., '4.90236', '4.86463',
            '4.95749']], dtype='<U18')




```python
# Remove the first column and row
matrix = my_data[1: , 1:]

# Print out the first four columns
matrix [:, :4]
```




    array([['23726706', '35815036', '31553121', '34745823'],
           ['$88.00', '$105.00', '$152.00', '$87.00'],
           ['52.34916', '52.42419', '52.43237', '52.2962'],
           ['4.97879', '4.95689', '4.91821', '5.01231']], dtype='<U18')




```python
# Transposing the dataset
matrix_T = matrix [:, :4].T
matrix_T
```




    array([['23726706', '$88.00', '52.34916', '4.97879'],
           ['35815036', '$105.00', '52.42419', '4.95689'],
           ['31553121', '$152.00', '52.43237', '4.91821'],
           ['34745823', '$87.00', '52.2962', '5.01231']], dtype='<U18')




```python
# Remove the dollar sign
matrix_T = np.char.replace(matrix_T, "$", "")
```


```python
# Remove the comma
matrix_T = np.char.replace(matrix_T, ",", "")
```


```python
# We check if the records contaning dollars and comma signs are replaced
matrix_T[(np.char.find(matrix_T, "$") > -1) | (np.char.find(matrix_T, ",") > -1)] 

# the is nothing in output, whihc means that symbols were removed
```




    array([], dtype='<U8')




```python
# To enable numerical operations we must convert the string/unicode to float32
matrix_T = matrix_T.astype(np.float32)

# Printing out the first fours rows 
matrix_T[:5, :]
```




    array([[23726706.     ,       88.     ,       52.34916,        4.97879],
           [35815036.     ,      105.     ,       52.42419,        4.95689],
           [31553120.     ,      152.     ,       52.43237,        4.91821],
           [34745824.     ,       87.     ,       52.2962 ,        5.01231]],
          dtype=float32)




```python
from currency_converter import CurrencyConverter

cc = CurrencyConverter()

# column = price_usd
matrix_T[:, 1]
```




    array([ 88., 105., 152.,  87.], dtype=float32)




```python
# We can check the number of currencies available 
cc.currencies
```




    {'AUD',
     'BGN',
     'BRL',
     'CAD',
     'CHF',
     'CNY',
     'CYP',
     'CZK',
     'DKK',
     'EEK',
     'EUR',
     'GBP',
     'HKD',
     'HRK',
     'HUF',
     'IDR',
     'ILS',
     'INR',
     'ISK',
     'JPY',
     'KRW',
     'LTL',
     'LVL',
     'MTL',
     'MXN',
     'MYR',
     'NOK',
     'NZD',
     'PHP',
     'PLN',
     'ROL',
     'RON',
     'RUB',
     'SEK',
     'SGD',
     'SIT',
     'SKK',
     'THB',
     'TRL',
     'TRY',
     'USD',
     'ZAR'}




```python
# Let's convert the rate from the US dollar to British Pound
gbp_rate = cc.convert(1, "USD","GBP")

# Multiply the dollar column by your currency of choice
matrix_T[:, 1] = matrix_T[:, 1]*gbp_rate
matrix_T[:, 1]
```




    array([55.91006, 66.71087, 96.57193, 55.27472], dtype=float32)



#### Airbnb's  inflation prices (we can use 7% as our inflation rate)


```python
# Multiply the British Pound column by the inflation percentage (1.00 + inflation)
matrix_T[:,1] = matrix_T[:,1] * 1.07
matrix_T[:, 1]
```




    array([ 94.16    , 112.350006, 162.64001 ,  93.090004], dtype=float32)




```python
# Rounding off the prices down to the nearest two decimals
matrix_T[:, 1] = np.around(matrix_T[:, 1], 2)
matrix_T[:, 1]
```




    array([ 94.16, 112.35, 162.64,  93.09], dtype=float32)


