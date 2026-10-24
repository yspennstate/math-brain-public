# R11 idea-before-code: sparse translation CTCS compiler / candidate C073

Date: 2026-09-19 UTC.

Continue from U051/C072. Use the prescribed nonrepeating moves #8, #15, #27.

## #8 GO THE OTHER WAY AND DISCRETIZE

C072 averages over all `p` translations of a growing-degree power permutation. Replace that full orbit by the deterministic initial interval

`T_p={0,1,...,L_p-1}`,  `L_p=ceil(p^(3/4))=o(p)`.

To preserve the macroscopic hazard scale, multiply each surviving translation clock by `p/L_p`: use rate

`p / (2 L_p u(p-u))`

for threshold `u` and translation `t in T_p`.

The total proposal rate per active clade stays exactly `H_{p-1}` despite deleting a `1-o(1)` fraction of translations.

## #15 BREAK THE SYMMETRY ON PURPOSE

The full additive translation group was the main symmetry in C072. Destroy it completely by keeping only the one-sided initial interval. The finite models should become strongly anisotropic while fixed visible restrictions still see asymptotic equidistribution.

For fixed visible dimension `m`, once the growing degree `d>=m+1`, every nonzero Fourier phase

`P_h(t)=sum_j h_j (t+a_j)^d`

has degree at least 2. Indeed, if it had degree at most 1, the coefficients of powers `t^d,...,t^2` would force the first `m` Vandermonde moments `sum_j h_j a_j^r=0`, hence `h=0`.

Therefore for every linear completion twist `b t`, `P_h(t)+bt` remains nonconstant of degree at least 2. Completing an interval sum to the full field and applying Weil gives

`|sum_{t<L} e_p(P_h(t))| <= C d sqrt(p) log p`.

Erdos--Turan--Koksma then gives fixed-dimensional star discrepancy

`D_{p,L}^{(m)} <= C_m [1/p + d sqrt(p) (log p)^(m+1)/L]`.

With `d=O(log p)` and `L=ceil(p^(3/4))`, this is

`O_m(p^(-1/4) (log p)^(m+2)) -> 0`.

## #27 SWAP THE QUANTIFIERS

Do not ask for one sparse translation set that is exactly good for every finite `N,m`. Prove instead that the explicit same rule `T_p=[0,L_p)` works for each fixed visible dimension `m` once `N` is sufficiently large. This is exactly the quantifier order needed for projective convergence:

`for every fixed k, as N->infinity, restriction to [k] converges`.

For a specified split `A|B`, the threshold box count over `T_p` differs from its volume by at most `L_p D`. After the clock normalization, the split-rate error is at most `2 H_{p-1} D` plus the beta Riemann-sum error. Hence every fixed specified split rate tends to `B(i,j)`.

Hidden labels lump out exactly as in C072, so fixed restrictions are finite-state CTMCs; generator convergence should imply bounded-window path-TV convergence, hence J1 and the projective CTCS(infinity) limit.

## Finite distinction to check

At `N=6`, C072 uses `d=3,p=11`; here `L=ceil(11^(3/4))=7`. Compute exact labeled split-rate multisets. Preliminary hand reasoning predicts many more zero `2|4` and `3|3` rates than C072's single zero `2|4` rate, giving a relabeling/time-rescaling invariant finite witness against both the source and C072.

No checker was written before this note.