SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T16:32:23Z.
attacking: the partner r33 aggregate cross-rectangle E2 branch — close its bounded-support physical spectral subproblem, then isolate the genuinely support-diffuse obstruction without selecting one minor.

# account02/B07 — aggregate E2 support concentration gives a real four-eigenvalue physical core

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Method: complementary constructions and source-valid counterexamples  
Run: `20260923T163223Z-account02-B07-QFORM-auto11`  
Initial control: `yspennstate/math-research-brain@45afbd9740350eae52908f0d5cc1ceb97cd91ea7`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW BOUNDED-SUPPORT E2 PHYSICAL-CORE RECEIVER / PINNED-e5 FRACTIONAL RESULT APPLIED / EXACT SUPPORT-DIFFUSE TARGET STRESS / FULL QFORM OPEN**.

The unrestricted theorem is not proved or disproved here. Inputs remain arbitrary independent ORIGINAL-coordinate laws with densities at most one. No moments, bounded support, connected support, log-concavity, iid assumption, diagonal-basis assumption, or independence after rotation is introduced. Essential boundedness is the target; continuity is kept separate.

## 1. First unpaid implication and exact incoming packet

The latest completed designated partner is account03/B07 r33:

`yspennstate/math-open-problems@316522c99a92f168d0e0dcfe3be3aa032bdf53f9`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T153842Z-account03-B07-qform-r33/REPORT.md`.

Its four-bank physical block is

`K=[[A,B],[C,D]]`,

with all four banks subsets of disjoint ORIGINAL-coordinate row/column sides. Put

`Omega=sum_(i,k,j,l) (A_ij D_kl-B_il C_kj)^2`.                 (1.1)

Each summand is the square of a literal physical `2 x 2` cross-rectangle determinant. At the current strict-N3 scale the partner uses

`h=(2sqrt(2)-1)/1572864`,                                      (1.2)

with the inherited physical bounds

`|A_uv|<=h/8` for every relevant off-diagonal physical entry,
`|A_uu|<h^2/128`,                                               (1.3)

and its aggregate-minor alternative is

`boxed: sqrt(Omega)>C0 h^2`,
`C0=462.4798790835328`.                                        (1.4)

The sibling is one global physical rank-one tube; it remains a separate low-tail/hub obligation. This run attacks (1.4).

The first unpaid implication after the calculation below is therefore precise:

`QFORM-R33-SUPPORTDIFFUSE-E2-OR-GLOBAL-R1-RECEIVER-v1`:

> once bounded support of the determinant packet has been eliminated, consume either the genuinely support-diffuse aggregate `E2` branch, using its curvature-safe fractional currency, or the partner's global rank-one tube, while retaining arbitrary same-bank curvature, outside couplings, nonzero tails and all additional spectrum.

## 2. Determinant law and support concentration

Normalize the cross-rectangle squared determinants from (1.1):

`w(i,k,j,l)=(A_ij D_kl-B_il C_kj)^2/Omega`.                    (2.1)

For the physical row pair `S={i,k}` and column pair `T={j,l}`, define inclusion marginals

`alpha_x=P_w(x in S)`, `beta_y=P_w(y in T)`.                   (2.2)

Thus

`sum_x alpha_x=2`, `sum_y beta_y=2`.                            (2.3)

For physical support sets `R0,C0` put

`delta_R=sum_(x notin R0) alpha_x`,
`delta_C=sum_(y notin C0) beta_y`,
`theta=1-delta_R-delta_C`.                                     (2.4)

Whenever `theta>0`, the union bound gives

`P_w(S subset R0 and T subset C0)>=theta`.                     (2.5)

Let

`K0=A[R0,C0]`, `p=|R0|`, `q=|C0|`, `r=min(p,q)`.               (2.6)

Every retained cross-rectangle determinant is among the ordinary physical `2 x 2` minors of `K0`; hence

`boxed: E2(K0)>=theta Omega`.                                  (2.7)

This is aggregate determinant support. No single determinant has been chosen.

## 3. From aggregate E2 to a second singular value

Let `s1>=s2>=...>=sr` be the singular values of `K0`, and write `L=||K0||op=s1`. Cauchy-Binet gives

`E2(K0)=sum_(a<b) s_a^2 s_b^2`.                                (3.1)

Every summand is at most `L^2 s2^2`, so

`E2(K0)<=binom(r,2)L^2 s2(K0)^2`.                              (3.2)

Combining (2.7)-(3.2),

`boxed:
s2(K0)>=sqrt(theta Omega)/[sqrt(binom(r,2)) L].`              (3.3)

Inside the strict partner chamber (1.3), every entry of `K0` is off diagonal in the ambient symmetric matrix and therefore has modulus at most `h/8`. Consequently

`L<=||K0||F<=sqrt(pq) h/8`.                                    (3.4)

If `p,q<=m`, equations (1.4), (3.3), (3.4) yield

`boxed:
s2(K0)>
 [8 C0 sqrt(theta)/(m sqrt(binom(m,2)))] h.`                   (3.5)

The point is that a second-compound packet is not yet a three-eigenvalue core in general. The strict-N3 smallness of the two same-side physical blocks supplies the missing step.

## 4. The actual bounded-dimensional spectral subproblem is paid

Let `H=R0 union C0`. The two sides are disjoint original-coordinate banks, so `|H|=p+q`. Split the physical principal block as

`A_H = O+B0`,                                                   (4.1)

where

`O=[[0,K0],[K0^T,0]]`,                                         (4.2)

and `B0` is block diagonal, consisting of the actual two same-side principal blocks. The nonzero singular values of `O` are

`s1(K0),s1(K0),s2(K0),s2(K0),...`,                             (4.3)

so

`s4(O)=s2(K0)`.                                                 (4.4)

By (1.3), each same-side block of cardinality at most `m` has maximum absolute row sum below

`mu_m=(m-1)h/8+h^2/128`.                                       (4.5)

Hence

`||B0||op<=mu_m`.                                               (4.6)

Weyl's singular-value perturbation inequality gives

`boxed:
s4(A_H)>=s2(K0)-mu_m.`                                       (4.7)

Since `A_H` is symmetric, its singular values are the absolute values of its eigenvalues. Thus positivity of the right side of (4.7) produces **four actual eigenvalues** of the bounded physical principal block, not an arbitrarily cancellable low-rank component.

### Concrete partner scale

Take the natural support-concentration gate

`delta_R+delta_C<=1/2`, so `theta>=1/2`.                        (4.8)

For `m<=31`, (3.5)-(4.7) imply

`s4(A_H)>sigma_m`,                                              (4.9)

where

`sigma_m = h[
  8 C0/(sqrt(2) m sqrt(binom(m,2)))
  -(m-1)/8-h/128
]`.                                                             (4.10)

The expression decreases across the relevant integer range; at the endpoint

`boxed:
sigma_31>0.163629064895129 h
        =1.9021595042617075e-7.`                               (4.11)

At `m=32` the same crude universal estimate changes sign, so this report claims the explicit support size `31`, not a larger one.

Now condition only on all ORIGINAL coordinates outside `H`. The remaining variables preserve independence and density caps, while every outside coupling becomes an arbitrary deterministic affine term. Apply the completed finite-dimensional projected-gradient theorem

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`

`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`, Corollary 4.1:

on `d` original coordinates, three actual eigenvalues of modulus at least `sigma` give

`||p_q||inf<=2 sqrt(6 pi d)/sigma`.                             (4.12)

Here `d<=62`, and in fact four eigenvalues satisfy (4.11). Therefore the entire partner branch satisfying (4.8) with `|R0|,|C0|<=31` obeys

`boxed:
||p_Q||inf < 3.595e8.`                                         (4.13)

The constant is intentionally unoptimized. It is universal. This closes the bounded-support `E2` spectral subproblem in the actual strict-N3 geometry. No reciprocal determinant or best-minor selection occurs anywhere.

## 5. Required e5 result applied directly to the r33 aggregate branch

The required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

and this run read `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The latter still reports no valid QFORM counterexample. The completed `D_k` volume estimate plus its fractional-potential lemma gives the already-derived curvature-safe endpoint

`H_(1/4)(Q):=sup_s E|Q-s|^(-1/4)
 <=3.929131771 E2(K)^(-1/16)`                                  (5.1)

for any physical cross block `K`; arbitrary two self-blocks, outside couplings and affine terms are retained by conditioning and decoupling.

Because every determinant in (1.1) is one of the `2 x 2` minors of the combined four-bank block,

`E2(K)>=Omega`.                                                 (5.2)

Insert the actual partner lower bound (1.4):

`boxed:
H_(1/4)(Q)
 <3.929131771 C0^(-1/8) h^(-1/4)
 <55.567.`                                                      (5.3)

Thus **the entire r33 aggregate-E2 branch already carries a universal quarter-Riesz bound**, even when its determinant support is completely diffuse. What remains is the nonlinear upgrade from this fractional currency to a density bound in the high-diffusion state; bounded-support states have now been removed by Section 4.

This is a real application of the completed e5 result to the latest partner inequality, not merely a citation.

## 6. Exact target-valid stress: aggregate E2 can be maximally diffuse

The support-diffuse alternative in Section 5 is real. It cannot be replaced by a theorem saying that constant aggregate `Omega`, or even arbitrarily many nonzero cross-rectangle minors, forces a bounded physical spectral core.

Fix `N>=2`. Take four mutually disjoint original-coordinate banks

`L1,L2,R1,R2`, each of size `N`, and write `J_N` for the all-ones matrix. Define the physical cross block

`K_N=diag(J_N/N,J_N/N)`                                        (6.1)

from `L1 union L2` to `R1 union R2`, and the symmetric target matrix

`A_N=[[0,K_N],[K_N^T,0]]`.                                     (6.2)

In the four-bank notation,

`A=J_N/N`, `D=J_N/N`, `B=C=0`.                                 (6.3)

### Spectrum and determinant packet

Each `J_N/N` has exactly one nonzero singular value, equal to one. Therefore

`s(K_N)=(1,1,0,...)`,                                          (6.4)

and

`spec_nonzero(A_N)={1,1,-1,-1}`.                              (6.5)

So this is a genuine target-class matrix with four eigenvalues of modulus one.

Moreover

`||A||F=||D||F=1`,                                             (6.6)

and every cross-rectangle determinant is

`A_ij D_kl-B_il C_kj=1/N^2`.                                  (6.7)

There are exactly `N^4` such terms. Hence

`boxed: Omega=1`.                                               (6.8)

The normalized determinant law is uniform. Every physical row coordinate has inclusion marginal `1/N`, and every physical column coordinate also has marginal `1/N`. Thus any fixed-cardinality supports leave essentially all determinant weight outside as `N->infinity`.

### No bounded physical core

Every nonzero entry of `A_N` has magnitude `1/N`. Therefore any principal block on at most `M` physical coordinates obeys

`||A_N[H,H]||op<=M/N ->0`                                      (6.9)

for fixed `M`. In particular no bounded-cardinality physical core has three eigenvalues bounded away from zero.

For sufficiently large `N` the same family lies in the current strict-N3 scale: diagonals vanish, off-diagonal coefficients are below `h/8`, and every physical principal-pair determinant has magnitude `1/N^2<h^2/128` once `N>sqrt(128)/h`.

Thus the r33 deterministic fact that its aggregate branch contains at least hundreds of millions of nonzero physical minors is genuine diffusion evidence, but it cannot by itself imply bounded-coordinate spectral localization.

This refutes only that intermediate shortcut. It is not a counterexample to QFORM.

## 7. The pinned e5 theorem pays the exact diffuse stress family

The same construction provides a clean source-valid regression. The physical range of `A_N` has dimension four. Its range projection has diagonal leverage exactly `1/N` on every physical coordinate, hence at most `1/2` for `N>=2`.

Apply the completed rank-`r` Fresnel-Brascamp-Lieb theorem from the required e5 `FOURIER_ROUTE_REPORT.md`. With four eigenvalues of absolute value one and Gram determinant one,

`|phi_Q(t)| <= (4 pi)^2 |t|^-2
             =16 pi^2 |t|^-2`.                                (7.1)

Together with `|phi_Q(t)|<=1`,

`int_R min(1,16 pi^2 |t|^-2) dt=16 pi`.                       (7.2)

Fourier inversion gives

`boxed: ||p_Q||inf<=8`.                                        (7.3)

In this special family the theorem also supplies a continuous density because the envelope is integrable. No spectral rotation of the random coordinates is used; the theorem is a product-measure estimate in the original coordinates.

So the exact obstruction to bounded-core extraction is itself paid for the correct reason: **diffuse physical leverage**, not a hidden good minor.

## 8. What changed in the proof map

Before this run, account03/B07 r33 had reduced its four-bank cancellation state to:

1. a large aggregate physical cross-rectangle `E2` packet, or
2. a single global physical rank-one tube.

The new result splits branch 1 further, before any reciprocal localization:

- if at least half of its determinant volume is captured, in the inclusion-marginal sense (2.4), by at most `31` row and `31` column physical coordinates, then the actual symmetric principal block on at most `62` original coordinates has four substantial eigenvalues and is fully paid by (4.13);
- otherwise the packet is quantitatively support-diffuse, but nevertheless has the universal curvature-safe quarter-Riesz bound (5.3).

The flat rank-two family (6.1) shows the support-diffuse survivor cannot be removed by a stronger bounded-core selection statement. Its successful e5 payment identifies the correct missing analytic feature: convert determinant-support diffusion, together with the current star/bank provenance or low-tail alternative, into a product-preserving Fresnel/decoupling receiver while arbitrary same-bank curvature remains present.

Accordingly the first unpaid implication is

`QFORM-R33-SUPPORTDIFFUSE-E2-OR-GLOBAL-R1-RECEIVER-v1`:

> Pay the support-diffuse aggregate-E2 branch (which already has `H_(1/4)<55.567`) or the r33 global rank-one tube, preserving all same-bank quadratic curvature, the true nonzero low-rank tail, outside couplings and extra spectrum. A valid argument may use grouped-coordinate/mixed-hub or another decoupled receiver, but may not infer a universally good physical minor or treat a small coefficient matrix as a small random quadratic perturbation on unbounded inputs.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains separate.

## 9. Checks and source status

`CHECKS.py` and `CHECKS.txt` beside this report evaluate the endpoint constants, verify that `m=31` is paid by the displayed crude bound while `m=32` is not claimed, and check the flat construction's singular values, spectrum and `Omega=1` at several finite sizes. Captured output ends `STATUS=PASS`. These are regression checks only; the proof is the exact determinant, singular-value and perturbation algebra above.

The required e5 source's `COUNTEREXAMPLE_SEARCH.md` reports no valid counterexample to the full conjecture. No independent end-to-end review of this new report has yet occurred.
