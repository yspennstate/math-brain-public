SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T14:28:23Z.
attacking: the aligned STAR4 two-channel survivor by testing whether the hub plus a quantitative rank-two physical cross block can itself be a universal receiver, before spending the genuine third spectral resource.

# fleet03/B19 r35 — the aligned two-channel packet alone is not a valid L-infinity receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Outcome: **INTERMEDIATE CLAIM REFUTED / MECHANISM CHANGED / THIRD-SPECTRAL-RESOURCE DEBT IS NECESSARY / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: the counterexample branch has a density but it is unbounded; the positive source-disjoint third-packet stress branch below has a continuous `C_0` density.

The unrestricted QFORM conjecture remains OPEN. This report does not add Gaussian, log-concave, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation-independence assumptions. It does not use a law-uniform pointwise scalar quadratic-phase decay estimate, arbitrary-joint coarea, fiber-supremum replacement, or truncation of a higher-rank physical cross block.

## 1. Why this is the first live missing implication

The current global proof graph, source-pinned in the shared programme and the preceding B19 runs, reaches the strict no-pivot packet `STAR4(tau,beta,E0)` at

`tau = 2^-20`,
`beta = 0.000038585661932302174...`,

with a literal original hub `h`, disjoint original leaf banks `J,K`, star vectors

`u=A[J,h]`, `v=A[K,h]`,

and a physical leaf cross block

`N=A[J,K]`.

The quantitative rank-two branch has

`sigma_1(N)sigma_2(N) > rho_* = 0.003845207509588222...`.

The newest fleet01/B19 selected-volume theorem further pays a large branch continuously, and otherwise reduces the unpaid geometry to either an original-coordinate selected-volume anchor or an aligned near-rank-two core in which the two hub stars lie predominantly in the top-two left/right singular planes of `N`.

A tempting next statement would be:

> a null (or tiny) physical hub, two nonzero aligned hub-star vectors, and a quantitative rank-two physical cross block already force a universally bounded density, despite arbitrary same-bank curvature.

The following theorem shows that statement is false even in arbitrarily strict N3 geometry. Therefore the full proof must actually spend the third spectral resource promised by `s_3(A)>=1`; the aligned hub/rank-two packet cannot be closed in isolation.

## 2. Exact diffuse counterexample family to the local aligned receiver

Fix an even integer `m`. Let `J` and `K` be disjoint original-coordinate banks of size `m`, and let `h` be one further original coordinate. Choose orthonormal flat vectors

`p,r in R^J`, `q,s in R^K`,

with every coordinate equal in modulus to `m^(-1/2)`. For example take two distinct normalized Hadamard rows in each bank. Put

`a = e_h + p + q`,
`b = e_h + r + s`,

and define the symmetric physical coefficient matrix

`A_core = a a^T - b b^T`.                                      (2.1)

Because

`||a||^2=||b||^2=3`, `a^T b=1`,                                (2.2)

the matrix has rank two and its only nonzero eigenvalues are

`boxed: +sqrt(8), -sqrt(8).`                                    (2.3)

Indeed its trace is zero and

`tr(A_core^2)=2(3^2-1^2)=16`.

### 2.1 The hub/rank-two geometry is stronger than the live STAR4 thresholds

The hub self coefficient vanishes exactly:

`(A_core)_{hh}=0`.                                               (2.4)

The two star vectors are

`u=p-r`, `v=q-s`,                                                (2.5)

so

`||u||^2=||v||^2=2`.                                             (2.6)

The physical leaf cross block is

`N=p q^T-r s^T`.                                                 (2.7)

Since `{p,r}` and `{q,s}` are orthonormal pairs, the two nonzero singular values of `N` are exactly `1,1`. Hence

`boxed: sigma_1(N)sigma_2(N)=1`,                                (2.8)

and the stars are **exactly aligned**:

`u in range(N)`, `v in range(N^T)`.                              (2.9)

There is no cross tail at all.

Thus this family lies far inside the numerical star/rank-two/alignment inequalities of the current survivor, except that it has only two large spectral eigenvalues. That final exception is the point of the construction.

### 2.2 The same family is arbitrarily strict N3 in physical coordinates

Every physical diagonal is zero. Indeed, on `J`,

`(A_core)_{jj}=p_j^2-r_j^2=0`,                                  (2.10)

and similarly on `K`; (2.4) handles the hub.

For off-diagonal entries,

`|(A_core)_{hj}|=|p_j-r_j| <=2/sqrt(m)`,
`|(A_core)_{hk}|<=2/sqrt(m)`,                                   (2.11)

while every `J-J`, `K-K`, or `J-K` off-diagonal entry has magnitude at most `2/m`. Consequently

`max_{i!=j}|(A_core)_{ij}|^2 <=4/m`.                             (2.12)

Because the physical diagonals vanish, every physical principal-pair determinant equals `-(A_core)_{ij}^2`. Therefore, for every fixed `tau>0`,

`m>4/tau`                                                        (2.13)

places the entire family in the strict N3 conditions

`|A_ii|<tau`, `|A_ii A_jj-A_ij^2|<tau`.                         (2.14)

At the live `tau=2^-20`, any `m>4194304` suffices.

This matters: the failure below is not caused by a large physical pivot or a coarse low-dimensional coefficient.

## 3. The local aligned packet has an unbounded density for admissible product laws

Take all original scalar inputs in the core to be independent `Uniform[-1/2,1/2]`; their densities equal one on their supports. Then

`Q_core = X^T A_core X`
`       = (a^T X)^2-(b^T X)^2`
`       = L_- L_+`,                                             (3.1)

where

`L_-=(a-b)^T X`, `L_+=(a+b)^T X`.                               (3.2)

We prove that the joint density `g_m` of `(L_-,L_+)` is bounded below by a positive constant on a rectangle around the origin. It then follows from the exact product-density formula that the density of `Q_core` diverges logarithmically at zero.

Choose a coordinate `j in J` on which `p_j=-r_j`; such a coordinate exists for the two distinct flat Hadamard rows. In the two physical variables `(X_j,X_h)`, the coefficient map to `(L_-,L_+)` is

`[[2/sqrt(m), 0],
  [0,         2]]`,                                             (3.3)

up to harmless signs, and has determinant `4/sqrt(m)`.

Let

`delta_m=1/(64m)`.                                               (3.4)

Restrict every other core coordinate to `[-delta_m,delta_m]`. The total absolute coefficient sum of each of `L_-` and `L_+` outside `(X_j,X_h)` is at most `4 sqrt(m)`, so the resulting translation of each displayed linear form is at most

`4 sqrt(m) delta_m =1/(16 sqrt(m)) <=1/16`.                     (3.5)

Hence for

`|ell_-|<=1/(8 sqrt(m))`, `|ell_+|<=1/8`,                       (3.6)

the unique solution `(X_j,X_h)` stays strictly inside `[-1/2,1/2]^2` throughout this positive-measure conditioning event. The conditional Jacobian density is `sqrt(m)/4`. Averaging the conditioning event therefore gives

`boxed:
 g_m(ell_-,ell_+) >= c_m >0
}`                                                                (3.7)

throughout (3.6), where one explicit (very nonoptimal) choice is

`c_m = [sqrt(m)/4] [1/(32m)]^(2m-1)`.                           (3.8)

Now the standard product change of variables gives, for almost every `z!=0`,

`p_{Q_core}(z)=int_R g_m(t,z/t) dt/|t|`.                         (3.9)

For

`0<|z|<1/(64 sqrt(m))`,                                         (3.10)

the positive integration interval

`8|z| <= t <= 1/(8 sqrt(m))`                                    (3.11)

lies inside the rectangle (3.6), because `|z/t|<=1/8`. Thus

`boxed:
 p_{Q_core}(z)
 >= c_m log[1/(64 sqrt(m)|z|)]
 -> infinity as z->0.
}`                                                                (3.12)

Therefore

`boxed: ||p_{Q_core}||_infinity = infinity.`                    (3.13)

This is a valid bounded-density product-law counterexample to the **intermediate aligned local receiver**, not to the full QFORM conjecture: by (2.3), `A_core` has only two nonzero eigenvalues.

### New correction

`QFORM-ALIGNED-NULLPIVOT-TWOSIDED-LOCAL-LINF-FALSE-v1`:

> A null physical hub with two nonzero aligned star vectors and a rank-two physical cross block with singular product bounded below does **not** by itself imply a bounded quadratic-form density when both active banks retain arbitrary self-curvature. The failure persists in arbitrarily strict N3 physical geometry.

Any proof route that tries to close the current aligned STAR4 survivor from only these local currencies is therefore invalid. A genuine third spectral/product-preserving resource must enter.

## 4. Adding an actual third spectral packet repairs the stress family

The counterexample also cleanly identifies the missing currency rather than merely destroying a route.

Add a new original-coordinate bank `D` of size `m`, disjoint from `{h} union J union K`. Let

`w=(1,...,1)/sqrt(m) in R^D`,
`C=w w^T`,                                                       (4.1)

and define

`A_full = A_core direct_sum C`.                                 (4.2)

Then

`spec_nonzero(A_full)={sqrt(8),-sqrt(8),1}`,                    (4.3)

so the exact full-target spectral hypothesis holds. Its physical diagonals are zero on the core and `1/m` on `D`; every `D-D` principal pair determinant is zero because `C` has rank one. Hence for `m>4/tau`, (4.2) is also strict N3 at the same fixed `tau`.

Now use the completed theorem `QFORM-RANK2-CROSS-PLUS-OFFDIAG-PACKET-v1` (fleet02/B01 auto14) at its proved scope:

- active banks are the original `J,K`;
- their exact cross block is (2.7), with `Delta=sigma_1 sigma_2=1`;
- the third bank is `D`;
- the hub `h` is put in the theorem's outside bank `W`, whose couplings to the active banks are allowed to be arbitrary;
- there are no `D-(J union K)` quadratic cross terms because (4.2) is a direct sum.

For `C=w w^T`, the theorem's off-diagonal energy is

`F_D=sum_{r!=s} C_rs^2 =1-1/m`.                                 (4.4)

At its proved `beta=1/4` specialization,

`||p_{X^T A_full X}||_infinity`
` <=22.104 Delta^(-2/5) F_D^(-1/10)`
` =22.104 (1-1/m)^(-1/10).                                      (4.5)

For the concrete live-strict choice `m=2^23>4/tau`,

`boxed: ||p_{X^T A_full X}||_infinity <22.105,}`                (4.6)

and this branch has a continuous `C_0` density.

So the exact same aligned rank-two/hub geometry that has an unbounded density with only two spectral directions is immediately paid once a genuinely independent third spectral packet is retained. This is a direct equation-level demonstration of what the global proof must route rather than discard.

## 5. Designated partner fleet04/B19 applied at an actual inequality

The completed fleet04/B19 theorem `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1` applies in its residual-diffuse exact-rank-three null-coloop normal form and proves, for `0<D_res<=1`,

`||p_Q||_infinity <34 sqrt(log(e/D_res)).`                       (5.1)

Therefore on the concrete proof-graph range

`e^-8 <= D_res <=1`,                                            (5.2)

one obtains the actual uniform inequality

`boxed: ||p_Q||_infinity <34 sqrt(9)=102.}`                     (5.3)

At its exact singular endpoint `D_res=0`, the same source records the completed bound `<5.844`; for `D_res>=1` it records `<11.748`. I do not infer a uniform punctured-endpoint bound as `D_res downarrow0`, and I do not transfer this theorem outside its proved null-coloop/residual-diffuse scope.

This satisfies the B19 partner requirement at equation level while preserving the partner's correction boundary.

## 6. Compact conditional full-proof assembly after the new correction

The strongest current end-to-end map is now:

1. Reduce the full target to one fixed strict `N3(tau)` problem only through the completed owner-pinned physical-pivot synthesis; take `tau=2^-20`.
2. If the `1/16` spectral-window leverage is diffuse, the completed spectral-window theorem gives `<217.085` with continuous `C_0` density.
3. Otherwise the tiny-N3 compiler produces one literal physical hub/cut packet with two star energies `>beta` and leaf cross Frobenius energy `>E0`.
4. If fifth-volume is diffuse, the completed `D_5` theorem gives `<198.634` continuously.
5. The only residual global packet is `STAR4`, split into a quantitative rank-two branch or a relative-rank-one tube.
6. In the rank-two branch, the newest selected-volume theorem pays one large branch continuously (`<356.765`) and otherwise produces either an actual physical selected-volume anchor or the aligned near-rank-two core.
7. **New this run:** the aligned hub/rank-two core cannot be paid from those local currencies alone. Section 3 provides an arbitrarily strict-N3 family with `Delta=1`, exact two-sided alignment, star energies `2,2`, and unbounded density. The reason it is not a full-target counterexample is exactly that it has only two large spectral directions.
8. Therefore the first essential implication is no longer a local two-channel smoothing theorem. It is the global, product-preserving third-resource routing statement below.

All signs are allowed in the cited analytic branches. Repeated eigenvalues are not treated as degeneracy. Exact null and nonzero-pivot endpoints remain separate. Arbitrary bounded-density laws, including fragmented supports, remain permitted.

## 7. First essential missing implication after this run

`QFORM-STAR4-THIRD-SPECTRAL-RESOURCE-ROUTING-v1`:

> In a full strict-N3 target matrix with `s_3(A)>=1` that has reached the aligned rank-two STAR4 survivor, locate the **third** spectral resource in original-product coordinates before any rotation destroys independence. Route it quantitatively to one of the already-paid mechanisms: a source-disjoint weighted-Fourier packet, a rank-three/selected-volume packet, a transverse receiver-curvature packet, an indefinite-pair/Schur bicore, a grouped-square/ridge branch, or an exact-null-coloop branch. The routing must retain arbitrary overlap/couplings; it may not simply delete the higher-rank/tail/self-curvature terms.

The stress family (4.2) proves this statement is correctly targeted: when the third resource is genuinely source-disjoint, an existing theorem pays it immediately. The remaining difficulty is precisely the overlapping third resource.

A useful invariant for the next run is the strict-N3 off-diagonal matrix

`Z=A-diag(A)`.                                                    (7.1)

Since `||diag(A)||_op<tau` and `s_3(A)>=1`, Weyl gives

`boxed: s_3(Z)>=1-tau.}`                                        (7.2)

Thus a third physical off-diagonal spectral direction of order one always exists in strict N3. The unresolved issue is not existence of third energy; it is converting (7.2), in the presence of the aligned STAR4 bicore, into a product-preserving packet to which a completed receiver applies.

This is the exact next mathematical target.

## 8. Status

- Full QFORM bounded-density conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.
- New negative theorem: `QFORM-ALIGNED-NULLPIVOT-TWOSIDED-LOCAL-LINF-FALSE-v1`, proved by (2.1)-(3.13).
- New positive stress splice: adding a genuine source-disjoint third rank-one spectral packet yields the continuous bound `<22.105` at the live strict-N3 scale.
- Partner application: exact-null-coloop residual-diffuse range `e^-8<=D_res<=1` gives `<102`.
- Execution remains `WITHOUT_VERIFIED_BRAIN`; repository retrieval/use is not claimed as native brain ingestion.
