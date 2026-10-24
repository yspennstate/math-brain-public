SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-23T01:26:58Z.
attacking: rank-two decoupled volume plus an aggregate square channel, preserving sum/difference dependence and paying the half-Riesz endpoint before any local coefficient inversion.

# account02/B03 — two-volume plus aggregate-square integrability compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Run: `20260923T012658Z-account02-B03-QFORM-auto11`  
Classification: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full universal QFORM theorem remains open. This report proves two dimension-free synthesis lemmas: a dependence-safe half-Riesz-to-square transducer allowing an active-dependent shift, and a direct L1 Fourier theorem for an independent aggregate square. It then applies them to an explicit no-pivot target family whose useful cross block has rank exactly two. No post-rotation independence, conditional cap for a conjugate sum/difference variable, law-uniform scalar pointwise Fresnel decay, moment assumption, support condition, or fixed-good-minor assertion is used.

## 1. Source-valid inputs

Fresh control was resolved from `yspennstate/math-research-brain` main, initially at `1aacbe1157ffc5aec3b67ab0448ade985816e65b` and refreshed before publication to `4adba71cf199af3b7a8ec29c33cab49635655524`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM is the sole target, and no account/slot pause applies.

The required pinned Claude input is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

For disjoint sets of ORIGINAL independent coordinates `I,J`, write `M=A[I,J]`. For the squared-minor two-volume

`Z2=e_2(M^T M)>0`

and its volume-sampling row marginals `alpha_i`, put `h=max_i alpha_i`. The Claude decoupling calculation preserves the actual sum/difference dependence: after one Cauchy--Schwarz step the difference coordinates on the J-bank are independent across coordinates, but no difference variable is declared independent of its conjugate sum. Its general `D_k` estimate is the input from which the partner theorem below is derived.

The designated partner result actually applied is account03/B03, `QFORM-VOLUME-MARGINAL-WEIGHTED-RIESZ-v1`, source state

`yspennstate/math-open-problems@370534c8763da810a1b81945e0e44344feab0b75`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T235821Z-account03-B03-QFORM-r22/REPORT.md`.

If `h<1`, set

`q=max(1,2h)`, so `1<=q<2`.

For the conditioned quadratic-plus-linear residual `R` the partner proves

`sup_s E |R-s|^(-1/2) <= C2(h) Z2^(-1/8)`,                     (1.1)

where

`C2(h)=8/(2-q) * (e/q)^(1/4)`.                                 (1.2)

Its proof starts from the dependence-safe envelope

`|phi_R(t)| <= min(1, B |t|^(-1/q))`,                          (1.3)

with

`B=(2 pi)^(1/q) (e/q)^(1/(2q)) Z2^(-1/(4q))`.                 (1.4)

The standard one-dimensional product-projection estimate used below is source-pinned in account02/B04 at `yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7`: for independent cap-one original coordinates and nonzero `v`,

`||p_(v^T X)||_infinity <= sqrt(2)/||v||_2`.                   (1.5)

Only disjoint original-coordinate banks are combined, so every independence assertion below is genuine.

## 2. New theorem I: aggregate square with an active-dependent shift

### Theorem 2.1 — `QFORM-TWOVOLUME-AGGREGATE-SQUARE-HALFRIESZ-v1`

Assume the residual `R(W)` has the certificate (1.1). Let `Y` be independent of `W`, with density bounded by `M_Y`, and let `m(W)` be an arbitrary measurable function, with no independence assumed between `m(W)` and `R(W)`. For `lambda != 0`, define

`Q=lambda [Y+m(W)]^2 + R(W)`.                                  (2.1)

Then

`boxed:
 ||p_Q||_infinity
 <= C2(h) M_Y |lambda|^(-1/2) Z2^(-1/8).
`                                                                  (2.2)

Therefore every interval `J0` satisfies

`P(Q in J0) <= C2(h) M_Y |lambda|^(-1/2) Z2^(-1/8) |J0|`.       (2.3)

#### Proof

Condition on `W=w`. Translation of a cap-`M_Y` density does not change its cap. The pushforward of `Y+m(w)` under `y -> lambda y^2` has, for almost every compatible `u`,

`p_(lambda(Y+m)^2 | W=w)(u)
 <= M_Y |lambda|^(-1/2) |u|^(-1/2)`.                            (2.4)

Indeed the two inverse roots each contribute the reciprocal derivative `1/(2 sqrt(|lambda u|))`. Averaging the conditional convolution therefore gives, for a.e. `s`,

`p_Q(s)
 <= M_Y |lambda|^(-1/2) E |s-R(W)|^(-1/2).`                    (2.5)

Apply (1.1). This proves (2.2)--(2.3). QED.

The point is structural: the square shift may depend arbitrarily on the SAME active variables that generate the residual. We never condition on a difference variable and then assign a false density cap to its conjugate sum.

### Corollary 2.2 — whole original-coordinate square bank

Let `K` be a disjoint original-coordinate bank and `Y=v^T X_K`, `v!=0`. Then (1.5) gives

`boxed:
 ||p_Q||_infinity
 <= [8 sqrt(2)/(2-q)] (e/q)^(1/4)
    |lambda|^(-1/2) ||v||_2^(-1) Z2^(-1/8).
`                                                                  (2.6)

Thus the partner's physical-scalar square peel extends without rotation to an entire disjoint aggregate bank. The price is the aggregate norm `||v||_2`, not the largest physical coefficient.

## 3. New theorem II: close an actual L1 time integral

When the square channel is genuinely independent of the residual after any permitted outside conditioning, one can do better than the half-Riesz transducer and close the exact B03 time-integrability obligation.

### Lemma 3.1 — translated square density in every `L^r`, `1<r<2`

Let `Y` have density at most `M`, let `b` be deterministic, and let

`S=lambda (Y-b)^2`, `lambda!=0`.

Then for every `1<r<2`,

`boxed:
 ||p_S||_r^r
 <= [2^(r-1)/(2-r)] M^(2r-2) |lambda|^(1-r).
`                                                                  (3.1)

#### Proof

It suffices to take `lambda>0`. Put

`H(u)=f_Y(b+u)+f_Y(b-u)`, `u>=0`.

Then `0<=H<=2M` and `integral_0^infinity H=1`. The root formula and the substitution `s=lambda u^2` give

`||p_S||_r^r
 =(2|lambda|)^(1-r) integral_0^infinity H(u)^r u^(1-r) du`.     (3.2)

Since `u^(1-r)` is decreasing, the bathtub principle with cap `2M` and mass one maximizes the last integral at `H=2M` on `[0,(2M)^(-1)]`. Hence

`integral H^r u^(1-r) du
 <= (2M)^(2r-2)/(2-r)`,                                           (3.3)

which is exactly (3.1). QED.

### Theorem 3.2 — `QFORM-TWOVOLUME-PLUS-SQUARE-L1-v1`

Assume (1.3)--(1.4). Let `S=lambda(Y-b)^2` be independent of `R`, with the cap `M` above. For any

`q<r<2`,                                                                (3.4)

put `p=r/(r-1)`. Then `phi_(R+S)` belongs to `L^1`, and

`boxed:
 ||p_(R+S)||_infinity
 <= 2 [ r/((r-q)(2-r)) ]^(1/r)
      (e/q)^(1/(2r))
      Z2^(-1/(4r))
      M^(2(r-1)/r)
      |lambda|^(-(r-1)/r).
`                                                                  (3.5)

In particular the density has a bounded continuous representative.

#### Proof

Write `a=1/q`. From (1.3), splitting at `T=B^(1/a)`,

`integral |phi_R(t)|^r dt
 <= [2 a r/(a r-1)] B^(1/a)`.                                  (3.6)

Therefore

`||phi_R||_r
 <= [2ar/(ar-1)]^(1/r)
    (2 pi)^(1/r)(e/q)^(1/(2r)) Z2^(-1/(4r)).`                   (3.7)

Hausdorff--Young with the Fourier convention `hat f(t)=integral e^(itx)f(x)dx`, together with Lemma 3.1, yields

`||phi_S||_p
 <= (2 pi)^(1/p)
    [2^(r-1)/(2-r)]^(1/r)
    M^(2(r-1)/r)|lambda|^(-(r-1)/r).`                           (3.8)

Since `1/r+1/p=1`, Holder gives `phi_R phi_S in L^1`. Fourier inversion and `(2 pi)^(-1)` cancel the `(2 pi)^(1/r+1/p)` factor. Using `a=1/q`, the remaining constants simplify to (3.5). Absolute integrability gives a bounded continuous density. QED.

A convenient symmetric choice is

`r=(q+2)/2`,                                                       (3.9)

which gives

`boxed:
 ||p_(R+S)||_infinity
 <= C(q) Z2^(-1/[2(q+2)])
    M^(2q/(q+2)) |lambda|^(-q/(q+2)),
`                                                                  (3.10)

where

`C(q)=2 [2(q+2)/(2-q)^2]^(2/(q+2)) (e/q)^(1/(q+2)).`           (3.11)

This is a literal integrated-time closure: two units of decoupled cross volume provide an `L^r` characteristic function just above the critical exponent, while the independent square contributes the dual `L^p` factor. No pointwise scalar Fresnel estimate is invoked.

## 4. Exact no-pivot target family paid by the new splice

This subsection applies (3.10) to a genuine source-valid N3 family rather than a toy residual.

Fix `m>=4`. Let `U_m,V_m` be `m x 2` real matrices with orthonormal columns and every row norm squared `2/m`; for example use the normalized sine/cosine frame

`u_j=sqrt(2/m)(cos(2 pi j/m), sin(2 pi j/m))`

and the same construction for `V_m`. Set

`M_m=U_m V_m^T`,                                                  (4.1)

and on a third disjoint `m`-coordinate bank set

`w=m^(-1/2)(1,...,1)`.                                           (4.2)

Consider the symmetric `3m x 3m` matrix

`A_m = [[0, M_m, 0], [M_m^T, 0, 0], [0, 0, w w^T]].`           (4.3)

### 4.1 Exact spectrum and physical no-pivot scales

`M_m` has singular values exactly `1,1`, so the first two banks contribute eigenvalues `+1,+1,-1,-1`. The last bank contributes eigenvalue `+1`. Thus `A_m` has five eigenvalues of modulus one and lies in the exact owner target.

Every diagonal entry has modulus at most `1/m`. Also

`|(M_m)_{ij}| <= ||u_i|| ||v_j|| =2/m`.                         (4.4)

Every physical two-coordinate determinant therefore has magnitude at most `4/m^2`: the only nonzero candidates are an I--J pair, whose determinant is `-(M_m)_{ij}^2`; a pair inside the rank-one `w w^T` bank has determinant zero. Consequently, for every fixed no-pivot threshold `tau>0`, all sufficiently large `m` satisfy the N3 diagonal/pair conditions while retaining five actual unit eigenvalues.

### 4.2 The two-volume certificate is dimension-free

Because `M_m` has exactly two unit singular values,

`Z2=e_2(M_m^T M_m)=1`.                                           (4.5)

For exact rank two, the squared-minor volume-sampling row marginal equals the row leverage in `U_m`, hence

`h=2/m <=1/2`, so `q=1`.                                         (4.6)

The aggregate square variable `Y=w^T X_K` is independent of the first two banks and, by (1.5),

`||p_Y||_infinity <= sqrt(2)`.                                   (4.7)

The quadratic variable is

`Q_m=2 X_I^T M_m X_J + (w^T X_K)^2`.                            (4.8)

Apply (3.10) with `q=1`, `Z2=1`, `M=sqrt(2)`, `lambda=1`. Then for every choice of cap-one input laws,

`boxed:
 ||p_(Q_m)||_infinity
 <= 2 * 6^(2/3) * e^(1/3) * 2^(1/3)
 = 11.6119633147... .
`                                                                  (4.9)

Moreover `p_(Q_m)` is continuous.

Thus a genuine N3 family with vanishing physical diagonals and pair determinants is uniformly controlled by a **rank-two decoupled volume + aggregate square** splice. The selected cross block has rank exactly two, so its third volume vanishes identically; the missing integrability exponent is supplied by the independent aggregate square, not by a fictitious third cross direction.

The more robust Theorem 2.1 also gives

`||p_(Q_m)||_infinity <= 8 sqrt(2) e^(1/4)=14.527...`,            (4.10)

and, unlike (4.9), survives replacement of `(w^T X_K)^2` by

`[w^T X_K + m0(W)]^2`

with an arbitrary shift `m0(W)` depending on the variables generating the residual, provided the same residual two-volume certificate remains valid. This is the dependence-safe version relevant after completing aligned square channels.

## 5. Relation to the previous local/global collision obstruction

The preceding account02/B03 run exhibited an N3 mixed-hub family for which every local physical-pair half-collision energy diverges like a positive power of the bank size while the correctly aggregated global collision energy stays bounded. The present result changes mechanism rather than repeating that diagnostic: it first aggregates a **rank-two** cross bank through the independent-copy/volume theorem, obtains the exact half-Riesz or `L^r` time resource, and only then spends the missing square direction.

This is compatible with the live correction `QFORM-UV-CONDITIONAL-CAP-FALSE`: the proof never conditions on `X-X'` and assigns a cap to `X+X'`. It is also compatible with the local-minor and one-Schur counterexamples: (4.9) is paid entirely at aggregate bank scale even though every physical pair certificate goes to zero.

## 6. What is paid and what remains

Paid here:

1. **Active-dependent aggregate square:** a rank-two decoupled cross bank with `h<1` and `Z2>0` plus one independent aggregate scalar closes linear small-ball scale by (2.2), even when the square shift is arbitrarily dependent on the residual variables.
2. **Actual L1 time integral:** if the aggregate square is independent of the residual after allowed outside conditioning, the explicit Holder splice (3.5) gives `phi in L1`, hence a bounded continuous density.
3. **A real N3 class:** the exact family (4.3) has five large eigenvalues, vanishing physical pivot scales, rank-two active cross block, and the uniform law-free bound (4.9).

Not paid:

- The bare hypothesis `s_3(A)>=1` has not been shown to yield a disjoint decomposition with a two-volume residual and an aligned aggregate square channel of universal normalized strength.
- Arbitrary in-bank quadratic curvature on the square bank can destroy the displayed one-square form; a small matrix coefficient is not a small random perturbation for unbounded inputs.
- A genuinely hybrid N3 matrix may have its third spectral direction entangled with the rank-two cross bank so that neither the independent-square Holder splice nor the aligned active-dependent square completion applies.

The first unpaid implication is therefore structural and precise: from an N3 matrix escaping the proved three/five-volume exits, either produce a rank-two cross packet `M` with controlled `Z2,h` and a product-preserving aggregate square direction transverse to it, or prove a different grouped certificate for the entangled third direction. The current theorem supplies the analytic endpoint once that product-preserving three-direction decomposition is available.

Independent end-to-end review status: **not performed in this run**. This is a supporting theorem, not a full proof candidate.
