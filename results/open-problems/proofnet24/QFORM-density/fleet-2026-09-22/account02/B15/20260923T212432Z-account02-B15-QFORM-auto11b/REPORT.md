SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-23T21:24:32Z.
attacking: the near-null physical-triple regularity interface—keep the ruled majority geometry through rough inputs and determine which vanishing-curvature sign is genuinely costly.

# account02/B15 — sign-sensitive ruled regularity and a target-valid conditional-sup obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T212432Z-account02-B15-QFORM-auto11b`  
Status: `SUPPORTING_LEMMA_PROVED / TARGET-VALID PROOF-INTERFACE OBSTRUCTION / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The unrestricted owner statement remains open:

`sup ||p_(X^T A X)||_infinity < infinity`

over every finite dimension, every product of cap-one densities, and every symmetric `A` with at least three eigenvalues of modulus at least one.

This run pays a sharper majority-side near-null branch and exhibits an exact target family showing why a bad physical triple cannot be controlled by taking a supremum over the outside conditioning variable. The unpaid local term remains the minority/two-sheet contribution; globally one must still route the third smoothing resource before a bad conditional supremum is taken.

## 2. Sources and live corrections consumed

The owner-pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I read its `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The result used below is its completed ruled one-sheet theorem (Theorem C). The current later audit in `20260922T231000Z-semidefinite-and-hub-reduction/README.md` is also consumed: the rank-three ruled theorem requires the affine term to lie in the quadratic range. In the ambient application below the active physical `3x3` block is invertible, so that condition is automatic after conditioning outside and completing the square.

The designated partner result actually applied is account03/B15 at

`yspennstate/math-open-problems@4d7b28c4737455388bd14f7bb7abeca5264dffd7`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260923T202515Z-account03-B15-qform-auto11/REPORT.md`.

It corrects the false affine-slope rescue and proves sharply, for cap-one `Z`, `gamma!=0`, `1<q<2`,

`||p_(gamma Z^2+2rZ)||_q <= [2^(q-1)/(2-q)]^(1/q)|gamma|^(-1+1/q)`,

with equality after translating a unit uniform to the moving critical point. Together with its cited completed account04/B15 physical hyperbolic-pair estimate, at `p=3,q=3/2` one has the valid convolution bound

`||p_(T+gamma Z^2)||_infinity <= 6 |b|^(-2/3)|gamma|^(-1/3)`

for a physical hyperbolic pair `T=aX^2+2bXY+...`, `b!=0`, on disjoint original coordinates. The partner correction says explicitly that no law-uniform gain from a large affine slope is available once nonzero square curvature remains.

All live prohibitions are retained: no arbitrary-joint coarea height theorem, no post-rotation independence, no generic two-sheet X-ray closure, no moment/support/log-concavity assumption, and no deletion of a small nonzero quadratic coefficient as a small random perturbation.

## 3. New sign-sensitive refinement of the ruled coefficient

Consider an invertible physical `3x3` block of signature `(2,1)`. Write the two same-sign (majority) eigenvalue magnitudes as `lambda1,lambda2>0` and the minority magnitude as `mu>0`. The completed ruled theorem gives the majority-side coefficient

`C_+(lambda1,lambda2,mu)`
`=(lambda1 lambda2 mu)^(-1/2)`
`  * int_0^(2pi) [sin^2(theta)/lambda1 + cos^2(theta)/lambda2 + 1/mu]^(-1/2) dtheta.`

Algebraically,

`C_+ = int_0^(2pi)`
` [lambda2 mu sin^2(theta)+lambda1 mu cos^2(theta)+lambda1 lambda2]^(-1/2) dtheta.`        (3.1)

Let `m=min(lambda1,lambda2)` and `M=max(lambda1,lambda2)`. Since

`lambda2 sin^2(theta)+lambda1 cos^2(theta) >= m`,

(3.1) yields the stronger sign-sensitive bound

`boxed( C_+ <= 2 pi / sqrt( m (M+mu) ) <= 2 pi/sqrt(lambda1 lambda2). )`                 (3.2)

The second inequality is the key point: **no lower bound on the minority magnitude `mu` is required**. If the two majority magnitudes satisfy `lambda1,lambda2>=kappa`, then

`boxed( C_+ <= 2 pi/kappa )`                                                              (3.3)

uniformly for every `mu>0`, even along `mu -> 0`.

When all three magnitudes are at least `kappa`, (3.2) recovers the familiar stronger value

`C_+ <= pi sqrt(2)/kappa`.

So the earlier use of `min(lambda1,lambda2,mu)` in a crude bound obscures an important fact: a vanishing **minority-sign** curvature does not make the one-sheet receiver singular.

### Ambient conditional form

Let `S` be three original coordinates, `W=X_(S^c)`, and suppose `B=A_SS` is invertible of signature `(2,1)`. Conditioning on `W=w` gives

`Q_w(u)=u^T B u + 2 d(w)^T u + c0(w)`.

Because `B` is invertible,

`Q_w(u)=(u+B^(-1)d(w))^T B (u+B^(-1)d(w))+c(w)`,

`c(w)=c0(w)-d(w)^T B^(-1)d(w)`.

This is a translation in the **original three independent coordinates**; it does not assert independence in an eigenbasis. Applying the ruled theorem conditionally and averaging gives, for the majority submeasure

`nu_+(E)=P(Q in E, Q>=c(W))`,

`boxed( nu_+(I) <= C_+(B)|I| <= [2 pi/sqrt(lambda1 lambda2)] |I| )`                     (3.4)

for every interval `I`, with no dependence on the minority magnitude `mu`.

Consequently the exact owner-scale tent payment is

`boxed( E[(eps-|Q-y|)_+ 1_{Q>=c(W)}] <= C_+(B) eps^2`                                   (3.5)

and in particular at most `(2pi/kappa) eps^2` when both majority curvatures are at least `kappa`.

This is an essential-boundedness statement for a positive submeasure. No continuity assertion is used to obtain (3.4) or (3.5).

## 4. Independent rough-input bridge check

The later audit's affine-in-range condition is automatic in Section 3 because `B` is invertible. It remains to justify arbitrary rough cap-one marginals without evaluating an `L^infinity` representative on a ruled curve.

Mollify only the three active original-coordinate densities:

`f_i^(eta)=f_i * gamma_eta`, `i in S`.

Then `f_i^(eta)<=1`, independence is preserved, and

`|| product_(i in S) f_i^(eta) - product_(i in S) f_i ||_1`
` <= sum_(i in S) ||f_i^(eta)-f_i||_1 ->0.`                                             (4.1)

The translation `u -> u+B^(-1)d(w)` does not change (4.1), uniformly in `w`. For every fixed `w`, deterministic quadratic pushforward and restriction to the majority event contract total variation. Hence the smooth conditional majority submeasures converge in total variation to the rough conditional one, uniformly in `w`, and the interval inequality passes with exactly the same `C_+(B)`. Averaging the untouched law of `W` proves (3.4).

Thus rough-input limiting is paid at the **measure inequality** level. Output continuity is neither assumed nor inferred in this passage.

For coefficient/source approximation one can also use the completed moving-sheet weak-closure mechanism: if `B_m -> B` with `B` still invertible of the same signature and the coordinate laws converge weakly, the product laws converge weakly; the moving boundary is the zero set of a nonzero quadratic polynomial and has zero limiting product mass; hence the majority submeasures converge weakly and any common interval domination passes by Portmanteau. Again this is a closure of an already-paid interval inequality, not a derivation of height from continuity.

## 5. A target-valid family where the bad conditional triple diverges logarithmically

The sign asymmetry in Section 3 is not cosmetic. The following exact target construction shows that if a **majority-sign** curvature tends to zero, a selected physical triple can have a genuinely divergent conditional density even though the full QFORM output is uniformly bounded.

Let `X,Y,Z,W` be iid `Uniform[-1/2,1/2]`, and for `0<gamma<=1` set

`Q_gamma = 2 X Y + gamma Z^2 + W^2.`                                                     (5.1)

The original-coordinate matrix is

`A_gamma = [[0,1,0,0], [1,0,0,0], [0,0,gamma,0], [0,0,0,1]]`,

whose eigenvalues are `{1,-1,gamma,1}`. Hence (5.1) is an **exact full-target instance**: three eigenvalues have modulus at least one.

Choose the active physical triple `(X,Y,Z)` and condition on `W=w`. Its block has spectral magnitudes `(1,gamma,1)` with signature `(2,1)`, and the conditional law is a translate of

`R_gamma = 2XY + gamma Z^2.`                                                             (5.2)

### Exact logarithmic conditional peak

For `T=2XY`, direct one-dimensional product integration gives

`p_T(t)=log(1/(2|t|)) 1_{0<|t|<1/2}.`                                                    (5.3)

Since `gamma Z^2 <= 1/4 < 1/2`, convolution at zero gives exactly

`p_(R_gamma)(0)`
` = E log(1/(2 gamma Z^2))`
` = log(1/(2 gamma)) - 2 E log|Z|.`

For `Z~Uniform[-1/2,1/2]`,

`E log|Z| = -1-log 2`,

so

`boxed( p_(R_gamma)(0) = 2 + log(2/gamma). )`                                            (5.4)

Therefore, for every outside value `w`,

`boxed( ||p_(Q_gamma | W=w)||_infinity >= 2+log(2/gamma) -> infinity. )`                  (5.5)

This is not a pathology of discontinuous output densities: for each `gamma>0`, the partner `L^p-L^q` convolution theorem puts the rank-three conditional density in `C_0`.

### Yet the full target density is uniformly bounded

Apply the completed partner inequality to the **different** original-coordinate smoothing resource `2XY+W^2`: with physical hyperbolic coefficient `b=1`, square coefficient `1`, and `(p,q)=(3,3/2)`,

`||p_(2XY+W^2)||_infinity <= 6.`                                                         (5.6)

Convolution with the independent probability law of `gamma Z^2` cannot increase `L^infinity`. Hence

`boxed( ||p_(Q_gamma)||_infinity <= 6 for every 0<gamma<=1. )`                           (5.7)

The full density is also in `C_0` by the same convolution result followed by convolution with a probability measure.

Thus the true inequality

`||p_Q||_infinity <= sup_w ||p_(Q|W=w)||_infinity`

can be **arbitrarily lossy inside the exact target class**: the right side grows like `log(1/gamma)` in (5.5), while the left side stays at most six in (5.7). Any proof architecture that freezes the outside third smoothing coordinate and then pays a reciprocal near-null physical-triple constant by a worst-fiber supremum cannot be uniform.

This is a proof-interface counterexample, not a counterexample to QFORM.

## 6. The completed ruled theorem identifies the correct local scale

The owner-pinned ruled theorem applies to (5.2) on its majority one-sheet side. With

`lambda1=1`, `lambda2=gamma`, `mu=1`,

its exact coefficient is

`C_gamma = int_0^(2pi)`
` [cos^2(theta)+gamma(1+sin^2(theta))]^(-1/2) dtheta.`                                   (6.1)

Using `sin u >= 2u/pi` on `[0,pi/2]`,

`C_gamma <= int_0^(2pi) [cos^2(theta)+gamma]^(-1/2)dtheta`
` <= 2 pi asinh(1/sqrt(gamma)).`                                                         (6.2)

Together with the explicit source lower bound (5.4),

`boxed( 2+log(2/gamma) <= C_gamma <= 2 pi asinh(1/sqrt(gamma)). )`                       (6.3)

So the selected physical triple has the genuine order

`C_gamma = Theta(log(1/gamma))`

at the level of its law-uniform ruled receiver. This is exactly the rank-two indefinite logarithm emerging as one majority curvature vanishes.

By contrast, if the vanishing curvature is the **minority** `mu`, Section 3 gives the uniform limit

`C_+ <= 2pi/sqrt(lambda1 lambda2)`.

Hence the near-null physical-triple problem has a sign-sensitive geometry:

- minority-null collar: majority one-sheet interval/tent mass is uniformly paid;
- majority-null collar: a logarithmic loss is real already for cap-one product uniforms;
- neither fact pays the minority/two-sheet submeasure.

## 7. Partner result applied as a method obstruction

The latest account03/B15 correction is essential here. If one prematurely splits the same near-null triple into a physical hyperbolic pair and an independent nonzero square and then uses conjugate `L^p` norms, the valid `p=3` estimate costs

`6 |gamma|^(-1/3)`                                                                           (7.1)

for the square coefficient `gamma` (after normalizing the physical cross coefficient to one). The translated-uniform sharpness theorem proves that the `gamma^(-1/3)` factor cannot be improved by the affine slope at the **one-coordinate** receiver stage.

But the joint ruled theorem improves that polynomial loss to the logarithmic coefficient (6.2), and removes it entirely when the vanishing curvature is the minority sign by (3.2). Therefore the partner correction and the ruled theorem together give a concrete design rule:

`do not condition away the coordinates that create the ruled three-dimensional geometry before paying the near-null branch.`

The missing improvement is not a better one-coordinate affine estimate; partner sharpness rules that out. It must come from retaining joint product geometry or from routing an outside smoothing coordinate before a worst conditional supremum.

## 8. Absolute continuity, essential boundedness, continuity: exact ledger

These implications remain distinct.

**Absolute continuity.** In fact product structure is not needed qualitatively. If a nonconstant quadratic polynomial `q` is applied to any absolutely continuous joint law, then `q_#P` is absolutely continuous. Choose a coordinate on which `q` depends. For almost every choice of the other coordinates, the resulting one-variable polynomial is nonconstant; the preimage of a null subset of `R` under a nonconstant one-variable polynomial is null. Fubini gives that `q^{-1}(N)` is Lebesgue-null for every null `N`, hence `P(q in N)=0`. Under the owner target `A` has rank at least three, so `q(x)=x^T A x` is nonconstant.

This qualitative fact does **not** imply an `L^infinity` density bound.

**Essential boundedness.** Equations (3.4), (3.5), and (5.7) are direct quantitative measure/convolution estimates. They do not follow from continuity.

**Continuity.** The current checked manuscript has an instance-dependent fixed-matrix `C_0` theorem in rank at least three, and the partner convolution branch gives `C_0` in (5.7). Neither supplies the universal owner constant. Conversely, the rough ruled majority submeasure in (3.4) is only claimed essentially bounded; this run does not infer a continuous representative for that submeasure from its interval cap.

So continuity is kept strictly downstream/separate from height throughout this report.

## 9. Exact remaining implication

The new result removes one false source of near-null difficulty: a small **minority** physical eigenvalue does not hurt the one-sheet majority coefficient at all when the two majority curvatures are controlled. The source-valid family (5.1) shows, however, that a small **majority** curvature can create a true logarithmic bad-fiber peak, while an outside original coordinate smooths the full target back to a universal constant.

Accordingly the first unpaid B15 implication is now:

**Integrate the outside product smoothing resource before the worst conditional supremum whenever the chosen physical triple has a vanishing majority curvature; equivalently, prove a product-provenance-sensitive compiler that combines the logarithmic one-sheet/two-sheet physical trace with an outside third resource without taking `sup_W`.**

The minority/two-sheet branch remains subject to the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction. A generic X-ray norm is not a substitute.

Globally the unrestricted theorem still also needs a structural guarantee that every target matrix either supplies such an aggregate receiver or enters one of the already-paid volume/hub/grouped-coordinate branches. No full solution or counterexample is claimed.
