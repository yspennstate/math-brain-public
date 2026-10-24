SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T08:18:21Z.
attacking: the normalized-heavy-core residue in partner account02/B19 — split only the diffuse original-coordinate tail, preserve every heavy row, and force a balanced repartition or a finite directionally concentrated core.

# account01/B19 r13 — diffuse-tail splitting inside the normalized-heavy-core branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Universal proof assembly / SYNTHESIS  
**Owner control used:** revision `2026-09-22.15`; programme revision `2026-09-22.5`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN`.

The unrestricted theorem remains open. This run proves a new product-preserving payment inside the latest designated-partner residue. It uses only exact repartitioning of ORIGINAL coordinates. It does not rotate the product law and declare the rotated coordinates independent; it does not delete a small quadratic component; it does not use an arbitrary-joint coarea inequality, a conditional density cap as a substitute for independence, a pointwise law-uniform oscillatory decay estimate, or a universal single-good-minor selector.

## 1. Source-pinned inputs actually used

### 1.1 Designated partner account02/B19

The current designated partner is

`yspennstate/math-open-problems@32e921cf63500a7118cf30724f9e67d7997185e0`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T071320Z-account02-B19-QFORM/REPORT.md`.

It works in the exact-rank-three state

`A=R M R^T`, `R^T R=I_3`,                                      (1.1)

where `M=M^T` is invertible and every eigenvalue of `M` has modulus at least one. For an ORIGINAL-coordinate partition `I union J`, it writes

`P=R_I`, `S=R_J`, `G=P^T P`, `H=S^T S=I-G`,                    (1.2)

and assumes

`rank(P)=3`, `rank(C)=2`, `C=A_IJ=P M S^T`.                    (1.3)

Then `rank(S)=rank(H)=2`. Let `u` span `ker H` and put `W=u^perp`. If `s_j` is row `j` of `S`, define the normalized `J`-frame

`v_j=(H|_W)^(-1/2)s_j`,                                         (1.4)

so

`sum_{j in J} v_j v_j^T=I_W`,
`ell_j:=||v_j||^2=s_j^T(H|_W)^(-1)s_j`,
`sum_j ell_j=2`.                                                (1.5)

The partner proves that if

`lambda_min(H|_W)>=1/64`                                        (1.6)

and every `ell_j<=1/16`, then one can repartition ORIGINAL coordinates and pay the exact same quadratic form by a continuous density bound `<776`. Hence its first exact-rank-three rank-two-cross residue is

`(NR) lambda_min(H|_W)<1/64`,                                   (1.7)

or

`(HC) J_h={j:ell_j>1/16} is nonempty and |J_h|<=31`.             (1.8)

The cardinality follows from `sum ell_j=2`.

### 1.2 Product-safe analytic receiver

The analytic receiver used by the partner is source-pinned at

`yspennstate/math-open-problems@d72be34399b8d0325c715973e7af3a37df7ce227`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260923T060843Z-account01-B19-QFORM-auto11/REPORT.md`.

In its stated original-product scope, for an exact-rank-two physical cross block with singular product `rho'=s1(C')s2(C')`, a three-dimensional source space containing all source self curvature, and transverse source-row norm `R'>0`, it gives

`||p_Q||_infinity <= C_* (R')^(-1/4) (rho')^(-3/8)`,             (1.9)

where

`C_*=2^(15/4) 3^(-3/8)=8.911319467...`,                         (1.10)

and the density is continuous and vanishes at infinity.

The present run applies (1.9) to a new partition produced from the partner's normalized frame. Thus peer mathematics is used in an actual inequality rather than cited as status.

## 2. A two-dimensional diffuse-remainder split

The partner's random split can be localized to a diffuse SUBFRAME while every normalized-heavy row is left untouched.

### Lemma 2.1 — `QFORM-2D-DIFFUSE-REMAINDER-SPLIT-v1`

Let `(w_j)_{j in D}` be a finite Parseval frame in `R^2`,

`sum_{j in D} w_j w_j^T=I_2`,                                   (2.1)

and suppose

`max_j ||w_j||^2 <= epsilon <1/2`.                              (2.2)

Then there is a subset `K subset D` such that, with

`W_K=sum_{j in K}w_jw_j^T`,
`W_{Kc}=sum_{j in D\K}w_jw_j^T=I-W_K`,                          (2.3)

one has

`eta0 I_2 <= W_K,W_{Kc} <=(1-eta0)I_2`,                         (2.4)

where

`eta0=(1-2epsilon)/16`.                                         (2.5)

#### Proof

For every unordered pair `T={i,k}` put

`d_T=det(w_i,w_k)^2`.                                            (2.6)

Cauchy--Binet gives

`sum_T d_T=det(sum_j w_jw_j^T)=1`.                              (2.7)

For each fixed `j`, the exact pair-marginal identity is

`sum_{T:j in T} d_T=||w_j||^2`.                                 (2.8)

Indeed,

`sum_k det(w_j,w_k)^2
 =||w_j||^2 sum_k||w_k||^2
  -w_j^T(sum_k w_kw_k^T)w_j
 =2||w_j||^2-||w_j||^2`.

Choose a random subset `K` by independent fair coins. By Cauchy--Binet again,

`det W_K=sum_{T subset K}d_T`,
`det W_{Kc}=sum_{U subset Kc}d_U`.                               (2.9)

For disjoint pairs `T,U`, the probability of `T subset K` and `U subset Kc` is `1/16`; for intersecting pairs it is zero. Hence

`E[det W_K det W_{Kc}]
 =(1/16) sum_{T cap U=empty}d_Td_U`.                             (2.10)

The ordered intersecting mass satisfies

`sum_{T cap U != empty}d_Td_U
 <=sum_j (sum_{T:j in T}d_T)^2
 =sum_j ||w_j||^4
 <=epsilon sum_j||w_j||^2
 =2epsilon`.                                                     (2.11)

Since the total ordered pair-pair mass is one,

`E[det W_K det W_{Kc}] >=(1-2epsilon)/16=eta0`.                 (2.12)

Therefore some deterministic `K` has

`det W_K det W_{Kc}>=eta0`.                                     (2.13)

Both matrices are positive semidefinite contractions, hence each determinant is at most one. Thus each determinant is at least `eta0`. In dimension two,

`lambda_min(T)=det(T)/lambda_max(T)>=det(T)`                     (2.14)

for every positive semidefinite contraction `T`. This gives the lower bounds in (2.4); the upper bounds follow from `W_K+W_{Kc}=I`. QED.

No physical coordinate is selected by a reciprocal determinant. The determinant mass is aggregated first and only then is one whole subset chosen.

## 3. Main theorem: the heavy core can be left in place if the diffuse tail has two-dimensional mass

Return to the partner setup (1.1)-(1.8) and assume the NR branch is excluded:

`lambda_min(H|_W)>=1/64`.                                       (3.1)

Let

`J_h={j in J: ell_j>1/16}`,
`D=J\J_h`,                                                       (3.2)

and define the normalized diffuse covariance

`V_D=sum_{j in D}v_jv_j^T`.                                     (3.3)

### Theorem 3.1 — `QFORM-RANK2-CROSS-HEAVYCORE-DIFFUSE-TAIL-SPLIT-v1`

Fix any

`delta>1/8`.                                                     (3.4)

If

`lambda_min(V_D)>=delta`,                                       (3.5)

then the exact quadratic form `Q=X^TAX`, for arbitrary independent scalar input densities bounded by one, has a continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <= 8192/[3^(3/8)(8 delta-1)].
`                                                                  (3.6)

All signs of `M` are allowed, all repeated-eigenvalue degeneracies are allowed, and no condition beyond the exact-rank-three setup is imposed on the input laws. In particular, at the convenient threshold

`delta=1/4`,                                                     (3.7)

one gets

`boxed: ||p_Q||_infinity <5426.`                                 (3.8)

#### Proof

Because (3.5) makes `V_D` invertible on `W`, normalize only the diffuse rows:

`w_j=V_D^(-1/2)v_j`, `j in D`.                                  (3.9)

Then

`sum_{j in D}w_jw_j^T=I_W`.                                    (3.10)

For every diffuse row,

`||w_j||^2
 =v_j^T V_D^(-1)v_j
 <=delta^(-1)||v_j||^2
 <=1/(16delta)=:epsilon`.                                       (3.11)

Because `delta>1/8`, `epsilon<1/2`; Lemma 2.1 therefore gives `K subset D` such that

`eta0 I_W <=sum_{j in K}w_jw_j^T,
              sum_{j in D\K}w_jw_j^T <=(1-eta0)I_W`,            (3.12)

and symmetrically with `K` and `D\K`, where

`eta0=(1-1/(8delta))/16=(8delta-1)/(128delta)`.                 (3.13)

Undoing the `V_D` normalization yields

`sum_{j in K}v_jv_j^T >=eta0 V_D>=eta I_W`,
`sum_{j in D\K}v_jv_j^T >=eta0 V_D>=eta I_W`,                   (3.14)

with the physical normalized balance parameter

`eta:=delta eta0=(8delta-1)/128`.                               (3.15)

Now return to unnormalized spectral rows. Since `s_j=H^(1/2)v_j` on `W`, put

`H_K=sum_{j in K}s_js_j^T`.                                     (3.16)

Equation (3.14) gives

`H_K>=eta H`.                                                    (3.17)

The retained bank is

`J'=J\K=J_h union (D\K)`.                                      (3.18)

Because the retained diffuse part alone satisfies the second inequality in (3.14),

`H':=R_{J'}^T R_{J'}>=eta H`.                                  (3.19)

On the other hand, (3.17) and `H'=H-H_K` imply

`H'<=(1-eta)H`.                                                  (3.20)

Define the complementary ORIGINAL-coordinate source bank

`I'=I union K`,                                                  (3.21)

so

`G':=R_{I'}^T R_{I'}=I-H'`.                                    (3.22)

On the kernel direction `u`, `H'u=0`, hence `G'u=u`. On `W`, (3.20) and `H<=I` give

`G'>=eta I`.                                                     (3.23)

Therefore

`G'>=eta I_3`.                                                   (3.24)

By (3.1) and (3.19),

`lambda_min^+(H')>=eta/64`.                                    (3.25)

Thus `P':=R_{I'}` has full column rank three and `S':=R_{J'}` has rank two.

The NEW physical cross block is the exact block of the original matrix

`C'=A[I',J']=P'MS'^T`.                                         (3.26)

Since `s_min(P')>=sqrt(eta)`, `s_min(M)>=1`, and the least nonzero singular value of `S'` is at least `sqrt(eta/64)`, one obtains

`boxed: s2(C')>=eta/8`.                                         (3.27)

Hence

`rho':=s1(C')s2(C')>=s2(C')^2>=eta^2/64`.                      (3.28)

The source self block is

`B'=A[I',I']=P'MP'^T`.                                         (3.29)

Let `Q'=P'(G')^(-1/2)`, so `Q'^TQ'=I_3`. On `range(P')`, `B'` is orthogonally represented by

`(G')^(1/2)M(G')^(1/2)`.                                       (3.30)

Therefore

`s_min^+(B')>=lambda_min(G')s_min(M)>=eta`.                     (3.31)

In particular, for the unit transverse source vector `r'` required by the receiver,

`R':=||B'r'||>=eta`.                                            (3.32)

Now apply the completed product-safe receiver (1.9) to the ACTUAL repartition `(I',J')`. It gives

`||p_Q||_infinity
 <=C_* eta^(-1/4)(eta^2/64)^(-3/8)
 =64*3^(-3/8) eta^(-1)`.                                       (3.33)

Substituting (3.15),

`||p_Q||_infinity
 <=8192/[3^(3/8)(8delta-1)]`,                                   (3.34)

which is (3.6). Because the receiver proves an `L^1` characteristic function in its stated scope, the density here is continuous and vanishes at infinity. QED.

### Numerical specialization

For `delta=1/4`,

`epsilon=1/4`,
`eta0=1/32`,
`eta=1/128`,
`s2(C')>=1/1024`,
`rho'>=2^(-20)`,
`R'>=1/128`.                                                     (3.35)

Then

`C_* eta^(-1/4)rho'^(-3/8)
 =8192/3^(3/8)
 =5425.871111295...<5426`.                                      (3.36)

The constant is deliberately not optimized; its role is to be universal and dimension-free.

## 4. What an unpaid heavy-core state must now look like

Take `delta=1/4`. If the partner HC state is NOT paid by Theorem 3.1, then

`lambda_min(V_D)<1/4`.                                          (4.1)

Choose a unit `w in W` with

`w^T V_D w<1/4`.                                                (4.2)

Because the full normalized frame is Parseval,

`V_h:=sum_{j in J_h}v_jv_j^T=I_W-V_D`.                          (4.3)

Therefore

`w^T V_h w>3/4`, i.e.
`sum_{j in J_h} |<w,v_j>|^2>3/4`.                              (4.4)

Since `|J_h|<=31`, one ORIGINAL heavy coordinate `j_*` satisfies

`boxed: |<w,v_{j_*}>|^2>3/124.`                                (4.5)

Thus the former qualitative HC branch has become a quantitative **finite directionally concentrated core**.

This has a physical-frame version. Put

`q=H^(-1/2)w / ||H^(-1/2)w||`.                                 (4.6)

By (3.1), `||H^(-1/2)w||^2<=64`. Since `s_j=H^(1/2)v_j`,

`|<q,s_{j_*}>|^2
 =|<w,v_{j_*}>|^2 / ||H^(-1/2)w||^2
 >3/7936`.                                                      (4.7)

Also the whole heavy core carries actual spectral-frame mass

`q^T (sum_{j in J_h}s_js_j^T) q
 =w^T V_h w / ||H^(-1/2)w||^2
 >3/256`.                                                       (4.8)

These are fixed positive numbers independent of dimension, input laws, and the signs or magnitudes of the three nonzero eigenvalues beyond their normalization `|lambda(M)|>=1`.

No conclusion is drawn from (4.5)-(4.8) by treating the remaining diffuse component as a small random perturbation. The live corrections forbid that step for arbitrary fragmented/unbounded cap-one laws.

## 5. Compact conditional proof assembly after this run

Within the current exact-rank-three rank-two-cross chamber, a source-valid conditional graph is now:

1. The current compound-energy route supplies the rank-two cross product threshold `rho=s1(C)s2(C)>=sqrt(29/3072)` before this collar.
2. The account03/B19 frame-defect identity plus the completed account01/B19 receiver pays every balanced-frame state `Theta>=2^-12` by a continuous bound `<96`.
3. In the near-coloop collar, designated partner account02/B19 pays every state satisfying (3.1) with **all** normalized row leverages `<=1/16` by `<776`.
4. This run pays the partner's HC state whenever the complement of its at-most-31 heavy rows still has normalized covariance `lambda_min(V_D)>=1/4`, by `<5426`.
5. Hence every still-unpaid exact-rank-three rank-two-cross state lies in one of only two geometries:

   `(NR) lambda_min(H|_W)<1/64`,                                  (5.1)

   or

   `(CHC) lambda_min(H|_W)>=1/64`, |J_h|<=31, and there is a unit w in W with
         sum_{j in J_h}|<w,v_j>|^2>3/4,                          (5.2)

   equivalently with one physical heavy row satisfying (4.7).

This is a strict narrowing of the designated partner's `(NR) or (HC)` residue: an HC state with genuinely two-dimensional diffuse tail is no longer open.

The global arbitrary-extra-spectrum/N3 descent into this exact-rank-three graph remains a separate debt. Therefore this report does NOT claim the full theorem.

## 6. First essential missing inequality

The first unresolved implication on this route is now

`QFORM-RANK2-CROSS-NEARRANKDROP-OR-CONCENTRATED-HEAVYCORE-v1`:

> In the exact-rank-three setup (1.1)-(1.3), under the current aggregate cross threshold, prove a universal density payment in either the near-rank-drop geometry `(NR)` of (5.1), or the concentrated finite-heavy-core geometry `(CHC)` of (5.2), without deleting a small frame component and without replacing an original product bank by a generic dependent projected pair.

The most concrete CHC subproblem is to use the finite set `J_h` (at most 31 ORIGINAL coordinates) together with the fixed directional mass (4.8) and the remaining nearly rank-one diffuse bank to expose one of the already-paid grouped-coordinate, scalar-Schur, ridge, or exact-null-coloop receivers. The right operation must aggregate the diffuse bank before reciprocal minor payment. The most concrete NR subproblem is the corresponding punctured line-bank stability statement. The exact rank-drop endpoints are already covered in several peer normal forms; the missing issue is a coefficient-uniform passage that retains original-product provenance.

## 7. Signs, degeneracies, regularity, and corrections

- **Signs:** the proof uses only singular values of `M`, frame Gramians, and the sign-free receiver (1.9). Every inertia pattern of the exact rank-three `M` is allowed.
- **Degeneracies:** repeated eigenvalues are harmless. The only rank assumptions are the explicit current branch assumptions `rank(P)=3`, `rank(C)=rank(S)=2`. The new diffuse-tail theorem assumes the quantitative lower bound (3.5); its failure is retained exactly as the new residue.
- **Input laws:** only independence of the ORIGINAL scalar coordinates and their density caps `<=1` are used through the completed receiver. No moments, centering, identical laws, compact support, connected support, or regularity of the input densities is required.
- **Product provenance:** `K` is literally a subset of ORIGINAL coordinate indices. Repartitioning changes no random variable and performs no spectral rotation of the product law.
- **Continuity:** Theorem 3.1 inherits continuity from the completed receiver. Full-target continuity remains OPEN and is tracked separately from essential boundedness.
- **Corrections preserved:** no arbitrary-joint rank-three coarea estimate; no positive moment of a conditional projection-density supremum; no post-rotation independence; no conditional density cap used as independence; no law-uniform pointwise quadratic-phase decay; no uniform matrix-perturbation continuity; no universal fixed-good-minor extraction.

## 8. Finite checks

The run checker verifies

`C_*=8.911319467025024`,
`delta=1/4`,
`epsilon=1/4`,
`eta0=1/32`,
`eta=1/128`,
`rho_min=2^-20`,
`bound=5425.871111295188`,
`3/(4*31)=0.024193548387096774`.

It also numerically verifies on random two-dimensional Parseval frames the exact Cauchy--Binet identities

`sum_{i<j}det(w_i,w_j)^2=1`,
`sum_{k!=j}det(w_j,w_k)^2=||w_j||^2`,

up to floating-point error. These computations are checks only; the proof above is exact.

## 9. Status

- `QFORM-2D-DIFFUSE-REMAINDER-SPLIT-v1`: **PROVED**.
- `QFORM-RANK2-CROSS-HEAVYCORE-DIFFUSE-TAIL-SPLIT-v1`: **PROVED** in the exact stated branch; `delta=1/4` gives continuous density `<5426`.
- Designated-partner `(HC)` branch with two-dimensional diffuse remainder: **PAID**.
- Remaining partner residue: **NR or concentrated finite heavy core CHC**.
- Full arbitrary-extra-spectrum/N3 splice: **OPEN**.
- Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.
