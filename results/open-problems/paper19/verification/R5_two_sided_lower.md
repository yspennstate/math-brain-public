# R5 verification: two-sided square-submatrix lower side

## Statement checked

For iid Gaussian `A_k in F^{N_k x n_k}` with
`N_k/k -> gamma_R > 1` and `n_k/k -> gamma_C > 1`, define

```tex
M_k^{two} = min_{|R|=|C|=k} s_min((A_k)_{R,C}).
```

Then, with `H = h(gamma_R)+h(gamma_C)`, for every `eps > 0`,

```tex
P{ M_k^{two} <= exp[-(H/d_F + eps)k] } -> 0.
```

## Audit

The entropy adds:

```tex
(1/k) log( binom(N_k,k) binom(n_k,k) )
  -> h(gamma_R)+h(gamma_C).
```

Each selected minor is a square `k x k` Gaussian matrix over `F`, so its
least-singular-value small-ball exponent is `d_F`.  The polynomial prefactor is
irrelevant at exponential scale.  The bounded-density tail in
`parts/universality.tex` gives a safe bound of the form

```tex
P{s_min(G) <= t} <= C_{F} k^{d_F+1} t^{d_F}.
```

Union at `t=exp[-(H/d_F+eps)k]` gives the theorem.

## Status split

The lower side is proved.  The exact two-sided base

```tex
(1/k) log M_k^{two} -> -[h(gamma_R)+h(gamma_C)]/d_F
```

is still conditional, because the upper side requires a second-moment estimate
over pairs of minors with two overlap parameters: row overlap and column
overlap.
