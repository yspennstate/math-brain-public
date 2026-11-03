# A prophet secretary instance with ratio below 0.7230

Yitzchak Shmalo

In the prophet secretary problem, independent nonnegative random variables with known distributions arrive in uniformly
random order, and a gambler who sees each value as it arrives may stop once and keep it. The best constant alpha such
that the gambler can always obtain alpha times the expected maximum lies between 0.688 (Chen, Huang, Li and Tang) and
0.7235 (Giambartolomei, Mallmann-Trenn and Saona).

This paper gives an explicit instance with 461 variables on which the optimal gambler obtains

    V / E max  in  [0.722933460012600477658647124, 0.722933460012600477658647127],

so alpha < 0.72294. The instance has 400 prizes worth 1 with probability 1e-9 each, 30 items worth 1.28233 x 4e-7 with
probability 0.2065/30 each, 30 items worth 1.38487 x 4e-7 with probability 0.17698/30 each, and one item worth
0.823 x 4e-7. Its optimal value is computed by the dynamic programme for random order, which depends only on how many
items of each kind are left (770,722 states), evaluated in interval arithmetic.

In the limit of many prizes the family is described by an ordinary differential equation. Its numerical solution gives
about 0.72274 with two medium values and 0.72268 with three; these values are not certified.

## Contents

- `paper/prophet_secretary_hardness.tex`, `paper/prophet_secretary_hardness.pdf` - the paper.
- `code/ps_check.py` - the dynamic programme. `python ps_check.py iv 400 30 100` produces the certificate of Theorem 1.1
  (interval arithmetic, about two and a half minutes); `brute k m` compares the count recursion with the recursion over
  all subsets; `float k m` runs it in double precision. Requires Python 3 and mpmath.
- `code/check_output.txt` - the output of the runs quoted in Section 3.
- `code/continuum.py`, `code/continuum_output.txt` - the numerical solutions of Section 4. Requires SciPy.

## License

The paper is released under CC BY 4.0 and the code under the MIT License.
