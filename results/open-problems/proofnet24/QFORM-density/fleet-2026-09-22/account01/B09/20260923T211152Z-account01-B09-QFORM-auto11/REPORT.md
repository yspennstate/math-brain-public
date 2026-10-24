SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T21:11:52Z.
attacking: aggregate the partner 3x2 kernel-derivative receiver over an arbitrary disjoint physical right bank, using a two-dimensional orthogonal pushforward only as a total-variation bound and retaining arbitrary right-bank curvature.

# account01/B09 — aggregate rank-two right bank and exact one-overlap compound identity

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control: revision `2026-09-22.15`  
Status: **ESSENTIAL STEP APPLIED / NEW SUPPORTING THEOREM / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted quadratic-form conjecture remains OPEN / not proved / not disproved. Full-target continuity also remains OPEN. This run closes the precise aggregation obstruction isolated by the newest completed designated partner theorem: for one fixed physical triple, a unit amount of one-index-overlap third-compound mass may be spread over arbitrarily many physical right pairs, so selecting a largest pair produces a dimension loss. The theorem below aggregates the entire right bank before reciprocal payment and gives a dimension-free continuous-density estimate.

No moment, compact-support, centering, iid, log-concavity, connected-support, diagonal-basis or post-rotation-independence assumption is introduced. No pointwise law-uniform quadratic-phase decay is used.

## 1. Fresh sources actually consumed

Fresh `math-research-brain/main` was read at observed head

`61bc5084156380142ff818045a8b3041e2d098c2`.

The current protected owner control remains QFORM-only at revision `2026-09-22.15`; account01/B09 is not paused. The owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` was consumed. The live `CURRENT_RESEARCH.md`, `CLAIMS.json`, `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, `scheduled_tasks/PROTOCOL.md`, `fleet.json`, `roles.json`, and the account01/B09 assignment were re-read.

The completed designated partner theorem actually used is

`QFORM-3x2-KERNELDERIVATIVE-L1-v1`,

`yspennstate/math-open-problems@65ed9ea70175fb28541d756aea01f6aeb491fd6c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T201318Z-account02-B09-QFORM-r14/REPORT.md`.

For a literal `3 x 2` physical packet with left self block `P`, rank-two cross columns `c_1,c_2`, `w=c_1 x c_2`, and `P w !=0`, it proves

`||p_Q||_infinity
 <= C_KD (||w|| ||P w||)^(-1/5)`,

`C_KD=5*6^(3/5)/2^(11/10)=6.834830666196632...`,

with a continuous density and the same coefficient multiplying interval length. The theorem retains arbitrary same-bank curvature and conditioned affine terms. Its Section 9 gives the aggregation obstruction addressed below.

A second completed receiver used only for the fixed-triple compiler in Section 7 is

`QFORM-PHYSICAL-D3-NO-MARGINAL-GATE-v1`,

`yspennstate/math-open-problems@8a4e6d0048174e047fc3b4ae8cabfbabba3cdc3b`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260923T165154Z-account01-B20-QFORM-auto11/NO_MARGINAL_D3.md`.

For any literal physical cut with third cross volume `Z_3>0`, it gives a continuous density and

`||p_Q||_infinity <= C_3 Z_3^(-1/6)`,

`C_3=3*2^(4/3)*exp(1/3)=10.5501688311...`,

with no row-marginal gate.

All live corrections are respected: no uniform pointwise van-der-Corput bound, no arbitrary-joint coarea lemma, no post-rotation independence, no conditional-fiber density supremum shortcut, no uniformly good single physical minor, and no deletion of a small quadratic coefficient on unbounded inputs is used.

## 2. Main theorem — fixed physical triple against an arbitrary rank-two right bank

Let `L` be **three original coordinates** and let `J` be any disjoint bank of original coordinates. Condition on every original coordinate outside `L union J`. Write

`Y=X_L in R^3`, `Z=X_J`,

`P=A[L,L]`, `C=A[L,J]`.

The conditional polynomial may contain arbitrary affine terms, arbitrary same-side quadratic curvature on `L` and `J`, and an arbitrary constant. Assume only

`rank(C)=2`.

Put

`G=C C^T`,

`Delta=sqrt(e_2(G))=s_1(C)s_2(C)>0`.

Let `n` be a unit vector spanning `ker(C^T)`, and set

`a=P n`.

### Theorem `QFORM-GROUPED-RANK2-KERNELDERIVATIVE-v1`

If `a!=0`, then for every admissible independent cap-one product input law the full ambient quadratic form has a bounded continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_G Delta^(-2/5)||a||^(-1/5),`

where

`C_G=2^(2/5) C_KD
    =5*6^(3/5)/2^(7/10)
    =9.018613132839628... .`

Consequently every interval `I` obeys

`boxed:
 P{Q in I}
 <= C_G Delta^(-2/5)||a||^(-1/5)|I|.`

The size of the right bank `J` does not enter the constant. No right-bank self-curvature restriction is imposed.

## 3. Source-coordinate normal form

The retained triples and the right bank are disjoint ORIGINAL-coordinate sets, hence `Y` and `Z` are independent groups. Their densities satisfy

`0<=F_Y<=1`, `0<=F_Z<=1`.

Choose an orthonormal `3 x 2` frame `E` spanning `n^perp`. Since `range(C)=n^perp`, the `2 x |J|` matrix

`B=E^T C`

has row rank two. Define

`S=(B B^T)^(1/2)=(E^T C C^T E)^(1/2)`

and

`R^T=S^(-1) B`.

Then

`B=S R^T`, `R^T R=I_2`,

so the two columns of `R` form an orthonormal frame in the physical right-coordinate space. Moreover

`det S = s_1(C)s_2(C)=Delta`.                         (3.1)

Write

`Y=n x+E u`,

and change variables

`r=S u`.

Then the physical cross term is exactly

`2Y^T C Z=2u^T B Z=2r^T(R^T Z)`.                    (3.2)

This is only an algebraic coordinate representation of the coefficient block. No independence is asserted for rotated coordinates inside `Y` or `Z`.

The transformed left density is

`g(x,r)=Delta^(-1)
 F_Y(n x+E S^(-1)r)`.                                  (3.3)

Thus

`0<=g<=Delta^(-1)`, `int g dx dr=1`.                   (3.4)

Its `r` marginal

`m(r)=int g(x,r) dx`

is the density of `S E^T Y`. The standard two-dimensional orthonormal projection-density theorem for an independent cap-one product source gives

`||p_(E^T Y)||_infinity<=2`.

After the determinant-`Delta` map `S`,

`boxed: m(r)<=2/Delta.`                                  (3.5)

## 4. The left moving quadratic fiber — unchanged from the completed partner proof

In the basis `(n,E)`, write

`P -> [[d,p^T],[p,H]]`,

where `d=n^T P n`, `p=E^T Pn`, and `H=E^TPE` is completely arbitrary. After substituting `u=S^(-1)r`, all terms depending only on `r` can be kept as a unit-modulus phase. The only `x`-dependent part is

`q_r(x)=d x^2+xi(r)x`,                                    (4.1)

where the arbitrary conditioned affine term is included in `xi`.

Its derivative satisfies the exact source-coordinate identity

`boxed:
 q_r'(x)=2(Pn)^T Y+beta=2a^T Y+beta,`                     (4.2)

for an arbitrary real conditioned `beta`.

Define

`h_r(x)=g(x,r)`,
`F_r(t)=int h_r(x) exp(i t q_r(x)) dx`,
`A0(t)^2=int_R2 |F_r(t)|^2 dr`.                           (4.3)

The completed account02/B09 quadratic-fiber argument uses only (3.4), (3.5), and (4.2). For completeness, its quantitative chain is recalled here.

For the pushforward density `nu_r` of `h_r(x)dx` under the degree-at-most-two polynomial `q_r`, one-dimensional coarea plus the at-most-two inverse branches gives

`int nu_r^(4/3)
 <=2^(1/3)
   int h_r(x)^(4/3)|q_r'(x)|^(-1/3) dx.`                 (4.4)

Set

`I(r)=int h_r^(4/3)|q_r'|^(-1/3)`.

Hausdorff--Young yields

`||F_r||_4^2 <=(4 pi)^(1/2) I(r)^(3/2).`                 (4.5)

Using `h_r<=Delta^(-1)`, then convexity on the normalized fiber and `m(r)<=2/Delta`, gives

`int I(r)^(3/2) dr
 <=sqrt(2) Delta^(-1)
   E|2a^T Y+beta|^(-1/2).`                               (4.6)

The variable `(a/||a||)^T Y` is a genuine one-dimensional orthonormal projection of the original independent triple and hence has density at most `sqrt(2)`. After scaling by `2||a||`, a direct near/far split gives

`E|2a^T Y+beta|^(-1/2)
 <=4*2^(-1/4)||a||^(-1/2),`                              (4.7)

uniformly in `beta`.

Minkowski applied to (4.5)-(4.7) therefore gives exactly the partner bound

`boxed:
 ||A0||_4
 <=2^(13/8) pi^(1/4)
   Delta^(-1/2)||a||^(-1/4).`                            (4.8)

No pointwise oscillatory decay has been used.

## 5. New step — arbitrary right-bank curvature via a complex pushforward

Let `psi(z)` denote the completely arbitrary right-bank quadratic-affine phase after outside conditioning. For each fixed `t`, define the complex measure on `R^2`

`mu_t(B)
 =int_{R^T z in B} F_Z(z) exp(i t psi(z)) dz`.             (5.1)

Let `nu` be the probability pushforward of `F_Z(z)dz` by the same **orthonormal projection** `R^T z`. Since `R` has orthonormal columns, the two-dimensional projection-density theorem gives a probability density `p_V` with

`||p_V||_infinity<=2`.                                     (5.2)

For every Borel `B`, total variation satisfies

`|mu_t|(B)
 <=int_{R^Tz in B}F_Z(z)dz
 =nu(B)`.                                                    (5.3)

Hence `mu_t` has a complex density `b_t(v)` satisfying

`|b_t(v)|<=p_V(v)` almost everywhere. In particular

`||b_t||_1<=1`,
`||b_t||_infinity<=2`,
`boxed: ||b_t||_2<=sqrt(2).`                                (5.4)

This is the critical product-safe step. The right variables are never rotated and declared independent. The orthogonal projection is used only to dominate the total variation of a pushforward measure.

Keeping the arbitrary left `r`-only phase inside `a_t(r)`, the conditional characteristic function has the exact representation

`phi_Q(t)
 =int_R2 int_R2
   a_t(r)b_t(v) exp(i 2t r^T v) dr dv,`                    (5.5)

with

`|a_t(r)|=|F_r(t)|`, `||a_t||_2=A0(t)`.                    (5.6)

Two-dimensional Plancherel and the scaling of the Fourier variable `2t v` give, for `t!=0`,

`boxed:
 |phi_Q(t)|
 <=sqrt(2) pi |t|^(-1) A0(t).`                             (5.7)

The only loss relative to the partner's literal two-coordinate right bank is therefore the factor `sqrt(2)` in (5.7).

## 6. Time integration and the direct O(interval length) estimate

Combine (5.7) with `|phi_Q|<=1`. The account02/B09 tail optimization applies verbatim. Hölder with the `L^4` norm (4.8) gives, for every `T>0`,

`int_R |phi_Q(t)|dt
 <=2T
  +sqrt(2) pi 6^(3/4) T^(-1/4)||A0||_4.`                  (6.1)

The minimizing split is the same as in the completed partner proof. Since the coefficient in the tail has acquired a factor `sqrt(2)`, the optimized density coefficient acquires exactly

`(sqrt(2))^(4/5)=2^(2/5)`.                                 (6.2)

Thus Fourier inversion gives

`||p_Q||_infinity
 <=2^(2/5) C_KD
   Delta^(-2/5)||a||^(-1/5)
 =C_G Delta^(-2/5)||a||^(-1/5).`                           (6.3)

The right side of (6.1) is finite after optimization, so `phi_Q in L^1`. Hence the density is continuous and vanishes at infinity. The density estimate immediately yields

`P{Q in I}
 <=C_G Delta^(-2/5)||a||^(-1/5)|I|`                       (6.4)

for every interval `I`. There is no squaring of a final probability and therefore no square-root small-ball loss. This proves `QFORM-GROUPED-RANK2-KERNELDERIVATIVE-v1`. `QED`

## 7. Exact aggregate physical-minor identity

Write the physical columns of `C` as `c_j in R^3`. For every pair `r<s` in the right bank put

`w_(rs)=c_r x c_s`.

The second-compound Cauchy--Binet identity gives

`boxed:
 sum_(r<s) w_(rs) w_(rs)^T = adj(G),
 G=CC^T.`                                                   (7.1)

One way to see (7.1) is entrywise: every diagonal cofactor of `G` is the sum of squares of the corresponding `2x2` minors of `C`, and polarized Cauchy--Binet gives the off-diagonal cofactors with exactly the cross-product signs.

Define the fixed-triple one-overlap kernel-derivative mass

`V_L=sum_(r<s)||P w_(rs)||^2.`                              (7.2)

Since `P` is symmetric,

`V_L
 =tr(P^2 adj(G)).`                                        (7.3)

When `rank C=2`, `G` has one-dimensional kernel `span{n}` and

`adj(G)=e_2(G) n n^T
       =Delta^2 n n^T`.                                    (7.4)

Therefore

`boxed:
 V_L=Delta^2 ||Pn||^2.`                                    (7.5)

The main theorem can consequently be written with no selected physical right pair at all:

`boxed:
 ||p_Q||_infinity
 <= C_G [ e_2(G) V_L ]^(-1/10).`                           (7.6)

Indeed `e_2(G)=Delta^2`, so

`[e_2(G)V_L]^(-1/10)
 =Delta^(-2/5)||Pn||^(-1/5)`.

This is exactly the aggregation that the partner report identified as missing: all physical right pairs are summed **before** the reciprocal scale is taken.

### Fixed-triple compiler

For the same fixed physical triple `L`, let `C=A[L,L^c]`.

- If `rank C=3`, then `Z_3=det(CC^T)>0`, and the completed no-marginal D3 receiver gives

  `||p_Q||_infinity<=C_3 det(CC^T)^(-1/6)`,

  with a continuous density.

- If `rank C=2` and `V_L>0`, the new grouped theorem gives (7.6), again with a continuous density.

- The only rank-two endpoint not paid by these two receivers is

  `V_L=0`, equivalently `Pn=0`.

- Rank `C<=1` remains a separate low-cross-rank branch.

This is an exhaustive source-coordinate classification for a fixed physical triple. It does **not** assert that the bare three-large-eigenvalue hypothesis supplies a fixed triple with a universally nondegenerate numerical scale.

## 8. Exact meaning of the rank-two endpoint

Let `tilde n in R^n` be the unit vector supported on the three coordinates `L`, with entries `n` there and zero elsewhere. Since

`C^Tn=0`,

the full coefficient matrix satisfies

`A tilde n=(Pn,0)`                                           (8.1)

under the decomposition `L | L^c`. Hence, using (7.5),

`boxed:
 ||A tilde n||^2
 =||Pn||^2
 =V_L/e_2(G).`                                              (8.2)

In particular,

`boxed:
 rank(C)=2 and V_L=0
 => A tilde n=0.`                                           (8.3)

Thus the exact analytic endpoint of the grouped theorem is not an unexplained failure of the method: it is a literal three-coordinate-supported **global kernel vector**. More generally the ratio `V_L/e_2(G)` is exactly the squared residual norm of this source-supported approximate kernel vector.

No density claim is made from operator-norm smallness of that residual; (8.2) is a deterministic structural identity only.

## 9. Required application of the designated partner theorem to an actual inequality

Take even `m>=2` and original coordinates

`Y_1,Y_2,Y_3,Z_1,...,Z_m`.

Define

`Q_m
 =2Y_1Y_3
  +2 sqrt(2/m) Y_1 sum_(j<=m/2) Z_j
  +2 sqrt(2/m) Y_2 sum_(j>m/2) Z_j.`                        (9.1)

This has left self block

`P=[[0,0,1],[0,0,0],[1,0,0]]`,

and full right cross columns

`c_j=sqrt(2/m)e_1` for `j<=m/2`,
`c_j=sqrt(2/m)e_2` for `j>m/2`.

Let

`U=sqrt(2/m) sum_(j<=m/2) Z_j`,
`V=sqrt(2/m) sum_(j>m/2) Z_j`.

At the coefficient-matrix level the nonzero action compresses to the five-dimensional matrix

`[[0,0,1,1,0],
  [0,0,0,0,1],
  [1,0,0,0,0],
  [1,0,0,0,0],
  [0,1,0,0,0]]`,

whose spectrum is exactly

`{sqrt(2),1,0,-1,-sqrt(2)}`.

Therefore the full physical matrix has four eigenvalues of modulus at least one and is target-valid for every even `m`.

Choose one literal right pair consisting of one coordinate from each half. For this pair,

`w=(2/m)e_3`,
`P w=(2/m)e_1`,

so the **completed account02/B09 theorem** gives the actual inequality

`boxed:
 ||p_(Q_m)||_infinity
 <= C_KD (4/m^2)^(-1/5)`                                   (9.2)

and the same coefficient times interval length, with a continuous density. For example, at `m=8`,

`boxed:
 ||p_(Q_8)||_infinity
 <11.901.`                                                  (9.3)

This verifies a genuine target-valid use of the designated partner theorem.

Now aggregate the entire right bank. Directly,

`CC^T=diag(1,1,0)`, `e_2(CC^T)=1`,

and there are `(m/2)^2` nonzero cross-half pairs, each contributing `||P w||^2=4/m^2`. Hence

`V_L=1`                                                      (9.4)

for every even `m`. The new grouped theorem therefore improves (9.2) to the uniform estimate

`boxed:
 ||p_(Q_m)||_infinity
 <=C_G
 =9.0186131328...<9.019,`                                   (9.5)

and

`boxed:
 P{Q_m in I}<9.019|I|`                                      (9.6)

for every interval `I`, with a continuous density, **uniformly in `m`**.

This exactly resolves the partner's Section 9 obstruction: the individual packet currency is `4/m^2 ->0`, but the grouped source-coordinate currency `e_2(G)V_L` is identically one.

## 10. What remains open

The full target is not closed. The first unpaid B09 implication is now

**`QFORM-AGGREGATE-TRIPLE-SELECTION-OR-SUPPORTED-KERNEL-v1`**:

> Starting only from `s_3(A)>=1`, aggregate over physical triples as well as over the right-pair bank. Either force a fixed original-coordinate triple with quantitative `rank-3` cross volume or quantitative `e_2(G_L)V_L`, or route the simultaneous degeneration to an already-paid grouped-coordinate/ridge/finite-collar branch. In the exact rank-two endpoint, use the identity `A tilde n=0` rather than pretending a single bad packet can be inverted.

The theorem here removes the *right-pair selection* loss but not the remaining *left-triple selection* problem. A sum of many small fixed-triple currencies cannot be replaced without proof by one uniformly good triple. The live correction forbidding a uniformly good single minor therefore remains fully in force.

A natural next analytic mechanism is to construct an aggregate left-triple version of the complex-pushforward argument, or to promote a bounded set of genuinely high-leverage physical coordinates until one of the completed D3, grouped rank-two, fixed-pair-volume, 3x2 kernel-derivative, or finite-hub receivers applies.

## 11. Scope audit

- Every conditioned bank is an original-coordinate bank, so the remaining random groups are genuinely independent.
- The orthogonal frame `R` is used only to define a deterministic projection and a pushforward measure; its coordinates are never declared independent.
- Arbitrary same-bank right curvature survives inside the complex pushforward `mu_t`.
- Arbitrary same-bank left curvature survives the quadratic-fiber calculation.
- No pointwise quadratic-phase decay is asserted.
- No probability is squared after the density estimate; the final small-ball estimate is linear in interval length.
- No small quadratic residual is deleted on unbounded inputs.
- The theorem has the correct scaling: `e_2(G)` has degree four in `A`, `V_L` degree six, and `[e_2(G)V_L]^(-1/10)` has density degree minus one.
- The exact endpoint `V_L=0` is recorded as a structural kernel identity, not mislabeled as a solved density branch.
- The unrestricted conjecture and unrestricted continuity claim remain OPEN.
