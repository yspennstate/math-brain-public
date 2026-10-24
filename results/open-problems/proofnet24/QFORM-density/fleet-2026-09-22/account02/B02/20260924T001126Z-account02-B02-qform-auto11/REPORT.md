SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-24T00:11:26Z.
attacking: the first unpaid zero-pivot near-rank-one shared-hub tail; first extract every D'/D5 physical cross-volume consequence, then change mechanism at the vanishing-tail endpoint rather than delete a nonzero tail.

# account02/B02 auto11 — physical hub-lift exterior volumes and a cross-volume obstruction family

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Integrated Fourier estimate / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER L1 OPEN-NOT-REFUTED**

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, support, log-concavity, iid, diagonal-basis, or post-rotation-independence assumption is introduced. Continuity is asserted only where an actual unweighted `L1_t` characteristic-function estimate is available.

## 1. Fresh control and source pins actually used

Fresh owner control was resolved on `yspennstate/math-research-brain@f29ba9864622bd4e4eeedf5c5243e95787c710d6`; owner revision remains `2026-09-22.15`, QFORM-only. The required `AGENTS.md`, root/scheduled README owner message, `fleet.json`, `roles.json`, `PROTOCOL.md`, QFORM `MANIFEST/CURRENT_RESEARCH/CLAIMS/DELTAS/CORRECTION_INBOX/PATHWAYS/MEMORY_PROTOCOL`, the proof-first/Claude-latest requests, and this slot's assignment were read before the mathematics below. The previous B02 receiver-memory snapshot was also retrieved and used.

Required base source package:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Reviewed sharp Hausdorff--Young source:

- `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

It proves, for a literal physical cross block `M=A[I,J]`, `Z=E3(M)>0`, `1<=q<3/2`, and third-volume row marginals `alpha_i<=q/2`,

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`,              (1.1)

with an actual `L1_t` characteristic function. Its reviewed fifth-volume branch is

`||p_Q||_infinity <= (5e/sqrt(2)) E5(M)^(-1/10)`,                 (1.2)

again with `phi_Q in L1`, and has no marginal gate.

The completed B02 heavy-row cascade recorded in the preceding B02 report gives the marginal-free physical third-volume consequence

`||p_Q||_infinity <= 10.345084 E3(M)^(-1/6)`,                     (1.3)

also with `phi_Q in L1`; it is obtained by combining the sharp `q`-dependent D' estimate with its paid heavy-row complement, not by a new pointwise decay claim.

Newest **completed** designated partner used here is account03/B02 r39,
`QFORM-V1-GLOBAL-THREEBANK-COMPILER-v1`, fresh master path
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T210023Z-account03-B02-qform-r39/REPORT.md`.
For the overlap-one third-compound mass `V1`, it produces one physical three-bank partition with

`W >= (16/3125) V1`,                                              (1.4)

and, if one shared hub carries at least half of `W`,

`D_h >= W/2 >= (8/3125)V1`.                                      (1.5)

At the exact zero pivot `A_hh=0`, its coefficient identity is

`D_h = T_h = ||c||^2 ||r||^2 ||P_(c^perp) N P_(r^perp)||_F^2`.   (1.6)

No later account03/B02 report was complete on the fresh master at invocation start; r41 had only checker artifacts there, so no theorem from r41 is promoted below.

The current interactive two-bank/chirp and multiscale sources were also read for mechanism boundaries. In particular, they independently confirm that a tiny nonzero in-span/tail coefficient cannot be handled by a law-uniform pointwise `t^{-3/2}` perturbation argument; high-frequency averaging, not phase deletion, is required.

## 2. New exterior identity: a physical hub lifts every residual exterior degree

Fix one physical coordinate `h` and two disjoint original-coordinate banks `L,R`. Write

`c=A[L,h]`, `r=A[h,R]`, `N=A[L,R]`,
`u=||c||^2`, `w=||r||^2`,                                       (2.1)

and, when `u,w>0`,

`P_c=I-cc^T/u`, `P_r=I-rr^T/w`, `C=P_c N P_r`.                   (2.2)

Let `E_k(B)=e_k(B^T B)`, equivalently the sum of the squares of all `k x k` minors of `B`. Consider the two literal physical cross blocks

`M_R=A[{h} union L,R]=[r^T;N]`,
`M_L=A[L,{h} union R]=[c,N]`.                                    (2.3)

### Theorem 2.1 — `QFORM-PHYSICAL-HUBLIFT-EXTERIOR-v1`

For every integer `s>=1`,

`boxed: E_(s+1)(M_R) >= w E_s(C),`
`boxed: E_(s+1)(M_L) >= u E_s(C).`                               (2.4)

Consequently, with `m=max(u,w)`, one of the two **actual original-coordinate** cross blocks satisfies

`boxed: E_(s+1)(M_*) >= m E_s(C).`                               (2.5)

#### Proof

Retain in `E_(s+1)(M_R)` only row minors whose row set contains the hub row and `s` rows of `N`. By Cauchy--Binet/exterior algebra,

`sum_(S subset L, |S|=s) sum_(|T|=s+1)
 det([r;N_S]_T)^2
 =sum_S ||r wedge N_(i1) wedge ... wedge N_(is)||^2
 =w E_s(N P_r).`                                                 (2.6)

The last identity uses `r wedge a_1 wedge ... = r wedge P_(r^perp)a_1 wedge ...`. Since

`(P_c N P_r)^T(P_c N P_r)
 =(N P_r)^T P_c (N P_r)
 <=(N P_r)^T(N P_r)`                                             (2.7)

in positive-semidefinite order, every singular value of `C` is no larger than the corresponding singular value of `N P_r`; hence `E_s(C)<=E_s(NP_r)`. This proves the first inequality. The second is the transposed argument. No random coordinate is rotated, and no coefficient is deleted. QED.

This simple identity is useful precisely in the live near-low-rank collar: any nonzero residual exterior tail is automatically a **physical disjoint-cut** D'/D5 currency once the shared hub is put on the appropriate side.

## 3. Integrated Fourier consequences on the live zero-pivot packet

Taking `s=2` in (2.5) and applying the marginal-free physical `E3` receiver (1.3) gives, whenever `E2(C)>0`,

`boxed:
 ||p_Q||_infinity
 <=10.345084 [m E2(C)]^(-1/6),
 phi_Q in L1(R).}`                                                (3.1)

If the actual chosen block already satisfies a sharp-HY marginal gate, (1.1) may be substituted directly and can improve the coefficient.

Taking `s=4` and using the reviewed D5 estimate (1.2) gives, whenever `E4(C)>0`,

`boxed:
 ||p_Q||_infinity
 <=(5e/sqrt(2)) [m E4(C)]^(-1/10),
 phi_Q in L1(R).}`                                                (3.2)

Thus D5 remains a live complementary receiver rather than a historical side remark. In particular, higher-rank residual tails are paid on an actual physical cross block even though the shared hub itself belongs to only one side of the cut.

For a quantitative near-rank-one parametrisation, let the squared singular values of `C` be

`x1>=x2>=...>=0`, `S=sum_j xj=||C||_F^2`,
`theta=(sum_(j>=2)xj)/S`,                                        (3.3)

and put

`T=u w S`, `b=min(u,w)/S`.                                       (3.4)

Then

`E2(C)>=x1 sum_(j>=2)xj=theta(1-theta)S^2`,                      (3.5)

while `m S^2=T/b`. Therefore (2.5) gives the explicit physical third-volume inequality

`boxed:
 E3(M_*) >= [theta(1-theta)/b] T,`                               (3.6)

and hence

`boxed:
 ||p_Q||_infinity
 <=10.345084 [theta(1-theta)T/b]^(-1/6).}`                       (3.7)

This is a genuine nonzero-tail estimate. It does not pretend that (3.7) remains uniform as `theta->0`; the degeneration is real for D'/D5 and is isolated below.

## 4. Designated partner r39 applied to a real inequality

On the r39 heavy shared-hub branch, assume the shared pivot is exactly zero, so (1.6) gives `T=D_h`, and suppose the partner's two-star scale parameter satisfies `b<=1`. If

`1/64 <= theta < 1/2`,                                           (4.1)

then from (1.5), (3.6), and monotonicity of `theta(1-theta)` on `[0,1/2]`, one actual physical cut obeys

`E3(M_*)
 >= (63/4096)(8/3125)V1
 = 3.9375e-5 V1`.                                                (4.2)

Substitution into (1.3) gives the new live bound

`boxed:
 ||p_Q||_infinity
 <=56.087222 V1^(-1/6),
 phi_Q in L1.}`                                                   (4.3)

On the target-scale branch `V1>1/4`,

`boxed: ||p_Q||_infinity <70.665472.`                            (4.4)

The partner r39 theorem already pays the favorable `sr(C)>=2` branch with a better coefficient. Since

`sr(C)=S/x1=1/(1-theta)`,                                        (4.5)

(4.3) extends that **same `b<=1` heavy-zero-pivot branch** down from stable rank `2` to stable rank `64/63`. What remains from this route is the genuinely ultra-near-rank-one collar `0<theta<1/64`, together with the partner's separately named `b>1` two-star-dominated collar. This is a strict narrowing, not a closure claim.

## 5. A physical carrier theorem: tails outside the carrier need not be deleted

The previous B02 tensor theorem was stated for a whole rank-one residual crossing. A useful strengthening is obtained by conditioning rather than perturbing.

Choose five distinct original coordinates: a hub `h`, two coordinates `Y={y1,y2}`, and two coordinates `Z={z1,z2}`. Assume

- `A_hh=0`;
- the two hub-star vectors `c=A[Y,h]` and `r=A[h,Z]` are nonzero;
- the literal `2 x 2` physical cross matrix `B=A[Y,Z]` has rank one;
- `P_(c^perp) B P_(r^perp)` is nonzero.

Put

`T_phys=||c||^2 ||r||^2 ||P_(c^perp) B P_(r^perp)||_F^2`.        (5.1)

### Theorem 5.1 — `QFORM-PHYSICAL-RANKONE-CARRIER-L1-v1`

For the **full ambient quadratic form**, with every coefficient involving every coordinate outside these five left completely arbitrary,

`boxed:
 ||p_Q||_infinity <=3 T_phys^(-1/6),
 integral_R |phi_Q(t)|dt <=6pi T_phys^(-1/6).}`                  (5.2)

Hence the density is continuous and vanishes at infinity.

#### Proof

Condition all original coordinates outside the five-coordinate carrier. Their quadratic terms become constants and all couplings into the carrier become affine terms; the carrier quadratic matrix itself is unchanged. The two original-coordinate pairs `Y` and `Z` have joint densities at most one.

Inside each pair, use a determinant-one orthogonal change to put the star vector on the first axis. The joint density cap stays at most one; no claim of coordinate independence after the change is made. The transformed rank-one cross matrix has the form

`[[d,q],[p,sigma]]`, `sigma!=0`, `d sigma-pq=0`.                 (5.3)

The determinant-one shears that preserve the first coordinates,

`Y2'=Y2+(q/sigma)Y1`, `Z2'=Z2+(p/sigma)Z1`,                     (5.4)

reduce the crossing **exactly** to `sigma Y2'Z2'`; they again preserve the two planar density caps. The conditional form is therefore exactly the three-bank tensor form proved in the preceding B02 run, now with `M_Y=M_Z=1`. Its uniform conditional estimates are (5.2). Averaging the conditional characteristic functions and using Tonelli gives the same global `L1_t` bound; averaging conditional densities gives the same `Linfinity` bound. No outside tail is thrown away. QED.

This theorem is intentionally a physical-carrier statement: it does not say that every diffuse near-rank-one singular vector admits such a five-coordinate carrier.

## 6. Exact-target obstruction to a D'/D5-only structural closure

Consider seven original coordinates

`(h,y1,z1,y2,z2,u,v)`

and the symmetric matrix `A_epsilon` whose only nonzero upper-triangular entries are

`A_(h,y1)=1`, `A_(h,z1)=1`, `A_(y2,z2)=1`, `A_(u,v)=epsilon`,     (6.1)

with `0<|epsilon|<=1`.

Its nonzero eigenvalues are

`+sqrt(2), -sqrt(2), +1, -1, +|epsilon|, -|epsilon|`,             (6.2)

so the exact owner spectral hypothesis is satisfied uniformly: in fact four eigenvalues have modulus at least one.

For **every** disjoint physical cut `I,J`, the crossing block is the sum of at most three rank-one pieces: the crossing part of the two-leaf star, the `(y2,z2)` edge, and the epsilon edge. Therefore

`rank A_epsilon[I,J] <=3`, hence `E5(A_epsilon[I,J])=0`.          (6.3)

At `epsilon=0` every such crossing block has rank at most two. More precisely, a nonzero `3 x 3` crossing minor for `epsilon!=0` must use the epsilon edge, the `(y2,z2)` edge, and one of the at most two star edges. The supports are disjoint, so each such determinant is `+/-epsilon`; a fixed cut supports at most two of them. Thus

`boxed:
 sup_(I cap J=emptyset) E3(A_epsilon[I,J]) <=2 epsilon^2,
 sup_(I cap J=emptyset) E5(A_epsilon[I,J]) =0.}`                 (6.4)

Consequently any proof architecture requiring a universal positive lower bound on a physical D' `E3` currency or a D5 currency from the three-large-eigenvalue hypothesis is false. The sharp-HY/D' bound on this family necessarily degenerates at least like `|epsilon|^(-1/3)`, and D5 is identically unavailable.

This is **not** a counterexample to QFORM or to Fourier `L1`. The five-coordinate carrier `(h,y1,z1,y2,z2)` has `T_phys=1`. Theorem 5.1 therefore yields, for every independent cap-one product law and every `epsilon`,

`boxed:
 ||p_(X^T A_epsilon X)||_infinity <=3,
 integral_R |phi_(X^T A_epsilon X)(t)|dt <=6pi.}`                (6.5)

Equivalently, one may condition `(u,v)`; the epsilon product becomes only a constant on the carrier slice. Thus (6.1) is a source-valid **method counterexample** to D'/D5-only structural closure while simultaneously exhibiting a uniform integrated-Fourier receiver. This is the intended complementary-mechanism lesson.

## 7. Why the first unpaid implication is now sharper

Three unchanged mechanisms were checked against the ultra-near-rank-one collar and were not promoted:

1. deleting a small nonzero tail is invalid without moment/support assumptions;
2. extending the rank-one tensor proof by a law-uniform pointwise `t^{-3/2}` perturbation is blocked by the chirp/bumpy-law mechanism in the current multiscale source;
3. D' and D5 see every nonzero tail through Theorem 2.1, but their exterior currencies vanish continuously as the tail exterior volume goes to zero, as the explicit target family (6.1) demonstrates.

The mechanism was therefore changed to **physical carrier conditioning** plus an explicit obstruction calculation. This pays every branch where a bounded physical `2+2` rank-one carrier exists, while retaining all nonzero outside coefficients, and it proves that a global E3/D5 extraction alone cannot finish the target.

The next B02 implication is

`QFORM-NEARRANK1-SHAREDHUB-MIXED2x2-L1-v1`:

handle the remaining zero-pivot shared-hub packet when the physical D'/D5 currencies are arbitrarily small and no rank-one physical carrier can be isolated. After the two physical hub cuts have vanishing third volume, the algebraic carrier is forced toward a two-dimensional bank on each side; the missing estimate is an **integrated** receiver for the resulting full-rank `2 x 2` mixed bank kernel, or an equivalent grouped/two-bank factorization. The current two-bank chirp/Strichartz sources strongly suggest averaging in frequency rather than pointwise tail perturbation.

The full QFORM conjecture remains OPEN. Full-target continuity remains OPEN. The unrestricted target-wide universal `sup integral |phi_Q|` assertion remains OPEN / not refuted.

## 8. Telemetry and protocol scope

Authenticated repository retrieval and the previous B02 receiver-memory snapshot were both used in this invocation, so the programme's narrow protocol label is `VERIFIED_BRAIN`; this does not assert native learned-memory ingestion (`full_brain_connected=false`). Model self-report: GPT-5.6 Sol. Configured reasoning effort, provider reasoning tokens, provider thinking seconds, and pure-thinking duration are not exposed: `UNKNOWN/null`. Any wall elapsed interval includes repository/runtime overhead and is not pure thinking time.
