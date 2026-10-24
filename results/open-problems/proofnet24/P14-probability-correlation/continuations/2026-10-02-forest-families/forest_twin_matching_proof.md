# Exact forest Rayleigh formula for two matching edges across four twins

Let `G_s` have four vertices `0,1,2,3`, independent hub vertices `h_1,...,h_s`,
all edges `i h_j`, and marked edges `e=01`, `f=23`. All four edges at hub `h_j`
have common weight `x_j >= 0`; the two marked weights may be arbitrary.
Write `a_j=1+4x_j`. The forest polynomial is

\[
 Z=A+z_eB+z_fB+z_ez_fD.
\]

Consequently the Rayleigh difference is `R_ef=B^2-AD`, independent of marked weights.

**Theorem.** For every `s >= 0`,

\[
\begin{aligned}
R_{ef}={}&\sum_{i<j}4x_i^2x_j^2(1+x_i+x_j)^2
  \prod_{k\notin\{i,j\}}a_k^2\\
 &+\sum_{i<j<k}8x_i^2x_j^2x_k^2
 (a_i a_j+a_i a_k+a_j a_k)
 \prod_{\ell\notin\{i,j,k\}}a_\ell^2.
\end{aligned}
\]

Empty sums are zero. Every coefficient in the variables `x_j` is nonnegative.
If at least two hub weights are positive then the Rayleigh difference is strictly
positive; the marked edge indicators are therefore strictly negatively correlated
whenever their two weights are positive.

For common hub weight `x>0` and `s>=2`, the formula reduces to

\[
 R_{ef}=2s(s-1)x^4(1+4x)^{2s-4}(1+4x+2sx^2).
\]

## Proof

Track the partition induced by connectivity on the four original vertices as hubs
are added. A new hub may be joined to any subset of original vertices that lie in
distinct current components. Otherwise a cycle is formed. The empty subset gives
an isolated hub. Subsets of size one preserve the terminal partition and contribute
total weight `4x_j`; together with the empty subset this gives the diagonal factor
`a_j` in every partition state.

Only the five partition shapes `1111,211,22,31,4` matter for the unmarked generating
functions. The non-diagonal transitions, listed with multiplicity and weight, are:

| Initial shape | Final shape | Weight |
|---|---|---|
| `1111` | `211` | `6x_j^2` |
| `1111` | `31` | `4x_j^3` |
| `1111` | `4` | `x_j^4` |
| `211` | `31` | `4x_j^2` |
| `211` | `22` | `x_j^2` |
| `211` | `4` | `2x_j^3` |
| `22` | `4` | `4x_j^2` |
| `31` | `4` | `3x_j^2` |

The transfer matrix has the form `a_j I + x_j^2 N_2 + x_j^3 N_3 + x_j^4 N_4`.
The three constant nilpotent matrices commute, and products of four non-diagonal
matrices vanish. Initial shapes for `A,B,D` are respectively `1111,211,22`.
The partition shapes account for edges `e,f` already present, with their weights
removed, so the transfer calculation gives exactly the coefficients of `Z` above.

Put

\[
 t_j=\frac{x_j^2}{a_j},\quad u_j=x_jt_j,\quad v_j=x_j^2t_j,
 \quad T=\sum_jt_j,\quad U=\sum_ju_j,\quad V=\sum_jv_j,
 \quad P=\prod_ja_j,
\]

and let `E_r(t)` be the elementary symmetric polynomial of degree `r` in the `t_j`.
Enumerating at most three non-diagonal transitions gives

\[
\begin{aligned}
 A/P&=1+6T+4U+V+30E_2(t)+12\sum_{i\ne j}t_i u_j+96E_3(t),\\
 B/P&=1+5T+2U+16E_2(t),\\
 D/P&=1+4T.
\end{aligned}
\]

For example the coefficient `30` comes from two successive size-two merges:
`6*(4+1)`. The mixed size-two/size-three coefficient is `12` in either order:
`6*2=4*3`. Three size-two merges contribute `6*(4*3+1*4)=96`.

Expand `(B/P)^2-(A/P)(D/P)` and group terms by their support in hub indices.
Terms on a single hub cancel, using

\[
 t_j^2+4t_ju_j+4u_j^2-v_j-4t_jv_j=0.
\]

The terms with exactly two distinct hub indices `i,j` simplify to

\[
 \frac{4t_it_j(1+x_i+x_j)^2}{a_i a_j}.
\]

The terms with exactly three distinct hub indices simplify to

\[
 t_it_jt_k\left(24-32(x_i+x_j+x_k)+128(t_i+t_j+t_k)\right)
 =8t_it_jt_k\left(\frac1{a_i}+\frac1{a_j}+\frac1{a_k}\right).
\]

The identity uses `128t_i-32x_i=-32x_i/a_i` and `4x_i/a_i=1-1/a_i`.
For four distinct indices, the `256 E_2(t)^2` contribution is `1536 t_it_jt_kt_l`,
and the `-384 T E_3(t)` contribution is its negative. Higher support is impossible.
Multiplying by `P^2` proves the stated formula.

## Relation to the high-fugacity equality case

For `s>=3`, `G_s` is 3-connected, since it contains the spanning 3-connected
complete bipartite graph `K_{4,s}`. Thus there is no two-vertex separator.
With unit conductances and the marked edges present, the current potential of `e`
is `+/-1/(s+2)` at its endpoints and zero elsewhere; the same holds for `f` on its
disjoint endpoint pair. Therefore both leading coefficients `H_0,H_1` in the
September 30, 2026 paper's expansion vanish. The exact formula gives

\[
 H_2=4^{2s-3}s^2(s-1)>0.
\]

This proves a family of exceptional cases; it does not prove high-fugacity negative
correlation on every graph and does not solve the general Kahn conjecture.

## Other independently derived result

The companion script `forest_k4s_symbolic.py` computes all three actual edge-pair
types of `K_{4,s}` in an exact rational polynomial ring from all 15 terminal
partitions. With `a=1+4x`, it finds `R_type=a^(2s-8) P_type(s,x)`.
For pairs sharing the four-vertex-side endpoint, and for disjoint pairs, every
coefficient of `P_type` in `s,x` is nonnegative. For pairs sharing a hub, every
coefficient after substituting `s=1+t` is nonnegative. Hence all actual edge-pair
types are negatively correlated for every `s` and common fugacity `x>0`.
The graph `K_{4,1}` is a tree and all its forest edge indicators are independent.
This last result is being independently audited by the parent agent.

Novelty has not been fully certified. The primary literature search to date did
not locate this exact `K_{4,s}` all-fugacity theorem or the heterogeneous marked-pair
formula, but absence from a search does not establish novelty.
