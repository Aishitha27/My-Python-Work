```python
import pandas as pd
data = pd.read_csv(r"C:\Users\Cashapona\Desktop\My Python work\Ecommerce Purchases\Ecommerce Purchases")
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Address</th>
      <th>Lot</th>
      <th>AM or PM</th>
      <th>Browser Info</th>
      <th>Company</th>
      <th>Credit Card</th>
      <th>CC Exp Date</th>
      <th>CC Security Code</th>
      <th>CC Provider</th>
      <th>Email</th>
      <th>Job</th>
      <th>IP Address</th>
      <th>Language</th>
      <th>Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16629 Pace Camp Apt. 448\nAlexisborough, NE 77...</td>
      <td>46 in</td>
      <td>PM</td>
      <td>Opera/9.56.(X11; Linux x86_64; sl-SI) Presto/2...</td>
      <td>Martinez-Herman</td>
      <td>6011929061123406</td>
      <td>02/20</td>
      <td>900</td>
      <td>JCB 16 digit</td>
      <td>pdunlap@yahoo.com</td>
      <td>Scientist, product/process development</td>
      <td>149.146.147.205</td>
      <td>el</td>
      <td>98.14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9374 Jasmine Spurs Suite 508\nSouth John, TN 8...</td>
      <td>28 rn</td>
      <td>PM</td>
      <td>Opera/8.93.(Windows 98; Win 9x 4.90; en-US) Pr...</td>
      <td>Fletcher, Richards and Whitaker</td>
      <td>3337758169645356</td>
      <td>11/18</td>
      <td>561</td>
      <td>Mastercard</td>
      <td>anthony41@reed.com</td>
      <td>Drilling engineer</td>
      <td>15.160.41.51</td>
      <td>fr</td>
      <td>70.73</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Unit 0065 Box 5052\nDPO AP 27450</td>
      <td>94 vE</td>
      <td>PM</td>
      <td>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...</td>
      <td>Simpson, Williams and Pham</td>
      <td>675957666125</td>
      <td>08/19</td>
      <td>699</td>
      <td>JCB 16 digit</td>
      <td>amymiller@morales-harrison.com</td>
      <td>Customer service manager</td>
      <td>132.207.160.22</td>
      <td>de</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7780 Julia Fords\nNew Stacy, WA 45798</td>
      <td>36 vm</td>
      <td>PM</td>
      <td>Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0 ...</td>
      <td>Williams, Marshall and Buchanan</td>
      <td>6011578504430710</td>
      <td>02/24</td>
      <td>384</td>
      <td>Discover</td>
      <td>brent16@olson-robinson.info</td>
      <td>Drilling engineer</td>
      <td>30.250.74.19</td>
      <td>es</td>
      <td>78.04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23012 Munoz Drive Suite 337\nNew Cynthia, TX 5...</td>
      <td>20 IE</td>
      <td>AM</td>
      <td>Opera/9.58.(X11; Linux x86_64; it-IT) Presto/2...</td>
      <td>Brown, Watson and Andrews</td>
      <td>6011456623207998</td>
      <td>10/25</td>
      <td>678</td>
      <td>Diners Club / Carte Blanche</td>
      <td>christopherwright@gmail.com</td>
      <td>Fine artist</td>
      <td>24.140.33.94</td>
      <td>es</td>
      <td>77.82</td>
    </tr>
  </tbody>
</table>
</div>



### 1) Finding out the datatype of each column


```python
data.dtypes
```




    Address              object
    Lot                  object
    AM or PM             object
    Browser Info         object
    Company              object
    Credit Card           int64
    CC Exp Date          object
    CC Security Code      int64
    CC Provider          object
    Email                object
    Job                  object
    IP Address           object
    Language             object
    Purchase Price      float64
    dtype: object



### 2) Checking if the data had any null values


```python
data.isnull().sum()
```




    Address             0
    Lot                 0
    AM or PM            0
    Browser Info        0
    Company             0
    Credit Card         0
    CC Exp Date         0
    CC Security Code    0
    CC Provider         0
    Email               0
    Job                 0
    IP Address          0
    Language            0
    Purchase Price      0
    dtype: int64



### 3) Checking the number of columns in the dataframe


```python
len(data.columns)
```




    14



### 4) Checking the length of dataframe


```python
len(data)
```




    10000




```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10000 entries, 0 to 9999
    Data columns (total 14 columns):
     #   Column            Non-Null Count  Dtype  
    ---  ------            --------------  -----  
     0   Address           10000 non-null  object 
     1   Lot               10000 non-null  object 
     2   AM or PM          10000 non-null  object 
     3   Browser Info      10000 non-null  object 
     4   Company           10000 non-null  object 
     5   Credit Card       10000 non-null  int64  
     6   CC Exp Date       10000 non-null  object 
     7   CC Security Code  10000 non-null  int64  
     8   CC Provider       10000 non-null  object 
     9   Email             10000 non-null  object 
     10  Job               10000 non-null  object 
     11  IP Address        10000 non-null  object 
     12  Language          10000 non-null  object 
     13  Purchase Price    10000 non-null  float64
    dtypes: float64(1), int64(2), object(11)
    memory usage: 1.1+ MB
    

### 5) Fetching the highest purchse price


```python
data['Purchase Price'].max()
```




    99.99



### 6) Fetching the lowest purchse price


```python
data['Purchase Price'].min()
```




    0.0



### 7) Finding the average purchase price


```python
data['Purchase Price'].mean()
```




    50.34730200000025



### 8) Fetching the data of all those people who have french as their language


```python
data[data['Language']=='fr'].head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Address</th>
      <th>Lot</th>
      <th>AM or PM</th>
      <th>Browser Info</th>
      <th>Company</th>
      <th>Credit Card</th>
      <th>CC Exp Date</th>
      <th>CC Security Code</th>
      <th>CC Provider</th>
      <th>Email</th>
      <th>Job</th>
      <th>IP Address</th>
      <th>Language</th>
      <th>Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>9374 Jasmine Spurs Suite 508\nSouth John, TN 8...</td>
      <td>28 rn</td>
      <td>PM</td>
      <td>Opera/8.93.(Windows 98; Win 9x 4.90; en-US) Pr...</td>
      <td>Fletcher, Richards and Whitaker</td>
      <td>3337758169645356</td>
      <td>11/18</td>
      <td>561</td>
      <td>Mastercard</td>
      <td>anthony41@reed.com</td>
      <td>Drilling engineer</td>
      <td>15.160.41.51</td>
      <td>fr</td>
      <td>70.73</td>
    </tr>
    <tr>
      <th>19</th>
      <td>125 Hall Summit\nBoothton, IL 41721</td>
      <td>99 CU</td>
      <td>PM</td>
      <td>Mozilla/5.0 (compatible; MSIE 7.0; Windows NT ...</td>
      <td>Turner-Mckinney</td>
      <td>676343504830</td>
      <td>02/20</td>
      <td>440</td>
      <td>VISA 16 digit</td>
      <td>ruiznicole@gmail.com</td>
      <td>Designer, interior/spatial</td>
      <td>25.105.209.214</td>
      <td>fr</td>
      <td>58.39</td>
    </tr>
    <tr>
      <th>53</th>
      <td>PSC 9431, Box 7059\nAPO AA 29285-1363</td>
      <td>14 qD</td>
      <td>AM</td>
      <td>Opera/9.34.(X11; Linux x86_64; it-IT) Presto/2...</td>
      <td>Higgins, Cardenas and Kennedy</td>
      <td>869972604798355</td>
      <td>08/17</td>
      <td>157</td>
      <td>JCB 16 digit</td>
      <td>amorales@yahoo.com</td>
      <td>Technical author</td>
      <td>44.108.117.122</td>
      <td>fr</td>
      <td>10.41</td>
    </tr>
    <tr>
      <th>76</th>
      <td>49206 Campbell Port\nNorth Cliffordshire, HI 3...</td>
      <td>71 iu</td>
      <td>PM</td>
      <td>Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_9...</td>
      <td>Jacobs-Tucker</td>
      <td>6011343518820988</td>
      <td>01/17</td>
      <td>806</td>
      <td>Voyager</td>
      <td>eperez@hotmail.com</td>
      <td>Paramedic</td>
      <td>210.207.58.168</td>
      <td>fr</td>
      <td>57.34</td>
    </tr>
    <tr>
      <th>82</th>
      <td>493 Smith Valleys Suite 004\nNew Madelineville...</td>
      <td>35 ls</td>
      <td>PM</td>
      <td>Mozilla/5.0 (iPod; U; CPU iPhone OS 4_0 like M...</td>
      <td>Robinson, Johnston and Valdez</td>
      <td>4351359627548412</td>
      <td>06/17</td>
      <td>937</td>
      <td>VISA 13 digit</td>
      <td>amendez@yahoo.com</td>
      <td>Engineer, materials</td>
      <td>163.129.163.100</td>
      <td>fr</td>
      <td>49.04</td>
    </tr>
  </tbody>
</table>
</div>




```python
# no of ppl who have french as their language
len(data[data['Language']=='fr'])
```




    1097




```python
# different way to find the no
data[data['Language']=='fr'].count()
```




    Address             1097
    Lot                 1097
    AM or PM            1097
    Browser Info        1097
    Company             1097
    Credit Card         1097
    CC Exp Date         1097
    CC Security Code    1097
    CC Provider         1097
    Email               1097
    Job                 1097
    IP Address          1097
    Language            1097
    Purchase Price      1097
    dtype: int64



### 9) Finding the no of people who are engineers as per job title


```python
len(data[data['Job'].str.contains('engineer', case=False)])
```




    984



### 10) Finding the details of the person who has a specific IP Address


```python
# finding out the details of the person who has IP Address ad 132.207.160.22
data[data["IP Address"]== '132.207.160.22']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Address</th>
      <th>Lot</th>
      <th>AM or PM</th>
      <th>Browser Info</th>
      <th>Company</th>
      <th>Credit Card</th>
      <th>CC Exp Date</th>
      <th>CC Security Code</th>
      <th>CC Provider</th>
      <th>Email</th>
      <th>Job</th>
      <th>IP Address</th>
      <th>Language</th>
      <th>Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Unit 0065 Box 5052\nDPO AP 27450</td>
      <td>94 vE</td>
      <td>PM</td>
      <td>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...</td>
      <td>Simpson, Williams and Pham</td>
      <td>675957666125</td>
      <td>08/19</td>
      <td>699</td>
      <td>JCB 16 digit</td>
      <td>amymiller@morales-harrison.com</td>
      <td>Customer service manager</td>
      <td>132.207.160.22</td>
      <td>de</td>
      <td>0.95</td>
    </tr>
  </tbody>
</table>
</div>



### 11) Finding the no of people who have master card as their credit card provider and have also made a purchase above 50


```python
len(data[(data['CC Provider'] == 'Mastercard')&(data['Purchase Price']>50)])
```




    5052




```python
data[(data['CC Provider'] == 'Mastercard')&(data['Purchase Price']>50)].head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Address</th>
      <th>Lot</th>
      <th>AM or PM</th>
      <th>Browser Info</th>
      <th>Company</th>
      <th>Credit Card</th>
      <th>CC Exp Date</th>
      <th>CC Security Code</th>
      <th>CC Provider</th>
      <th>Email</th>
      <th>Job</th>
      <th>IP Address</th>
      <th>Language</th>
      <th>Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>9374 Jasmine Spurs Suite 508\nSouth John, TN 8...</td>
      <td>28 rn</td>
      <td>PM</td>
      <td>Opera/8.93.(Windows 98; Win 9x 4.90; en-US) Pr...</td>
      <td>Fletcher, Richards and Whitaker</td>
      <td>3337758169645356</td>
      <td>11/18</td>
      <td>561</td>
      <td>Mastercard</td>
      <td>anthony41@reed.com</td>
      <td>Drilling engineer</td>
      <td>15.160.41.51</td>
      <td>fr</td>
      <td>70.73</td>
    </tr>
    <tr>
      <th>18</th>
      <td>461 Christopher Square\nWest Michaelchester, C...</td>
      <td>17 SB</td>
      <td>PM</td>
      <td>Mozilla/5.0 (X11; Linux i686; rv:1.9.6.20) Gec...</td>
      <td>Beard, Abbott and Pena</td>
      <td>6011350184276270</td>
      <td>12/22</td>
      <td>767</td>
      <td>Mastercard</td>
      <td>hannah63@yahoo.com</td>
      <td>Photographer</td>
      <td>73.250.176.201</td>
      <td>el</td>
      <td>70.15</td>
    </tr>
    <tr>
      <th>31</th>
      <td>USNS Alvarado\nFPO AA 27052-1231</td>
      <td>26 Lh</td>
      <td>PM</td>
      <td>Opera/8.84.(X11; Linux i686; sl-SI) Presto/2.9...</td>
      <td>Nicholson Group</td>
      <td>4614997834548</td>
      <td>03/22</td>
      <td>909</td>
      <td>Mastercard</td>
      <td>ashley12@hotmail.com</td>
      <td>Sales executive</td>
      <td>94.176.142.201</td>
      <td>en</td>
      <td>94.14</td>
    </tr>
    <tr>
      <th>35</th>
      <td>93392 Webb Gardens Apt. 220\nLaurabury, AR 999...</td>
      <td>37 om</td>
      <td>AM</td>
      <td>Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7...</td>
      <td>Mora Ltd</td>
      <td>6011049630969815</td>
      <td>09/16</td>
      <td>367</td>
      <td>Mastercard</td>
      <td>hgonzalez@mcdowell.com</td>
      <td>Lecturer, further education</td>
      <td>216.23.95.40</td>
      <td>zh</td>
      <td>97.46</td>
    </tr>
    <tr>
      <th>90</th>
      <td>431 Bowen Lights\nFergusonborough, MH 01362</td>
      <td>31 tG</td>
      <td>AM</td>
      <td>Mozilla/5.0 (Windows NT 5.2; it-IT; rv:1.9.1.2...</td>
      <td>Copeland-Lee</td>
      <td>639032576097</td>
      <td>06/18</td>
      <td>868</td>
      <td>Mastercard</td>
      <td>nrogers@brown.com</td>
      <td>Teacher, English as a foreign language</td>
      <td>153.188.13.203</td>
      <td>es</td>
      <td>78.86</td>
    </tr>
  </tbody>
</table>
</div>



### 12) Finding the email id of the person who has a specific credit card


```python
# finding out the email of the person who has a credit number as 4664825258997302
data[data['Credit Card']== 4664825258997302]['Email']
```




    9992    bberry@wright.net
    Name: Email, dtype: object



### 13) Finding out the number of purchases made during AM and PM


```python
data['AM or PM'].value_counts()
```




    PM    5068
    AM    4932
    Name: AM or PM, dtype: int64



### 14) Finding out the number of people hose credit card expires in 2020


```python
def fun():
    count = 0
    for date in data ['CC Exp Date']:
        if date.split('/')[1] == '20':
            count = count+1
    print(count)
```


```python
fun()
```

    988
    


```python
data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')].head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Address</th>
      <th>Lot</th>
      <th>AM or PM</th>
      <th>Browser Info</th>
      <th>Company</th>
      <th>Credit Card</th>
      <th>CC Exp Date</th>
      <th>CC Security Code</th>
      <th>CC Provider</th>
      <th>Email</th>
      <th>Job</th>
      <th>IP Address</th>
      <th>Language</th>
      <th>Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16629 Pace Camp Apt. 448\nAlexisborough, NE 77...</td>
      <td>46 in</td>
      <td>PM</td>
      <td>Opera/9.56.(X11; Linux x86_64; sl-SI) Presto/2...</td>
      <td>Martinez-Herman</td>
      <td>6011929061123406</td>
      <td>02/20</td>
      <td>900</td>
      <td>JCB 16 digit</td>
      <td>pdunlap@yahoo.com</td>
      <td>Scientist, product/process development</td>
      <td>149.146.147.205</td>
      <td>el</td>
      <td>98.14</td>
    </tr>
    <tr>
      <th>19</th>
      <td>125 Hall Summit\nBoothton, IL 41721</td>
      <td>99 CU</td>
      <td>PM</td>
      <td>Mozilla/5.0 (compatible; MSIE 7.0; Windows NT ...</td>
      <td>Turner-Mckinney</td>
      <td>676343504830</td>
      <td>02/20</td>
      <td>440</td>
      <td>VISA 16 digit</td>
      <td>ruiznicole@gmail.com</td>
      <td>Designer, interior/spatial</td>
      <td>25.105.209.214</td>
      <td>fr</td>
      <td>58.39</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Unit 3628 Box 6778\nDPO AE 72362</td>
      <td>39 Qm</td>
      <td>PM</td>
      <td>Mozilla/5.0 (Windows 98; Win 9x 4.90) AppleWeb...</td>
      <td>Martinez-Wilson</td>
      <td>4942281854569455</td>
      <td>01/20</td>
      <td>8360</td>
      <td>JCB 16 digit</td>
      <td>shane21@atkinson.com</td>
      <td>Civil Service fast streamer</td>
      <td>196.37.134.217</td>
      <td>pt</td>
      <td>56.63</td>
    </tr>
    <tr>
      <th>36</th>
      <td>9374 Skinner Common Apt. 254\nChristopherfort,...</td>
      <td>80 Fq</td>
      <td>PM</td>
      <td>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...</td>
      <td>Hanna-Grant</td>
      <td>180042289507877</td>
      <td>09/20</td>
      <td>912</td>
      <td>VISA 16 digit</td>
      <td>saundersernest@walsh.com</td>
      <td>Animal technologist</td>
      <td>85.134.58.250</td>
      <td>zh</td>
      <td>9.77</td>
    </tr>
    <tr>
      <th>38</th>
      <td>9671 Riley Drives Apt. 746\nPort Davidtown, TN...</td>
      <td>15 vj</td>
      <td>AM</td>
      <td>Mozilla/5.0 (X11; Linux i686; rv:1.9.6.20) Gec...</td>
      <td>Bryant, Hubbard and Gonzales</td>
      <td>210094965373094</td>
      <td>12/20</td>
      <td>248</td>
      <td>Voyager</td>
      <td>djennings@boyd-english.org</td>
      <td>Music therapist</td>
      <td>143.138.65.219</td>
      <td>en</td>
      <td>30.07</td>
    </tr>
  </tbody>
</table>
</div>


