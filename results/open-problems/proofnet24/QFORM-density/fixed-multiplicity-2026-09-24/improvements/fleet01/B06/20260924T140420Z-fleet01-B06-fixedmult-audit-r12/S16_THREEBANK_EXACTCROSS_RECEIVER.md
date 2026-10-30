# fleet01/B06 improvement — exact-crossing receiver for the terminal `s_16` collar

Run: `20260924T140420Z-fleet01-B06-fixedmult-audit-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Fresh repository state inspected before this note included the terminal `s_16` collar results of fleet01/B09 and fleet01/B20 and the earlier exact-rank physical-crossing theorem.

Status: **proved new synthesis / direct receiver; no unconditional 16-eigenvalue theorem claimed.** A source-matching exact-rank crossing theorem already exists, so this run does not duplicate that proof. Instead it applies it to the actual three-bank determinant-transfer geometry forced in the terminal `s_16` chamber.

## Inputs already proved in the repository

### 1. Terminal `r=4` determinant transfer

In the unpaid normalized no-pivot `s_16(A)>=1` chamber, an order-four seed `S,T` supplied by the low-residual interpolation has

\[
B=A[S,T],\qquad b:=|\det B|>0,
\]

and there is a disjoint physical four-set `H` for which, with

\[
C=A[H,T],\qquad G=A[S,H],
\]

one has

\[
P_{H,H}=CB^{-1}G,
\]

and the stronger fleet01/B09 diagonal-dominance estimate gives

\[
\sigma_{\min}(P_{H,H})\ge\delta,
\qquad
\delta:=\frac{74-3\sqrt{101}}{100}=0.4385037313\ldots.
\]

Consequently

\[
|\det C|\,|\det G|
\ge \delta^4 b.
\tag{1}
\]

This is a statement about three disjoint banks of **original coordinates**.

### 2. Exact-rank physical-crossing density theorem

The repository theorem

`proofnet24/QFORM-density/interactive/20260923T194300Z-exact-cross-rank-fourier/REPORT.md`

proves that if, after conditioning all other original coordinates, two remaining original-coordinate banks have an exact rank-`k>=3` crossing block `M`, then arbitrary within-bank quadratic terms and all induced affine terms are allowed and

\[
\|p_Q\|_\infty
\le \frac{2k}{k-2}\,
\left(\prod_{j=1}^k s_j(M)\right)^{-1/k}.
\tag{2}
\]

For an invertible physical `4x4` crossing,

\[
\boxed{
\|p_Q\|_\infty\le4\,|\det M|^{-1/4}.
}
\tag{3}
\]

The theorem retains arbitrary terms internal to the two banks. Conditioning variables outside those two banks merely change those terms' affine coefficients, so the bound remains uniform and may be averaged over the conditioning variables. No rotated coordinate is treated as independent.

## New theorem — three-bank determinant-transfer receiver

Under the terminal three-bank hypotheses above, for arbitrary affine terms and arbitrary independent cap-one coordinate densities,

\[
\boxed{
\|p_Q\|_\infty
\le 4\delta^{-1/2}\,b^{-1/8}
< 6.041\,b^{-1/8}.
}
\tag{4}
\]

A second simultaneous bound is

\[
\|p_Q\|_\infty\le4b^{-1/4}.
\tag{5}
\]

Thus the three-bank transfer weakens the dangerous reciprocal seed-determinant exponent from `1/4` to `1/8` without any law, sign, support, spectrum, or affine restriction.

### Proof

Put

\[
c:=|\det C|,\qquad g:=|\det G|.
\]

Equation (1) implies

\[
\max(c,g)^2\ge cg\ge\delta^4b,
\]

hence

\[
\max(c,g)\ge\delta^2\sqrt b.
\tag{6}
\]

Suppose first that `c>=g`. Condition on **every original coordinate outside `H union T`**. The remaining eight coordinates are still independent with the original cap-one densities. Their physical crossing block is the invertible `4x4` matrix `C`; all conditioned couplings become affine terms and all `H`- and `T`-internal terms remain arbitrary. Applying (3) conditionally gives

\[
\|p_{Q\mid X_{(H\cup T)^c}}\|_\infty\le4c^{-1/4}.
\]

The bound is uniform in the conditioning variables, so averaging the conditional output measures gives

\[
\|p_Q\|_\infty\le4c^{-1/4}.
\]

The case `g>=c` is identical after conditioning outside `S union H`. Therefore

\[
\|p_Q\|_\infty
\le4\max(c,g)^{-1/4}
\le4(\delta^2\sqrt b)^{-1/4}
=4\delta^{-1/2}b^{-1/8},
\]

which is (4). Conditioning outside `S union T` and applying (3) to `B` gives (5).

Numerically,

\[
4\delta^{-1/2}=6.0405063428\ldots.
\]

Only an essential `L^infinity` conclusion is asserted after averaging; the conditional exact-crossing densities are continuous, but continuity of the unconditional mixture is not needed here.

## A second consequence: the random-cut `s_16` survivor is now sharply localized

The earlier fleet01/B20 endpoint theorem gives, unless the order-five branch already pays the density, a physical cut with crossing `M` satisfying

\[
Z_4(M)\ge\frac{\kappa^4}{1280},
\qquad
\frac{Z_5(M)}{Z_4(M)}\le\frac{5\kappa}{16},
\qquad
\sum_{j\ge5}s_j(M)^2\le\frac1{4096}.
\tag{7}
\]

There are now two immediate paid subbranches.

### Exact rank four

If `rank(M)=4`, then `Z_4(M)=(\prod_{j=1}^4s_j(M))^2`. The exact-rank theorem (2) gives

\[
\|p_Q\|_\infty\le4Z_4(M)^{-1/8}
\le 320\,1280^{1/8}
=782.620509\ldots.
\tag{8}
\]

### Diffuse physical leverage

The previous fleet01/B06 fractional graph-determinant theorem proves that if either the maximum physical **row** leverage or, after swapping the two banks, the maximum physical **column** leverage of `M` is at most `3/4`, then

\[
\|p_Q\|_\infty
\le\frac{8e}{\sqrt3}Z_4(M)^{-1/8}
\le2456.491.
\tag{9}
\]

Therefore every still-unpaid cut furnished by (7) must satisfy simultaneously

\[
\boxed{
\operatorname{rank}M\ge5,\qquad
\sum_{j\ge5}s_j(M)^2\le1/4096,\qquad
\max_i\ell_i^{\rm row}>3/4,\qquad
\max_j\ell_j^{\rm col}>3/4.
}
\tag{10}
\]

So the unresolved `s_16` endpoint is not merely “order four.” It is a **near-rank-four crossing with a genuinely nonzero tiny tail and heavy physical leverage on both sides**, together with the second same-bank crossing already forced by fleet01/B20. Exact rank four and either diffuse side are fully paid.

## What remains for an unconditional `17 -> 16` theorem

The three-bank analytic endpoint is now paid at cost `b^{-1/8}`, but the volume-sampled seed determinant `b` itself has no dimension-free lower bound from `V_4>=kappa^4`; determinant-squared mass may be spread among many physical seeds. Therefore (4) is not yet a uniform constant.

Equivalently, the random-cut formulation reduces the remaining problem to (10): a heavy-bileverage, rank-`>=5` crossing lying within Frobenius distance `1/64` of rank four. A valid next implication must exploit the tiny nonzero tail together with the heavy physical hubs and/or the second internal crossing, without deleting the tail as a probabilistic perturbation and without assuming bounded support or moments.

The unconditional same-scope multiplicity therefore remains **17** in this run. The full three-eigenvalue conjecture remains open.
