SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-23T18:22:25Z.
attacking: a source-valid compression of the punctured heavy null-hub collar when the shear outside the active spectral plane is carried by a disjoint original-coordinate bank; combine the sharp product-projection theorem with the completed zero-pivot 1+2 trace receiver, then splice the latest fleet04/B18 moderate-edge result.

# fleet03/B18 r32 — source-separated shear compresses exactly to a zero-pivot 1+2 trace

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** literature-to-proof transfer  
**Status:** `NEW SUPPORTING TARGET-LEVEL RECEIVER + PARTNER SPLICE / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** continuous `C_0` density on the new receiver; unrestricted continuity remains open.

## 1. Exact target and correction boundary

The owner target remains the full arbitrary-law statement: independent real original-coordinate inputs with one-dimensional probability densities bounded by one, and an arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one. No Gaussian, log-concave, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation-independence hypothesis is introduced below.

The proof uses neither the refuted law-uniform pointwise quadratic-phase decay, nor arbitrary-joint indefinite coarea, nor a conditional density cap as a substitute for independence, nor a fixed-good-minor extraction, nor deletion of a small nonzero edge. The source partition below is literal in original coordinates.

## 2. Primary literature and completed nonlinear receiver

### 2.1 Livshyts--Paouris--Pivovarov

Primary source: Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949.

For a product probability density with every one-dimensional factor bounded by one, every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. I use only `k=2`, hence the cap `2`. The theorem assumes no moments, support condition, log-concavity, centering, symmetry, smoothness, or identical laws. It gives a joint density cap; it does **not** assert independence of the two projected coordinates.

I also checked Juškevičius--Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190. Its sharp Rogozin-type theorem controls maximum densities of sums of independent bounded-density variables. It can sharpen the scalar cap in special source banks, but it is not used to infer any nonlinear quadratic estimate here.

### 2.2 Zero-pivot scalar-versus-vector theorem

The nonlinear receiver is the completed theorem `QFORM-ZEROPIVOT-1PLUS2-DENSITY-v1`, source-pinned at

`yspennstate/math-open-problems@dd94932dae1791af1bca9396c062e17d0e55142a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B18/20260922T175509Z-qform-B18-a01-r15/REPORT.md`.

It states: if a scalar `X` with density cap one is genuinely independent of a two-dimensional random vector `Y` whose arbitrary joint density is capped by `M`, and

`H=[[0,ell^T],[ell,B]]`

is real symmetric and nonsingular, then `(X,Y)^T H (X,Y)` has a continuous density and

`||p||_infinity <= 6 M^(2/3) |det H|^(-1/3)`.                 (2.1)

Fleet04/B18 independently transferred and applied this receiver in its completed run r2,

`yspennstate/math-open-problems@f852e87a4002c603ac47039f22a1921061b19f2d`,

showing in particular how sharp one-dimensional product-bank rearrangement can be inserted without inventing independence after rotation.

A scaling consequence needed below is worth recording. If the scalar density cap is `N` rather than one, rescale `X_tilde=N X`. Then `X_tilde` has cap one and the zero-pivot determinant is divided by `N^2`. Therefore

`boxed:
 ||p||_infinity <= 6 (MN)^(2/3) |det H|^(-1/3).`               (2.2)

No new analysis is hidden in (2.2); it is exactly (2.1) under scalar rescaling.

## 3. New theorem: source-separated shear compression

Use the exact-rank-three null-hub normal form already established in the fleet:

`Q = 2 (X_0 + ell dot X_L)(g dot X_L) + d (beta dot X_L)^2`,       (3.1)

where the original coordinates are independent cap-one variables,

`||beta||_2=1`, `beta dot g=0`, `gamma:=||g||_2>0`, `d!=0`.         (3.2)

### Theorem `QFORM-NULLHUB-SOURCE-SEPARATED-SHEAR-v1`

Suppose the leaf indices admit a literal original-coordinate partition

`L = J disjoint_union K`                                                     (3.3)

such that

`g_K=0`, `beta_K=0`,                                                    (3.4)

and for some real `a,b`,

`ell_J = a g_J/gamma + b beta_J`.                                  (3.5)

There is **no** restriction on `ell_K`. Then `Q` has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= 6 * 2^(2/3) * (|d| gamma^2)^(-1/3).`                         (3.6)

The exact-alignment case `ell in span{g,beta}` is the special case `K=emptyset`.

### Proof

Define the two active leaf projections

`S = (g_J dot X_J)/gamma`,
`T = beta_J dot X_J`.                                              (3.7)

By (3.2)--(3.4), the deterministic coefficient vectors `g_J/gamma` and `beta_J` are orthonormal in `R^J`. Thus `(S,T)` is a two-dimensional orthogonal marginal of the genuine original-coordinate product source `X_J`. Livshyts--Paouris--Pivovarov gives a joint density `rho_ST` satisfying

`||rho_ST||_infinity <= 2`.                                       (3.8)

No independence of `S` and `T` is claimed or needed.

Put

`W = ell_K dot X_K`, `X_* = X_0 + W`.                              (3.9)

Because `{0}`, `J`, and `K` are disjoint original-coordinate source blocks, `X_*` is genuinely independent of `(S,T)`. Moreover convolution with the independent law of `W` cannot raise the density cap of `X_0`, so

`||p_(X_*)||_infinity <= 1`.                                      (3.10)

Using (3.4)--(3.5),

`g dot X_L = gamma S`,
`beta dot X_L = T`,
`ell dot X_L = aS+bT+W`.                                          (3.11)

Hence (3.1) becomes exactly

`Q = 2 gamma X_* S + 2 a gamma S^2 + 2 b gamma S T + d T^2`.       (3.12)

In the variables `(X_*,S,T)`, this is the quadratic form with matrix

`H = [[0, gamma, 0],
      [gamma, 2a gamma, b gamma],
      [0, b gamma, d]]`.                                          (3.13)

The determinant is independent of the shear parameters:

`det H = -d gamma^2`.                                              (3.14)

Thus `H` is nonsingular. Apply (2.1) with scalar cap one and vector cap `M=2`. Equations (3.8), (3.10), and (3.14) give (3.6), and the receiver also gives continuity and vanishing at infinity. QED.

### Quantitative version with a sharper scalar bank cap

If an independent source-separated shear bank produces `X_*` with density cap `N<=1`, then (2.2) gives

`boxed:
 ||p_Q||_infinity
 <= 6 (2N)^(2/3) (|d|gamma^2)^(-1/3).`                           (3.15)

For example, if `W=cX_k` is one additional independent original coordinate, Young gives `N<=min(1,|c|^(-1))` for `c!=0`.

## 4. Exact target normalization

In the rank-three null-hub spectral normalization already proved in the fleet, if `h` is the hub spectral leverage and `D=|pdet A|=|det M|`, then

`|d| gamma^2 = h D`.                                               (4.1)

Therefore the theorem is exactly

`boxed:
 ||p_Q||_infinity
 <=6*2^(2/3) (hD)^(-1/3).`                                       (4.2)

If all three nonzero eigenvalue magnitudes are at least `s`, then `D>=s^3`, so

`||p_Q||_infinity
 <=6*2^(2/3) h^(-1/3) s^(-1).`                                   (4.3)

For the live Schur-isotropic range `r>=1/2`,

`h=r^2/(1+r^2)>=1/5`,                                             (4.4)

and hence

`boxed:
 ||p_Q||_infinity
 <=6*20^(1/3) s^(-1)
 =16.28650569956944... s^(-1).`                                  (4.5)

At large shear `h->1`, the certificate tends to `6*2^(2/3)=9.5244063118...`.

The important feature is that (4.2) is completely independent of every individual physical hub-leaf edge `g_i`; in particular it stays bounded through the punctured regime `0<|g_i|<<1` whenever the shear provenance (3.3)--(3.5) holds.

## 5. Literal target-valid example with dependent projected coordinates

Let `X_0,X_1,...,X_5` be independent arbitrary cap-one variables. On `J={1,2,3,4}`, put

`u=(1,1,1,1)/2`,
`v=(1,1,-1,-1)/2`.                                                (5.1)

These are orthonormal but the random variables `S=u dot X_J`, `T=v dot X_J` are generally **dependent**, because they use the same four original coordinates. Let `c` be arbitrary and define

`Q_c = 2 (X_0+cX_5) S + T^2`.                                    (5.2)

This is Theorem 3 with `gamma=d=1`, `a=b=0`, `K={5}`. Hence

`||p_(Q_c)||_infinity <=6*2^(2/3)<9.525`                          (5.3)

for every `c`, with a continuous density. If `w=e_0+c e_5`, the physical matrix factors through the three mutually orthogonal coefficient directions `w,u,v`; its nonzero eigenvalues are exactly

`{+||w||,-||w||,1}={+sqrt(1+c^2),-sqrt(1+c^2),1}`.                (5.4)

Thus (5.2) is inside the owner target for every real `c`, including arbitrarily strong source-separated shear. The proof did not make `S,T` independent; the LPP joint cap is exactly what is needed.

For `|c|>=1`, the sharper scalar cap in (3.15) yields the additional valid estimate

`||p_(Q_c)||_infinity
 <=6*2^(2/3)|c|^(-2/3)`.                                         (5.5)

This refinement is not needed for the universal target constant.

## 6. Actual splice with the designated fleet04/B18 partner

The latest compatible fleet04/B18 theorem is the corrected r4 result

`QFORM-NULLHUB-DIAGONAL-GATED-PAIRLOG-v1`,

source-pinned at

`yspennstate/math-open-problems@3460488b1a730f54dbac848cddc3e2761d3f348e`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260923T162049Z-fleet04-B18-QFORM-r4/REPORT.md`.

Inside the target-normalized exact-rank-three null-hub `N3(1/64)` state with `r>=1/2`, it proves the actual inequality

`q_i>1/2`, `|g_i|>=1/64`
`=> ||p_Q||_infinity <64.1795826152`.                             (6.1)

The present theorem adds a different exit:

`source-separated shear (3.3)--(3.5)`
`=> ||p_Q||_infinity <16.286506`                                  (6.2)

with continuity, independently of `g_i`.

The previous fleet03/B18 r31 exact endpoint gives

`q_i>1/2`, `g_i=0`
`=> ||p_Q||_infinity <9.262319472`                                (6.3)

with continuity, while the completed transverse-diffuse theorem gives `<12.927` when every `q_i<=1/2`.

Consequently, within this live null-hub compiler, the combination of existing proved exits and (6.2) leaves only the genuinely source-entangled heavy collar:

- the shear is not reducible by (3.3)--(3.5);
- a heavy witness `q_i>1/2` exists;
- every heavy witness available to this splice has `0<|g_i|<1/64`.

This is precisely the collar in which the new fleet02/B18 punctured-edge stress test shows that a small nonzero edge cannot simply be replaced by zero: a rank-two source-valid construction develops a logarithmic saddle singularity under an arbitrarily small edge. The true rank-three target still has compensating rank-one Schur curvature, so that obstruction does not refute QFORM; it rules out a perturbative use of (6.3).

Equation (6.1) is the requested actual use of a completed fleet04/B18 partner result, not merely a citation.

## 7. Why this implication is source-valid

1. `(S,T)` is a projection of the original product law, so LPP applies literally. Its joint cap is never converted to independence.
2. The scalar `X_*` is independent of `(S,T)` only because the source sets `{0} union K` and `J` are disjoint.
3. The nonlinear passage is exactly the completed zero-pivot 1+2 theorem, which was designed for a dependent two-dimensional vector.
4. The residual source bank enters only by convolution into `X_*`; no support or moment bound is used.
5. No small coefficient is dropped. The determinant identity (3.14) is exact and retains all shear coefficients `a,b`.
6. Arbitrarily fragmented and unbounded input supports are allowed.

## 8. Remaining debt

The unrestricted QFORM conjecture is still **OPEN / NOT PROVED**, and full-target continuity remains open. This theorem does not force the source partition (3.3)--(3.5) from the spectral hypothesis. Its value is to remove an entire aligned/source-separated shear mechanism from the punctured null-hub debt without any lower bound on an individual edge.

The next local analytic target is therefore sharper: preserve the target's rank-one Schur curvature in the genuinely source-entangled state `0<|g_i|<1/64`, and combine its improving `O(|g_i|)` critical-value anti-concentration with the triangular pair singularity without paying the generic `kappa_i^(-1/4)` loss. The fleet02/B18 rank-two obstruction shows that the rank-one curvature must remain visible; small-edge continuity alone is false.

No exact prior literature theorem found in the checked primary sources matches that rough-law source-entangled endpoint. This is a hypothesis audit, not a novelty claim from absence.
