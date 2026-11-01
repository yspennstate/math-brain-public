# R2 verification: bounded-density real/complex lower side

## Statement checked

For `F in {R,C}`, `d_F = dim_R F`, and an `m x m` matrix `G` with independent
entries whose `d_F`-dimensional Lebesgue densities are bounded by `K`,

```tex
P{s_min(G) <= t} <= C_{F,K} m^{d_F+1} t^{d_F},   0 < t <= 1.
```

Consequently, for `N_m/m -> gamma > 1`,

```tex
P{ min_{|T|=m} s_min(A_T) <= exp[-(h(gamma)/d_F + eps)m] } -> 0.
```

## Proof audit

The negative second-moment identity gives

```tex
sum_k sigma_k(G)^{-2} = sum_i dist(R_i, span{R_j:j != i})^{-2}.
```

Thus `s_min(G) <= t` implies some row distance is at most `sqrt(m)t`.
After conditioning on all other rows and all but one coordinate of the selected
row, the distance is `|u_j xi_j + c|` for a coordinate with
`|u_j| >= m^{-1/2}`.  The affine image has density at most
`K |u_j|^{-d_F} <= K m^{d_F/2}` on `F ~= R^{d_F}`.  The ball of radius
`sqrt(m)t` has volume `O_F(m^{d_F/2}t^{d_F})`.  Multiplying and unioning over
`m` rows gives the displayed polynomial tail.

The row-submatrix lower bound is then the union bound over
`binom(N_m,m)=exp((h(gamma)+o(1))m)` at
`t=exp[-(h(gamma)/d_F+eps)m]`.  Polynomial factors are `exp(o(m))`.

## Limitations

This proves only the lower side of the extremal law.  The matching upper side
still needs pair-correlation control and is not implied by the one-matrix tail.
