SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T09:35:25Z.
attacking: QFORM-RANK2-CROSS-NEAR-COLOOP-STABILITY-v1 — convert the remaining three-row TRIANGLE endpoint into a uniformly nondegenerate two-physical-gradient packet, then identify the exact coupled third-source inequality still needed for L-infinity.

# account03/B19 — triangle cross-packet identity and a uniform 2/3 small-ball receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** universal proof assembly / quantitative inequalities and rigorous computations  
**Fresh owner control:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport is not native learned-memory ingestion.  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW TARGET-LEVEL STRUCTURAL + ANALYTIC REDUCTION / FULL QFORM OPEN`.

The unrestricted theorem remains OPEN. This report works only with original-coordinate partitions and arbitrary cap-one product laws. It does not assume moments, bounded or connected support, Gaussianity, log-concavity, post-rotation independence, arbitrary-joint coarea, law-uniform pointwise quadratic-phase decay, or a uniformly large physical principal minor.

## 1. Incoming correction-safe state

The preceding account03/B19 report is

`yspennstate/math-open-problems@4d5181180f8d5e9e14c9b1c5c5e44679c8c212b9`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T080333Z-account03-B19-QFORM-r28/REPORT.md`.

Its exact-rank-three rank-two-cross chamber writes

`A = R M R^T`, `R^T R = I_3`, `s_min(M)>=1`,                    (1.1)

and splits the ORIGINAL coordinates as `I union J`. Put

`P=R_I`, `S=R_J`, `G=P^T P`, `H=S^T S=I-G`.                    (1.2)

The chamber has `rank(P)=3`, `rank(S)=2`, and

`C=A[I,J]=P M S^T`, `rho=s_1(C)s_2(C)>=rho_0`,                  (1.3)

where

`rho_0=sqrt(29/3072)=0.097160198469675...`.                      (1.4)

Let `W=range(H)` and normalize the physical rows `s_j` of `S` by

`v_j=(H|_W)^(-1/2)s_j`, `j in J`.                               (1.5)

Then `(v_j)` is a two-dimensional Parseval frame. For a physical pair `T={j,k}` define

`d_T=det(v_j,v_k)^2`,                                            (1.6)

so `sum_T d_T=1`.

The preceding run proved the weighted star/triangle reduction. In the TRIANGLE branch there is an actual three-coordinate set `S_0 subset J` such that

`q_(S_0):=sum_(T subset S_0, |T|=2)d_T > q_0:=377/448`.          (1.7)

It paid the triangle whenever the complementary source Gram is not nearly singular, and otherwise reduced to a globally heavy small-pivot row. The open question was how to use the remaining original-product resources without returning circularly to the same rank-two-cross compiler.

The analytic receiver used below is the completed account03/B19 r24 theorem

`yspennstate/math-open-problems@2c88af5e0ac6a4faf8d923a621c7d7006d544ffe`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T034239Z-account03-B19-QFORM-r24/REPORT.md`.

For two original physical coordinates `X=(X_1,X_2)`, a disjoint original-product bank `Y`, arbitrary symmetric two-coordinate self block, arbitrary affine term, arbitrary measurable residual `S(Y)`, and rank-two cross matrix `B_cross`, it proves

`sup_z P(|R-z|<=eps) <= 12(2 Delta_2)^(-1/3) eps^(2/3)`,          (1.8)

where

`Delta_2=sqrt(det(B_cross B_cross^T))`.                           (1.9)

It also gives

`sup_z E|R-z|^(-1/2)
 <=4*12^(3/4)*(2 Delta_2)^(-1/4)`.                               (1.10)

Both estimates use only original-coordinate conditioning.

## 2. Exact pairwise cross-area identity inside the normalized frame

For an actual physical pair `T={j,k} subset J`, let `S_T` be the `2 x 3` matrix whose rows are `s_j^T,s_k^T`. Consider the cross block from this pair to the whole original source bank `I`:

`C_T=A[T,I]=S_T M P^T`.                                          (2.1)

Define its two-row area currency

`Delta_T=s_1(C_T)s_2(C_T)=sqrt(det(C_T C_T^T))`,                 (2.2)

with the convention `Delta_T=0` when the pair is rank deficient.

### Theorem 2.1 — `QFORM-TRIANGLE-PAIR-CROSS-IDENTITY-v1`

In the setup (1.1)-(1.6), for **every** physical pair `T subset J`,

`boxed: Delta_T = rho sqrt(d_T).`                                (2.3)

This identity is signature-free and remains valid when `d_T=0`.

### Proof

Because every row of `S` lies in `W`, restrict all two-dimensional determinants below to the Euclidean plane `W`. From (2.1),

`C_T C_T^T = S_T M G M S_T^T`.                                  (2.4)

Write `K_T` for the `2 x 2` coordinate matrix of the two rows `s_j,s_k` in an orthonormal basis of `W`, and write

`B_W=(M G M)|_W`.                                                (2.5)

Since `G` is positive definite and `M` invertible, `B_W` is positive definite. Therefore

`Delta_T^2
 =det(K_T B_W K_T^T)
 =det(K_T)^2 det(B_W).`                                          (2.6)

On the other hand, (1.5) gives

`d_T=det(K_T (H|_W)^(-1/2))^2
    =det(K_T)^2/det(H|_W)`.                                     (2.7)

Thus

`det(K_T)^2=d_T det(H|_W)`.                                     (2.8)

The exact rank-two cross identity from the preceding B19 run is

`rho^2=det(H|_W) det(B_W)`.                                     (2.9)

Substituting (2.8) and (2.9) into (2.6) yields

`Delta_T^2=d_T rho^2`.                                          (2.10)

All quantities are nonnegative singular products, so (2.3) follows. QED.

The point is that the complete normalized Pluecker weight `d_T` is not merely combinatorial bookkeeping: it is **exactly** the fraction of the full rank-two cross determinant carried by the physical pair `T`.

## 3. Every TRIANGLE contains a uniformly strong actual two-coordinate cross packet

There are only three pairs inside `S_0`. Hence (1.7) gives one actual pair `T_* subset S_0` with

`d_(T_*) > q_0/3 = 377/1344 =0.2805059523...`.                  (3.1)

By Theorem 2.1 and the live lower bound (1.4),

`Delta_(T_*)
 > Delta_0
 :=sqrt(29/3072)*sqrt(377/1344)
 =0.0514587738859587...`.                                       (3.2)

This is not a physical principal-pair determinant. It is the singular product of the cross block from two actual independent coordinates to an entire disjoint original-coordinate bank, so it does not contradict the live `QFORM-CROSSMINOR-ALONE-FALSE` or the fresh account02/B19 extreme-coloop example in which all local principal pivots vanish.

### Corollary 3.1 — `QFORM-TRIANGLE-TWOGRADIENT-2OVER3-v1`

Throughout the entire TRIANGLE branch (1.7), including the small-pivot/high-star residue, for every `z` and `eps>0`,

`boxed:
 P(|Q-z|<=eps)
 <25.607 eps^(2/3).`                                             (3.3)

Moreover

`boxed:
 sup_z E|Q-z|^(-1/2) <45.533.`                                  (3.4)

### Proof

Condition on every original coordinate in `J\T_*`. Given that conditioning, the only unconditioned variables are the two genuine physical coordinates `X_(T_*)` and the disjoint original-product bank `X_I`. The conditioned quadratic form has exactly the shape required by the r24 theorem:

`Q = X_T^T B_T X_T
    + X_T^T(2 C_T X_I + beta_omega)
    + S_omega(X_I)`,                                             (3.5)

where `B_T` is arbitrary symmetric, `beta_omega` is an arbitrary conditioned affine term, and `S_omega` contains all source self curvature and conditioned terms. No coefficient is deleted.

Its two-gradient currency is exactly `Delta_(T_*)`, which is bounded below by (3.2). Applying (1.8) conditionally and then averaging gives

`P(|Q-z|<=eps)
 <=12(2 Delta_0)^(-1/3)eps^(2/3)
 =25.6065716235... eps^(2/3)`,                                   (3.6)

which is (3.3). Applying (1.10), or equivalently layer cake to (3.3), gives

`sup_z E|Q-z|^(-1/2)
 <=4*12^(3/4)*(2 Delta_0)^(-1/4)
 =45.5327172529...`,                                             (3.7)

proving (3.4). QED.

This is a target-valid statement for arbitrary cap-one laws and every signature allowed by the exact-rank-three chamber. It uses no assumptions on the physical pair self block, including the fully degenerate zero-self case.

## 4. Why this still does not justify an L-infinity conclusion

The designated partner account04/B19 most recently isolated a generic interpolation obstruction. Its example can be sharpened to the exact exponent obtained in (3.3).

For every integer `N>=2`, define

`p_N(x)=N 1_[0,N^(-3)](x)+(1-N^(-2))1_[2,3](x)`.                (4.1)

Then

`int p_N=1`, `||p_N||_3^3<=2`, and `||p_N||_infinity=N`.         (4.2)

In addition,

`sup_z int_(z-eps)^(z+eps) p_N(x)dx <=4 eps^(2/3)`               (4.3)

for every `eps>0`, uniformly in `N`. Indeed:

- if `eps<=N^(-3)`, the spike contributes at most `2N eps<=2eps^(2/3)` and the broad block at most `2eps<=2eps^(2/3)`;
- if `N^(-3)<eps<=1`, the spike contributes at most `N^(-2)<=eps^(2/3)` and the broad block at most `2eps<=2eps^(2/3)`;
- if `eps>=1`, total mass is at most one.

Thus even a uniform `L^3` bound plus a uniform **two-thirds Holder concentration estimate** does not generically imply a bounded density. Call this strengthened interface obstruction

`QFORM-L3-PLUS-2OVER3-HOLDER-NOT-LINFINITY-v1`.                  (4.4)

It is not a QFORM counterexample. Its role is to prevent an invalid final interpolation step: the third spectral resource must remain coupled to the same source/product structure that produces (3.3).

## 5. Designated partner account04/B19 applied to an actual inequality

The completed account04/B19 theorem

`QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`,

canonical source

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`,

proves in its **residual-diffuse exact-null-coloop** scope

`||p_Q||_infinity <34 sqrt(log(e/D_res))`, `0<D_res<=1`.         (5.1)

Therefore on the actual endpoint interval

`e^(-8)<=D_res<=1`,                                              (5.2)

`log(e/D_res)<=9`, and hence

`boxed: ||p_Q||_infinity<102.`                                   (5.3)

The same source separately pays `D_res=0` and `D_res>=1`. No near-coloop stability is inferred from (5.1).

The partner's later `QFORM-L3-PLUS-HALF-HOLDER-NOT-LINFINITY-v1` is also respected: Section 4 above shows that the obstruction persists even at the stronger `2/3` concentration exponent now available on the TRIANGLE branch.

## 6. Compact conditional proof assembly after this run

Inside the current exact-rank-three rank-two-cross route, the correction-safe proof graph is now:

1. The balanced frame-defect branch is paid continuously by the earlier B19 receiver.
2. If the normalized two-basis disjoint mass is at least `1/64`, the exact original-coordinate repartition theorem pays continuously by `<1626`.
3. If disjoint mass is below `1/64`, the weighted graph reduction gives STAR or TRIANGLE.
4. TRIANGLE is no longer merely a three-row concentration statement: Theorem 2.1 forces an **actual two-physical-coordinate cross packet** with `Delta_2>0.0514587` into the disjoint source bank. Consequently every TRIANGLE state, including the former small-pivot/high-star endpoint, has the uniform full-form estimates (3.3)-(3.4).
5. These estimates do not by generic interpolation yield `L^infinity`; Section 4 supplies an explicit sharp obstruction. The remaining TRIANGLE task must spend the third rank direction jointly with this fixed cross packet.
6. STAR remains the parallel extreme-coloop/grouped-third-source problem isolated by account02/B19. The fresh account02 counterexample rules out replacing that task by a claim of a uniformly large physical scalar or principal-pair pivot.

The first essential missing implication is therefore sharpened to

`QFORM-TRIANGLE-CROSSPACKET-THIRD-SOURCE-COUPLED-LINFINITY-v1`:

> In the exact-rank-three TRIANGLE chamber, combine the guaranteed original pair `T_*` with `Delta_(T_*)>=Delta_0` and the genuinely third rank direction **before** any fiber supremum or generic interpolation, to prove a universal `L^infinity` density bound or route to an already-paid grouped/ridge branch. The required mechanism must retain original-product provenance; a bare `L^3` norm plus (3.3) cannot suffice.

The unrestricted theorem still has the separate arbitrary-extra-spectrum descent debt. No exact-rank-three result in this report is promoted to higher rank without such a descent.

## 7. Signs, degeneracies, and regularity audit

- `M` may have any signature and repeated eigenvalues. Only invertibility and `s_min(M)>=1` are used.
- The two-coordinate physical self block in (3.5) may be definite, indefinite, singular, or zero.
- `d_T=0` is never divided by; the selected pair has strictly positive `d_T` by (3.1).
- `H|_W` may be arbitrarily ill-conditioned; it cancels exactly in (2.3).
- Every conditioning is on original independent coordinates.
- The result (3.3) is a concentration estimate and (3.4) a half-Riesz estimate; neither alone proves continuity or an `L^infinity` density. Full-target continuity remains OPEN.
- The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

## 8. Exact numerical check values

The arithmetic used above is

`rho_0=sqrt(29/3072)=0.09716019846967515`,

`q_0=377/448=0.8415178571428571`,

`d_0=q_0/3=377/1344=0.2805059523809524`,

`Delta_0=rho_0 sqrt(d_0)=0.05145877388595875`,

`12(2Delta_0)^(-1/3)=25.606571623544564`,

`4*12^(3/4)*(2Delta_0)^(-1/4)=45.53271725291665`.

These decimal evaluations are checks only; the proof is the exact determinant identity (2.3) and the already-proved r24 receiver.
