### Description

This script generates a set of orthonormal functions, called ![](https://latex.codecogs.com/gif.latex?%5Cphi_i%5E%7B%5Cperp%7D%28x%29), based on the set of non-orthonormal functions ![](https://latex.codecogs.com/gif.latex?%5Cphi_i%5E%28x%29)

![equation](https://latex.codecogs.com/gif.latex?%5Cphi_i%28x%29%20%3D%20x%5E%7B%5Cfrac%7B1%7D%7Bi&plus;1%7D%7D%2C%20%5Cquad%20i%20%3D%20i_0%2C%5Cdots%2C%20i_0&plus;n)

The orthonormalized functions ![](https://latex.codecogs.com/gif.latex?%5Cphi_i%5E%7B%5Cperp%7D%28x%29) are linear combination of the functions ![](https://latex.codecogs.com/gif.latex?%5Cphi_i%5E%28x%29), as

![equation](https://latex.codecogs.com/gif.latex?%5Cphi_j%5E%7B%5Cperp%7D%28x%29%20%3D%20%5Calpha_j%20%5Csum_%7Bi%3Di_0%7D%5E%7Bi_0&plus;n%7D%20a_%7Bji%7D%20%5Cphi_i%28x%29%2C%5Cqquad%20j%20%3D%20i_0%2C%5Cdots%2Ci_0&plus;n)

The functions ![](https://latex.codecogs.com/gif.latex?%5Cphi_i%5E%7B%5Cperp%7D%28x%29) are orthonormal in the interval ![](https://latex.codecogs.com/gif.latex?x%20%5Cin%20%5B0%2CL%5D) with respect to the weight function ![](https://latex.codecogs.com/gif.latex?w%28x%29%20%3D%20%5Cfrac%7B1%7D%7Bx%7D). That is
        
![equation](https://latex.codecogs.com/gif.latex?%5Cint_0%5EL%20%5Cphi_i%5E%7B%5Cperp%7D%28x%29%20%5Cphi_j%5E%7B%5Cperp%7D%28x%29%20%5Cfrac%7B1%7D%7Bx%7D%20%5Cmathrm%7Bd%7Dx%20%3D%20%5Cdelta_%7Bij%7D)

where ![](https://latex.codecogs.com/gif.latex?%5Cdelta_%7Bij%7D) is the Kronecker delta function. The orthogonal functions are generated by [Gram-Schmidt orthogonalization process](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process). This script produces the symbolic functions using [Sympy](https://www.sympy.org), a Python computer algebraic package.

#### Package Prerequisits

The Python packages that are required are `numpy`, `sympy`, and `matplotlib`. If you are using [anaconda](https://www.anaconda.com/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) python distirbutions in the linux environment, these Python packages can be installed by

    $ sudo conda install -c conda-forge numpy sympy matplotlib -y

#### Usage

	$ python GenerateOrthogonalFunctions.py [options]
Optional arguments:

| Option| Description |
| -- | ----- |
| `-h`, `--help`                  | Prints a help message. |
| `-v`, `--version`               | Prints version. |
| `-l`, `--license`               | Prints author info, citation and license. |
| `-n`, `--num-func[=int]`        | Number of orthogonal functions to generate. Positive integer. Default is 9. |
| `-s`, `--start-func[=int]`      | Starting function index. Non-negative integer. Default is 1. |
| `-e`, `--end-interval[=float]`  | End of the interval of functions domains. Real number greater than zero. Default is 1. |
| `-c`,`--check`                  | Checks orthogonality of generated functions. |
| `-p`, `--plot`                  | Plots generated functions, also saves the plot as pdf file in the current directory.|

The variables ![](https://latex.codecogs.com/gif.latex?i_0), ![](https://latex.codecogs.com/gif.latex?n), and ![](https://latex.codecogs.com/gif.latex?L) can be set in the script by the following arguments,

| Variable | Variable in script    |          Option            |
| --------    -------------------- |  ------------------------- |
| ![](https://latex.codecogs.com/gif.latex?i_0)        | `StartFunctionIndex`  | `-s`, or `--start-func` |
| ![](https://latex.codecogs.com/gif.latex?n)        | `NumFunctions`        | `-n`, or `--num-func`     |
| ![](https://latex.codecogs.com/gif.latex?)        | `EndInterval`         | `-e`, or `--end-interval`  |

#### Examples

1. Generate nine orthogonal functions from function index 1 to 9
       $ python GenerateOrthogonalFunctions.py

2. Generate seven orthogonal functions from function index 1 to 7
       $ python GenerateOrthogonalFunctions.py -n 7

3. Generate nine orthogonal functions from function index 0 to 8
       $ python GenerateOrthogonalFunctions.py -s 0

4. Generate nine set of orthogonal functions starting from function 1, that are orthonormal in the interval [0,10]
       $ python GenerateOrthogonalFunctions.py -e 10

4. Check orthogonality of each two function, and plot the orthonormal functions and save the plot to pdf
       $ python GenerateOrthogonalFunctions.py -c -p

5. A complete example:
       $ python GenerateOrthogonalFunctions.py -n 9 -s 1 -e 1 -c -p
       
#### Output

* Prints the orthogonal functions as computer algebraric symbolic functions. For instance

```
Function 1:
sqrt(x)

Function 2:
sqrt(6)*(5*x**(1/3) - 6*sqrt(x))/3

Function 3:
sqrt(2)*(21*x**(1/4) - 40*x**(1/3) + 20*sqrt(x))/2

Function 4:
sqrt(10)*(84*x**(1/5) - 210*x**(1/4) + 175*x**(1/3) - 50*sqrt(x))/5

Function 5:
sqrt(3)*(330*x**(1/6) - 1008*x**(1/5) + 1134*x**(1/4) - 560*x**(1/3) + 105*sqrt(x))/3

Function 6:
sqrt(14)*(1287*x**(1/7) - 4620*x**(1/6) + 6468*x**(1/5) - 4410*x**(1/4) + 1470*x**(1/3) - 196*sqrt(x))/7

Function 7:
5005*x**(1/8)/2 - 10296*x**(1/7) + 17160*x**(1/6) - 14784*x**(1/5) + 6930*x**(1/4) - 1680*x**(1/3) + 168*sqrt(x)

Function 8:
sqrt(2)*(19448*x**(1/9) - 90090*x**(1/8) + 173745*x**(1/7) - 180180*x**(1/6) + 108108*x**(1/5) - 37422*x**(1/4) + 6930*x**(1/3) - 540*sqrt(x))/3

Function 9:
sqrt(5)*(75582*x**(1/10) - 388960*x**(1/9) + 850850*x**(1/8) - 1029600*x**(1/7) + 750750*x**(1/6) - 336336*x**(1/5) + 90090*x**(1/4) - 13200*x**(1/3) + 825*sqrt(x))/5

```

* Prints a human readable coefficients, ![](https://latex.codecogs.com/gif.latex?%5Calpha_j) and ![](https://latex.codecogs.com/gif.latex?a_%7Bji%7D) of the functions. For instance,

```
j       alpha_j      a_[ji]
------  ----------   ---------
j = 1:  +sqrt(2/2)   [1]
j = 2:  -sqrt(2/3)   [6, -5]
j = 3:  +sqrt(2/4)   [20, -40, 21]
j = 4:  -sqrt(2/5)   [50, -175, 210, -84]
j = 5:  +sqrt(2/6)   [105, -560, 1134, -1008, 330]
j = 6:  -sqrt(2/7)   [196, -1470, 4410, -6468, 4620, -1287]
j = 7:  +sqrt(2/8)   [336, -3360, 13860, -29568, 34320, -20592, 5005]
j = 8:  -sqrt(2/9)   [540, -6930, 37422, -108108, 180180, -173745, 90090, -19448]
j = 9:  +sqrt(2/10)  [825, 75582, -13200, 90090, -336336, 750750, -1029600, 850850, -388960]

```
* Prints a matrix of mutual inner product of functions to check orthogonality (with option `-c`). For instance,

```
[[1 0 0 0 0 0 0 0 0]
 [0 1 0 0 0 0 0 0 0]
 [0 0 1 0 0 0 0 0 0]
 [0 0 0 1 0 0 0 0 0]
 [0 0 0 0 1 0 0 0 0]
 [0 0 0 0 0 1 0 0 0]
 [0 0 0 0 0 0 1 0 0]
 [0 0 0 0 0 0 0 1 0]
 [0 0 0 0 0 0 0 0 1]]

```

*Plots the set of functions and saves the plot as pdf in the current directory (with option `-p`). For instance

![](https://raw.github.com/ameli/orthogonalfunctions/master/OrthogonalFunctions.svg "Orthonormal functions")

#### Credits

__Author:__

   Siavash Ameli
   University of California, Berkeley

__Citation:__

   Ameli, S. and Shadden. S. C., _Maximum Likelihood Estimation of Variance and Nugget in General Linear Model_.

__License:__ [GNU General Public License v3.0](https://raw.github.com/ameli/orthogonalfunctions/master/LISENSE.txt)
