SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T22:53:18Z.
attacking: the epsilon-uniform vector TT* bridge in the exact-rank-three shared-hub survivor; first isolate exactly what the new grouped projected-crossing theorem sees, then route its one-hub leakage failure to a two-physical-hub compiler rather than a false conditional-cap argument.

# account03/B16 r36 — exact Pluecker/Schur factorization for grouped projected crossings

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM + MECHANISM BARRIER + PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** the new receiver branches below have a continuous `C_0` density because they inherit an `L^1` characteristic-function estimate. The unrestricted continuity conclusion remains OPEN.

## 1. Source boundary

The exact owner target remains: independent real original-coordinate inputs with one-dimensional probability densities bounded by one; arbitrary real symmetric `A`; at least three eigenvalues of `A` have modulus at least one; prove one universal finite density bound, or give a valid counterexample. No moment, compact-support, connected-support, Gaussian, log-concavity, iid, diagonal-basis, or post-rotation-independence assumption is used below.

Fresh control at run start was `yspennstate/math-research-brain@3ab7c190bf7672ed80bebac86bb004c755b33c87`, OWNER CONTROL revision `2026-09-22.15`, with QFORM still the sole assignment. The live corrections were read, including the failures of arbitrary-joint coarea, conditional projection-height moments, fiberwise trace control, pointwise law-uniform quadratic-phase decay, and independence after rotation.

The analytic input actually used is the checked grouped projected-crossing theorem

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For `k` hub directions and an `ell`-volume projected light crossing, `d=k+ell>2`, its estimate is

`||p_Q||_infinity <= [d/(d-2)] 2^((k+3ell)/(2d)) exp(ell/(2d))
 M_H^(1/d) S^(-1/d) Z_ell^(-1/(2d))`,                              (1.1)

with the exponential factor omitted for `ell=1`. Here `S` is the singular-value product of the hub-to-`J` crossing and `Z_ell` is the projected crossing volume. It allows arbitrary internal hub functions and arbitrary same-side light quadratic terms. It does **not** assume the projected coordinates are independent.

The designated partner input is account04/B16 r2,

`yspennstate/math-open-problems@a70c05e517e8a195a31ab4f4c301c672d1c8d4e6`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260923T192012Z-account04-B16-QFORM-r2/REPORT.md`.

Its physical-pair overlap theorem and the concrete three-bank gate are applied in Section 7.

## 2. Exact-rank-three setup and notation

Let

`A = R Lambda R^T`, `R^T R=I_3`,                                  (2.1)

where `Lambda` is real symmetric and invertible. Thus `A` has exact rank three. Write `r_i` for row `i` of `R`. For every three-set `T` of original coordinates define its Pluecker weight

`v_T = det(R_T)^2 >=0`.                                            (2.2)

Cauchy--Binet gives

`sum_(|T|=3) v_T = det(R^T R)=1`.                                 (2.3)

Fix `k in {1,2}` literal original hub coordinates `H`, and let

`ell=3-k`.                                                         (2.4)

Take disjoint original-coordinate sets `I,J` outside `H`; any remaining coordinates may simply be included in `I` or `J` for the theorem below, or conditioned before applying it, in which case they create only deterministic affine terms.

Put

`M=A_(H,J)`                                                        (2.5)

and assume `rank M=k`. Let `Pi` be the orthogonal projection in `R^J` onto the row space of `M`, and define the residual light crossing

`C=A_(I,J)(I-Pi)`.                                                 (2.6)

Let

`S_M^2=det(M M^T)`                                                 (2.7)

(the square of the singular-value product), and define

`Z_ell = sum_(S subset I, |S|=ell) det(C_S C_S^T)`.                (2.8)

Finally define the two Pluecker masses

`V_(H,ell)(I)=sum_(S subset I, |S|=ell) v_(H union S)`,             (2.9)

`V_3(J)=sum_(T subset J, |T|=3) v_T`.                              (2.10)

## 3. Main identity — `QFORM-PLUCKER-SCHUR-PROJECTED-CROSSING-v1`

### Theorem 3.1

Under the setup above,

`boxed:
 S_M^2 Z_ell
 = (det Lambda)^2 V_(H,ell)(I) V_3(J).
}`                                                                   (3.1)

Moreover, whenever the right side is positive, the `ell`-volume sampling weights used by the grouped projected-crossing theorem are **exactly**

`w_S = v_(H union S)/V_(H,ell)(I)`, `|S|=ell`,                    (3.2)

and hence their row marginals are

`boxed:
 alpha_i
 = [sum_(S subset I, |S|=ell, i in S) v_(H union S)]
   / V_(H,ell)(I).
}`                                                                   (3.3)

Thus both the nonlinear analytic denominator and the volume-marginal gate can be read directly from the original rank-three Pluecker data. No conditional projection density is introduced.

### Proof

Fix one `ell`-set `S subset I`. Stack the `k` rows of `M` and the `ell` rows `A_(S,J)`:

`B_S = [ M ; A_(S,J) ]`,                                           (3.4)

which has exactly `k+ell=3` rows. Orthogonally subtract from every row of `A_(S,J)` its projection onto `row(M)`. Gram--Schmidt at the row-space level gives the exact block-volume factorization

`det(B_S B_S^T)
 =det(MM^T) det(C_S C_S^T)
 =S_M^2 det(C_S C_S^T).`                                          (3.5)

This is only Euclidean row-volume; it says nothing about probabilistic independence.

Now apply Cauchy--Binet to the three-row matrix `B_S=A_(H union S,J)`:

`det(B_S B_S^T)
 =sum_(T subset J, |T|=3) det(A_(H union S,T))^2.`                 (3.6)

Because `A` has exact rank three,

`A_(H union S,T)=R_(H union S) Lambda R_T^T`,                      (3.7)

and both outer matrices in (3.7) are `3 x 3`. Therefore

`det(A_(H union S,T))^2
 =(det Lambda)^2 v_(H union S) v_T`.                               (3.8)

Combining (3.5)--(3.8),

`S_M^2 det(C_S C_S^T)
 =(det Lambda)^2 v_(H union S) V_3(J).`                            (3.9)

Sum (3.9) over all `ell`-sets `S subset I` to obtain (3.1). Dividing an individual identity (3.9) by the sum proves (3.2), and summing the weights containing a fixed row proves (3.3). QED.

## 4. Dependence-safe density receivers

Apply the checked grouped projected-crossing theorem to the actual quadratic form. The hub block consists of exactly the `k` literal physical coordinates `X_H`; hence its joint density is the product of `k` cap-one densities and has height at most one. We use `W=X_H` itself, not independent spectral coordinates. All terms internal to `H` are absorbed into the theorem's arbitrary `F(X_H)`, while all light-side diagonal, affine, and same-side quadratic terms remain in `R(X')`.

Since `k+ell=3`, equation (1.1) and (3.1) give the following two explicit receivers.

### Corollary 4.1 — one physical hub, two projected crossing directions

For `k=1`, `ell=2`, if every marginal in (3.3) is at most `1/2`, then the full exact-rank-three form has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= C_1 |det Lambda|^(-1/3)
       [V_(H,2)(I)V_3(J)]^(-1/6),
}`                                                                   (4.1)

where

`C_1=3*2^(7/6)*exp(1/3)=9.3991318878... <9.4`.                    (4.2)

### Corollary 4.2 — two literal physical hubs, one projected crossing direction

For `k=2`, `ell=1`, if every weight

`v_(H union {i})/V_(H,1)(I) <=1/2`,                               (4.3)

then the full exact-rank-three form has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= C_2 |det Lambda|^(-1/3)
       [V_(H,1)(I)V_3(J)]^(-1/6),
}`                                                                   (4.4)

with the better constant

`C_2=3*2^(5/6)=5.3453923088...`.                                  (4.5)

No exponential entropy loss occurs at `ell=1`.

These statements are nonlinear density bounds for the **full** quadratic polynomial in their exact-rank-three scope. They are not merely projection-density bounds.

## 5. Why the one-hub projected-crossing theorem cannot by itself remove the near-coloop parameter

Take one physical hub `H={h}` and set

`c_h=||r_h||^2`.                                                    (5.1)

The total three-basis mass containing `h` is exactly `c_h`, while the total three-basis mass avoiding `h` is exactly `1-c_h`:

`sum_(i<j, i,j!=h) v_{hij}=c_h`,                                  (5.2)

`sum_(T subset h^c, |T|=3) v_T=1-c_h`.                            (5.3)

For completeness, (5.3) follows from

`R_(h^c)^T R_(h^c)=I_3-r_h^T r_h`

and the matrix determinant lemma; its determinant is `1-||r_h||^2`. Equation (5.2) then follows from (2.3).

Consequently every disjoint split `I,J subset h^c` obeys

`V_(h,2)(I)V_3(J) <= c_h(1-c_h)`.                                 (5.4)

Combining (5.4) with the exact factorization (3.1) proves a precise **method barrier**:

> Any application of the one-physical-hub `k=1,ell=2` grouped projected-crossing denominator to a true near-coloop `c_h ->1` necessarily carries the vanishing Pluecker factor `1-c_h`.

This is not a lower bound on the true density and not a counterexample to QFORM. It shows that the one-hub projected-volume route is algebraically the same leakage currency already seen in the earlier B16 balanced-basis argument; it cannot become epsilon-uniform merely by replacing a conditional slice with the newer grouped Fourier theorem.

This is the first essential missing implication attempted in this run. It rules out spending further runs on a scalar-hub TT* estimate whose only quantitative currency is `S_M^2 Z_2`.

## 6. The two-hub identity gives a genuinely different escape route

The `k=2,ell=1` formula is not tied to the same chosen near-coloop. For a literal physical pair `H={h_1,h_2}`,

`sum_(i notin H) v_(H union {i})
 =det(R_H R_H^T)`,                                                 (6.1)

again by Cauchy--Binet. Thus the first factor in (4.4) is an actual physical-pair area currency. If the two-hub pair is chosen away from the near-coloop, the second factor `V_3(J)` may include bases **containing** the old near-coloop and therefore need not carry the small factor `1-c_h`.

This identifies a concrete next structural lemma rather than a vague "use more hubs" instruction:

`QFORM-TWO-PHYSICAL-HUB-PLUCKER-COVER-v1`:
find, in every still-unpaid exact-rank-three near-coloop state, either

1. a literal physical pair `H` and disjoint `I,J` with
   `V_(H,1)(I)V_3(J)` bounded below universally and the weights (4.3) at most `1/2`, so (4.4) closes the branch; or
2. route the failure (concentrated pair area / heavy one-row marginal) into an already completed physical-pair or aggregate-coloop receiver.

Unlike the one-hub denominator, this proposed compiler is not algebraically forced to lose `1-c_h`.

## 7. Designated account04/B16 result applied at an actual inequality

The current designated partner theorem is account04/B16 r2. In its live exact-rank-three physical-pair/three-bank packet it proves

`||p_Q||_infinity
 <=9.2002740353 [D |det Lambda| tau det G_b]^(-1/5).`              (7.1)

Its concrete super-volume gate is

`det G_b >= W_b s^2/(64 D tau)`,                                  (7.2)

with

`W_b>61/1728`, `|det Lambda|>=s^3`, `s>=1`.                       (7.3)

Substitution is literal:

`D |det Lambda| tau det G_b
 >= W_b s^5/64
 > (61/1728)s^5/64`,                                              (7.4)

so

`||p_Q||_infinity
 <9.2002740353 (64*1728/61)^(1/5) s^(-1)
 =41.2552799658... s^(-1)
 <=41.256.`                                                        (7.5)

Thus every bank satisfying (7.2) is already paid without any projected-row marginal condition. The two-hub Pluecker compiler in Section 6 should therefore be aimed only at the complementary shear-flat/heavy-row packet, rather than duplicating this branch.

## 8. A dimension-free disjoint-overlap statistic

For the one-hub identity, define

`Omega_h = sum_[{i,j} cap T = empty]
          v_{hij} v_T`,                                           (8.1)

where `{i,j}` ranges over two leaf coordinates and `T` over three leaf coordinates. Independently send every leaf to `I` or `J` with probability `1/2`. Then

`E[V_(h,2)(I)V_3(J)] = Omega_h/32`.                               (8.2)

Hence there exists a deterministic partition with

`V_(h,2)(I)V_3(J) >= Omega_h/32`.                                 (8.3)

Whenever that partition also obeys the exact marginal gate (3.3), (4.1) gives

`||p_Q||_infinity
 <= C_1 32^(1/6)|det Lambda|^(-1/3) Omega_h^(-1/6)
 <16.748 |det Lambda|^(-1/3) Omega_h^(-1/6).`                     (8.4)

This is a clean dimension-free conversion from a disjoint Pluecker-overlap certificate to a nonlinear density bound. In the true near-coloop it still cannot remove leakage because `Omega_h<=c_h(1-c_h)`, exactly as Section 5 predicts.

## 9. Exact deterministic test case

The companion checker uses a ten-row Parseval frame:

- two copies of `e_1/sqrt(2)` (one is the hub),
- four copies of `e_2/2`,
- four copies of `e_3/2`,

and `Lambda=diag(2,-3,5)`. Choose `I` as two `e_2/2` rows and two `e_3/2` rows, and `J` as the other `e_1/sqrt(2)` row plus the remaining two `e_2/2` and two `e_3/2` rows.

Then, exactly,

`V_(h,2)(I)=1/8`, `V_3(J)=1/8`, `det(Lambda)^2=900`,               (9.1)

`S_M^2=1`, `Z_2=225/16`,                                         (9.2)

and therefore

`S_M^2 Z_2=225/16=900*(1/8)*(1/8)`.                              (9.3)

Every projected-volume row marginal equals exactly `1/2`, so the analytic gate is met at equality. Corollary 4.1 gives the finite numerical bound

`||p_Q||_infinity <=6.049842`                                     (9.4)

for this nontrivial exact-rank-three example. The checker records the fractions and constants; it is a regression check, not the proof of Theorem 3.1.

## 10. Current boundary

`QFORM-PLUCKER-SCHUR-PROJECTED-CROSSING-v1`: **PROVED SUPPORTING THEOREM**.  
One-hub leakage barrier (5.4): **PROVED METHOD OBSTRUCTION**, not a QFORM counterexample.  
Two-physical-hub receiver (4.4): **PROVED CONDITIONAL TARGET BRANCH**.  
Designated partner super-volume branch: **PAID by <=41.256**.  
Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Global continuity: **OPEN**, although the receiver branches (4.1), (4.4) are continuous.

A fresh universal structural implication is still required to produce the two-hub certificate in Section 6 (or to route every failure to an existing receiver). The separate arbitrary-rank problem is narrowed by the recent principal-minimal induction of account03/B19: extra threshold-large spectrum can be removed by exact original-coordinate conditioning, but subthreshold spectral tails are not thereby discarded and remain part of the full target.

No schedule, enabled/paused state, notification, email, task, permission, public-release, paid model/API/Codex call, remote workflow, or cross-account authentication was changed in this run.
