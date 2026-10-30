SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-24T06:47:11Z.
attacking: the exact singular-principal-pair chamber left by r45; polynomialize the whole Schur star and pay it without dividing by a physical diagonal or pair determinant.

# fleet03/B09 r46 — polynomial singular-star closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / quantitative inequalities and rigorous computations  
Run: `20260924T064711Z-fleet03-B09-QFORM-r46`  
Status: **NEW SOURCE-COMPOSED COROLLARY + LOCAL SINGULAR-PAIR CLOSURE / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

All stochastic coordinates below are literal ORIGINAL coordinates. No random-variable rotation is used. No Gaussian, moment, compact-support, connected-support, log-concavity, iid, or post-rotation independence assumption is introduced. Pointwise law-uniform quadratic-phase decay is not used.

## 1. Exact debt from r45

The same-slot predecessor is

`yspennstate/math-open-problems@4eb95514089a21f787b60af1ed9ea65610d79660`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260924T054559Z-fleet03-B09-QFORM-r45/REPORT.md`.

It polynomialized the invertible-pair Schur currencies and proved the exact Cauchy--Binet identity

`det(P^2+CC^T)=(det P)^2+sum_k ||g_k||^2+Delta^2||Pn||^2`,

but also exhibited a target-valid chamber in which every physical `2 x 2` principal pair in the three-coordinate core is singular semidefinite, so the aggregate indefinite-pair receiver is identically zero. Its next exact debt was `QFORM-SINGULAR-DEFINITE-PAIR-ROUTING-v1`.

This run closes the **exact singular-pair** part of that debt. The punctured near-singular definite case remains open.

## 2. Source theorem consumed: exact singular hub star

A fresh existing-worker source is

`yspennstate/math-open-problems@cdd0eb22227a505e827a658038a1512897c0ad56`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/fleet02-B08-20260924T034000Z-7c4f/REPORT.md`,

Theorem `QFORM-SINGULAR-HUB-STAR-HALFRIESZ-v1`.

In original physical coordinates, write a full ambient matrix as

`A=[[a,c,u^T],[c,b,v^T],[u,v,C]]`,

with `a!=0`, arbitrary symmetric `C`, arbitrary affine terms, and assume

`ab-c^2=0`.

Set

`g=v-(c/a)u`.

If `g!=0`, the theorem gives the essential density bound

`||p_Q||_infinity <= 2^(11/4) (|a| ||g||_2)^(-1/2)`.              (2.1)

The proof is product-preserving: it completes the square only in the original coordinate carrying `a`, keeps the entire light-block curvature inside the remainder, and uses original-coordinate linear anti-concentration for the star. Continuity is not asserted by that theorem.

## 3. Polynomialization removes the reciprocal physical diagonal

Define the **polynomial singular-star vector**

`H := a v - c u`.                                                   (3.1)

Then `H=a g`, so

`|a| ||g|| = ||H||`.                                                (3.2)

Thus (2.1) is exactly equivalent to the following denominator-free statement.

### Corollary 3.1 — `QFORM-SINGULARPAIR-POLYNOMIAL-STAR-v1`

Under the hypotheses of Section 2, if `H!=0`, then

`boxed:
 ||p_Q||_infinity <= 2^(11/4) ||H||_2^(-1/2).
`                                                                        (3.3)

Consequently every interval `I` satisfies

`P{Q in I} <= 2^(11/4) ||H||_2^(-1/2) |I|`.                         (3.4)

This proves an actual linear small-ball estimate. There is no reciprocal `a`, `det B`, conditional fiber cap, or square-root decoupling loss in the final statement.

The significance is algebraic: `H` is a vector of degree-two original matrix minors. It remains meaningful at the singular face and can be aggregated with the polynomial currencies from r45.

## 4. A local spectral singular-pair closure

The denominator-free form (3.3) becomes quantitative under an exact three-coordinate spectral certificate.

### Theorem 4.1 — `QFORM-LOCAL3-SINGULARPAIR-CLOSURE-v1`

Let `P=A[L,L]` be a literal original-coordinate `3 x 3` principal block of the full ambient symmetric matrix `A`. Assume

`min_{lambda in spec(P)} |lambda| >= sigma > 0`.                    (4.1)

Assume one of the three physical `2 x 2` principal pairs of `P` is singular. Then for every admissible independent cap-one input law, with completely arbitrary coefficients and curvature outside `L`,

`boxed:
 ||p_{X^T A X}||_infinity <= 8/sigma.
`                                                                        (4.2)

Hence

`boxed:
 P{X^TAX in I} <= (8/sigma)|I|
`                                                                        (4.3)

for every interval `I`. This branch proves essential boundedness. Continuity is not separately proved here.

### Proof

Relabel the singular physical pair as coordinates `1,2` and write

`P=[[a,c,u],[c,b,v],[u,v,d]]`,
`B=[[a,c],[c,b]]`,
`det B=ab-c^2=0`.                                                     (4.4)

Because (4.1) makes `P` invertible, `B` cannot be the zero matrix. A nonzero singular real symmetric `2 x 2` matrix with determinant zero is semidefinite and has one nonzero eigenvalue `tau=tr B`. Cauchy interlacing between `B` and `P` gives

`|tau| >= sigma`.                                                     (4.5)

Since `B` is rank-one semidefinite, its two diagonal entries have the same sign and

`|tau|=|a|+|b|`.                                                      (4.6)

Choose the orientation inside the pair so that `|a|>=|b|`. Then

`|a| >= sigma/2`.                                                     (4.7)

Let `H_3` be the component of the full polynomial star (3.1) in the third coordinate:

`H_3=a v-c u`.                                                        (4.8)

Expanding `det P` and using `ab=c^2`,

`det P
 = -a v^2+2cuv-bu^2
 = -a (v-(c/a)u)^2
 = -H_3^2/a`.                                                        (4.9)

Thus the exact determinant identity is

`boxed: H_3^2 = -a det P`.                                          (4.10)

By (4.1),

`|det P| >= sigma^3`.                                                (4.11)

Combining (4.7), (4.10), and (4.11),

`|H_3| >= sigma^2/sqrt(2)`.                                         (4.12)

The full ambient star vector `H` includes the third-coordinate component `H_3`, so

`||H||_2 >= sigma^2/sqrt(2)`.                                       (4.13)

Apply Corollary 3.1:

`||p_Q||_infinity
 <= 2^(11/4) (sigma^2/sqrt(2))^(-1/2)
 = 2^(11/4+1/4)/sigma
 = 8/sigma`.                                                         (4.14)

This proves (4.2)-(4.3). QED.

### Why the outside matrix is harmless

No assumption is made on the outside block. In the source theorem of Section 2 it is the arbitrary `C` and can contain any sign, rank, magnitude, and dense same-bank curvature. Couplings from the displayed physical pair to every outside original coordinate are precisely the arm rows `u,v`; they enter the polynomial vector `H`. Thus Theorem 4.1 is a full-ambient conditional statement, not a theorem about an isolated three-variable polynomial.

## 5. r45's singular-pair no-go family is now paid

Take r45's explicit family at `epsilon=1/2`:

`P=2[[1,1,1],[1,1,-1],[1,-1,1]]`,
`C=(1/2)[[1,0],[0,1],[0,0]]`,
`A=[[P,C],[C^T,0_2]]`.                                                (5.1)

The full spectrum is approximately

`{-2.0806348802,-0.0615528128,0.0597660039,4.0208688763,4.0615528128}`, (5.2)

so exactly three eigenvalues have modulus at least one.

For the singular pair `(1,2)`,

`a=2`, `c=2`,
`u=(2,1/2,0)`, `v=(-2,0,1/2)`,

where the arm coordinates are physical coordinates `3,4,5`. Hence

`H=a v-c u=(-8,-1,1)`,
`||H||=sqrt(66)`.                                                     (5.3)

Corollary 3.1 gives the direct full-law estimate

`boxed:
 ||p_Q||_infinity
 <= 2^(11/4) 66^(-1/4)
 = 2.36018749055712... .
`                                                                        (5.4)

The three-coordinate core has spectrum `{-2,4,4}`, so Theorem 4.1 independently gives the coarser but scale-transparent bound

`boxed: ||p_Q||_infinity <= 4`.                                      (5.5)

Thus the exact family used by r45 to show `R_pair=0` is no longer an unpaid chamber.

## 6. Designated fleet04/B09 result applied to an actual inequality

The designated partner theorem is

`QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1`,

canonical source

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`.

For a literal invertible `3 x 3` original-coordinate cross block `K`, with arbitrary same-side quadratic curvature and outside couplings, it proves a continuous density and

`||p_Q||_infinity <= 3 |det K|^(-1/3)`.                             (6.1)

Apply it to

`K=diag(3,2,1)`,
`A_cross=[[0,K],[K,0]]`.                                             (6.2)

The spectrum is exactly

`{-3,-2,-1,1,2,3}`,                                                  (6.3)

and `det K=6`. Therefore the completed partner theorem gives the actual target-valid inequality

`boxed:
 ||p_Q||_infinity
 <= 3*6^(-1/3)
 = 1.65096362444731...,
`                                                                        (6.4)

with

`P{Q in I} <= 1.65096362444731... |I|`                              (6.5)

and a continuous density in this partner branch.

## 7. Deterministic verification

`CHECK.py` beside this report performs 2000 seeded rank-one-pair tests. It verifies

1. the singular pair relation numerically;
2. the exact polynomial identity `H_3^2=-a det P`;
3. the interlacing consequence `|a|>=sigma/2` after orienting the singular pair;
4. the derived inequality `|H_3|/sigma^2>=1/sqrt(2)`;
5. the r45 regression spectrum and star vector; and
6. the partner numerical inequality.

The maximum relative error in `H_3^2+a det P` was `2.56e-15`; the smallest observed ratio `|H_3|/sigma^2` was `0.8021`, above the theorem's `1/sqrt(2)=0.7071`. These are regression checks only; the proof is Sections 3-4.

## 8. Exact remaining B09 debt

The exact singular pair is paid, so the next unpaid mechanism is the **punctured near-singular definite pair**:

`QFORM-NEAR-SINGULAR-DEFINITE-PAIR-INTERPOLATION-v1`.

After completing one original coordinate of a definite physical pair, the exact remainder has the form

`delta X_q^2 + 2 X_q <g,X_R> + W(X_R)`,

with `delta=det(B)/a`. At `delta=0`, Corollary 3.1 pays the whole star without conditioning or deleting `W`. For `delta!=0`, simply deleting the small quadratic term is invalid for arbitrary unbounded/fragmented supports, and the fleet02/B08 stress analysis explicitly warns against extending the zero face by continuity. The next step is therefore to spend the `delta X_q^2` term jointly with the polynomial star and/or an aggregate crossing resource, uniformly as `delta ->0`, while retaining arbitrary remaining curvature exactly.

This is a narrower obstruction than r45's `QFORM-SINGULAR-DEFINITE-PAIR-ROUTING-v1`: the exact singular face is now closed.

Full unrestricted QFORM remains **OPEN**. Full-target continuity remains **OPEN**. The theorem in Section 4 is a supporting localized closure, not a claim that the bare three-large-eigenvalue hypothesis supplies such a physical triple.

## 9. Source/control provenance

Startup math-brain main: `476dac163193307b170035c926b485fb62baf20b`.  
Prepublication math-brain refresh: `b128a0ddd5a3d9fb05c5637ff2145850ff1cb2a7`.  
Prepublication math-open-problems master observed: `a03856e50323746433d26e0f9b2b112e2736f66e`.

Repository use and source retrieval are verified. Separate native learned-memory ingestion is not, so status remains `WITHOUT_VERIFIED_BRAIN`.
