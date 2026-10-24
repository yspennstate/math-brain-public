SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T10:15:49Z.
attacking: a spectral-threshold / local-footprint-rank compiler that makes arbitrarily many huge signed eigenvalue replacements free when their physical compression has low rank, while paying all smaller eigenvalues only through one operator-norm threshold.

# account01/B12 — spectral-threshold local-rank compiler for arbitrary added eigenvalues

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T101549Z-account01-B12-QFORM-auto11`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED.**  
Continuity: **not claimed by this branch**.

## 1. Exact target and corrections consumed

Target: for independent real `X_i` with densities `<=1` and real symmetric `A` with at least three eigenvalues of absolute value `>=1`, prove a universal bound on the density of `X^TAX`, or give a valid counterexample.

This proof does **not** rotate the random variables, does **not** convolve a dependent quadratic remainder as if independent, and does **not** use any pointwise van-der-Corput estimate. Small operator norm is used only as a deterministic matrix perturbation bound on an original-coordinate physical certificate. The full conjecture and full continuity claim remain open.

Fresh control read: `math-research-brain@fa03254e799d6452bd554991e9402ee068c24bfb`, OWNER CONTROL revision `2026-09-22.15`. The required current corrections include the false law-uniform pointwise oscillatory decay claim, the fiber-sup dimension-loss obstruction, and the no-independence-after-rotation warning; the newer arbitrary-joint coarea and positive conditional-moment gates are also refuted in current research.

## 2. Partner theorem actually used

The newest completed designated partner result was read in full at

`yspennstate/math-open-problems@639e7e151f5d8b83be56a2c6093257fe83deddc3`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T093023Z-account02-B12-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-D5-CROSS-RANK-RESERVE-HYBRID-v1` says the following. Let `H=I disjoint_union J` be `m` ORIGINAL coordinates and

`A0[H,H]=[[C,B],[B^T,D]]`.

If `S=S^T` is arbitrary with `rank S[H,H]<=r`, `T=T^T` is arbitrary with `||T[H,H]||op<=Delta`, and

`s_(2r+11)(D)>=kappa>2Delta`,

then, writing

`C5=5 sqrt(2e)`, `Cm=2 sqrt(6 pi m)`,

one has

`||p_(X^T(A0+S+T)X)||infinity <= (C5+Cm)/(kappa-2Delta)`.    (2.1)

Its proof uses the actual final original-coordinate cross block in the high-cross case and a physical-block singular-value reserve in the low-cross case. No spectral-coordinate independence is used.

## 3. New theorem — `QFORM-SPECTRAL-THRESHOLD-LOCAL-RANK-COMPILER-v1`

Let `E=E^T` be an arbitrary symmetric spectral modification with decomposition

`E = sum_(a=1)^N theta_a v_a v_a^T`,                         (3.1)

where the `v_a` are orthonormal and the `theta_a` are real. Let `R=R^T` be any additional symmetric matrix with

`||R||op <= delta`.                                          (3.2)

Fix a threshold `h>=0`, and define the large spectral set

`L_h={a: |theta_a|>h}`.                                      (3.3)

For a fixed physical original-coordinate core `H`, let

`V_H(h)=[P_H v_a]_(a in L_h)`,

`r_H(h)=rank V_H(h)`.                                        (3.4)

Consider a baseline physical block

`A0[H,H]=[[C,B],[B^T,D]]`,                                  (3.5)

where `H=I disjoint_union J` has cardinality `m`.

Assume

`s_(2 r_H(h)+11)(D) >= kappa > 2(h+delta).`                  (3.6)

Then

`boxed: ||p_(X^T(A0+E+R)X)||infinity`

`       <= [5 sqrt(2e)+2 sqrt(6 pi m)]/[kappa-2(h+delta)].`  (3.7)

The bound is completely independent of:

1. the number of eigenvalues with `|theta_a|>h`;
2. their signs;
3. their magnitudes;
4. their behavior outside `H`.

Only the dimension of their **physical footprint** `span{P_Hv_a:|theta_a|>h}` enters. Every remaining eigenvalue, of either sign and arbitrary multiplicity, is paid collectively only through the single spectral threshold `h`.

### Proof

Split

`E=S_h+W_h`,                                                 (3.8)

where

`S_h=sum_(a in L_h) theta_a v_a v_a^T`,

`W_h=sum_(a notin L_h) theta_a v_a v_a^T`.                  (3.9)

Since the `v_a` are orthonormal,

`||W_h||op = max_(a notin L_h)|theta_a| <= h`.               (3.10)

Therefore

`T_h:=W_h+R`

satisfies

`||T_h[H,H]||op <= ||T_h||op <= h+delta`.                   (3.11)

For the large part, write `Theta_h=diag(theta_a)_(a in L_h)`. Its physical compression is

`S_h[H,H]=V_H(h) Theta_h V_H(h)^T`.                          (3.12)

Hence

`rank S_h[H,H] <= rank V_H(h)=r_H(h)`.                      (3.13)

Now apply the partner theorem (2.1) with

`S=S_h`, `T=T_h`, `r=r_H(h)`, `Delta=h+delta`.               (3.14)

Condition (3.6) is exactly the partner reserve condition. Equation (3.7) follows immediately. QED.

### Exact-rank sharpening

If one can compute

`r_*(h)=rank(S_h[H,H])`,                                     (3.15)

then `r_*(h)<=r_H(h)` and the same theorem holds with `r_H(h)` replaced by `r_*(h)`. This can be strictly better because opposite-signed large modes may cancel on the physical compression. The footprint rank (3.4) is the robust sign-independent upper bound.

### Optimization over threshold

For a fixed core `H`, every `h>=0` gives a separate valid certificate. Therefore one may minimize

`F_H(h)=[5 sqrt(2e)+2 sqrt(6 pi m)]/[kappa_H(h)-2(h+delta)]`, (3.16)

where `kappa_H(h)=s_(2r_H(h)+11)(D)`, over all `h` with positive denominator. This gives a deterministic multiscale compiler: lowering `h` decreases the paid spectral tail but may increase footprint rank; raising `h` decreases footprint rank but costs a larger small-spectrum budget.

## 4. Why this is genuinely stronger than counting large eigenvalues

A large spectral set can have arbitrarily large cardinality while its restriction to one protected physical core has tiny rank. The partner theorem only needs the rank of the **local compression**, not the global rank of the spectral update. The spectral-threshold theorem packages that fact in a basis-invariant, directly checkable form.

In particular, if all large modes obey

`P_H v_a in W`                                               (4.1)

for one fixed `r`-dimensional subspace `W subset R^H`, then `r_H(h)<=r` no matter how many such modes exist and no matter how large the coefficients `theta_a` are.

## 5. Explicit exact-target family with arbitrarily many huge eigenvalue replacements but rank-one physical footprint

This family shows that the number of arbitrary-magnitude replacements can be unbounded while the theorem pays only `r=1`.

Fix any integer `q>=1`. Let the ambient dimension be `n=18+q`. Let `H` be the first 18 original coordinates and split

`|I|=5`, `|J|=13`.

Take the baseline

`A0=2 I_n`.                                                  (5.1)

Then in the chosen core,

`C=2I_5`, `B=0`, `D=2I_13`,                                 (5.2)

so every singular value of `D` equals two.

Let `e` be the first basis vector in `H`. In a `q`-dimensional outside subspace with standard basis `f_1,...,f_q`, set

`u=q^(-1/2) sum_a f_a`,

`c=1-1/sqrt(2)`,

`w_a=f_a-(c/sqrt(q))u`,

`alpha=1/sqrt(2q)`,

`v_a=alpha e+w_a`.                                          (5.3)

A direct calculation gives

`<w_a,w_b>=delta_ab-1/(2q)`,                                (5.4)

hence

`<v_a,v_b>=delta_ab`.                                       (5.5)

Thus `v_1,...,v_q` are orthonormal. Since `A0=2I_n`, they are all exact eigenvectors of `A0` with eigenvalue two.

Now choose completely arbitrary real numbers

`tau_1,...,tau_q in R`                                      (5.6)

and set

`S_big=sum_(a=1)^q tau_a v_a v_a^T`.                        (5.7)

This literally replaces `q` baseline eigenvalues

`2 -> 2+tau_a`,                                             (5.8)

with no sign or magnitude restriction. Yet

`P_H v_a=alpha e` for every `a`,                             (5.9)

so

`r_H(0)=1`,                                                  (5.10)

and explicitly

`S_big[H,H]=alpha^2(sum_a tau_a) ee^T`,                     (5.11)

which has rank at most one regardless of `q`.

Next allow an arbitrary additional symmetric spectral cloud `W` with

`||W||op<=h`,                                                (5.12)

and an arbitrary dense symmetric perturbation `R` with

`||R||op<=delta`.                                            (5.13)

Take, for example,

`h+delta=1/4`.                                               (5.14)

Then `r=1`, `kappa=2`, `m=18`, and

`s_(2r+11)(D)=s_13(D)=2>2(h+delta)=1/2`.                    (5.15)

Therefore (3.7) gives

`||p_Q||infinity`

` <= [5sqrt(2e)+2sqrt(108pi)]/(2-1/2)`

` = 32.331987596039475...`.                                 (5.16)

This bound is uniform in `q` and in every `tau_a`.

### Exact-target check

Before the small/dense perturbations, at least `n-q=18` eigenvalues of `A0+S_big` remain exactly two because the update acts only on the orthonormal span of the `v_a`. After adding `W+R` of operator norm at most `1/4`, Weyl gives at least 18 eigenvalues with magnitude at least

`2-1/4=7/4>1`.                                              (5.17)

Hence the family lies inside the exact QFORM target class for every `q` and every choice of arbitrary signed replacements `tau_a`.

This illustrates the main point: **arbitrarily many huge added eigenvalues can be free when their original-coordinate footprint on the protected core is low-dimensional.**

## 6. Direct equation-level application of the newest account02/B12 partner theorem

For the family above, the partner theorem is applied with

`r=1`, `Delta=h+delta=1/4`, `kappa=2`, `m=18`.              (6.1)

The exact reserve inequality is

`s_(2r+11)(D)=s_13(2I_13)=2 > 2Delta=1/2`.                  (6.2)

Therefore partner equation (3.6) from its canonical report gives

`||p_Q||infinity <= (C5+C18)/(2-1/2)`                       (6.3)

with

`C5=5sqrt(2e)=11.658219907985622...`,

`C18=2sqrt(108pi)=36.839761486073584...`,                   (6.4)

hence exactly

`boxed: ||p_Q||infinity <=32.331987596039475...`.            (6.5)

The partner theorem is therefore not merely cited: its actual inequality is instantiated on an explicit arbitrary-cardinality spectral-replacement family.

## 7. Forbidden shortcut explicitly avoided

The tail bound `||W+R||op<=h+delta` is **not** used to claim that `X^T(W+R)X` is a small random variable. Such a claim is false on unbounded translated inputs. The norm enters only through the partner theorem's deterministic Weyl stability of an actual original-coordinate physical block/cross certificate.

Likewise, no random vector is rotated to the eigenbasis of `E`; the spectral decomposition is used only to decompose the deterministic matrix. All probabilistic conditioning in the partner theorem remains on original independent coordinates.

## 8. Remaining full-target gap

The theorem solves a stability/reduction problem, not the unrestricted conjecture. The bare hypothesis `s3(A)>=1` still does not guarantee a physical core `H` and split `H=I disjoint_union J` for which the reserve

`s_(2r_H(h)+11)(D) > 2(h+delta)`                             (8.1)

holds at some useful threshold `h`. Diffuse exact-rank-three and grouped-bank correction families forbid simply asserting a universally good bounded physical core.

The next structural implication suggested by this theorem is therefore:

> In the no-pivot/no-D5 survivor class, either find a physical bank on which the large spectral window has low restriction rank relative to complementary reserve, or prove that failure at every spectral threshold forces one of the already-paid ridge, grouped-bank/hub, cross-volume, scalar-Schur, or aggregate product-preserving exits.

A particularly natural quantity is the multiscale ratio

`r_H(h)` versus `s_(2r_H(h)+11)(D)-2h`.                     (8.2)

A universal positive lower bound for this quantity on some product-preserving physical decomposition would close the added-eigenvalue bookkeeping step, but such a structural extraction is not proved here.
