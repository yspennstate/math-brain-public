SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T14:49:13Z.
attacking: localized-triangle plus second-arm receiver: convert Schur-cancellation packet into a physical 3x3 determinant or a two-bank fractional smoothing inequality while retaining arbitrary curvature.

# fleet03/B08 r40 — triangle rank-one escape and a cancellation-stable pair receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T144913Z-fleet03-B08-qform-diffuse-r40`  
Owner control used at final refresh: `2026-09-22.15`  
Assignment: diffuse eigenvector case / quantitative inequalities and rigorous computations  
Status: `NEW SUPPORTING STRUCTURAL ROUTER + PROVED SCOPED TARGET FAMILY / FULL TARGET OPEN / INDEPENDENT REVIEW PENDING`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. Global continuity remains OPEN. This run keeps all variables in original independent coordinates and assumes only one-dimensional density caps `0<=f_i<=1`. No moment, compact-support, connected-support, Gaussian, log-concavity, iid, post-rotation-independence, arbitrary-joint coarea, pointwise scalar Fresnel decay, or worst-fiber supremum is used.

The first essential question from r38 was whether its localized Schur-cancellation packet can itself be converted into a well-conditioned physical pair or a nonzero three-coordinate determinant. The answer is **no**: there is an exact rank-one endpoint. The useful replacement proved here is an exhaustive quantitative router: either the triangle carries real two-/three-coordinate determinant currency, or the full third singular direction is forced into the outside cross block/complement. In the diffuse rank-three part of that outside cross block, the newest volume-stability theorem pays the full form continuously. Separately, the exact rank-one endpoint can be paid when the second physical arm is an invertible pair; this includes an explicit target-valid maximally-cancelled anisotropic family with a universal `128/L` bound.

## 1. Source-valid inputs actually used

### 1.1 Immediate B08 predecessor

`yspennstate/math-open-problems@1a70497363989dfea9fa4ce9e515fa279677df69`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T131815Z-fleet03-B08-qform-diffuse-r38/REPORT.md`.

Its scalar-Schur anisotropic-core router says that, for outer physical coefficient `a=epsilon L`, pre-completion core `L diag(R,R^{-1})`, and couplings `u_i,v_i`, either a physical post-Schur `2x2` determinant survives and is analytically paid, or an actual arm satisfies

`|u_i v_i| > (1-theta)L|h_i|/2`.

At `theta=1/2` this gives `|u_i v_i|>L|h_i|/4`. r38 explicitly left the localized-triangle-plus-second-arm receiver unpaid.

### 1.2 Orientation-free rank-two half-Riesz theorem

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For any two-dimensional original-coordinate projection with symmetric invertible `2x2` matrix `B` and **arbitrary affine term**,

`sup_t E |Y^T B Y + ell^T X-t|^{-1/2} <=128 |det B|^{-1/4}`.       (1.1)

This theorem is used below after conditioning only original coordinates, so its arbitrary-affine scope is essential.

### 1.3 Newest required volume-stability theorem

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md` and `PEER_TAIL_EXTENSION.md`.

The exact part used here is the baseline perturbative diffuse exit. If an original-coordinate cross block `M` has a rank-three reference `M0` with

`s3(M0)>=gamma`, `max_i (P_range(M0))_ii<=1/2`, `||M-M0||op<=gamma/16`,

then the **full ambient form** has a continuous `C_0` density with

`||p_Q||infinity <23/gamma`.                                      (1.2)

All self blocks, outside couplings and affine terms are retained. In our application `M0=M`, so the perturbation term is exactly zero.

### 1.4 Ridge/spectral-window exit

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

After scaling by `L`, if the projection onto all spectral directions `|lambda(A)|>=L/64` has every original-coordinate diagonal at most `1/32`, then

`||p_Q||infinity <64/L`,                                           (1.3)

and the density is continuous. This is used only as the already-proved global diffuse-window exit; failure means a genuine high spectral-window leverage coordinate remains.

### 1.5 Designated partner fleet04/B08

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B08/20260923T091414Z-fleet04-B08-QFORM-r1/REPORT.md`.

For

`Q_(R,L)=L X0^2+2LR U1V1+2L R^{-1} U2V2`, `R>=3`,

the completed partner theorem gives the actual target inequality

`boxed: ||p_(Q_(R,L))||infinity <7.251/L.`                         (1.4)

This is the non-cancelled anisotropic endpoint. Section 5 constructs and pays the exact maximally-cancelled companion endpoint.

## 2. Exact physical-triangle algebra

Consider an actual original-coordinate principal triangle

```
T = [[a,u,v],
     [u,b,h],
     [v,h,c]],        a != 0.
```

Define its pivoted physical minors

`d1=ab-u^2`, `d2=ac-v^2`, `k=ah-uv`.                            (2.1)

### Lemma 2.1 — triangle determinant identity

Exactly,

`boxed: a det(T)=d1 d2-k^2.`                                      (2.2)

Also, with `w=(a,u,v)^T`,

```
T=(1/a) w w^T
  + [[0,0,0],
     [0,d1/a,k/a],
     [0,k/a,d2/a]].                                               (2.3)
```

Both formulas are direct expansion. Define the rank-one defect

`Delta_T := sqrt(d1^2+d2^2+2k^2)/|a|`.                            (2.4)

Then (2.3) gives

`dist_op(T,{rank<=1}) <= Delta_T`.                                (2.5)

The Frobenius expression in (2.4), not a selected reciprocal minor, is the quantity used below.

### Exact obstruction to the naive localized-triangle implication

Take

`b=u^2/a`, `c=v^2/a`, `h=uv/a`.                                  (2.6)

Then

`d1=d2=k=det(T)=0`,                                               (2.7)

and

`T=(1/a)(a,u,v)^T(a,u,v)` has rank one.                           (2.8)

Yet `uv=ah`. Consequently every fixed packet `|uv|>c0 |a h|` with `c0<1` is satisfied maximally while **every** pivoted `2x2` minor and the `3x3` determinant vanish. Thus the r38 localized product packet alone cannot imply a usable pair, an invertible triangle, or post-Schur `E2`. This is a correction to that possible proof shortcut, not a counterexample to QFORM.

## 3. Main structural theorem: near-rank-one triangle forces an outside spectral escape

Partition the full symmetric matrix by this physical triangle and its complement:

```
A = [[T,C],
     [C^T,D]].                                                    (3.1)
```

Let `s_j` denote singular values in decreasing order.

### Theorem 3.1 — `QFORM-TRIANGLE-RANK1-ESCAPE-v1`

For every `a!=0`,

`boxed: s3(A) <= s1(C)+||D||op+Delta_T.`                          (3.2)

Therefore, if `s3(A)>=L` and `0<rho<1`, at least one of the following holds:

1. **local determinant currency**

   `max{|d1|,|d2|,|k|} > (rho/2)|a|L`;                           (3.3)

2. **outside escape**

   `max{s1(C),||D||op} >= (1-rho)L/2`.                            (3.4)

At the concrete choice `rho=1/4`,

`max{|d1|,|d2|,|k|}>|a|L/8`                                     (3.5)

or

`max{s1(C),||D||op}>=3L/8`.                                     (3.6)

If the r38 outer pivot has `|a|=L`, the first alternative carries an actual physical minor scale `>L^2/8`.

#### Proof

Let

`T1=(1/a) w w^T`,                                                (3.7)

so `rank(T1)<=1`, and put

`R=T-T1`.                                                        (3.8)

By (2.3), `||R||op<=||R||F=Delta_T`. Embed `T1` into the full matrix and write

```
A = diag(T1,0) + E,
E = [[R,C],[C^T,D]].                                             (3.9)
```

The singular-value sum inequality with indices `(2,2)` gives

`s3(A)<=s2(E)+s2(diag(T1,0))=s2(E)`,                             (3.10)

because the second singular value of a rank-one matrix vanishes.

Next write

```
E = diag(R,0) + E0,
E0=[[0,C],[C^T,D]].                                              (3.11)
```

Hence

`s2(E)<=s2(E0)+Delta_T`.                                         (3.12)

Finally

```
E0 = [[0,C],[C^T,0]] + diag(0,D).                                (3.13)
```

The symmetric off-diagonal matrix in (3.13) has singular values `s1(C),s1(C),s2(C),s2(C),...`; in particular its second singular value is exactly `s1(C)`. Another singular-value sum inequality gives

`s2(E0)<=s1(C)+||D||op`.                                         (3.14)

Equations (3.10)-(3.14) prove (3.2).

If `Delta_T<=rho L`, (3.2) and `s3(A)>=L` imply

`s1(C)+||D||op >=(1-rho)L`,                                     (3.15)

and hence (3.4). If `Delta_T>rho L`, then

`sqrt(d1^2+d2^2+2k^2)>rho |a|L`.                                (3.16)

The left side is at most twice `max{|d1|,|d2|,|k|}`, proving (3.3). QED.

### Why this is the correct replacement for the failed shortcut

The rank-one example (2.6) shows no local pair need survive. Theorem 3.1 says exactly where the missing third singular direction must then go: into the physical outside cross block `C` or the complementary principal block `D`. Nothing is discarded probabilistically and no upper bound on coefficient size is assumed.

## 4. Joining this escape to the newest diffuse-volume theorem

The preceding theorem becomes a B08 diffuse/localized router at fixed constants.

Assume `s3(A)>=L` and

`Delta_T<=L/4`.                                                   (4.1)

Then (3.6) holds. If

`||D||op<3L/8`,                                                   (4.2)

we necessarily have

`s1(C)>3L/8`.                                                     (4.3)

Now orient the actual physical cross block as

`M=C^T`,                                                         (4.4)

so its row coordinates belong to the (possibly large) outside bank and its three columns are the physical triangle coordinates. Fix the threshold

`gamma=L/16`.                                                     (4.5)

Exactly one of the following occurs:

### 4A. Diffuse rank-three cross escape

If

`s3(C)>=L/16`                                                    (4.6)

and the projection `P=Proj(range(C^T))` on the outside original-coordinate bank obeys

`max_i P_ii<=1/2`,                                               (4.7)

apply the newest volume-stability theorem with `M0=M`, error `E=0`, and `gamma=L/16`. Its perturbation hypothesis is automatic. Therefore the **full ambient quadratic form**, including this triangle, all of `D`, every other coupling and all affine terms generated by conditioning, has

`boxed: ||p_Q||infinity <368/L`,                                 (4.8)

and `p_Q` has a continuous `C_0` representative.

This is an equation-level application of the required `c2414ef...` result to the r38 cancellation survivor, not a copied citation.

### 4B. Low-cross-rank survivor

If (4.6) fails, then because `C` has only three triangle rows,

`dist_op(C,{rank<=2})=s3(C)<L/16`.                               (4.9)

Thus the unpaid cross geometry is quantitatively in an operator-norm rank-two tube while still carrying `s1(C)>3L/8` from (4.3).

### 4C. High-leverage survivor

If (4.6) holds but (4.7) fails, then an **actual outside original coordinate** has

`P_ii>1/2`.                                                      (4.10)

So failure of the diffuse volume gate produces a genuine localized coordinate, not an unlabelled failure of a Fourier estimate.

Together, (4.8)-(4.10) give the promised quantitative join from the near-rank-one triangle into a paid diffuse-volume branch or the exact two survivor types assigned to B08: high leverage and low cross rank. The only other branch from Theorem 3.1 is complementary curvature `||D||op>=3L/8`; it is not declared paid here.

Independently, the already-completed spectral-window theorem gives a global early exit: if the projection onto `|lambda(A)|>=L/64` has all diagonal entries at most `1/32`, then `||p_Q||infinity<64/L` continuously. Hence every still-unpaid state after the present router is also compatible with a genuine high spectral-window leverage coordinate unless that global exit has already paid it.

## 5. Analytic receiver for the exact rank-one cancellation endpoint

The deterministic obstruction (2.6) is not merely a dead end. If a second physical pair remains invertible on disjoint original coordinates, it can be paid directly while retaining arbitrary outside couplings.

### Theorem 5.1 — `QFORM-RANK1-TRIANGLE-PLUS-PAIR-v1`

Let `S` be three original coordinates and `P` two disjoint original coordinates. Suppose the physical principal block on `S union P` is block diagonal,

`A_[S union P] = diag(sigma c c^T, B)`,                          (5.1)

where `sigma in {+1,-1}`, `c in R^3\{0}`, and `B` is a real symmetric invertible `2x2` matrix. All entries involving coordinates outside `S union P` are arbitrary.

For independent cap-one inputs, the full ambient quadratic form has an essentially bounded density satisfying

`boxed: ||p_Q||infinity <=128 sqrt(3) ||c||_2^{-1}|det B|^{-1/4}.` (5.2)

If `h` is any off-diagonal coefficient of the rank-one triangle, so `h=sigma c_r c_s`, then

`boxed: ||p_Q||infinity <=128 sqrt(3/2)|h|^{-1/2}|det B|^{-1/4}.` (5.3)

Numerically the prefactor in (5.3) is

`128 sqrt(3/2)=156.767343538123...`.                              (5.4)

Continuity is not asserted by this argument.

#### Proof

Condition on every coordinate outside `S union P`. This preserves independence of the five retained original coordinates and turns all outside couplings into arbitrary affine terms.

Choose `j in S` with

`|c_j|>=||c||_2/sqrt(3)`.                                        (5.5)

Condition also on the other two coordinates in `S`. The remaining dependence on `X_j` is a one-variable quadratic with coefficient `sigma c_j^2`, plus an arbitrary linear term. Completing the square and using `f_j<=1`, its conditional density is bounded by

`|c_j|^{-1}|z-z0|^{-1/2}`                                      (5.6)

on the appropriate half-line (and by zero on the other half-line), for a conditioning-dependent vertex value `z0`.

The two coordinates in `P` contribute

`Y^T B Y+ell^T Y+constant`,                                     (5.7)

with arbitrary conditioning-dependent affine vector `ell`. By the orientation-free half-Riesz theorem (1.1), uniformly in every such affine vector and every shift,

`E |Y^T B Y+ell^T Y-t|^{-1/2} <=128 |det B|^{-1/4}.`             (5.8)

Convolving (5.6) with (5.7), still conditionally on the fixed original coordinates, gives

`||p_Q||infinity <=128 |c_j|^{-1}|det B|^{-1/4}`.                (5.9)

Use (5.5) and then average over the conditioning to prove (5.2).

Finally `2|h|=2|c_r c_s|<=||c||_2^2`, so (5.3) follows. QED.

### Clean no-affine refinement

When the rank-one triangle is an independent direct summand with no induced affine term, the one-dimensional product-projection theorem gives density at most `sqrt(2)/||c||_2` for `c^T X_S`. Squaring and applying (1.1) improves (5.3) to

`||p_Q||infinity <=128 |h|^{-1/2}|det B|^{-1/4}.`                (5.10)

This refinement is used only for the explicit direct-sum family below; (5.3) is the conditioning-stable ambient statement.

## 6. A target-valid maximally-cancelled anisotropic family is now paid

Fix `L>0`, `R>=1`, and let

`c_(R,L)=(sqrt(L), sqrt(L/R), sqrt(L/R))`.                       (6.1)

On three original coordinates take

`T_(R,L)=c_(R,L)c_(R,L)^T`.                                     (6.2)

Thus, using the first coordinate as the scalar pivot,

`a=L`, `u=v=L/sqrt(R)`, `b=c=h=L/R`,                             (6.3)

and therefore

`d1=d2=k=0`.                                                     (6.4)

The small anisotropic arm is **exactly cancelled by scalar Schur completion**:

`h-uv/a=0`.                                                      (6.5)

On two further disjoint original coordinates take the large hyperbolic pair

`B_(R,L)=[[0,LR],[LR,0]]`.                                      (6.6)

The five-coordinate matrix

`A^cancel_(R,L)=diag(T_(R,L),B_(R,L))`                           (6.7)

has spectrum

`{ L(1+2/R), +LR, -LR, 0, 0 }`.                                 (6.8)

Hence for every `R>=1` it has at least three eigenvalues of absolute value at least `L`; at `L>=1` it is an actual target matrix.

Here the triangle coefficient `h=L/R` and

`|det B_(R,L)|=(LR)^2`,                                         (6.9)

so

`|h|^{-1/2}|det B_(R,L)|^{-1/4}=L^{-1}`.                        (6.10)

The clean direct-sum refinement (5.10) therefore gives, for **every** admissible product input law,

`boxed: ||p_(X^T A^cancel_(R,L) X)||infinity <=128/L`,           (6.11)

uniformly in the anisotropy `R`.

If arbitrary outside coordinates and couplings are appended while the displayed five-coordinate principal block (6.7) is retained, Theorem 5.1 gives the conditioning-stable bound

`boxed: ||p_Q||infinity <=156.768/L.`                            (6.12)

Thus the maximally-cancelled endpoint of the r38 mechanism is not an obstruction by itself.

## 7. Actual application of the designated partner result

For comparison, the completed fleet04/B08 family is the **non-cancelled** direct sum

`L X0^2+2LR U1V1+2L R^{-1}U2V2`.                                (7.1)

Applying the designated partner theorem at its exact scope gives

`boxed: ||p_Q||infinity<7.251/L.`                                (7.2)

The new family (6.7) instead folds the scalar square and the small arm into the exact rank-one triangle with zero Schur residual and retains the large arm. Equation (6.11) pays that opposite endpoint. The two bounds are therefore genuinely complementary:

- non-cancelled fixed-`E2` anisotropic direct sum: `<7.251/L` by fleet04/B08;
- exact maximal scalar-Schur cancellation: `<=128/L` by Theorem 5.1/clean refinement.

This does **not** prove a uniform interpolation for arbitrary couplings between the two endpoints; that is part of the remaining low-rank/high-leverage work.

## 8. Exact computational checks

`CHECKS.py` and `CHECKS.txt` in this run directory execute the following finite regression tests:

1. 5,000 random physical triangles verify (2.2) to maximum floating error `3.5527136788e-14`.
2. The exact rank-one decomposition (2.3) has maximum error `7.1054273576e-15`.
3. 5,000 random full block matrices verify (3.2), with maximum observed violation `0.0`.
4. The exact target-valid family (6.7) was checked for `L=2.5` and `R=1,3,10,100`; each instance has at least three eigenvalues of magnitude at least `L`.
5. The constants `128 sqrt(3/2)=156.76734353812338` and `9 sqrt(3)e/2=21.186910062820317` are recorded.

The checker terminates `QFORM_B08_R40_CHECK_PASS`. These finite tests support the algebra and constants; they are not proof of the universal theorem.

## 9. What changed in the proof map

Before this run, the r38 localized product packet could have been misread as likely to produce a good physical pair after one more inequality. The exact rank-one example (2.6) rules that out. The replacement map is now quantitative and correction-safe:

1. a non-negligible triangle rank-one defect produces actual physical determinant currency by (3.3);
2. a small defect forces scale into the outside cross/complement by (3.4);
3. a rank-three diffuse outside cross is paid continuously by the newest volume theorem, with the concrete bound `368/L` at threshold `L/16`;
4. failure of that diffuse cross payment is explicitly a rank-two cross tube or a high-leverage original coordinate;
5. exact maximal triangle collapse plus an invertible second pair is analytically payable, and an explicit target-valid anisotropic cancellation family has bound `128/L`.

This is a stricter join between the diffuse-volume branch and the localized/low-rank survivors than r38 supplied.

## 10. Remaining gap

The unrestricted conjecture remains **OPEN**. The first B08 debt after this run is now:

`QFORM-LOWRANK-HIGHLEVERAGE-TWOARM-INTERPOLATION-v1`.

One must handle the states where the triangle is near rank one, the outside cross block lies in the quantitative rank-two tube or has a high-leverage coordinate, and the second arm is not an isolated invertible principal pair because arbitrary within-bank curvature/cross-couplings interact with it. The new rank-one-plus-pair theorem pays the exact block-separated endpoint, not arbitrary triangle-pair coupling. The complementary-curvature branch `||D||op>=3L/8` also remains to be integrated with the global high-spectral-leverage/ridge router.

Essential boundedness is proved for Theorem 5.1 and the explicit cancellation family; continuity is **not** proved there. Continuity is proved on the volume-stability branch (4.8) and on the spectral-window branch (1.3). A full candidate would still need every sign/degenerate case and two independent end-to-end reviews.

## 11. Execution/status notes

The current UTC hour already contained the canonical fleet03/B08 login for an earlier incomplete run id `20260923T142157Z-fleet03-B08-qform-diffuse-r39`; protocol forbids overwriting it. This run therefore recorded its own unique start/finish records while preserving that login. No mathematical report/handoff for r39 was present at the checked paths, so no r39 theorem was assumed.

Repository access occurred, but no authenticated native brain retrieval/receiver-use evidence was exposed; status remains `WITHOUT_VERIFIED_BRAIN`. No schedule/task identity, enabled/paused state, cadence, notification, email, permission, public-release setting, or paid model/API/Codex setting was changed.
