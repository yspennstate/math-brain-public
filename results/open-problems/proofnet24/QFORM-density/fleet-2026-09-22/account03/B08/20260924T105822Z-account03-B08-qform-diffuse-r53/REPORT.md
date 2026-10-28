SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T10:58:22Z.
attacking: the exact-rank-two child punctured alignment collar by re-cutting the hidden bankwise mismatch direction into a literal third-compound crossing, with no dependence on the physical hub scalar.

# account03/B08 r53 — mismatch re-cut removes the near-null-hub obstruction outside the ultra-puncture

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW CONTINUOUS DENSITY BRANCH + ULTRA-COLLAR SHRINK / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains **OPEN** and global continuity remains **OPEN**. This report works only in the inherited exact-rank-two deletion-child chamber. It proves a new product-safe re-cut theorem which turns the globally transverse bank-slope mismatch into an actual third singular crossing direction. It uses only original-coordinate partitions and therefore does not rotate the independent random coordinates. No moment, compact-support, connected-support, Gaussian, log-concave, iid, conditional-density-cap, arbitrary-joint coarea, pointwise quadratic-phase decay, or random-small-perturbation assumption is used.

## 1. Fresh controls and source pins


The current-hour canonical account03/B08 login already existed from the immediately preceding run, so it was preserved rather than overwritten, as required by `PROTOCOL.md`; this run has its own unique start/finish records.

Immediate predecessor used here:

- account03/B08 r52, `yspennstate/math-open-problems@fc449241245b5ca5762686d95cedee5acfd2f2e9`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T102327Z-account03-B08-qform-diffuse-r52/REPORT.md`.

The literal-crossing endpoint used below is the completed marginal-free third-compound receiver already used in the B08 chain: for an original-coordinate crossing matrix `M`, if

`Delta_3(M):=e_3(M M^T)^(1/6)>0`,

then the complete ambient quadratic form has

`||p_Q||_infinity <= 6^(4/3)/Delta_3(M)`,

and `p_Q in C_0(R)`. The receiver retains arbitrary same-side quadratic curvature. A source-pinned B08 application with this exact constant is account01/B08 r49, and its source chain points to account02/B08 r35, `yspennstate/math-open-problems@087cf5aa5cfcee4eb6ae243facb9e0fcf2391e29`.

The designated account04/B08 partner input actually applied in Section 6 is `QFORM-DISTRIBUTED-STAR-DERIVATIVE-SPLIT-v1`, `yspennstate/math-open-problems@f324267086411b9725aa0733e108ab6efc2e760a`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260924T081435Z-account04-B08-QFORM-r3/REPORT.md`.

The newest correction `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1` is respected: this report does **not** attempt to upgrade the partner square-root small-ball bound through the refuted universal mixed-norm interface. Instead the new density estimate is obtained directly from a literal physical crossing.

## 2. Inherited exact-child geometry

Write the actual original-coordinate deletion geometry as

`A = [[a,b^T],[b,C]]`,                                            (2.1)

with physical hub coordinate indexed by `0`. On the exact-rank-two child endpoint,

`C=V Lambda V^T`, `V^T V=I_2`,                                  (2.2)

and

`m:=s_2(Lambda) >= m_0 L`, `m_0=sqrt(47/48)=0.9895285072531598...` (2.3)

in the live chamber. The physical two-frame is diffuse:

`mu:=max_i ||V_i||_2^2 <=1/16`.                                 (2.4)

The previous balanced physical cut `J union K` satisfies

`G:=V_J^T V_J >= g I_2`,
`H:=V_K^T V_K=I-G >= g I_2`,                                    (2.5)

with

`g=1/2-1/(4 sqrt(2))=0.32322330470336313...`.                    (2.6)

Let the bankwise least-squares coefficients be

`c_J=G^{-1} V_J^T b_J`, `c_K=H^{-1} V_K^T b_K`,                  (2.7)

with residuals

`r_J=b_J-V_J c_J`, `r_K=b_K-V_K c_K`,                            (2.8)

so `V_J^T r_J=0`, `V_K^T r_K=0`. Put

`e_J=||r_J||`, `e_K=||r_K||`, `e=(e_J^2+e_K^2)^(1/2)`,            (2.9)

`delta=c_J-c_K`, `c_*=G c_J+H c_K`,                              (2.10)

and

`u=b-V c_*`, `beta=||u||=dist(b,range(V))`.                       (2.11)

The exact split-alignment identity from r51/r52 gives

`u=r+w`,                                                          (2.12)

where `r=(r_J,r_K)` and

`w_J=V_J H delta`, `w_K=-V_K G delta`.                            (2.13)

Moreover

`V^T w=0`, `r perpendicular w`,                                  (2.14)

and

`beta^2=e^2+||w||^2`.                                            (2.15)

The old cut therefore hides the mismatch `w` completely inside the two bankwise carrier planes. The purpose of this run is to **re-cut the same original coordinates** so that this hidden global direction becomes transverse to one bank and can feed a third-compound crossing.

## 3. The mismatch direction itself is a diffuse third frame vector

Set `omega=||w||`, and suppose `omega>0`. Because `H=I-G`, the matrices `G,H` commute and their eigenvalues lie in `[g,1-g]`. Hence

`omega^2 = delta^T G H delta >= g(1-g)||delta||^2`.               (3.1)

For `i in J`,

`|w_i|^2=|V_i H delta|^2`
` <= ||V_i||^2 ||H delta||^2`
` <= mu (1-g)^2 ||delta||^2`,                                   (3.2)

and the same bound holds on `K` with `G` in place of `H`. Therefore

`max_i |w_i|^2/omega^2 <= alpha`,                                 (3.3)

where

`alpha:=mu(1-g)/g=0.1308647700847534...`.                         (3.4)

Let

`W=w/omega`, `U=[V,W]`.                                          (3.5)

By `V^T w=0`, `U` has orthonormal columns. Its physical row leverage is bounded by

`max_i ||U_i||^2 <= mu+alpha = mu/g =:q`.                         (3.6)

At the live constants,

`q=0.1933647700847534... <1/3`.                                  (3.7)

This is the first useful implication: although the original transverse vector `u/beta` may be too concentrated when `beta` is only a few times `e`, the *mismatch part* `w/omega` is automatically diffuse enough to balance as a genuine three-frame.

## 4. New theorem: re-cut the mismatch into a literal third crossing direction

### Theorem 4.1 — `QFORM-MISMATCH-RECUT-THIRDCOMPOUND-v1`

Assume (2.1)-(2.15), `mu<=1/16`, the live value of `g` in (2.6), and

`beta>4e`.                                                        (4.1)

Define

`q=mu/g`,
`c=1/2-sqrt(3q/4)=0.11918038710753742...`,                        (4.2)

and

`d_*=(sqrt(15c)-1)/4=0.08426279020153638...`.                    (4.3)

Then there is an ORIGINAL-coordinate partition `P union T` of the child coordinates for which the literal crossing

`M=A[{0} union P,T]=[b_T^T; V_P Lambda V_T^T]`                    (4.4)

satisfies

`boxed: Delta_3(M)
 >= (c m)^(2/3) (d_* beta)^(1/3).`                               (4.5)

Consequently every admissible cap-one product law has

`boxed: ||p_Q||_infinity
 <= 6^(4/3) (c m)^(-2/3)(d_* beta)^(-1/3),`                      (4.6)

and on this branch

`boxed: p_Q in C_0(R).`                                          (4.7)

In particular, using `m>=m_0 L`,

`boxed: ||p_Q||_infinity
 <=103.411219 L^(-2/3) beta^(-1/3).`                             (4.8)

The bound is completely independent of the physical hub scalar `a`.

### Proof

**Step 1: balance the three-frame `[V,W]` by a fresh physical half-cut.**

Put each child coordinate independently in `T` with probability `1/2`. Then

`E[U_T^T U_T]=(1/2)I_3`.                                         (4.9)

Since the rows `U_i` have squared norms at most `q` and `sum_i ||U_i||^2=3`,

`E ||U_T^T U_T-(1/2)I_3||_F^2`
` =(1/4) sum_i ||U_i||^4`
` <=3q/4`.                                                       (4.10)

Therefore at least one actual physical cut satisfies

`||U_T^T U_T-(1/2)I_3||_op`
` <=||.||_F<=sqrt(3q/4)`.                                       (4.11)

For that cut, and its complement `P`,

`U_T^T U_T >=c I_3`, `U_P^T U_P>=c I_3`.                        (4.12)

In particular the two-frame principal blocks obey

`V_T^T V_T>=cI_2`, `V_P^T V_P>=cI_2`.                            (4.13)

**Step 2: the exact rank-two child keeps two target directions across the new cut.**

Set

`D=V_P Lambda V_T^T`.                                            (4.14)

Both `V_P` and `V_T` have smallest singular value at least `sqrt(c)`. Hence

`s_2(D)>=c m`.                                                    (4.15)

Also `row(D)=range(V_T)` because `V_P` has rank two and `Lambda` is invertible.

**Step 3: the mismatch vector is genuinely transverse on the new bank.**

The Gram matrix of `[V_T,W_T]` is at least `cI_3`. Taking the Schur complement of its `V_T^T V_T` block gives

`dist(W_T,range(V_T))^2>=c`.                                     (4.16)

Hence

`dist(w_T,range(V_T))>=sqrt(c) omega`.                            (4.17)

Since `b=Vc_*+r+w`, restriction to `T` and the triangle inequality give

`dist(b_T,range(V_T))`
` >=sqrt(c) omega-||r_T||`
` >=sqrt(c) omega-e`.                                            (4.18)

By (2.15) and `beta>4e`,

`omega=sqrt(beta^2-e^2)>sqrt(15/16) beta`,
`e<beta/4`.                                                       (4.19)

Substitution into (4.18) yields

`dist(b_T,row(D))>=d_* beta`,                                    (4.20)

with `d_*` exactly as in (4.3), which is positive.

**Step 4: third compound and density.**

Because `D` has rank two, appending the row `b_T^T` gives the exact rank-three pseudodeterminant identity

`e_3(MM^T)
 =s_1(D)^2 s_2(D)^2 dist(b_T,row(D))^2`.                          (4.21)

Using (4.15) and (4.20),

`Delta_3(M)=e_3(MM^T)^(1/6)`
` >=(c m)^(2/3)(d_* beta)^(1/3)`,                                (4.22)

which is (4.5). The source-pinned marginal-free physical third-compound receiver then gives (4.6) and the continuous `C_0` conclusion (4.7). No same-side term of the ambient quadratic form has been deleted. QED.

## 5. Live r52 application: the near-null hub obstruction disappears outside the ultra-puncture

The previous r52 collar first pays continuously if either old bank residual exceeds

`eta L`, `eta=2^(-20)`.                                          (5.1)

Thus on the still-unpaid hard collar we may assume

`e_J<eta L`, `e_K<eta L`,

hence

`e<sqrt(2) eta L`.                                               (5.2)

Define

`beta_0:=4 sqrt(2) eta L`
`       =5.394796609394436e-6 L`.                                (5.3)

If

`beta>beta_0`,                                                   (5.4)

then (5.2) implies `beta>4e`, so Theorem 4.1 applies **without any condition on `a`**. At the lower endpoint `beta=beta_0`, (4.8) gives

`boxed: ||p_Q||_infinity<5896.251/L,`
`boxed: p_Q in C_0(R).`                                          (5.5)

This is the main gain over r52. The previous Schur-Fresnel payment in this chamber required the separate pivot condition `|a|>=L/64`. The new re-cut theorem removes that requirement entirely: a nonzero bank-slope mismatch of size above `beta_0` itself creates a physical third-compound crossing after a fresh source-safe partition.

The exact aligned endpoint `beta=0` was already paid by `QFORM-EXACT-ALIGNED-RANK2-CHILD-ENDPOINT-v1` with

`||p_Q||_infinity<362.039/L`.                                    (5.6)

Therefore, after the already-paid old-bank residual branch, **the exact-rank-two child obstruction has been narrowed to the punctured ultra-collar**

`boxed: 0<beta<=5.394797e-6 L.`                                  (5.7)

There is no longer an independent near-null-hub scalar obstruction outside (5.7). Global continuity is still not claimed at the aligned endpoint (5.6); the new branch (5.5) itself is continuous.

## 6. Designated account04/B08 partner applied on the narrowed survivor

The live distributed-star gate from the B08 chain is

`||b||_2>rho_* L`,
`rho_*=0.0006247538095703261`.                                   (6.1)

Account04/B08 `QFORM-DISTRIBUTED-STAR-DERIVATIVE-SPLIT-v1` applies directly to the same matrix

`Q=aX_0^2+2X_0<b,Y>+Y^T C Y`,                                    (6.2)

retaining the entire child term `Y^T C Y`, regardless of its dependence on the star slope. The cap-one product marginal bound gives

`||p_{2<b,Y>}||_infinity<=1/(sqrt(2)||b||)`.                     (6.3)

The partner theorem therefore yields, on the actual remaining ultra-collar (5.7),

`boxed: sup_t P(|Q-t|<epsilon)
 <190.311 sqrt(epsilon/L).`                                      (6.4)

This is an actual partner inequality on the narrowed survivor. It is deliberately **not** relabeled as a bounded-density estimate. In view of the live correction against the universal hub-star fiber-`L^2` mixed-norm closure, no invalid upgrade of (6.4) is made here.

## 7. Deterministic regression and constants

A seeded deterministic checker was run on a 64-coordinate Hadamard two-frame and 100 independently generated admissible old cuts/mismatch directions. For each instance it verified:

- `V^T w=0` and the exact Pythagorean identity `beta^2=e^2+||w||^2`;
- the analytic augmented row-leverage gate `max_i ||[V_i,W_i]||^2<=q`;
- existence, by direct search, of a new physical cut satisfying both three-frame Gram lower bounds `>=cI_3`;
- the new-cut star-distance lower bound;
- the two nonzero singular directions of the exact child crossing;
- the third-compound lower bound in (4.22).

The run ended

`QFORM_B08_R53_MISMATCH_RECUT_CHECK_PASS`.

The exact constants checked were

`g=0.323223304703363`,
`alpha=0.130864770084753`,
`q=0.193364770084753`,
`c=0.119180387107537`,
`d_*=0.084262790201536`,
`beta_0/L=5.394796609394436e-06`,
`K_0=103.411218124048`,
`K_live=5896.250986754885`.

Across 100 seeded instances, the maximum observed augmented row leverage was `0.090770716030042`; the minimum observed `beta/e` was `4.284986710727479`; the minimum observed new-cut star distance divided by `beta` was `0.509143513863970`; the minimum observed new-cut Gram eigenvalue was `0.159661250630851`; and the minimum observed ratio of the actual third-compound `e_3` to the analytic lower bound was `10437.619522616809`. These computations are regression evidence only; Theorem 4.1 is analytic.

## 8. What remains

The full conjecture is not proved. This run closes the `beta>beta_0` part of the exact-rank-two child collar, including the formerly separate near-null physical-hub case. The next exact-child obstruction is now

`QFORM-EXACTTAIL-ULTRAPUNCTURE-COMPILER-v2`:

`0<dist(b,range(V))<=5.394797e-6 L`,                              (8.1)

with arbitrary hub scalar and arbitrary cap-one product laws, while the exact `beta=0` endpoint is already paid. A successful continuation must be genuinely uniform through this puncture; matrix-coefficient continuity alone is not sufficient because the source variables have no moment or bounded-support assumptions.

Separately, the nonzero child-tail version (`s_3(C)>0`) remains an overlapping-leakage problem and is not solved by this exact-rank-two theorem. The fresh correction against a universal hub-star fiber-`L^2` mixed norm makes direct literal crossings, pair-log hybrids, or another joint source-safe receiver the appropriate next mechanisms.

Full-target status: **OPEN**. Global continuity status: **OPEN**. No task state, cadence, quiet-delivery setting, email/push notification, permission, public-release setting, cross-account authentication, paid model/API/Codex call, or unrelated workflow was changed.
