SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-23T10:41:26.294416Z.
attacking: close or sharply quantify the one-child/two-cross hybrid using the newest scalar-Schur E2 receiver, the actual spectral gate, and an exact delocalized Hadamard stress calculation.

# account02/B08 r26 — actual-gate rank-four routing and exact Schur-E2 anatomy of the diffuse hybrid

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case / complementary constructions and source-valid counterexamples  
**Classification:** `NEW SUPPORTING ROUTERS + EXACT TARGET-VALID MECHANISM OBSTRUCTION / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains OPEN. Throughout, the random variables are the original independent coordinates and every one-dimensional density is bounded by one. No moment, support, iid, log-concavity, spectral-coordinate conditioning, post-rotation independence, arbitrary-joint coarea estimate, one-good-minor selection, or small-random-quadratic-perturbation principle is used.

## 1. First unpaid implication

The r25 actual spectral gate leaves two genuine hybrid states after arbitrary ORIGINAL-coordinate conditioning:

* `k=1`: two actual cross singular directions plus one actual child eigendirection;
* `k=2`: one actual cross singular direction plus two actual child eigendirections.

The full-ambient missing theorem must use the child curvature without rotating the product source. The newest partner result changes the `k=1` diagnosis: once a physical scalar Schur pivot leaves a residual physical `E_2`, Linfinity is already paid. The calculation below shows that on the canonical delocalized Hadamard witness the residual `E_2` does **not** disappear at all. What disappears is the scalar pivot coefficient itself, at rate `1/m`. Thus the remaining `k=1` diffuse debt is a **grouped-square aggregation problem**, not an `E_2`-survival problem.

Before reaching that endpoint, Section 3 removes arbitrary high cross-rank complementary spectrum by a marginal-free fifth-volume theorem. Section 4 gives a positive leakage-stable localized-pivot receiver. Sections 5-6 compute the exact diffuse obstruction and apply both the designated partner and the required `e5f71d79...` theorem to actual inequalities.

## 2. Source-pinned completed inputs

Fresh brain control before this run was `math-research-brain@915fc256ee363b302e6acc0ce0c853a92f86c520`, with OWNER CONTROL revision `2026-09-22.15`. The programme claims file still records the unrestricted target as OPEN.

The current predecessor is account02/B08 r25:

`math-open-problems@ac9b000da88c4923d8a3adb6a0a8bdccbd27ccae`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T093606Z-account02-B08-qform-diffuse-r25/REPORT.md`.

Its actual spectral gate uses

`c_L=(L/2)sqrt(3/5)`,
`beta_L=(3L/16)sqrt(3/5)`.                                      (2.1)

In the `k=1` branch the actual physical cross block has at least two singular values greater than `beta_L`; in the `k=2` branch it has at least one. Its target-valid Hadamard family realizes these counts sharply while all selected large eigenvectors are delocalized.

The newest completed designated partner is account03/B08 r32:

`math-open-problems@2cb64b71f8aafa0892547dffebcf6af647ea7c64`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T102108Z-account03-B08-qform-diffuse-r32/REPORT.md`.

The theorem used here is `QFORM-SCALAR-SCHUR-E2-LINF-v1`: if one ORIGINAL coordinate has quadratic coefficient `a!=0`, and after exact scalar Schur complementation a literal residual physical cross block `M` satisfies `Delta_2=E_2(M)>0`, then

`||p_Q||_infinity <36.45 |a|^(-1/2) Delta_2^(-1/8)`.           (2.2)

It retains arbitrary same-bank residual curvature, all other residual couplings and extra spectrum. It assumes no rank bound on `M`.

The required fixed Claude source was read at exactly

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`
with `RESULTS.md`, `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md`.

Two completed results are used below.

1. **D5:** for every original-coordinate cross block `B`, with `Z_5=e_5(B^T B)`, no marginal condition is required and

`||p_Q||_infinity <=5 sqrt(2e) Z_5^(-1/10)`.                    (2.3)

All same-side blocks and outside couplings remain arbitrary, and the Fourier proof gives a continuous density.

2. **Fresnel--Brascamp--Lieb:** for an exact diffuse rank-`r` spectral form, the source-valid rank-`r` consequence used already by r25 is

`||p_Q||_infinity <= [4r/(r-2)] |det Lambda|^(-1/r)`            (2.4)

when every physical spectral-row leverage is at most `1/2`. This is a deterministic frame argument in original product coordinates, not independence after rotation.

The later volume-stability continuation `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba` was also read. In particular, its two-cross collective-tail extension remains available, but the D5 reduction below is completely marginal-free and is therefore the cleaner first router for the arbitrary complementary cross spectrum.

## 3. New structural router: the actual hybrid plus D5 is either paid or within a rank-four cross tube

Put

`beta=(3/16)sqrt(3/5)=0.145236875482778...`.                    (3.1)

Let `B` be the **actual full physical cross block** at the r25 gate, including every complementary spectral contribution, and write its singular values as

`s_1>=s_2>=...`.

### Theorem 3.1 — `QFORM-ACTUAL-GATE-D5-RANK4-ROUTER-v1`

Fix `eta in (0,1)`. In the `k=1` branch, where

`s_2(B)>=beta L`,                                                (3.2)

if `s_5(B)>=eta L` then the full ambient law has a continuous density and

`||p_Q||_infinity
 <=5 sqrt(2e) beta^(-2/5) eta^(-3/5) L^(-1)`.                  (3.3)

In the `k=2` branch, where

`s_1(B)>=beta L`,                                                (3.4)

if `s_5(B)>=eta L` then

`||p_Q||_infinity
 <=5 sqrt(2e) beta^(-1/5) eta^(-4/5) L^(-1)`.                  (3.5)

Consequently, at `eta=1/64`, either

`k=1: ||p_Q||_infinity <306/L`,                                 (3.6)

`k=2: ||p_Q||_infinity <478/L`,                                 (3.7)

or

`dist_op(B,{rank<=4})=s_5(B)<L/64`.                             (3.8)

#### Proof

For `k=1`, the five-volume contains the positive term using the first five singular directions, hence

`Z_5=e_5(B^T B)
 >=s_1^2 s_2^2 s_3^2 s_4^2 s_5^2
 >=beta^4 eta^6 L^10`.                                         (3.9)

Insert (3.9) into D5, giving (3.3). The `k=2` case similarly gives

`Z_5>=beta^2 eta^8 L^10`,                                      (3.10)

which yields (3.5). Numerically, at `eta=1/64`, the constants are

`305.85069281929094`, `477.70616146059024`.                     (3.11)

If the corresponding paid branch fails, `s_5<eta L`; Eckart--Young gives (3.8). QED.

This theorem is useful specifically because `B` is the actual cross block. No selected rank-three component is peeled off and no complementary spectrum is discarded. Arbitrary high-rank complementary cross curvature is therefore harmless unless it collapses into a fixed rank-four operator tube.

The canonical r25 Hadamard hybrids lie sharply in the survivor: their cross rank is only three, so `s_5=0` identically. They are therefore appropriate stress tests for the genuinely mixed low-rank branch rather than counterexamples to (3.6)-(3.7).

## 4. New positive receiver: a localized scalar pivot plus two actual cross directions

The partner theorem (2.2) combines with one elementary singular-value estimate to pay a useful localized subbranch without any rank assumption on the rest of the form.

Partition the ORIGINAL coordinates as one scalar pivot, two disjoint residual banks `I,J`, and arbitrary outside coordinates. Write the relevant quadratic matrix entries as

`a=A_00`,
`u=A[I,0]`,
`v=A[J,0]`,
`B=A[I,J]`.                                                      (4.1)

After exact scalar Schur completion, the literal residual cross block is

`M=B-u v^T/a`.                                                   (4.2)

Put

`r=||u||_2 ||v||_2/|a|=||u v^T/a||op`.                         (4.3)

### Theorem 4.1 — `QFORM-HYBRID-SCALAR-SCHUR-CROSS2-ROUTER-v1`

If `a!=0` and `s_2(B)>r`, then

`boxed:
 ||p_Q||_infinity
 <36.45 [ |a| (s_2(B)-r) ]^(-1/2).
`                                                                    (4.4)

In particular, if an actual `k=1` gate has

`s_2(B)>=beta L`, `|a|>=alpha L`, `r<=beta L/2`,                (4.5)

then

`boxed:
 ||p_Q||_infinity
 <36.45 sqrt(2/(alpha beta)) L^(-1).
`                                                                    (4.6)

#### Proof

Weyl's singular-value inequality applied to the rank-one Schur update gives

`s_2(M)>=s_2(B)-r>0`.                                           (4.7)

For every matrix,

`E_2(M)=sum_(i<j) s_i(M)^2 s_j(M)^2
 >=s_1(M)^2s_2(M)^2>=s_2(M)^4`.                                (4.8)

Insert (4.7)-(4.8) into the partner bound (2.2). This gives (4.4), and (4.6) follows from (4.5). QED.

Everything not displayed in (4.1) is left inside the partner theorem's full ambient residual form. This is therefore compatible with conditioning localized ORIGINAL coordinates: such conditioning only changes affine terms and deletes conditioned rows/columns before (4.1) is applied.

The complementary structural alternative is also explicit. If a pivot obeys `|a|>=alpha L` but fails the small-update condition in (4.5), then

`||u||_2||v||_2 > (alpha beta/2)L^2`.                            (4.9)

Thus a localized scalar pivot is either paid by (4.6) or creates a genuine two-sided physical star product. The remaining diffuse case is precisely the regime in which no scalar pivot carries a fixed fraction of the child curvature.

## 5. Exact Schur anatomy of the target-valid diffuse Hadamard hybrid

Now return to the r25 construction. Let `m=2^q`, `U` be the first three normalized columns of the `m x m` Sylvester--Hadamard matrix, and

`A_(m,k,d)=
 [ U P U^T          U(I-P)U^T ]
 [ U(I-P)U^T        U P U^T   ]`,                              (5.1)

where `k in {1,2}`, `0<d<=1/10`, and `P` has `k` entries `1-d` and the remaining entries `1/5`.

Its spectrum is

`1,1,1`, together with `k` copies of `1-2d` and `3-k` copies of `-3/5`. (5.2)

Thus it has exactly three eigenvalues of modulus at least one. Its selected three-large-eigenvector frame has maximum physical row leverage `3/(2m)->0`. It is a literal target-valid diffuse family.

Let

`D=UPU^T`, `B=U Q U^T`, `Q=I-P`.                               (5.3)

Choose **any** physical scalar pivot in the left half; the right-half calculation is identical. The corresponding row of `U` is

`r=z^T/sqrt(m)`, `z in {+-1}^3`.                                (5.4)

Put

`s=z^T P z=tr P`.                                                (5.5)

Because every Hadamard row has equal squared coordinates, the scalar pivot is exactly

`a=r P r^T=s/m`.                                                 (5.6)

After deleting that row on the left, the exact Schur cross block from the remaining left coordinates to the full right bank is

`M=U_T K U^T`,
`K=(I-P z z^T/s)Q`.                                              (5.7)

The key cancellation is

`z^T K=0`.                                                       (5.8)

Since

`U_T^T U_T=I-z z^T/m`,                                          (5.9)

(5.8) implies

`K^T U_T^T U_T K=K^TK`.                                        (5.10)

Therefore the nonzero singular values of the **physical** Schur block `M` are exactly those of the `3x3` deterministic matrix `K`; there is no asymptotic error and no rotated-independence statement.

Let

`L_0=I-P z z^T/s`, so `K=L_0Q`.                                 (5.11)

Since `z^T P z=s`, `L_0` is a rank-two idempotent. Its right null vector is `Pz`, its left null vector is `z`, and

`adj(L_0)=Pz z^T/s`.                                            (5.12)

For `d>0`, `Q` is invertible, so

`adj(K)=adj(Q)adj(L_0)
       =(det Q/s) Q^(-1)Pz z^T`.                               (5.13)

As `rank K=2`, the complete physical second-compound mass is

`E_2(M)=E_2(K)=||adj K||_F^2
 =3 (det Q)^2 s^(-2) ||Q^(-1)Pz||_2^2`.                        (5.14)

All signs in `z` disappear from (5.14), so **every physical pivot has the same exact Schur-E2 value**.

### 5.1 One-child branch `k=1`

Here

`P=diag(1-d,1/5,1/5)`,
`Q=diag(d,4/5,4/5)`,
`s=7/5-d`.                                                       (5.15)

Equation (5.14) becomes

`boxed:
 Delta_1(d):=E_2(M)
 =(768/625)
   [(1-d)^2+d^2/8]/(7/5-d)^2.
`                                                                    (5.16)

If

`f(d)=[(1-d)^2+d^2/8]/(7/5-d)^2`,                               (5.17)

then direct differentiation gives a numerator proportional to

`23d-16`.                                                        (5.18)

Hence `Delta_1` is decreasing throughout `0<d<=1/10`, and

`boxed:
 Delta_1(d)>=Delta_1(1/10)
 =62304/105625
 =0.5898603550295858....
`                                                                    (5.19)

There is no residual-E2 loss as `d->0`. In fact one Schur singular value is exactly `4/5`, while the other remains at least `0.9600...` on this interval.

### 5.2 Two-child branch `k=2`

Now

`P=diag(1-d,1-d,1/5)`,
`Q=diag(d,d,4/5)`,
`s=11/5-2d`,                                                     (5.20)

and (5.14) gives

`boxed:
 Delta_2(d)
 =(48/25)
 [2(1-d)^2d^2+d^4/16]/(11/5-2d)^2.
`                                                                    (5.21)

Moreover `Delta_2(d)/d^2` is decreasing on `0<d<=1/10` and

`Delta_2(d)>= (7779/10000)d^2`.                                 (5.22)

As `d->0`,

`Delta_2(d)~(96/121)d^2`.                                       (5.23)

Here one Schur singular value is exactly `d`; the second stays bounded below. Thus the newest E2 receiver distinguishes the two hybrid states exactly as expected: `k=1` retains two robust cross directions after scalar Schur complementation, whereas `k=2` does not.

## 6. Actual inequalities from the designated partner, and why they do not close the diffuse endpoint

### 6.1 `k=1`

Every physical pivot has

`a=(7/5-d)/m >=(13/10)/m`.                                      (6.1)

Combine (5.19) with the completed partner theorem (2.2):

`||p_Q||_infinity
 <36.45 sqrt(m/(7/5-d)) Delta_1(d)^(-1/8)
 <34.15 sqrt(m).`                                               (6.2)

This is an actual full-form inequality for every cap-one product source. The point is not the numerical quality: it proves that the new partner theorem already sees a **uniformly nondegenerate residual E2** on the exact diffuse hybrid. Its only dimension loss is the scalar coefficient `a=Theta(1/m)`.

Thus the tempting closure

`one child + two cross -> choose one physical scalar pivot -> Schur E2 -> Linfinity`

is not dimension-free even on a source-valid target family. The obstruction is not failure of E2 or an adversarial complementary spectrum; it occurs in the clean exact-rank-six model because a delocalized child square is distributed among `m` scalar pivots.

### 6.2 `k=2`

Here

`a=(11/5-2d)/m >=2/m`.                                         (6.3)

Using (5.22) in (2.2) gives the actual inequality

`||p_Q||_infinity
 <26.60 sqrt(m) d^(-1/4).`                                     (6.4)

Now both losses are genuine: the scalar pivot vanishes like `m^-1`, and the residual E2 vanishes like `d^2`. This quantitatively confirms that the `k=2` state needs a mechanism using two child directions rather than a single-square compiler.

### 6.3 Required fixed source applied to the same actual family

The divergence in (6.2)-(6.4) is a **mechanism obstruction, not a QFORM counterexample**. The entire nonzero six-dimensional spectral range of (5.1) is diffuse, with row leverage `3/m<=1/2` for `m>=6`. Apply the completed Fresnel--Brascamp--Lieb theorem (2.4) with `r=6`.

For `k=1`, uniformly over `0<d<=1/10`,

`boxed:
 ||p_Q||_infinity
 <=6[(4/5)(3/5)^2]^(-1/6)
 =7.3833337852872525....
`                                                                    (6.5)

For `k=2`,

`boxed:
 ||p_Q||_infinity
 <=6[(4/5)^2(3/5)]^(-1/6)
 =7.037677794089426....
`                                                                    (6.6)

These are continuous-density bounds for every admissible product law. They use the fixed `e5f71d79...` theorem at an actual target inequality. No random spectral coordinates are introduced; the spectral frame appears only in the deterministic Fresnel representation.

The contrast between (6.2) and (6.5) is the exact information needed for the next proof step: a valid compiler must aggregate the many weak physical manifestations of the child square **before** paying the half-density singularity. Selecting one scalar pivot first necessarily loses `sqrt(m)` on this diffuse family.

## 7. Interaction with localized-coordinate conditioning

R25 proves that conditioning an arbitrary set of `h<=m/100` ORIGINAL coordinates preserves the hybrid gate on (5.1): in the `k=1` state there are still exactly two gate-large cross singular values and one child direction, while in the `k=2` state there is still exactly one gate-large cross direction and two child directions. For fixed `h` or `h=o(m)`, the missing cross singular values can still tend to zero.

The positive theorem of Section 4 is fully compatible with such conditioning, because it is applied only after the conditioned principal matrix is formed. But the exact stress family shows why conditioning a bounded number of coordinates does not solve the diffuse endpoint: the surviving physical scalar pivots still have size `Theta(1/m)`.

Thus the localized/diffuse split can now be phrased cleanly at the mixed receiver:

* a localized pivot with `|a|` of target scale and moderate Schur update is paid by Theorem 4.1;
* arbitrary high cross-rank complement is paid or reduced to a rank-four tube by Theorem 3.1;
* the source-valid diffuse survivor has low cross rank and every scalar child pivot of size `Theta(1/m)`.

No step assumes that localized conditioning creates the missing cross rank.

## 8. First remaining implication

The next exact B08 obligation is

**`QFORM-K1-GROUPED-CHILD-SQUARE-E2-COMPILER-v1` — OPEN.**

Starting from the genuine `k=1` state after the actual spectral gate and rank-four routing, prove a full-ambient Linfinity bound that combines

1. one **collective actual child eigendirection**, spread over many original coordinates, with
2. the two-cross / residual-E2 currency already available from account03/B08,

without selecting one scalar pivot before smoothing. The theorem must retain arbitrary same-bank curvature and arbitrary complementary spectrum, and it must reduce to the dimension-free Fresnel bound on the Hadamard family above. The exact calculation (5.16)-(6.2) shows that a proof based on one physical scalar Schur pivot cannot be dimension-free even when the Schur residual E2 is uniformly excellent.

The `k=2` branch remains a separate, strictly harder obligation: its exact scalar-Schur E2 is only `Theta(d^2)`, so a successful compiler must genuinely use **two** child directions together with the one forced cross direction.

This is compatible with the current tiny-N3 reduction: in that regime the amplified R1/E2/BICORE determinant-core descendants remain a parallel debt, and a small matrix tail may not be deleted as a small random quadratic perturbation.

## 9. Checks and status

`CHECKS.py` verifies:

* the D5 constants at `eta=1/64`;
* the exact endpoint fractions `62304/105625` and `7779/10000`;
* the partner bounds `<34.15 sqrt(m)` and `<26.60 sqrt(m)d^(-1/4)`;
* the Fresnel constants (6.5)-(6.6);
* direct finite Sylvester-Hadamard Schur complements for `m=8,16,32`, `k=1,2` and three values of `d`, agreeing with (5.16),(5.21) to absolute error below `1e-15`.

The executed output terminates `QFORM_B08_R26_CHECK_PASS`.

The full universal essential-density conjecture remains **OPEN**. Global continuity remains **OPEN**. The D5 and exact-range Fresnel branches above yield continuous densities; the partner scalar-Schur theorem supplies an essential bound in its branch but does not by itself assert global continuity.
