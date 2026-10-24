# account01/B16 — exact two-bank innovation/slope decomposition at the ultra-coloop boundary

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T20:42:05Z.
attacking: projection-product interaction in the true near-coloop two-bank endpoint; identify exactly what the two one-bank innovations and inter-bank slope separation can and cannot pay, then apply the newest completed account02/B16 receiver to an actual target family.

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T204205Z-account01-B16-QFORM-auto11`  
**Status:** `NEW EXACT STRUCTURAL IDENTITY + REFUTED INTERMEDIATE LOWER-BOUND MECHANISM + LATEST PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not claimed by the new structural theorem or the partner application below; the unrestricted continuity problem remains separate/open.

## 1. Source boundary and corrections actually used

Fresh control was read from `yspennstate/math-research-brain` main before the work, under OWNER CONTROL revision `2026-09-22.15`, with QFORM as the sole research target and no B16 stop. The full conjecture remains OPEN / NOT PROVED / NOT DISPROVED.

The mathematical inputs pinned for this report are:

1. **Newest completed designated partner account02/B16 r36:** `yspennstate/math-open-problems@be8062b160868bcc71aff45a77c56ff2d0501a9a`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T203140Z-account02-B16-QFORM-r36/REPORT.md`, blob `57cf025ef533e6cfad52761553dfc9013d486ec0`. Its theorem `QFORM-FRESH-HUB-DIVISIBLE-TWIST-ABSORPTION-v1` says that for an untouched independent cap-one physical hub `H`, arbitrary light-source functions `L,V,T`, `||p_(L,V)||_infinity<=M`, and
   
   `Q=2 gamma H L+2LT+alpha L^2+2delta LV+kappa V^2`, `gamma*kappa!=0`,
   
   one has
   
   `||p_Q||_infinity <=3*2^(2/3) M^(2/3)|gamma^2 kappa|^(-1/3)`.
   
   The dependence of `T` on the same leaf sources as `(L,V)` is allowed. The theorem uses the untouched physical source before the curved trace; it does not infer projected independence.

2. **Current two-bank hard-chamber geometry:** account03/B16 r30, `yspennstate/math-open-problems@3b18a20df2659c5c26d6853e69ceae081a3abc7e`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T162348Z-account03-B16-QFORM-r30/REPORT.md`. In the surviving exact-rank-three near-coloop branch it supplies a hub row `r_0=sqrt(h)e`, `h>63/64`, and a partition of all leaves into disjoint original-coordinate banks `J,K` with
   
   `(1/4)I_2 <= G_J,G_K <=(3/4)I_2`, `G_J+G_K=I_2`.

3. **Current punctured-hub reduction:** account03/B16 `yspennstate/math-open-problems@439aec7deecbf989b3885d5038861959a2e18ddb`, which pays the exact zero pivot and the outer nonzero collar, and proves that conditional scalar cap plus a planar marginal cap do **not** control an arbitrary nonzero-pivot quadratic.

4. **Fresh arbitrary-joint warning:** `yspennstate/math-open-problems@696dde471191684734577b129bd9f4cc6074dadc`, `proofnet24/QFORM-density/interactive/20260923T204332Z-arbitrary-joint-central-obstruction/REPORT.md`. Even very strong coordinate marginal caps for an arbitrary dependent joint law do not replace original-product provenance in the nonlinear trace.

The live corrections are preserved throughout: no independence after spectral rotation, no arbitrary-joint indefinite coarea step, no worst-fiber/conditional-height supremum, no law-uniform pointwise stationary-phase decay, and no deletion of a small coefficient multiplying an unbounded source.

## 2. Exact two-bank least-squares coordinates

Work in the exact-rank-three Parseval frame. Thus

`A=R Lambda R^T`, `R^T R=I_3`,

and choose the near-coloop hub row

`r_0=sqrt(h)e`, `||e||=1`.

Identify `e^perp` with `R^2` and write every leaf row as

`r_i=alpha_i e+z_i`, `z_i in R^2`.

Parseval gives the exact identities

`sum_i alpha_i^2=1-h`,
`sum_i alpha_i z_i=0`,
`sum_i z_i z_i^T=I_2`.                                           (2.1)

Partition the leaves into `J disjoint_union K`, and put

`G_B=sum_(i in B) z_i z_i^T`, `B in {J,K}`.                    (2.2)

Assume `G_J,G_K` are positive definite; in the r30 packet they satisfy the stronger balanced inequalities above.

For each bank let `Z_B` denote the `2 x |B|` matrix whose columns are the `z_i`, and let `alpha_B=(alpha_i)_(i in B)`. Define the least-squares slope

`q_B=G_B^(-1) Z_B alpha_B`                                      (2.3)

and residual

`eta_B=alpha_B-Z_B^T q_B`, `delta_B=||eta_B||_2`.               (2.4)

Then, by construction,

`Z_B eta_B=0`.                                                   (2.5)

The quantities `delta_B` are exactly the source-level longitudinal innovations left after the best fit to that bank's transverse two-row span. They are the objects whose smallness makes a one-bank rank-one Fresnel determinant degenerate.

## 3. Main theorem — coupled innovation/slope identity

### Theorem `QFORM-TWO-BANK-COUPLED-INNOVATION-GRAM-IDENTITY-v1`

Under (2.1)--(2.5), let

`d=q_J-q_K`.                                                     (3.1)

Then

`G_J q_J+G_K q_K=0`,                                            (3.2)

and, because `G_J+G_K=I_2`,

`q_J=G_K d`, `q_K=-G_J d`.                                     (3.3)

Moreover the near-coloop defect admits the **exact nonnegative decomposition**

`boxed:
 1-h
 =delta_J^2+delta_K^2+d^T G_J G_K d.
`                                                                    (3.4)

Let

`V_mix := sum_{i<j in J, k in K} det(r_i,r_j,r_k)^2
        + sum_{i in J, j<k in K} det(r_i,r_j,r_k)^2`             (3.5)

be the total squared leaf-only three-volume involving both banks. Then

`boxed:
 V_mix
 =d^T G_J G_K d
  +delta_J^2(1-det G_J)
  +delta_K^2(1-det G_K).
`                                                                    (3.6)

If in addition

`(1/4)I_2<=G_J,G_K<=(3/4)I_2`,                                  (3.7)

then

`boxed:
 V_mix >=(3/16)||d||_2^2+(7/16)(delta_J^2+delta_K^2),
`                                                                    (3.8)

while

`boxed:
 1-h >=delta_J^2+delta_K^2+(3/16)||d||_2^2.
`                                                                    (3.9)

In particular

`delta_J,delta_K <=sqrt(1-h)`,
`||q_J-q_K||_2 <=sqrt((16/3)(1-h))`,                              (3.10)

and from (3.3)

`||q_J||_2,||q_K||_2 <=(3/4)sqrt((16/3)(1-h))`.                 (3.11)

### Proof

The global orthogonality relation in (2.1), together with (2.3)--(2.5), gives

`0=sum_i alpha_i z_i=G_J q_J+G_K q_K`,

which proves (3.2). Since `q_K=q_J-d`, `G_J+G_K=I_2` gives

`q_J-G_K d=0`; hence `q_J=G_Kd` and `q_K=-G_Jd`, proving (3.3).

For a bank `B`, define its `3 x 3` row Gram

`S_B=sum_(i in B) r_i r_i^T`.

In the basis `(e,e^perp)`, least-squares orthogonality (2.5) gives exactly

`S_B=
 [[q_B^T G_B q_B+delta_B^2, q_B^T G_B],
  [G_B q_B,                         G_B ]].`                    (3.12)

The Schur complement of `G_B` therefore yields

`det S_B=delta_B^2 det G_B`.                                    (3.13)

Summing the two bank Grams and using (2.1),

`S_J+S_K=diag(1-h,I_2)`.                                        (3.14)

Hence

`1-h=det(S_J+S_K)`.

On the other hand its upper-left entry equals

`q_J^T G_J q_J+q_K^T G_K q_K+delta_J^2+delta_K^2`.

Substitute (3.3). Since `G_K=I-G_J`, the two matrices commute, and

`q_J^T G_J q_J+q_K^T G_K q_K
 =d^T[G_K G_J G_K+G_J G_K G_J]d
 =d^T G_J G_K(G_J+G_K)d
 =d^T G_J G_K d.`                                               (3.15)

This proves (3.4).

Now apply Cauchy--Binet. `det S_B` is exactly the sum of squared determinants of all triples drawn entirely from bank `B`, while `det(S_J+S_K)=1-h` is the corresponding sum over all leaf triples. Subtracting the two pure-bank contributions gives

`V_mix=(1-h)-delta_J^2 detG_J-delta_K^2 detG_K`.

Insert (3.4) to obtain (3.6).

Under (3.7), the eigenvalues of `G_J` lie in `[1/4,3/4]`, and those of `G_K=I-G_J` are their complements. Hence

`G_JG_K >=(3/16)I_2`.                                           (3.16)

Also `det G_B<=9/16`, so `1-detG_B>=7/16`. Equations (3.8)--(3.11) follow immediately. QED.

## 4. Consequence: the proposed two-slope reciprocal currency cannot be universal

The identity changes the interpretation of the r30/r35 residual chamber. The newest partner r35 identified a one-bank Fresnel determinant proportional to the square of the genuine source innovation `delta_B`. A natural next hope was that, when both `delta_J,delta_K` are tiny, the **inter-bank slope separation** `||q_J-q_K||` must remain order one and can replace them.

Equation (3.4) proves the opposite in the true ultra-coloop limit: all three quantities are charged to the same small Parseval defect `1-h`. As `h->1`,

`delta_J ->0`, `delta_K->0`, `q_J-q_K->0`                       (4.1)

simultaneously. Therefore no proof of the full near-coloop branch can rely on a universal positive lower bound for one of these three currencies or on an estimate containing their reciprocal without an additional hub-stable mechanism.

This is not a QFORM counterexample. It is a rigorous refutation of the intermediate structural implication

`"two one-bank innovations small => inter-bank slope separation universally large"`.

The correct limiting receiver has to stay finite at the exact coloop `h=1`. The newest account02/B16 fresh-hub theorem does exactly that at zero physical hub pivot; the remaining analytic problem is its stability under the genuinely nonzero fresh physical hub square in the punctured collar.

## 5. Exact target witness where every innovation/slope currency vanishes

The failure is not merely asymptotic. Take five physical coordinates and the Parseval spectral rows

`r_0=(1,0,0)`,
`r_1=(0,1/sqrt(2),0)`,
`r_2=(0,0,1/sqrt(2))`,
`r_3=(0,1/sqrt(2),0)`,
`r_4=(0,0,1/sqrt(2))`.                                         (5.1)

Then `R^T R=I_3`. Let

`J={1,2}`, `K={3,4}`.

We have

`h=1`, `G_J=G_K=(1/2)I_2`,
`alpha_i=0`, `delta_J=delta_K=0`, `q_J=q_K=0`, `V_mix=0`.       (5.2)

Choose the spectral core

`Lambda=[[0,1,0],[1,0,0],[0,0,1]]`.                            (5.3)

Its eigenvalues are exactly `{1,-1,1}`. Thus

`A=R Lambda R^T`                                                (5.4)

is an exact-rank-three member of the owner's target even though every one-bank innovation and the inter-bank slope-separation currency in (3.4) vanish exactly.

Writing

`L=(X_1+X_3)/sqrt(2)`, `V=(X_2+X_4)/sqrt(2)`,                  (5.5)

the quadratic form is

`Q=2X_0 L+V^2
  =sqrt(2)X_0(X_1+X_3)+(X_2+X_4)^2/2`.                         (5.6)

This witness is useful precisely because the target remains healthy at the point where a reciprocal innovation/slope strategy has zero denominator.

## 6. Newest designated partner r36 applied to an actual inequality

The witness (5.6) is paid immediately by the newest account02/B16 theorem. The physical source `H=X_0` is untouched and independent of all leaves. The pair `(L,V)` is an orthonormal two-dimensional projection of the leaf product law, so the actual bounded-density projection theorem gives

`||p_(L,V)||_infinity<=2`.                                      (6.1)

Use partner r36 with

`gamma=1`, `kappa=1`, `T=0`, `alpha=delta=0`, `M=2`.

Then

`boxed:
 ||p_Q||_infinity
 <=3*2^(4/3)
 =7.559526299369239...<7.56.
`                                                                    (6.2)

Thus the exact target point at which every two-bank innovation/slope currency vanishes is nevertheless uniformly controlled by a source-valid fresh-hub receiver.

The same completed partner theorem gives a genuinely higher-dimensional overlapping family, not just the five-variable example. Let a single leaf product bank carry any orthonormal coefficient family

`ell, v, p_1,...,p_m`,

set

`L=<ell,X_leaf>`, `V=<v,X_leaf>`, `P_j=<p_j,X_leaf>`,           (6.3)

and let `epsilon=(epsilon_1,...,epsilon_m)` be arbitrary. With a fresh physical hub `X_0`, define

`Q_epsilon
 =2X_0 L+V^2+2L sum_j epsilon_j P_j`.                          (6.4)

The projected variables `L,V,P_j` may be strongly dependent; only their original product provenance is used. Put

`T=sum_j epsilon_j P_j`.

Again `(L,V)` is an orthonormal two-dimensional projection, so `M<=2`, and r36 yields the dimension- and coefficient-free estimate

`boxed:
 ||p_(Q_epsilon)||_infinity <7.56
`                                                                    (6.5)

for every `m`, every real `epsilon`, and every choice of independent cap-one original source laws.

This family lies in the full spectral target. In the orthonormal carrier `(X_0,L,V,P_1,...,P_m)`, the star block on `(X_0,L,P_1,...,P_m)` has nonzero eigenvalues

`+sqrt(1+||epsilon||_2^2)`, `-sqrt(1+||epsilon||_2^2)`,          (6.6)

while the `V` direction contributes the exact eigenvalue `1`; all remaining carrier eigenvalues are zero. Hence there are always exactly three nonzero eigenvalues of modulus at least one.

This is an actual application of the newest completed partner result to a target-valid inequality with arbitrarily many dependent leaf projections. It also demonstrates why the `T`-dependence is no longer the hard issue: every light term divisible by the hub partner `L` is absorbed before the curved trace.

## 7. A positive punctured-square control in the fully source-split model

The small nonzero fresh-hub square is not intrinsically singular when the three active scalar receivers are genuinely on disjoint source banks. For `a>=0`, put

`b=sqrt(1+a)`

and take three genuinely independent normalized scalar bank outputs `H,L,V` with density caps

`K_H<=1`, `K_L,K_V<=sqrt(2)`.

Consider

`Q_a=aH^2+2sqrt(1+a)HL+V^2`.                                   (7.1)

Its carrier matrix is

`B_a=[[a,sqrt(1+a),0],[sqrt(1+a),0,0],[0,0,1]]`,               (7.2)

whose eigenvalues are exactly

`{1+a,-1,1}`                                                    (7.3)

and whose determinant is `-(1+a)`.

The previously proved account01/B16 theorem `QFORM-DISJOINT-BANK-TRANSVERSE-TRIPLE-v1` (`math-open-problems@85f22101c29c831c4958eef1b2522c78e6966f84`) therefore gives

`||p_(Q_a)||_infinity
 <=C_3*2^(2/3)*(1+a)^(-1/3)
 <=165.434001`,                                                 (7.4)

where `C_3=16sqrt(30)2^(1/4)`.

This remains finite uniformly as `a downarrow0`. Hence the first unpaid punctured-collar difficulty is not merely the presence of `aH^2`; it is the combination of that square with **overlapping leaf provenance** in the true near-coloop packet. That distinction is important for the next receiver.

## 8. What remains

The new identity closes a structural ambiguity but does not prove the unrestricted theorem. In the actual r30 ultra-coloop packet, (3.4) says that chasing a scale-free lower bound on `delta_J`, `delta_K`, or `||q_J-q_K||` cannot close the proof as `h->1`. The newest partner r36 simultaneously shows that all leaf terms divisible by the hub partner are harmless at zero pivot.

The first unpaid B16 implication is therefore sharpened to

`QFORM-PUNCTURED-FRESH-HUB-SQUARE-OVERLAP-STABILITY-v2`:

> In `0<|a|D<2^-12`, retain the untouched physical hub and the original scalar factorization of the overlapping leaf bank while controlling the added physical square `acX_0^2`; the bound must remain finite as both `a->0` and `h->1`, and it must not invert the vanishing currencies in (3.4).

A successful argument must interpolate directly to the r36 zero-pivot fresh-hub trace, or exploit another source-valid curvature resource. Replacing the leaf bank by an arbitrary capped joint law is ruled out by the current caps-only and arbitrary-joint counterexamples.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**
