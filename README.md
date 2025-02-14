# contfunc: A Library for Continued-Function Expansions

Every positive real number can be expressed in a continued-function expansion as long 
as the function has certain properties.
Those properties are outlined in [Rényi (1957)](https://link.springer.com/article/10.1007/BF02020331), 
which treats a number of such continued-function expansions for a real number $r$ of the form

$r = b_{0} + f(b_{1} + f(b_{2} + f(b_{3} + f(\dots))))$,

where $B = \{b_{0}; b_{1}, b_{2}, b_{3}, \dots\}$ is the list of digits of the expansion.

Some well-known continued-function expansions are:

- The continued fraction expansion,

$r = b_{0} + \frac{1}{b_{1} + \frac{1}{b_{2} + \frac{1}{b_{3} + \dots}}}$

- The Bolyai expansion,

$r = b_{0} - 1 + \sqrt[m]{b_{1} + \sqrt[m]{b_{2} + }\sqrt[m]{b_{3} + \dots}}$

- The Engel expansion,

$r = \frac{1}{b_{0}} + \frac{1}{b_{0} b_{1}} + \frac{1}{b_{0} b_{1} b_{2}} + \frac{1}{b_{0} b_{1} b_{2} b_{3}} + \dots$

- And its close relative the Pierce expansion.

$r = \frac{1}{b_{0}} - \frac{1}{b_{0} b_{1}} + \frac{1}{b_{0} b_{1} b_{2}} - \frac{1}{b_{0} b_{1} b_{2} b_{3}} + \dots$

This library aims to learn about other continued-function expansions of the real numbers, 
in particular those of fundamental constants like Euler's number $e$, the circle constant 
$\pi$, and the Euler-Mascheroni constant $\gamma_{E}$.
In order for that learning to take place, these and other numbers must known and treated 
with tremendous precision, beyond the ordinary machine precision of Python. 
This has required the use of the `mpmath` library, which was facilitated high-precision 
calculation with admirable simplicity.

Current functionality includes the continued function expansions in

- $f(x) = \mathrm{tanh}(x)$ in `tanh_expansion.ipynb`
- $f(x) = \exp(-x)$ in `expneg_expansion.ipynb`

and highly precise constants (available in `fccf/constants.py`)

- $e$
- $\pi$