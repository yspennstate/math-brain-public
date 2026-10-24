SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T05:50:35Z.
attacking: determinant-weighted disjoint pair mass -> a q=1 entropy weight by a symmetric KL-halving identity, then splice account02/B04's rank-two half-Riesz theorem.

# account01/B04 auto13 — disjoint E2 entropy halving and square-assisted product Fourier smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`.
Fresh owner control before publication: revision `2026-09-22.15`, QFORM only; full conjecture OPEN.
Status: `ESSENTIAL_STEP_APPLIED / NEW_SUPPORTING_THEOREM / FULL_TARGET_OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The new theorem below is an aggregate-before-inversion product-Fourier statement. It does not use law-uniform pointwise quadratic-phase decay, independence after a spectral rotation, arbitrary-joint coarea, a worst conditional projection-density cap, a uniformly good local minor, compact support, log-concavity, moments, or connected support. Same-bank quadratic curvature is retained through the partner theorem.

The density conclusion of the scalar-square branch is essential boundedness / absolute continuity. Continuity is **not** claimed for that branch. The unrestricted three-large-eigenvalue conjecture is not proved here.

## 1. Source boundary and partner theorem actually used

The designated partner result used at equation level is account02/B04's completed

`QFORM-ENTROPY-WEIGHTED-RANK2-HALFRIESZ-v1`,

current source report

`yspennstate/math-open-problems@10a74bd7d75466fe46f4ff6ecf3362fba6cb2e5d`
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260923T052139Z-account02-B04-qform-auto11/REPORT.md`

(with subsequent arithmetic checks committed separately by that worker).

Its exact input is as follows. Let `I,J` be disjoint sets of ORIGINAL independent coordinates and, after conditioning all other original coordinates, write

`R=F(X_I)+2 X_I^T M X_J+G(X_J)`,

where `F,G` may contain arbitrary within-bank quadratic and affine terms. For any probability law `w` on nonzero physical `2 x 2` minors `M[S,T]`, set

`G_2(w)=exp( sum_(S,T) w_(S,T) log det(M[S,T])^2 + H(w) )`.

If every row inclusion marginal is at most `q/2`, `1<=q<2`, then

`sup_s E |R-s|^(-1/2)
 <= [4 sqrt(2e) q^(-1/4)/(2-q)] G_2(w)^(-1/8)`.          (1.1)

If one further untouched original coordinate `Z` is independent of the residual variables and

`Q=a[Z+m]^2+R`, `a!=0`,

then

`||p_Q||_infinity
 <= [4 sqrt(2e) q^(-1/4)/(2-q)] |a|^(-1/2) G_2(w)^(-1/8)`. (1.2)

The purpose of this run is to construct a useful admissible weight `w` from a completely canonical statistic of the physical cross block, without solving a convex program and without paying a reciprocal single minor.

## 2. Symmetric conditioning halves the entropy cost

The key point is elementary but quantitatively important.

### Lemma 2.1 — `QFORM-SYMMETRIC-DISJOINT-KL-HALVING-v1`

Let `mu` be any probability law on finite subsets of a ground set. Draw `S,S'` independently from `mu`, let

`D={S cap S'=empty}`, `delta=P(D)>0`,

and let `Q` denote the conditional law `Law(S,S' | D)`. Let `nu` be either marginal of `Q` (the two marginals agree by symmetry). Then

`D_KL(nu || mu) <= (1/2) log(1/delta)`.                         (2.1)

If all sets in the support of `mu` have the same size `k`, then every coordinate inclusion marginal under `nu` is at most `1/2`.

#### Proof

Because `Q` is just `mu x mu` restricted to `D` and renormalized,

`D_KL(Q || mu x mu)=log(1/delta)`.                              (2.2)

Both marginals of `Q` equal `nu`. The KL chain rule relative to the product reference gives the exact identity

`D_KL(Q || mu x mu)
 = I_Q(S;S') + D_KL(nu||mu)+D_KL(nu||mu)
 = I_Q(S;S') + 2D_KL(nu||mu)`.                                 (2.3)

Mutual information is nonnegative, so (2.1) follows.

For any physical index `i`, disjointness gives

`1_{i in S}+1_{i in S'}<=1` under `Q`.

Taking expectations and using the exchangeability of the two coordinates,

`2 P_nu(i in S)<=1`.

Hence every inclusion marginal is at most `1/2`. QED.

The factor `1/2` in (2.1) is stronger than ordinary data processing, which would only give `D_KL(nu||mu)<=log(1/delta)`. This factor propagates directly into the density exponent below.

## 3. Global two-volume disjointness theorem

Let `M=A[I,J]` be any physical cross block between disjoint banks of original independent coordinates. Put

`Z_2=e_2(M^T M)
    =sum_(|S|=|T|=2) det(M[S,T])^2`.                            (3.1)

Assume `Z_2>0`. Define the canonical full two-volume law

`w^0_(S,T)=det(M[S,T])^2/Z_2`,                                 (3.2)

and its row-pair marginal

`mu_S=sum_T w^0_(S,T)`.                                        (3.3)

Draw `S,S'` independently from `mu` and define the determinant-weighted disjointness mass

`delta_2=P(S cap S'=empty)`.                                    (3.4)

### Theorem 3.1 — `QFORM-DISJOINT-E2-ENTROPY-HALVING-v1`

If `delta_2>0`, then for the full residual quadratic-plus-affine form

`R=F(X_I)+2X_I^T M X_J+G(X_J)`

with arbitrary same-bank curvature and affine terms,

`boxed:
 sup_s E|R-s|^(-1/2)
 <=4 sqrt(2e) Z_2^(-1/8) delta_2^(-1/16).`                     (3.5)

Consequently, if one untouched original coordinate supplies

`Q=a[Z+m]^2+R`, `a!=0`,

then the law of `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(2e) |a|^(-1/2) Z_2^(-1/8) delta_2^(-1/16).`          (3.6)

No continuity claim is made in (3.6).

#### Proof

Condition the iid pair `(S,S')` from (3.4) on disjointness and let `nu` be the first marginal. By Lemma 2.1 every physical row inclusion marginal of `nu` is at most `1/2`.

For every row pair `S` with `mu_S>0`, keep the canonical conditional column law

`w^0(T|S)=w^0_(S,T)/mu_S`,

and lift `nu` to a probability law on full nonzero minors:

`pi_(S,T)=nu_S w^0(T|S)`.                                      (3.7)

The row inclusion marginals of `pi` are precisely those of `nu`, hence satisfy the partner theorem at the endpoint `q=1`.

The lift preserves conditional column distributions, so the KL chain rule gives

`D_KL(pi||w^0)=D_KL(nu||mu)
 <=(1/2)log(1/delta_2)`.                                       (3.8)

The entropy-adjusted determinant currency has the exact Gibbs form

`log G_2(pi)
 =log Z_2-D_KL(pi||w^0)`.                                      (3.9)

Therefore

`G_2(pi)>=Z_2 delta_2^(1/2)`.                                  (3.10)

Apply account02/B04's theorem (1.1) with `q=1` and use (3.10):

`sup_s E|R-s|^(-1/2)
 <=4sqrt(2e) [Z_2 delta_2^(1/2)]^(-1/8)
 =4sqrt(2e) Z_2^(-1/8) delta_2^(-1/16)`.

This is (3.5). Applying the partner scalar-square transducer (1.2) gives (3.6). QED.

The exponent `delta_2^(-1/16)` is deliberately weak: disjointness may be small, but its entropy cost enters only through one half-power and then one eighth-root.

## 4. Exact residual-volume identity: the complement is a near-pair/hub certificate

The same `delta_2` has a direct deterministic interpretation. For a fixed row pair `S`,

`P(S' cap S=empty | S)
 =sum_(S' subset S^c) mu_(S')
 =E_2(M[S^c,J])/Z_2`.                                          (4.1)

The last equality is Cauchy--Binet summed over all column pairs. Averaging in `S~mu` gives the exact identity

`boxed:
 delta_2
 =E_(S~mu)[ E_2(M[S^c,J])/Z_2 ].`                             (4.2)

Therefore some actual physical row pair `S` with `mu_S>0` obeys

`boxed:
 E_2(M[S^c,J])<=delta_2 Z_2.`                                  (4.3)

More quantitatively, Markov gives

`mu{S: E_2(M[S^c,J])<=2delta_2 Z_2}>=1/2`.                     (4.4)

So the alternative to the new smoother is not an unspecified bad marginal: small disjointness says that deleting a determinant-weighted physical pair destroys almost all remaining two-volume. This is precisely the kind of pair/hub concentration that the current mixed-hub and grouped-coordinate branches are designed to consume.

For reference, the already-proved pair-Pluecker collision identity gives, if `alpha_i=P_mu(i in S)`,

`delta_2=1-sum_i alpha_i^2+sum_S mu_S^2`.                       (4.5)

The already-completed zero-disjointness classification says that when the support comes from a genuine rank-two row frame and `delta_2=0`, the nonzero pair-support graph is a star or a triangle. I use that as prior fleet structure, not as a new claim of this report. The remaining issue for the full theorem is a quantitative near-star/near-triangle routing together with the outer zero/near-zero-pivot cases.

## 5. Actual application to account02/B04's rotated indefinite stress matrix

Use the partner's explicit physical rank-two matrix. Let `theta=pi/8`,

`V=[[cos theta,-sin theta],[sin theta,cos theta]]`,

and let the four left row vectors before the right rotation be

`r1=8e1`,
`r2=e2`,
`r3=(e1+e2)/sqrt(2)`,
`r4=(e1-e2)/sqrt(2)`.

Set `M=R V`. Every physical entry of `M` is nonzero. Right multiplication by `V` preserves singular values and absolute `2x2` minors. The six squared row-pair minors are exactly

`d12^2=64`,
`d13^2=d14^2=32`,
`d23^2=d24^2=1/2`,
`d34^2=1`,                                                     (5.1)

and hence

`Z_2=130`.                                                       (5.2)

The partner proved that `M^T M` has eigenvalues `65,2`. For

`Q_*=Z^2+2X^T M Y`,                                             (5.3)

its symmetric coefficient matrix has exact spectrum

`{1,+sqrt(65),-sqrt(65),+sqrt(2),-sqrt(2),0,0}`.                (5.4)

Thus this is a genuinely rotated indefinite target-valid matrix with five eigenvalues of modulus at least one and all eight physical cross coefficients nonzero.

### 5.1 Generic disjointness certificate

The canonical row-pair law is proportional to (5.1). In four vertices, the only disjoint pairs are complements, so

`delta_2
 =2[64*1+32*(1/2)+32*(1/2)]/130^2
 =192/16900
 =48/4225
 =0.01136094674556213... .`                                    (5.5)

The generic entropy-halving lower bound gives

`G_2(pi)>=130 sqrt(delta_2)=sqrt(192)=8sqrt(3)`.                (5.6)

Therefore Theorem 3.1 already gives, for every admissible product input law,

`||p_(Q_*)||_infinity
 <=4sqrt(2e)(8sqrt(3))^(-1/8)
 =2^(17/8) sqrt(e) 3^(-1/16)
 =6.714534402560991... .`                                      (5.7)

This uses no optimization over minor weights.

### 5.2 The conditioned-disjoint weight itself is almost optimal

Here the first marginal of the conditioned-disjoint pair law can be written exactly:

`nu_12=nu_34=1/3`,
`nu_13=nu_14=nu_23=nu_24=1/12`.                                (5.8)

Every physical row inclusion marginal is exactly `1/2`, as guaranteed abstractly by Lemma 2.1. Direct substitution in the determinant-entropy functional gives

`G_2(nu)=3*2^(10/3)=30.238105197476955... .`                    (5.9)

Applying the partner theorem at `q=1` therefore sharpens (5.7) to

`boxed:
 ||p_(Q_*)||_infinity
 <=4sqrt(2e)[3*2^(10/3)]^(-1/8)
 =2^(25/12) sqrt(e) 3^(-1/8)
 =6.090499451399227... .`                                      (5.10)

The partner's full convex optimization over all admissible weights gives `6.047536285398243...`; hence the canonical disjointness construction lands within about `0.71%` of the globally optimized certificate while requiring only the physical volume law and one conditioning operation. By contrast, the unmodified canonical volume law has a nearly-coloop row marginal `64/65` and its first admissible q-certificate is about `139.247856557` on the same matrix.

This is an actual application of the designated partner theorem to a genuinely rotated indefinite target form, not merely a restatement of the partner result.

## 6. Fleet-facing byproduct: the same KL halving improves the order-three disjointness penalty

The entropy-halving lemma is order-independent. The completed account03/B02 theorem `QFORM-GLOBAL-VOLUME-DISJOINT-ENTROPY-L1-v1` conditions two iid determinant-weighted row triples on being disjoint. Its published proof used the data-processing estimate

`D_KL(nu||mu)<=log(1/delta_3)`

and consequently obtained

`||p_Q||_infinity<=3e delta_3^(-1/6) E_3(M)^(-1/6)`.

The exact identity (2.3) improves that KL input to

`D_KL(nu||mu)<=1/2 log(1/delta_3)`.

Keeping every other step of that completed proof unchanged replaces the penalty by

`boxed:
 ||p_Q||_infinity
 <=3e delta_3^(-1/12) E_3(M)^(-1/6).`                           (6.1)

In that order-three branch the characteristic function remains L1, so its density conclusion remains continuous. This is a corollary of the present entropy identity plus the already-completed B02 calculation; it is not a full-target theorem.

## 7. Remaining implication

The first unpaid B04 implication is now

`QFORM-E2-SMALL-DISJOINTNESS-PAIR-OR-HUB-ROUTING-v1`:

> Starting from the bare hypothesis that A has at least three eigenvalues of modulus at least one, combine the existing scalar/pair/ridge reductions with (3.6)-(4.4) to prove that either a genuine original-coordinate scalar-square branch has universal aggregate currency
>
> `|a|^4 Z_2 delta_2^(1/2) >= c`,
>
> or small `delta_2` forces the physical pair/hub concentration into an already-paid mixed-hub, grouped-bank, pair-log, null-coloop, or zero-diagonal branch.

The combination in the displayed currency is exactly what (3.6) needs after raising its reciprocal factor to the eighth power. Nothing in this report claims that the bare spectral hypothesis already forces that currency. The zero/near-zero outer scalar pivot remains a separate structural debt.

Full QFORM: OPEN.
Full-target continuity: OPEN.
New scalar-square branch continuity: NOT PROVED.
Independent end-to-end review of the new theorem: NOT YET RECORDED.

## 8. Reproducible exact arithmetic

The only numerical constants used above come from exact expressions:

`delta_2=48/4225`,
`Z_2=130`,
`G_generic=8sqrt(3)`,
`G_conditioned=3*2^(10/3)`,
`B_generic=2^(17/8)*sqrt(e)*3^(-1/16)=6.714534402560991...`,
`B_conditioned=2^(25/12)*sqrt(e)*3^(-1/8)=6.090499451399227...`.

These numerics are checks of exact formulas, not empirical evidence for the conjecture.

Privacy/source review: changed-file allowlist for the mathematical repository consists only of this report path; it contains mathematical statements and repository source pins, no credentials, scheduler IDs, private personal data, or unrelated material. No public release, remote workflow, paid model/API call, permission change, scheduler mutation, email, or notification change was performed.
