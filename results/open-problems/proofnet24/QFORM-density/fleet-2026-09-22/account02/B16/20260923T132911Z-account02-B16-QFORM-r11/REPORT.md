SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-23T13:29:11Z.
attacking: the true near-null shared-bank endpoint by testing the opposite-sign scalar Schur route, then the full-leaf mixed-hub/cross-volume routes in the partner's true near-coloop survivor while retaining original-product provenance.

# account02/B16 r11 — two-sided square-peel logarithm and near-coloop spectral-certificate barrier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW ROUTE OBSTRUCTIONS + EXACT STRUCTURAL IDENTITIES / FULL QFORM OPEN`  
**Regularity:** the supporting positive bounds cited below establish essential boundedness in their stated scopes; continuity is not claimed here except where a cited theorem itself supplies it.

## 1. Scope and sources

The owner target is unchanged: for every finite `n`, arbitrary independent real original-coordinate inputs with probability densities at most one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal essential density bound for `X^T A X`, or give a valid counterexample. No support, moment, log-concavity, identical-law, diagonal-basis, or post-rotation-independence hypothesis is used below.


`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed results used below are Theorem F, Theorem H / mixed-Fresnel, Theorem D/D', D5, and the two-dimensional product-marginal/ruled interface at their exact stated scopes.

The newest designated partner read in this run is account03/B16 r29,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T132339Z-account03-B16-QFORM-r29/REPORT.md`.

It proves that after its paid exact-rank-three exits, the true near-coloop survivor has a hub leverage `c>63/64`, all physical diagonals `<1/64`, all hub-star atoms `<1/16`, normalized star masses `<1/251`, and at least 80 disjoint original-coordinate star banks. Its remaining debt is the same-side curvature of those banks.

## 2. First obstruction: the opposite-sign scalar Schur remainder still loses a logarithm

Fix even `m>=4`, balanced signs `epsilon_j in {+1,-1}`, and

`Y=m^(-1/2) sum_j X_j`, `Z=m^(-1/2) sum_j epsilon_j X_j`

for independent original coordinates with densities bounded by one. For `0<eta<=1`, put

`c_eta=sqrt(1+eta)`,

`Q_eta=-eta X_0^2+2 c_eta X_0 Y+Z^2`.                           (2.1)

On the orthonormal aggregate span `(X_0,Y,Z)` the coefficient matrix is

`M_eta=[[-eta,c_eta,0],[c_eta,0,0],[0,0,1]]`,

whose nonzero spectrum is exactly

`{1,1,-(1+eta)}`.                                                (2.2)

Thus (2.1) is a strict target family.

Before Schur completion, the pinned mixed-Fresnel theorem applies directly to the original leaf factors. Its augmented rows are

`w_j=(c_eta/sqrt(m), epsilon_j/sqrt(m))`,

with Gram `diag(1+eta,1)` and normalized leverage `2/m<=1/2`. Hence

`boxed: ||p_(Q_eta)||_infinity
 <=3*2^(4/3)*(1+eta)^(-1/3)
 <=7.559526300... .`                                             (2.3)

No independence between `Y` and `Z` is inferred.

Now complete the negative hub pivot:

`Q_eta=-eta (X_0-c_eta Y/eta)^2+R_eta`,

`R_eta=((1+eta)/eta)Y^2+Z^2`.                                   (2.4)

If one retains only the source height bound `f_0<=1`, the exact translation-uniform square envelope at level zero is

`K_eta(0)=eta^(-1/2) E[R_eta^(-1/2)]`.                          (2.5)

Take `m=4`, signs `(+,+,-,-)`, and iid leaf inputs `Unif[-1/2,1/2]`. With

`A_+=(X_1+X_2)/2`, `A_-=(X_3+X_4)/2`,

one has `Y=A_++A_-`, `Z=A_+-A_-`. The genuine dependent projected pair has exact density

`rho(y,z)=(1/2)p((y+z)/2)p((y-z)/2)`,

`p(u)=2(1-2|u|) 1{|u|<=1/2}`.                                  (2.6)

Its support is a diamond, not a product set. On `|y|,|z|<=1/8`, `rho>=9/8`. Writing `L=(1+eta)/eta`, a direct rectangle integral gives

`K_eta(0)
 >=[9 sqrt(2)/(64 sqrt(1+eta))] log L`.                         (2.7)

Therefore

`boxed: K_eta(0)->infinity as eta downarrow0.`                   (2.8)

The earlier B16 calculation gave the analogous logarithmic loss when the Schur remainder was indefinite. Equation (2.8) proves that changing the sign so that the rank-two remainder is positive definite does not repair scalar square peeling. The lost quantity is the translating original-coordinate hub density itself. This is a certificate obstruction, not a QFORM counterexample, because the true density stays bounded by (2.3).

## 3. Exact rank-jump identity for a near-coloop leaf block

The partner r29 survivor suggests trying the pinned hub Fresnel theorem on several diffuse banks. The following exact identity shows a necessary limitation of that idea.

Let an exact-rank-three form be

`A=R Lambda R^T`, `R^T R=I_3`,                                  (3.1)

with `Lambda` invertible, and let physical coordinate `0` have spectral row

`r_0=sqrt(c)e`, `||e||=1`, `0<c<1`, `a=1-c`.                    (3.2)

Let `L` denote all remaining physical coordinates and set

`G=R_L^T R_L=I_3-c ee^T`,                                      (3.3)

`B=A_LL=R_L Lambda R_L^T`,

`g=A_L0=sqrt(c) R_L Lambda e`,

`d=A_00=c e^T Lambda e`.                                       (3.4)

Because `a>0`, `G` is positive definite and `det G=a`. Put

`K=G^(1/2) Lambda G^(1/2)`.                                    (3.5)

Then `R_L G^(-1/2)` has orthonormal columns, so the three nonzero eigenvalues of `B` are exactly those of `K`. In particular

`boxed: pdet(B)=det K=a det Lambda.`                             (3.6)

Moreover `Range(B)=Range(R_L)` and `g` belongs to this same range. The unique range solution of `Bx=g` is

`boxed: B^+ g=(sqrt(c)/a) R_L e.`                               (3.7)

Indeed, using `G e=a e`,

`B[(sqrt(c)/a)R_L e]
 =R_L Lambda G[(sqrt(c)/a)e]
 =sqrt(c)R_L Lambda e=g`.

Equations (3.3) and (3.7) also give

`boxed: ||B^+g||^2=c/a,`                                       (3.8)

and

`boxed: g^T B^+ g=d.`                                           (3.9)

Thus the generalized Schur complement of the complete leaf block is identically zero:

`d-g^T B^+g=0`.                                                  (3.10)

The coefficient needed to express the hub star inside the leaf-curvature range has norm `sqrt(c/a)`, which diverges at the true-coloop boundary.

### Theorem `QFORM-EXACT-R3-HUB-AUGMENTED-RANK-DEFECT-v1`

More generally, for **any** leaf subset `I` with `rank(R_I)=3`, put `B_I=R_I Lambda R_I^T` and `g_I=A_I0`. Then

`rank(B_I)=3`, `Range(B_I)=Range(R_I)`, and `g_I in Range(B_I)`. (3.11)

Consequently, if one diagonalizes all three modes of `B_I` as `B_I=V diag(mu_1,mu_2,mu_3)V^T`, the augmented Gram in the pinned hub theorem H is

`G_tilde=[[I_3,V^T g_I],[g_I^T V,||g_I||^2]]`,                 (3.12)

and

`boxed: det G_tilde=0.`                                         (3.13)

Hence Theorem H cannot gain a new full hub direction by linearizing **all** rank-three curvature on such a bank: the hub coupling is algebraically already in that curvature range. This is not a failed leverage estimate; the augmented determinant is exactly zero. A successful hub-Fresnel application must expose lower-rank-plus-diagonal leaf structure, or leave some same-side curvature to a separately paid product-preserving mechanism.

## 4. Exact cross-volume factorization and a second near-coloop barrier

The same Parseval geometry gives an exact obstruction to paying the determinant-one near-coloop collar solely by the pinned rank-three cross-volume theorem.

For any two disjoint original-coordinate sets `I,J`, let

`M=A_IJ=R_I Lambda R_J^T`,

`G_I=R_I^T R_I`, `G_J=R_J^T R_J`.                              (4.1)

Cauchy--Binet, applied first to each physical `3x3` minor and then to the two frame restrictions, gives the exact identity

`boxed:
 Z_3:=e_3(M^T M)
 =det(G_I) det(Lambda)^2 det(G_J).`                              (4.2)

Proof: for physical triples `S subset I`, `T subset J`,

`det(M_ST)=det(R_S) det(Lambda) det(R_T)`,

and summing the squared determinants factorizes into the two Cauchy--Binet sums.

Because `I` and `J` are disjoint, at least one of them excludes the hub `0`. For any set `S` excluding the hub,

`G_S<=R_L^T R_L=I-cee^T`,

so determinant monotonicity gives

`det G_S<=a`; every coordinate Gram is at most `I`, hence the other determinant is at most one. Therefore

`boxed: Z_3<=a det(Lambda)^2.`                                  (4.3)

In the important determinant-one target subclass `|det Lambda|=1`, every disjoint physical cross block therefore satisfies

`boxed: Z_3<=a.`                                                 (4.4)

The pinned Theorem D and its D' marginal relaxation both have the reciprocal factor `Z_3^(-1/6)`. Thus their **formula itself** cannot produce a near-coloop-uniform constant on this determinant-one subclass by changing the coordinate cut: the best possible right side still pays at least the scale `a^(-1/6)`. The pinned D5 route is identically unavailable in exact rank three because every cross block has rank at most three and hence `e_5(M^T M)=0`.

Again, (4.4) is a barrier to these certificate currencies, not a lower bound on the true density.

## 5. A source-valid witness showing the certificate singularity is not density blow-up

The fully shared Walsh family from the preceding B16 report makes the distinction explicit. For `0<a<1/64`, `c=1-a`, `m` divisible by four, balanced sign pairs `(epsilon_j,tau_j)`, set

`r_0=(sqrt(c),0,0)`,

`r_j=m^(-1/2)(sqrt(a),epsilon_j,tau_j)`,                         (5.1)

and

`Lambda=[[0,1,0],[1,0,0],[0,0,1]]`.                            (5.2)

Then `R^T R=I_3`, `|det Lambda|=1`, and the nonzero physical spectrum is exactly `{1,-1,1}`. With

`L=m^(-1/2)sum X_j`, `U=m^(-1/2)sum epsilon_j X_j`, `T=m^(-1/2)sum tau_j X_j`,

`Q=2(sqrt(c)X_0+sqrt(a)L)U+T^2`.                               (5.3)

The pair `(U,T)` is a genuine two-dimensional projection of the same original leaf product law and has joint density at most two; it is not declared independent.

For `a>0`, the complete leaf block in the normalized `(L,U,T)` coordinates is

`K_a=[[0,sqrt(a),0],[sqrt(a),0,0],[0,0,1]]`,                    (5.4)

with eigenvalues `{sqrt(a),-sqrt(a),1}`. Thus the full-leaf hub augmented Gram is singular by (3.13), while the pinned Theorem F, whose normalized leaf leverages are exactly `3/m`, gives only

`||p_Q||_infinity<=12 a^(-1/3)`.                                (5.5)

At the exact coloop endpoint `a=0`, however,

`Q_0=2X_0U+T^2`,                                                 (5.6)

and the pinned mixed-Fresnel theorem has augmented Gram `I_2` and leverage `2/m`; it gives

`boxed: ||p_(Q_0)||_infinity<=3*2^(4/3)<7.56.`                  (5.7)

For every `a in (0,1/64)`, the previous B16 source-plane/source-line regrouping of the **original sign banks** applies account03/B16 r27 and gives instead

`boxed: ||p_Q||_infinity<27.015`                                (5.8)

uniformly in `m`, `a`, and all independent cap-one source laws. Thus the divergence/singularity of (3.13), (4.4), and (5.5) is not a true-density phenomenon; regrouping original sources before curvature removes it.

## 6. Application to the latest designated partner and the next unpaid implication

Account03/B16 r29 converts the true near-coloop survivor into 80 independent original-coordinate star banks, each carrying a quantitative amount of hub-star energy. Sections 3-4 show two things that this bank compiler must respect:

1. if a chosen bank has full spectral row rank three and one tries to linearize all of its rank-three same-side curvature together with the hub, the pinned hub-Fresnel augmented determinant is exactly zero;
2. on determinant-one exact-rank-three forms, no rearrangement of disjoint coordinate cuts can make the rank-three cross-volume currency uniformly nondegenerate as `a=1-c` tends to zero.

Therefore the first unpaid B16 implication is sharpened to

**`QFORM-SUPERDIFFUSE-BANK-LOWRANK-OR-CROSSBANK-TRANSDUCER-v1`.**

Starting from the partner's 80 disjoint source banks, prove one of the following with universal quantitative constants:

- extract a bank/union with lower-rank-plus-diagonal leaf curvature and an augmented hub direction not already in its curvature range, so the pinned mixed-Fresnel theorem genuinely applies; or
- retain several full-rank banks simultaneously and pay their same-side curvature with a source-preserving cross-bank/product-marginal transducer before taking absolute values.

A bounded two-dimensional projected density is admissible input to such a transducer, but it must not be upgraded to projected independence or a uniform conditional density. Small leaf coefficients also cannot be deleted on arbitrary unbounded inputs.

The exact-rank-three problem is still open after this sharpening, and arbitrary additional spectrum remains a separate full-target interface.
