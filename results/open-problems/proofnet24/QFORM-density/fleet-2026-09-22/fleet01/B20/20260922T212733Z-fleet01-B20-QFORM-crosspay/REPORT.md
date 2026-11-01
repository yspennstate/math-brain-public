SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-22T21:27:33.980639Z.
attacking: fleet02/B20 r19's first unpaid implication — pay the opposite-sign two-pivot state with a fixed-scale residual Schur cross bank while keeping original-coordinate product provenance.

# fleet01/B20 — strong Schur-cross payment after two physical pivots

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed:** revision `2026-09-22.15`  
**Run:** `20260922T212733Z-fleet01-B20-QFORM-crosspay`  
**Classification:** `ESSENTIAL_STEP_APPLIED / OPPOSITE-PAIR-STRONG-SCHUR-CROSS-PAID / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not proved by this argument; this report proves an essential-boundedness payment on the stated branch only.

## 1. Exact target and correction boundary

The parent target remains: for every finite `n`, every independent real family `X_1,...,X_n` with probability densities bounded by one, and every real symmetric `A` with `s_3(A)>=1`, prove that `Q=X^T A X` has a density whose essential supremum is bounded by one universal finite constant, or give a target-valid counterexample.

No Gaussianity, moment, iid, compact-support, connected-support, log-concavity, or post-rotation independence is used. In particular this proof does **not** use the refuted law-uniform pointwise quadratic oscillatory decay, an unrestricted fiber supremum, a conditional density cap after exposing a dependent rotated statistic, or a single-cross-minor payment with uncontrolled same-side curvature.

## 2. Completed fleet02/B20 result actually consumed

The designated completed partner result is fleet02/B20 run

`20260922T210111Z-fleet02-B20-QFORM-r19`,

canonical mathematics

`yspennstate/math-open-problems@e004778aef69cbf704ab9ccfb216a6f9bbba327b`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260922T210111Z-fleet02-B20-QFORM-r19/REPORT.md`.

On the validated two-pivot survivor it gives successive **physical scalar Schur pivots** `i,p` with

`a=A_ii`,

`S=A_{-i,-i}-A_{-i,i}A_{i,-i}/a`,

`d=S_pp`,

and exact second Schur complement `T` on the untouched ORIGINAL coordinates, satisfying

`a d<0`,

`|a|>=m:=3501/8000`,

`|d|>1/8`.                                                    (2.1)

It further proves `||T||_op>=s_3(A)>=1`. Its physical-third-diagonal alternative is already paid. In every remaining state it produces a nontrivial original-coordinate cut

`R=L disjoint_union K`

with

`beta:=s_1(T[L,K])>1/4`.                                     (2.2)

Equivalently the original-matrix bordered-minor packet satisfies `Delta_jk=a d T_jk`, but the present proof will pay (2.2) directly before any reciprocal minor extraction.

The precise unpaid statement in that report is `QFORM-OPPOSITE-PAIR-STRONG-SCHUR-CROSS-PAYMENT-v1`. This report closes it.

## 3. Source-valid one-dimensional projection input

I use the standard sharp product-marginal consequence recorded and applied elsewhere in the QFORM programme:

> If `Y=(Y_1,...,Y_r)` has independent coordinates with scalar probability densities bounded by one and `c in R^r`, then the scalar linear form `c^T Y` has a density with
>
> `||p_{c^T Y}||_infinity <= C_P/||c||_2`, with `C_P=sqrt(2)`.   (3.1)

A source-pinned programme proof is fleet03/B18, scientific snapshot `yspennstate/math-open-problems@313aaf988145f63be448447eaf661aa399772088`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/B18-20260922T155856Z-r13/REPORT.md`, which cites and applies Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Theorem 1.1. This is a bound on one physical-source linear functional; it does not declare rotated coordinates independent.

For transparency I carry `C_P` through the proof and only substitute `C_P=sqrt(2)` at the end.

## 4. Exact triangular square representation and provenance

Order the physical coordinates as `(i,p,R)`. Two ordinary scalar square completions give the exact identity

`Q = a U^2 + d V^2 + Z^T T Z`,                          (4.1)

where `Z=X_R` consists of the untouched original coordinates,

`V = X_p + d^{-1} S_{pR} Z`,                              (4.2)

and `U` is `X_i` plus a deterministic affine function of `(X_p,Z)` obtained from the first Schur completion.

The only probabilistic facts needed from (4.1) are triangular and remain in original coordinates:

1. conditional on `Z`, `V` is a translation of the original physical coordinate `X_p`, hence its conditional density is at most one;
2. conditional on `(X_p,Z)`, `U` is a translation of the original physical coordinate `X_i`, hence its conditional density is at most one;
3. after integrating the pivot coordinates, `Z` retains the original independent cap-one product law.

No independence is asserted between the shifted variables `U,V` and `Z`.

Put

`R_0:=Z^T T Z`,

`W:=d V^2+R_0`,

so `Q=aU^2+W`.

The proof has three steps: rank-one cross-bank decoupling gives a quarter-power small-ball bound for `R_0`; the second physical square raises the exponent to `3/4`; the first physical square then spends the resulting half-Riesz integrability.

## 5. Lemma 1 — one strong cross singular value gives a quarter-power residual small-ball bound

### Lemma 5.1 — `QFORM-RANK1-CROSS-QUARTER-SMALLBALL-v1`

Let `Z` have independent cap-one physical coordinates, let `T` be real symmetric, and let `L,K` be disjoint physical banks with

`B:=T[L,K]`, `s_1(B)>=beta>0`.

Then for every `h>0`,

`L_{R_0}(h):=sup_t P(|Z^T T Z-t|<=h)`

satisfies

`L_{R_0}(h) <= min(1, K_0 h^(1/4))`,                       (5.1)

where

`K_0 = 2 sqrt(C_P) beta^(-1/4)`.                           (5.2)

For `C_P=sqrt(2)`, this is

`K_0=2^(5/4) beta^(-1/4)`.                                 (5.3)

#### Proof

Write the remaining residual coordinates as `(X_L,X_K,X_O)`. Take an independent copy `X_L'` of the **original physical bank** `X_L`, keeping `(X_K,X_O)` common. For a fixed interval event

`E={|R_0-t|<=h}`,

Cauchy--Schwarz/Jensen conditional on `(X_K,X_O)` gives

`P(E)^2 <= P(|R_0(X_L,X_K,X_O)-R_0(X_L',X_K,X_O)|<=2h)`.  (5.4)

Let `D=X_L-X_L'`. After conditioning on `(X_L,X_L',X_O)`, every term in the difference is constant except the cross interaction with `X_K`; the difference is

`c + 2 D^T B X_K`                                           (5.5)

for a conditioned scalar `c`. By (3.1), the conditional probability in (5.4) is at most

`min(1, 2 C_P h / ||B^T D||_2)`.                           (5.6)

Choose a unit left singular vector `u` for `s_1(B)`. Then

`||B^T D||_2 >= beta |u^T D|`.                             (5.7)

Let `S=u^T D`. The scalar `u^T X_L` has density at most `C_P`; its independent difference `S` therefore also has density at most `C_P` (convolution does not increase the `L^infinity` norm). With

`r:=2 C_P h/beta`,

for every `delta>0`,

`E min(1,r/|S|)
 <=P(|S|<=delta)+r/delta
 <=2 C_P delta+r/delta`.                                    (5.8)

Choosing `delta=sqrt(h/beta)` gives

`E min(1,r/|S|) <=4 C_P sqrt(h/beta)`.                     (5.9)

Combining (5.4)--(5.9) and taking a square root proves

`P(E)<=2 sqrt(C_P) (h/beta)^(1/4)`,

which is (5.1)--(5.2). QED.

The key point is that a **single** singular direction is enough here because it is paid before the square-root decoupling exponent is asked to become integrable; the second genuine physical square will supply the missing exponent.

## 6. Lemma 2 — a physical square raises the exponent from 1/4 to 3/4

First record the elementary slab measure. For `d!=0`, every real `c` and `h>0`,

`Leb{v: |d v^2-c|<=h}
 <= 4h / [sqrt(|d|) sqrt(max(h,|c|))]`.                     (6.1)

For `|c|<=h`, the left side is at most `2 sqrt(2h/|d|)`, which is below the right side. For `c` of the sign of `d` and `|c|>h`, subtract the two square roots; for the opposite sign the set is empty once `|c|>h`.

Apply (6.1) conditionally on `Z`. Since `V|Z` has density at most one,

`P(|W-t|<=h)
 <= (4h/sqrt(|d|)) E[max(h,|t-R_0|)^(-1/2)]`.              (6.2)

Let `F_t(r)=P(|R_0-t|<=r)`. Lemma 5.1 says

`F_t(r)<=min(1,K_0 r^(1/4))`.                              (6.3)

Set

`h_0:=K_0^(-4)=beta/(16 C_P^2)`.                           (6.4)

For `0<h<=h_0`, the exact layer-cake identity

`E[max(h,|t-R_0|)^(-1/2)]
 =(1/2) integral_h^infinity r^(-3/2) F_t(r) dr`             (6.5)

and (6.3) imply

`E[max(h,|t-R_0|)^(-1/2)]
 <=2 K_0 h^(-1/4)`.                                         (6.6)

Indeed, integrating `K_0 r^(1/4)` from `h` to `h_0` and `1` above `h_0` gives the slightly sharper value `2K_0 h^(-1/4)-K_0^2`.

Substitution into (6.2) proves

`L_W(h):=sup_t P(|W-t|<=h)
 <=8 K_0 |d|^(-1/2) h^(3/4),    0<h<=h_0`.                 (6.7)

Thus the second genuine physical square has upgraded the residual exponent from `1/4` to `3/4`, crossing the half-Riesz threshold.

## 7. Lemma 3 — uniform half-Riesz payment for the inner residual

For every `t`, another layer-cake identity gives

`E|W-t|^(-1/2)
 =(1/2) integral_0^infinity h^(-3/2) P(|W-t|<h) dh`.        (7.1)

Use (6.7) on `(0,h_0]` and the trivial probability bound one above `h_0`. The first integral is

`(1/2) integral_0^{h_0} h^(-3/2)
          8K_0 |d|^(-1/2) h^(3/4) dh
 =16 |d|^(-1/2)`,                                           (7.2)

because `h_0^(1/4)=K_0^(-1)`. The tail is

`(1/2) integral_{h_0}^infinity h^(-3/2) dh
 =h_0^(-1/2)=K_0^2`.                                        (7.3)

Therefore

`boxed:
 sup_t E|W-t|^(-1/2)
 <=16 |d|^(-1/2) + 4 C_P beta^(-1/2).`                      (7.4)

For `C_P=sqrt(2)`, the second term is `2^(5/2) beta^(-1/2)`.

## 8. Main theorem — the fleet02/B20 r19 strong-cross branch is paid

### Theorem 8.1 — `QFORM-OPPOSITE-PAIR-STRONG-SCHUR-CROSS-PAYMENT-v1`

Assume the two physical pivots and untouched-original-coordinate cut supplied by fleet02/B20 r19, or more generally assume the exact triangular representation (4.1) with `a,d!=0` and

`s_1(T[L,K])>=beta>0`.

Then the full ambient quadratic form has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= |a|^(-1/2)
    [16 |d|^(-1/2) + 4 C_P beta^(-1/2)].`                  (8.1)

#### Proof

Conditioned on all residual physical coordinates `(X_p,Z)`, `U` is a translate of the original cap-one variable `X_i`. Consequently the conditional density of `aU^2` at nonzero displacement `y` is at most

`|a|^(-1/2)|y|^(-1/2)`.                                    (8.2)

Equivalently, conditioning only on `W` is also safe: the conditional law of `U|W` is a mixture of translations of `X_i`, so its density is still at most one. Averaging (8.2) over `W` yields

`p_Q(t) <= |a|^(-1/2) E|t-W|^(-1/2)`                       (8.3)

for almost every `t`. Apply (7.4). QED.

Note that the sign condition `ad<0` is not used analytically in this last payment; it is part of the partner's structural route identifying the surviving branch.

## 9. Actual numerical payment of the partner inequalities

Now insert the **actual fleet02/B20 r19 inequalities**

`|a|>=m=3501/8000`,

`|d|>1/8`,

`beta=s_1(T[L,K])>1/4`,

and `C_P=sqrt(2)` into (8.1). Then

`16|d|^(-1/2) <16 sqrt(8)=32 sqrt(2)`,

`4 C_P beta^(-1/2) <4 sqrt(2)*2=8 sqrt(2)`.

Hence

`boxed:
 ||p_Q||_infinity
 <40 sqrt(2/m)
 =40 sqrt(16000/3501)
 =85.51138237264878... <85.512.`                            (9.1)

This directly pays the first unpaid implication named in the completed fleet02/B20 r19 report. In particular, its physical-third-diagonal alternative was already bounded by `<386.981`, while its complementary strong residual Schur cross-bank alternative is now bounded by `<85.512`.

A tiny arithmetic self-check is saved beside this report; it is not an independent mathematical audit.

## 10. Conditional end-to-end effect and remaining debt

On the fleet02/B20 r19 route the third spectral resource is now completely paid:

- if the second Schur complement `T` has a physical diagonal of magnitude at least `1/2`, the partner's physical-triple theorem pays the full ambient form;
- otherwise the partner produces `s_1(T[L,K])>1/4` on untouched original banks, and Theorem 8.1 pays the full ambient form with `<85.512`.

Thus `QFORM-OPPOSITE-PAIR-STRONG-SCHUR-CROSS-PAYMENT-v1` is no longer an unpaid implication.

This is **not** a proof of the full QFORM conjecture. The synthesis still has separately tracked structural debts outside the r19 low-leverage two-pivot survivor, notably high-leverage/strong-star or grouped-coordinate packets and the zero/near-isotropic physical-pivot branch. The next proof-closure task should route one of those surviving structural states into this now-paid two-square-plus-cross mechanism, a reviewed ridge/window packet, or another already-paid product-preserving packet.

Continuity remains separate: the argument above establishes existence and a uniform essential `L^infinity` bound on this branch, but I do not claim a continuous representative from the two dependent square-smoothing steps alone.

## 11. Status

**Classification:** `ESSENTIAL_STEP_APPLIED / OPPOSITE-PAIR-STRONG-SCHUR-CROSS-PAID / FULL_TARGET_OPEN`.

**New proved implication:** a rank-one residual physical cross bank becomes fully payable after two genuine nonzero physical scalar pivots; no rank-two cross singular value is needed in this branch.

**Partner result actually applied:** fleet02/B20 r19 inequalities (2.1)--(2.2), not merely cited.

**Corrections preserved:** no law-uniform pointwise quadratic oscillatory decay; no post-rotation independence; no arbitrary-joint coarea shortcut; no single cross minor with uncontrolled both-side curvature.

**Full QFORM:** OPEN / not proved / not disproved.
