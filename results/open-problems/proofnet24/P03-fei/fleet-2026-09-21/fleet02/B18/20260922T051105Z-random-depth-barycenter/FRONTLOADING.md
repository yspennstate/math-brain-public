# Supplement — sharp front-loading of random-restriction Poincare currency

**Classification:** `PROVED SUPPORTING LEMMA`. Full FEI remains **OPEN / NOT PROVED**.

This strengthens the random-block contraction in the main report and is proved directly from its exact depth-currency formula.

Let

\[
P_r=\frac14\sum_{k\ge2}W_k\left[k\left(1-\frac rn\right)-1+\frac{(r)_k}{(n)_k}\right],
\qquad 0\le r\le n-1,
\]

and `Delta_r=P_r-P_{r+1}`.  The main report gives

\[
\Delta_r=
\frac1{4n}\sum_{k\ge2} kW_k
\left[1-\frac{(r)_{k-1}}{(n-1)_{k-1}}\right].
\tag{1}
\]

## Theorem — sharp currency front-loading

For every Boolean source and every `0<=r<=n-3`,

\[
\boxed{\Delta_r\ge\Delta_{r+1}.}
\tag{2}
\]

Consequently, for every `0<=m<=n-1`,

\[
\boxed{
Q_m:=P_0-P_m\ge\frac{m}{n-1}P_0,
}
\tag{3}
\]

or equivalently

\[
\boxed{
P_m\le\frac{n-1-m}{n-1}P_0.
}
\tag{4}
\]

For `1<=m<=n-2`, equality in (3) for a positive-currency spectral profile can occur only if all its positive higher-order mass is on level `k=n`; pure top level attains equality.  Thus the constant `m/(n-1)` is sharp at the level-profile relaxation.

### Proof

For fixed `k>=2`, the falling factorial `(r)_{k-1}` is nondecreasing in `r`.  Therefore every summand in (1) is nonincreasing in `r`; summing with nonnegative weights `kW_k` proves (2).

There are exactly `n-1` increments `Delta_0,...,Delta_{n-2}`, they are nonnegative and nonincreasing, and they sum to `P_0` because `P_{n-1}=0`.  Hence the first `m` increments have average at least the average of all `n-1` increments:

\[
Q_m=\sum_{r=0}^{m-1}\Delta_r
\ge \frac{m}{n-1}\sum_{r=0}^{n-2}\Delta_r
=\frac{m}{n-1}P_0.
\]

This proves (3)--(4).

For strictness, fix `1<=m<=n-2`.  The level-`k` normalized increment profile is

\[
w_r^{(k)}=
\frac{k}{n(k-1)}
\left[1-\frac{(r)_{k-1}}{(n-1)_{k-1}}\right].
\]

For `k<n` this profile is not constant on `0,...,n-2`, hence its first `m` partial sum is strictly larger than `m/(n-1)`.  For `k=n`, `(r)_{n-1}=0` throughout this range and `w_r^{(n)}=1/(n-1)` exactly.  A nonnegative mixture can attain equality only if every active higher level has the constant profile, i.e. only `k=n` is active. `QED`

## Why this matters to the live signed target

The previous B18 contraction `P_m<=(1-m/n)P_0` was valid but not sharp.  The new bound shows that fixed-size random restrictions consume at least the uniform fraction `m/(n-1)` of all quadratic-lift currency, and generally more unless the higher spectrum is concentrated entirely at top degree.

In the signed depth notation of the main report,

\[
\sum_{r=0}^{m-1}w_r=\frac{Q_m}{P_0}\ge\frac{m}{n-1}.
\]

Thus any amortized proof that stops after a positive fraction of the physical coordinates has a guaranteed positive fraction of the full `a_*P_0` bank available.  This does **not** itself bound the signed base deficit or prove FEI; it is a quantitative input for the required two-generation/adaptive-depth compensation step.
