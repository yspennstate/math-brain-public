# QFORM fleet02/B01 r24 — condition one heavy residual row, then diffuse; exact Pluecker cross-volume identity

Status: **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / proved supporting theorem / full target OPEN / WITHOUT_VERIFIED_BRAIN**.

Run: `20260922T162930Z-fleet02-B01-qform-r24`  
Programme: `QFORM-DENSITY-3EIG-20260922`.  
Current owner control observed before publication: revision `2026-09-22.7`, QFORM only, no B01 pause.  
Assignment: fleet02/B01 `Oscillatory replacement`, complementary constructions/source-valid counterexamples.  
Later owner request also applied: `QFORM-PROOF-FIRST-20260922T161801Z` — maintain a conditional end-to-end proof and attack its first unpaid implication.

## 1. Exact target and corrections retained

The target is unchanged: for every dimension, every independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove one universal finite bound for the essential supremum of the density of

`Q=X^T A X`,

or construct a valid counterexample. No moments, Gaussianity, log-concavity, compact or connected support, diagonal-basis hypothesis, or post-rotation independence is allowed.

The following live corrections are retained and not used as premises:

* law-uniform pointwise quadratic-phase decay is false by phase-aligned densities;
* absolute Fourier `L1` is not a necessary target interface;
* a uniformly good fixed cross minor or single local Schur packet is not forced by the three-large-eigenvalue hypothesis;
* bounded projected-pair density plus an unrelated conditional cap does not substitute for original product provenance;
* one heavy row plus one same-bank square does not by itself absorb arbitrary curvature (`QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1`);
* directly averaging same-sign Pluecker weights against a two-pivot local certificate can fail (`QFORM-PLUCKER-PIVOT-SUPPORT-DISJOINT-v1`).

The result below keeps an actually independent third physical square and conditions a heavy residual coordinate before applying the product-frame theorem. It therefore does not revive either of the last two refuted shortcuts.

## 2. Completed partner results actually applied

### 2.1 fleet03/B01 r12: diffuse rank-two `L^3` plus sharp dependence-safe square

Canonical source:

`yspennstate/math-open-problems@a80bb254a3a1e2883cbfabdf03b53919d6621990`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/20260922T142626Z-fleet03-B01-qform-r12/REPORT.md`.

It proves the following two facts used below.

First, if `T` is an `m x 2` frame with orthonormal columns and every row leverage at most `1/2`, `Gamma` is invertible symmetric, the coordinates are independent with density caps one, and arbitrary coordinatewise measurable potentials are allowed, then

`R=(T^T X)^T Gamma(T^T X)+sum_j V_j(X_j)`

has an `L^3` density with

`||p_R||_3 <= (3e)^(2/3) |det Gamma|^(-1/3)`.           (2.1)

Second, if `R` has an `L^3` density of norm `M`, and conditional on `R=r` a variable `V` has density at most one, then for every `d!=0`

`||p_{R+dV^2}||_infinity`
` <= [2 sqrt(pi)/3^(1/4)] |d|^(-1/2) M^(3/4)`.         (2.2)

No independence of `R` and `V` is required in (2.2).

### 2.2 fleet03/B01 r14: Schur rank-two cross-volume

Canonical source:

`yspennstate/math-open-problems@af5fc5be9cdae6d915c5d864c7cd398a2a1b95c5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260922T155128Z-r14/REPORT.md`.

After one physical scalar pivot, for a residual physical pair `I` with rank-two cross block `C=H[I,J]`, it defines

`s_I=sqrt(det(C C^T))`

and proves the essential-density bound

`||p_Q||_infinity`
` <= 2 sqrt(pi) 3^(1/4) C_RV^(1/2)`
`    |d|^(-1/2) s_I^(-1/4)`.                           (2.3)

I use (2.3) below on an exact target-valid stress family and show that **every** physical-pair certificate can deteriorate there, even though a grouped-coordinate conditioning repair gives a uniform-in-dimension bound.

## 3. New theorem: condition one heavy residual row, then apply the diffuse theorem

### Theorem 3.1 — `QFORM-CONDITION-ONE-HEAVY-ROW-v1`

Let `X_0,X_1,...,X_m` be independent real variables, each with a probability density bounded by one. Let `S` be an `m x 2` matrix with orthonormal columns, let `Gamma` be an invertible real symmetric `2 x 2` matrix, and let

`R=(S^T X)^T Gamma(S^T X)+sum_{j=1}^m V_j(X_j)`,       (3.1)

where the `V_j` are arbitrary measurable real functions for which the displayed random variable is defined.

Suppose the full form can be written

`Q=d (X_0 + M(X_1,...,X_m))^2 + R`, `d!=0`,            (3.2)

with arbitrary measurable shift `M`.

Choose one residual physical row `h`; write its row vector as `s_h` and

`c=|s_h|^2 <1`.

Delete that row and set

`G = S_{-h}^T S_{-h} = I_2-s_h s_h^T`.                 (3.3)

Assume the whitened remaining frame

`T=S_{-h} G^(-1/2)`                                    (3.4)

has every row leverage at most `1/2`.

Then `Q` has an essentially bounded density and

`boxed(
 ||p_Q||_infinity
 <= 2*3^(1/4)*sqrt(pi e)
    |d|^(-1/2) [(1-c)|det Gamma|]^(-1/4).
)`                                                       (3.5)

The numerical leading constant is

`2*3^(1/4)*sqrt(pi e)=7.6918797590...`.                 (3.6)

This is a genuine one-level grouped-coordinate extension of the diffuse rank-two-plus-square branch: the original residual frame itself may have a row of leverage greater than `1/2`; one conditions that physical coordinate, whitens the remaining product coordinates, and only then applies the diffuse theorem.

### Proof

Condition on `X_h=x`. Write `X_-` for the remaining residual physical coordinates. Since `S_{-h}=T G^(1/2)`,

`S^T X = s_h x + G^(1/2) T^T X_-`.                    (3.7)

Substitute (3.7) into the quadratic part of (3.1). Up to an additive constant depending only on `x`, the conditional residual equals

`R_x=(T^T X_-)^T Gamma_x (T^T X_-)`
`    + linear_x(T^T X_-) + sum_{j!=h} V_j(X_j)`,       (3.8)

where

`Gamma_x = G^(1/2) Gamma G^(1/2)`.                     (3.9)

The subscript `x` on `Gamma_x` is only mnemonic: the matrix in (3.9) does **not** depend on `x`; all `x`-dependence in (3.8) is linear or constant. A linear form in `T^T X_-` is a sum of one-coordinate linear potentials, so it lies exactly inside the arbitrary-coordinatewise-potential scope of the partner theorem (2.1).

By the matrix determinant lemma in dimension two,

`det G=det(I_2-s_h s_h^T)=1-|s_h|^2=1-c`.              (3.10)

Therefore

`|det Gamma_x|=(1-c)|det Gamma|`.                      (3.11)

The hypothesis on the whitened frame `T` allows direct application of (2.1), uniformly in the conditioned value `x`:

`||p_{R | X_h=x}||_3`
` <= (3e)^(2/3)[(1-c)|det Gamma|]^(-1/3).`             (3.12)

Now keep `x` fixed and set

`V=X_0+M(x,X_-)`.

Conditional on the finer variable `X_-`, `V` is a translate of the independent physical coordinate `X_0`, hence has density at most one. Conditioning further only on the coarser sigma-field generated by `R_x` produces a mixture of such translates, so

`||p_{V | R_x=r, X_h=x}||_infinity <=1`               (3.13)

for almost every `r`. Apply the partner's sharp dependence-safe square theorem (2.2) to (3.12):

`||p_{Q | X_h=x}||_infinity`
` <= [2 sqrt(pi)/3^(1/4)] |d|^(-1/2)`
`    * [(3e)^(2/3)((1-c)|det Gamma|)^(-1/3)]^(3/4)`
` = 2*3^(1/4)*sqrt(pi e)`
`   |d|^(-1/2)[(1-c)|det Gamma|]^(-1/4).`              (3.14)

The right side is independent of `x`. Averaging the conditional densities in `x` cannot increase the same essential supremum, proving (3.5). QED.

### What the theorem does and does not do

The theorem genuinely removes **one** heavy row from the residual diffuse hypothesis, at an exact determinant cost `(1-c)^(-1/4)`. It does not prove that `1-c` is universally bounded below, nor that the whitened tail is always diffuse. Iterated heavy-row peeling can make the surviving Gram determinant small; that is the next structural debt rather than an assumption silently discarded here.

## 4. Exact rank-two Pluecker formula for the partner cross-volume

The partner's quantity `s_I=sqrt(det(C C^T))` has a useful exact expression when the residual itself has rank two.

Let

`H=S Gamma S^T`, `S^T S=I_2`,                          (4.1)

and for each physical pair `I={j,k}` let `J` be its complement and

`C=H[I,J]`.

Write the row vectors of `S` as `s_j`, and define the nonnegative Pluecker weights

`w_jk = det(S[I,:])^2`.                                (4.2)

Let `c_j=|s_j|^2` be the row leverages.

### Lemma 4.1 — `QFORM-RANK2-PLUCKER-CROSSVOLUME-v1`

For every pair `{j,k}`,

`boxed(
 s_{jk}^2 := det(C C^T)
 = det(Gamma)^2 w_jk (1-c_j-c_k+w_jk).
)`                                                       (4.3)

Equivalently,

`boxed(
 s_{jk}=|det Gamma| sqrt(w_jk W_{complement(j,k)}),
)`                                                       (4.4)

where

`W_{complement(j,k)}`
` = sum_{p<q, p,q notin {j,k}} w_pq`
` =1-c_j-c_k+w_jk`.                                    (4.5)

Also

`sum_{j<k} w_jk=1`,                                    (4.6)

`sum_{k!=j} w_jk=c_j`.                                 (4.7)

#### Proof

Since

`C=S_I Gamma S_J^T`,

we have

`C C^T = S_I Gamma (S_J^T S_J) Gamma S_I^T`
`        =S_I Gamma (I_2-S_I^T S_I) Gamma S_I^T`.      (4.8)

Every matrix in (4.8) is `2 x 2`, so determinants multiply:

`det(C C^T)`
` =det(S_I)^2 det(Gamma)^2 det(I_2-S_I^T S_I).`        (4.9)

Now

`det(S_I)^2=w_jk`,

and for the `2 x 2` positive semidefinite matrix `S_I^T S_I`,

`det(I_2-S_I^T S_I)`
` =1-tr(S_I^T S_I)+det(S_I^T S_I)`
` =1-c_j-c_k+w_jk`.                                    (4.10)

This proves (4.3). Cauchy--Binet applied to `S` gives (4.6), and applied to the complement matrix `S_J` gives (4.5). Finally,

`sum_{k!=j} det(s_j,s_k)^2`
` = s_j^T [sum_k (|s_k|^2 I_2-s_k s_k^T)] s_j`
` =s_j^T[(tr I_2)I_2-I_2]s_j`
` =|s_j|^2=c_j`,

proving (4.7). QED.

Formula (4.4) is the exact boundary between a **single physical pair** and **grouped-coordinate** aggregation: the partner's pair certificate is large only when one pair carries both nontrivial Pluecker mass itself and leaves nontrivial Pluecker mass completely outside that pair.

## 5. Target-valid stress family: heavy localization does not force a good pair cross-volume

Fix any even `m>=4` and `0<epsilon<1/2`. Choose signs `sigma_r in {+1,-1}`, `r=1,...,m`, with exactly `m/2` of each sign. Define an `(m+1) x 2` frame by

`s_0=(sqrt(1-epsilon),0)`,                              (5.1)

`s_r=(sqrt(epsilon/m), sigma_r/sqrt(m)), 1<=r<=m`.     (5.2)

Then directly

`S^T S=I_2`.                                           (5.3)

Take

`Gamma=diag(1,-1)`                                     (5.4)

and form the exact target matrix

`A_{m,epsilon}=[1] direct_sum S Gamma S^T`.             (5.5)

Its nonzero spectrum is exactly

`{1,1,-1}`.                                            (5.6)

Thus (5.5) satisfies the owner's spectral hypothesis with equality and has no additional hidden assumptions.

The residual frame has one heavy row

`c_0=1-epsilon>1/2`,                                   (5.7)

while each cloud row has leverage

`c_r=(1+epsilon)/m`.                                   (5.8)

The Pluecker weights are explicit:

`w_{0r}=(1-epsilon)/m`,                                (5.9)

and for cloud rows `r<s`,

`w_{rs}=0` when `sigma_r=sigma_s`,

`w_{rs}=4 epsilon/m^2` when `sigma_r=-sigma_s`.        (5.10)

Their total is exactly one:

`m*(1-epsilon)/m + (m/2)^2*(4epsilon/m^2)=1`.          (5.11)

### Every pair cross-volume deteriorates

For a heavy-cloud pair `{0,r}`, formula (4.5) gives

`W_complement = epsilon(1-2/m)`,                       (5.12)

so

`s_{0r}`
` =sqrt(epsilon(1-epsilon)(1-2/m)/m)`.                 (5.13)

For a same-sign cloud pair, `s_rs=0`. For an opposite-sign cloud pair,

`s_rs^2`
` =(4epsilon/m^2)`
`  *[1-2(1+epsilon)/m+4epsilon/m^2]`,                  (5.14)

hence

`s_rs <= 2 sqrt(epsilon)/m`.                           (5.15)

Therefore

`max_{j<k} s_jk = O_epsilon(m^(-1/2)) ->0`.            (5.16)

This gives a genuine source-valid refutation of the intermediate structural implication

> a localized rank-two residual (some row leverage `>1/2`) must force one physical pair with a dimension-free Schur cross-volume certificate.

It does not refute QFORM. Indeed, applying the partner theorem (2.3) to any physical pair necessarily pays at least a growing reciprocal power along this family; for heavy-cloud pairs the stated bound grows like `m^(1/8)`.

The point is not that the partner theorem is false—it is exact in its stated scope—but that **pair selection after localization is still the wrong aggregation level**.

## 6. The same stress family is repaired by Theorem 3.1

Now condition the heavy residual coordinate `X_0` belonging to row `s_0` in (5.1). For this row,

`G=I_2-s_0 s_0^T=diag(epsilon,1)`.                    (6.1)

Whitening the remaining rows gives

`t_r=s_r G^(-1/2)=(1/sqrt(m), sigma_r/sqrt(m)).`       (6.2)

Hence every tail leverage is exactly

`|t_r|^2=2/m <=1/2`.                                   (6.3)

The whitened coefficient matrix is

`G^(1/2) Gamma G^(1/2)=diag(epsilon,-1)`,              (6.4)

whose determinant has magnitude `epsilon`.

Use the outer scalar coordinate in (5.5) as the independent third square, so `d=1`. Theorem 3.1 gives the dimension-free bound

`boxed(
 ||p_{X^T A_{m,epsilon} X}||_infinity
 <= 2*3^(1/4)*sqrt(pi e) epsilon^(-1/4),
)`                                                       (6.5)

uniformly for every even `m>=4` and all admissible input densities.

For the concrete choice `epsilon=1/4`,

`||p||_infinity <10.878`.                              (6.6)

Thus the exact same family that defeats every fixed residual-pair cross-volume certificate is controlled once the heavy coordinate is **grouped/conditioned before whitening the cloud**. This is the mechanism the global proof needs to generalize, not another best-pair search.

## 7. Conditional end-to-end route after this run

A compact current route is now:

1. the ridge-window theorem closes a quantitatively diffuse high-spectral projection branch while retaining arbitrary smaller eigenvalues;
2. scalar Schur completion plus fleet03/B01 r14 closes any branch with a quantitatively good rank-two residual cross-volume;
3. fleet03/B01 r12 closes a diffuse rank-two residual plus an independent physical third square;
4. Theorem 3.1 above extends item 3 by allowing **one heavy residual physical row to be conditioned away**, provided the whitened tail becomes diffuse;
5. the explicit family (5.5) proves that item 2 cannot replace item 4 by selecting a single good residual pair.

The first unpaid universal implication is therefore sharper:

### `QFORM-GROUPED-LEVERAGE-PEELING-v1` — OPEN

Starting only from the three-large-eigenvalue hypothesis, control the case in which after one scalar/spectral Schur reduction the rank-two residual has a heavy row `c close to1` and, after conditioning and whitening that row, the remaining frame is **still** localized or the determinant factor `1-c` is arbitrarily small. One needs a dimension-free product-preserving iteration or a different signed-Fejer/ridge mechanism that recovers the shrinking Gram determinant rather than paying `(1-c)^(-1/4)` repeatedly.

A mere fixed-pair extraction is now ruled out by (5.5)-(5.16). A mere conditional-density assertion is also insufficient by the live correction inbox. Any successful continuation must retain the actual grouped original-coordinate provenance.

This is not a full-proof candidate. The full arbitrary-matrix theorem remains OPEN, and no truth promotion is made from the finite checker below.

## 8. Exact finite checker used only as regression

Checker source was committed before this report at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260922T162930Z-fleet02-B01-qform-r24/checks.py`,

commit `15cdcbe7b208e59da6076228f788271a070e93b9`.

Captured output is at the adjacent `CHECKS.txt`, commit

`e34baaa2aef3363c9c1e82b3bfe5f7b1637ccae3`.

It verifies with exact rational arithmetic the Pluecker mass and leverage identities for `epsilon=1/4`, and prints the pair cross-volumes for `m=4,10,100,1000`; output terminates `STATUS=PASS`. The checker is regression evidence only. Equations (3.1)-(6.6) are symbolic proofs.

## 9. Source/status summary

**Proved in this run**

* `QFORM-CONDITION-ONE-HEAVY-ROW-v1`, equation (3.5);
* `QFORM-RANK2-PLUCKER-CROSSVOLUME-v1`, equations (4.3)-(4.7);
* the exact uniform-in-`m` bound (6.5) for the target-valid family (5.5).

**Refuted intermediate claim**

* `QFORM-HEAVY-ROW-FORCES-GOOD-SCHUR-PAIR-FALSE-v1`: one localized residual row does not force a dimension-free physical-pair cross-volume; the family (5.1)-(5.16) has `max_I s_I ->0`.

**Named partner actually applied**

* fleet03/B01 r14, to quantify why every residual-pair certificate deteriorates on the family;
* fleet03/B01 r12, first to obtain the conditional tail `L^3` bound after whitening, then to use the sharp dependence-safe third-square smoother and prove (3.5)/(6.5).

**Not proved**

* a universal lower bound on `1-c`;
* termination/control of repeated grouped heavy-row peeling;
* an exhaustive ridge/grouped-coordinate dichotomy for arbitrary additional spectral directions;
* the full QFORM theorem;
* continuity in Theorem 3.1 (only essential boundedness is claimed).

Execution remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval supplied source transport, but no native learned-memory receiver/ingestion evidence was observed. No scheduler mutation, email, notification change, new task/account, paid call, public release, remote workflow, permission change, credential material, machine path, unrelated private data, or benchmark material is used in this mathematical report.
