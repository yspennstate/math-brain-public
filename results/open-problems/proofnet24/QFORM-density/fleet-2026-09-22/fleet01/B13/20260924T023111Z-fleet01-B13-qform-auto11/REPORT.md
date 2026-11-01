SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-24T02:31:11Z.
attacking: convert fleet02/B13 r39's tau-clean star-or-low-score physical two-volume into an aggregate near-pivot-line bank with fixed physical two-volume, without selecting or inverting an individual minor.

# fleet01/B13 — low-score Pluecker bank forces an aggregate near-hub strip

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Extremal product laws / analytic structural identities  
Run: `20260924T023111Z-fleet01-B13-qform-auto11`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **supporting theorem proved; full unrestricted QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Continuity remains separately OPEN.**

No moment, compact-support, connected-support, Gaussian, log-concavity, post-rotation independence, centered-interval extremality, common support diameter, fixed fragment count, or perturbative deletion of coefficient-small quadratic terms is used.

## 1. Exact product-indicator reduction retained

For completeness, the valid extremal-product interface is the witnesswise bathtub reduction already established by this slot.

Let `K>=0` be bounded and measurable and let `f_1,...,f_n` satisfy

`0<=f_i<=1`, `int_R f_i=1`.

Holding all coordinates except `i` fixed gives a bounded nonnegative fiber function `h_i`. Choose a threshold `t` and a measurable set `E_i` with

`{h_i>t} subset E_i subset {h_i>=t}`, `|E_i|=1`.

Then

`int (1_{E_i}-f_i)(h_i-t)>=0`,

while `int(1_{E_i}-f_i)=0`, hence replacing `f_i` by `1_{E_i}` does not decrease the objective. Iterating over the finitely many coordinates yields unit-measure measurable sets `E_i` such that

`int K(x) prod_i 1_{E_i}(x_i) dx >= int K(x) prod_i f_i(x_i) dx`.      (1.1)

For the slab kernel `K=1_{x^T A x in J}`, every actual cap-one product-law witness therefore transfers to a product-indicator witness for the same `A` and same `J`, with zero loss in slab ratio. Strict witnesses may subsequently be approximated by bounded finite-union unit sets with arbitrarily small loss. This is not an attained global optimizer statement and gives no single-interval, centering, common-diameter, or uniform-fragment-count conclusion.

## 2. Fresh designated-partner premise: fleet02/B13 r39

The completed designated partner result used here is fleet02/B13 r39:

- canonical mathematics: `yspennstate/math-open-problems@7270e9d36fa20c464994a6f989f32f83565f234e`
- report: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260924T014613Z-fleet02-B13-qform-r39/REPORT.md`
- theorem: `QFORM-TAUCLEAN-PHYSICAL-STAR-OR-LOWSCORE-E2-v1`.

Its hard diffuse exact-rank-two chamber is

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i ||u_i||^2<=1/3`, `s_3(A)>=1`.  (2.1)

There is a physical pivot `k` with `|d_k|>=1`. Put

`q_ij=det(u_i,u_j)^2`, `c=||u_k||^2`.                              (2.2)

In the non-rank-one hard branch,

`|det Lambda|>H0 rho^-2`, `H0=sqrt(1536 e^2)`,                     (2.3)

and fleet02/B13 r38-r39 produce a physical cut `C | C^c` of `[n]\{k}` and a good row-pair family `G subset binom(C,2)` with

`X:=sum_{E in G}q_E`,
`Y:=sum_{F subset C^c, |F|=2}q_F`,
`X Y>=1/384`,                                                       (2.4)

hence separately `X,Y>=1/384`, and every `E in G` is tau-clean. Across this physical cut,

`det A[E,F]^2=(det Lambda)^2 q_E q_F`.                              (2.5)

Partner r39 also proves the denominator-free disjoint-edge score inequality. Rotate only the deterministic two-dimensional coefficient basis so

`u_k=(sqrt(c),0)`, `u_i=(x_i,y_i)`, `s_i=y_i^2`.                  (2.6)

For a good edge `E={i,j}`, define

`a_E:=q_ij s_i s_j`.                                                (2.7)

When `c>0`, any two vertex-disjoint good edges satisfy

`sqrt(a_E a_E') <= K rho^-1`,                                      (2.8)

with the safe explicit constant

`K=2974`.                                                           (2.9)

If `c=0`, partner r39 already gives `rho<10.322...`, so below I work only with `c>0`.

Partner r39 obtained the alternative: one physical-center star carries slab-scale two-volume, or the low-score set

`L0={E in G: a_E<=K/rho}`                                          (2.10)

carries positive aggregate two-volume. The purpose of this run is to sharpen and geometrize the latter alternative.

## 3. New combinatorial sharpening: the low-score mass is at least 5/8 of the good mass

Normalize the good edge weights by

`p_E=q_E/X`, `E in G`,                                              (3.1)

and define vertex marginals

`r_v=sum_{E in G: v in E}p_E`.                                     (3.2)

Then

`sum_v r_v=2`.                                                      (3.3)

If some `r_h>=1/4`, this is exactly the partner's star alternative, so suppose from now on that

`max_v r_v<1/4`.                                                    (3.4)

Let

`H_+={E in G: a_E>K/rho}`.                                         (3.5)

By (2.8), no two edges of `H_+` are vertex-disjoint, so `H_+` is a pairwise-intersecting simple graph.

### Lemma 3.1 — intersecting graph classification

Every pairwise-intersecting family of 2-subsets is either contained in one star or contained in the three edges of one triangle.

Proof. Pick two distinct edges. If all edges meet at their common vertex, the family is a star. Otherwise, after relabeling, two edges are `{a,b}` and `{a,c}` and some edge avoids `a`; to meet both it must be `{b,c}`. Any further edge must meet each of `{a,b}`, `{a,c}`, `{b,c}`, hence it is one of those three. QED.

If `H_+` is a star, its normalized mass is `<1/4` by (3.4). If it is contained in a triangle on vertices `a,b,c`, then each triangle edge contributes to two of the three marginals, so

`2 p(H_+) <= r_a+r_b+r_c <3/4`,

therefore

`p(H_+)<3/8`.                                                       (3.6)

Thus in every non-star case

`p(L0)>5/8`.                                                        (3.7)

Equivalently, putting

`M:=sum_{E in L0}q_E`,                                              (3.8)

we have the strengthened bound

`boxed: M>5X/8 >=5/3072`.                                          (3.9)

This improves the partner's safe `X/4` low-score mass by a factor `5/2`.

## 4. Immediate target-level improvement of the physical two-volume

By (2.5), the low-score physical cross two-volume is

`Z_low=(det Lambda)^2 M Y`.                                        (4.1)

Using (3.9), (2.4), and `(det Lambda)^2>1536 e^2 rho^-4`,

`Z_low > (5/8)(det Lambda)^2 X Y`
`      >=(5/8)(det Lambda)^2/384`
`      >(5/2)e^2 rho^-4`.                                          (4.2)

Hence partner r39's low-score branch can be strengthened to

`boxed: Z_low>(5/2)e^2 rho^-4`.                                   (4.3)

No individual `q_ij`, `q_ki`, `q_kj`, or physical determinant is inverted.

## 5. New theorem: `QFORM-LOWSCORE-TO-HUBSTRIP-18-v1`

The low pivot-tripod score cannot remain diffusely spread. It forces a fixed amount of the actual two-volume to touch an increasingly narrow physical coefficient strip about the pivot line.

Because the coefficient rotation in (2.6) is deterministic and `U^T U=I_2`,

`sum_{i ne k}s_i=1`.                                                (5.1)

Also the Parseval-frame identity gives, for every physical row `i`,

`sum_{j ne i}q_ij=||u_i||^2=:c_i`.                                (5.2)

Indeed, `sum_j det(u_i,u_j)^2=2||u_i||^2-u_i^T(sum_j u_j u_j^T)u_i=||u_i||^2`.

For `tau>0` define the near-pivot-line strip

`H_tau={i in C: s_i<tau}`, `T_tau=C\H_tau`.                        (5.3)

Every low-score edge `{i,j} subset T_tau` obeys

`q_ij s_i s_j<=K/rho`.                                              (5.4)

If `s_i,s_j>0`, write `r_i=x_i/y_i`; then

`q_ij=s_i s_j(r_i-r_j)^2`.                                         (5.5)

From (5.4),

`(r_i-r_j)^2<=K/(rho s_i^2 s_j^2)`,

and because `s_i,s_j>=tau`,

`q_ij<= [K/(rho tau^4)] s_i s_j`.                                 (5.6)

Summing over all unordered pairs in `T_tau` gives

`sum_{E in L0: E subset T_tau}q_E`
` <= [K/(rho tau^4)] sum_{i<j in T_tau}s_i s_j`
` <= K/(2 rho tau^4)`.                                              (5.7)

On the other hand, every low-score edge touching `H_tau` is counted at least once by the row identity (5.2), hence

`sum_{i in H_tau}c_i`
` >= sum_{E in L0: E cap H_tau not empty}q_E`
` >= M-K/(2 rho tau^4)`.                                            (5.8)

This is the useful parameterized inequality:

`boxed: sum_{i in C: s_i<tau} ||u_i||^2 >= M-K/(2 rho tau^4)`.      (5.9)

Now use only the universal lower mass `M>5X/8` and choose

`tau_X := (8K/(5X rho))^(1/4)`.                                    (5.10)

Then the high-high contribution in (5.7) is at most `5X/16`, so

`boxed: sum_{i in H_{tau_X}}c_i >5X/16 >=5/6144`.                 (5.11)

Moreover the low-score edge mass touching this strip is itself `>5X/16`; multiplying by the entire opposite-bank pair volume gives

`Z_strip`
`:=sum_{E in L0: E cap H_{tau_X} not empty}`
`    sum_{F subset C^c, |F|=2} det A[E,F]^2`
` >(5/16)(det Lambda)^2 X Y`
` >(5/4)e^2 rho^-4`.                                                (5.12)

Thus a fixed slab-scale amount of the **actual physical squared-two-minor currency** is forced to touch the near-pivot strip.

Finally, the geometric distance of row `u_i=(x_i,y_i)` to the pivot line `span(u_k)` is exactly `|y_i|=sqrt(s_i)`. Hence every row in the strip obeys

`dist(u_i,span u_k) < tau_X^(1/2)`
` = (8K/(5X rho))^(1/8)`.                                          (5.13)

Since `X>=1/384` and `K=2974`,

`boxed: dist(u_i,span u_k)<6.064 rho^(-1/8)`                       (5.14)

for every `i` in the strip.

Equations (5.11), (5.12), and (5.14) are the theorem `QFORM-LOWSCORE-TO-HUBSTRIP-18-v1`.

## 6. Fixed-energy versus high-cardinality refinement

The strip leverage decomposes as

`sum_{i in H}c_i=sum_{i in H}x_i^2+sum_{i in H}s_i`.               (6.1)

Using (5.11), at least one of the following holds:

`sum_{i in H}x_i^2 >=5X/32`,                                       (6.2)

or

`sum_{i in H}s_i >5X/32`.                                          (6.3)

In the second case each `s_i<tau_X`, therefore

`|H| > (5X)/(32 tau_X)`
`     =(5X/32)(5X rho/(8K))^(1/4)`.                                (6.4)

Using only `X>=1/384`, this gives the explicit dichotomy

`boxed: sum_{i in H}x_i^2 >=5/12288`,                              (6.5)

or

`boxed: |H|>1.1067e-5 rho^(1/4)`.                                 (6.6)

So the surviving near-hub endpoint has either fixed physical coefficient energy along the pivot direction or polynomially growing physical cardinality. Both are aggregate statements; neither chooses one small reciprocal star coefficient.

## 7. Complete hard-branch structural alternative obtained this run

Within the partner r39 exact diffuse rank-two hard chamber and `c>0`, every slab witness of ratio `rho` satisfies one of the following.

1. **Physical-center star:** some physical center `h` anchors partner r39's tau-clean squared-two-minor subsum `>e^2 rho^-4`.

2. **Aggregate near-pivot strip:** there is a physical row set `H subset C` with

   `sum_{i in H}||u_i||^2>5/6144`,

   `dist(u_i,span u_k)<6.064 rho^-1/8` for every `i in H`,

   and row pairs touching `H` carry physical cross squared-two-minor volume

   `Z_strip>(5/4)e^2 rho^-4`.

   In addition, either `sum_{i in H}x_i^2>=5/12288` or `|H|>1.1067e-5 rho^(1/4)`.

3. **Small-ratio triviality:** if the adaptive threshold in (5.10) is not `<1`, then

   `rho <= 8 K*384/5 =1,827,225.6`,                                (7.1)

   which is already a finite bound within this branch.

4. **`c=0` endpoint:** partner r39 already gives `rho<10.322...`.

The point of alternative 2 is not the numerical constant. It eliminates the possibility that the partner's low-score bank remains an unstructured diffuse set of tiny Pluecker edges: a fixed amount of both leverage and actual cross-two-volume must move into an `O(rho^-1/8)` neighborhood of one physical pivot line.

## 8. Geometric product-set formulation

By the exact witnesswise purification (1.1), the same structural alternative holds for a strict bad slab after replacing the arbitrary cap-one product law by a product of measurable unit sets, with the same `A` and same slab ratio or better. Thus in the exact rank-two hard chamber a hypothetical sequence of unit-product-set witnesses with `rho_m->infinity` must, after passing to the partner's physical cut, place a fixed amount of coefficient-frame currency and `rho_m^-4`-scale cross two-volume on rows converging projectively to one physical pivot line at rate `O(rho_m^-1/8)`, unless the physical-center star branch occurs.

Strict witnesses may be approximated by bounded finite unions after this reduction; no bounded diameter or uniform component count is inferred.

## 9. Why this does not yet prove full QFORM

The full conjecture remains open. The new theorem is a structural conversion inside the exact diffuse rank-two hard endpoint. A density receiver still has to consume either:

- the single physical-center star carrying slab-scale two-volume, or
- the aggregate near-pivot strip while retaining all same-bank quadratic curvature and outside couplings.

In the near-pivot branch, coefficient closeness to a line cannot be treated by deleting the transverse quadratic coefficients: the input supports may be arbitrarily separated/fragmented, so coefficient-small is not distribution-small. The receiver must aggregate the whole physical bank before any reciprocal payment. In a general non-exact-rank-two survivor, the already-proved every-cut `s_5=O(rho^-1)` tail must likewise remain in the phase and cannot be discarded as a random perturbation.

The first unpaid implication is therefore

`QFORM-HUBSTRIP-18-OR-CENTERSTAR-PRODUCT-RECEIVER-v1`:

> Consume the physical-center star or the fixed-mass `O(rho^-1/8)` near-pivot bank by an original-coordinate product-preserving density/small-ball estimate, using the fixed along-line energy or forced `Omega(rho^(1/4))` cardinality without individual-minor inversion. Otherwise construct a valid bounded-finite-union product-indicator counterexample.

## 10. Corrections and scope retained

- Uniform lawwise pointwise quadratic oscillatory decay is false.
- Rotating random coordinates destroys independence and is not used.
- Projection density alone does not solve indefinite quadratic pushforward.
- Arbitrary-joint coarea and positive conditional-density-moment gates are false.
- `pi` is only the diagonal control, not a universal rotated constant.
- Bounded-diameter and fixed-fragment-count extremal localization are false.
- A physical cross minor by itself is not a density receiver.
- No coefficient-small quadratic tail is deleted.

The theorem above is coefficient algebra plus original-coordinate aggregation only.
