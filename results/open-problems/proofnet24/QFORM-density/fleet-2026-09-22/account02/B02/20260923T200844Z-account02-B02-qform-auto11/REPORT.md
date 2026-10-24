SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-23T20:08:44Z.

# account02/B02 auto11 — zero-pivot rank-one shared-hub tensor Fourier receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T200844Z-account02-B02-qform-auto11`  
Role: Integrated Fourier estimate / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER L1 OPEN-NOT-REFUTED**

The exact owner target remains unchanged: independent ORIGINAL real coordinates with one-dimensional densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, support, log-concavity, iid, diagonal-basis, or post-rotation-independence hypothesis is introduced. Continuity is claimed only where an actual unweighted `L1_t` characteristic-function estimate is proved.

## 1. Fresh controls and source pins actually used

Fresh `math-research-brain/main` was resolved at invocation start and refreshed before publication. Owner control remains revision `2026-09-22.15`, QFORM-only, with the exclusive continuation request `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` active and no later stop/reassignment observed.

Required source package read at the owner-pinned commit:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Reviewed sharp Hausdorff--Young `q`-dependent source:

- `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Newest designated partner consumed at equation level:

- account03/B02 r38, `QFORM-V1-ZEROPIVOT-SHAREDHUB-E2-L1-v1`, report commit `98980f99df26af2b9193f70aabbdcd7316ab5aa1`, checker state through `343750e0bd888523ca52f424f46de7a25d070930`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T194347Z-account03-B02-qform-r38/REPORT.md`.

Other current sources used:

- grouped projection / exact-rank crossing source `yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`, `NEW_PROJECTED_CROSSING.md`;
- account03/B04 r40 sharp critical `E2` and pivoted `C1` receiver, `yspennstate/math-open-problems@8192c4990fff2ba5dee1ce62fdf92e815b5b89c1`;
- current Fisher-information continuation `yspennstate/math-open-problems@4a65677d185d35154dc3dfae320c5df9f939b8a2`, `FISHER_INFORMATION.md`;
- preceding account02/B02 overlap-compound report `yspennstate/math-open-problems@edbef27e79cf6725a25aad1f9bbcd1e3eaf61583`.

The live corrections are respected: no law-uniform scalar pointwise Fresnel decay, no post-rotation or post-Schur independence, no arbitrary-joint coarea cap, no worst conditional-density supremum, no selection of one dimension-degrading minor from aggregate mass, and no deletion of a small nonzero coefficient tail on unbounded product inputs.

## 2. Required independent Fisher analytic review: PASS on assigned scope

The current owner handoff requests account02/B02 to check the weak integration by parts, cutoff limits, inverse-distance estimate, and density-domination normalization in `FISHER_INFORMATION.md`. I re-read the source in this invocation and independently obtain the same verdict as the immediately preceding B02 run: **PASS on that analytic scope**.

In brief, `sqrt(f_i) in H1` gives `f_i in W^{1,1}`, score identities `E S_i=0`, `E S_i^2=I_i`, and `E|U^T S|^2=J_E`. For

`W_delta=Uz/(|z|^2+delta)`

one has

`div W_delta >= (r-2)/(|z|^2+delta)`.

A compact cutoff removes the boundary term for fixed `delta` without a moment assumption, and Cauchy--Schwarz gives

`E|z|^(-2) <= J_E/(r-2)^2`.

For

`V_delta=U Lambda^(-1)z/[2(|z|^2+delta)]`,

the chosen center makes

`grad Q . V_delta = |z|^2/(|z|^2+delta)`

exactly. The divergence and score terms are dominated by the inverse-distance estimate. With the centered primitive `Phi` of a nonnegative test function of mass `m`, `||Phi||_infinity<=m/2`; together with the explicit `1/2` in `V_delta`, this gives the source's factor `1/4` in

`E psi(Q) <= m [rD+sqrt(J_E D)]/(4s)`.

Thus the density-domination conclusion is valid under the extra Fisher/H1 hypothesis. This does **not** close the rough cap-one target and is not used below to regularize arbitrary inputs.

## 3. Where D', D5, and the sharp-HY receiver stop on the live endpoint

For any literal original-coordinate cross block `M` with `Z=E3(M)>0`, the reviewed sharp-HY theorem gives, for `1<=q<3/2` and third-volume row marginals `alpha_i<=q/2`,

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`.             (3.1)

The completed B02 heavy-row cascade combines this at the rational threshold `q=9/8` with the complementary heavy-row theorem to give the marginal-free live-block estimate

`||p_Q||_infinity <=10.345084 E3(M)^(-1/6)`,                     (3.2)

with `phi_Q in L1`. The reviewed sharp-HY fifth-volume exit remains

`||p_Q||_infinity <=(5e/sqrt(2)) E5(M)^(-1/10)`.                 (3.3)

These continue to pay the disjoint-compound branch and every physical block carrying quantitative third/fifth volume.

The zero-pivot rank-one endpoint attacked here is a **real obstruction to those two receivers**. In the notation below, if the residual crossing `N` has rank one, then both natural hub-plus-bank physical cross matrices

`[r^T; N]` and `[c^T; N^T]`

have rank at most two. Hence their `E3` and `E5` vanish identically. There is no D'/D5 currency to spend on this literal endpoint. The new theorem below gains the missing half power from the shared physical hub without duplicating it into independent row and column variables.

## 4. A grouped three-bank tensor lemma

### Lemma 4.1 — `QFORM-SHAREDHUB-2x2-TENSOR-L1-v1`

Let `H`, `Y=(Y1,Y2)`, and `Z=(Z1,Z2)` be three independent banks. Assume `H` has a scalar density at most one and `Y,Z` have joint densities bounded by `M_Y,M_Z`. Let `F_H,F_Y,F_Z` be arbitrary measurable real phases. For nonzero real `alpha,beta,sigma`, put

`Q0=F_H(H)+F_Y(Y)+F_Z(Z)
    +2H(alpha Y1+beta Z1)+2 sigma Y2 Z2`.                         (4.1)

Then

`boxed:
 |phi_Q0(t)|
 <=min{1,
   pi^(3/2) sqrt(M_Y M_Z)
   |alpha beta sigma|^(-1/2)|t|^(-3/2)}.}`                        (4.2)

Consequently, with `T=(alpha beta sigma)^2`,

`boxed:
 int_R |phi_Q0(t)|dt
 <=6 pi (M_Y M_Z)^(1/3) T^(-1/6),}`                              (4.3)

and

`boxed:
 ||p_Q0||_infinity
 <=3 (M_Y M_Z)^(1/3) T^(-1/6).}`                                 (4.4)

The density is continuous and vanishes at infinity.

### Proof

Push the phase-twisted measures in the three independent banks to the displayed coordinates. Write `g_t(h)`, `a_t(y)`, `b_t(z)` for their complex densities. Then

`|g_t(h)|<=f_H(h)<=1`,
`||a_t||_2^2<=M_Y`, `||b_t||_2^2<=M_Z`.                           (4.5)

Set

`k_t(s)=int g_t(h) exp(i2t h s)dh`.

After integrating `H`, the remaining bilinear kernel on `L2(R^2)` factors as

`K_t(y,z)
 =k_t(alpha y1+beta z1) exp(i2t sigma y2 z2)
 =K_{1,t}(y1,z1)K_{2,t}(y2,z2)`.                                 (4.6)

For

`(T1 f)(y)=int k_t(alpha y+beta z)f(z)dz`,

angular Fourier transform gives

`hat(T1 f)(xi)
 =|alpha|^(-1) hat(k_t)(xi/alpha)
   hat(f)(-beta xi/alpha)`

up to an irrelevant reflection convention. Hence Plancherel yields

`||T1||_{2->2}
 <=|alpha beta|^(-1/2)||hat(k_t)||_infinity`.                     (4.7)

Since `k_t(s)=hat(g_t)(2ts)`, Fourier inversion on this one-dimensional scaling gives

`hat(k_t)(xi)=(pi/|t|)g_t(-xi/(2t))`,

so

`||T1||_{2->2}
 <=pi |t|^(-1)|alpha beta|^(-1/2)`.                              (4.8)

For

`(T2 f)(y)=int exp(i2t sigma yz)f(z)dz`,

Plancherel and the change `xi=2t sigma y` give exactly

`||T2||_{2->2}=(pi/(|t sigma|))^(1/2)`.                          (4.9)

The tensor-product operator therefore has norm at most the product of (4.8) and (4.9). Pair with `a_t,b_t` and use (4.5) to obtain (4.2).

If `K=pi^(3/2)sqrt(M_YM_Z)T^(-1/4)`, then

`int_R min(1,K|t|^(-3/2))dt=6K^(2/3)`.

This is (4.3); division by `2pi` gives (4.4). QED.

The proof uses no independence inside `Y` or inside `Z`. It requires only their joint density caps and their independence as the two original-coordinate banks. This is exactly why deterministic rotations/shears inside a bank are harmless analytically without ever being declared new independent random coordinates.

## 5. Literal original-coordinate rank-one reduction

Fix one physical shared coordinate `i` and a literal residual cut `K=L disjoint_union R`. Write

`a=A_ii`, `c=A[L,i]`, `r=A[i,R]`, `N=A[L,R]`.                     (5.1)

Assume

`a=0`, `rank(N)=1`,

and the partner overlap packet on this cut is positive. Put

`u=||c||^2`, `w=||r||^2`,
`P_c=I-cc^T/u`, `P_r=I-rr^T/w`,
`C=P_c N P_r`.                                                    (5.2)

Partner r38 proves at the exact zero-pivot endpoint that positivity of its packet is equivalent here to

`T:=u w ||C||_F^2>0`.                                             (5.3)

Let

`e=c/sqrt(u)`, `f=r/sqrt(w)`.

Because `N` has rank one and `C!=0`, choose unit vectors `v perpendicular e`, `z perpendicular f` so that the column/row directions of `N` lie in `span{e,v}` and `span{f,z}`. In these orthonormal two-dimensional coordinates the entire rank-one crossing is represented by

`B=[[d,q],[p,sigma]]`,                                             (5.4)

with

`sigma=v^T N z !=0`, `det B=0`,
`|sigma|=||C||_F`.                                                 (5.5)

Use the determinant-one shears

`Y1'=Y1`, `Y2'=Y2+(q/sigma)Y1`,
`Z1'=Z1`, `Z2'=Z2+(p/sigma)Z1`.                                  (5.6)

They preserve Lebesgue measure and leave the two hub-star coordinates `Y1,Z1` unchanged. Since `det B=0`, direct substitution gives the exact crossing identity

`Y^T B Z = sigma Y2' Z2'`.                                       (5.7)

No small coefficient is dropped. The within-`L` and within-`R` quadratic terms merely become arbitrary new functions of their respective banks.

The original independent cap-one coordinates in `L` have a two-dimensional orthonormal projection density bounded by `2`; the same holds in `R`. The determinant-one shears (5.6) preserve these caps. After conditioning all coordinates outside `{i} union L union R`, arbitrary outside couplings become affine terms and are absorbed in the three within-bank phases. Thus Lemma 4.1 applies with

`M_Y,M_Z<=2`,
`alpha=sqrt(u)`, `beta=sqrt(w)`,
`T=(alpha beta sigma)^2=u w ||C||_F^2`.                           (5.8)

### Theorem 5.1 — `QFORM-ZEROPIVOT-RANKONE-CROSS-TENSOR-L1-v1`

Under (5.1)-(5.3) with `a=0` and `rank(N)=1`, the full ambient quadratic form has a continuous `C0` density and

`boxed:
 |phi_Q(t)|
 <=min{1,2 pi^(3/2)T^(-1/4)|t|^(-3/2)},}`                       (5.9)

`boxed:
 int_R |phi_Q(t)|dt
 <=6 pi 2^(2/3)T^(-1/6),}`                                      (5.10)

`boxed:
 ||p_Q||_infinity
 <=3*2^(2/3)T^(-1/6)
 =4.762203155904598... T^(-1/6).}`                               (5.11)

Arbitrary same-bank curvature, all conditioned outside couplings, and all affine terms are retained.

## 6. Designated account03/B02 result applied to an actual inequality

For the same zero-pivot shared coordinate `i`, define the partner's anchored overlap-one mass

`Delta_i
 =sum_{P cap Q=emptyset, |P|=|Q|=2}
   det A[{i} union P,{i} union Q]^2`.                             (6.1)

Partner r38 proves that a fair residual physical cut has mean `Delta_i/16`, so one actual cut satisfies

`D_i(L,R)>=Delta_i/16`,                                           (6.2)

and at `A_ii=0` its exact shared-hub identity is

`D_i(L,R)
 =||c||^2||r||^2||P_cNP_r||_F^2=T`.                              (6.3)

If the maximizing cut from (6.2) has `rank N=1`, Theorem 5.1 therefore gives the new live inequality

`boxed:
 ||p_Q||_infinity
 <=3*2^(4/3) Delta_i^(-1/6)
 =7.559526299369238... Delta_i^(-1/6),}`                          (6.4)

and

`boxed:
 int_R |phi_Q(t)|dt
 <=6 pi 2^(4/3) Delta_i^(-1/6)
 =47.49790457343447... Delta_i^(-1/6).}`                          (6.5)

This directly fills the **exact rank-one residual-crossing endpoint** where the partner's stable-rank factor `gamma(rho)=(rho-1)/(2rho)` vanishes. It also has no two-star dominance ratio `b` gate: even if both star arms are arbitrarily larger than the transverse scale, the tensor estimate spends their product exactly through `T`.

There is no contradiction with the partner's theorem. The two estimates cover complementary geometries:

- `sr(P_cNP_r)>1`: r38 promotes transverse second volume to a one-hub `E2` resource;
- `rank N=1`: the present theorem keeps the exact rank-one crossing and takes the missing Fourier half-power from the same physical hub.

The remaining difficult collar is genuinely a **nonzero rank-two-or-higher tail near a rank-one transverse crossing**, not the exact rank-one endpoint.

## 7. Relation to the current global `C1` overlap frontier

The preceding account02/B02 report proves the exact global decomposition

`e3(A^2)=V0+V1+V2+V3>=1`

and pays `V0>=1/4` through a random physical cut plus the marginal-free `E3` theorem, with D5 as a sharper complementary exit whenever its fifth-volume threshold is met. It also proves `V1=sum_i Delta_i`.

The current account03/B04 r40 result pays an aggregate **nonzero-pivot** `C1` packet via a scalar square plus the sharp critical `E2` collision estimate. The present theorem is complementary: it pays an exact **zero-pivot** anchored packet whenever the partner cut's entire residual crossing is rank one, and it supplies actual Fourier `L1` and continuity on that branch.

Thus an unpaid `V1/C1` state is narrower than before. Besides global spreading of `Delta_i`, a zero-pivot heavy slice can survive both r38 and this report only if the selected residual crossing retains a nonzero rank-two-or-higher tail while its transverse second-volume currency is too weak, or if it lies in the partner's two-star-dominated/near-rank-one collar with that nonzero tail. The tail cannot be deleted: arbitrary rough cap-one laws provide no perturbative moment control.

## 8. Deterministic algebra check

A deterministic-seed check (`seed=20260923`) generated 1,000 random rectangular rank-one matrices `N` with random nonparallel star directions `c,r`. In the normalized bases of Section 5 it verified:

- `det B=0` to maximum absolute floating discrepancy `4.37e-14`;
- the post-shear residual `d-qp/sigma=0` to maximum discrepancy `2.73e-15`;
- `u w ||P_cNP_r||_F^2=u w sigma^2` to maximum relative discrepancy `6.22e-14`.

This is diagnostic only; the proof is the exact rank-one factorization and determinant-one shear above.

## 9. Status and next exact implication

No target-valid QFORM counterexample was found, and the required Claude search source likewise reports none. No exact-target counterexample to a universal unweighted Fourier-`L1` criterion was found in this invocation. The full conjecture, full-target continuity, and target-wide uniform Fourier-`L1` bound therefore remain **OPEN**.

The first B02 implication is now

`QFORM-ZEROPIVOT-NEARRANK1-NONZERO-TAIL-L1-v1`:

> Start from the partner identity `T=||c||^2||r||^2||P_cNP_r||_F^2` on a heavy zero-pivot `V1` slice after the exact-rank-one residual crossing has been paid. Retain a genuinely nonzero rank-two-or-higher residual tail and prove a product-preserving integrated-Fourier receiver that stays uniform as that tail tends to zero, or route it quantitatively to the row-marginal-free `E2`, D', D5, kernel-curvature, or pivoted-overlap mechanisms. Do not delete the tail, duplicate the shared hub, or infer post-shear independence.

A separate global proof-assembly debt remains for the `V2` and `V3` compound strata and for aggregate spreading among many overlap anchors.

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token and pure-thinking-time telemetry: `null / NOT_EXPOSED`. Execution context for this run is `VERIFIED_BRAIN` in the programme's narrow protocol sense: authenticated repository retrieval plus actual receiver-memory use occurred; `full_brain_connected=false`, so no native learned-memory ingestion is claimed. Elapsed pure-thinking time is not exposed and is not inferred from wall time.