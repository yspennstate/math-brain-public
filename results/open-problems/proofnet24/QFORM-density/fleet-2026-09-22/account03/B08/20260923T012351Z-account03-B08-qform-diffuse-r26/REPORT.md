SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T01:23:51Z.
attacking: consume the q=1,2,3 aggregate Pluecker-overlap packets from r25 without selecting a tiny local minor, by exact shared-coordinate determinant expansions and an aggregate deshearing inequality.

# account03/B08 r26 — overlap-packet monomial compiler and aggregate q=1 deshearing

**Run:** `20260923T012351Z-account03-B08-qform-diffuse-r26`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control followed:** revision `2026-09-22.15` (later than the historical `.5` embedded in the scheduled prompt)  
**Assignment:** diffuse eigenvector case  
**Classification:** `PROVED SUPPORTING TARGET-RELEVANT THEOREMS / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source-valid inputs

The full owner target remains open. Inputs are independent original real coordinates with probability densities at most one; no moment, support, Gaussian, log-concavity, iid, connected-support, diagonal-basis, or independence-after-rotation hypothesis is added. Continuity is stated only in branches where an integrable characteristic-function estimate proves it.

The live correction ledger was reread. In particular, this report does not use law-uniform pointwise quadratic stationary phase, arbitrary-joint rank-three coarea, positive conditional projection-density moments, fiber suprema, a fixed good physical minor, or any near-zero-as-zero perturbation. The entire point of the new compiler is to retain the aggregate bank mass **before** reciprocal local payment.

The immediate input is own r25,

`yspennstate/math-open-problems@d30dba6db19d1eceabde6222c84a5b57a85506f0`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T002108Z-account03-B08-qform-diffuse-r25/REPORT.md`.

If `R` consists of three orthonormal genuine eigenvectors, `AR=R Lambda`, `min_j |lambda_j|>=L`, and

`mu=max_i ||R_{i,*}||_2^2 <=1/48`,

r25 proves that one of the following **disjoint original-coordinate** packets exists:

* q=0: six banks with squared third-minor mass `P0>=L^6/2304`;
* q=1: five banks `H,R1,R2,C1,C2` with `P1>4L^6/9375`;
* q=2: four banks `H1,H2,R,C` with `P2>L^6/384`;
* q=3: three banks `H1,H2,H3` with `P3>2L^6/27`.

The bank selection is the completed account03/B07 overlap-coloring theorem; an immutable source containing the exact Schur ledger is

`yspennstate/math-open-problems@f27ca4fcb70a4608efe9d4007cf774a7a1fb942d`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T000734Z-account03-B07-qform-r20/REPORT.md`.

A fresh same-assignment result used below is account01/B08 `QFORM-RANKR-PHYSICAL-CROSS-L2-v1`, immutable source

`yspennstate/math-open-problems@f97aa31585b7b547a116d4580f898576af4e0842`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T004211Z-account01-B08-qform-r21/REPORT.md`.

For an original-coordinate cross block `B` of exact rank `r>=3`, it gives, with arbitrary same-side quadratic curvature and arbitrary conditioned outside couplings,

`||p_Q||_infinity <= [2r/(r-2)] (prod_(nu=1)^r s_nu(B))^(-1/r)`,

and a continuous `C_0` density.

The designated partner `account04/B08` still has no completed current-QFORM handoff at the fresh lookup, so none is fabricated. A compatible completed account04 result actually used below is account04/B18, source

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

Its sharp product-projection/rearrangement input yields for a nonzero coefficient vector `u` supported on an original-coordinate bank

`||p_(u^T X)||_infinity <= sqrt(2)/||u||_2`.

On disjoint banks the two projections are genuinely independent, hence the joint cap is the product of the one-dimensional caps.

## 2. q=1 packet: aggregate deshearing without selecting the shared coordinate

Let the five banks `H,R1,R2,C1,C2` be pairwise disjoint and put

`D=A[R1 union R2, C1 union C2]`.

For `h in H`, set

`b_h=A_hh`,
`kappa_h(r)=A_rh` for `r in R1 union R2`,
`rho_h(c)=A_hc` for `c in C1 union C2`.

For `r1 in R1`, `r2 in R2`, `c1 in C1`, `c2 in C2`, define

`C[r1,r2;c1,c2]
 =D[r1,c1]D[r2,c2]-D[r1,c2]D[r2,c1]`.

The actual q=1 minor is exactly

`T_h[r1,r2;c1,c2]
 = b_h C[r1,r2;c1,c2]
   -rho_h(c1) kappa_h(r1) D[r2,c2]
   +rho_h(c1) kappa_h(r2) D[r1,c2]
   +rho_h(c2) kappa_h(r1) D[r2,c1]
   -rho_h(c2) kappa_h(r2) D[r1,c1].`                 (2.1)

Let

`P1=sum_h ||T_h||_F^2`,
`B2=sum_h b_h^2`,
`C2split=||C||_F^2`,

and abbreviate

`K_(h,e)^2=sum_(r in Re) A_rh^2`,
`R_(h,d)^2=sum_(c in Cd) A_hc^2`,
`F_(e,d)^2=sum_(r in Re,c in Cd) A_rc^2`,

for `e,d in {1,2}`. Write `bar 1=2`, `bar 2=1`.

### Theorem 2.1 — `QFORM-Q1-AGGREGATE-DESHEAR-COMPILER-v1`

One of the following two alternatives holds:

`boxed: B2*C2split >= P1/4`,                                      (2.2)

or there exist `e,d in {1,2}` such that

`boxed:
 F_(bar e,bar d)^2
 sum_(h in H) K_(h,e)^2 R_(h,d)^2
 >= P1/64.
`                                                                  (2.3)

#### Proof

View the tensors `(T_h)_h`, `(b_h C)_h` and the four-term remainder `(G_h)_h` as vectors in the direct Hilbert sum over `h`. Equation (2.1) says `T=bC+G` up to an irrelevant sign convention. Therefore

`||G|| >= ||T||-||bC||
       =sqrt(P1)-sqrt(B2*C2split).`                                 (2.4)

If (2.2) fails, (2.4) gives `||G||^2>P1/4`.

Each coordinate of `G_h` is a sum of four scalar monomials. Hence

`|G_h|^2 <=4(sum of the four monomial squares)`.                    (2.5)

After summation over all indices, each one of the four monomial energies factors exactly. For example,

`sum rho_h(c1)^2 kappa_h(r1)^2 D[r2,c2]^2
 =F_(2,2)^2 sum_h K_(h,1)^2 R_(h,1)^2`,                             (2.6)

and the other three terms are the three other choices of `(e,d)`, with the core on the complementary banks. Thus the sum of the four factored energies is at least `||G||^2/4>P1/16`, so one is larger than `P1/64`. QED.

This is stronger for the current purpose than selecting one `h`: the entire shared-coordinate mass remains summed in (2.3).

### Diffuse numerical consequence

In the q=1 branch produced by r25,

`P1>4L^6/9375`.

Hence either

`boxed: B2*C2split > L^6/9375`,                                   (2.7)

or some aggregate star-star-core packet satisfies

`boxed:
 F_(bar e,bar d)^2
 sum_h K_(h,e)^2 R_(h,d)^2
 > L^6/150000.
`                                                                  (2.8)

No number of coordinates occurs in either constant.

## 3. account04 result applied to the q=1 aggregate at an actual inequality

For a fixed `h` in a star-star-core branch, put

`U_h=sum_(r in Re) A_rh X_r`,
`V_h=sum_(c in Cd) A_hc X_c`.

The banks `Re` and `Cd` are disjoint original-coordinate banks, so `U_h,V_h` are genuinely independent. The completed account04/B18 product-projection input gives the certified joint-density cap

`M_h := 2/(K_(h,e) R_(h,d))`                                      (3.1)

whenever both norms are nonzero. Therefore (2.3) implies the aggregate **density-cap currency**

`boxed:
 F_(bar e,bar d)^2 sum_h M_h^(-2) >= P1/256.
`                                                                  (3.2)

In the diffuse q=1 branch this is

`boxed:
 F_(bar e,bar d)^2 sum_h M_h^(-2) > L^6/600000.
`                                                                  (3.3)

Equation (3.2) is a real downstream use of the account04 theorem, not a citation-only regression. It still does **not** by itself bound the final indefinite quadratic pushforward: the correction ledger forbids treating a bounded projected joint density as a generic nonlinear receiver. What (3.2) does is convert the structural bank packet into an aggregate family of genuine product-projection caps without selecting a single shared coordinate. The next analytic transducer must consume this sum before reciprocal selection.

## 4. q=2 packet: five-term original-coordinate monomial compiler

Let `h1 in H1`, `h2 in H2`, `r in R`, `c in C`, with the four banks pairwise disjoint. Write

`a=A[h1,h1]`, `b=A[h2,h2]`, `x=A[h1,h2]`,
`p=A[r,h1]`, `q=A[r,h2]`, `u=A[h1,c]`, `v=A[h2,c]`, `z=A[r,c]`.

A direct determinant expansion gives

`det A[{h1,h2,r},{h1,h2,c}]
 =(ab-x^2)z-aqv-bpu+xpv+xqu.`                                     (4.1)

Define five nonnegative aggregate energies

`E20=(sum_(h1,h2)(A_h1h1*A_h2h2-A_h1h2^2)^2)
     * ||A[R,C]||_F^2`,                                            (4.2)

`E21=(sum_(h1 in H1) A_h1h1^2)
     *sum_(h2 in H2)||A[R,h2]||_2^2 ||A[h2,C]||_2^2`,              (4.3)

`E22=(sum_(h2 in H2) A_h2h2^2)
     *sum_(h1 in H1)||A[R,h1]||_2^2 ||A[h1,C]||_2^2`,              (4.4)

`E23=sum_(h1,h2) A_h1h2^2
        ||A[R,h1]||_2^2 ||A[h2,C]||_2^2`,                          (4.5)

`E24=sum_(h1,h2) A_h1h2^2
        ||A[R,h2]||_2^2 ||A[h1,C]||_2^2`.                          (4.6)

### Theorem 4.1 — `QFORM-Q2-MONOMIAL-PACKET-COMPILER-v1`

If `P2` is the q=2 packet mass, then

`boxed: max(E20,E21,E22,E23,E24) >= P2/25.`                         (4.7)

#### Proof

Apply `|t1+...+t5|^2<=5 sum |tj|^2` to (4.1), sum over all four bank indices, and use the disjoint-index factorisations shown in (4.2)-(4.6). If every `E2j<P2/25`, their sum would be `<P2/5`, contradicting `P2<=5 sum_j E2j`. QED.

For the diffuse r25 q=2 packet,

`P2>L^6/384`,

so one of the five fully original-coordinate energies obeys

`boxed: E2j > L^6/9600.`                                           (4.8)

Again there is no local-minor or bank-cardinality loss.

## 5. q=3 packet: principal determinant energy becomes five aggregate currencies

For `h1 in H1`, `h2 in H2`, `h3 in H3`, write

`a=A[h1,h1]`, `b=A[h2,h2]`, `c=A[h3,h3]`,
`x=A[h1,h2]`, `y=A[h1,h3]`, `z=A[h2,h3]`.

Then

`det A[{h1,h2,h3}]
 =abc+2xyz-a z^2-b y^2-c x^2.`                                    (5.1)

Define

`E30=(sum_H1 a^2)(sum_H2 b^2)(sum_H3 c^2)`,                        (5.2)

`E31=4 sum_(h1,h2,h3) x^2 y^2 z^2`,                               (5.3)

`E32=(sum_H1 a^2)(sum_(h2,h3) z^4)`,                              (5.4)
`E33=(sum_H2 b^2)(sum_(h1,h3) y^4)`,                              (5.5)
`E34=(sum_H3 c^2)(sum_(h1,h2) x^4)`.                              (5.6)

### Theorem 5.1 — `QFORM-Q3-MONOMIAL-PACKET-COMPILER-v1`

If `P3` is the q=3 packet mass, then

`boxed: max(E30,E31,E32,E33,E34) >= P3/25.`                         (5.7)

This is the same five-term Cauchy inequality applied to (5.1), followed by exact factorisation of the diagonal-square terms.

For the diffuse r25 q=3 packet,

`P3>2L^6/27`,

so one of the five aggregate currencies obeys

`boxed: E3j > 2L^6/675.`                                           (5.8)

The triangle branch `E31` is particularly useful because it records a full three-bank cycle before any physical edge is inverted.

## 6. Actual analytic payment of a coherent q=3 triangle output

The compiler itself does not assert that three arbitrary bank-to-bank matrices are coherent rank one. When they are, however, an existing aggregate theorem pays the branch with a dimension-free constant.

Assume the active q=3 triangle has the exact product-preserving form

`A[H1,H2]=alpha u v^T`,
`A[H1,H3]=beta u w^T`,
`A[H2,H3]=gamma v w^T`,                                            (6.1)

on three disjoint original-coordinate banks, with the zero/self-block and aligned-outside hypotheses of account03/B09 `QFORM-THREE-BANK-RANKONE-TRIANGLE-v1` (`yspennstate/math-open-problems@f97aa31585b7b547a116d4580f898576af4e0842`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260922T194535Z-account03-B09-QFORM-r16/REPORT.md`).

Let

`s12=|alpha|||u||||v||`, `s13=|beta|||u||||w||`, `s23=|gamma|||v||||w||`.

Then the q=3 triangle energy factorizes exactly as

`E31=4(s12*s13*s23)^2.`                                             (6.2)

If this is the winning branch in (5.8),

`s12*s13*s23
 > (L^3/2) sqrt(2/675).`                                           (6.3)

The B09 theorem therefore gives the actual density estimate

`||p_Q||_infinity
 <=2(3+log 8)(s12*s13*s23)^(-1/3)
 <33.773/L.`                                                        (6.4)

This branch establishes essential boundedness. The B09 theorem does not claim continuity here, so neither do I. Equation (6.4) is deliberately scoped: arbitrary q=3 triangle matrices need a matrix-valued aggregate receiver, which remains open.

## 7. q=0 improvement from the fresh whole-cross-block L2 theorem

The r25 q=0 packet gives a physical cross block `B` with

`Delta3(B)=sum_(|S|=|T|=3) det B[S,T]^2 >=L^6/2304.`                (7.1)

The previous r25 Fourier receiver needed a range-leverage gate because it was designed to tolerate arbitrary additional nonzero singular directions. The fresh account01/B08 theorem removes that gate when the **actual cross block has exact rank three**.

Indeed, if `rank(B)=3`, then

`Delta3(B)=(s1 s2 s3)^2`,

so (7.1) gives

`s1 s2 s3 >=L^3/48.`                                                (7.2)

Applying `QFORM-RANKR-PHYSICAL-CROSS-L2-v1` at `r=3` yields

`boxed:
 ||p_Q||_infinity <=6*48^(1/3)/L <21.806/L.
`                                                                  (7.3)

The full ambient form may have arbitrary same-side quadratic blocks and arbitrary outside couplings. This branch has a continuous `C_0` density. Thus the q=0 diffuse packet is now paid in two complementary ways:

1. arbitrary cross rank, provided the r25 ridge-range leverage gate holds; or
2. no leverage gate at all, provided the actual cross block has exact rank three.

The still-unpaid q=0 bridge is precisely the higher-rank cross block with tiny extra singular directions and a failed ridge-leverage gate; coefficient truncation is not permitted under the owner hypotheses.

## 8. What changed and the next missing implication

The r25 overlap ledger reduced diffuse selected eigenvectors to four finite bank types. This run removes the first purely combinatorial obstruction in all three shared-coordinate types:

* q=1 is now either a diagonal-times-second-compound aggregate or a five-bank star-star-core aggregate, with explicit dimension-free constants and no selected shared coordinate;
* q=2 is now one of five explicit four-bank monomial energies at scale `>L^6/9600`;
* q=3 is now one of five explicit three-bank energies at scale `>2L^6/675`;
* q=0 exact-rank-three cross blocks are analytically paid with continuity and no leverage gate.

The full conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`; the full continuity conclusion remains open.

The first B08 analytic debt is now `QFORM-AGGREGATE-SHARED-PACKET-RECEIVER-v1`: consume (2.7)/(2.8), (4.8), and (5.8) **before** selecting an individual anchor or edge. In particular, the star-star-core currency (3.3) should be combined with a dependence-safe grouped half-Riesz or matrix-valued bilinear receiver; the q=3 triangle currency needs a matrix-valued extension of the coherent rank-one B09 theorem. The q=0 sibling needs a bridge between the whole-cross-block L2 theorem and ridge regularization when tiny extra singular directions are present.

## 9. Verification

`CHECKS.py` in this run directory verifies the q=1, q=2, and q=3 determinant identities on 200 random instances each and checks the exact rational constants. Its captured output ends

`QFORM_B08_R26_CHECK_PASS`.

It also records

`6*48^(1/3)=21.80544711398567...`

and the coherent-triangle constant

`33.77289244134676...`.

These computations check algebra/constants only; they are not Monte Carlo evidence for the universal theorem.
