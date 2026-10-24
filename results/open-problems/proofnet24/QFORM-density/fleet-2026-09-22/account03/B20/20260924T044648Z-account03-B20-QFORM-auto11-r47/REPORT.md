SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-24T04:46:48Z.
attacking: the r49 four-latent / six-physical survivor by coupling an indefinite physical pair to a disjoint third cross singular through quarter-Riesz logarithmic smoothing; then record the resulting punctured-rank-two obstruction.

# account03/B20 r47 — indefinite-pair + third-cross quarter smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW TARGET-LEVEL BRANCH RECEIVER / r49 FRONTIER NARROWED / FULL QFORM OPEN**  
Execution memory: **WITHOUT_VERIFIED_BRAIN**. Repository transport is not native learned-memory ingestion.  
Continuity: **not proved for the new receiver**; the result below is an essential `L^infinity` density bound.

All coordinates below are literal ORIGINAL coordinates. No random variable is rotated. No Gaussian, moment, compact-support, connected-support, log-concavity or iid assumption is used. No small nonzero coefficient tail is removed.

## 1. Fresh source-pinned frontier

The current assembly source is account03/B19 r49:

`yspennstate/math-open-problems@35b71af9bbf9feb9542681486f190155c71ff247`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T040014Z-account03-B19-QFORM-r49/REPORT.md`.

Its active strong-rank-two chamber has disjoint original-coordinate banks `R,C`,

`N=A[R,C]`,

`dist_F(N,rank<=2)<2^-16`,

`sigma_2(N)>=1/64`,

and in the common-plane/no-large-light-star subbranch the exact active coefficient matrix is

`A[R union C,R union C]
 = diag(q)+K_16+(E_R direct_sum E_C)+T_cross`,

with

`rank K_16<=16`,

`||T_cross||_F<sqrt(2) 2^-16`,

while the `|lambda|>=1/2` spectral projections of each self residual `E_R,E_C` have physical leverage `<1/32`.  The full target remains open at the coupled-payment step; in particular neither the residuals nor `T_cross` may be discarded.

Two source-valid analytic inputs are used below.

1. The physical indefinite-pair envelope from the pair-log report

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For an invertible indefinite physical pair `B`, with `D=|det B|` and `kappa=sigma_min(B)`, after completing the pair the full conditional pair density obeys for every `r>0`

`p(t) <= 2 sqrt(2)/r
        + D^(-1/2) E log_+(2r^2/(kappa |t-R|))`.                 (1.1)

The pair shifts may depend arbitrarily on the remaining ORIGINAL variables.

2. The completed designated partner account04/B20 r3 result

`yspennstate/math-open-problems@25ad8faaac5064b6814d51ae63d894fe97c1eac4`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260922T172057Z-account04-B20-QFORM-r3/REPORT.md`.

Its Lemma 5.1 (`QFORM-LOG-TO-QUARTER-TRANSFER-v1`) says that if

`sup_s E|W-s|^(-1/4) <= L`,                                      (1.2)

then for every `delta>0`,

`sup_s E Psi((W-s)/delta) <= 6 delta^(1/4) L`,                   (1.3)

where `Psi(u)=1+log(1/|u|)` for `0<|u|<=1` and `Psi(u)=|u|^-1/4` for `|u|>=1`.

The quarter-Riesz input used by that report, from account01/B19, is: if a quadratic-affine form on independent ORIGINAL coordinates has a physical cross block with top singular value `sigma`, arbitrary same-bank quadratic blocks and affine terms are allowed and

`sup_s E|W-s|^(-1/4) <= B_1 sigma^(-1/4)`,                       (1.4)

`B_1=(2+sqrt(pi))(4e)^(1/4)=6.8503467322...`.

## 2. A rank-two Schur correction cannot erase a third physical cross singular

Let the selected physical pair be `I={i,j}` and write, after reordering coordinates,

`A = [[B,C^T],[C,A_0]]`,                                         (2.1)

where `B` is `2x2`, symmetric, invertible and indefinite.  Its Schur complement is

`S=A_0-C B^(-1) C^T`.                                            (2.2)

Let `L,M` be disjoint subsets of the remaining physical coordinates. Then

`S[L,M]=A[L,M]-C_L B^(-1) C_M^T`.                                (2.3)

The second term has rank at most two. Therefore

`boxed: s_1(S[L,M]) >= s_3(A[L,M]).`                              (2.4)

Proof: for every matrix `G`, `s_3(G)=inf_{rank F<=2} ||G-F||_op`. Apply this with `G=A[L,M]` and `F=C_L B^(-1)C_M^T`. QED.

This is the key product-preserving observation: one may complete an arbitrary physical two-coordinate pair without losing *all* cross anti-concentration carried by a disjoint third singular direction.

## 3. New receiver: indefinite physical pair + disjoint third cross singular

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-THIRDCROSS-QUARTER-SMOOTHING-v1`

Let `X_1,...,X_n` be independent real random variables with densities at most one. Let `A=A^T`. Suppose two ORIGINAL coordinates form an invertible indefinite principal pair `B`, and put

`D=|det B|>0`, `kappa=sigma_min(B)>0`.                             (3.1)

Suppose that after deleting those two coordinates there are disjoint ORIGINAL-coordinate sets `L,M` such that

`s_3(A[L,M]) >= sigma >0`.                                        (3.2)

Then `Q=X^TAX` has an essentially bounded density and

`boxed:
||p_Q||_infinity
 <= C_pc D^(-1/3) kappa^(-1/6) sigma^(-1/6),`                    (3.3)

where

`C_pc = 3 (6 B_1)^(2/3) < 35.730`.                               (3.4)

Arbitrary affine terms and arbitrary coefficients on every other coordinate are allowed. No sign assumption is made outside the selected indefinite pair.

### Proof

Condition on any ambient coordinates outside the displayed principal block if desired; their couplings create only affine terms in the retained ORIGINAL coordinates. Write the pair variables as `x` and all remaining retained variables as `z`. Completing the pair gives

`Q=(x+m(z))^T B (x+m(z)) + R(z)`,                                (3.5)

where the quadratic coefficient matrix of `R` is exactly the Schur complement `S` in (2.2); the rest is affine/constant. For each fixed `z`, translating the two pair coordinates preserves their two scalar density caps and their independence.

By (2.4), the residual physical cross block `S[L,M]` has

`s_1(S[L,M]) >= sigma`.                                           (3.6)

Hence the source-valid quarter-Riesz theorem (1.4) applies to the *actual Schur remainder* `R`:

`sup_t E|R-t|^(-1/4) <= B_1 sigma^(-1/4)=:L`.                    (3.7)

Now apply the physical-pair envelope (1.1). Put

`delta=2r^2/kappa`.                                               (3.8)

Since

`log_+(delta/|u|) <= Psi(u/delta)`,                               (3.9)

the designated partner theorem (1.3), applied at the actual inequality (3.7), gives

`E log_+(2r^2/(kappa|t-R|))
 <=6 (2r^2/kappa)^(1/4) B_1 sigma^(-1/4)`.                       (3.10)

Thus, for every `r>0`,

`p_Q(t)
 <= A r^(-1) + C r^(1/2)`,                                      (3.11)

with

`A=2sqrt(2)`,

`C=6*2^(1/4) B_1 D^(-1/2) kappa^(-1/4) sigma^(-1/4)`.           (3.12)

The exact minimizer satisfies `r^(3/2)=2A/C`. At this value,

`min_{r>0} [A/r+C sqrt(r)]
 =3*2^(-2/3) A^(1/3) C^(2/3)`.                                  (3.13)

The powers of two cancel:

`2^(-2/3) * (2^(3/2))^(1/3) * (2^(1/4))^(2/3)=1`.               (3.14)

Substitution gives precisely (3.3)-(3.4). The conditional pair measures in the pair-log proof are absolutely continuous; Tonelli supplies an ambient density. Nothing in this argument proves continuity of the resulting representative, so only essential boundedness is claimed. QED.

## 4. Concrete all-small-diagonal gate relevant to r49

Assume the already-live all-small-diagonal collar

`|A_ii|, |A_jj| <= 1/64`                                         (4.1)

and suppose a physical edge satisfies

`|A_ij| >= 1/32`.                                                 (4.2)

Write `a=A_ii`, `b=A_jj`, `c=A_ij`. Then the pair is automatically indefinite because

`c^2-ab >= c^2-|ab| >= 1/1024-1/4096 =3/4096`.                  (4.3)

Therefore

`D>=3/4096`.                                                      (4.4)

Also, for a symmetric `2x2` indefinite matrix, `kappa=D/s_max(B)`. Since

`s_max(B) <= max row-sum <= |c|+1/64`,                            (4.5)

and

`D >= |c|^2-(1/64)^2=(|c|-1/64)(|c|+1/64)`,                     (4.6)

we obtain

`kappa >= |c|-1/64 >=1/64`.                                      (4.7)

Consequently, if after deleting this pair there is any disjoint physical cross block satisfying

`s_3(A[L,M]) >= 2^-16`,                                          (4.8)

Theorem 3.1 gives the fully explicit target-level bound

`boxed: ||p_Q||_infinity <5034.`                                 (4.9)

The computation is

`35.730*(3/4096)^(-1/3)*(1/64)^(-1/6)*(2^-16)^(-1/6)
 =5033.6924...`.

This branch allows every same-bank quadratic coefficient, all outside couplings, all signs, unbounded/fragmented cap-one input laws and arbitrary additional spectrum.

### Corollary 4.2 — the new punctured-rank-two obstruction

In any still-unpaid all-small-diagonal state, every physical edge with `|A_ij|>=1/32` must satisfy the following rigid alternative after its endpoints are punctured:

`boxed:
s_3(A[L,M])<2^-16
for every pair of disjoint remaining physical sets L,M,`          (4.10)

unless an already-paid branch applies.

Thus an entry-heavy physical pair can no longer coexist with an independent third cross singular even at the very small fixed scale `2^-16`. The remaining entry-heavy geometry is a genuinely punctured rank-two cross system, not an arbitrary higher-rank remainder.

## 5. Designated partner applied to the live r49 cross inequality

The current r49 main physical crossing obeys

`s_1(N)>=s_2(N)>=1/64`.                                          (5.1)

Applying the quarter-Riesz theorem (1.4) to the actual r49 active quadratic form, with all of its same-bank curvature retained, gives

`sup_s E|W-s|^(-1/4)
 <= B_1 64^(1/4)
 <19.376.`                                                        (5.2)

Now apply the completed account04/B20 log-to-quarter theorem at the concrete scale

`delta=2^-12`.                                                    (5.3)

It yields

`boxed:
sup_s E Psi((W-s)/2^-12)
 <=6*2^-3*B_1*64^(1/4)
 <14.532.`                                                        (5.4)

This is a real inequality on the live strong-rank-two survivor, not a generic restatement. It does **not** by itself prove a density bound; its role is the exact logarithmic smoothing reserve used in Theorem 3.1 whenever an indefinite physical pair is exposed without destroying all third-cross currency.

## 6. What this closes, and the first remaining implication

For the r49 four-latent / six-physical chamber, the new receiver removes the following entire subcase:

- an entry-heavy physical pair (`|A_ij|>=1/32`) in the all-small-diagonal collar; and
- any disjoint post-puncture physical cross block with third singular value at least `2^-16`.

Such a state has an essentially bounded density with universal bound `<5034`.

Therefore the first still-unpaid implication on this route is sharpened to

`QFORM-R49-PUNCTURED-R2-OR-AGGREGATE-DIFFUSE-PAYMENT-v1`:

> in the r49 survivor, pay the state in which every entry-heavy physical pair leaves only `s_3<2^-16` on every disjoint punctured cross block, together with the entry-diffuse branch where all physical edges are `<1/32`; retain both diffuse self residuals, the genuine `2^-16` cross tail, arbitrary same-bank curvature, outside couplings and extra spectrum.

A natural next deterministic step is a dimension-free gluing theorem for the punctured rank-two system: either its varying rank-two cross planes align into a bounded-rank physical carrier, or failure of alignment generates a disjoint third cross singular and returns to Theorem 3.1 / the existing physical-`E3` receiver.

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**.

## 7. Integrity / corrections

This proof never uses law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, conditional projection-density moments, post-rotation independence, interval extremality, Monte Carlo certification, or deletion of a nonzero coefficient tail. Repeated eigenvalues cause no issue. The new theorem is sign-free outside the explicitly indefinite pair.

A quick literature search during this run found standard maximum-density/rearrangement results for sums of independent bounded-density variables, but no source matching Theorem 3.1 or the unrestricted QFORM target; no published-theorem closure is claimed.
