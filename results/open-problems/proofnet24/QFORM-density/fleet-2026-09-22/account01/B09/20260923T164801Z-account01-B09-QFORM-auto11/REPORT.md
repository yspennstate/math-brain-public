SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T16:48:01Z.
attacking: spend a fixed physical hub-pair's aggregate source-coordinate third volume directly, with arbitrary same-side leaf curvature, by a random original-coordinate split and the completed two-hub crossing-block theorem.

# account01/B09 — fixed-pair aggregate third volume pays arbitrary leaf curvature

## Status

**ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL TARGET OPEN.**

This run proves a product-preserving theorem that removes the `general leaf curvature` obstruction from the fixed two-physical-hub-pair branch. The theorem uses only actual source-coordinate minors, a literal random partition, and completed two-/three-hub Fourier estimates. It does not rotate the random variables, delete a small quadratic operator, or take a square-root small-ball loss.

The unrestricted owner target remains **OPEN / not proved / not disproved**. Full-target continuity remains open. Continuity is proved in the new fixed-pair aggregate-volume branch below.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh sources actually used

### 1.1 Current owner/brain state

Fresh `math-research-brain/main` at run start resolved to `15d5ecc437ef47d46394d4d5ce502f8482abd90a`. OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only, with no pause of account01/B09. I read the current MANIFEST, CURRENT_RESEARCH, CLAIMS, live CORRECTION_INBOX, MEMORY_PROTOCOL and account01/B09 assignment, plus the newest owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.

The source corrections retained throughout include: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; arbitrary-joint rank-three coarea is false; worst conditional projection-density moments are unavailable; a small matrix operator cannot be discarded as a small random quadratic error under arbitrary unbounded cap-one laws; and a uniformly good single physical minor/cross cut is not automatic.

### 1.2 Newest Claude continuation — the analytic receiver

The newest required continuation was read at

`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`,

`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`.

I use two completed theorems there.

**Theorem 6.3 (three hubs).** If `H` consists of three literal original coordinates and `M=A[H,H^c]` has singular values `s1>=s2>=s3>0`, then, uniformly in the physical 3x3 hub core and in the entire remaining quadratic function,

`||p_Q||_inf <= 3 sqrt(2) (s1 s2 s3)^(-1/3)`.

The proof gives an integrable characteristic-function envelope and hence a continuous density.

**Theorem 6.5 (two hubs plus arbitrary crossing remainder).** If `H={a,b}` are two literal original hub coordinates, `L=M X' in R^2`, and the light-coordinate remainder is an arbitrary quadratic polynomial, split the light bank as `I disjoint J`. Let `M_J` have singular values `s1'>=s2'>0`, let `Pi_J` be the orthogonal projection in `R^J` onto `row(M_J)`, and let

`C=(A_R)[I,J](Id-Pi_J)`, `F=||C||_F`.

If every row `c_i` of `C` satisfies `||c_i||^2<=F^2/2`, then, uniformly in the arbitrary physical 2x2 hub core,

`||p_Q||_inf <= 5.35 (s1' s2' F)^(-1/3)`.

Again the proof has an integrable Fourier envelope, so the density is continuous and the same coefficient gives a direct linear interval bound.

These exact scopes are essential below: arbitrary same-side curvature is retained, while the source-coordinate row-spread gate is verified by a new deterministic volume argument.

### 1.3 Designated partner account02/B09

The latest completed designated-partner result is account02/B09 r15,

`yspennstate/math-open-problems@c27ff5b752bf25d2933cbdfac5a870b0dcf71181`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T154445Z-account02-B09-QFORM-r15/REPORT.md`.

I use its exact physical-volume identity at an actual target inequality in Section 6. In its rank-one leaf packet it proves

`V_ab(S)=||q_S||_2^2 det Gram(q_T,A[T,a],A[T,b])`,

and for its explicit target-valid family this equals `1/4`. I do not infer any general low-rank representation from that theorem.

A second structural source used for the consequence in Section 5 is account03/B09 r35,

`yspennstate/math-open-problems@82f6ea83f0e981f756fd18080ffdd11a447b60a8`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T144532Z-account03-B09-QFORM-r35/REPORT.md`.

Its localized fixed physical pair `a,b` retains an anchored source-coordinate volume `V_ab(S)>=27 G_*/400` while the leaf block itself is arbitrary. The present theorem spends that volume without any assumption that the leaf block is diagonal plus low rank.

## 2. Setup: aggregate volume anchored on one literal physical pair

Fix two distinct literal original coordinates

`H={a,b}`

and put

`L=H^c`.

Write

`M=A[H,L] in R^(2 x |L|)`,
`D=A[L,L]`.

No condition is imposed on the physical `2x2` core `A[H,H]`, on `D`, on signs, or on any affine terms produced by conditioning outside variables.

For every leaf `i in L`, define its fixed-pair physical third volume

`V_i := sum_{T subset L\{i}, |T|=3} det A[H union {i},T]^2`,          (2.1)

and the aggregate

`V := sum_{i in L} V_i`.                                             (2.2)

Every determinant in (2.1) is a genuine physical `3x3` cross minor: the row set `H union {i}` and column set `T` are disjoint original-coordinate sets.

The new theorem concerns the nontrivial endpoint `V>0`. If `V=0`, the theorem makes no assertion; that is a structural degeneration to be routed separately in the full proof.

## 3. Exact partition identity

Take any literal partition

`L=I disjoint_union J`.

Let

`M_J=A[H,J]`,
`G_J=M_J M_J^T`,
`Delta_J=det G_J`,                                               (3.1)

and let `Pi_J` be the orthogonal projection of `R^J` onto `row(M_J)`. Define the projected crossing-curvature block

`C_{I,J}:=D[I,J](Id-Pi_J)`,
`F^2:=||C_{I,J}||_F^2`.                                        (3.2)

For each `i in I`, let

`c_i=D[i,J](Id-Pi_J)`                                          (3.3)

be the corresponding row.

### Lemma 3.1 — exact source-coordinate identity

For every `i in I`,

`boxed:
 Delta_J ||c_i||_2^2
 = sum_{T subset J, |T|=3} det A[H union {i},T]^2.`             (3.4)

Consequently

`boxed:
 W(I,J):=Delta_J F^2
 =sum_{i in I} sum_{T subset J, |T|=3}
     det A[H union {i},T]^2.`                                  (3.5)

#### Proof

Form the `3 x |J|` physical row matrix

`R_i=[ M_J ; D[i,J] ]`.

When `G_J` is invertible, the Gram determinant / Schur-complement identity gives

`det(R_i R_i^T)
 =det(M_J M_J^T)
  dist(D[i,J],row(M_J))^2
 =Delta_J ||c_i||_2^2.`                                        (3.6)

Cauchy--Binet applied to `R_i` gives

`det(R_i R_i^T)
 =sum_{T subset J, |T|=3} det R_i[:,T]^2
 =sum_{T subset J, |T|=3} det A[H union {i},T]^2.`             (3.7)

Equations (3.6)-(3.7) give (3.4). Summing over `i` gives (3.5).

The identity also extends continuously to singular `G_J`; for the application below `W>0` automatically forces `Delta_J>0` and `F>0`, so no singular inversion is used. QED.

The central point is that (3.5) is not an operator-norm approximation. It is an exact equality between the source-coordinate three-volume and precisely the projected crossing block appearing in Theorem 6.5.

## 4. Random physical partition and an exhaustive diffuse/heavy dichotomy

Put each leaf coordinate independently into `J` with probability `p` and into `I` with probability `1-p`.

Each fixed term in (2.1), indexed by one distinguished row `i` and a disjoint three-set `T`, appears in (3.5) exactly when

`i in I` and `T subset J`.

The probability is

`(1-p)p^3`.

Therefore the exact first moment is

`boxed:
 E W(I,J)=(1-p)p^3 V.`                                         (4.1)

The function `(1-p)p^3` is maximal at `p=3/4`, where

`(1-p)p^3=27/256`.                                             (4.2)

Hence there is at least one literal source-coordinate partition such that

`boxed:
 W(I,J)>= (27/256)V.`                                          (4.3)

Now split into two exhaustive cases.

### Case A: diffuse fixed-pair singleton volume

Assume

`max_i V_i <= (27/512)V.`                                     (4.4)

Choose a partition satisfying (4.3). For every `i in I`, define its contribution

`W_i:=Delta_J ||c_i||^2
     =sum_{T subset J,|T|=3} det A[H union {i},T]^2.`           (4.5)

Since the sum in (4.5) is a sub-sum of (2.1),

`W_i<=V_i<= (27/512)V <= W/2.`                                (4.6)

Because `W=Delta_J F^2>0`, (4.6) is exactly

`||c_i||^2 <= F^2/2`                                          (4.7)

for every row. Thus the row-spread gate of Theorem 6.5 is not assumed; it is forced by aggregate source-coordinate volume.

If `s1',s2'` are the two singular values of `M_J`, then

`s1' s2'=sqrt(Delta_J)`,

so

`s1' s2' F=sqrt(Delta_J F^2)=sqrt(W).`                         (4.8)

Applying Theorem 6.5 gives a continuous density with

`||p_Q||_inf
 <=5.35 W^(-1/6)
 <=5.35 (256/27)^(1/6) V^(-1/6)`                              (4.9)

and numerically

`boxed:
 ||p_Q||_inf <7.784 V^(-1/6).`                                (4.10)

The same coefficient gives `P{Q in B}<7.784 V^(-1/6)|B|` for every interval `B`.

### Case B: a heavy physical singleton volume

Otherwise there is a literal leaf `i` such that

`V_i>(27/512)V.`                                               (4.11)

Promote that same original coordinate to form the three-hub set

`H_i=H union {i}`.

Its physical cross block to the complementary original coordinates is

`N_i=A[H_i,L\{i}]`.

Cauchy--Binet gives exactly

`det(N_i N_i^T)
 =sum_{T subset L\{i}, |T|=3} det A[H_i,T]^2
 =V_i.`                                                        (4.12)

If its singular values are `r1,r2,r3`, then

`r1 r2 r3=sqrt(V_i)`.

Theorem 6.3 therefore gives a continuous density and

`||p_Q||_inf
 <=3 sqrt(2) V_i^(-1/6)
 <3 sqrt(2) (512/27)^(1/6) V^(-1/6).`                         (4.13)

The constant simplifies exactly:

`3 sqrt(2) (512/27)^(1/6)=4 sqrt(3)=6.928203...`               (4.14)

which is smaller than the diffuse-case constant.

The same coefficient again gives the direct linear interval estimate.

## 5. Main theorem and localized-pair consequence

### Theorem `QFORM-FIXEDPAIR-AGGREGATE-THREEVOLUME-v1`

Let `X_1,...,X_n` be independent real variables with probability densities at most one. Let `Q=X^T A X+b^T X+c` for an arbitrary real symmetric `A`. Fix any two literal physical coordinates `H={a,b}` and define `V` by (2.1)-(2.2).

If `V>0`, then `Q` has a **continuous density** and

`boxed:
 ||p_Q||_inf
 <=5.35 (256/27)^(1/6) V^(-1/6)
 <7.784 V^(-1/6).`                                            (5.1)

Consequently, for every interval `B`,

`boxed:
 P{Q in B}<7.784 V^(-1/6)|B|.`                                (5.2)

The theorem is uniform in:
- the entire physical `2x2` hub core, including zero/rank-one/definite/indefinite and near-stratum transitions;
- all same-side leaf curvature `A[L,L]`, with no low-rank or diagonal-plus-low-rank hypothesis;
- all signs and all affine terms.

No spectral rotation of the product input is made. No small operator is deleted. No moment, support, log-concavity, connected-support or Gaussian assumption is introduced.

The scaling is exact: under `A -> sA`, every physical `3x3` determinant scales as `s^3`, so `V -> s^6 V`, and `V^(-1/6)` scales as `|s|^-1`, exactly like a one-dimensional output density.

### Consequence for account03/B09 r35

In the localized physical-pair branch of r35, the fixed literal pair `a,b` has disjoint banks `S,T` with

`V_ab(S)>=27 G_*/400.`                                        (5.3)

The global aggregate `V` in (2.2) contains those same physical minors, so

`V>=V_ab(S)>=27G_*/400.`                                      (5.4)

Therefore (5.1) gives

`boxed:
 ||p_Q||_inf
 <7.784 (400/(27G_*))^(1/6)
 <12.198 G_*^(-1/6).`                                         (5.5)

This estimate is **uniform across the entire physical-pair core rank/sign transition and permits completely arbitrary leaf curvature**.

Thus the r35/r15 debt `QFORM-LOCALIZED-HUBPAIR-GENERAL-LEAFCURVATURE-ROUTING-v1` is paid inside that localized-pair branch. The remaining full-target debt is upstream: from the bare three-large-eigenvalue hypothesis, force either such a positive fixed-pair aggregate volume at universal scale or another already-paid three-hub/ridge/diffuse/grouped-coordinate/definite/singular exit.

## 6. Required actual use of the designated account02/B09 result

I now apply partner r15's exact identity to an actual target-valid inequality rather than merely citing it.

Partner r15 constructs, for every real `delta`,

`Q_delta
 =X_a^2+delta X_b^2
  +2 X_a <c_1,X_T>
  +2 X_b <c_2,X_T>
  +<q,X_{S union T}>^2`,                                      (6.1)

using a Sylvester-Walsh flat orthonormal triple on `T` and a disjoint flat vector on `S`. Its exact nonzero spectrum is

`{(1+sqrt(5))/2,(1-sqrt(5))/2,
  (delta+sqrt(delta^2+4))/2,(delta-sqrt(delta^2+4))/2,1}`,      (6.2)

so at least three eigenvalues have modulus at least one for **every** real `delta`.

The completed partner identity gives, on its actual disjoint banks,

`V_ab(S)=||q_S||^2 det Gram(q_T,c_1,c_2)=1/4.`                 (6.3)

Therefore the global `V` in Theorem (5.1) satisfies `V>=1/4`, and the new arbitrary-curvature compiler gives the actual inequality

`||p_{Q_delta}||_inf
 <7.784 (1/4)^(-1/6)
 <9.807`,                                                      (6.4)

uniformly in `delta`, with a continuous density and

`P{Q_delta in B}<9.807 |B|.`                                  (6.5)

Partner r15's low-rank-specific mixed-frame theorem is sharper on this exact family (`<4.399`). The point of (6.4) is different: the new payment uses only the partner's **physical aggregate volume currency** and survives completely arbitrary same-side leaf curvature, with no diagonal-plus-low-rank decomposition required.

This satisfies the designated-partner requirement at an actual target inequality and identifies precisely what new scope has been gained.

## 7. Why this does not solve the full conjecture

Theorem (5.1) is conditional on a fixed pair having `V>0`, and the numerical bound depends on `V^(-1/6)`. The bare assumption `sigma_3(A)>=1` does not, by itself, imply that one arbitrarily chosen physical pair has `V` bounded below. There are known diffuse/grouped families in which individual physical minors are small, and the live correction ledger forbids promoting a single-minor heuristic to a global theorem.

The new theorem nevertheless removes a previously genuine analytic obstruction: **once a fixed physical pair carries aggregate third volume, no additional assumption on the leaf curvature or pair-core rank/sign is needed.** The source-coordinate random partition converts that volume exactly into either:
1. a diffuse projected crossing block paid by Theorem 6.5, or
2. one promoted physical third hub paid by Theorem 6.3.

The first unpaid B09 implication is therefore

`QFORM-FIXEDPAIR-VOLUME-OR-PAID-EXIT-v1`:

> Under the three-large-eigenvalue hypothesis, in the remaining no-pivot/high-hub configurations, prove that either some literal physical pair has aggregate anchored three-volume `V>=c` at the correct normalized scale, or route the matrix into an existing three-hub, ridge/diffuse, grouped-coordinate, definite/singular-pair, or low-rank carrier theorem. The route must use aggregate original-coordinate currency rather than assert one uniformly good minor.

A natural next step is to splice (5.1) directly into the existing rank-two hub/star aggregate compiler before any near-core inversion: the fixed-pair localization already supplies (5.3), so the entire downstream general-leaf-curvature branch is now analytic rather than perturbative.

## 8. Constants and integrity checks

The exact partition coefficient is maximized at `p=3/4`:

`max_{0<=p<=1} (1-p)p^3=27/256.`                              (8.1)

The diffuse constant is

`5.35(256/27)^(1/6)=7.783348603264946...`,                    (8.2)

while the heavy-row constant at threshold `(27/512)V` is

`3sqrt(2)(512/27)^(1/6)=4sqrt(3)=6.92820323027551...`.         (8.3)

Thus `7.784` safely covers both exhaustive cases. For the partner family,

`7.783348603264946 * 4^(1/6)=9.806404743923364...<9.807.`      (8.4)

For the r35 localized compiler,

`7.783348603264946 * (400/27)^(1/6)=12.197828419627104...`.   (8.5)

All determinant quantities are squared physical minors; no sign assumption is present. No numerical histogram is used as proof.

## 9. Final scope

New claim: `QFORM-FIXEDPAIR-AGGREGATE-THREEVOLUME-v1`.

Status: **supporting theorem proved from completed source theorems; full conjecture still open**.

Continuity: **proved in this branch**, because both exhaustive receiver branches inherit integrable characteristic-function estimates. Full-target continuity remains open.

Repository transport/readback is not native learned-memory ingestion; this run remains `WITHOUT_VERIFIED_BRAIN`.
