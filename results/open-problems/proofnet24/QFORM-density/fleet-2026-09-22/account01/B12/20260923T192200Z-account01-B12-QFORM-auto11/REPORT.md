# account01/B12 — local physical-footprint inertia stability

Run: `20260923T192200Z-account01-B12-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Additional eigenvalue control  
Claim: `QFORM-LOCAL-PHYSICAL-FOOTPRINT-INERTIA-SQUARE-STABILITY-v1`  
Status: **PROVED SUPPORTING STABILITY THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED.**  
Regularity: the concrete application below proves an essentially bounded density through the designated partner's six-mode carrier theorem; continuity is **not claimed** for that theorem as a whole.

## 1. Exact target and first unpaid implication

The owner target is: for every dimension, independent real inputs whose scalar densities are bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal `L^infinity` density bound for `Q=X^TAX`, or produce a valid counterexample. No moments, compact support, log-concavity, iid hypothesis, or independence after a spectral rotation may be inserted.

For this B12 assignment the first unpaid implication is structural. If one starts with a useful original-coordinate spectral-square carrier and then adds many additional positive or negative eigenvalues, can the carrier be protected without pretending the resulting random quadratic remainder is independent? This run proves a sharper deterministic answer: an arbitrarily large signed symmetric addition costs, at a fixed physical carrier, only the dimension of its **local physical footprint** there. In particular the destructive square-energy loss is one reserve direction per local footprint direction, not two directions per global rank as in the earlier Krylov-rank argument.

## 2. Designated partner result actually used

I read and use the newest compatible completed `account02/B12` report:

`yspennstate/math-open-problems@c635fcdce6aa206c68f1f14e061cf617d72376fb`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/account02-B12-20260923T185321Z-r11/REPORT.md`.

Its Theorem 4.1 says that if `H` is a set of `m>=6` ORIGINAL coordinates and the actual final symmetric matrix `A` satisfies

`lambda_6((A^2)[H,H]) >= g^2 > 0`,

then every independent cap-one product source has an essentially bounded quadratic-form density satisfying

`||p_(X^TAX)||_infinity <= C_m/g`,

where, with `N_2=binom(m,2)`,

`C_m=max{ 8 N_2 sqrt(6 pi m), 4 pi N_2, 3*400^(1/3)*(4N_2)^(5/6), 10 sqrt(2e/3) }`.

The theorem is an exhaustive combination of an actual-final-cross-block D5 receiver, an original-coordinate projected-gradient receiver, and a physical-pair receiver. It does **not** claim continuity for the theorem as a whole. I apply this theorem below to an actual inequality produced by the new local-footprint lemma.

## 3. New theorem: local physical footprint controls destructive square inertia

Let `A_0,S` be arbitrary real symmetric `n x n` matrices. Let `H` be any set of original coordinates, let `P=P_H` be its coordinate projection, and set `m=|H|`. Define

`B=A_0+S`

and the local physical footprint dimension

`r_H(S)=rank(SP)=rank(PS)`.

(The two ranks agree because `(SP)^T=PS`.)

### Theorem 3.1 — local-footprint square stability

For every `k` with `k+r_H(S)<=m`,

`boxed: lambda_k((B^2)[H,H]) >= lambda_(k+r_H(S))((A_0^2)[H,H]).`      (3.1)

No assumption is made on the sign, rank, norm, spectrum, or commutation properties of `S`.

### Proof

Write the exact square difference

`D=B^2-A_0^2=A_0S+SA_0+S^2`.                                  (3.2)

Inside the physical carrier define

`K={x in Ran(P): Sx=0}`.                                       (3.3)

The restriction `S|_(Ran P)` has rank `r=r_H(S)`, hence

`dim K=m-r`.                                                    (3.4)

For every `x,y in K`, symmetry of `S` gives

`x^T D y`
` = x^T A_0 S y + x^T S A_0 y + x^T S^2 y`
` = 0 + (Sx)^T A_0 y + (Sx)^T S y`
` = 0`.                                                        (3.5)

Thus `K` is a totally isotropic subspace for the symmetric compression

`D_H=PDP |_(Ran P)`.                                           (3.6)

We use the following elementary inertia fact.

**Lemma 3.2.** If a real symmetric operator `M` on an `m`-dimensional space has a subspace `K` of codimension `r` with

`x^T M y=0` for all `x,y in K`,                                (3.7)

then both the positive and negative inertia of `M` are at most `r`.

Indeed, if the positive spectral subspace `E_+` had dimension `>r`, then `E_+ intersect K` would contain a nonzero vector `x`. Positivity on `E_+` gives `x^TMx>0`, while (3.7) gives `x^TMx=0`, a contradiction. The negative case is identical.

Apply Lemma 3.2 to `D_H`. Its negative part

`N=(-D_H)_+`                                                     (3.8)

has rank at most `r`. Since `D_H >= -N`,

`(B^2)[H,H] = (A_0^2)[H,H] + D_H`
`            >= (A_0^2)[H,H] - N`.                             (3.9)

A rank-`r` negative Hermitian perturbation can lower the `k`-th decreasing eigenvalue no further than the `(k+r)`-th original eigenvalue:

`lambda_k(G-N) >= lambda_(k+r)(G)`                              (3.10)

whenever `N>=0`, `rank N<=r`, and `k+r<=m`. Taking `G=(A_0^2)[H,H]` proves (3.1). QED.

### Why this improves the earlier global-rank/Krylov compiler

The raw difference (3.2) can have rank `2 rank(S)` even when `rank(S)=1`; for example

`A_0=[[0,1],[1,0]],  S=t[[1,0],[0,0]]`

has

`D=[[t^2,t],[t,0]]`,

which has rank two for `t != 0`. The previous safe argument therefore paid a two-step Krylov footprint. The new argument observes that the **negative inertia**, rather than the full rank of `D`, is what matters for lower spectral-square bounds. In the same example `det D=-t^2<0`, so there is exactly one negative eigenvalue. Thus the one-direction loss in (3.1) is in general sharp even though the full square perturbation has rank two.

## 4. Arbitrary dense small remainder

Let now

`A=B+R=A_0+S+R`,

with `R=R^T` and `||R||_op<=epsilon`. Since

`sqrt(lambda_k((M^2)[H,H])) = s_k(MP)`                          (4.1)

for the nonzero singular values, ordinary singular-value Weyl gives

`s_k(AP) >= s_k(BP)-||(A-B)P||_op`
`        >= s_k(BP)-epsilon`.                                  (4.2)

Combining (3.1) and (4.2),

`boxed:`
` sqrt(lambda_k((A^2)[H,H]))`
` >= ( sqrt(lambda_(k+r_H(S))((A_0^2)[H,H])) - epsilon )_+.`    (4.3)

The dense `R` is paid only through its deterministic matrix norm. No claim is made that `X^TRX` is a small random variable; with arbitrary unbounded cap-one source densities such a claim would be invalid.

## 5. Threshold compiler for arbitrary added eigenvalues of either sign

Let an arbitrary symmetric spectral addition be

`E=sum_j theta_j v_j v_j^T`,                                   (5.1)

where the `v_j` are orthonormal and the real `theta_j` have unrestricted signs and magnitudes. For a threshold `h>=0`, split

`S_h=sum_(|theta_j|>h) theta_j v_j v_j^T`,
`W_h=sum_(|theta_j|<=h) theta_j v_j v_j^T`.                    (5.2)

Then

`||W_h||_op<=h`.                                                (5.3)

Let `T=T^T` be any further full dense symmetric remainder with `||T||_op<=delta`, and set

`A=A_0+E+T`.

For an original-coordinate carrier `H`, define

`r_H(h)=rank(S_h P_H)`.                                        (5.4)

Applying (4.3) with `S=S_h` and `R=W_h+T` yields, whenever `k+r_H(h)<=|H|`,

`boxed:`
` sqrt(lambda_k((A^2)[H,H]))`
` >= ( sqrt(lambda_(k+r_H(h))((A_0^2)[H,H])) - h - delta )_+.` (5.5)

This is the requested additional-eigenvalue reduction. All eigenvalues with modulus larger than `h` may be positive or negative, arbitrarily numerous, and arbitrarily large; **their amplitudes disappear completely**. Their only charge is the dimension of the subspace they create when the added operator acts on the original-coordinate carrier. Every remaining eigenvalue, of either sign and arbitrary orientation/multiplicity, costs only the single operator threshold `h`. The statement is entirely deterministic and never rotates the random vector.

A useful geometric reformulation is

`r_H(h)=dim(S_h(Ran P_H))`.                                    (5.6)

Thus global rank can be enormous while the carrier charge is one. This can happen for many orthogonal spectral directions whose restrictions to `H` are all collinear.

## 6. Exact target-class family with arbitrarily many unbounded signed additions

This section applies the designated account02/B12 result to a concrete inequality.

Fix any integer `q>=1`. Let `H` be seven original coordinates and let the outside space have dimension `q`. Put

`A_0=2P_H = diag(2 I_7,0_q)`.                                  (6.1)

Let `e_1` be the first coordinate vector in `H`. Set

`alpha=1/sqrt(2q)`.                                            (6.2)

Choose vectors `w_1,...,w_q` in the outside `R^q` whose Gram matrix is

`<w_i,w_j> = delta_ij-alpha^2`.                                (6.3)

Such vectors exist because

`G=I_q-alpha^2 11^T`

has eigenvalues `1` with multiplicity `q-1` and `1-q alpha^2=1/2` in the all-ones direction, hence `G>0`.

Define

`v_j=alpha e_1 + w_j`.                                         (6.4)

Then

`<v_i,v_j>=alpha^2+delta_ij-alpha^2=delta_ij`,                 (6.5)

so the `v_j` are orthonormal. For completely unrestricted amplitudes

`tau_1,...,tau_q in R`,                                        (6.6)

set

`S_tau=sum_(j=1)^q tau_j v_jv_j^T`.                            (6.7)

For `x in Ran P_H`,

`S_tau x = alpha x_1 sum_j tau_j v_j`.                         (6.8)

Consequently

`rank(S_tau P_H)<=1`                                           (6.9)

for **every** number `q` of added modes and every simultaneous signed choice of their amplitudes, however large.

Now add an arbitrary symmetric small spectral cloud `W` and an arbitrary full symmetric dense tail `T`, with

`||W||_op<=1/8,   ||T||_op<=1/8`.                              (6.10)

Set

`A=A_0+S_tau+W+T`.                                             (6.11)

Since

`(A_0^2)[H,H]=4I_7`,                                           (6.12)

Theorem 3.1 followed by (4.3), with `k=6`, `r_H<=1` and `epsilon<=1/4`, gives the actual final-matrix inequality

`boxed: sqrt(lambda_6((A^2)[H,H])) >= 2-1/4 = 7/4.`            (6.13)

Equivalently,

`lambda_6((A^2)[H,H]) >= 49/16`.                              (6.14)

This is precisely the hypothesis of the designated partner's six-mode theorem with

`m=7,  g=7/4`.                                                 (6.15)

For `m=7`, `N_2=21`, and the four partner constants are

`8 N_2 sqrt(6 pi m) = 1929.7847196790035...`,
`4 pi N_2             = 263.89378290154264...`,
`3*400^(1/3)*(4N_2)^(5/6) = 887.23906785811...`,
`10 sqrt(2e/3)         = 13.461752804294704...`.               (6.16)

Therefore

`C_7=1929.7847196790035...`

and

`boxed: ||p_(X^TAX)||_infinity <= C_7/(7/4)`
`       = 1102.734125530859... < 1103.`                        (6.17)

This is uniform in `q`, all `tau_j`, every admissible `W,T`, and every independent cap-one input law.

### Verification of the owner's global spectral hypothesis

Let

`K=span{e_2,...,e_7}`.                                         (6.18)

For every `x in K`, `v_j^Tx=0`, hence `S_tau x=0`, while `A_0x=2x`. Thus `A_0+S_tau` has the exact eigenvalue `2` on the six-dimensional reducing subspace `K`. It follows that

`s_6(A_0+S_tau)>=2`,                                           (6.19)

so in particular `s_3(A_0+S_tau)>=2`. By singular-value Weyl and (6.10),

`boxed: s_3(A)>=2-1/4=7/4>1.`                                 (6.20)

Hence every member of this family lies literally inside the owner's exact target class. The example is not merely a local-block toy model.

## 7. Why this does not prove the full conjecture

The theorem solves a genuine additional-eigenvalue stability issue, but the unrestricted target remains open. Starting only from

`s_3(A)>=1`,

we do not yet know how to force an original-coordinate set `H` for which a six-mode square carrier survives after paying the local footprint `r_H(h)`, nor have we proved that failure of every such carrier necessarily produces one of the already-paid exact-cross-rank/D5/ridge/grouped-bank/hub/physical-pair/core/half-Riesz/Schur exits.

The missing implication can be stated sharply as a product-preserving extraction/dichotomy problem:

> From `s_3(A)>=1`, either produce `H,h` with `6+r_H(h)<=|H|` and a universal lower bound on `lambda_(6+r_H(h))((A_0^2)[H,H])^(1/2)-h`, for a useful decomposition `A=A_0+E`, or force a different completed original-coordinate receiver.

Nothing in Theorem 3.1 supplies this extraction automatically. Exact rank-three matrices already show that a universal six-mode carrier cannot be demanded without alternate branches.

## 8. Scope checks against the live corrections

1. No spectral change of variables is applied to `X`; independence is used only by the partner's already completed original-coordinate receiver.
2. No pointwise van-der-Corput bound for arbitrary bounded densities is used.
3. No arbitrary-joint coarea or projection-density shortcut is used.
4. No fiber-supremum argument is used.
5. The dense tail is controlled only in deterministic matrix inequalities, never by claiming `X^TTX` is small or independent.
6. No Gaussian, log-concavity, support, iid, moment, or connected-support assumption is introduced.
7. Repeated eigenvalues are irrelevant to the proof.
8. The numerical constant in (6.17) is arithmetic from the proved partner formula, not Monte Carlo evidence.

## 9. New mathematical payload and next step

**New proved payload:** the negative inertia of the physical compression of

`(A_0+S)^2-A_0^2`

is at most `rank(SP_H)`. This reduces the reserve loss for arbitrary signed additions from a two-step/global rank charge to a one-step **local physical footprint** charge.

**Next step:** combine this one-sided inertia compiler with a structural extraction lemma that selects `H` so that a globally complicated high-amplitude spectral packet has small `rank(S_hP_H)` relative to a baseline square reserve, while the complementary case forces an exact-cross-rank or localized pair/core receiver.

## 10. Provenance and operational scope


A narrow pre-write privacy review found only mathematical statements, repository names/paths, public commit identifiers, run identifiers, and nonsecret operational status. No credentials, tokens, signed download URLs, scheduler IDs, private source excerpts, machine paths, or personal data are included. No installation, scheduler, notification, email, permission, visibility, public-release, paid-model/API, cross-account-authentication, or remote-workflow changes were made.
