# checkvalues package

## Setup
The package can be installed either from GitHub:


```python
!pip install git+https://github.com/rcabanasdepaz/checkvalues.git#egg=checkvalues
```

or from PyPI:


```python
!pip install checkvalues
```

## Exercise and solution set

Consider the following exercises:

- **Exercise 1**: Define a variable `x` with the integer value 2.
- **Exercise 2**: Define a variable `y` with the float value 3.0.
- **Exercise 3**: Define a variable `z` with the result of 2+2.
- **Exercise 4**: Define a variable `L` with a list containing the values `"1", 2, 3.0`.
- **Exercise 5**: Define a function `func1` taking two input arguments `a` and `b` and returning the result of the operation $10\cdot a + b$.



We will consider the following csv file with the correct solutions.


```python
import pandas as pd
pd.read_csv("https://raw.githubusercontent.com/rcabanasdepaz/checkvalues/main/examples/solution_example.csv")
```





  <div id="df-1c3f63f2-1853-4895-906a-8edfd2185ff2" class="colab-df-container">
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
      <th>label</th>
      <th>type</th>
      <th>name</th>
      <th>args</th>
      <th>kwargs</th>
      <th>encrypted</th>
      <th>expected</th>
      <th>points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Exercise 1</td>
      <td>var</td>
      <td>x</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>c81e728d9d4c2f636f067f89cc14862c</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Exercise 2</td>
      <td>var</td>
      <td>y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>55c82b601deae028c1c5e87fd820923d</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Exercise 3</td>
      <td>var</td>
      <td>z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>a87ff679a2f3e71d9181a67b7542122c</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Exercise 4</td>
      <td>var</td>
      <td>L</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>3730122527a164abdec1a5acb762af67</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Exercise 5</td>
      <td>func</td>
      <td>func1</td>
      <td>int:2;float:3</td>
      <td>NaN</td>
      <td>True</td>
      <td>6bc071ec71e51c704acd13cdc898fd93</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Exercise 5</td>
      <td>func</td>
      <td>func1</td>
      <td>NaN</td>
      <td>b=int:2;a=int:3</td>
      <td>True</td>
      <td>6364d3f0f495b6ab9dcf8d3b5c6e0b01</td>
      <td>0.5</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-1c3f63f2-1853-4895-906a-8edfd2185ff2')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-1c3f63f2-1853-4895-906a-8edfd2185ff2 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-1c3f63f2-1853-4895-906a-8edfd2185ff2');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


<div id="df-bbfc163c-d809-4fee-8f3d-6e48de6813b6">
  <button class="colab-df-quickchart" onclick="quickchart('df-bbfc163c-d809-4fee-8f3d-6e48de6813b6')"
            title="Suggest charts."
            style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
  </button>

<style>
  .colab-df-quickchart {
    background-color: #E8F0FE;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: #1967D2;
    height: 32px;
    padding: 0 0 0 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: #E2EBFA;
    box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: #174EA6;
  }

  [theme=dark] .colab-df-quickchart {
    background-color: #3B4455;
    fill: #D2E3FC;
  }

  [theme=dark] .colab-df-quickchart:hover {
    background-color: #434B5C;
    box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
    filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
    fill: #FFFFFF;
  }
</style>

  <script>
    async function quickchart(key) {
      const charts = await google.colab.kernel.invokeFunction(
          'suggestCharts', [key], {});
    }
    (() => {
      let quickchartButtonEl =
        document.querySelector('#df-bbfc163c-d809-4fee-8f3d-6e48de6813b6 button');
      quickchartButtonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';
    })();
  </script>
</div>
    </div>
  </div>




## Usage

Import the function `check_solution`.


```python
from checkvalues.checker import check_solution
```

This function takes as input the address with the solution file. If invoked without havind solved the exercises, error messages will be shown.


```python
# Run the checker without having defined the variables and functions
check_solution("https://raw.githubusercontent.com/rcabanasdepaz/checkvalues/main/examples/solution_example.csv")

```

    Exercise 1. ERROR: x is not defined.
    Exercise 2. ERROR: y is not defined.
    Exercise 3. ERROR: z is not defined.
    Exercise 4. ERROR: L is not defined.
    Exercise 5. ERROR: func1 is not defined.
    Exercise 5. ERROR: func1 is not defined.
    Total points: 0/5.0


The correct code is shown below.


```python

# Correct code
def func1(a,b):
    return 10*a+b
x = 2
y = 3.0
z = 2+2
L = ["1", 2, 3.0]


```

Check that the results are correct.


```python

check_solution("https://raw.githubusercontent.com/rcabanasdepaz/checkvalues/main/examples/solution_example.csv")

```

    Exercise 1. correct (1.0 points)
    Exercise 2. correct (1.0 points)
    Exercise 3. correct (1.0 points)
    Exercise 4. correct (1.0 points)
    Exercise 5. correct (0.5 points)
    Exercise 5. correct (0.5 points)
    Total points: 5.0/5.0


A single exercise can be checked.


```python
check_solution("https://raw.githubusercontent.com/rcabanasdepaz/checkvalues/main/examples/solution_example.csv", label="Exercise 5")

```

    Exercise 5. correct (0.5 points)
    Exercise 5. correct (0.5 points)
    Total points: 1.0/1.0


We can also use the functionality with a wrong code.


```python
# Wrong code
def func1(a,b):
    return 100*a+b
x = 2.0
y = 3
z = 5
L = ["1", 2, 3.0, 3]

```


```python
check_solution("https://raw.githubusercontent.com/rcabanasdepaz/checkvalues/main/examples/solution_example.csv")
```

    Exercise 1. ERROR: x is a variable with a wrong value.
    Exercise 2. ERROR: y is a variable with a wrong value.
    Exercise 3. ERROR: z is a variable with a wrong value.
    Exercise 4. ERROR: L is a variable with a wrong value.
    Exercise 5. ERROR: function func1 return a wrong value for inputs args=[2, 3.0], kwargs={}.
    Exercise 5. ERROR: function func1 return a wrong value for inputs args=[], kwargs={'b': 2, 'a': 3}.
    Total points: 0/5.0

