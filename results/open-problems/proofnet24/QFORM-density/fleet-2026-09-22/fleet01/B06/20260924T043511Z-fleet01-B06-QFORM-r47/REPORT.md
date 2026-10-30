SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-24T04:35:11Z.
attacking: three-hub localized curved receiver — combine aggregate Pluecker disjoint-cross exit with a one-direction localized hub and a rank-two product half-Riesz remainder, without a largest-minor or fiber-sup step.

# fleet01/B06 r47 — anchored Pluecker tensor receiver inside the three-hub branch

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `NEW SUPPORTING PRODUCT-WEIGHTED DENSITY THEOREM / THREE-HUB HIT REFINED TO ANCHORED TENSOR OR TWO-HUB PLANE / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. Global continuity remains OPEN. This run proves essential boundedness only in the quantitative branches stated below. All random coordinates used for conditioning or product partitions are literal original coordinates. No independence after a spectral rotation, arbitrary-joint coarea estimate, pointwise van-der-Corput decay, or unrestricted fiber supremum is used.

## 1. Fresh sources and immediate predecessor

Fresh owner control at publication remains revision `2026-09-22.15`, programme revision `2026-09-22.5`, QFORM-only, with no fleet01/B06 pause. The live correction inbox still includes the required warnings that pointwise quadratic-phase decay is false for arbitrary cap-one densities, naive integrated fiber suprema can grow with dimension, and spectral rotations destroy independence. The newer balanced-energy/E3 correction is also compatible with the present argument: no rank-three physical crossing is inferred from an aggregate kernel energy.

Immediate predecessor:

`yspennstate/math-open-problems@1277453a076d5c7b711f6e3ca6d6f07aec5ebf0d`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260924T034045Z-fleet01-B06-QFORM-r46/REPORT.md`.

Its exact rank-three carrier setting is

`A=D+L`, `L=R Lambda R^T`, `R^T R=I_3`,                            (1.1)

where `D` is diagonal in the original coordinates and `Lambda` is invertible symmetric. Writing

`Delta=|det Lambda|`,                                              (1.2)

r46 defines the Pluecker probability law on literal physical triples

`mu(I)=det(R_I)^2`, `sum_(|I|=3) mu(I)=1`.                         (1.3)

It proves the compiler: either a diffuse deletion gives

`||p_Q||infinity <=6e Delta^(-1/3)`                                (1.4)

with a continuous `C_0` density, or there is a literal set `H`, `|H|<=3`, such that

`P_(I~mu){I cap H != empty}>7/8`.                                  (1.5)

The latter is the branch attacked here.

The designated completed partner input is fleet02/B06,

`yspennstate/math-open-problems@d84423f410ceb77238e5d6446aba6f428d7556d6`.

Its theorem `QFORM-ANCHORED-3MINOR-SQUARE-E2-v1` says: for a literal physical anchor `h` with scalar pivot `a=A_hh!=0` and disjoint literal banks `I,J` avoiding `h`, define

`W_h(I,J)=sum_(P subset I,R subset J, |P|=|R|=2)
             det A[{h} union P,{h} union R]^2`.                    (1.6)

Then, retaining all same-bank curvature and affine/outside terms,

`boxed:
 ||p_Q||infinity <=8 e^(1/4)|a|^(-1/4) W_h(I,J)^(-1/8).`           (1.7)

The proof of (1.7) is the partner's square peel followed by its row-gate-free E2 half-Riesz theorem. Equation (1.7) is applied below to an explicit weighted cut; it is not merely cited.

## 2. Exact anchored-minor tensor

Let `r_i in R^3` denote row `i` of `R`. Fix a physical anchor `h` and put

`r=r_h`, `c=||r||_2^2`, `d=D_hh`,
`a=A_hh=d+r^T Lambda r`.                                           (2.1)

Let `J=[n]\{h}`. For each oriented unordered pair `P={p,q} subset J`, set

`z_P=r_p cross r_q`.                                               (2.2)

Define the symmetric `3 x 3` anchored matrix

`K_h = r r^T + d Lambda^(-1)`.                                    (2.3)

### Lemma 2.1 — exact disjoint anchored-minor identity

If `P,R subset J` are two-element sets with `P cap R=empty`, then

`boxed:
 det A[{h} union P,{h} union R]
 = det(Lambda) z_P^T K_h z_R.`                                    (2.4)

#### Proof

Because `D` is diagonal and `P,R` are disjoint, the only entry of `D` inside the indicated `3 x 3` rectangular submatrix is the `(h,h)` entry `d`. Expanding in that entry gives

`det A[{h}∪P,{h}∪R]
 =det L[{h}∪P,{h}∪R] + d det L[P,R].`                              (2.5)

For the rank-three carrier,

`det L[{h}∪P,{h}∪R]
 =det(Lambda) det R_{hP} det R_{hR}
 =det(Lambda)(r.z_P)(r.z_R).`                                      (2.6)

The three-dimensional compound-matrix identity gives

`det L[P,R]
 =det(Lambda) z_P^T Lambda^(-1) z_R`.                              (2.7)

Substitution of (2.6)-(2.7) into (2.5) gives (2.4). QED.

This identity is the curved-fiber currency of the run. It packages the diagonal twist and the rank-three carrier before any inverse minor is paid.

## 3. Pair-wedge frame identity and total anchored energy

Define

`S_h=sum_(P subset J, |P|=2) z_P z_P^T`.                            (3.1)

Since `R_J^T R_J=I-r r^T`, the second compound Cauchy-Binet identity gives

`S_h=adj(I-r r^T)`.                                                 (3.2)

For a rank-one update of the identity,

`boxed:
 S_h=(1-c)I+r r^T.`                                                (3.3)

In particular,

`det S_h=(1-c)^2`.                                                  (3.4)

Define the algebraic total anchored energy

`E_h=Delta^2 sum_(P,R) (z_P^T K_h z_R)^2`,                          (3.5)

where the sum is over all ordered pair-pairs in `J`, with overlap allowed. Using (3.1),

`boxed:
 E_h=Delta^2 tr(K_h S_h K_h S_h)
    =Delta^2 ||S_h^(1/2)K_hS_h^(1/2)||_F^2.`                       (3.6)

Only the disjoint part of this energy consists of literal anchored minors of `A`; overlap is retained merely as a normalization device.

Put

`omega_h=
 [sum_(P cap R=empty) Delta^2(z_P^T K_h z_R)^2]/E_h`               (3.7)

when `E_h>0`. Thus `0<=omega_h<=1`.

## 4. Weighted product cut before reciprocal payment

Give each coordinate of `J` an independent fair label `I` or `K`. For a fixed ordered disjoint pair `(P,R)`, the event `P subset I` and `R subset K` has probability `1/16`. Hence by (2.4),

`E_partition W_h(I,K)
 = (omega_h E_h)/16`.                                               (4.1)

Therefore some literal product cut satisfies

`boxed:
 W_h(I,K)>=omega_h E_h/16.`                                        (4.2)

Now apply the designated fleet02/B06 theorem (1.7) at this actual inequality. If `a!=0`, `E_h>0`, and `omega_h>0`, then

`boxed:
 ||p_Q||infinity
 <=8 sqrt(2)e^(1/4)
   |a|^(-1/4) omega_h^(-1/8) E_h^(-1/8).`                          (4.3)

This is theorem `QFORM-ANCHORED-PLUCKER-TENSOR-DENSITY-v1`.

The order of operations is essential: the complete disjoint anchored packet is averaged over product cuts first; only after (4.2) is the inverse eighth power taken. No fiber maximum and no largest-minor selection appears.

## 5. General nonzero diagonal-twist lower bound

The determinant of `K_h` has an exact closed form:

`boxed:
 det K_h = d^2 a / det Lambda.`                                    (5.1)

For `d!=0` this is the matrix determinant lemma; the identity extends polynomially through `d=0`.

Let

`B_h=S_h^(1/2)K_hS_h^(1/2)`.                                      (5.2)

For its three singular values, AM-GM gives

`||B_h||_F^2>=3 |det B_h|^(2/3)`.                                 (5.3)

Using (3.4), (5.1), and (3.6),

`boxed:
 E_h >=3 Delta^(4/3)(1-c)^(4/3)|d|^(4/3)|a|^(2/3).`                (5.4)

Combining (4.3) and (5.4) yields the explicit branch bound

`boxed:
 ||p_Q||infinity
 <= C_gen omega_h^(-1/8)
    Delta^(-1/6)(1-c)^(-1/6)|d|^(-1/6)|a|^(-1/3),`                 (5.5)

where

`C_gen=8 sqrt(2) 3^(-1/8)e^(1/4)
     =12.6630536964... .`                                          (5.6)

The homogeneity is exactly density scale `-1`.

Thus the three-hub branch is paid whenever one localized hub has quantitative pivot, diagonal twist, non-coloop slack `1-c`, and disjoint anchored-tensor fraction. Smallness of any of these quantities is now an explicit structural residue rather than an uncontrolled fiber integral.

## 6. Zero-twist endpoint becomes a conditional Pluecker pair law

The important endpoint `d=0` admits a sharper identity. Then

`K_h=r r^T`.                                                       (6.1)

For each pair `P subset J`, put

`u_P=r.z_P=det R_{hP}`.                                            (6.2)

The rank-three projection-DPP marginal identity gives

`sum_P u_P^2=c`.                                                    (6.3)

When `c>0`, define

`nu_h(P)=u_P^2/c`.                                                  (6.4)

This is exactly the Pluecker triple law `mu` conditioned on the event `h in I`, after deleting the anchor `h` from the sampled triple.

Equations (3.6)-(3.7) now simplify to

`boxed: E_h=Delta^2 c^2,`                                         (6.5)

and

`boxed:
 omega_h=Omega_h
 =P_(P,R iid~nu_h){P cap R=empty}.`                                (6.6)

Hence (4.3) becomes

`boxed:
 ||p_Q||infinity
 <=8 sqrt(2)e^(1/4)
   |a|^(-1/4)Delta^(-1/4)c^(-1/4)Omega_h^(-1/8).`                  (6.7)

Let

`beta_j=P_(P~nu_h){j in P}`, `sum_(j!=h) beta_j=2`.                (6.8)

For two independent 2-subsets, exact inclusion-exclusion gives

`Omega_h
 =1-sum_j beta_j^2 + sum_P nu_h(P)^2
 >=1-sum_j beta_j^2`.                                              (6.9)

Therefore if

`max_j beta_j<=3/8`,                                               (6.10)

then

`sum_j beta_j^2 <= (3/8)sum_j beta_j=3/4`,                         (6.11)

so `Omega_h>=1/4`. The zero-twist diffuse-pair endpoint is therefore paid by

`boxed:
 ||p_Q||infinity
 <=8 2^(3/4)e^(1/4)
   (|a| Delta c)^(-1/4).`                                         (6.12)

The numerical front constant is `17.2757179198...`.

If (6.10) fails, choose `j` with `beta_j>3/8`. The joint Pluecker inclusion probability is

`P_mu(h,j in I)=c beta_j
 =||r_h wedge r_j||_2^2`.                                         (6.13)

Thus the failure branch has the quantitative two-hub plane localization

`boxed:
 ||r_h wedge r_j||_2^2 > 3c/8.`                                   (6.14)

This is not a large individual `3 x 3` minor claim; it is a two-coordinate carrier-plane statement obtained from the complete conditional pair law.

## 7. Apply to r46's three-hub hitting alternative

Assume r46's obstruction (1.5). Since the one-point inclusion marginal of the rank-three volume-sampling law is

`P_mu(h in I)=||r_h||^2=c_h`,                                      (7.1)

we have by the union bound

`7/8 < P_mu(I cap H !=empty) <= sum_(h in H)c_h`.                  (7.2)

Therefore some `h in H` satisfies

`boxed:
 c_h>7/(8|H|)>=7/24.`                                              (7.3)

This converts the aggregate three-hub obstruction into a genuine one-direction localized physical hub without selecting a Pluecker minor.

For this `h`, if `d_h=0`, `a_h!=0`, and its conditional pair law satisfies `max beta_j<=3/8`, then (6.12) and (7.3) give

`boxed:
 ||p_Q||infinity
 <=23.5079308554 (|a_h| Delta)^(-1/4).`                            (7.4)

If instead `max beta_j>3/8`, then (6.14) and (7.3) give a second literal coordinate `j` with

`boxed:
 ||r_h wedge r_j||_2^2 >7/64.`                                    (7.5)

For `d_h!=0`, theorem (5.5) pays the branch whenever `a_h`, `1-c_h`, `|d_h|`, and `omega_h` have quantitative floors.

Thus `QFORM-THREEHUB-HIT-PLUS-SMALLPAIR-RECEIVER-v1` is sharpened to a smaller set of explicit endpoint geometries:

- zero/near scalar pivot `a_h`;
- coloop/near-coloop `c_h near 1`;
- zero/near physical diagonal twist `d_h` together with concentrated conditional pair law;
- or a genuine two-hub carrier plane with area at least `7/64` in the exact zero-twist collision branch.

The theorem does not claim those endpoints are all paid. In particular (7.5) need not give a well-conditioned physical `2 x 2` principal block for indefinite `Lambda`; the third resource can still be coupled to the same original bank.

## 8. Exact checks

Finite arithmetic checks were used only to guard the identities, not as proof. On random Parseval `n x 3` frames and random invertible symmetric `Lambda`, the following worst observed errors over the test sample were at floating-point scale:

- disjoint anchored-minor identity (2.4): `<2e-15`;
- pair-wedge frame identity (3.3): `<3e-15`;
- determinant identity (5.1): `<3e-14`;
- conditional Pluecker normalization (6.3): `<1e-15`;
- zero-twist total-energy identity (6.5): `<3e-14`.

Random tests of (5.4) found no violation; the closest sampled ratio `E_h / RHS` was about `1.005`. The proof of (5.4) is the exact singular-value AM-GM argument, not the check.

## 9. Remaining implication

The first local unpaid implication is now

`QFORM-TWOHUB-PLANE-OR-ANCHOR-DEGENERACY-RECEIVER-v1`:

starting from the literal localized hub `c_h>7/24`, pay either the two-hub plane alternative (7.5) or the simultaneous small-pivot/near-coloop/small-diagonal-twist endpoints through an original-product curved receiver, retaining every nonzero tail. The next mechanism should condition or group the two literal hubs and aggregate the remaining third carrier direction before any reciprocal physical determinant is taken.

The full arbitrary-dimensional QFORM conjecture remains OPEN. Global continuity remains OPEN. This run's density bounds are essential `L^infinity` bounds; no continuity conclusion is claimed from the partner anchored-square/E2 endpoint.
