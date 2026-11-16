# Cosmic coin flipping with at most nine bits

Paper and programs for a computer-assisted proof that, for $n\le 9$ source bits and $2\le k\le 9$ parties, the
first-bit protocol is the best antisymmetric protocol in the cosmic coin flipping problem of Mossel and O'Donnell
(Open Problem 1 of *Coin flipping from a cosmic source: on error correction of truly random bits*, Random Structures
Algorithms 26 (2005)). The cases $k\le5$ follow from Witsenhausen, Mossel and O'Donnell, and Yu (PTRF 186 (2023)).

- `paper/` LaTeX source and PDF.
- `code/op1_float.py` enumerates the antisymmetric left-monotone functions on $n$ bits and certifies the coefficient
  inequalities in binary64 with the error bound of Section 3. Usage: `python op1_float.py n kmin kmax [out.json]`, for $n\ge3$ (the paper treats $n\le2$ directly).
  With Apple Accelerate, NumPy may print floating-point status warnings at the matrix products; the coefficient
  vectors $q$ are nonetheless exact, which was checked against integer arithmetic for $n\le7$.
- `code/op1_exact.py` repeats the comparison in exact rational arithmetic (SymPy) for $n\le8$.
- `code/num_check.py` evaluates the differences on a grid of $\epsilon$ in double precision.
- `results/` the output files: `f*.json` and `g*.json` from the floating-point certificate, `n*.json` from the exact check,
  `num*.log` from the grid check.

Python 3.13.2, NumPy 2.2.3, SymPy 1.13.1. The run for $n=9$, $2\le k\le9$ took about twenty minutes on a Mac mini.
