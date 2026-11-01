# B17 handoff — selector-phase obstruction and low-plaquette cut replacement

Status: full FEI OPEN. Stronger bridge REFUTED; replacement theorem PROVED.

Consumed source: `fleet03/B12/20260921T211211Z-ordered-parent-flag-nonreuse/REPORT.md`, specifically its stop-conditioned prefix remainder
`R_T = I TC(P|T) - E log2(K!)`.

## Exact Boolean adversary

For `m` selector blocks, let
`F_m(a,y)=prod_b y_{b,a_b}` and let `c_m(a)` be `-1` only at the all-zero address, `+1` elsewhere. Put `G_m=c_m F_m`.

For every address-only Boolean phase `c(a)`, multiplication by `c` changes each selector Fourier coefficient only by a sign indexed by the selected data-label vector. Hence `cF_m` and `F_m` have **identical squared Fourier spectra**. In particular

- `H(G_m)=2m`, `I(G_m)=3m/2`, so `H/I=4/3`;
- the prefix law and `R_T` are exactly those of the disjoint tensor `F_m`.

Yet `G_m` is physically interaction-connected: within each selector block the address--data plaquettes have defect probability `1`, while for distinct addresses `p_ij=2^{2-m}>0`.

For `c0=2 h2(1/8)-h2(1/4)-1/4=0.0258507619400599...`, the stop-conditioned prefix law obeys

`TC(P|T) >= c0 (m-1)/6`, hence

`R_T(G_m)/I(G_m) >= c0 (m-1)/6 - (4/3) log2(2m) -> infinity`.

Therefore no finite universal `R_T <= C I` can hold, **even restricted to actual Boolean interaction-connected common potentials**. This is not an FEI counterexample.

## Replacement theorem

For a coordinate cut `A|B`, define
`Q_AB=sum_{i in A,j in B} p_ij(f)`.
Then there exist Boolean factors `g(x_A),h(x_B)` with

`Pr[f != g h] <= Q_AB/4`.

Proof: a random large rectangle second difference is the XOR of shifted elementary cross-plaquette defects, so its defect probability is at most `Q_AB/4`; averaging the anchor product
`f(a,b0) f(a0,b) f(a0,b0)` gives the factorization.

If `Q<=1/4`, the squared-spectrum TV distance to the product is at most `sqrt(Q)`. Thus, when the two factors already satisfy FEI with constant `C`,

`H(f) <= C I(f) + (C+1)n sqrt(Q) + h2(sqrt(Q))`.

For the adversary `G_m`, a cut separating `k` whole selector blocks has
`Q=k(m-k)2^{2-m}`, so the exact connectedness caused by the rare phase is recognized as an exponentially cheap approximate split.

Next shared target: amortize the low-cut penalties over an adaptive factorization tree, or prove an `O(I)` code on the terminal plaquette-expander cores. Do not revive global/connected `R_T=O(I)`.
