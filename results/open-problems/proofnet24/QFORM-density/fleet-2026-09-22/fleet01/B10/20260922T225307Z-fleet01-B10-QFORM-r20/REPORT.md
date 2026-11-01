SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B10, 2026-09-22T22:53:07Z.
attacking: the double-small Schur-defect chamber via a mixed-norm source-product Fresnel estimate, then an exact graph-plane discriminant audit of the generated mismatch.

# fleet01/B10 QFORM r20 — one-sided defect Fresnel bridge and graph-plane discriminant

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW_SUPPORTING_THEOREM / NEW_EXACT_STRUCTURAL_IDENTITY / LOCAL_MECHANISM_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and fresh source state

The full owner target remains open. The inputs are independent original real coordinates with densities at most one; no moment, support, Gaussian, log-concavity, or post-rotation independence assumption is introduced.

Fresh owner control during this run remained QFORM-only under revision `2026-09-22.15`. The live corrections against arbitrary-joint three-dimensional coarea, positive conditional projection-height moments, conditional-cap-as-independence, fiber suprema, law-uniform one-dimensional quadratic-phase decay, and one-good-local-minor completion are retained.

The latest completed designated partner is fleet02/B10 `20260922T225540Z-fleet02-B10-QFORM-auto11`, canonical

`yspennstate/math-open-problems@9005415f079b7b46c0618c0187bf29b3f8d44167`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T225540Z-fleet02-B10-QFORM-auto11/REPORT.md`.

It proves the tripartite heavy-hub delete-or-isolate lemma. In particular a surviving exact-rank-three core can be reduced either by deleting a heavy original coordinate while retaining spectral condition at scale `2^-18`, or to a singleton hub plus two original-coordinate banks carrying fixed-hub exterior packet at least `1/512`; its diffuse child is paid by `768`. The local-pivot/pair/triple shortcut is refuted by an exact target family.

I also use the immediately preceding completed fleet02/B10 generated-mismatch result,

`yspennstate/math-open-problems@ceae35deb4625f33bb99551dc50e455285d44da0`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T214629Z-fleet02-B10-qform/REPORT.md`.

In its heavy-null two-bank state it gives disjoint banks `J,K`, transverse Grams `S_J,S_K` with

`det S_J det S_K >= 1/640`,

least-squares decompositions

`alpha_G = V_G p_G + eta_G`, `V_G^T eta_G=0`, `tau_G=||eta_G||^2`,

and, with `d=p_J-p_K`,

`p_J=S_K d`, `p_K=-S_J d`,
`rho:=1-c=d^T S_J S_K d+tau_J+tau_K`.                              (1.1)

It also proves that if `max(tau_J,tau_K)>=1/64`, a grouped full-bank Fresnel argument gives `||p_Q||_infinity<46.282`, continuously. Hence the genuinely hard leakage chamber has `0<tau_J,tau_K<1/64`.

This run changes mechanism: rather than another local extraction or peeling step, it proves a mixed Fourier estimate that uses a full three-dimensional bank on only one side and only the two-dimensional transverse marginal on the other. It then derives the exact algebra controlling the zero-defect graph-plane limit and shows that large generated mismatch by itself does not force a rank-two physical cross bank.

## 2. Mixed-norm Fourier lemma for one hub, one full bank, one transverse bank

Fix a unit vector `r` and identify `R^3=R r direct_sum r^perp`. Let three mutually independent original-coordinate source groups produce:

- a scalar spectral variable `W r`, where `W` has density cap `K_0`;
- a full three-dimensional spectral vector `Z_S` with density cap `M_S`;
- an arbitrary spectral vector `Z_T=(L_T,Y_T)` in the splitting `R r direct_sum r^perp`, for which only the transverse marginal `Y_T` is assumed to have a two-dimensional density cap `H_T`.

Allow an arbitrary real measurable self-phase on each source group. Such phases include arbitrary within-bank quadratic terms and affine terms arising after conditioning on outside original coordinates.

For fixed Fourier time `t`, weight each source law by its unit-modulus self-phase and denote the corresponding complex measures by `mu_0,mu_S,mu_T`.

### Lemma 2.1 — mixed source Fourier budget

With Fourier convention `hat f(xi)=int exp(i xi dot x) f(x) dx`, the convolution

`c_t=mu_0*mu_S*mu_T`

satisfies

`||hat c_t||_1 <= (2 pi)^3 (K_0 M_S H_T)^(1/2)`.                  (2.1)

#### Proof

Write a frequency as `(u,zeta)` with `u in R` along `r` and `zeta in r^perp`.

For the scalar group, disintegration is trivial and Plancherel gives

`||hat mu_0||_(L2(du)) <= (2 pi)^(1/2) K_0^(1/2)`.                (2.2)

For the full bank, its complex density has modulus bounded by the positive bank density, hence

`||hat mu_S||_(L2(R^3)) <= (2 pi)^(3/2) M_S^(1/2)`.              (2.3)

For the third bank, fix `u`. Disintegrate its positive law over the transverse variable `Y_T=y`. Multiplication by `exp(iuL_T)` and by the arbitrary unit-modulus self-phase produces a complex transverse density `b_u(y)` satisfying pointwise

`|b_u(y)| <= p_(Y_T)(y)`.

Therefore `||b_u||_2<=H_T^(1/2)`, and two-dimensional Plancherel yields the uniform slice estimate

`sup_u ||hat mu_T(u,.)||_(L2(dzeta)) <= (2 pi) H_T^(1/2)`.       (2.4)

Now

`hat c_t(u,zeta)=hat mu_0(u) hat mu_S(u,zeta) hat mu_T(u,zeta)`.

For fixed `u`, Cauchy--Schwarz in `zeta` gives

`int |hat mu_S hat mu_T| dzeta
 <= ||hat mu_S(u,.)||_2 ||hat mu_T(u,.)||_2`.

Use (2.4), then Cauchy--Schwarz in `u` and (2.2)--(2.3). The powers of `2 pi` add to three, proving (2.1). QED.

The point is that no density of `(L_T,Y_T)` is required. In particular this estimate remains valid when the third bank has zero Schur defect and is supported on a two-dimensional graph plane.

## 3. New theorem: one-sided Schur-defect Fresnel bridge

Let `M` be an invertible real symmetric `3x3` matrix. Put

`Y=W r+Z_S+Z_T`

and allow arbitrary block-separable source phases as above. Define

`Q=Y^T M Y + (block-separable phases interpreted as real additive terms)`.

### Theorem 3.1 — `QFORM-HUB-MIXED-L2-FRESNEL-v1`

Under the hypotheses of Section 2, `Q` has a bounded continuous density vanishing at infinity and

`boxed{ ||p_Q||_infinity
 <= 3 |det M|^(-1/3) (K_0 M_S H_T)^(1/3). }`                    (3.1)

#### Proof

By (2.1), Fourier inversion gives a bounded continuous complex density `c_t`. The standard regularized three-dimensional Fresnel identity used in the completed grouped-L2 theorem gives, for `t!=0`,

`|phi_Q(t)|
 <= pi^(3/2) |t|^(-3/2) |det M|^(-1/2) (K_0 M_S H_T)^(1/2)`.     (3.2)

Together with `|phi_Q(t)|<=1`, if the coefficient in (3.2) is `A`,

`int_R |phi_Q(t)|dt <= 6 A^(2/3)`.

Fourier inversion therefore yields

`||p_Q||_infinity <= (1/(2 pi)) 6 A^(2/3)`
`=3 |det M|^(-1/3)(K_0M_SH_T)^(1/3)`.

Since `phi_Q in L1`, the density has a continuous representative tending to zero at infinity. QED.

This is a genuinely mixed-dimensional source theorem: one group pays one Fourier dimension, one bank pays three, and the last bank pays only its two transverse dimensions. Total `1+3+2=6`, exactly the L2/Fresnel scaling needed for `|t|^(-3/2)`. No conditional spectral density or post-rotation independence is used.

## 4. Application to the designated partner's heavy-null two-bank state

Return to the fleet02/B10 two-bank state (1.1), in a null basis with distinguished original coordinate

`u_0=sqrt(c) r`, `c>=7/9`, `r^T M r=0`, `D:=|det M|>=1/2`.

For each bank `G=J,K`, its full spectral Gram has block form

`H_G=[[rho_G,b_G^T],[b_G,S_G]]`

and exact determinant

`det H_G=det S_G * tau_G`.                                           (4.1)

The cap-one product-projection theorem therefore gives, when `tau_G>0`,

`||p_(Z_G)||_infinity <= 2^(3/2) [det S_G tau_G]^(-1/2)`.          (4.2)

For either bank, regardless of `tau_G`, its transverse two-dimensional projection has

`||p_(Y_G)||_infinity <= 2 [det S_G]^(-1/2)`.                     (4.3)

The scalar `W=sqrt(c)X_0` has cap `c^(-1/2)` and is genuinely independent of both banks.

Apply Theorem 3.1 with the bank having the larger defect used as the full bank. Writing

`tau_*:=max(tau_J,tau_K)`,

we obtain the one-sided estimate

`boxed{ ||p_Q||_infinity
 <= 3*2^(5/6) D^(-1/3)c^(-1/6)
       [det S_J det S_K tau_*]^(-1/6). }`                          (4.4)

The density is continuous.

This is an actual inequality-level use of the fleet02/B10 state. With the partner's quantitative packet

`det S_J det S_K>=1/640`, `D>=1/2`, `c>=7/9`,

if `tau_*>=1/64` then

`||p_Q||_infinity
 <=3*2^(5/6)*2^(1/3)*(9/7)^(1/6)*(40960)^(1/6)`
` <41.233`.                                                         (4.5)

Thus the partner's already-paid one-large-leakage branch admits a slightly sharper continuous-density estimate and, structurally more importantly, the opposite bank is required to supply only a bounded transverse marginal. It may have zero Schur defect.

Equation (4.4) still degenerates as both defects tend to zero. It therefore does not falsely promote the full rank-three theorem.

## 5. Exact graph-plane discriminant at the zero-defect boundary

The partner identities show that the remaining difficulty is not arbitrary: when a bank defect vanishes, its spectral rows lie exactly on a graph plane over `r^perp`.

Write the null-basis spectral matrix as

`M=[[0,m^T],[m,D_0]]`,                                               (5.1)

with `m in R^2`, `m!=0`, and `D_0=D_0^T`. For `p in R^2`, define the graph-plane basis

`R(p)=[[p_1,1,0],[p_2,0,1]]`

and its oriented normal

`n(p)=(1,-p_1,-p_2)^T`.

### Lemma 5.1 — `QFORM-GRAPH-PLANE-COFACTOR-v1`

For every `p,q in R^2`,

`boxed{ det( R(p) M R(q)^T )
       = n(p)^T adj(M) n(q). }`                                    (5.2)

If `M` is invertible this is also

`det M * n(p)^T M^(-1)n(q)`.

#### Proof

The two rows of `R(p)` have cross product `n(p)`, and similarly for `R(q)`. The Cauchy--Binet/exterior-square identity for a `2x3`, `3x3`, `3x2` product states that the determinant of the induced `2x2` bilinear compression is the pairing of these two exterior vectors through `wedge^2 M`. Under the Hodge identification in dimension three, `wedge^2 M` is `adj(M)`; symmetry removes any transpose ambiguity. QED.

There is a more revealing centered form. Put

`h=(p+q)/2`, `d=p-q`.

Make the determinant-one null shear `x=x'+h dot y`. It sends the two graph slopes to `+d/2` and `-d/2`, leaves `m` unchanged, and changes the transverse block to

`D_c=D_0+h m^T+m h^T`.                                               (5.3)

The cross compression becomes

`K=D_c +(d m^T-m d^T)/2`.                                           (5.4)

Since the second summand is a `2x2` skew matrix, its unique off-diagonal magnitude is `det(d,m)/2`. Hence

`boxed{ det K = det D_c + (1/4) det(d,m)^2. }`                      (5.5)

This identity pinpoints what the generated mismatch can and cannot buy. Only the component of `d` transverse to the null-coupling vector `m=M r` contributes the positive skew-discriminant term. A mismatch parallel to `m` contributes nothing to the rank-two cross determinant.

## 6. Quantitative angular information from the partner state

In the double-small chamber `tau_J,tau_K<1/64`, if additionally

`rho=1-c>=1/16`,

then (1.1) gives

`E_gen:=d^T S_J S_K d
 =rho-tau_J-tau_K >0`,

and in the worst limiting case `rho>=1/16` gives `E_gen>=rho-1/32>=1/32` (with strict inequality when the defects are strictly below `1/64`). The partner bounds

`(1/160)I_2<=S_JS_K<=(1/4)I_2`

therefore imply

`||d||^2 >=4E_gen >=1/8`,
`||d||^2 <=160E_gen <=320/9`.                                      (6.1)

The graph-plane normals satisfy

`n(p_J) cross n(p_K)
 =(det(p_J,p_K), d_2,-d_1)`,

hence

`||n(p_J) cross n(p_K)||>=||d||`.                                  (6.2)

Since `||p_J||,||p_K||<=||d||`, the sine of the angle `theta` between the two graph planes obeys

`sin theta
 >= ||d||/(1+||d||^2)
 >= 24 sqrt(5)/329
 >0.163`.                                                          (6.3)

Thus away from the very-near-coloop chamber `rho<1/16`, the two zero-defect graph limits are quantitatively separated in projective spectral geometry. Equation (5.5), however, shows that this angular separation alone is not enough to force a rank-two cross determinant.

## 7. Source-valid falsifier: large generated mismatch need not force a rank-two cross bank

The latest fleet02/B10 hard family can be specialized to make the obstruction exact.

Take

`M=[[0,1,0],[1,0,0],[0,0,1]]`,                                    (7.1)

so the spectrum is exactly `{-1,1,1}` and in (5.1)

`m=(1,0)`, `D_0=diag(0,1)`.

Use the partner's two-bank construction with

`S_J=S_K=I_2/2`,
`tau_J=tau_K=epsilon^2`,

and choose the generated slope vector `p` parallel to `m`, with

`p_J=p`, `p_K=-p`,
`||p||^2=2/9-2epsilon^2`,
`0<epsilon<1/8`.                                                    (7.2)

The partner construction supplies an exact Parseval physical frame with heavy leverage `c=7/9`, cap-one original product provenance, and both defects strictly positive and below `1/64`. Here

`d=2p` is nonzero and quantitatively macroscopic, but `d parallel m`. The centered shear is already centered (`h=0`), so (5.4) gives

`K=D_0`,
`det K=0`.                                                         (7.3)

Equivalently, the generated two-plane cross interaction has only rank one even though the graph planes are separated and almost all longitudinal energy is generated mismatch. The full physical cross bank regains rank three only through the two residual innovations; its three-singular-value product consequently collapses with the defects exactly as recorded by the partner.

Therefore the candidate implication

`large generated mismatch => uniformly nondegenerate rank-two cross bank`

is **false even inside the exact target class**. This is not a counterexample to QFORM; it is a source-valid counterexample to that intermediate mechanism.

The identity (5.5) shows the correct replacement. A future bridge must distinguish:

1. **transverse mismatch:** `|det(d,m)|` is appreciable, where the positive skew-discriminant can feed an aggregate rank-two mechanism unless cancelled by an indefinite `D_c`;
2. **aligned mismatch:** `d` is nearly parallel to `m`, where the generated cross term becomes essentially block-separable and the only nontrivial inter-bank rank restoration comes from the genuine residual innovations;
3. **near-coloop:** `rho<1/16`, where all longitudinal complement energy is small in coefficient space but cannot be discarded probabilistically because no moments or support bounds exist.

This is a sharper trichotomy than simply `tau_J,tau_K small`.

## 8. Conditional end-to-end map and first unpaid implication

The current rank-three route can now be stated compactly.

- The latest fleet02/B10 tripartite theorem routes every surviving uniformly conditioned core either to a deletable heavy row or to a singleton hub plus two aggregate banks; diffuse children are already paid.
- In the heavy-null two-bank realization, if one Schur defect is at least `1/64`, Theorem 3.1 gives the continuous bound `<41.233` using the other bank only through its transverse marginal.
- If one defect is exactly zero, the preceding B10 hyperbolic-square boundary theorem gives the uniform essential bound `<=96`.
- The remaining punctured chamber has both defects in `(0,1/64)`. When `rho>=1/16`, its graph limits are quantitatively separated by (6.3), but Section 7 proves that separation/generated mismatch does not itself force rank-two cross curvature. When `rho<1/16`, one is in the true near-coloop endpoint.

The first unpaid implication is therefore

`QFORM-DOUBLE-SMALL-DEFECT-TRANSVERSE-OR-ALIGNED-BRIDGE-v1`:

> In the heavy-null two-bank state with `0<tau_J,tau_K<1/64`, combine the exact discriminant (5.5) with the product-origin residual directions. In the transverse-mismatch branch, convert the skew discriminant or its cancellation against `det D_c` into a paid bank-level rank-two/log-smoothing exit. In the aligned branch, exploit that the generated mismatch is block-separable before paying the two residual innovations. Do not treat the residual coefficients as small random perturbations.

The new mixed-norm lemma identifies the analytic interface needed for such a proof: a bank can be kept at the transverse `L2` level without paying its Schur defect, while another independent source group supplies the missing Fourier dimension. The unresolved task is to manufacture that missing dimension uniformly when **both** defects are positive but arbitrarily small.

## 9. Status

- `QFORM-HUB-MIXED-L2-FRESNEL-v1`: **PROVED SUPPORTING THEOREM**; bounded continuous density in its stated scope.
- `QFORM-GRAPH-PLANE-COFACTOR-v1` and centered discriminant (5.5): **PROVED EXACT STRUCTURAL IDENTITIES**.
- `large generated mismatch => rank-two cross bank`: **REFUTED by a target-valid specialization of the designated partner family**.
- arbitrary exact-rank-three orientation: **OPEN / NOT PROVED / NOT DISPROVED**.
- full owner target, including arbitrary additional spectrum: **OPEN / NOT PROVED / NOT DISPROVED**.
- continuity: **proved for Theorem 3.1 branches only; not proved in full generality**.

No Monte Carlo, finite census, hidden support bound, post-rotation independence, conditional-profile supremum, or law-uniform pointwise oscillatory decay is used.
