```python
#read excel file in pandas
import pandas as pd
df = pd.read_excel(r"C:\Users\vmsof\Downloads\bank_customers.xlsx")
df
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
      <th>customer_id</th>
      <th>vintage</th>
      <th>age</th>
      <th>gender</th>
      <th>phone_number</th>
      <th>address</th>
      <th>dependents</th>
      <th>occupation</th>
      <th>city</th>
      <th>customer_nw_category</th>
      <th>...</th>
      <th>average_monthly_balance_prevQ2</th>
      <th>current_month_credit</th>
      <th>previous_month_credit</th>
      <th>current_month_debit</th>
      <th>previous_month_debit</th>
      <th>current_month_balance</th>
      <th>previous_month_balance</th>
      <th>churn</th>
      <th>last_transaction</th>
      <th>not_useful_column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2101</td>
      <td>66</td>
      <td>Male</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>...</td>
      <td>1449.07</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2101</td>
      <td>66</td>
      <td>Male</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>...</td>
      <td>1449.07</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>7066950392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>...</td>
      <td>12419.41</td>
      <td>0.56</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>7066950392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>...</td>
      <td>12419.41</td>
      <td>0.56</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2194</td>
      <td>31</td>
      <td>/Male/</td>
      <td>123-543-2345</td>
      <td>980 Paper Avenue, Pennsylvania, 18503</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>146.0</td>
      <td>2</td>
      <td>...</td>
      <td>2815.94</td>
      <td>0.61</td>
      <td>0.61</td>
      <td>6046.73</td>
      <td>259.23</td>
      <td>5006.28</td>
      <td>5070.14</td>
      <td>0</td>
      <td>NaT</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>28380</th>
      <td>30297</td>
      <td>2325</td>
      <td>10</td>
      <td>Female</td>
      <td>876|678|31828</td>
      <td>29269 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1020.0</td>
      <td>2</td>
      <td>...</td>
      <td>2787.70</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>1076.43</td>
      <td>1076.43</td>
      <td>0</td>
      <td>2019-10-22 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>28381</th>
      <td>30298</td>
      <td>1537</td>
      <td>34</td>
      <td>Female</td>
      <td>876|678|31829</td>
      <td>29270 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>1046.0</td>
      <td>2</td>
      <td>...</td>
      <td>3865.55</td>
      <td>1.71</td>
      <td>2.29</td>
      <td>901.00</td>
      <td>1014.07</td>
      <td>3738.54</td>
      <td>3690.32</td>
      <td>0</td>
      <td>2019-12-17 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>28382</th>
      <td>30299</td>
      <td>2376</td>
      <td>47</td>
      <td>Male</td>
      <td>876|678|31830</td>
      <td>29271 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>1096.0</td>
      <td>2</td>
      <td>...</td>
      <td>21925.81</td>
      <td>4666.84</td>
      <td>3883.06</td>
      <td>168.23</td>
      <td>71.80</td>
      <td>61078.50</td>
      <td>57564.24</td>
      <td>1</td>
      <td>2019-12-31 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>28383</th>
      <td>30300</td>
      <td>1745</td>
      <td>50</td>
      <td>Male</td>
      <td>876|678|31831</td>
      <td>29272 Tatooine Road, Tatooine</td>
      <td>3.0</td>
      <td>self_employed</td>
      <td>1219.0</td>
      <td>3</td>
      <td>...</td>
      <td>1857.42</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1625.55</td>
      <td>1625.55</td>
      <td>0</td>
      <td>NaT</td>
      <td>True</td>
    </tr>
    <tr>
      <th>28384</th>
      <td>30301</td>
      <td>1175</td>
      <td>18</td>
      <td>Male</td>
      <td>876|678|31832</td>
      <td>29273 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1232.0</td>
      <td>2</td>
      <td>...</td>
      <td>4447.45</td>
      <td>0.11</td>
      <td>7.44</td>
      <td>714.40</td>
      <td>1094.09</td>
      <td>2402.62</td>
      <td>3260.58</td>
      <td>1</td>
      <td>2019-11-02 00:00:00</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>28385 rows × 24 columns</p>
</div>




```python
#set index
df = df.set_index('customer_id')
df
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
      <th>vintage</th>
      <th>age</th>
      <th>gender</th>
      <th>phone_number</th>
      <th>address</th>
      <th>dependents</th>
      <th>occupation</th>
      <th>city</th>
      <th>customer_nw_category</th>
      <th>branch_code</th>
      <th>...</th>
      <th>average_monthly_balance_prevQ2</th>
      <th>current_month_credit</th>
      <th>previous_month_credit</th>
      <th>current_month_debit</th>
      <th>previous_month_debit</th>
      <th>current_month_balance</th>
      <th>previous_month_balance</th>
      <th>churn</th>
      <th>last_transaction</th>
      <th>not_useful_column</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>Male</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>1449.07</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>Male</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>1449.07</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>7066950392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>12419.41</td>
      <td>0.56</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>7066950392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>12419.41</td>
      <td>0.56</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2194</td>
      <td>31</td>
      <td>/Male/</td>
      <td>123-543-2345</td>
      <td>980 Paper Avenue, Pennsylvania, 18503</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>146.0</td>
      <td>2</td>
      <td>41</td>
      <td>...</td>
      <td>2815.94</td>
      <td>0.61</td>
      <td>0.61</td>
      <td>6046.73</td>
      <td>259.23</td>
      <td>5006.28</td>
      <td>5070.14</td>
      <td>0</td>
      <td>NaT</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>30297</th>
      <td>2325</td>
      <td>10</td>
      <td>Female</td>
      <td>876|678|31828</td>
      <td>29269 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1020.0</td>
      <td>2</td>
      <td>1207</td>
      <td>...</td>
      <td>2787.70</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>1076.43</td>
      <td>1076.43</td>
      <td>0</td>
      <td>2019-10-22 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>30298</th>
      <td>1537</td>
      <td>34</td>
      <td>Female</td>
      <td>876|678|31829</td>
      <td>29270 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>1046.0</td>
      <td>2</td>
      <td>223</td>
      <td>...</td>
      <td>3865.55</td>
      <td>1.71</td>
      <td>2.29</td>
      <td>901.00</td>
      <td>1014.07</td>
      <td>3738.54</td>
      <td>3690.32</td>
      <td>0</td>
      <td>2019-12-17 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>30299</th>
      <td>2376</td>
      <td>47</td>
      <td>Male</td>
      <td>876|678|31830</td>
      <td>29271 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>1096.0</td>
      <td>2</td>
      <td>588</td>
      <td>...</td>
      <td>21925.81</td>
      <td>4666.84</td>
      <td>3883.06</td>
      <td>168.23</td>
      <td>71.80</td>
      <td>61078.50</td>
      <td>57564.24</td>
      <td>1</td>
      <td>2019-12-31 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>30300</th>
      <td>1745</td>
      <td>50</td>
      <td>Male</td>
      <td>876|678|31831</td>
      <td>29272 Tatooine Road, Tatooine</td>
      <td>3.0</td>
      <td>self_employed</td>
      <td>1219.0</td>
      <td>3</td>
      <td>274</td>
      <td>...</td>
      <td>1857.42</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1625.55</td>
      <td>1625.55</td>
      <td>0</td>
      <td>NaT</td>
      <td>True</td>
    </tr>
    <tr>
      <th>30301</th>
      <td>1175</td>
      <td>18</td>
      <td>Male</td>
      <td>876|678|31832</td>
      <td>29273 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1232.0</td>
      <td>2</td>
      <td>474</td>
      <td>...</td>
      <td>4447.45</td>
      <td>0.11</td>
      <td>7.44</td>
      <td>714.40</td>
      <td>1094.09</td>
      <td>2402.62</td>
      <td>3260.58</td>
      <td>1</td>
      <td>2019-11-02 00:00:00</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>28385 rows × 23 columns</p>
</div>




```python
# check for duplicate values 
duplicate_values = df.duplicated()
print(duplicate_values)
```

    customer_id
    1        False
    1         True
    2        False
    2         True
    4        False
             ...  
    30297    False
    30298    False
    30299    False
    30300    False
    30301    False
    Length: 28385, dtype: bool
    


```python
# remove the dublicate rows data
df.drop_duplicates()
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
      <th>vintage</th>
      <th>age</th>
      <th>gender</th>
      <th>phone_number</th>
      <th>address</th>
      <th>dependents</th>
      <th>occupation</th>
      <th>city</th>
      <th>customer_nw_category</th>
      <th>branch_code</th>
      <th>...</th>
      <th>average_monthly_balance_prevQ2</th>
      <th>current_month_credit</th>
      <th>previous_month_credit</th>
      <th>current_month_debit</th>
      <th>previous_month_debit</th>
      <th>current_month_balance</th>
      <th>previous_month_balance</th>
      <th>churn</th>
      <th>last_transaction</th>
      <th>not_useful_column</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>Male</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>1449.07</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>7066950392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>12419.41</td>
      <td>0.56</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2194</td>
      <td>31</td>
      <td>/Male/</td>
      <td>123-543-2345</td>
      <td>980 Paper Avenue, Pennsylvania, 18503</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>146.0</td>
      <td>2</td>
      <td>41</td>
      <td>...</td>
      <td>2815.94</td>
      <td>0.61</td>
      <td>0.61</td>
      <td>6046.73</td>
      <td>259.23</td>
      <td>5006.28</td>
      <td>5070.14</td>
      <td>0</td>
      <td>NaT</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2194</td>
      <td>31</td>
      <td>/Male</td>
      <td>876|678|3469</td>
      <td>123 Dragons Road</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>146.0</td>
      <td>2</td>
      <td>41</td>
      <td>...</td>
      <td>2815.94</td>
      <td>0.61</td>
      <td>0.61</td>
      <td>6046.73</td>
      <td>259.23</td>
      <td>5006.28</td>
      <td>5070.14</td>
      <td>0</td>
      <td>NaT</td>
      <td>False</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1579</td>
      <td>42</td>
      <td>Male</td>
      <td>304-762-2467</td>
      <td>768 City Parkway</td>
      <td>2.0</td>
      <td>self_employed</td>
      <td>1494.0</td>
      <td>3</td>
      <td>388</td>
      <td>...</td>
      <td>1871.12</td>
      <td>0.33</td>
      <td>714.61</td>
      <td>588.62</td>
      <td>1538.06</td>
      <td>1157.15</td>
      <td>1677.16</td>
      <td>1</td>
      <td>2019-11-03 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>30297</th>
      <td>2325</td>
      <td>10</td>
      <td>Female</td>
      <td>876|678|31828</td>
      <td>29269 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1020.0</td>
      <td>2</td>
      <td>1207</td>
      <td>...</td>
      <td>2787.70</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>1076.43</td>
      <td>1076.43</td>
      <td>0</td>
      <td>2019-10-22 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>30298</th>
      <td>1537</td>
      <td>34</td>
      <td>Female</td>
      <td>876|678|31829</td>
      <td>29270 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>1046.0</td>
      <td>2</td>
      <td>223</td>
      <td>...</td>
      <td>3865.55</td>
      <td>1.71</td>
      <td>2.29</td>
      <td>901.00</td>
      <td>1014.07</td>
      <td>3738.54</td>
      <td>3690.32</td>
      <td>0</td>
      <td>2019-12-17 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>30299</th>
      <td>2376</td>
      <td>47</td>
      <td>Male</td>
      <td>876|678|31830</td>
      <td>29271 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>1096.0</td>
      <td>2</td>
      <td>588</td>
      <td>...</td>
      <td>21925.81</td>
      <td>4666.84</td>
      <td>3883.06</td>
      <td>168.23</td>
      <td>71.80</td>
      <td>61078.50</td>
      <td>57564.24</td>
      <td>1</td>
      <td>2019-12-31 00:00:00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>30300</th>
      <td>1745</td>
      <td>50</td>
      <td>Male</td>
      <td>876|678|31831</td>
      <td>29272 Tatooine Road, Tatooine</td>
      <td>3.0</td>
      <td>self_employed</td>
      <td>1219.0</td>
      <td>3</td>
      <td>274</td>
      <td>...</td>
      <td>1857.42</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1625.55</td>
      <td>1625.55</td>
      <td>0</td>
      <td>NaT</td>
      <td>True</td>
    </tr>
    <tr>
      <th>30301</th>
      <td>1175</td>
      <td>18</td>
      <td>Male</td>
      <td>876|678|31832</td>
      <td>29273 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1232.0</td>
      <td>2</td>
      <td>474</td>
      <td>...</td>
      <td>4447.45</td>
      <td>0.11</td>
      <td>7.44</td>
      <td>714.40</td>
      <td>1094.09</td>
      <td>2402.62</td>
      <td>3260.58</td>
      <td>1</td>
      <td>2019-11-02 00:00:00</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>28382 rows × 23 columns</p>
</div>




```python
#delete unnecessary column data
df = df.drop(columns = 'not_useful_column')
df
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
      <th>vintage</th>
      <th>age</th>
      <th>gender</th>
      <th>phone_number</th>
      <th>address</th>
      <th>dependents</th>
      <th>occupation</th>
      <th>city</th>
      <th>customer_nw_category</th>
      <th>branch_code</th>
      <th>...</th>
      <th>average_monthly_balance_prevQ</th>
      <th>average_monthly_balance_prevQ2</th>
      <th>current_month_credit</th>
      <th>previous_month_credit</th>
      <th>current_month_debit</th>
      <th>previous_month_debit</th>
      <th>current_month_balance</th>
      <th>previous_month_balance</th>
      <th>churn</th>
      <th>last_transaction</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>Male</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>1458.71</td>
      <td>1449.07</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>Male</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>1458.71</td>
      <td>1449.07</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>7066950392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>7799.26</td>
      <td>12419.41</td>
      <td>0.56</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>7066950392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>7799.26</td>
      <td>12419.41</td>
      <td>0.56</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2194</td>
      <td>31</td>
      <td>/Male/</td>
      <td>123-543-2345</td>
      <td>980 Paper Avenue, Pennsylvania, 18503</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>146.0</td>
      <td>2</td>
      <td>41</td>
      <td>...</td>
      <td>4910.17</td>
      <td>2815.94</td>
      <td>0.61</td>
      <td>0.61</td>
      <td>6046.73</td>
      <td>259.23</td>
      <td>5006.28</td>
      <td>5070.14</td>
      <td>0</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>30297</th>
      <td>2325</td>
      <td>10</td>
      <td>Female</td>
      <td>876|678|31828</td>
      <td>29269 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1020.0</td>
      <td>2</td>
      <td>1207</td>
      <td>...</td>
      <td>2282.19</td>
      <td>2787.70</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>1076.43</td>
      <td>1076.43</td>
      <td>0</td>
      <td>2019-10-22 00:00:00</td>
    </tr>
    <tr>
      <th>30298</th>
      <td>1537</td>
      <td>34</td>
      <td>Female</td>
      <td>876|678|31829</td>
      <td>29270 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>1046.0</td>
      <td>2</td>
      <td>223</td>
      <td>...</td>
      <td>3668.83</td>
      <td>3865.55</td>
      <td>1.71</td>
      <td>2.29</td>
      <td>901.00</td>
      <td>1014.07</td>
      <td>3738.54</td>
      <td>3690.32</td>
      <td>0</td>
      <td>2019-12-17 00:00:00</td>
    </tr>
    <tr>
      <th>30299</th>
      <td>2376</td>
      <td>47</td>
      <td>Male</td>
      <td>876|678|31830</td>
      <td>29271 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>1096.0</td>
      <td>2</td>
      <td>588</td>
      <td>...</td>
      <td>53444.81</td>
      <td>21925.81</td>
      <td>4666.84</td>
      <td>3883.06</td>
      <td>168.23</td>
      <td>71.80</td>
      <td>61078.50</td>
      <td>57564.24</td>
      <td>1</td>
      <td>2019-12-31 00:00:00</td>
    </tr>
    <tr>
      <th>30300</th>
      <td>1745</td>
      <td>50</td>
      <td>Male</td>
      <td>876|678|31831</td>
      <td>29272 Tatooine Road, Tatooine</td>
      <td>3.0</td>
      <td>self_employed</td>
      <td>1219.0</td>
      <td>3</td>
      <td>274</td>
      <td>...</td>
      <td>1683.20</td>
      <td>1857.42</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1625.55</td>
      <td>1625.55</td>
      <td>0</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>30301</th>
      <td>1175</td>
      <td>18</td>
      <td>Male</td>
      <td>876|678|31832</td>
      <td>29273 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1232.0</td>
      <td>2</td>
      <td>474</td>
      <td>...</td>
      <td>3213.44</td>
      <td>4447.45</td>
      <td>0.11</td>
      <td>7.44</td>
      <td>714.40</td>
      <td>1094.09</td>
      <td>2402.62</td>
      <td>3260.58</td>
      <td>1</td>
      <td>2019-11-02 00:00:00</td>
    </tr>
  </tbody>
</table>
<p>28385 rows × 22 columns</p>
</div>




```python
#clean geneder column data
df['gender']= df['gender'].str.lstrip('/')
df['gender']= df['gender'].str.rstrip('/')
df['gender']= df['gender'].str.strip()
df['gender'] = df['gender'].str.replace('Female','F')
df['gender'] = df['gender'].str.replace('Male','M')
df
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
      <th>vintage</th>
      <th>age</th>
      <th>gender</th>
      <th>phone_number</th>
      <th>address</th>
      <th>dependents</th>
      <th>occupation</th>
      <th>city</th>
      <th>customer_nw_category</th>
      <th>branch_code</th>
      <th>...</th>
      <th>average_monthly_balance_prevQ</th>
      <th>average_monthly_balance_prevQ2</th>
      <th>current_month_credit</th>
      <th>previous_month_credit</th>
      <th>current_month_debit</th>
      <th>previous_month_debit</th>
      <th>current_month_balance</th>
      <th>previous_month_balance</th>
      <th>churn</th>
      <th>last_transaction</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>M</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>1458.71</td>
      <td>1449.07</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>M</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>1458.71</td>
      <td>1449.07</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>7066950392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>7799.26</td>
      <td>12419.41</td>
      <td>0.56</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>7066950392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>7799.26</td>
      <td>12419.41</td>
      <td>0.56</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2194</td>
      <td>31</td>
      <td>M</td>
      <td>123-543-2345</td>
      <td>980 Paper Avenue, Pennsylvania, 18503</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>146.0</td>
      <td>2</td>
      <td>41</td>
      <td>...</td>
      <td>4910.17</td>
      <td>2815.94</td>
      <td>0.61</td>
      <td>0.61</td>
      <td>6046.73</td>
      <td>259.23</td>
      <td>5006.28</td>
      <td>5070.14</td>
      <td>0</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>30297</th>
      <td>2325</td>
      <td>10</td>
      <td>F</td>
      <td>876|678|31828</td>
      <td>29269 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1020.0</td>
      <td>2</td>
      <td>1207</td>
      <td>...</td>
      <td>2282.19</td>
      <td>2787.70</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>1076.43</td>
      <td>1076.43</td>
      <td>0</td>
      <td>2019-10-22 00:00:00</td>
    </tr>
    <tr>
      <th>30298</th>
      <td>1537</td>
      <td>34</td>
      <td>F</td>
      <td>876|678|31829</td>
      <td>29270 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>1046.0</td>
      <td>2</td>
      <td>223</td>
      <td>...</td>
      <td>3668.83</td>
      <td>3865.55</td>
      <td>1.71</td>
      <td>2.29</td>
      <td>901.00</td>
      <td>1014.07</td>
      <td>3738.54</td>
      <td>3690.32</td>
      <td>0</td>
      <td>2019-12-17 00:00:00</td>
    </tr>
    <tr>
      <th>30299</th>
      <td>2376</td>
      <td>47</td>
      <td>M</td>
      <td>876|678|31830</td>
      <td>29271 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>1096.0</td>
      <td>2</td>
      <td>588</td>
      <td>...</td>
      <td>53444.81</td>
      <td>21925.81</td>
      <td>4666.84</td>
      <td>3883.06</td>
      <td>168.23</td>
      <td>71.80</td>
      <td>61078.50</td>
      <td>57564.24</td>
      <td>1</td>
      <td>2019-12-31 00:00:00</td>
    </tr>
    <tr>
      <th>30300</th>
      <td>1745</td>
      <td>50</td>
      <td>M</td>
      <td>876|678|31831</td>
      <td>29272 Tatooine Road, Tatooine</td>
      <td>3.0</td>
      <td>self_employed</td>
      <td>1219.0</td>
      <td>3</td>
      <td>274</td>
      <td>...</td>
      <td>1683.20</td>
      <td>1857.42</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1625.55</td>
      <td>1625.55</td>
      <td>0</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>30301</th>
      <td>1175</td>
      <td>18</td>
      <td>M</td>
      <td>876|678|31832</td>
      <td>29273 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1232.0</td>
      <td>2</td>
      <td>474</td>
      <td>...</td>
      <td>3213.44</td>
      <td>4447.45</td>
      <td>0.11</td>
      <td>7.44</td>
      <td>714.40</td>
      <td>1094.09</td>
      <td>2402.62</td>
      <td>3260.58</td>
      <td>1</td>
      <td>2019-11-02 00:00:00</td>
    </tr>
  </tbody>
</table>
<p>28385 rows × 22 columns</p>
</div>




```python
#clean phone_number column data
df['phone_number'] = df['phone_number'].apply(lambda x : str(x))
df['phone_number'] = df['phone_number'].str.replace('[^a-zA-Z0-9]', '', regex=True)
df['phone_number'] = df['phone_number'].apply(lambda x : x[0:3] + '-' + x[3:6] + '-' + x[6:10])
df['phone_number'] = df['phone_number'].str.replace('nan--','')
df['phone_number'] = df['phone_number'].str.replace('Na--','')
df
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
      <th>vintage</th>
      <th>age</th>
      <th>gender</th>
      <th>phone_number</th>
      <th>address</th>
      <th>dependents</th>
      <th>occupation</th>
      <th>city</th>
      <th>customer_nw_category</th>
      <th>branch_code</th>
      <th>...</th>
      <th>average_monthly_balance_prevQ</th>
      <th>average_monthly_balance_prevQ2</th>
      <th>current_month_credit</th>
      <th>previous_month_credit</th>
      <th>current_month_debit</th>
      <th>previous_month_debit</th>
      <th>current_month_balance</th>
      <th>previous_month_balance</th>
      <th>churn</th>
      <th>last_transaction</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>M</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>1458.71</td>
      <td>1449.07</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>M</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>1458.71</td>
      <td>1449.07</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>706-695-0392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>7799.26</td>
      <td>12419.41</td>
      <td>0.56</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>706-695-0392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>7799.26</td>
      <td>12419.41</td>
      <td>0.56</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2194</td>
      <td>31</td>
      <td>M</td>
      <td>123-543-2345</td>
      <td>980 Paper Avenue, Pennsylvania, 18503</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>146.0</td>
      <td>2</td>
      <td>41</td>
      <td>...</td>
      <td>4910.17</td>
      <td>2815.94</td>
      <td>0.61</td>
      <td>0.61</td>
      <td>6046.73</td>
      <td>259.23</td>
      <td>5006.28</td>
      <td>5070.14</td>
      <td>0</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>30297</th>
      <td>2325</td>
      <td>10</td>
      <td>F</td>
      <td>876-678-3182</td>
      <td>29269 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1020.0</td>
      <td>2</td>
      <td>1207</td>
      <td>...</td>
      <td>2282.19</td>
      <td>2787.70</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>1076.43</td>
      <td>1076.43</td>
      <td>0</td>
      <td>2019-10-22 00:00:00</td>
    </tr>
    <tr>
      <th>30298</th>
      <td>1537</td>
      <td>34</td>
      <td>F</td>
      <td>876-678-3182</td>
      <td>29270 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>1046.0</td>
      <td>2</td>
      <td>223</td>
      <td>...</td>
      <td>3668.83</td>
      <td>3865.55</td>
      <td>1.71</td>
      <td>2.29</td>
      <td>901.00</td>
      <td>1014.07</td>
      <td>3738.54</td>
      <td>3690.32</td>
      <td>0</td>
      <td>2019-12-17 00:00:00</td>
    </tr>
    <tr>
      <th>30299</th>
      <td>2376</td>
      <td>47</td>
      <td>M</td>
      <td>876-678-3183</td>
      <td>29271 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>1096.0</td>
      <td>2</td>
      <td>588</td>
      <td>...</td>
      <td>53444.81</td>
      <td>21925.81</td>
      <td>4666.84</td>
      <td>3883.06</td>
      <td>168.23</td>
      <td>71.80</td>
      <td>61078.50</td>
      <td>57564.24</td>
      <td>1</td>
      <td>2019-12-31 00:00:00</td>
    </tr>
    <tr>
      <th>30300</th>
      <td>1745</td>
      <td>50</td>
      <td>M</td>
      <td>876-678-3183</td>
      <td>29272 Tatooine Road, Tatooine</td>
      <td>3.0</td>
      <td>self_employed</td>
      <td>1219.0</td>
      <td>3</td>
      <td>274</td>
      <td>...</td>
      <td>1683.20</td>
      <td>1857.42</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1625.55</td>
      <td>1625.55</td>
      <td>0</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>30301</th>
      <td>1175</td>
      <td>18</td>
      <td>M</td>
      <td>876-678-3183</td>
      <td>29273 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1232.0</td>
      <td>2</td>
      <td>474</td>
      <td>...</td>
      <td>3213.44</td>
      <td>4447.45</td>
      <td>0.11</td>
      <td>7.44</td>
      <td>714.40</td>
      <td>1094.09</td>
      <td>2402.62</td>
      <td>3260.58</td>
      <td>1</td>
      <td>2019-11-02 00:00:00</td>
    </tr>
  </tbody>
</table>
<p>28385 rows × 22 columns</p>
</div>




```python
#clean address column ans spilt it
df[['street_address','state','zip_code']]= df['address'].str.split(',',  n=2 , expand=True)
df
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
      <th>vintage</th>
      <th>age</th>
      <th>gender</th>
      <th>phone_number</th>
      <th>address</th>
      <th>dependents</th>
      <th>occupation</th>
      <th>city</th>
      <th>customer_nw_category</th>
      <th>branch_code</th>
      <th>...</th>
      <th>previous_month_credit</th>
      <th>current_month_debit</th>
      <th>previous_month_debit</th>
      <th>current_month_balance</th>
      <th>previous_month_balance</th>
      <th>churn</th>
      <th>last_transaction</th>
      <th>street_address</th>
      <th>state</th>
      <th>zip_code</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>M</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
      <td>123 Shire Lane</td>
      <td>Shire</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>M</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
      <td>123 Shire Lane</td>
      <td>Shire</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>706-695-0392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
      <td>298 Drugs Driveway</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>706-695-0392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>NaN</td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
      <td>298 Drugs Driveway</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2194</td>
      <td>31</td>
      <td>M</td>
      <td>123-543-2345</td>
      <td>980 Paper Avenue, Pennsylvania, 18503</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>146.0</td>
      <td>2</td>
      <td>41</td>
      <td>...</td>
      <td>0.61</td>
      <td>6046.73</td>
      <td>259.23</td>
      <td>5006.28</td>
      <td>5070.14</td>
      <td>0</td>
      <td>NaT</td>
      <td>980 Paper Avenue</td>
      <td>Pennsylvania</td>
      <td>18503</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>30297</th>
      <td>2325</td>
      <td>10</td>
      <td>F</td>
      <td>876-678-3182</td>
      <td>29269 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1020.0</td>
      <td>2</td>
      <td>1207</td>
      <td>...</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>1076.43</td>
      <td>1076.43</td>
      <td>0</td>
      <td>2019-10-22 00:00:00</td>
      <td>29269 Tatooine Road</td>
      <td>Tatooine</td>
      <td>None</td>
    </tr>
    <tr>
      <th>30298</th>
      <td>1537</td>
      <td>34</td>
      <td>F</td>
      <td>876-678-3182</td>
      <td>29270 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>1046.0</td>
      <td>2</td>
      <td>223</td>
      <td>...</td>
      <td>2.29</td>
      <td>901.00</td>
      <td>1014.07</td>
      <td>3738.54</td>
      <td>3690.32</td>
      <td>0</td>
      <td>2019-12-17 00:00:00</td>
      <td>29270 Tatooine Road</td>
      <td>Tatooine</td>
      <td>None</td>
    </tr>
    <tr>
      <th>30299</th>
      <td>2376</td>
      <td>47</td>
      <td>M</td>
      <td>876-678-3183</td>
      <td>29271 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>1096.0</td>
      <td>2</td>
      <td>588</td>
      <td>...</td>
      <td>3883.06</td>
      <td>168.23</td>
      <td>71.80</td>
      <td>61078.50</td>
      <td>57564.24</td>
      <td>1</td>
      <td>2019-12-31 00:00:00</td>
      <td>29271 Tatooine Road</td>
      <td>Tatooine</td>
      <td>None</td>
    </tr>
    <tr>
      <th>30300</th>
      <td>1745</td>
      <td>50</td>
      <td>M</td>
      <td>876-678-3183</td>
      <td>29272 Tatooine Road, Tatooine</td>
      <td>3.0</td>
      <td>self_employed</td>
      <td>1219.0</td>
      <td>3</td>
      <td>274</td>
      <td>...</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1625.55</td>
      <td>1625.55</td>
      <td>0</td>
      <td>NaT</td>
      <td>29272 Tatooine Road</td>
      <td>Tatooine</td>
      <td>None</td>
    </tr>
    <tr>
      <th>30301</th>
      <td>1175</td>
      <td>18</td>
      <td>M</td>
      <td>876-678-3183</td>
      <td>29273 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1232.0</td>
      <td>2</td>
      <td>474</td>
      <td>...</td>
      <td>7.44</td>
      <td>714.40</td>
      <td>1094.09</td>
      <td>2402.62</td>
      <td>3260.58</td>
      <td>1</td>
      <td>2019-11-02 00:00:00</td>
      <td>29273 Tatooine Road</td>
      <td>Tatooine</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>28385 rows × 25 columns</p>
</div>




```python
#remove Nan N/a
df=df.fillna('')
df = df.replace('NaT','')
df
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
      <th>vintage</th>
      <th>age</th>
      <th>gender</th>
      <th>phone_number</th>
      <th>address</th>
      <th>dependents</th>
      <th>occupation</th>
      <th>city</th>
      <th>customer_nw_category</th>
      <th>branch_code</th>
      <th>...</th>
      <th>previous_month_credit</th>
      <th>current_month_debit</th>
      <th>previous_month_debit</th>
      <th>current_month_balance</th>
      <th>previous_month_balance</th>
      <th>churn</th>
      <th>last_transaction</th>
      <th>street_address</th>
      <th>state</th>
      <th>zip_code</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>M</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
      <td>123 Shire Lane</td>
      <td>Shire</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>2101</td>
      <td>66</td>
      <td>M</td>
      <td>123-545-5421</td>
      <td>123 Shire Lane, Shire</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>187.0</td>
      <td>2</td>
      <td>755</td>
      <td>...</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1458.71</td>
      <td>1458.71</td>
      <td>0</td>
      <td>2019-05-21 00:00:00</td>
      <td>123 Shire Lane</td>
      <td>Shire</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>706-695-0392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td></td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
      <td>298 Drugs Driveway</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>2348</td>
      <td>35</td>
      <td>F</td>
      <td>706-695-0392</td>
      <td>298 Drugs Driveway</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td></td>
      <td>2</td>
      <td>3214</td>
      <td>...</td>
      <td>0.56</td>
      <td>5486.27</td>
      <td>100.56</td>
      <td>6496.78</td>
      <td>8787.61</td>
      <td>0</td>
      <td>2019-11-01 00:00:00</td>
      <td>298 Drugs Driveway</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>2194</td>
      <td>31</td>
      <td>M</td>
      <td>123-543-2345</td>
      <td>980 Paper Avenue, Pennsylvania, 18503</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>146.0</td>
      <td>2</td>
      <td>41</td>
      <td>...</td>
      <td>0.61</td>
      <td>6046.73</td>
      <td>259.23</td>
      <td>5006.28</td>
      <td>5070.14</td>
      <td>0</td>
      <td></td>
      <td>980 Paper Avenue</td>
      <td>Pennsylvania</td>
      <td>18503</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>30297</th>
      <td>2325</td>
      <td>10</td>
      <td>F</td>
      <td>876-678-3182</td>
      <td>29269 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1020.0</td>
      <td>2</td>
      <td>1207</td>
      <td>...</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>0.30</td>
      <td>1076.43</td>
      <td>1076.43</td>
      <td>0</td>
      <td>2019-10-22 00:00:00</td>
      <td>29269 Tatooine Road</td>
      <td>Tatooine</td>
      <td></td>
    </tr>
    <tr>
      <th>30298</th>
      <td>1537</td>
      <td>34</td>
      <td>F</td>
      <td>876-678-3182</td>
      <td>29270 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>self_employed</td>
      <td>1046.0</td>
      <td>2</td>
      <td>223</td>
      <td>...</td>
      <td>2.29</td>
      <td>901.00</td>
      <td>1014.07</td>
      <td>3738.54</td>
      <td>3690.32</td>
      <td>0</td>
      <td>2019-12-17 00:00:00</td>
      <td>29270 Tatooine Road</td>
      <td>Tatooine</td>
      <td></td>
    </tr>
    <tr>
      <th>30299</th>
      <td>2376</td>
      <td>47</td>
      <td>M</td>
      <td>876-678-3183</td>
      <td>29271 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>salaried</td>
      <td>1096.0</td>
      <td>2</td>
      <td>588</td>
      <td>...</td>
      <td>3883.06</td>
      <td>168.23</td>
      <td>71.80</td>
      <td>61078.50</td>
      <td>57564.24</td>
      <td>1</td>
      <td>2019-12-31 00:00:00</td>
      <td>29271 Tatooine Road</td>
      <td>Tatooine</td>
      <td></td>
    </tr>
    <tr>
      <th>30300</th>
      <td>1745</td>
      <td>50</td>
      <td>M</td>
      <td>876-678-3183</td>
      <td>29272 Tatooine Road, Tatooine</td>
      <td>3.0</td>
      <td>self_employed</td>
      <td>1219.0</td>
      <td>3</td>
      <td>274</td>
      <td>...</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>1625.55</td>
      <td>1625.55</td>
      <td>0</td>
      <td></td>
      <td>29272 Tatooine Road</td>
      <td>Tatooine</td>
      <td></td>
    </tr>
    <tr>
      <th>30301</th>
      <td>1175</td>
      <td>18</td>
      <td>M</td>
      <td>876-678-3183</td>
      <td>29273 Tatooine Road, Tatooine</td>
      <td>0.0</td>
      <td>student</td>
      <td>1232.0</td>
      <td>2</td>
      <td>474</td>
      <td>...</td>
      <td>7.44</td>
      <td>714.40</td>
      <td>1094.09</td>
      <td>2402.62</td>
      <td>3260.58</td>
      <td>1</td>
      <td>2019-11-02 00:00:00</td>
      <td>29273 Tatooine Road</td>
      <td>Tatooine</td>
      <td></td>
    </tr>
  </tbody>
</table>
<p>28385 rows × 25 columns</p>
</div>




```python

```
