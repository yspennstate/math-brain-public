SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T00:04:41Z.
attacking: coordinate-minor selection by a new mechanism: pay the exact scalar-Schur numerator before dividing by the tiny pivot, then use compound-tail/overlap alternatives on that numerator.

# account01/B07 r13 — Schur-numerator cancellation and a finite compound-rank cascade

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: Coordinate minor selection / GEOMETRY.
Run: `20260923T000441Z-account01-B07-QFORM-r13`.
Control at start: OWNER CONTROL revision `2026-09-22.15`.
Execution state: `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).
Outcome: **ESSENTIAL_STEP_APPLIED / SUPPORTING ANALYTIC + STRUCTURAL THEOREMS; FULL QFORM OPEN.**

The exact owner target remains the unrestricted product-law statement: independent original real coordinates, every scalar density bounded by one, arbitrary real symmetric coefficient matrix with at least three eigenvalues of absolute value at least one. No moment, support, log-concavity, connected-support, Gaussian, or post-rotation independence assumption is used. The full continuous-density conclusion is not proved here.

This run deliberately changes mechanism after the preceding fixed-order/ridge-selection runs. Instead of trying to choose another physical minor, it keeps the exact scalar Schur **numerator** and proves that the dangerous reciprocal small pivot cancels analytically before any determinant bank is paid.

## 1. Completed inputs actually used

### 1.1 Designated partner account02/B07 r20

Canonical mathematics:

`yspennstate/math-open-problems@489b9fea1b2a0ec252021c6905fcbec0b797d18e`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T234330Z-account02-B07-QFORM-r20/REPORT.md`.

Its theorem `QFORM-ANCHOR-EXTERIOR-PACKET-v1` applies to a physical anchor in a symmetric matrix

`S=[[d,w^T],[w,C]]`, `beta=||w||_2`,

and proves, under the current tiny-pivot collar `0<|d|<1/16`, `beta>200^(-1/4)`, `s_2(S)>=1`, that the anchor exterior packet splits exactly into

`E_h=A_h+B_h^shared+B_h^disjoint`,

where

`A_h=||dC-ww^T||_F^2`,

and one of the three banks is larger than

`c0:=1/(3sqrt(200))=0.0235702260395516...`.

The disjoint and shared winners already route to cross-bank / second-pivot mechanisms. The first unpaid numerator winner is

`L:=||N||_F^2>c0`, `N:=dC-ww^T`, `rank(N)>=2`,                       (1.1)

because r20 separately pays the exact `rank(N)=1` endpoint by the orientation-free rank-two theorem.

This report applies (1.1) to explicit new inequalities below. Thus the designated partner is consumed mathematically, not cited only for context.

### 1.2 Half-Riesz determinant-bank theorem

account03/B03, canonical

`yspennstate/math-open-problems@924b3c4c70f86a64402863fe228f641bf3db60b2`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T175531Z-account03-B03-QFORM-r17/REPORT.md`.

For an original-coordinate residual cross block `B`, it proves

`H_(1/2)(R):=sup_t E|R-t|^(-1/2)
 <= c2 E_2(B)^(-1/8),   c2=7.673759290384858`,                    (1.2)

when one selected-side cross-range leverage is at most `1/2`, and, with no leverage assumption,

`H_(1/2)(R)<=c3 E_3(B)^(-1/12),   c3=9.840655864922019`.          (1.3)

All same-side curvature, affine terms and additional coordinates are retained.

### 1.3 Square half-Riesz theorem

account03/B07 r20, canonical

`yspennstate/math-open-problems@1fcbb0cf28b6ad654bb94777188ded86ac1613d3`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T235048Z-account03-B07-qform-r20/REPORT.md`.

Its theorem `QFORM-SQUARE-HALFRIESZ-QUARTERROOT-v1` says that for cap-one `X` independent of `Z`,

`F=d(X+m(Z))^2+H(Z)`, `d!=0`,

`H_(1/2)(F)<=4|d|^(-1/4) H_(1/2)(H)^(1/2)`.                    (1.4)

No independence between the shift `m(Z)` and the residual `H(Z)` is assumed.

### 1.4 Exact-rank-two affine half-Riesz theorem

Canonical

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For an exact rank-two real symmetric quadratic matrix with nonzero spectral determinant `D` and arbitrary affine term,

`H_(1/2)<=128 D^(-1/4)`.                                          (1.5)

## 2. First new theorem: the scalar-Schur numerator cancels the small pivot exactly

The central observation is that the correct object to pay is not the divided Schur matrix `T=N/d`; it is the numerator `N` itself.

### Theorem 2.1 — `QFORM-SCHUR-NUMERATOR-CANCELLATION-v1`

Let `X` have a probability density bounded by one and be independent of a random vector `Z`. Let `d!=0`, let `m(Z)` be arbitrary measurable, and let `G(Z)` be any real random variable. Put

`F=d(X+m(Z))^2+d^(-1)G(Z)`.                                      (2.1)

If

`K:=sup_s E|G-s|^(-1/2)<infinity`,                              (2.2)

then:

`boxed: ||p_F||_infinity <= K`,                                 (2.3)

and, using (1.4),

`boxed: H_(1/2)(F)<=4 sqrt(K).`                                 (2.4)

The density assertion is essential boundedness; continuity is not asserted.

#### Proof of the density cancellation

Condition on `Z`. The translated square `d(X+m)^2` has conditional density bounded pointwise by

`|d|^(-1/2)|u|^(-1/2)`.

Therefore, for a.e. `t`,

`p_F(t)
 <= |d|^(-1/2) E |t-d^(-1)G|^(-1/2)
 = E |dt-G|^(-1/2)
 <= K`.                                                         (2.5)

The two powers of the small pivot cancel **exactly**. No limiting argument in `d`, no perturbative deletion, and no conditional projected-density supremum is used.

For (2.4), scaling gives

`H_(1/2)(G/d)=|d|^(1/2) K`.

Substitute this in (1.4):

`H_(1/2)(F)
 <=4|d|^(-1/4)(|d|^(1/2)K)^(1/2)
 =4sqrt(K)`.                                                    (2.6)

QED.

### Physical scalar-pivot form

For the actual original-coordinate polynomial

`Q=dX_h^2+2X_h w^T Z+Z^T C Z+alpha X_h+beta^T Z+c`,             (2.7)

define the exact Schur numerator

`N=dC-ww^T`.                                                     (2.8)

Completing only the physical coordinate `X_h` gives

`Q=d(X_h+(w^T Z+alpha/2)/d)^2+d^(-1)G_N(Z)`,                    (2.9)

where

`G_N(Z)=Z^T N Z+(d beta-alpha w)^T Z+dc-alpha^2/4`.             (2.10)

Thus **any** source-valid half-Riesz estimate for the numerator form `G_N`, with arbitrary affine term retained, immediately gives (2.3)-(2.4) with no `|d|^-theta` loss.

This is the first essential missing implication attempted in this run. It directly targets the partner r20 numerator branch, where previous bookkeeping exposed `N=dC-ww^T` but dividing by `d` made the tiny pivot look dangerous.

## 3. Exact determinant transfer for the numerator

For two-subsets `R,C` of coordinates outside the pivot `h`, Sylvester/block-determinant algebra gives

`boxed:
 det N[R,C]
 = d det S[{h} union R,{h} union C].
`                                                                  (3.1)

Indeed `N=dT` for the exact Schur complement `T=C-ww^T/d`, while

`det S[{h} union R,{h} union C]=d det T[R,C]`.

Consequently, if

`C_2(N):=e_2(NN^T)=sum_(|R|=|C|=2) det N[R,C]^2`,               (3.2)

and `W_h^(3)(S)` denotes the complete third-minor mass whose row and column triples both contain `h`, then

`boxed: C_2(N)=d^2 W_h^(3)(S).`                                 (3.3)

Equation (3.3) is useful conceptually: the second compound of the numerator is the correctly scaled shared third-compound resource. It is not a selected principal minor.

## 4. A general compound-tail inequality

Let the squared singular values of an arbitrary matrix `M` be

`lambda_1>=lambda_2>=...>=0`,

and let

`C_r(M)=e_r(lambda)`,
`T_r(M)=sum_(j>r) lambda_j=dist_F(M,{rank<=r})^2`.               (4.1)

### Lemma 4.1 — `QFORM-COMPOUND-TAIL-v1`

For every `r>=1` with `C_r>0`,

`boxed: T_r C_r <= (r+1) C_(r+1).`                              (4.2)

#### Proof

Expand

`(r+1)C_(r+1)
 =sum_(|I|=r) (prod_(i in I)lambda_i) sum_(j notin I)lambda_j`. (4.3)

Among all `r`-sets `I`, the complementary sum is minimized by deleting the `r` largest squared singular values. Hence every complementary sum in (4.3) is at least `T_r`. Factoring it out gives (4.2). QED.

The first two instances are

`T_1 C_1<=2C_2`,
`T_2 C_2<=3C_3`.                                                (4.4)

This is an exact, dimension-free alternative to perturbatively deleting small singular directions.

## 5. Apply the designated partner: a finite rank-tube / robust-compound cascade

Return to the partner r20 unpaid numerator winner (1.1):

`L=C_1(N)=||N||_F^2>c0=1/(3sqrt(200))`, `rank(N)>=2`.            (5.1)

Define `C_2=e_2(NN^T)` and `C_3=e_3(NN^T)`.

### Alternative R1: quantitative rank-one tube

If

`C_2<L^2/64`,                                                   (5.2)

then (4.4) gives

`dist_F(N,{rank<=1})^2=T_1< L/32`.                              (5.3)

Equivalently,

`dist_F(N,{rank<=1})/||N||_F <1/sqrt(32)=0.176777... .`         (5.4)

This is not declared paid: the live correction forbids deleting the small residual directions. It is a sharply isolated near-rank-one chamber.

### Alternative R2: stable second compound, but a quantitative rank-two tube

Assume instead

`C_2>=L^2/64`.                                                   (5.5)

If

`C_3< C_2 L/192`,                                               (5.6)

then again by (4.4),

`dist_F(N,{rank<=2})^2=T_2< L/64`,                              (5.7)

so

`dist_F(N,{rank<=2})/||N||_F <1/8`.                            (5.8)

Again, (5.8) is a structural reduction, not permission to replace `N` by rank two.

### Alternative R3: robust third compound

If neither (5.2) nor (5.6) holds, then

`C_3>=C_2L/192>=L^3/12288`.                                    (5.9)

Using the partner's absolute lower bound `L>c0`,

`boxed: C_3>c0^3/12288=1.0656388364...*10^(-9).`                (5.10)

Thus the numerator winner admits an exhaustive **finite** trichotomy: near rank one, near rank two, or a dimension-free third-compound bank. No singular direction is silently dropped.

## 6. Actual analytic payments inside the stable-compound alternatives

The numerator cancellation theorem makes existing half-Riesz estimates much stronger in this chamber because they no longer carry a small-pivot penalty.

### 6.1 Stable `C_2`, disjoint physical two-minor mass, diffuse range

Decompose `C_2(N)` by overlap size of the row and column two-sets:

`C_2=M_0+M_1+M_2`.                                              (6.1)

Suppose the disjoint class wins, `M_0>=C_2/3`. A fair physical two-coloring puts a fixed disjoint ordered pair of two-sets on opposite sides with probability `1/16`, so some original-coordinate cut has cross block `B=N[I,J]` satisfying

`E_2(B)>=M_0/16>=C_2/48`.                                      (6.2)

If one selected side of this cross block has range leverage at most `1/2`, (1.2) gives

`K_N:=H_(1/2)(G_N)
 <= c2 (C_2/48)^(-1/8)`.                                      (6.3)

By (2.3)-(2.4), the physical scalar-pivot form (2.7) therefore satisfies

`boxed: ||p_Q||_infinity <=c2 (C_2/48)^(-1/8),`                 (6.4)

`boxed: H_(1/2)(Q)<=4sqrt(c2)(C_2/48)^(-1/16).`                 (6.5)

There is **no factor involving `d`**.

Under the actual partner branch (5.1),(5.5),

`C_2>=c0^2/64=1/115200`,                                       (6.6)

so (6.4)-(6.5) become the fully numerical bounds

`boxed: ||p_Q||_infinity <53.438`,                              (6.7)

`boxed: H_(1/2)(Q)<29.241`.                                    (6.8)

This closes a genuine part of the designated partner's previously unpaid `A_h` numerator winner.

If `rank(N)=2` exactly, the orientation-free theorem (1.5) gives without any physical leverage condition

`K_N<=128 C_2^(-1/8)`.                                         (6.9)

Together with (2.3)-(2.4), the stable branch (6.6) has

`||p_Q||_infinity<549.404`,
`H_(1/2)(Q)<93.758`.                                           (6.10)

The exact rank-two statement is distinct from a rank-two **tube**; no perturbation is used.

### 6.2 Robust `C_3`, disjoint physical third-minor mass: unconditional payment

Decompose the full third compound of `N` by row/column triple overlap,

`C_3=O_0+O_1+O_2+O_3`.                                         (6.11)

If the disjoint class wins, `O_0>=C_3/4`, a fair physical cut retains each ordered disjoint triple pair with probability `1/64`. Hence some cross block has

`E_3(B)>=O_0/64>=C_3/256`.                                     (6.12)

Now use the unconditional half-Riesz theorem (1.3), then Theorem 2.1:

`||p_Q||_infinity<=c3(C_3/256)^(-1/12)`,                       (6.13)

`H_(1/2)(Q)<=4sqrt(c3)(C_3/256)^(-1/24)`.                      (6.14)

In the partner robust branch (5.9),

`E_3(B)>c0^3/(12288*256)`,                                    (6.15)

and therefore

`boxed: ||p_Q||_infinity<87.380`,                              (6.16)

`boxed: H_(1/2)(Q)<37.391`.                                    (6.17)

Crucially, (6.16) has **no leverage assumption** and still no tiny-pivot loss.

If instead `O_1,O_2`, or `O_3` dominates, the numerator has a robust **non-disjoint** third-compound packet. That packet is now in the exact scope of the existing shared-coordinate/shared-pair Schur ledgers; it is not silently treated as a cross block.

## 7. A genuine target-class stress: the rank-one tube is real

One might hope that the owner hypothesis, or even the partner collar plus `rank(N)>=2`, forces `C_2(N)/||N||_F^4` away from zero. This is false.

For `0<d<1/16`, take

`S_d=[[d,2,0],[2,0,0],[0,0,1]].`                              (7.1)

This is already a full target matrix. Its eigenvalues are

`1`,
`lambda_+=(d+sqrt(d^2+16))/2`,
`lambda_-=(d-sqrt(d^2+16))/2`.                                 (7.2)

For every `0<d<1/16`, `lambda_+>1` and

`|lambda_-|=(sqrt(d^2+16)-d)/2>(4-d)/2>1`,                    (7.3)

so all three eigenvalue magnitudes are at least one. The pivot row has `beta=2` and `0<d<1/16`, exactly in the tiny-pivot geometry.

Here

`w=(2,0)`, `C=diag(0,1)`,

and therefore

`N=dC-ww^T=diag(-4,d)`.                                        (7.4)

Thus

`L=16+d^2`,
`C_2(N)=16d^2`,

and

`C_2(N)/L^2 ->0`, `dist_F(N,{rank<=1})^2=d^2`.                 (7.5)

So even the **full three-large-eigenvalue hypothesis** allows a genuinely rank-two numerator arbitrarily close, relatively, to rank one. Any attempted proof that declares the tube harmless merely because its second singular value is small is invalid.

This is not a counterexample to QFORM. The physical pair on the first two coordinates is invertible indefinite with

`D=|det|=4`,
`kappa=|lambda_-|>63/32`,

while `s_3(S_d)>=1`. The completed full-matrix physical-pair theorem

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`

therefore gives a universal essential-density bound (numerically `<12.44` from its formula). The family refutes only the proposed intermediate implication “three large eigenvalues force a stable Schur numerator second compound.”

Classification: **`QFORM-NUMERATOR-STABLE-RANK-FORCED-FALSE-v1` — CANDIDATE_REFUTED for that intermediate selector; QFORM itself not refuted.**

## 8. Compact conditional end-to-end map

The relevant current proof map is now:

1. Existing global reductions isolate the O0/S0 scalar-pivot collar without rotating the independent coordinates.
2. Designated partner account02/B07 r20 forces one of three determinant-weighted anchor banks. Its disjoint/shared winners keep their prior routes. In the numerator winner, it supplies (5.1).
3. Exact `rank(N)=1` is already paid by the partner. For `rank(N)>=2`, Theorem 2.1 changes the analytic currency: pay `G_N`, not `T=N/d`. Every valid half-Riesz estimate for `G_N` pays the full scalar-pivot density with **zero small-pivot loss**, and pays its half-Riesz potential with only a square-root loss.
4. Lemma 4.1 makes the remaining numerator geometry finite: near rank one, near rank two, or robust third compound.
5. Stable second-compound + disjoint/diffuse overlap is paid by (6.7); exact rank two is paid by (6.10). Robust third-compound + disjoint overlap is paid unconditionally by (6.16).
6. The only numerator states left by this run are therefore:
   - a genuine rank-one tube (5.2)-(5.4), where tiny directions may be at the same scale as `d` and cannot be deleted;
   - a genuine rank-two tube (5.5)-(5.8), again without perturbative deletion;
   - stable/robust compound mass concentrated in shared/principal physical-overlap classes or in the high-leverage two-minor branch. These route into the exact shared-coordinate/shared-pair ledgers rather than a false cross-block identification.

This is strictly narrower than the partner r20 debt “`||N||_F` is constant and `rank(N)>=2`.”

## 9. First unpaid implication after this run

**`QFORM-NUMERATOR-RANKTUBE-OR-SHAREDOVERLAP-PAYMENT-v1`.**

Starting from the partner numerator resource `L>c0`, pay one of the following without deleting small singular directions:

- **R1:** `dist_F(N,rank<=1)^2<L/32`, with `rank(N)>=2`;
- **R2:** `C_2>=L^2/64` and `dist_F(N,rank<=2)^2<L/64`, but `N` is not exactly rank two;
- **R3-overlap:** robust `C_3>=L^3/12288` whose third-minor mass is predominantly one-/two-/three-shared, or stable `C_2` whose two-minor mass is shared/principal/high-leverage.

The natural next mechanism is **scale-matched rank-tube analysis**, not perturbation: compare the small numerator singular scales to the physical pivot `|d|` before dividing. Stress (7.1) shows why—its small numerator singular value is exactly `|d|`, and after Schur division it becomes a genuine order-one third direction.

## 10. Continuity and integrity status

- Full universal QFORM density theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Theorem 2.1 density conclusion: **essentially bounded density only**; continuity not proved.
- Branches relying on the determinant-bank half-Riesz theorem plus Theorem 2.1 inherit only the essential-density conclusion stated here; no global continuity upgrade is claimed.
- No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, post-rotation independence, pointwise van-der-Corput, arbitrary-joint coarea, or Monte Carlo extremality assumption is used.
- No scheduler, notification, email, Drive, public-release, permission, paid-model/API/Codex, or cross-account native state was changed.
