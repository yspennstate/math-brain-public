SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-23T11:45:11Z.
attacking: the exact two-bank near-null/null-sum endpoint; preserve product provenance through the rank-two logarithmic receiver.

# fleet02/B11 r30 — null-sum provenance obstruction and aligned near-null closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** indefinite signatures; complementary constructions/source-valid counterexamples  
**Status:** `ESSENTIAL_STEP_APPLIED / INTERMEDIATE_RECEIVER_REFUTED / TARGET-VALID SUBCLASS CLOSED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication and sources actually used

The first unpaid B11 implication was the exact shared-line-null endpoint isolated by completed partner fleet03/B11 r29. Its canonical mathematics is

`yspennstate/math-open-problems@2d86ea167ae1b16705983d4cf95198e254de6ca6`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T111415Z-fleet03-B11-QFORM-r29/REPORT.md`

with endpoint algebra in `NEAR_NULL_ADDENDUM.md`.

The partner theorem `QFORM-TWOBANK-SHARED-SQUARE-RANK2-HALFRIESZ-v1` says that for two independent planar source banks `(U,Z)` and `(V,W)`, joint density caps `M_L,M_R`, invertible symmetric `N`, and

`T=a[bZ+cW+xi(U,V)]^2 +(U,V)N(U,V)^T+affine`,

one has

`||p_T||_inf <=128 |a|^(-1/2)|det N|^(-1/4) sqrt(M_L M_R/|bc|)`.

On the exact two-plane overlap `G_S=diag(1,rho,0)`, `G_T=diag(0,1-rho,1)`, it gives for shared curvature `m_22 !=0`

`||p_Q||_inf <=128e [rho(1-rho)]^(-1/4)|det M|^(-1/4)|m_22|^(-1/4)`.  (1.1)

The partner addendum then proposed the remaining cap-only endpoint receiver

`beta U^2+2alpha V(Z+W)+2gamma UV+delta V^2+affine`, `alpha beta !=0`,

for arbitrary independent planar vectors with bounded joint densities. Section 2 below shows that this cap-only endpoint statement is false; the actual QFORM endpoint must retain stronger product-projection provenance.

The required newest-Claude source was also used at an actual inequality, not merely cited:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

Its proved Theorem A gives `||p||_inf <=6 sqrt(pi)/sigma` for a three-dimensional physical quadratic form whose three eigenvalues have modulus at least `sigma`; its proved Theorem C gives the one-sheet bound `p(s)<=pi sqrt(2)` for exact rank-three `(2,1)` forms with all three nonzero eigenvalue magnitudes at least one and `s>=0`.

## 2. Counterexample to the arbitrary-planar-cap null-sum receiver

### Proposition 2.1 — `QFORM-PLANAR-CAP-NULLSUM-FALSE-v1`

There is no universal bound on the density, or even on the small-ball ratio, of

`U^2+2V(Z+W)`

over pairs of independent planar random vectors `(U,Z)` and `(V,W)` whose planar joint densities are bounded by one.

### Proof

Fix `0<eps<=1/3`. Let `(U,Z)` have density one on

`L_eps=[0,eps] x [0,eps^{-1}]`.

The area is one. Independently, let `(V,W)` have density one on

`R_eps={ (v,w): a_eps<=v<=eps^2, 0<=w<=eps^2/v }`,
`a_eps=eps^2 exp(-eps^{-2})`.

Again the area is exactly

`int_(a_eps)^(eps^2) eps^2/v dv = eps^2 log(eps^2/a_eps)=1`.

Thus both planar densities are probability densities with exact cap one. Set

`T_eps=U^2+2V(Z+W)`.

Every point in the support satisfies

`0<=U^2<=eps^2`,
`0<=2VZ<=2eps`,
`0<=2VW<=2eps^2`.

Therefore

`P(0<=T_eps<=2eps+3eps^2)=1`.

For `eps<=1/3` this interval has length at most `3eps`, hence

`P(T_eps in [0,3eps])/(3eps)=1/(3eps) -> infinity`.              (2.1)

Consequently any density, if present, has essential supremum at least `1/(3eps)`. This disproves the proposed cap-only null-sum receiver.

The quadratic matrix of `T_eps` in the four variables `(U,Z,V,W)` is

`H=[[1,0,0,0],[0,0,1,0],[0,1,0,1],[0,0,1,0]]`,

with exact spectrum

`{1,sqrt(2),0,-sqrt(2)}`.                                       (2.2)

Thus even the spectral shape is precisely a three-large-eigenvalue indefinite one. This is **not** a QFORM counterexample: within the first planar bank `U,Z` are dependent and within the second `V,W` are dependent. It is a source-valid counterexample only to discarding the original product-projection provenance. The construction also uses unbounded support in `W`; that is intentional, because neither the proposed receiver nor QFORM permits a hidden support or moment bound.

The failure mechanism is transparent: the cap-one planar law can place almost all `U` at scale `eps` while spreading `Z` to scale `eps^{-1}`, and the independent second bank can correlate `W` with the reciprocal of a very small `V`. A planar `L^infinity` cap alone does not prevent the two products `VZ` and `VW` from being simultaneously `O(eps)`.

## 3. A target-valid aligned null-sum family is uniformly bounded

The preceding obstruction is exactly about lost provenance, not the spectral form. To demonstrate the difference, consider genuinely independent original coordinates `X_1,...,X_4`, each with density at most one, and for real `c` put

`Y=X_2+X_3`,
`Q_c=X_1^2 +(c/2)Y^2 +2Y X_4`.                                  (3.1)

Since `Y` uses coordinates disjoint from `X_1,X_4`, the three scalars `(X_1,Y,X_4)` are independent. Young's inequality gives

`||p_Y||_inf=||f_2*f_3||_inf <=||f_2||_inf ||f_3||_1 <=1`.       (3.2)

So the grouped variable retains a genuine cap-one product law.

In the original four coordinates, (3.1) has matrix

`A_c=[[1,0,0,0],
      [0,c/2,c/2,1],
      [0,c/2,c/2,1],
      [0,1,1,0]]`,                                               (3.3)

with exact spectrum

`{1,0,(c+sqrt(c^2+8))/2,(c-sqrt(c^2+8))/2}`.                    (3.4)

Hence for `|c|<=1` it is a genuine target instance: there are two positive and one negative eigenvalues, all of magnitude at least one. Negating the form gives the sign-dual `(1,2)` case.

### 3.1 Completed partner fleet03/B11 applied

Use the Parseval frame

`r_1=e_1`, `r_2=e_2/sqrt(2)`, `r_3=e_2/sqrt(2)`, `r_4=e_3`

and spectral matrix

`M_c=[[1,0,0],[0,c,sqrt(2)],[0,sqrt(2),0]]`.                     (3.5)

For the cut `S={1,2}`, `T={3,4}`,

`G_S=diag(1,1/2,0)`, `G_T=diag(0,1/2,1)`,

and the physical cross block is

`A_{S,T}=[[0,0],[c/2,1]]`,                                      (3.6)

which has rank exactly one. Thus this is precisely the partner r29 cross-collapse geometry with `rho=1/2`, `m_22=c`, and `det M_c=-2`. For every `c!=0`, (1.1) yields the concrete target inequality

`||p_(Q_c)||_inf <=128 e 2^(1/4) |c|^(-1/4)`.                    (3.7)

This is an actual application of the completed designated partner theorem. Its blow-up as `c->0` is a limitation of that shared-square receiver, not evidence of blow-up of `Q_c`.

### 3.2 Pinned Claude result closes the aligned near-null interval uniformly

After the source-preserving grouping in (3.1), the three-dimensional quadratic matrix in independent cap-one coordinates `(X_1,Y,X_4)` is

`B_c=[[1,0,0],[0,c/2,1],[0,1,0]]`.                               (3.8)

Its eigenvalues are

`1`, and `c/4 +/- sqrt(1+c^2/16)`.

For `|c|<=1`, every eigenvalue has modulus at least

`sigma_0=(sqrt(17)-1)/4`.                                        (3.9)

Applying the proved Theorem A from the pinned `e5f71d79.../COUNTEREXAMPLE_SEARCH.md` gives

`boxed: ||p_(Q_c)||_inf <= 6 sqrt(pi)/sigma_0
                         =24 sqrt(pi)/(sqrt(17)-1)
                         <13.621 }`                               (3.10)

uniformly for the entire target-valid interval `|c|<=1`, including the exact null endpoint `c=0`.

Thus the partner's `|c|^{-1/4}` loss can be removed in this aligned realization only because the actual original product source lets us aggregate `X_2+X_3` **before** paying any reciprocal curvature.

### 3.3 Sign-specific ruled bound on the one-sheet side

For `|c|<=1`, the original matrix (3.3) is exact rank three with signature `(2,1)` and all nonzero eigenvalue magnitudes at least one. The proved ruled Theorem C in the same pinned Claude source therefore gives directly

`boxed: p_(Q_c)(s) <= pi sqrt(2),  s>=0. }`                       (3.11)

This is the one-sheet side. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids extending (3.11) to `s<0` from line-integral control alone. The product-preserving grouped bound (3.10) pays the opposite two-sheet side as well. For `-Q_c`, the roles of the two sides are reflected and the same constants hold.

## 4. The rank-two logarithm is retained, and the third direction is identified exactly

At the null endpoint `c=0`, remove the third square `X_1^2`. Then

`R_0=2Y X_4`, `Y=X_2+X_3`.                                      (4.1)

Take `X_2,X_3,X_4` independent Uniform`[-1/2,1/2]`. The density of `Y` is `h(y)=1-|y|` for `|y|<=1`. A direct product-density calculation gives, for `0<|t|<1`,

`p_(R_0)(t)=int_(|t|)^1 (1-y)/y dy
           =log(1/|t|)-1+|t|`,                                  (4.2)

so the opposite-sign rank-two core has the required logarithmic divergence.

Now restore the independent third direction `X_1^2`. The rank-two form in independent cap-one variables `(Y,X_4)` has matrix

`N_c=[[c/2,1],[1,0]]`, `det N_c=-1`                              (4.3)

for every `c`. The completed orientation-free rank-two affine half-Riesz theorem (`QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, source `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`) gives

`sup_t E |(c/2)Y^2+2YX_4-t|^(-1/2) <=128`.                       (4.4)

For any cap-one `X_1`, the density of `X_1^2` is bounded by `u^(-1/2) 1_{u>0}`. Hence conditioning on the rank-two saddle gives

`p_(Q_c)(t)
 <=E[(t-R_c)_+^(-1/2)]
 <=128`.                                                         (4.5)

Equation (4.5) holds for every real `c`; (3.10) is the sharper pinned-Claude bound in the target interval.

This is the precise third-direction mechanism in the aligned null-sum chamber: the rank-two saddle remains logarithmically singular; the independent square does not make that rank-two density bounded. Instead it asks for the half-order Riesz potential of the saddle, which is finite. The product grouping `Y=X_2+X_3` is what makes the receiver legitimate. Proposition 2.1 shows that replacing this provenance by an arbitrary bounded planar joint density destroys the conclusion completely.

## 5. Exact corrected remaining implication

The completed fleet03/B11 r29 nonzero-shared-curvature theorem remains valid and useful. What is false is only its proposed next **cap-only** null-sum abstraction.

The corrected first unpaid implication is

`QFORM-TWOPLANAR-NULLSUM-PRODUCT-PROJECTION-v1`:

> In the exact two-plane overlap endpoint `m_22=0`, exploit that each planar bank is an orthogonal projection of an original-coordinate product measure, with its actual frame coefficients and disjoint-bank independence. Prove a uniform null-sum half-Riesz/ruled estimate, or route the frame quantitatively to an already-paid grouped-coordinate, physical-pair, hub, ridge, or volume exit. It is not enough to retain only a planar joint-density cap.

A useful target for the next step is to recover, from the two planar projection frames, a layer-cake or Brascamp-Lieb estimate that plays the role of the exact scalar grouping in Section 3 without asserting independence between the two coordinates inside either projected bank.

This report does not solve arbitrary additional spectrum beyond the exact-rank-three core and does not prove the full QFORM conjecture. Essential boundedness is proved only in the stated target-valid aligned family. Continuity remains separate.
