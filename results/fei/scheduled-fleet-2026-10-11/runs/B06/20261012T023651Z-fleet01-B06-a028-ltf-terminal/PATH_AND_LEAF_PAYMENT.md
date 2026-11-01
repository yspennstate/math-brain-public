# Path and leaf payment

At level `ell`, let `P_ell` be the squared Fourier mass of `f_{ell-1}` on
odd-cardinality sets.  The complete physical tree querying the fresh blocks
from newest to oldest has

```
expected path entropy = sum_ell P_ell H(q_{m_ell}),
expected terminal entropy = H(f_0),
root entropy = terminal + path,
```

and, with the same decomposition,

```
queried influence = sum_ell P_ell I(q_{m_ell}),
terminal influence = I(f_0),
root influence = terminal + queried.
```

Each block is fresh and is queried once.  The path and terminal pieces are
therefore paid from one partition of the root influence, not from duplicated
credits.  Since `H(q_m)<4 I(q_m)` and every leaf is an actual LTF with the
same spectrum as `f_0`,

```
H(f_L) <= max(4,C_LTF) I(f_L) = C_LTF I(f_L),
C_LTF = log2(4+e)+2 log2(e*pi) < 8.937.
```

The tree passes the long character-coded plateau control if `q_m` is replaced
by a character (zero added entropy).  It also pays the rare logarithm of the
point defect explicitly.  It does not apply to a bent splice, reused block,
or branches with unequal squared spectra.  Those are the first unpaid cases.
