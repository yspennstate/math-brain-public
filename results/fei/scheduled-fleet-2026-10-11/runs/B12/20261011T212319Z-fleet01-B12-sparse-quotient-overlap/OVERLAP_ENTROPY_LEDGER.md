# Coefficient and payment ledger

For `K(x,z)=1-2 1_{x=-1}1_{Lz in B}`, set `p=|B|/2^r`,
`a_alpha=E[1_{Lz in B} chi_{L^T alpha}(z)]`, and
`q=2p-p^2`.

| Sector | Fourier coefficient | Total mass | Influence contribution |
|---|---:|---:|---:|
| empty | `1-p` | `(1-p)^2` | `0` |
| selector only | `p` | `p^2` | `p^2` |
| data, `alpha != 0` | `-a_alpha` | `sum a_alpha^2=p-p^2` | `sum |L^T alpha| a_alpha^2` |
| selector + data | `a_alpha` | `sum a_alpha^2=p-p^2` | `sum (1+|L^T alpha|) a_alpha^2` |

Therefore the nonconstant mass is exactly `q`, selector influence
is exactly `p`, and

`I(K)=p+2 sum_{alpha!=0}|L^T alpha|a_alpha^2=p+I(D_A)/2`.

The full collision/entropy payment is

`H(K) <= h2(q)+q log2(2^(r+1)-1) < h2(q)+q(r+1)`.

For `p<=1/4`, the binary term is at most `4p log2(1/p)` and the
support term at most `2p(r+1)`.  The physical edge boundary pays

`I(K) >= p[1+log2(1/p)]`.

Thus `log2(1/p)>=r/2` gives `H(K)<8I(K)`.  The logarithmic rare-event
cost is paid by the data boundary, not by the vanishing selector
influence.  Arbitrary overlap among the rows of `L` is retained in
the exact Hamming weights `|L^T alpha|`.

Two quotient cells do not extend the previous affine result: every
two-point subset of `F_2^r` is an affine line, whose preimage is one
affine coset of codimension `r-1`.  Three cells (for example when
`r>=4`) are the first genuinely non-affine case covered here.

Guard checks:

- The branches have inner product `1-2p`, so the neighboring-
  orthogonality theorem does not apply when `p != 1/2`.
- Selector influence is `p` and tends to zero; no uniform positive-
  energy hypothesis applies.
- Bent splice is not contradicted: selector-only payment still
  fails in general; this class uses the full physical boundary of
  `A`.
- Shared-variable product subadditivity is not used.  The optional
  leaf corollary uses only honest disjoint tensorization.
- Whole-set addressing and arbitrary rare defects are not claimed:
  the structural condition is the explicit quotient-support bound
  `log2(1/p)>=r/2`.
