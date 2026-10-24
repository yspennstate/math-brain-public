SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-24T04:17:43Z.
attacking: the fresh account03/B05 pair-star theorem leaves only longitudinal concentration in the heavy-null Witt branch; force all transverse rows uniformly diffuse, extract a quantitatively nondegenerate two-dimensional product bank, pay the exact planar defect endpoint, and test which weaker grouped-data interfaces are actually false.

# account02/B05 r11 — longitudinal-spike compiler, planar endpoint, and a grouped-data obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: quadratic coarea / complementary constructions and source-valid counterexamples  
Status: **PROVED SUPPORTING STRUCTURAL THEOREM + EXACT PLANAR ENDPOINT / PROVED INTERFACE COUNTEREXAMPLE / FULL QFORM OPEN**  
Continuity: separate; only essential boundedness is claimed in paid branches.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

Fresh owner control was resolved from `math-research-brain` main; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. I reread the live QFORM manifest/current research/claims/deltas/corrections/pathways/memory protocol, the proof-first and latest-Claude requests, this slot assignment, the required pinned `e5f71d79...` RESULTS/FOURIER_ROUTE_REPORT/COUNTEREXAMPLE_SEARCH, the prior account02/B05 memory snapshot, and the newest compatible account03/B05 r39 report.

The new account03/B05 theorem `QFORM-PAIR-ANCHORED-DETSTAR-COAREA-v1` changes the heavy-null obstruction materially: every literal pair carrying aggregate principal-triple star `T_I` has

`||p_Q||_(infinity,ess) <= C_star T_I^(-1/3),`

`C_star=24(3+sqrt(2))10^(2/3)=491.735145127...`,                       (1.1)

including an exactly singular physical pair.

The first unpaid implication after the reductions below is therefore

`QFORM-ORTHOGONAL-DEFECT-PUNCTURED-RECEIVER-v1`:

> in the exact-rank-three heavy-null near-coloop branch, after conditioning at most two literal longitudinal spikes, prove a rough interval bound for
>
> `Q=2aHV+2bVP+A V^2+2B VW+delta W^2+affine`,
>
> where `H` is a genuine independent cap-one original coordinate, `(P,V,W)` are three linear forms of one remaining original-coordinate product bank, the coefficient vector of `P` is orthogonal to those of `V,W`, the `(V,W)` coefficient Gram matrix is `>= (7/8)I_2`, and `b=a*kappa*eta` may tend to zero. The bound must be uniform through `b->0` and depend on the target curvature only through `a^2|delta|>=1/2`, without deleting `P`, taking a curved-fiber supremum, or replacing the product-projection law by an arbitrary joint law.

The exact `eta=0` endpoint is paid below. The new counterexample in Section 5 shows why the remaining same-bank linear-projection provenance is indispensable.

## 2. Starting heavy-null Witt geometry

Use the exact physical Witt normal form from account01/B05. A heavy literal original coordinate `H=X_i` has spectral leverage `c>1/2` and physical diagonal zero. After an orthogonal change only inside the three-dimensional spectral subspace,

`r_i=(sqrt(c),0,0)`

and the spectral matrix is

`M=[[0,beta,0],[beta,alpha,gamma],[0,gamma,delta]],`                   (2.1)

with `beta*delta !=0` and

`Delta_3=|det M|=beta^2|delta|>=1`.                                  (2.2)

Writing `tau=sqrt(1-c)` and normalizing the residual first coefficient column, the residual Parseval rows are

`g_j=(xi_j,y_j,z_j)`, `sum_j g_j g_j^T=I_3`.                         (2.3)

Set the residual linear projections

`U=sum xi_j X_j`, `V=sum y_j X_j`, `W=sum z_j X_j`.

Then

`Q=2aV(H+kappa U)+alpha V^2+2gamma VW+delta W^2`,                    (2.4)

up to arbitrary affine terms, where

`a=beta sqrt(c)`, `kappa=tau/sqrt(c)`,

and the exact determinant-star identity is

`boxed{ a^2|delta|=c Delta_3>=1/2. }`                                (2.5)

For every residual physical row let

`q_j=y_j^2+z_j^2`.                                                    (2.6)

The pair-star identity from account01/B05 is

`boxed{ T_(ij)=sum_(k notin {i,j}) |det A[{i,j,k}]|
              =c Delta_3 q_j. }`                                    (2.7)

## 3. Fresh partner r39 applied: force every transverse row below 1/16

Apply account03/B05 r39, not just as background but to the live inequality (2.7). If some residual row satisfies

`q_j>=1/16`,                                                         (3.1)

then target normalization and `c>1/2` give

`T_(ij)>=1/32`.                                                       (3.2)

Hence (1.1) yields the concrete full-output bound

`boxed{
 ||p_Q||_(infinity,ess)
 <= C_star 32^(1/3)
 =1561.161773328... <1561.162.
}`                                                                   (3.3)

Therefore every still-unpaid heavy-null exact-rank-three instance may be assumed to satisfy

`boxed{ q_j<1/16 for every residual original coordinate j. }`        (3.4)

This strengthens the predecessor's `q_j<1/4` longitudinal alternative from a statement about heavy residual rows to a uniform statement about **every** residual row.

## 4. Longitudinal-spike compiler and exact planar endpoint

Define the normalized residual-heavy set

`S={j: ||g_j||^2=xi_j^2+q_j>1/2}`.                                  (4.1)

Under (3.4), every `j in S` satisfies

`xi_j^2>1/2-1/16=7/16`.                                              (4.2)

Since `sum_j xi_j^2=1`, there are at most two such coordinates:

`boxed{ |S|<=2. }`                                                    (4.3)

Let `K=S^c`, and restrict the transverse coefficient vectors to K:

`v=(y_k)_(k in K)`, `w=(z_k)_(k in K)`.

Their coefficient Gram matrix is

`T_K=[[||v||^2,<v,w>],[<v,w>,||w||^2]]
    =I_2-sum_(j in S) (y_j,z_j)^T(y_j,z_j).`                         (4.4)

The deleted positive-semidefinite matrix has operator norm at most its trace, and by (3.4),(4.3) that trace is `<2/16=1/8`. Therefore

`boxed{ T_K > (7/8) I_2,  det T_K>(7/8)^2=49/64. }`                  (4.5)

The sharp two-dimensional product-projection bound from the pinned Fourier source now applies to the literal source bank K. Thus the pair

`(V_K,W_K)=(v.X_K,w.X_K)`

has an honest joint density cap

`boxed{ M_K <=2/sqrt(det T_K)<16/7. }`                               (4.6)

This remains true after conditioning the at-most-two literal spike coordinates in S, because K is source-disjoint from S.

Now restrict the normalized longitudinal coefficient vector to K,

`u=(xi_k)_(k in K)`,

and perform only a deterministic coefficient-space regression

`u=r v+s w+p`, `p perpendicular span{v,w}`.                           (4.7)

Put

`P=p.X_K`, `eta=||p||_2`.                                             (4.8)

After conditioning `X_S`, all conditioned contributions are affine shifts, and (2.4) becomes exactly

`boxed{
 Q=2aHV_K+2a kappa V_K P+A V_K^2+2B V_KW_K+delta W_K^2+affine.
}`                                                                   (4.9)

No independence is asserted among `P,V_K,W_K`; only `H independent X_K` is used.

### Theorem `QFORM-LONGSPIKE-PLANAR-ENDPOINT-v1`

If `eta=0`, equivalently `p=0`, then the full output density obeys

`boxed{ ||p_Q||_(infinity,ess)<16.970. }`                            (4.10)

Indeed `P=0` and `U_K=rV_K+sW_K`, so the shared term only changes the `V_K^2` and `V_KW_K` coefficients. The quadratic is therefore exactly in the scope of the proved account02/B05 theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1` with independent hub `aH`, pair-density cap `M_K<16/7`, and transverse square coefficient `delta`. That theorem gives

`||p_Q||_(infinity,ess)
 <= C_0 (16/(7|a|))^(2/3)|delta|^(-1/3)
 = C_0(16/7)^(2/3)(a^2|delta|)^(-1/3),`                              (4.11)

where `C_0=7.761982175235...`. Using (2.5),

`||p_Q||_(infinity,ess)
 <=C_0(16/7)^(2/3)2^(1/3)
 =16.9693002778...`,                                                  (4.12)

which proves (4.10).

Thus the longitudinal-spike survivor has been compressed to **one scalar coefficient-space defect `eta>0`**. The transverse product pair stays uniformly nondegenerate, and the exact defect-zero endpoint is uniformly paid.

There is also an exact bookkeeping identity useful for the next run. Let

`G_K=sum_(k in K) g_k g_k^T`.

Because (4.7) is a determinant-one shear of coefficient coordinates and `p` is orthogonal to `v,w`,

`boxed{ det G_K=eta^2 det T_K. }`                                    (4.13)

Hence `eta` is exactly the missing third coefficient-volume after the at-most-two longitudinal spikes are removed; it is not a heuristic size parameter.

## 5. A sharp grouped-data obstruction: pair cap + joint cap are not enough

The remaining receiver cannot forget that `P,V,W` are **linear projections of the same product bank**. Even extremely strong grouped density caps do not replace that provenance.

### Proposition `QFORM-PAIRCAP-DEPENDENT-CANCELLATION-v1`

For every `R>=2` there is a probability density `rho_R(p,v,w)<=1` such that

- the `(V,W)` joint density is at most `1/R<=1`;
- each one-dimensional coordinate marginal `P,V,W` has density at most one;
- if `H` is independent uniform on `[0,1]`, then

`Q_R=2HV+2VP+W^2`                                                     (5.1)

has a density satisfying

`boxed{ p_(Q_R)(1/R) >= (1/2) log(2R-1). }`                          (5.2)

In particular no universal density receiver for (4.9) can depend only on an independent cap-one hub, an ambient joint cap for `(P,V,W)`, and a two-dimensional `(V,W)` marginal cap.

#### Construction and proof

Let

`E_R={0<v<1, 0<w<R,
      |p+w^2/(2v)|<1/(2R)}`                                          (5.3)

and set

`rho_R=1_(E_R)`.                                                      (5.4)

For each `(v,w)` the p-fiber has length `1/R`, so `|E_R|=1` and `rho_R` is a probability density with cap one. Its `(V,W)` marginal is exactly `(1/R)1_((0,1)x(0,R))`.

The V-marginal is the uniform density on `(0,1)` and the W-marginal is `R^(-1)1_(0,R)`. For P, fix p. The allowed interval for

`x=w^2/(2v)`

has length at most `1/R`. Since `w=sqrt(2vx)`, its w-preimage has length at most

`sqrt(2v/R)`.                                                        (5.5)

Therefore

`f_P(p)<=int_0^1 sqrt(2v/R) dv=(2/3)sqrt(2/R)<=2/3<1.`               (5.6)

Now make the nonlinear change of variable

`U=P+W^2/(2V)`.                                                       (5.7)

Its Jacobian in P is one, and `(U,V,W)` has constant density one on the box

`|U|<1/(2R), 0<V<1, 0<W<R`.                                         (5.8)

Hence U and V are independent, with U uniform on `[-1/(2R),1/(2R)]`, while H is independently uniform on `[0,1]`. Equation (5.1) becomes

`Q_R=2V(H+U)`.                                                        (5.9)

Let `Z=H+U`. Its density is identically one on

`[1/(2R),1-1/(2R)]`.                                                 (5.10)

For `q=1/R`, the product-density formula gives

`p_(Q_R)(q)
 =int_0^1 (1/(2v)) f_Z(q/(2v)) dv`
` >= (1/2) int_(1/(2R-1))^1 dv/v`
` = (1/2) log(2R-1),`                                                 (5.11)

which proves (5.2).

This is **not a QFORM counterexample**: P in (5.3) is nonlinearly coupled to `(V,W)` and is not asserted to be a linear product projection. Its role is to rule out an invalid proof interface. The exact cancellation `2VP+W^2=2VU` shows why replacing the remaining same-bank linear-projection structure by an arbitrary joint density—even one with cap one and with a very small `(V,W)` marginal cap—would lose the target theorem.

## 6. Required pinned `e5f71d79...` package applied to the live obstruction

The required source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, was reread through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` on the current compatible descendant.

Two completed results are applied to actual branches.

First, Theorem F says an exact-rank-three spectral frame with every original-coordinate leverage at most `1/2` has

`boxed{ ||p_Q||_infinity<=12 Delta_3^(-1/3)<=12. }`                  (6.1)

Thus the entire analysis above is needed only because the literal heavy null row has leverage `c>1/2`; the diffuse target branch is already paid.

Second, on signature `(2,1)`, the completed ruled theorem gives

`boxed{ p_Q(s)<=pi sqrt(2), s>=0 }`                                  (6.2)

in its normalized one-sheet convention. Hence the punctured receiver in Section 1 is genuinely aimed at the complementary convex/two-sheet side (and the definite signature), not at the already-controlled ruling.

The pinned counterexample search still supplies no target-valid counterexample.

## 7. What changed and what remains

The fresh pair-star theorem lets one choose a deliberately small threshold before entering the longitudinal branch. At threshold `1/16` the still-unpaid geometry is much more rigid than the predecessor state:

- every residual transverse row has `q_j<1/16`;
- there are at most **two**, not three, normalized longitudinal-heavy rows;
- after conditioning them, the surviving transverse coefficient Gram is `>(7/8)I_2`;
- the actual `(V,W)` product-projection pair has joint density cap `<16/7`;
- the only coefficient direction outside that robust transverse plane is the exact orthogonal regression defect `p`, with `det G_K=||p||^2 det T_K`;
- the endpoint `p=0` has full-line essential density `<16.970`.

The obstruction is therefore no longer a generic aggregate determinant star or an arbitrary three-dimensional joint coarea problem. It is a **punctured linear-product-projection defect**: `eta=||p||>0` can be arbitrarily small while `P=p.X_K` has unbounded support, so it cannot be deleted as a small random error. Section 5 proves that forgetting the linear product provenance is genuinely fatal.

The next source-valid route should keep the orthogonality `p perpendicular v,w` inside a coarea/Fourier/decoupling argument and obtain a bound continuous through `kappa*eta=0`; any argument using only grouped joint-density caps is ruled out by (5.2).

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**.

## 8. Source pins

- Fresh owner/control source at run start: `math-research-brain@c05e34d9e65883f9e6fb22159e9dbce3f6aea9d3`, OWNER CONTROL revision `2026-09-22.15`.
- Required pinned compatible source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`; current compatible descendant at source read: `47deae65829b8cae5282751e32d7aa0fb07c51c9`.
- Fresh partner: account03/B05 r39, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260924T033744Z-account03-B05-QFORM-r39/REPORT.md` at descendant `47deae65829b8cae5282751e32d7aa0fb07c51c9`.
- Structural Witt source: account01/B05 `20260924T015848Z-account01-B05-QFORM-auto11/REPORT.md` and `STRUCTURAL_ADDENDUM.md`.
- Predecessor account02/B05 memory: canonical math `4ad9d206dba1b22fd917280717c24f4e1dd6ea09`.

Independent review of the new reduction, endpoint, and interface counterexample is **PENDING**.
