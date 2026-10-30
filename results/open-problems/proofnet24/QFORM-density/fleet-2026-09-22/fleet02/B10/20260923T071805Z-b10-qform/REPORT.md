SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B10, 2026-09-23T07:18:05.120462Z.
attacking: the exact-rank-three hybrid/near-null physical direction; consume the ruled-side theorem and preserve source-product provenance after projection.

# fleet02/B10 — heavy-hub two-vector-bank packet and a genuinely noncollinear true-collar stress family

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: rank-three coupled case; complementary constructions/source-valid counterexamples  
Run: `20260923T071805Z-b10-qform`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Classification: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / LOCAL_CANDIDATE_REFUTED / FULL_QFORM_OPEN`.

The unrestricted target remains OPEN: independent original-coordinate probability densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and no moment, support, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumptions. Essential boundedness is the target; continuity is separate.

## 1. Source boundary and first unpaid implication


The latest completed designated partner result actually used is fleet03/B10 r24,

`QFORM-NEARCOLOOP-MIXED-TRANSVERSE-EXCISION-v1`,

`yspennstate/math-open-problems@06f180467d43940acc1f939e216db2e23b7d7c88`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T044329Z-fleet03-B10-QFORM-r24/REPORT.md`,

with the later fleet03/B10 r25 transverse-heavy closure at

`yspennstate/math-open-problems@291d344e0c5af27b8b5074dbba22fee22abddbf8`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T034310Z-fleet03-B10-QFORM-r25/REPORT.md`.

Write the exact-rank-three form as

`A=R Lambda R^T`, `R^T R=I_3`, `sigma_min(Lambda)>=1`,

and let the heavy physical row be

`r_0=sqrt(c)e`, `c>63/64`, `rho=1-c<1/64`.

Put

`alpha=e^T Lambda e`, `|alpha|<1/16`,

and write every complementary row as

`r_j=s_j e+w_j`, `w_j perpendicular e`.

Let `M` be the genuinely mixed rows (`s_j!=0` and `w_j!=0`), and define

`rho_M=sum_(j in M) s_j^2`,

`H=sum_(j in M) w_jw_j^T`.

The Parseval identities give

`sum_(j in M) s_jw_j=0`

and the total transverse Gram of all complement rows is exactly `I_2`.

Write the eigenvalues of `H` as

`eta>=theta>=0`.

The full fleet03/B10 r24 payment condition is

`(1-rho_M)|alpha| <= (1/2) min(1-rho_M,1-eta)`.                    (1.1)

Therefore every genuinely unpaid state obeys

`boxed: 1-eta < 2(1-rho_M)|alpha| <=2|alpha|.`                    (1.2)

This is the starting collar below. Fleet03/B10 r25 separately pays any state having a second physical row with transverse leverage at least `1/4`; hence the live hard collar may also be taken with every individual transverse row light.

The required newest-Claude source was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The ruled theorem in the last file applies to the ACTUAL exact-rank-three form, not to a rotated independent law. For signature `(2,1)` it gives the genuine target inequality

`boxed: ess sup_(t>=0) p_Q(t) <= pi sqrt(2),`                     (1.3)

and the sign-reversed statement for signature `(1,2)`. Thus throughout this report the only density side still under discussion is the minority/two-sheet side.

The first unpaid implication at the start of this run was the prior B10 statement `QFORM-TRUECOLLAR-NONCOLLINEAR-HUBPACKET-RECEIVER-v1`: turn the constant hub-incident Pluecker mass into a product-safe two-sheet estimate when the mixed bank is genuinely noncollinear.

## 2. A two-colour theorem with NO small-longitudinal factor

For two positive semidefinite `2 x 2` matrices define

`M_perp(G_1,G_2)=tr(adj(G_1)G_2)`.

When

`G_1=sum_(j in Y) w_jw_j^T`, `G_2=sum_(k in Z) w_kw_k^T`,

the two-dimensional Cauchy--Binet identity is

`M_perp(G_1,G_2)=sum_(j in Y,k in Z) det(w_j,w_k)^2`.             (2.1)

### Theorem 2.1 — `QFORM-TRUECOLLAR-HUB-TWOBANK-PLUCKER-SPLIT-v1`

There is a partition of the MIXED ORIGINAL coordinates

`M=Y disjoint_union Z`

such that

`boxed: M_perp(H_Y,H_Z) >= (1/2) det H = (1/2)eta theta,`         (2.2)

where `H_Y=sum_Y w_jw_j^T`, `H_Z=sum_Z w_jw_j^T`.

Consequently the singleton physical hub and the two original-coordinate banks are three genuinely independent sources, and their aggregate hub-incident Pluecker packet obeys

`boxed:
 sum_(j in Y,k in Z) det(r_0,r_j,r_k)^2
 =c M_perp(H_Y,H_Z)
 >=(c/2)eta theta.}`                                              (2.3)

In particular, inside the true collar (1.2), if

`theta>=1/16`,

then `eta>7/8` and

`boxed:
 sum_(j in Y,k in Z) det(r_0,r_j,r_k)^2 >= 7c/256.}`              (2.4)

#### Proof

Colour each mixed original coordinate independently by `Y` or `Z`, each with probability `1/2`. Every unordered pair `{j,k}` is separated by the cut with probability `1/2`; if separated, its squared transverse determinant occurs exactly once in (2.1). Hence

`E M_perp(H_Y,H_Z)
 =(1/2)sum_(j<k; j,k in M) det(w_j,w_k)^2
 =(1/2)det H`,                                                    (2.5)

where the last equality is Cauchy--Binet for the `2 x |M|` transverse row matrix. Some deterministic cut attains its expectation. Because `r_0=sqrt(c)e`,

`det(r_0,r_j,r_k)^2=c det(w_j,w_k)^2`,                            (2.6)

which proves (2.3). Equation (2.4) follows from `eta>7/8`. QED.

### Why this improves the existing regression split in this collar

Fleet04/B10's completed `QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1`,

`yspennstate/math-open-problems@afdea9634d9e3f5fb09659da436292cf7dbe5b20`,

applied to this mixed bank (its regression residual is exactly `rho_M`, because `sum s_jw_j=0`) gives a three-colour certificate proportional to

`rho_M det H`.

That theorem is correct and useful in the positive-regression setting, but the factor `rho_M` can vanish in the near-coloop limit. The heavy physical hub already supplies a longitudinal source of mass `c~1`; using it before colouring removes that loss and yields (2.3), which stays uniformly positive whenever the second transverse eigenvalue `theta` does.

This is a product-provenance theorem only. It does NOT turn the two vector-valued banks into independent spectral coordinates. Their internal longitudinal/transverse projections remain dependent and must remain inside the eventual receiver.

## 3. Exact dichotomy: vector-bank packet or crossed near-collinearity

Let `T` denote all complement rows with `s_j=0` (pure transverse rows). Rows with `w_j=0` contribute nothing to the transverse Gram. Since the total complement transverse Gram is `I_2`,

`K:=sum_(j in T) w_jw_j^T=I_2-H`.                                (3.1)

Choose the transverse eigenbasis `(v,u)` of `H`, so

`H=eta vv^T+theta uu^T`,

`K=(1-eta)vv^T+(1-theta)uu^T`.                                  (3.2)

Combining (1.2) with Theorem 2.1 gives the following exhaustive coefficient-level split.

### Corollary 3.1 — `QFORM-TRUECOLLAR-TRANSVERSE-DICHOTOMY-v1`

Every live near-coloop state is in exactly one of the following two chambers.

**(A) Genuine two-dimensional mixed curvature:** `theta>=1/16`. Then there are disjoint mixed original-coordinate banks `Y,Z` whose hub packet is at least `7c/256`, equation (2.4).

**(B) Crossed near-collinear chamber:** `theta<1/16`. Then

`sum_(j in M) (u dot w_j)^2=theta<1/16`,                          (3.3)

while the pure-transverse complement satisfies

`sum_(j in T) (v dot w_j)^2=1-eta<2|alpha|`,                      (3.4)

`sum_(j in T) (u dot w_j)^2=1-theta>15/16`.                      (3.5)

Thus the mixed bank is quantitatively concentrated around the `v` transverse ray, while the disjoint pure-transverse bank is quantitatively concentrated around the crossed `u` ray, with its wrong-direction mass tied directly to the small physical Rayleigh pivot.

No random-variable perturbation statement is made. Equations (3.3)--(3.5) are exact coefficient identities/inequalities.

This is a genuine narrowing of the previous single gap: the noncollinear case now has a constant source-valid two-bank packet, whereas the remaining small-`theta` problem is explicitly an interpolation between two crossed almost-collinear original-coordinate banks.

## 4. A target-valid TRUE-COLLAR family showing scalar-bank reduction is insufficient

The preceding packet theorem would be much less useful if every live noncollinear state could already be reduced to the scalar collinear-bank theorem from the previous B10 run. The following exact target family shows that is false.

Fix any integer `m>=128`. Work in an orthonormal spectral basis `(e,v,u)`. Set

`epsilon=1/m`, `s=sqrt(1-epsilon^2)`,

`Lambda_m=[[-epsilon,0,s],[0,1,0],[s,0,epsilon]]`.                (4.1)

Then `Lambda_m^2=I_3`, hence

`spec(Lambda_m)={-1,1,1}`, `|det Lambda_m|=1`.                   (4.2)

Put

`rho=1/m`, `c=1-rho`,

`rho_M=1/(2m)`,

`eta=1-1/(4m)`,

`theta=1/2`.                                                       (4.3)

Use the physical hub

`r_0=sqrt(c)e`.                                                    (4.4)

For `j=0,...,m-1`, with `phi_j=2 pi j/m`, define the genuinely mixed rows

`r_j^M=(1/(sqrt(2)m))e
       +sqrt(2eta/m) cos(phi_j) v
       +sqrt(1/m) sin(phi_j) u`.                                  (4.5)

Add three disjoint pure banks, each with `m` rows:

`r_j^L=(1/(sqrt(2)m))e`,                                          (4.6)

`r_j^V=(1/(2m))v`,                                                (4.7)

`r_j^U=(1/sqrt(2m))u`.                                            (4.8)

The roots-of-unity identities give

`sum_j cos(phi_j)=sum_j sin(phi_j)=sum_j sin(phi_j)cos(phi_j)=0`,

`sum_j cos(phi_j)^2=sum_j sin(phi_j)^2=m/2`.                      (4.9)

Therefore the mixed-bank cross Gram vanishes and

`sum_M s_j^2=rho_M`,

`sum_M w_jw_j^T=eta vv^T+(1/2)uu^T`.                             (4.10)

The total spectral masses are

`e: c+rho_M+(rho-rho_M)=1`,

`v: eta+(1-eta)=1`,

`u: 1/2+1/2=1`.                                                   (4.11)

Hence the full row matrix `R_m` satisfies

`R_m^T R_m=I_3`.                                                   (4.12)

Consequently

`A_m=R_m Lambda_m R_m^T`                                         (4.13)

is an exact target matrix whose three nonzero eigenvalues are exactly `{-1,1,1}`.

### 4.1 It lies in the actual fleet03/B10 true collar

The hub has

`alpha=e^T Lambda_m e=-1/m`,                                      (4.14)

and `c>63/64`, `rho<1/64` for `m>=128`. The r24 obstruction scale is

`1-eta=1/(4m)`,

whereas

`(1-rho_M)|alpha|=(1-1/(2m))/m>1/(8m)=(1-eta)/2`.                (4.15)

Thus the full partner gate (1.1) genuinely fails. Equivalently,

`1-eta < 2(1-rho_M)|alpha|`,                                     (4.16)

so this is a true sharpened-collar family, not merely a coarse `eta>7/8` example.

Every complementary transverse row is light. For a mixed row,

`||w_j||^2=(2eta/m)cos(phi_j)^2+(1/m)sin(phi_j)^2<2/m<=1/64`,     (4.17)

and the pure rows are smaller. Hence the fleet03/B10 r25 transverse-heavy exit (`>=1/4`) is also absent.

The newest-Claude ruled theorem nevertheless gives, for every admissible product input law,

`boxed: ess sup_(t>=0) p_(X^T A_m X)(t) <= pi sqrt(2).}`          (4.18)

Only the two-sheet side remains a stress test.

### 4.2 Every local physical certificate collapses

Since `Lambda_m` is orthogonal,

`|x^T Lambda_m x|<=||x||^2`.                                     (4.19)

The hub squared norm is `<1`; every nonhub row has squared norm at most `2/m` (for the mixed rows the maximum is exactly `2/m`). Therefore

`boxed: max_i |(A_m)ii| <=2/m.`                                  (4.20)

For two physical rows `x,y`,

`det [[x^T Lambda x,x^T Lambda y],[y^T Lambda x,y^T Lambda y]]
 =<x wedge y,(wedge^2 Lambda)(x wedge y)>`,                       (4.21)

and `||wedge^2 Lambda_m||op=1`. Hence

`boxed: max_(i<j)|det A_m[{i,j},{i,j}]| <=2/m.`                  (4.22)

For any physical triple `S`, exact rank three gives

`|det A_m[S,S]|=det(R_{m,S})^2`,                                 (4.23)

so Hadamard yields

`boxed: max_(|S|=3)|det A_m[S,S]| <=4/m^2.`                      (4.24)

Thus no uniformly good physical pivot, pair, or triple survives.

### 4.3 The mixed bank is genuinely noncollinear

Every mixed row has the same strictly positive `e` coefficient `1/(sqrt(2)m)`. If two mixed rows were collinear, comparing their `e` components would force the scalar multiple to be one, and then their transverse vectors would be equal. Distinct roots of unity give distinct transverse vectors. Hence every collinear subset of mixed rows has cardinality one.

The only nontrivial collinear original-coordinate banks are therefore the pure `e`, pure `v`, and pure `u` banks (plus singleton mixed rows). Their maximal aggregate squared row norms are

`e-bank <1`, `u-bank=1/2`, `v-bank=1/(4m)`,                      (4.25)

while a singleton mixed row has squared norm at most `2/m`.

For ANY three disjoint exact-collinear product banks, Hadamard therefore gives

`boxed: w_col:=det(tilde r_1,tilde r_2,tilde r_3)^2 <=1/m.}`      (4.26)

Indeed the largest possible product is attained in scale by the pure `e`, pure `u`, and one mixed singleton: `<1*(1/2)*(2/m)=1/m`; every other combination is smaller.

Hence the preceding B10 scalar collinear-bank theorem would pay this family only with a cost proportional to `w_col^(-1/3)>=m^(1/3)`. Exact collinear compression is therefore NOT an exhaustive true-collar mechanism.

### 4.4 Yet the aggregate noncollinear hub packet is constant

For the mixed bank,

`det H=eta/2`.                                                     (4.27)

Its total hub-incident packet is

`sum_(j<k; j,k in M) det(r_0,r_j,r_k)^2
 =c det H
 =c eta/2`,                                                       (4.28)

which tends to `1/2` as `m->infinity`.

Theorem 2.1 supplies a deterministic partition `M=Y disjoint_union Z` with

`sum_(j in Y,k in Z) det(r_0,r_j,r_k)^2
 >=c eta/4`.                                                      (4.29)

For `m>=128`,

`c eta/4 >= (127/128)(511/512)/4
 =64897/262144
 >0.2475.`                                                        (4.30)

Thus the source-valid geometric resource remains uniformly positive even while every scalar pivot, physical pair, physical triple, and exact-collinear three-bank determinant tends to zero.

This family is NOT a counterexample to QFORM. It is a counterexample to the local/scalar-bank reduction strategy in the exact unpaid collar.

## 5. What the new result changes

The live near-coloop proof obligation now splits cleanly.

### Chamber A: `theta>=1/16`

The existence problem is solved at the source level. There is a singleton physical hub plus two disjoint ORIGINAL-coordinate vector banks with a universal aggregate Pluecker packet, equation (2.4). The family in Section 4 shows this chamber cannot in general be collapsed to finitely many exact-collinear scalar banks or one good physical minor.

The first unpaid theorem here is

`QFORM-HUB-TWO-VECTOR-BANK-CURVATURE-RECEIVER-v1`:

> For an exact-rank-three indefinite form in the true collar, prove a uniform two-sheet density estimate from a fixed lower bound on
> `sum_(j in Y,k in Z) det(r_0,r_j,r_k)^2`, where `{0}`, `Y`, and `Z` are disjoint original-coordinate sources, while retaining every same-bank longitudinal/transverse term.

The receiver may not replace a vector bank by independent spectral coordinates, may not take a worst conditional projection-density supremum, and may not select one reciprocal minor from the packet. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction also forbids using only generic line-marginal control on the two-sheet side.

### Chamber B: `theta<1/16`

Equations (3.3)--(3.5) give a crossed near-collinear coefficient geometry:

- mixed coordinates carry almost all of the `v` direction and less than `1/16` total `u` energy;
- the disjoint pure-transverse coordinates carry more than `15/16` of the `u` direction and only `<2|alpha|` of the `v` direction.

The exact endpoint with zero wrong-direction energy is covered by the earlier scalar-bank compression theorem. The first unpaid theorem here is a nonperturbative crossed-bank interpolation: absorb positive but arbitrarily small wrong-direction energy without treating it as a small random quadratic perturbation on unbounded inputs.

These are mathematically different debts. A successful proof can now attack the vector-bank receiver and the near-collinear interpolation separately rather than treating all noncollinear mixed leakage as one undifferentiated case.

## 6. Source-validity notes

1. The ruled estimate (1.3)/(4.18) is used only on its proved one-sheet side. No conclusion is drawn from it for `t<0`.
2. All independence statements concern disjoint sets of ORIGINAL input coordinates. No spectral rotation is declared independent.
3. The random two-colour argument is only an existence proof for a deterministic partition of original indices; it does not randomize the input law.
4. The stress family has exact Parseval frame and exact spectrum `{-1,1,1}` for every `m`; the asymptotic statements are only about the collapse of candidate certificates.
5. No moment, support, or regularity assumption beyond one-dimensional density cap one is used.
6. The full exact-rank-three theorem remains OPEN, and the arbitrary-rank full QFORM theorem remains OPEN.

## 7. Deterministic regression checks

Independent numerical algebra checks were run locally for `m=128,256,512` only as regression diagnostics, not as proof. They confirmed to machine precision:

- `Lambda_m` eigenvalues `{-1,1,1}`;
- `R_m^T R_m=I_3`;
- `H=diag(eta,1/2)`;
- scalar pivots and physical pair determinants decay like `O(1/m)`;
- `c eta/4` agrees with the lower bound in (4.29).

The proof is the exact algebra above; no finite computation is used to establish the arbitrary-`m` statements.
