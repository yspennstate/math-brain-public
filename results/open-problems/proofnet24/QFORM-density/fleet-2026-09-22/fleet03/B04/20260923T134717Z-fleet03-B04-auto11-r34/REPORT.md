SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T13:47:17Z.
attacking: finite three-hub lower-compound dilution in original product coordinates, with a dimension-free estimate for a high-leverage rotated rank-three projection family.

# fleet03/B04 r34 — three-hub lower-compound Fourier compiler for a delocalized rank-three projection family

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Owner control observed:** revision 2026-09-22.15; QFORM only  
**Execution:** WITHOUT_VERIFIED_BRAIN; repository transport only  
**Full QFORM:** OPEN  
**Continuity:** proved on the family below because the characteristic function is in L1; not proved for the full target.

## 1. Corrections and completed peer theorem actually used

This run uses no law-uniform pointwise quadratic-phase decay, no post-rotation independence, no arbitrary-joint coarea lemma, no conditional projection-height moment, and no naive fiber-supremum argument.

The completed peer theorem applied at an actual inequality is fleet03/B02, `QFORM-WEIGHTED-MIXED32-FOURIER-L1-v1`, at

`yspennstate/math-open-problems@ff8ec2ee90d4846f39e728e1ca20d50c717cc894:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T085705Z-fleet03-B02-qform-r25/REPORT.md`.

For one anchor it requires, with mixture parameter theta and average order s=2+theta, a q satisfying

`1 <= q < (2+theta)/2`

and every mixed physical inclusion marginal at most q/2.

The new positive estimate uses this slot's immediately preceding proved finite-family extension `QFORM-MULTI-COMPOUND-FOURIER-MIXTURE-v1` from r33:

`yspennstate/math-open-problems@8df80736853803f472ba6662c9c4a07e7801dfdb:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T124716Z-fleet03-B04-auto11-r33/REPORT.md`.

That theorem permits finitely many fractionally allocated determinant families. If their mixture has average compound order s, row or column marginals at most q/2, and 1<=q<s/2, then

`||p_Q||_infinity
 <= [e s/((s-2q)sqrt(q))]
    [prod_l theta_l^(theta_l)]^(1/(2s))
    prod_l Z_l^[-theta_l/(2s)]`,

and the resulting density is continuous and vanishes at infinity.

The designated partner is fleet04/B04. Fresh direct lookups again found no completed current-QFORM canonical report or shared handoff for that slot, so no partner result is invented.

## 2. A continuum of genuinely rotated indefinite rank-three projection targets

Fix `h in (0,1)` and an integer `m>=1`. Let the first three rows of a `(3+4m) x 3` matrix U be

`u_1=sqrt(h)e_1, u_2=sqrt(h)e_2, u_3=sqrt(h)e_3`.

Let the four tetrahedral sign vectors be

`s_1=(1,1,1), s_2=(1,-1,-1), s_3=(-1,1,-1), s_4=(-1,-1,1)`.

For each a=1,...,4 include m identical rows

`v_{a,r}=sqrt(1-h)/(2 sqrt(m)) s_a`,  r=1,...,m.

Because `sum_a s_a s_a^T=4I_3`,

`U^T U = h I_3 + (1-h) I_3 = I_3`.

Hence

`P=UU^T`

is an orthogonal projection of rank three. On two disjoint copies of these original coordinates define

`A_{h,m} = [[0,P],[P,0]]`.

Then

`spec(A_{h,m})={+1,+1,+1,-1,-1,-1,0,...,0}`.

Thus every A_{h,m} is an exact target instance with six eigenvalues of modulus one. It is genuinely nonseparable in the independent coordinates: every heavy coordinate couples to all 4m spread coordinates. For fixed h, those heavy-to-spread coefficients are O(m^{-1/2}).

The three heavy physical leverage scores are h. Every spread row has leverage

`3(1-h)/(4m)`.

For h>=3/4 the canonical third-volume Fourier law has a physical marginal >=3/4, so the pure E3 fractional Fourier gate cannot satisfy q<3/2.

## 3. Residual second-compound law after deleting one heavy coordinate

Delete heavy coordinate 1 from both the row and column bank. The nonzero eigenvalues of the principal residual block P_{-1,-1} are

`1, 1, 1-h`.

Therefore its squared singular values are

`1, 1, (1-h)^2`,

and the full residual second-compound currency is

`E2_raw(h)=1+2(1-h)^2`.                                         (3.1)

Set

`D(h)=1+2(1-h)^2`,
`r(h)=h [1+(1-h)^2]/D(h)`.                                     (3.2)

Under the canonical squared-2x2-minor law of that residual block, each of the two undeleted heavy coordinates has inclusion marginal exactly r(h). This follows from the order-two singular-direction inclusion weight

`[1+(1-h)^2]/D(h)`

on each unit singular direction, multiplied by the heavy physical squared coordinate h.

All 4m spread coordinates are symmetric. Since second-compound marginals sum to two, each spread coordinate has marginal

`ell(h,m)=[2-2r(h)]/(4m)=[1-r(h)]/(2m)`.                       (3.3)

The same formulas hold after deleting either of the other two heavy coordinates.

## 4. One-anchor peer theorem genuinely fails on every heavy anchor at h=3/4

Take h=3/4. Then

`D=9/8`,
`r=17/24`.

Apply fleet03/B02's one-anchor weighted mixed-(3+2) theorem at a heavy anchor. The incident third-volume row law conditioned on containing that anchor has each of the two other heavy-coordinate marginals equal to 3/4: the heavy frame rows are orthogonal, so conditioning on one of them does not lower either of the other two inclusion probabilities.

Hence for any one-anchor mixing parameter `0<theta<1`, either other heavy coordinate has mixed marginal

`alpha_heavy(theta)
 = theta*(3/4)+(1-theta)*(17/24)
 = (17+theta)/24`.                                             (4.1)

The peer theorem would require a q with

`q >= 2 alpha_heavy(theta)=(17+theta)/12`

and simultaneously

`q < (2+theta)/2=(12+6theta)/12`.

These inequalities imply

`17+theta < 12+6theta`, i.e. `theta>1`,

which is impossible. Therefore the completed one-heavy mixed-(3+2) gate fails for **every heavy anchor** in this family. This is an equation-level application of the peer result, not a generic comparison.

Spread-coordinate anchors have incident third-volume currency of order m^{-2}, so they do not supply the dimension-free three-heavy resource used below.

## 5. New supporting lemma — `QFORM-THREE-HUB-LOWER-COMPOUND-DILUTION-v1`

Assume

`r(h)<3/4`.                                                     (5.1)

Equivalently,

`4h^3-14h^2+20h-9<0`.

The unique root in (0,1) is

`h_*=0.783561874946009...`,

so (5.1) holds throughout `h<h_*`, in particular on the genuinely high-leverage interval

`3/4 <= h < h_*`.

Use four fractionally allocated determinant families.

**Third-order hub family F3.** Keep only the physical 3x3 minor whose row and column triples are exactly the three heavy coordinates. Its determinant is h^3, hence

`Z3=h^6`,                                                       (5.2)

and its heavy-coordinate marginals are all one while spread-coordinate marginals are zero.

**Three second-order deletion families F2^(a).** For each heavy coordinate a=1,2,3, take every 2x2 determinant term avoiding physical row a and physical column a, but allocate coefficient 1/3 to every such term. A second-order minor can be eligible for at most all three families, so the total allocation of any determinant term is at most one. The allocated currency of each family is

`Z2=D(h)/3`.                                                    (5.3)

The normalized inclusion marginals are unchanged from Section 3.

Give F3 mixture weight theta and each F2^(a) weight `(1-theta)/3`. The average compound order is

`s=2+theta`.                                                    (5.4)

Every heavy physical coordinate has mixed marginal

`a_H(theta)=theta + [2(1-theta)/3] r(h)`.                       (5.5)

Every spread coordinate has mixed marginal

`a_L(theta)=(1-theta)[1-r(h)]/(2m) <= 1/2`.                    (5.6)

Choose the maximal positive theta that makes the heavy marginals exactly 1/2:

`theta_*(h)= [1/2-2r(h)/3]/[1-2r(h)/3]
            = [3-4r(h)]/[2(3-2r(h))]`.                         (5.7)

Condition (5.1) is exactly theta_*(h)>0. With q=1 we then have

`a_H=1/2`, `a_L<=1/2`, and `1<s/2`.

Therefore `QFORM-MULTI-COMPOUND-FOURIER-MIXTURE-v1` applies in the original independent coordinates and gives

`boxed:
 ||p_{X^T A_{h,m} X}||_infinity <= C(h)
}`                                                              (5.8)

for every m>=1 and every admissible independent cap-one product law, where

`C(h)= [e(2+theta)/theta]
       [theta^theta ((1-theta)/3)^(1-theta)]^[1/(2(2+theta))]
       [h^6]^[-theta/(2(2+theta))]
       [D(h)/3]^[-(1-theta)/(2(2+theta))]`,                     (5.9)

with `theta=theta_*(h)`.

The bound is **independent of m**. The proof gives `phi_Q in L1`, hence a continuous density vanishing at infinity.

This is a product-Fourier rearrangement estimate; no coordinate rotation of the random input is performed.

## 6. Exact h=3/4 specialization

At h=3/4,

`r=17/24`, `theta_*=1/19`, `s=39/19`.

The three residual family weights are each

`(1-theta_*)/3 = 6/19`.

The exact mixed marginals are

`heavy: 1/2`,
`spread: 21/(152m)`.

The allocated determinant currencies are

`Z3=(3/4)^6=729/4096`,
`Z2=3/8` for each of the three deletion families.

Thus

`boxed:
 ||p_{X^T A_{3/4,m}X}||_infinity
 <= 39 e * 19^(-1/78) * (16/19)^(3/13) * (4/3)^(1/13)
 = 100.311873421375... < 100.312.
}`                                                              (6.1)

This holds for every integer m>=1 and every independent input law with one-dimensional densities at most one.

As m grows, each spread leverage is `3/(16m)` and each heavy-to-spread coefficient is `sqrt(3)/(8 sqrt(m))`, yet the bound (6.1) does not deteriorate. The family therefore exhibits a dimension-free high-leverage/delocalized regime that is not paid by selecting one uniformly large local spread coefficient.

## 7. What this resolves and what remains

The result is not the full conjecture. It gives a new continuum of genuinely rotated indefinite targets, including the strict high-leverage interval `3/4<=h<h_*`, and shows concretely how three simultaneous heavy coordinates can be diluted by lower-compound product laws while preserving average Fourier order strictly above two.

The remaining full-target implication is structural: starting from an arbitrary rank-three volume law or a finite compound-hub residue produced by the fleet's E3/E4 entropy arguments, construct such a finite lower-compound allocation with dimension-free determinant currency, or route its failure into an already-paid pair/star/ridge endpoint. The present calculation suggests treating at most three >3/4 leverage coordinates simultaneously rather than recursively one at a time.

Full QFORM and full-target continuity remain OPEN.
