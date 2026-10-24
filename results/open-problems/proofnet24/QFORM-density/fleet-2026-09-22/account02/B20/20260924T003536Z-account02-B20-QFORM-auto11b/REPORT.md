SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-24T00:35:36Z.
attacking: the fresh account03/B20 r42 localized overlap-one endpoint, specifically its E2>4/9 branch, by decomposing the exact-rank-two anchored third volume into four invariant currencies and paying every quantitatively transverse side by a new source-valid Fourier receiver.

# account02/B20 — exact-rank-two anchored four-currency compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: proof closure and keeper / SYNTHESIS  
Status: **NEW SUPPORTING THEOREM + NEW FULL-LAW PAYMENT + SHARPER LIVE COLLAR / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: proved for the new transverse payment below; full-target continuity remains open.

## 1. Source boundary and live interface

The exact target is unchanged: for every finite n, independent real original-coordinate variables with probability densities `0<=f_i<=1`, and every real symmetric A with at least three eigenvalues of absolute value at least one, prove that `X^T A X` has a density whose essential supremum is bounded by one universal finite constant, or give a valid counterexample.

No Gaussianity, log-concavity, moments, bounded/connected support, iid hypothesis, diagonal-basis independence, or post-rotation independence is introduced. Coefficient-space orthogonal changes below are used only to state deterministic singular-vector identities. Every probabilistic smoothing step is applied to literal independent source banks and uses only marginal density bounds for their linear projections.

Fresh owner control at this invocation remained OWNER CONTROL revision `2026-09-22.15`, QFORM-only, with no account02/B20 stop. The same-hour canonical account02/B20 login already existed and was preserved rather than overwritten. The current account-local native inventory contained the same twenty B01--B20 QFORM tasks, enabled/hourly and quiet; no scheduler mutation, re-enable, duplicate creation, or B19 fallback was needed.

The newest compatible completed designated partner is account03/B20 r42,

`yspennstate/math-open-problems@eb50a2dc3acc7884f284a1f94847106c89bf5889`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T234606Z-account03-B20-QFORM-r42/REPORT.md`.

Its third-compound operator funnel proves that, after its already-paid macroscopic diagonal, principal-triple, and disjoint-E3 exits, every unpaid target state has all physical diagonals `<1/64` in magnitude and either a localized physical pair `J_2(S)>=1/144`, or a localized physical anchor j. In the one-anchor branch it produces disjoint literal banks R,C and the exact anchored block

`M = [[b,r^T],[c,N]] = A[{j} union R,{j} union C]`                (1.1)

with

`J_sep >= 1/2304`,                                                 (1.2)

and, by the corrected account04/B20 anchored-volume inequality,

`E_2(N)>4/9`                                                        (1.3)

or

`||r||_2 ||c||_2 ||N||_F >=1/96`.                                (1.4)

This run consumes (1.2) and directly attacks the exact-rank-two part of (1.3).

Two fresh peer reductions are also compatible and retained rather than duplicated. account03/B03 r43 pays the exact-rank-one one-anchor endpoint by its three-group triangle theorem, with `<17.307` at (1.2). account03/B19 r45 reduces the overlap-two weak-pair branch to the same E2 currency, a two-star packet, or a giant near-rank-one crossing. Thus exact/near rank two is a genuine current common interface.

## 2. Exact rank-two anchored third-volume identity

Assume for this section that `rank N=2`. Write an SVD as deterministic coefficient geometry,

`N=s_1 u_1 v_1^T+s_2 u_2 v_2^T`,   `s_1>=s_2>0`.                 (2.1)

Decompose the physical star vectors into singular-plane and orthogonal parts,

`c=a_1u_1+a_2u_2+c_perp`,
`r=d_1v_1+d_2v_2+r_perp`,                                         (2.2)

where `c_perp` is perpendicular to `span(u_1,u_2)` and `r_perp` is perpendicular to `span(v_1,v_2)`. Put

`q=b-d_1a_1/s_1-d_2a_2/s_2`.                                     (2.3)

### Theorem 2.1 — `QFORM-R42-RANK2-ANCHORED-FOURCURRENCY-v1`

The complete anchored third-volume is exactly

`boxed:
J_sep
 = (s_1s_2 q)^2
 + ||c_perp||^2[(s_1d_2)^2+(s_2d_1)^2]
 + ||r_perp||^2[(s_1a_2)^2+(s_2a_1)^2]
 + ||c_perp||^2||r_perp||^2(s_1^2+s_2^2).`                       (2.4)

In particular, under the designated-partner scale (1.2), at least one of

`T_0:=|s_1s_2q|`,                                                  (2.5)
`T_c:=||c_perp|| sqrt((s_1d_2)^2+(s_2d_1)^2)`,                    (2.6)
`T_r:=||r_perp|| sqrt((s_1a_2)^2+(s_2a_1)^2)`,                    (2.7)
`T_cr:=||c_perp||||r_perp|| sqrt(s_1^2+s_2^2)`                    (2.8)

is at least `1/96`.

### Proof

For `x,y` on the C-side, consider the component containing the shared physical anchor in the exterior image of the bordered block (1.1). Identifying that output component with `wedge^2 R`, it is

`T(x wedge y)
 = b Nx wedge Ny
   -(r.x)c wedge Ny
   +(r.y)c wedge Nx`.                                             (2.9)

Cauchy--Binet gives

`J_sep=||T||_HS^2`.                                                (2.10)

Use the orthonormal input basis consisting of `v_1 wedge v_2`, `v_1 wedge w`, `v_2 wedge w` for an orthonormal basis w of `ker N`, and null-null pairs. On the first input,

`T(v_1 wedge v_2)
 = s_1s_2 q u_1 wedge u_2
   + c_perp wedge (d_2s_1u_1-d_1s_2u_2)`.                         (2.11)

The two displayed summands are orthogonal, so its squared norm is

`(s_1s_2q)^2+||c_perp||^2[(s_1d_2)^2+(s_2d_1)^2]`.                (2.12)

For `w in ker N`,

`T(v_1 wedge w)=s_1(r_perp.w)c wedge u_1`,
`T(v_2 wedge w)=s_2(r_perp.w)c wedge u_2`.                         (2.13)

Summing their squared norms over w gives

`||r_perp||^2[s_1^2(a_2^2+||c_perp||^2)
              +s_2^2(a_1^2+||c_perp||^2)]`,                      (2.14)

which splits into the last two terms of (2.4). Null-null inputs vanish. This proves (2.4). Since four nonnegative squares sum to at least `1/2304=(1/48)^2`, one square-root is at least `(1/48)/2=1/96`. QED.

This is sharper than the generic anchored inequality in this rank-two chamber and, importantly, does not select one physical tiny minor.

## 3. New source-valid one-transverse Fourier receiver

The next theorem pays a substantial part of the four-currency interface while keeping arbitrary same-bank curvature.

### Theorem 3.1 — `QFORM-RANK2-CROSS-ONE-TRANSVERSE-HUB-v1`

Let Z be a scalar random variable of density at most `M_0`, independent of two source banks `X_R,X_C`. Let

`Y=(Y_1,Y_2,Y_3)` be a linear projection of `X_R` with joint density at most `M_R`, and
`W=(W_1,W_2)` a linear projection of `X_C` with joint density at most `M_C`.

Let `F_0,F_R,F_C` be arbitrary finite measurable real functions of their respective independent source groups. For nonzero `s_1,s_2,alpha`, and arbitrary real `gamma_1,gamma_2,delta_1,delta_2`, set

`Q = F_0(Z)+F_R(X_R)+F_C(X_C)
   +2(s_1Y_1W_1+s_2Y_2W_2)
   +2Z(gamma_1Y_1+gamma_2Y_2+alpha Y_3
       +delta_1W_1+delta_2W_2).`                                  (3.1)

Then

`|phi_Q(t)|
 <= min{1,
         pi^(3/2)(M_0M_RM_C)^(1/2)
         |s_1s_2alpha|^(-1/2)|t|^(-3/2)}`                         (3.2)

for nonzero t, and Q has a continuous `C_0` density with

`boxed:
||p_Q||_infinity
 <=3(M_0M_RM_C)^(1/3)|s_1s_2alpha|^(-1/3).}`                     (3.3)

The completely symmetric statement holds with the transverse coordinate on the C bank instead.

### Proof

Push the complex measure `exp(itF_R)dP_R` onto Y; call its density `b_t(y)`. Then `|b_t|<=p_Y`, so `int|b_t|^2<=M_R`. Similarly the pushed C-bank density `c_t(w)` has `int|c_t|^2<=M_C`, and the pushed Z density has modulus at most `p_Z<=M_0`.

Partially Fourier transform only the transverse R coordinate,

`B_t(y_1,y_2,xi)=int b_t(y_1,y_2,y_3)e^(i xi y_3)dy_3`,
`G_R(xi)=int_R2 |B_t(y_1,y_2,xi)|^2dy_1dy_2`.                    (3.4)

Plancherel gives

`int G_R(xi)dxi=2pi int|b_t|^2<=2pi M_R`.                         (3.5)

For fixed z, the z-linear terms in `(Y_1,Y_2)` and W are merely unitary modulations. The two-dimensional bilinear Fourier operator with kernel

`exp(i2t(s_1y_1w_1+s_2y_2w_2))`

has exact `L^2 -> L^2` norm

`pi/(|t| sqrt(|s_1s_2|))`.                                       (3.6)

Consequently the conditional oscillatory integral is bounded by

`pi/(|t|sqrt(|s_1s_2|))
 * G_R(2t alpha z)^(1/2) M_C^(1/2)`.                              (3.7)

Integrate z. Cauchy--Schwarz with respect to the probability measure `p_Z(z)dz` and (3.5) give

`int p_Z(z)G_R(2t alpha z)^(1/2)dz
 <= [pi M_0 M_R/(|t alpha|)]^(1/2)`.                              (3.8)

Equations (3.7)--(3.8) prove (3.2). Finally

`int_R min(1,K|t|^(-3/2))dt = 6K^(2/3)`,                          (3.9)

and Fourier inversion gives `(2pi)^(-1)*6K^(2/3)`, which is exactly (3.3). QED.

The argument proves an averaged Fourier estimate, not any false law-uniform pointwise decay for a one-dimensional quadratic phase.

## 4. Application to the designated-partner exact-rank-two E2 branch

Return to (1.1)--(1.3) with `rank N=2`. The three R-side projections `(u_1^TX_R,u_2^TX_R,c_perp^TX_R/||c_perp||)` are an orthonormal three-dimensional projection whenever `c_perp!=0`; their joint density is at most `2^(3/2)` by the sharp product-marginal theorem. The two C-side singular projections have density at most `2`. The source groups `X_j,X_R,X_C` are genuinely independent.

Therefore Theorem 3.1 gives the full-law payment

`boxed:
 s_1s_2||c_perp|| >=1/96
 => ||p_Q||_infinity
    <=3*2^(5/6)*96^(1/3)
    <24.476.}`                                                    (4.1)

The symmetric argument gives the same bound when

`s_1s_2||r_perp|| >=1/96`.                                       (4.2)

Every same-bank quadratic term on R and C is absorbed into `F_R,F_C`; the anchor square and affine anchor terms are absorbed into `F_0`. No tail is deleted.

Thus in every unpaid exact-rank-two E2 state we may assume

`alpha:=||c_perp|| <1/(96p)`,
`beta :=||r_perp|| <1/(96p)`,
`p:=s_1s_2 >2/3`,                                                 (4.3)

where the last inequality is exactly (1.3).

Combine (4.3) with the four-currency dichotomy of Theorem 2.1. At least one of the following sharply scoped residuals holds:

1. **Schur currency:**
   `|q| >=1/(96p)`.                                                (4.4)

2. **C-transverse / internal-R-star currency:**
   either `|d_2|>s_2/sqrt(2)` or `|d_1|>s_1/sqrt(2)`.              (4.5)

   Indeed `T_c>=1/96` and `alpha<1/(96p)` imply
   `sqrt((s_1d_2)^2+(s_2d_1)^2)>p`.

3. **R-transverse / internal-C-star currency:**
   either `|a_2|>s_2/sqrt(2)` or `|a_1|>s_1/sqrt(2)`.              (4.6)

4. **Extreme-condition-number collar:**
   `s_2<sqrt(2)/64=0.0220971...` and
   `s_1/s_2>4096/3=1365.333...`.                                  (4.7)

   For if `T_cr>=1/96`, then (4.3) yields
   `sqrt(s_1^2+s_2^2)>96p^2`. Since the left side is at most `sqrt(2)s_1=sqrt(2)p/s_2`, we get `s_2<sqrt(2)/(96p)<sqrt(2)/64`; hence `s_1/s_2=p/s_2^2>4096/3`.

This is a genuine shrinkage of the live E2 debt: a generic exact-rank-two anchored packet is now paid; an unpaid one must carry a quantitative Schur/internal-star degeneracy or be extremely ill-conditioned.

## 5. Pinned interactive theorem applied at an actual cut

The required pinned source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was re-read at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. In particular the proved unrestricted fifth-volume theorem D_5 says that for any literal disjoint physical crossing block B,

`||p_Q||_infinity <=5 sqrt(2e) e_5(B^TB)^(-1/10)`,                (5.1)

with no row-marginal gate.

Apply it to the actual literal R|C block N in (1.1). If

`e_5(N^TN)>=1/1024`,                                               (5.2)

then the entire ambient quadratic law is paid by

`boxed: ||p_Q||_infinity <=10 sqrt(2e)<23.317.}`                  (5.3)

Thus every state reaching the low-rank analysis above may additionally be assumed to have `e_5(N^TN)<1/1024`; in the exact-rank-two chamber it vanishes identically. This is an actual full-law use of the pinned theorem, not a heuristic volume comparison.

The pinned counterexample search still reports no valid counterexample to the full target; its tested maxima remain bounded. No numerical evidence is used as proof here.

## 6. Target-valid stress family showing the Schur currency is genuine

The four-currency theorem cannot be simplified by forcing a transverse star. Let m be a sufficiently large power of two, choose two orthonormal Walsh columns on R and two on C, and let

`N_L=L(u_1v_1^T+u_2v_2^T)`,                                      (6.1)

with `L>=3`. Put `c=r=0` and

`b_L=1/(48L^2)`.                                                   (6.2)

Take the symmetric full matrix on `j union R union C` with j-j entry `b_L`, R-C block `N_L`, and all other same-bank and anchor-star coefficients zero. Its nonzero spectrum is

`{L,L,-L,-L,b_L}`,                                                 (6.3)

so it lies in the exact target class. Choosing `m>128L` makes every physical R-C entry `<1/64`, and `b_L<1/64`.

For the literal anchored split,

`E_2(N_L)=L^4`,
`J_sep=b_L^2 E_2(N_L)=1/2304`,                                    (6.4)

while

`c_perp=r_perp=0`.                                                 (6.5)

Hence all three transverse currencies vanish and the entire anchored volume is exactly

`T_0=L^2 b_L=1/48`.                                                (6.6)

Moreover `e_3(N_L^TN_L)=e_5(N_L^TN_L)=0`. This is not a QFORM counterexample: it is a mechanism stress family. It proves that anchored volume plus large E2 does not force a transverse hub edge, a disjoint E3/E5 volume, or a physical pivot bounded away from zero; indeed `b_L ->0` as `L->infinity`. A future closure must genuinely pay the Schur/internal-star/ill-conditioned collar rather than discard it.

## 7. First unpaid implication after this run

The source-complete next interface is

`QFORM-LOCAL-E2-RANK2-COLLAR-OR-TWOSTAR-PAYMENT-v1`:

under the full original independent cap-one hypotheses and the fresh all-small-diagonal r42 compiler, uniformly pay the remaining local packets while retaining every same-bank coefficient, every outside coupling, all signs, affine terms and extra spectrum. In particular:

- in the one-anchor branch `J_sep>=1/2304`, `E_2(N)>4/9`, `e_5(N^TN)<1/1024`, pay the exact/near-rank-two residual after (4.1)--(4.2), whose exact-rank-two endpoint is now confined to (4.4)--(4.7);
- splice this with account03/B03's already-paid exact-rank-one endpoint and its quantitative near-rank-two tail relation after disjoint E3 exits;
- in the overlap-two branch retain account03/B19 r45's genuine two-star and giant-near-rank-one collars without deleting their nonzero transverse tails.

A productive next mechanism is not another search for one good minor. The formula (2.4) says to attack the Schur scalar and internal-star currencies by a source-bank Fourier transform that is stable as `s_2->0`, while the extreme-condition branch should be matched directly to the already-proved exact-rank-one triangle receiver. The small second singular direction cannot simply be dropped because the rough input laws have no moments or support bound.

## 8. Verification and status

The identity (2.4) was independently checked on 5000 random rank-two rectangular matrices by direct enumeration of every anchored physical 3x3 minor. The maximum normalized discrepancy was `4.20e-15`; the exact exterior proof above is the proof, and the computation is only a regression check.

Numerical constants independently recomputed:

- `3*2^(5/6)=5.345392308842036`;
- transverse gate (4.1): `24.475786831866067`;
- pinned D5 gate (5.3): `23.316439815971243`;
- `sqrt(2)/64=0.02209708691207961`;
- condition threshold `4096/3=1365.3333333333333`.

Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**. No valid target counterexample was found. Global continuity remains a separate open issue. No scheduler, notification, email, permission, public-release, installation, paid-call, or cross-account-authentication mutation is part of this mathematical report.
