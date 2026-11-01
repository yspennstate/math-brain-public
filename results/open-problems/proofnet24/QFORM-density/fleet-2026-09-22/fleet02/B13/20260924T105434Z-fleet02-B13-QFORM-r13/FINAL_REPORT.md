SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-24T10:54:34.446238Z.
attacking: repair the affine/grouping scope in the forced ultracollapsed rank-one-plus-four-diagonal endpoint by proving a receiver for exactly the group-compatible affine directions, then force either quadratic support spread or a translation-gradient misalignment that cannot be hidden inside the dominant rank-one bank.

# fleet02/B13 — corrected final: compatible-affine core receiver and translation-gradient escape

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: extremal product laws / complementary constructions and source-valid counterexamples  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING THEOREM / FULL QFORM OPEN / CONTINUITY OPEN**.

`CORRECTION.md` in this same immutable run wins over the earlier initial `REPORT.md`: the late-loaded current B13 memory state records that r12's use of the finite-direction grouping theorem for a completely arbitrary physical affine term was out of scope. The new argument below does not make that extension. It identifies the exact affine subspace that the physical grouping really supports and keeps the residual translation-gradient mismatch inside the rough tail.

No moment, compact-support, log-concavity, connected-support, diagonal-basis, post-rotation independence, bounded-diameter, fixed-fragment-count, or attained global optimizer is assumed. All tail terms are retained.

## 1. Starting point after the immediately preceding B13 reduction

The latest completed compatible designated partner remains fleet03/B13 r48,

`math-open-problems@ba4c0f14cf9ca505e346b284a530662c6522b514:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260924T095803Z-fleet03-B13-qform-r48/REPORT.md`.

The immediately preceding canonical fleet02/B13 run already combined r48 with the arbitrary-rank physical-pair theorem and proved that every high-density diffuse exact-rank-two survivor is forced into

`A=D_C+lambda_1 vv^T+D_(C^c)+lambda_2 ww^T`, `|C|<=4`,             (1.1)

with

`||D_(C^c)||op <= C_D/rho`, `C_D:=2 sqrt(30 pi)=19.41625912555699...`,

`|lambda_2| <= C_u/rho^2`, `C_u:=32 sqrt(6)e=213.06891061773865...`, (1.2)

and dominant core

`M_C:=D_C+lambda_1 vv^T`                                          (1.3)

satisfying, throughout the r48 chamber `rho>=rho0=82.572423603571...`,

`s_3(M_C) >= s_*`, `s_*:=0.7336078268845... >1/2`.                (1.4)

That same preceding run correctly withdrew the claim that the old grouping theorem was affine-uniform for an arbitrary physical linear term. The missing receiver is therefore not spectral anymore; it is an affine/product-structure issue.

## 2. A correct affine-uniform receiver on the exact group-compatible subspace

Let

`L_(C,v):={a in R^n : there exists alpha in R with a_i=alpha v_i for every i notin C}`. (2.1)

Inside `C` the affine coefficients are arbitrary; outside `C` they must be parallel to the one physical bank direction actually present in the rank-one core.

### Theorem 2.1 — `QFORM-RANK1-FINITECORE-COMPATIBLE-AFFINE-v1`

There is a universal finite constant `K_core` such that for every matrix `M_C` of the form (1.3) with `|C|<=4` and `s_3(M_C)>=s_*`, every independent cap-one input vector `X`, every `a in L_(C,v)` and every constant `c`,

`boxed:
 ||p_(X^T M_C X+a^T X+c)||_infinity <= K_core.}`                  (2.2)

One may take

`K_core = e C_5^aff/s_*`,                                        (2.3)

where `C_5^aff<infinity` is any uniform constant supplied by the completed fixed-dimensional affine QFORM theorem for dimensions at most five and matrices with third singular value at least one.

#### Proof

Put

`q:=||v_(C^c)||_2`.                                               (2.4)

If `q>0`, define the single grouped outside variable

`Z:=q^(-1) sum_(i notin C) v_i X_i`.                              (2.5)

The coefficient vector in (2.5) is unit. The completed weighted affine-fiber Brascamp-Lieb theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` with `k=1` gives

`||p_Z||_infinity <= sqrt(e)`.                                    (2.6)

The variables `(X_i)_(i in C)` and `Z` are independent because their underlying original-coordinate banks are disjoint. Let

`W=((X_i)_(i in C),Z)`,                                          (2.7)

so `dim W<=5`. The quadratic core depends only on these variables:

`X^T M_C X=W^T B W`,                                             (2.8)

where `B` is the compression of `M_C` to

`H=span({e_i:i in C}, q^(-1)v_(C^c))`.                           (2.9)

Since `M_C` vanishes on `H^perp`, `B` has exactly the nonzero eigenvalues of `M_C`; in particular

`s_3(B)>=s_*`.                                                    (2.10)

Now take `a in L_(C,v)`. For some scalar `alpha`, the outside affine term is

`sum_(i notin C) a_i X_i=alpha q Z`,                             (2.11)

while the coordinates in `C` remain arbitrary. Thus the entire affine term is an ordinary affine function of the same at-most-five independent grouped variables `W`. No second uncontrolled outside projection is introduced.

Every component of `W` has density cap at most `sqrt(e)`. Set

`V=sqrt(e) W`.                                                    (2.12)

Then the components of `V` are independent and cap one, and

`e[W^T B W+linear+c]=V^T B V+arbitrary affine in V`.              (2.13)

The completed fixed-dimensional affine theorem applies in dimension at most five. After dividing `B` by `s_*`, it yields

`||p_(V^T B V+affine)||_infinity <= C_5^aff/s_*`.                 (2.14)

Scaling back by the factor `e` gives (2.2)-(2.3).

If `q=0`, the core and every compatible affine term depend only on the at-most-four original coordinates in `C`; apply the same fixed-dimensional affine theorem directly (or harmlessly use the larger constant (2.3)). QED.

### Scope

This theorem does **not** claim a bound for an arbitrary physical affine vector. If `a_(C^c)` is not parallel to `v_(C^c)`, the extra linear form generally cannot be represented by the single grouped scalar `Z`. That is exactly the r12 scope gap, now isolated rather than ignored.

## 3. Compatible-affine slab-defect principle

For a product set `G=prod_i G_i` define

`Delta_(C,v)(F;G)`
` := inf_(a in L_(C,v), c in R) esssup_(x in G) |x^T F x-a^T x-c|`, (3.1)

where

`F:=D_(C^c)+lambda_2 ww^T`.                                      (3.2)

Let `J` be an interval of length `ell` and

`p:=P(X^T A X in J)=rho ell`.                                    (3.3)

Choose arbitrary measurable physical-coordinate sets `G_i` with

`eta:=sum_i P(X_i notin G_i)<=p/2`.                              (3.4)

Exactly the slab-enlargement argument from the abstract affine-defect lemma, but now using only Theorem 2.1's allowed affine subspace, gives

`rho ell-eta <= K_core(ell+2 Delta_(C,v)(F;G))`.                  (3.5)

Therefore, whenever

`rho>=4 K_core`,                                                 (3.6)

one has

`boxed:
 Delta_(C,v)(F;G) >= p/(8 K_core).}`                              (3.7)

This is fully justified: the affine approximation added to the core is restricted to the exact physical subspace for which Theorem 2.1 proved uniform density control.

## 4. Exact Taylor upper bound: the unpaid quantity is translation-gradient misalignment

Assume first each `G_i` is essentially contained in a finite interval about a chosen center `m_i`:

`|x_i-m_i|<=r_i` on `G_i`.                                       (4.1)

Write `m=(m_i)` and

`m_w:=w^T m`.                                                     (4.2)

Expanding the retained tail exactly,

`x^T F x`
` =m^T Fm+2(Fm)^T(x-m)+(x-m)^T F(x-m)`.                          (4.3)

Inside the named center set `C`, the compatible affine space allows every linear coefficient, so choose it to equal the exact Taylor gradient there. Outside `C`, only one scalar multiple of `v` is allowed. Hence, for every `alpha in R`, choose the compatible affine vector with

`a_i=2(Fm)_i` for `i in C`,
`a_i=alpha v_i` for `i notin C`.                                 (4.4)

The remaining outside gradient is

`g_i(m,alpha)`
` :=2 d_i m_i+2 lambda_2 w_i m_w-alpha v_i`, `i notin C`.        (4.5)

The centered quadratic remainder obeys

`|(x-m)^T F(x-m)|`
` <=sum_(i notin C)|d_i|r_i^2`
`   +|lambda_2|(sum_i |w_i|r_i)^2`.                              (4.6)

Therefore

`boxed:
 Delta_(C,v)(F;G)`
` <= inf_alpha sum_(i notin C) r_i |g_i(m,alpha)|`
`    +sum_(i notin C)|d_i|r_i^2`
`    +|lambda_2|(sum_i |w_i|r_i)^2.}`                            (4.7)

Combining (3.7) and (4.7) is the new rough-law obstruction. It makes the affine debt explicit: high density can survive small centered curvature only if the translation-induced tail gradient has a substantial component, measured on the actual product widths, outside the dominant physical rank-one direction `v`.

Using the coefficient bounds (1.2), every high-density survivor satisfies

`boxed:
 inf_alpha sum_(i notin C) r_i |2d_i m_i+2lambda_2 w_i m_w-alpha v_i|`
` +(C_D/rho) sum_(i notin C) r_i^2`
` +(C_u/rho^2)(sum_i |w_i|r_i)^2`
` >= p/(8K_core).}`                                              (4.8)

No coefficient-small random term has been discarded.

## 5. Fragmentation-preserving form for finite-union indicator witnesses

The partner's optimizer-free extremal-product reduction permits any strict violation to be approximated, with arbitrarily small loss, by a product of indicators of bounded finite unions `E_i` of total measure one. Do **not** assume a bounded common diameter or bounded fragment count.

For a measurable set `S` of positive measure define

`kappa(S):=inf_(alpha,beta) esssup_(x in S)|x^2-alpha x-beta|`.    (5.1)

The following elementary shell-radius fact is independent of connectedness.

### Lemma 5.1 — `QFORM-QUADRATIC-DEFECT-SHELL-RADIUS-v1`

If `|S|=m>0` and `kappa(S)<infinity`, then for every `epsilon>0` there exists a center `c` for which

`esssup_(x in S)|x-c| <=4(kappa(S)+epsilon)/m`.                   (5.2)

#### Proof

For a fixed center `c`, completing the affine square shows that the best constant approximation to `(x-c)^2` has error

`(b^2-a^2)/2`,                                                   (5.3)

where

`a=essinf_S |x-c|`, `b=esssup_S |x-c|`.                          (5.4)

The two-sided annulus `a<=|x-c|<=b` has Lebesgue measure `2(b-a)` and contains `S` a.e., so

`m<=2(b-a)`.                                                      (5.5)

Thus

`(b^2-a^2)/2=(b-a)(b+a)/2 >= mb/4`.                              (5.6)

Choose `c` within `epsilon` of the infimum in (5.1). QED.

Now use the trimming condition (3.4) on a unit-indicator witness. Since `p<=1`, each retained set satisfies

`|G_i|>=1-p/2>=1/2`.                                             (5.7)

Choose the centers `m_i` in Lemma 5.1 and let `epsilon downarrow0`; then one may take

`r_i<=8 kappa(G_i)`.                                             (5.8)

Insert this into (4.8), use `||w||_2=1` and Cauchy-Schwarz:

`(sum_i |w_i|r_i)^2<=64 sum_i kappa(G_i)^2`.                     (5.9)

Define the exact translation-gradient mismatch at these quadratic-defect centers by

`Gamma(G,m)`
` := inf_alpha sum_(i notin C) kappa(G_i)`
`    *|2d_i m_i+2lambda_2 w_i(w^T m)-alpha v_i|`.                (5.10)

Then every sufficiently high purified witness obeys

`boxed:
 8 Gamma(G,m)`
` +64(C_D/rho+C_u/rho^2) sum_i kappa(G_i)^2`
` >= p/(8K_core).}`                                              (5.11)

Consequently at least one of the following must hold:

`boxed:
 Gamma(G,m) >= p/(128 K_core),}`                                 (5.12)

or

`boxed:
 sum_i kappa(G_i)^2`
` >= p rho/[1024 K_core(C_D+C_u/rho)].}`                         (5.13)

Because `p=rho ell`, the second branch is a genuine `Omega(rho^2 ell)` fragmentation-preserving quadratic-defect escape. The first branch is the new structural endpoint: the translation gradient of the retained `O(rho^-1)` diagonal tail plus `O(rho^-2)` secondary carrier remains quantitatively misaligned with the only outside affine direction that the dominant rank-one core can absorb.

Unlike a convex-hull diameter, `kappa` does not simply charge an empty gap. For the legal two-fragment shell

`S_R=[R-1/4,R+1/4] union[-R-1/4,-R+1/4]`,                       (5.14)

one has exactly

`kappa(S_R)=R/2`.                                                 (5.15)

Thus remote thin fragments are still allowed to pay the obstruction, at precisely their true quadratic non-affineness scale. No compactness is inferred.

## 6. Why this repairs, rather than repeats, the previous affine-defect attempt

The old invalid step was: subtract an arbitrary coordinatewise affine approximation of the tail and then assert that the resulting arbitrary physical linear term can be absorbed by a one-scalar grouping of the rank-one bank.

The corrected mechanism is:

1. prove a density cap only for the exact affine space `L_(C,v)` that the physical grouping represents;
2. subtract only affine terms in that space;
3. keep the orthogonal part of the tail Taylor gradient explicitly as `Gamma`;
4. retain both centered quadratic tails in (4.8)/(5.11).

Thus no hidden affine-uniform theorem is used. The new first unpaid implication is

`QFORM-TRANSLATION-GRADIENT-MISALIGNMENT-RECEIVER-v1`:

> Pay the branch (5.12) by exploiting the original-coordinate product law before any fiber supremum, or else force the quadratic-defect escape (5.13) to generate a genuine bounded-finite-union counterexample. A valid payment must retain the centered diagonal and secondary quadratic tails.

## 7. Required pinned Fourier obstruction

The required owner-pinned source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was reread in `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed unconditional D5 theorem gives for every disjoint original-coordinate physical cross block `B=A[I,J]`

`||p_Q||infinity <=5 sqrt(2e) e_5(B^T B)^(-1/10)`.                (7.1)

Therefore every ratio-`rho` slab witness satisfies

`boxed:
 e_5(B^T B)<=(5 sqrt(2e)/rho)^10,`
` s_5(B)<=5 sqrt(2e)/rho=11.6582199079856.../rho.}`               (7.2)

This is a real simultaneous obstruction before exact-rank-two collapse. In the exact-rank-two endpoint every physical cross block has rank at most two, so D5 is identically blind and does not pay the new gradient-misalignment branch. The pinned numerical search still reports no counterexample; its numerics are not used as proof.

## 8. Status

Full unrestricted QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains OPEN.

The substantive gain of this invocation is not the already-known pair-branch elimination. It is the compatible-affine repair: the rank-one-plus-four-diagonal core has a genuine uniform affine receiver on precisely the physical affine subspace generated by its finite centers and dominant rank-one bank, and every remaining high-density finite-union witness must pay either a large coordinatewise quadratic-defect budget or an explicit translation-gradient component transverse to that bank. This is the next product-law obstruction to attack.