# Distribution plots


```python
import seaborn as sns
import matplotlib.pyplot as plt
```


```python
tips = sns.load_dataset('tips')
```


```python
tips.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.displot(tips.total_bill)
plt.show() 
```


    
![png](output_4_0.png)
    



```python
sns.displot(tips.total_bill, stat = 'density', kde = True)
plt.show()
```


    
![png](output_5_0.png)
    



```python
sns.displot(tips.total_bill, bins = 30)
plt.show()
```


    
![png](output_6_0.png)
    



```python
sns.jointplot(x = 'total_bill', y = 'tip', data = tips)
plt.show()
```


    
![png](output_7_0.png)
    



```python
sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'hex')
plt.show()
```


    
![png](output_8_0.png)
    



```python
sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'reg')
plt.show()
```


    
![png](output_9_0.png)
    



```python
sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'kde')
plt.show()
```


    
![png](output_10_0.png)
    



```python
sns.pairplot(tips)
plt.show()
```


    
![png](output_11_0.png)
    



```python
sns.pairplot(tips, hue = 'sex')
plt.show()
```


    
![png](output_12_0.png)
    



```python
sns.pairplot(tips, hue = 'sex', palette = 'coolwarm')
plt.show()
```


    
![png](output_13_0.png)
    



```python
sns.rugplot(tips.total_bill, color = 'blue')
plt.show()
```


    
![png](output_14_0.png)
    


# Categorical plots


```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
tips = sns.load_dataset('tips')
tips.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.barplot(x = 'sex', y = 'total_bill', data = tips)
plt.show()
```


    
![png](output_17_0.png)
    



```python
sns.barplot(x = 'sex', y = 'total_bill', data = tips, estimator = np.std)
plt.show()
```


    
![png](output_18_0.png)
    



```python
sns.countplot(x = 'sex', data = tips)
```




    <Axes: xlabel='sex', ylabel='count'>




    
![png](output_19_1.png)
    



```python
sns.boxplot(x = 'day', y = 'total_bill', data = tips)
plt.show()
```


    
![png](output_20_0.png)
    



```python
sns.boxplot(x = 'day', y = 'total_bill', data = tips, hue = 'smoker')
plt.show()
```


    
![png](output_21_0.png)
    



```python
sns.violinplot(x = 'day', y = 'total_bill', data = tips)
plt.show()
```


    
![png](output_22_0.png)
    



```python
sns.violinplot(x = 'day', y = 'total_bill', data = tips, hue = 'sex')
plt.show()
```


    
![png](output_23_0.png)
    



```python
sns.violinplot(x='day', y='total_bill', data =tips, hue='sex', split=True)
plt.show()
```


    
![png](output_24_0.png)
    



```python
sns.stripplot(x='day', y='total_bill', data=tips)
plt.show()
```


    
![png](output_25_0.png)
    



```python
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)
plt.show()
```


    
![png](output_26_0.png)
    



```python
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex')
plt.show()
```


    
![png](output_27_0.png)
    



```python
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex')
plt.show()
```


    
![png](output_28_0.png)
    



```python
sns.swarmplot(x='day', y='total_bill', data=tips, color='purple')
plt.show()
```


    
![png](output_29_0.png)
    



```python
sns.catplot(x='day', y='total_bill', data=tips)
plt.show()
```


    
![png](output_30_0.png)
    


# Matrix plots


```python
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
flights.head()
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
      <th>year</th>
      <th>month</th>
      <th>passengers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1949</td>
      <td>Jan</td>
      <td>112</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1949</td>
      <td>Feb</td>
      <td>118</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1949</td>
      <td>Mar</td>
      <td>132</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1949</td>
      <td>Apr</td>
      <td>129</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1949</td>
      <td>May</td>
      <td>121</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips_corr = tips.corr(numeric_only=[True,False])
```


```python
tips_corr
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
      <th>total_bill</th>
      <th>tip</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>total_bill</th>
      <td>1.000000</td>
      <td>0.675734</td>
      <td>0.598315</td>
    </tr>
    <tr>
      <th>tip</th>
      <td>0.675734</td>
      <td>1.000000</td>
      <td>0.489299</td>
    </tr>
    <tr>
      <th>size</th>
      <td>0.598315</td>
      <td>0.489299</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.heatmap(tips_corr)
plt.show()
```


    
![png](output_36_0.png)
    



```python
sns.heatmap(tips_corr, annot=True)
plt.show()
```


    
![png](output_37_0.png)
    



```python
sns.heatmap(tips_corr, annot=True, cmap='coolwarm')
plt.show()
```


    
![png](output_38_0.png)
    



```python
flights
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
      <th>year</th>
      <th>month</th>
      <th>passengers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1949</td>
      <td>Jan</td>
      <td>112</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1949</td>
      <td>Feb</td>
      <td>118</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1949</td>
      <td>Mar</td>
      <td>132</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1949</td>
      <td>Apr</td>
      <td>129</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1949</td>
      <td>May</td>
      <td>121</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>139</th>
      <td>1960</td>
      <td>Aug</td>
      <td>606</td>
    </tr>
    <tr>
      <th>140</th>
      <td>1960</td>
      <td>Sep</td>
      <td>508</td>
    </tr>
    <tr>
      <th>141</th>
      <td>1960</td>
      <td>Oct</td>
      <td>461</td>
    </tr>
    <tr>
      <th>142</th>
      <td>1960</td>
      <td>Nov</td>
      <td>390</td>
    </tr>
    <tr>
      <th>143</th>
      <td>1960</td>
      <td>Dec</td>
      <td>432</td>
    </tr>
  </tbody>
</table>
<p>144 rows × 3 columns</p>
</div>




```python
flights.pivot_table(index='month', columns='year', values='passengers')
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
      <th>year</th>
      <th>1949</th>
      <th>1950</th>
      <th>1951</th>
      <th>1952</th>
      <th>1953</th>
      <th>1954</th>
      <th>1955</th>
      <th>1956</th>
      <th>1957</th>
      <th>1958</th>
      <th>1959</th>
      <th>1960</th>
    </tr>
    <tr>
      <th>month</th>
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
      <th>Jan</th>
      <td>112</td>
      <td>115</td>
      <td>145</td>
      <td>171</td>
      <td>196</td>
      <td>204</td>
      <td>242</td>
      <td>284</td>
      <td>315</td>
      <td>340</td>
      <td>360</td>
      <td>417</td>
    </tr>
    <tr>
      <th>Feb</th>
      <td>118</td>
      <td>126</td>
      <td>150</td>
      <td>180</td>
      <td>196</td>
      <td>188</td>
      <td>233</td>
      <td>277</td>
      <td>301</td>
      <td>318</td>
      <td>342</td>
      <td>391</td>
    </tr>
    <tr>
      <th>Mar</th>
      <td>132</td>
      <td>141</td>
      <td>178</td>
      <td>193</td>
      <td>236</td>
      <td>235</td>
      <td>267</td>
      <td>317</td>
      <td>356</td>
      <td>362</td>
      <td>406</td>
      <td>419</td>
    </tr>
    <tr>
      <th>Apr</th>
      <td>129</td>
      <td>135</td>
      <td>163</td>
      <td>181</td>
      <td>235</td>
      <td>227</td>
      <td>269</td>
      <td>313</td>
      <td>348</td>
      <td>348</td>
      <td>396</td>
      <td>461</td>
    </tr>
    <tr>
      <th>May</th>
      <td>121</td>
      <td>125</td>
      <td>172</td>
      <td>183</td>
      <td>229</td>
      <td>234</td>
      <td>270</td>
      <td>318</td>
      <td>355</td>
      <td>363</td>
      <td>420</td>
      <td>472</td>
    </tr>
    <tr>
      <th>Jun</th>
      <td>135</td>
      <td>149</td>
      <td>178</td>
      <td>218</td>
      <td>243</td>
      <td>264</td>
      <td>315</td>
      <td>374</td>
      <td>422</td>
      <td>435</td>
      <td>472</td>
      <td>535</td>
    </tr>
    <tr>
      <th>Jul</th>
      <td>148</td>
      <td>170</td>
      <td>199</td>
      <td>230</td>
      <td>264</td>
      <td>302</td>
      <td>364</td>
      <td>413</td>
      <td>465</td>
      <td>491</td>
      <td>548</td>
      <td>622</td>
    </tr>
    <tr>
      <th>Aug</th>
      <td>148</td>
      <td>170</td>
      <td>199</td>
      <td>242</td>
      <td>272</td>
      <td>293</td>
      <td>347</td>
      <td>405</td>
      <td>467</td>
      <td>505</td>
      <td>559</td>
      <td>606</td>
    </tr>
    <tr>
      <th>Sep</th>
      <td>136</td>
      <td>158</td>
      <td>184</td>
      <td>209</td>
      <td>237</td>
      <td>259</td>
      <td>312</td>
      <td>355</td>
      <td>404</td>
      <td>404</td>
      <td>463</td>
      <td>508</td>
    </tr>
    <tr>
      <th>Oct</th>
      <td>119</td>
      <td>133</td>
      <td>162</td>
      <td>191</td>
      <td>211</td>
      <td>229</td>
      <td>274</td>
      <td>306</td>
      <td>347</td>
      <td>359</td>
      <td>407</td>
      <td>461</td>
    </tr>
    <tr>
      <th>Nov</th>
      <td>104</td>
      <td>114</td>
      <td>146</td>
      <td>172</td>
      <td>180</td>
      <td>203</td>
      <td>237</td>
      <td>271</td>
      <td>305</td>
      <td>310</td>
      <td>362</td>
      <td>390</td>
    </tr>
    <tr>
      <th>Dec</th>
      <td>118</td>
      <td>140</td>
      <td>166</td>
      <td>194</td>
      <td>201</td>
      <td>229</td>
      <td>278</td>
      <td>306</td>
      <td>336</td>
      <td>337</td>
      <td>405</td>
      <td>432</td>
    </tr>
  </tbody>
</table>
</div>




```python
flight_pivot = flights.pivot_table(index='month', columns='year', values='passengers')
```


```python
sns.heatmap(flight_pivot)
plt.show()
```


    
![png](output_42_0.png)
    



```python
sns.heatmap(flight_pivot, cmap='magma')
plt.show()
```


    
![png](output_43_0.png)
    



```python
sns.heatmap(flight_pivot, cmap='magma', linecolor='white', linewidths=3)
plt.show()
```


    
![png](output_44_0.png)
    



```python
sns.clustermap(flight_pivot)
plt.show()
```


    
![png](output_45_0.png)
    



```python
sns.clustermap(flight_pivot, cmap='coolwarm')
plt.show()
```


    
![png](output_46_0.png)
    



```python
sns.clustermap(flight_pivot, cmap='coolwarm', standard_scale=1)
plt.show()
```


    
![png](output_47_0.png)
    


# Grids


```python
import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset('iris')
iris.head()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(iris.species.unique())
```

    ['setosa' 'versicolor' 'virginica']
    


```python
sns.PairGrid(iris)
plt.show()
```


    
![png](output_51_0.png)
    



```python
mapping = sns.PairGrid(iris)
mapping.map(plt.scatter)
plt.show()
```


    
![png](output_52_0.png)
    



```python
mapping = sns.PairGrid(iris)
mapping.map_diag(sns.violinplot)
mapping.map_upper(sns.kdeplot)
mapping.map_lower(plt.scatter)
plt.show()
```


    
![png](output_53_0.png)
    



```python
tips = sns.load_dataset('tips')
tips
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
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
    </tr>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>240</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>241</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>242</th>
      <td>17.82</td>
      <td>1.75</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>243</th>
      <td>18.78</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 7 columns</p>
</div>



mapping = sns.FacetGrid(data=tips, col='time', row='smoker')


```python
mapping = sns.FacetGrid(data=tips, col='time', row='smoker')
mapping.map(sns.histplot,'total_bill')
plt.show()
```


    
![png](output_56_0.png)
    


# Regression plots


```python
import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.lmplot(x='total_bill', y='tip', data=tips)
plt.show()
```


    
![png](output_59_0.png)
    



```python
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex')
plt.show()
```


    
![png](output_60_0.png)
    



```python
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='magma')
plt.show()
```


    
![png](output_61_0.png)
    



```python
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='magma', markers=['s', 'v'])
plt.show()
```


    
![png](output_62_0.png)
    



```python
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='magma', markers=['s', 'v'], scatter_kws={'s':70})
plt.show()
```


    
![png](output_63_0.png)
    



```python
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex')
plt.show()
```


    
![png](output_64_0.png)
    



```python
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time')
plt.show()
```


    
![png](output_65_0.png)
    



```python
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', row='time', hue='sex')
plt.show()
```


    
![png](output_66_0.png)
    



```python
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', aspect=0.6)
plt.show()
```


    
![png](output_67_0.png)
    



```python
sns.set_context('poster')
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', aspect=0.6)
plt.show()
```


    
![png](output_68_0.png)
    


# Style and Color


```python
sns.set_style('dark')
sns.countplot(x='sex', data=tips)
plt.show()
```


    
![png](output_70_0.png)
    



```python
sns.set_style('darkgrid')
sns.countplot(x='sex', data=tips)
plt.show()
```


    
![png](output_71_0.png)
    



```python
sns.set_style('white')
sns.countplot(x='sex', data=tips)
plt.show()
```


    
![png](output_72_0.png)
    



```python
sns.set_style('whitegrid')
sns.countplot(x='sex', data=tips)
plt.show()
```


    
![png](output_73_0.png)
    



```python
sns.set_style('ticks')
sns.countplot(x='sex', data=tips)
plt.show()
```


    
![png](output_74_0.png)
    



```python
sns.set_style('ticks')
sns.countplot(x='sex', data=tips)
sns.despine()
```


    
![png](output_75_0.png)
    



```python
sns.set_style('ticks')
sns.countplot(x='sex', data=tips)
sns.despine(left=True, bottom=True)
```


    
![png](output_76_0.png)
    



```python
plt.figure(figsize=(12,3))
sns.countplot(x='sex', data=tips)
plt.show()
```


    
![png](output_77_0.png)
    



```python
sns.set_context('talk')
plt.figure(figsize=(12,3))
sns.countplot(x='sex', data=tips)
plt.show()
```


    
![png](output_78_0.png)
    



```python
sns.set_context('talk',font_scale=2)
plt.figure(figsize=(12,3))
sns.countplot(x='sex', data=tips)
plt.show()
```


    
![png](output_79_0.png)
    



```python
sns.set_context('notebook')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='hot')
plt.show()
```


    
![png](output_80_0.png)
    



```python
sns.set_context('notebook')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='plasma')
plt.show()
```


    
![png](output_81_0.png)
    



```python
# Matplotlib colormap link - https://matplotlib.org/stable/tutorials/colors/colormaps.html
```


```python

```
