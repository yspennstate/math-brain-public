SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T23:53:37Z.
attacking: grouped two-hub projection-product closure in the true near-coloop; test whether aggregating physical hubs removes the Pluecker leakage, and if not identify the exact algebraic obstruction.

# account03/B16 r37 — grouped Pluecker factorization and the disjoint full-volume near-coloop barrier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING IDENTITY + CORRECTION OF PRIOR B16 MECHANISM + PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** the grouped projected-crossing branch below has a continuous `C_0` density because the source theorem supplies an `L^1` characteristic-function majorant. The unrestricted continuity conclusion remains OPEN.

## 1. Source boundary

The exact owner target remains: for every dimension, every independent real original-coordinate input with density at most one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal density bound for `Q=X^T A X`, or give a valid counterexample. No moment, compact-support, connected-support, Gaussian, log-concavity, iid, diagonal-basis, or post-rotation-independence assumption is added below.


The analytic input is the completed grouped projected-crossing theorem

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The designated partner input is account04/B16 r3,

`yspennstate/math-open-problems@c47c53d4ef3e255431a6fb13960de1794bf2698f`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260923T211939Z-account04-B16-QFORM-r3/REPORT.md`.

Its innovation/slope collar is applied explicitly in Section 7.

## 2. Exact-rank-three notation

Let

`A = R Lambda R^T`, `R^T R=I_3`,

with `Lambda` invertible and symmetric. For every physical three-set `T`, put

`v_T = det(R_T)^2`.

Then `sum_{|T|=3} v_T=1` by Cauchy--Binet.

Take pairwise disjoint original-coordinate sets `H,I,J`. Put

`B=A_{H,J}`

and suppose `rank B=k`, where `k` is 1 or 2. Set `ell=3-k`. Let `Pi` be the orthogonal projection in `R^J` onto `row(B)`, and define

`C=A_{I,J}(I-Pi)`.

Let `S_B` be the product of the `k` nonzero singular values of `B`, so

`S_B^2=e_k(BB^T)=sum_{P subset H, |P|=k} det(B_P B_P^T)`.

For `S subset I`, `|S|=ell`, define

`q_S = sum_{P subset H, |P|=k} v_{P union S}`,

and set

`V_{k,ell}(H,I)=sum_{S subset I, |S|=ell} q_S`,

`V_3(J)=sum_{T subset J, |T|=3}v_T`,

`Z_ell=sum_{S subset I, |S|=ell} det(C_S C_S^T)`.

## 3. Main identity — `QFORM-GROUPED-PLUCKER-SCHUR-FACTOR-v2`

### Theorem 3.1

For every fixed `S subset I`, `|S|=ell`,

`boxed:
 S_B^2 det(C_S C_S^T)
 = (det Lambda)^2 q_S V_3(J).
`

Consequently

`boxed:
 S_B^2 Z_ell
 = (det Lambda)^2 V_{k,ell}(H,I)V_3(J).
}`

Whenever the right side is positive, the volume-sampling weights in the grouped projected-crossing theorem are exactly

`w_S=q_S/V_{k,ell}(H,I)`,

so the corresponding physical row marginals are

`alpha_i = [sum_{S containing i} q_S]/V_{k,ell}(H,I)`.

### Proof

Fix an `ell`-set `S`. For each `k`-set `P subset H`, form the three-row matrix

`D_{P,S}=A_{P union S,J}`.

If `B_P` has rank less than `k`, then `D_{P,S}` has rank at most `(k-1)+ell=2`, hence `det(D_{P,S}D_{P,S}^T)=0`. If `B_P` has full row rank `k`, its row space equals `row(B)`, because `B` itself has rank `k`. Orthogonally removing from the rows `A_{S,J}` their projection onto `row(B)` therefore gives

`det(D_{P,S}D_{P,S}^T)
 =det(B_PB_P^T) det(C_SC_S^T)`.

This equality also holds in the singular case because both sides vanish. Summing over `P` gives

`sum_P det(D_{P,S}D_{P,S}^T)
 = S_B^2 det(C_SC_S^T).`                                      (3.1)

For each `P`, Cauchy--Binet on the three-row matrix `D_{P,S}` gives

`det(D_{P,S}D_{P,S}^T)
 =sum_{T subset J, |T|=3} det(A_{P union S,T})^2.`              (3.2)

Exact rank three now matters. Since

`A_{P union S,T}=R_{P union S} Lambda R_T^T`,

all three factors are `3 x 3`, and hence

`det(A_{P union S,T})^2
 =(det Lambda)^2 v_{P union S}v_T.`                              (3.3)

Summing (3.3) over `P,T` and comparing with (3.1)-(3.2) proves the fixed-`S` identity. Summing over `S` proves the aggregate factorization. Dividing the fixed-`S` identity by the aggregate one proves the weight formula and then the row-marginal formula. QED.

This is an algebraic identity in original coordinates. It does not assert that projected spectral variables are independent.

## 4. Dependence-safe grouped two-hub receiver

To turn the identity into a density estimate, impose the actual source theorem's additional hub hypothesis: all hub-light interactions are carried by a `k`-dimensional orthonormal projection `W=U^T X_H`, and `B=A_{H,J}` has rank `k`. This is automatic when `H` consists of exactly `k` literal physical hub coordinates; more generally it holds whenever the full hub-to-light crossing has rank `k` and `B` retains that rank.

For `k=2`, `ell=1`, the bounded-density projection theorem gives

`||p_W||_infinity <= 2`

for the two-dimensional orthonormal projection of the product cap-one law on `X_H`. If the exact volume row marginals

`alpha_i=q_{ {i} }/V_{2,1}(H,I)`

are all at most `1/2`, the grouped projected-crossing theorem with `d=3`, together with Theorem 3.1, yields

`boxed:
 ||p_Q||_infinity
 <= 3*2^(7/6) |det Lambda|^(-1/3)
    [V_{2,1}(H,I)V_3(J)]^(-1/6).
}`                                                              (4.1)

Numerically `3*2^(7/6)=6.734772289856...`.

The point of (4.1) is that the joint projection-density theorem is not being used as if it controlled an indefinite level-set integral. It enters only as the `L^2` hub pushforward input inside the nonlinear grouped Fourier argument; the projected crossing supplies the remaining integrability. Arbitrary dependence inside `W` is retained. In this branch the source theorem gives a continuous `C_0` density.

## 5. New barrier — `QFORM-DISJOINT-FULLVOLUME-NEARCOLOOP-BARRIER-v1`

Let `h` be one physical coordinate with spectral leverage

`c_h=||r_h||^2=1-epsilon`, `0<=epsilon<=1`.

Cauchy--Binet on the frame with row `h` removed gives the exact identity

`sum_{T: |T|=3, h notin T} v_T
 =det(I_3-r_h^T r_h)
 =1-||r_h||^2
 =epsilon.`                                                      (5.1)

Now take any pairwise disjoint `H,I,J` and any `k+ell=3` as in Theorem 3.1. Every triple contributing to `V_{k,ell}(H,I)` lies in `H union I`, while every triple contributing to `V_3(J)` lies in `J`.

If `h in J`, every triple counted by `V_{k,ell}(H,I)` avoids `h`, so by (5.1)

`V_{k,ell}(H,I)<=epsilon`.

If `h notin J`, every triple counted by `V_3(J)` avoids `h`, so

`V_3(J)<=epsilon`.

Both factors are submasses of the probability weights `{v_T}`, hence each is at most one. Therefore, in every case,

`boxed:
 V_{k,ell}(H,I)V_3(J) <= epsilon.
}`                                                              (5.2)

Combining with Theorem 3.1,

`boxed:
 S_B^2 Z_ell <= (det Lambda)^2 epsilon.
}`                                                              (5.3)

This is a **method barrier, not a lower bound on the true QFORM density**. Every `d=3` disjoint grouped projected-crossing certificate that spends exactly three rank-three volume directions necessarily loses the near-coloop mass `epsilon=1-c_h` somewhere.

### Correction to account03/B16 r36

Run r36 proposed that a two-physical-hub choice away from `h`, with the old near-coloop placed inside `J`, might avoid the `1-c_h` leakage because `V_3(J)` can then contain `h`. Equation (5.2) shows that this is false as a uniform mechanism: in precisely that placement the complementary factor `V_{2,1}(H,I)` contains only triples avoiding `h`, hence is at most `epsilon`.

The r36 exact factorization and its stated density receiver remain valid; only the proposed structural escape in its Section 6 is retracted. This does not refute the QFORM conjecture.

## 6. Sharpness inside the actual marginal gate

The order `epsilon` in (5.2) cannot be improved for the disjoint grouped-crossing currency, even while the source theorem's row-marginal gate is satisfied exactly.

Fix `0<epsilon<1` and use a seven-row Parseval frame in `R^3`:

- near-coloop coordinate `h` in `J`: `r_h=sqrt(1-epsilon)e_3`;
- two literal hubs `H={H_1,H_2}`: `r_{H_1}=e_1/sqrt2`, `r_{H_2}=e_2/sqrt2`;
- two further `J` rows: `e_1/sqrt2`, `e_2/sqrt2`;
- two `I` rows: each `sqrt(epsilon/2)e_3`.

The row outer products sum to `I_3`. For any diagonal invertible `Lambda=diag(lambda_1,lambda_2,lambda_3)`,

`V_{2,1}(H,I)=epsilon/4`,

`V_3(J)=(1-epsilon)/4`,

and therefore

`V_{2,1}(H,I)V_3(J)=epsilon(1-epsilon)/16.`                       (6.1)

Each of the two `I` rows has volume marginal exactly `1/2`, so the analytic gate is met with equality. Moreover

`S_B^2=lambda_1^2 lambda_2^2/16`,

`Z_1=lambda_3^2 epsilon(1-epsilon)`,

and hence

`S_B^2 Z_1=(det Lambda)^2 epsilon(1-epsilon)/16`,

exactly as Theorem 3.1 predicts.

Thus the epsilon loss is not an artifact of an imbalanced volume distribution; it persists in a perfectly admissible projected-crossing example.

## 7. Designated account04/B16 result applied at an actual inequality

The current partner result, account04/B16 r3, treats the balanced near-coloop packet with

`epsilon=1-h`

and exact identity

`epsilon=delta_J^2+delta_K^2+d^T G_JG_K d`.

On its innovation-dominant branch it proves

`||p_Q||_infinity
 <= (20/3)[|Gamma|(s_1s_2)^2 epsilon]^(-1/5).`                   (7.1)

Therefore the concrete gate

`|Gamma|(s_1s_2)^2 epsilon >= 2^(-20)`                            (7.2)

is already paid by

`boxed:
 ||p_Q||_infinity <= (20/3)*2^4 = 320/3 < 106.667.
}`                                                              (7.3)

On the complementary slope-dominant branch the same partner theorem proves

`2 epsilon < ||d||_2^2 <= (16/3)epsilon.`                        (7.4)

Apply the new barrier (5.2) to any disjoint `d=3` grouped projected-crossing partition in that same near-coloop geometry. If

`P:=V_{k,ell}(H,I)V_3(J)`,

then

`P<=epsilon<||d||_2^2/2.`                                        (7.5)

Thus its structural factor in the projected-crossing upper bound necessarily obeys

`P^(-1/6) > 2^(1/6)||d||_2^(-1/3).`                              (7.6)

Equation (7.6) is **not** a lower bound on the true density. It proves that this entire disjoint full-volume receiver class cannot interpolate uniformly to the exact-coloop endpoint along the partner's punctured slope collar: its own certificate deteriorates as `d ->0`, while the exact-coloop branch is known to admit a separate bounded receiver.

This is the actual partner-to-equation application requested for B16. It eliminates another duplicate mechanism and localizes the next mathematical debt.

## 8. First remaining implication

After (7.3), the B16 endpoint that matters is the slope-dominant punctured near-coloop with overlapping original-coordinate leaf provenance, small `epsilon`, and no innovation/Fresnel product bounded below. The new result shows that another disjoint `k+ell=3` Pluecker-volume split cannot close it, no matter whether one uses one physical hub, two literal hubs, or a larger hub group whose crossing rank is one or two.

The next mechanism must therefore **share** the near-coloop source across the smoothing argument, or exploit cancellation that survives `epsilon ->0`; it cannot pay two disjoint three-basis masses independently. A natural precise target is:

`QFORM-OVERLAP-AWARE-PUNCTURED-HUB-STABILITY-v1`:
prove a density bound uniform as `epsilon ->0` for the partner's slope-dominant packet by coupling the exact-coloop fresh-hub receiver to the nonzero puncture before taking absolute values, retaining the same original leaf sources in both pieces.

Arbitrary additional spectrum remains a separate full-target interface. Nothing here claims a full solution.

## 9. Deterministic arithmetic check

The companion checker evaluates the exact seven-row example at

`epsilon=1/100`, `Lambda=diag(2,3,5)`.

It obtains

`V_{2,1}=1/400`, `V_3=99/400`, `P=99/160000`,

`S_B^2=9/4`, `Z_1=99/400`,

and exactly

`S_B^2 Z_1 = (det Lambda)^2 P = 891/1600`.

Both row marginals are exactly `1/2`. It also checks `P<=epsilon` and the constants in (4.1) and (7.3). The committed output ends `STATUS=PASS`.

## 10. Scope accounting

**Proved here:** the grouped exact-rank-three Pluecker/Schur identity; the exact volume-marginal formula; the universal near-coloop leakage barrier for every disjoint full-volume `k+ell=3` certificate; sharp epsilon scaling under the actual row-marginal gate; the grouped two-hub density receiver under the source theorem's stated interaction-rank and marginal hypotheses; and the concrete partner implications (7.3)-(7.6).

**Corrected here:** the r36 suggestion that placing a near-coloop in `J` while choosing two hubs away from it can remove the small Pluecker factor.

**Not proved:** the unrestricted QFORM theorem; a uniform punctured-hub stability theorem; arbitrary additional-spectrum reduction; or global continuity.

Repository transport and source retrieval occurred, but no authenticated native learned-memory receiver was invoked, so status remains `WITHOUT_VERIFIED_BRAIN`.
