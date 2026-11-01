SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B04, 2026-09-22T17:47:02Z.
attacking: product-space logarithmic rearrangement for a zero-diagonal hyperbolic coordinate pair over a partner-controlled residual, to close a concrete grouped-coordinate branch of the bank-dominant frontier.

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B04-20260922T174702Z-r15`  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication and source scope

The full theorem remains open. The first unpaid implication used here is a concrete sub-interface of the current grouped-coordinate routing gap:

`QFORM-HYPERBOLIC-PAIR-SELECTION-v1` — from the unresolved bank-dominant / near-isotropic branch, produce a quantitatively useful original-coordinate mixed pair, or a substitute grouped packet, whose residual already lies in a completed density branch. No assertion is made that the bare three-large-eigenvalue hypothesis always supplies such a pair.

This run proves the analytic transfer once such a mixed pair is present. The transfer is deliberately in original coordinates and therefore does not use post-rotation independence, a conditional projection-density cap, pointwise one-dimensional Fresnel decay, or a uniformly good small principal minor.

Fresh owner control advanced during the run to revision `2026-09-22.10`; QFORM remains the sole target. The live corrections consumed include the refutations of uniform pointwise oscillatory decay, conditional-cap-as-independence, one-Schur extraction, local-good-minor/cross-rank-three dichotomies, and fiberwise trace control.

Named partner actually applied: `fleet03/B04`, theorem `QFORM-RANK2-SCHUR-NOLEVERAGE-v1`, canonical source `yspennstate/math-open-problems@2761bd3896c56a1f929761e69035ba7cb8ebc2bc`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260922T164839Z-r14/REPORT.md`. In its exact explicit heavy-row instance it gives the all-input-law density bound `B_partner=9.8345318556`.

## 2. Product-density logarithmic envelope

### Lemma 2.1 — shifted hyperbolic product

Let `U,V` be independent real random variables with densities bounded by one. For `c!=0`, the random variable

`T=2cUV`

has a density `g_c` satisfying, for almost every `s!=0`,

`g_c(s) <= |c|^(-1) [1 + log_+(2|c|/|s|)]`.               (2.1)

The same bound holds after arbitrary deterministic translations of `U,V`.

**Proof.** Put `r=|s|/(2|c|)`. The product-density formula is

`g_c(s)=(2|c|)^(-1) int f_U(u) f_V(s/(2cu)) du/|u|`.

If `0<r<=1`, split the integral into `|u|<r`, `r<=|u|<=1`, and `|u|>1`. On `|u|>1`, use `1/|u|<=1` and `int f_U=1`, giving at most `1/(2|c|)`. On the middle annulus use only both caps, giving

`(2|c|)^(-1) int_{r<=|u|<=1} du/|u| = |c|^(-1) log(1/r)`.

On `|u|<r`, the substitution `v=s/(2cu)` maps to `|v|>1` and gives the symmetric bound `1/(2|c|)`. This proves (2.1) for `r<=1`. If `r>1`, split instead at `sqrt(r)` and use the same symmetry to obtain `g_c(s)<=1/(|c|sqrt(r))<1/|c|`, which is stronger than (2.1). Deterministic translations preserve the density caps and independence. QED.

The logarithm is the correct rank-two indefinite singularity. The point is that it is integrable against one further bounded-density residual even when the shifts of `U,V` are completely correlated with that residual.

## 3. Main transfer theorem

### Theorem 3.1 — `QFORM-HYPERBOLIC-PAIR-DENSITY-TRANSFER-v1`

Let `Y,Z,W_1,...,W_m` be independent real random variables with densities bounded by one. Let `L_1,L_2` be arbitrary real linear forms in `W=(W_1,...,W_m)`, let `R(W)` be any measurable real random variable of the form induced by a quadratic polynomial in `W`, and let `c!=0`. Define

`Q = 2cYZ + 2Y L_1(W) + 2Z L_2(W) + R(W)`

and

`H(W) = R(W) - 2 L_1(W)L_2(W)/c`.                         (3.1)

If `H` has a density bounded by `B`, then `Q` has an essentially bounded density and

`||p_Q||_infinity <= |c|^(-1) + 4B`.                       (3.2)

**Proof.** Condition on `W`. Completing the hyperbolic product in the two untouched original coordinates gives the exact identity

`Q = 2c (Y + L_2(W)/c)(Z + L_1(W)/c) + H(W)`.             (3.3)

Given `W`, the two factors are still independent translations of the original variables `Y,Z`, hence both conditional density caps remain one. Lemma 2.1 therefore yields for almost every `t`

`p_Q(t) <= |c|^(-1) [1 + E log_+(2|c|/|t-H|)]`.

Using `||p_H||_infinity<=B`,

`E log_+(2|c|/|t-H|)
 <= B int_R log_+(2|c|/|u|) du
 = 4B|c|`,

because `int_{-M}^M log(M/|u|)du=2M` with `M=2|c|`. Substitution gives (3.2). QED.

No independence between the shifts `L_1,L_2` and the residual `H` is asserted or used. This is exactly the product-preserving feature missing from naive spectral conditioning.

### Corollary 3.2 — actual use of fleet03/B04

Assume in addition that the effective residual `H` is itself an original-coordinate quadratic form to which the completed partner theorem applies: one physical scalar pivot `a!=0` has Schur complement of rank exactly two with nonzero eigenvalues `mu_1,mu_2`. Fleet03/B04 gives

`B <= C_* |a|^(-1/2)|mu_1mu_2|^(-1/4)`,

where

`C_*=23.3905905108...`.

Hence Theorem 3.1 gives the explicit inequality

`||p_Q||_infinity
 <= |c|^(-1)
    + 4 C_* |a|^(-1/2)|mu_1mu_2|^(-1/4)`.                 (3.4)

Thus a completed scalar-pivot/rank-two residual certificate survives the addition of an arbitrarily shifted original-coordinate hyperbolic pair. This is a strict extension of the partner scope: the pair can reuse every residual coordinate through `L_1,L_2`, so the added directions are not post-rotation independent noise.

## 4. A zero-diagonal three-coordinate packet without any residual density premise

The same rearrangement also pays the exact two-zero-diagonal local packet directly.

### Theorem 4.1 — `QFORM-TWO-ZERO-DIAGONAL-PACKET-v1`

Let `X,Y,Z` be independent cap-one variables. Let

`M = [[d,a,b],[a,0,c],[b,c,0]]`,  with `c!=0` and `det M!=0`.

Allow arbitrary affine terms in `X,Y,Z`; these may depend on variables already conditioned outside the packet. Then the resulting quadratic polynomial has a density satisfying

`||p||_infinity <= 1/|c| + 8 sqrt(|c|/|det M|)`.           (4.1)

Consequently, if `sigma_min(M)>=1`, then

`||p||_infinity <= 2 + 8sqrt(2) < 13.314`.                 (4.2)

**Proof.** Condition on any outside variables first; they contribute only constants and affine coefficients to the packet. For fixed `X=x`, complete the `Y,Z` product. The remaining scalar polynomial in `x` has quadratic coefficient

`kappa = d - 2ab/c = -det(M)/c^2 !=0`.                     (4.3)

After a translation of `X`, Lemma 2.1 gives

`p(t) <= |c|^(-1) [1 + int f_X(x)
 log_+(2|c|/|t_0-kappa x^2|) dx]`.

Since `f_X<=1`, drop it and bound by the full Lebesgue integral. Put `M_0=2|c|`. After scaling `u=x sqrt(|kappa|/M_0)`, it remains to control

`J(tau,eps)=int_R log_+(1/|tau+eps u^2|) du`, `eps in {+1,-1}`.

By layer cake,

`J = int_0^infinity |{u: |tau+eps u^2|<e^{-s}}| ds`.

For every `delta>0` and every real `alpha`, the one-dimensional quadratic sublevel set satisfies

`|{u: |u^2-alpha|<delta}| <= 2sqrt(2delta)`.

Hence

`J <= int_0^infinity 2sqrt(2)e^{-s/2} ds = 4sqrt(2)`.

Therefore the logarithmic integral is at most

`4sqrt(2) sqrt(M_0/|kappa|)
 = 8 |c|^(3/2)/sqrt(|det M|)`,

which proves (4.1).

For (4.2), `sigma_min(M)>=1` implies `||M^{-1}||<=1`. Since `(M^{-1})_{11}=-c^2/det M`, one has `c^2<=|det M|`. Also writing `D=2ab-cd`, so `det M=cD`, the inverse entries give `a^2<=|det M|`, `b^2<=|det M|`, and `|ab-cd|<=|det M|`. Thus `|ab|<=|det M|` and

`|det M|=|c| |ab+(ab-cd)| <=2|c||det M|`,

so `|c|>=1/2`. Substituting into (4.1) gives (4.2). QED.

This packet theorem is conditional on an actual physical packet; it does not revive the refuted universal-good-small-minor dichotomy.

## 5. Explicit genuinely rotated indefinite full-rank-nearby example

Use the partner's explicit four-coordinate residual `H(W)=W^T A_0 W` with

`u=(sqrt(3)/2,1/2,0)`, `v=(0,0,1)`,
`S=2uu^T-2vv^T`, `b=(0.1,0.1,0.1)`,
`A_0=[[S+bb^T/2,b],[b^T,2]]`.

The partner proof gives

`||p_H||_infinity <= 9.8345318556`.                         (5.1)

Take `c=0.5`, `L_1(W)=0.01 W_1`, `L_2(W)=0.01 W_2`, and choose

`R(W)=H(W)+2L_1(W)L_2(W)/c`.

Then the full six-coordinate matrix is

```
[[ 1.505,          0.871225403784,  0.005,  0.1,  0.01, 0.  ],
 [ 0.871225403784, 0.505,           0.005,  0.1,  0.,   0.01],
 [ 0.005,          0.005,          -1.995,  0.1,  0.,   0.  ],
 [ 0.1,            0.1,             0.1,    2.,    0.,   0.  ],
 [ 0.01,           0.,              0.,     0.,    0.,   0.5 ],
 [ 0.,             0.01,            0.,     0.,    0.5,  0.  ]].
```

The exact checker saved beside this report returns

`eig(A6)=(-1.997504888364,-0.500189249266,0,0.499951120822,1.869581593576,2.143161423232)`

(up to numerical roundoff at the displayed zero) and perturbation norm `0.010100499987500613` from `A_0 direct_sum [[0,0.5],[0.5,0]]`. Hence this genuinely rotated indefinite form has exactly three eigenvalues of modulus greater than one, while retaining two additional small nonzero directions and nontrivial cross-couplings.

Applying (3.2) to the partner value (5.1) gives the all-input-law estimate

`||p_Q||_infinity <= 2 + 4(9.8345318556)
                   = 41.3381274224`.                        (5.2)

This example is inside the exact target and does not discard or declare independence of the additional spectral directions.

## 6. What changed and what remains

The new transfer theorem pays one concrete version of the current bank-aggregation interface: once a product-preserving routing exposes a zero-diagonal hyperbolic pair over any already-controlled residual, arbitrary cross shifts into that residual cost only `|c|^{-1}+4B`. The logarithmic rank-two singularity is therefore harmless after averaging against one bounded-density residual, without any conditional-density independence assumption.

The first unpaid implication is now the **selection/routing** step, not the analytic smoothing of such a packet: under the bare three-large-eigenvalue hypothesis, prove that every unresolved bank-dominant/near-isotropic configuration either exposes a quantitatively strong hyperbolic pair with a completed residual certificate, or enters another already-proved grouped/ridge branch. Existing counterexamples forbid replacing this by a universally good single 3x3 minor or a single Schur extraction.

No full-solution, continuity, novelty, or source-external counterexample claim is made. The result is `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

## 7. Exact calculation record and privacy review

The checker used only NumPy linear algebra on the displayed harmless matrices. Source file: `check_example.py`; recorded output: `check_output.txt`. No external data, credentials, scheduler identifiers, private transcripts, benchmark material, or machine paths occur in this run folder. A manual changed-file fallback review was used because no repository secret-scanner execution interface was exposed in this connector-only run.