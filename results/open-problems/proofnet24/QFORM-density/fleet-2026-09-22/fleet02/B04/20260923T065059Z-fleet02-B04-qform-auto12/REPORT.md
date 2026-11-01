SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-23T06:50:59Z.
attacking: exact/near double-star two-minor overlap geometry, closing the exact-star outer-square branch and quantifying the near-star entropy/ridge tradeoff on one physical matrix.

# fleet02/B04 — star endpoint closure and exact near-star entropy optimization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control: revision `2026-09-22.15`  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING LEMMA / EXPLICIT TARGET-VALID ESTIMATES / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Regularity claimed here: essential boundedness / absolute continuity in the stated branches; continuity is not asserted for arbitrary measurable input densities.

## 1. First unpaid implication

The first B04 debt after this run is

`QFORM-QUANTITATIVE-NEAR-STAR-TO-AGGREGATE-RANK2-OR-HUB-v1`:

> In a surviving full-target cut whose canonical physical two-minor law is concentrated near a row or column star, convert the small non-star two-volume into either (i) a product-preserving aggregate exact/regularized rank-two packet at target scale, or (ii) a genuine original-coordinate hub/square mechanism, without paying the logarithmic near-star entropy cost and without selecting a vanishing individual minor.

The exact-star endpoint itself is paid below. The new near-star computation shows that globally optimizing every admissible two-volume weight improves the natural power loss to a logarithm, but the logarithm can still diverge while a robust physical rank-two excision stays uniform. Thus the remaining issue is structural, not the rank-two Fourier endpoint.

Full QFORM remains OPEN.

## 2. Source-pinned inputs and corrections

Required Claude source consumed at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`:
`RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.
The exact input used is Theorem D's determinant/weighted-AM-GM step: arbitrary probability weights on nonzero physical minors are allowed, with determinant scale replaced by the entropy-adjusted volume

`G=exp(E_w log det^2+H(w))`.

The designated partner result actually applied is fleet03/B04 r26 at

`yspennstate/math-open-problems@85c3d540cf82ea6a6aca0f22f31811516a8b81aa`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T055256Z-fleet03-B04-qform-auto11-r26/REPORT.md`.

It proves `QFORM-KSAMPLE-MINOR-OVERLAP-ENTROPY-v1` and `QFORM-THREE-MINOR-STAR-DICHOTOMY-v1`. In particular, if the three-sample common-row overlap probability of the canonical squared-2-minor law is zero, every supported row pair contains one physical row, and deleting that row leaves rank at most one; hence the full cross block has rank at most two. The analogous statement holds for columns. For `k>=2`, its quantitative bound is

`||p_Q||_infinity <= C_k |a|^(-1/2) Z2^(-1/8) delta_k^(-1/(8k))`,

`C_k=2k sqrt(2e) [k/(2(k-1))]^(1/4)`,

when one untouched original scalar square of coefficient `a` is available.

I also use the completed fleet02/B04 r22 theorem
`QFORM-SQUARE-RANKR-TWOSIDED-CONTAMINATION-v1`, source commit
`8f8913581643a7e7bcbe7d8c178a2255194dfc3d`, which at exact cross rank two states

`||p_Q||_infinity <= C2 |a|^(-1/2) (sigma1 sigma2)^(-1/4)`,
`C2=8 sqrt(e)/3^(1/4)=10.022058057366376...`,

allowing arbitrary within-bank quadratic/affine contamination on both original-coordinate banks and arbitrary overlap of the square shift with those banks.

For the ridge comparison I use `QFORM-SQUARE-ASSISTED-RIDGE-L32-v1`, source commit
`b129377880c18fe011dd4513282f2e0b60e412e0`, and the fleet03/B04 checked ridge source. No source-refuted law-uniform scalar pointwise decay, arbitrary-joint coarea bound, conditional projection-cap moment, fiber supremum, post-rotation independence, uniformly good single minor, or universally rank-three physical cross cut is used.

## 3. Exact star endpoint: partner r26 plus exact-rank-two Fourier closes it

Let `M` be a physical cross block between disjoint ORIGINAL-coordinate product banks and define

`Z2=e2(M^T M)=sum_{|S|=|T|=2} det(M_ST)^2`.

Assume `Z2>0`. If either canonical three-sample overlap probability vanishes,

`delta3^r=0` or `delta3^c=0`,

then fleet03/B04 r26 gives `rank(M)<=2`. Positivity of `Z2` forces exact rank two. Hence, if `sigma1,sigma2` are its nonzero singular values,

`Z2=sigma1^2 sigma2^2`, so `sigma1 sigma2=sqrt(Z2)`.

Therefore the completed exact-rank-two theorem immediately gives:

### Corollary `QFORM-STAR-SUPPORT-SQUARE-CLOSURE-v1`

For

`Q=a[Z+m(X,Y,W)]^2+F(X,W)+G(Y,W)+2 X^T M Y`,

with `a!=0`, one untouched original coordinate `Z` of density cap one, disjoint original product banks `X,Y`, arbitrary outside original coordinates `W`, and arbitrary measurable within-bank contaminations/shift at the exact r22 scope,

`boxed:
 ||p_Q||_infinity
 <= [8 sqrt(e)/3^(1/4)] |a|^(-1/2) Z2^(-1/8).
`

This is aggregate: no individual minor or coefficient is inverted. Thus the exact row-star or column-star residue left by the partner's overlap theorem is no longer an analytic B04 obstruction when the surrounding structural reduction supplies one genuine original scalar square.

## 4. Exact-star target matrix: volume and ridge both fail, joint rank-two Fourier succeeds

Take

`M0 = [[2,1,1],[1,1,1],[1,1,1]].`

All nine physical cross entries are nonzero. Its only nonzero physical 2x2 minors are the four using the first row and first column, and every such determinant equals one. Consequently

`Z2=4`, `delta3^r=delta3^c=0`.

Every probability weight supported on nonzero physical 2x2 minors has first-row marginal one (and first-column marginal one). Hence **there is no admissible entropy-weighted rank-two law for any `q<2`**: the row condition `alpha_i<=q/2` fails maximally.

The two nonzero singular values of `M0` are

`2+sqrt(2)`, `2-sqrt(2)`,

with product two. Let

`Q0=Z^2+2 X^T M0 Y`.

Its symmetric coefficient matrix has exact spectrum

`{1, +(2+sqrt(2)), -(2+sqrt(2)), +(2-sqrt(2)), -(2-sqrt(2)), 0,0}`.

Thus it is genuinely non-diagonal, indefinite, and satisfies the target with exactly three eigenvalues of modulus at least one. The new exact-star corollary yields

`boxed:
 ||p_Q0||_infinity
 <= [8 sqrt(e)/3^(1/4)] 2^(-1/4)
 = 8.427512693903992... .
`

Now compare ridge on this **same physical matrix**. Put `g=gamma^2` and

`K=M0 M0^T (gI+M0 M0^T)^(-1)`.

Exact multiplication gives

`K_11=(6g+4)/(g^2+12g+4)=:k`,
`K_22=K_33=k/2`,
`theta=tr K=2k`.

Any square-assisted ridge exponent must satisfy

`q>=2 max_i K_ii=2k`.

But the completed square-assisted ridge gate requires `theta>4q/3`; here

`theta=2k<=q<4q/3`,

so the gate fails for **every** `gamma>0` and every admissible `q`. The direct ridge criterion is stronger and fails a fortiori. On this one target-valid matrix the current mechanisms therefore separate sharply:

- arbitrary admissible two-volume weighting: infeasible;
- direct or square-assisted ridge: no certificate at any scale;
- exact-rank joint product-Fourier plus the outer square: `<8.428`.

This is the requested actual obstruction/inequality comparison, not a claim that the target density itself is large.

## 5. Rank-three near-star family and global optimization of all admissible weights

Now perturb the exact star by

`M_eps = [[2,1,1],[1,1,1],[1,1,1+eps]],  eps>0.`

Every physical entry remains nonzero and

`det(M_eps)=eps`,

so this is exact rank three. The squared 2x2 minors, grouped by left row pair

`A={1,2}`, `B={1,3}`, `C={2,3}`,

have total group masses

`W_A=2`,
`W_B=2+4 eps+5 eps^2`,
`W_C=2 eps^2`,

and therefore

`Z2=4+4 eps+7 eps^2`.

The canonical row-pair probabilities are

`r_A=2/Z2`,
`r_B=(2+4eps+5eps^2)/Z2`,
`r_C=2eps^2/Z2`.

Let `w` be **any** probability weight on the nonzero physical 2x2 minors and let

`x_A,x_B,x_C`

be its row-pair marginal. Since each minor uses two of exactly three physical rows,

`alpha_1=1-x_C`, `alpha_2=1-x_B`, `alpha_3=1-x_A`.

Write

`ell=1-q/2=(2-q)/2`.

The admissibility condition `max alpha_i<=q/2` is therefore exactly

`x_A,x_B,x_C >= ell`.

In particular a weight exists iff `ell<=1/3`, equivalently

`q>=4/3`.

Let `nu` be the canonical squared-minor law. Relative entropy decomposes exactly by the row-pair partition:

`D(w||nu)
 =D(x||r)+sum_{S=A,B,C} x_S D(w(.|S)||nu(.|S)).`

Hence at every fixed row-pair mass `x`, the unique entropy-optimal choice preserves the canonical conditional law inside each row-pair class. Since

`log G2(w)=log Z2-D(w||nu)`,

the full global optimization over minor weights reduces to the three-point KL projection

`min D(x||r)` subject to `x_A,x_B,x_C>=ell`.

Because `r_C<r_A<r_B`, the solution is explicit. Put

`ell0 = r_A/(2r_A+r_B)=2/(6+4eps+5eps^2)`.

For `0<ell<=ell0`, only the rare non-star class is pushed up:

`x_C=ell`,
`x_A=(1-ell) r_A/(1-r_C)`,
`x_B=(1-ell) r_B/(1-r_C)`,

and

`D_min(ell)=D_Ber(ell || r_C)`.

For `ell0<=ell<=1/3`, both smaller classes bind:

`x_A=x_C=ell`, `x_B=1-2ell`,

with

`D_min(ell)
 = ell log(ell/r_A)
 +(1-2ell) log((1-2ell)/r_B)
 +ell log(ell/r_C).`

Therefore the **globally optimal** entropy-adjusted two-volume at exponent `q=2(1-ell)` is

`boxed:
 G2,opt(ell)=Z2 exp[-D_min(ell)].
}`

The corresponding outer-square density certificate from the preceding B04 theorem is

`boxed:
 B_vol(ell)
 =2^(5/4) sqrt(e) ell^(-1)(1-ell)^(-1/4)
  Z2^(-1/8) exp[D_min(ell)/8],
  0<ell<=1/3.
}`

This solves the admissible-weight optimization exactly for the whole family, not just for a symmetric ansatz.

On the first branch,

`d/dell log B_vol
 = -1/ell +1/[4(1-ell)]
   +(1/8) log[ell(1-r_C)/(r_C(1-ell))],`

and

`d^2/dell^2 log B_vol
 =1/ell^2+1/[4(1-ell)^2]
  +(1/8)(1/ell+1/(1-ell))>0.`

The second branch is also strictly log-convex because

`D_min''(ell)=2/ell+4/(1-2ell)>0`.

Thus the global optimizer is unique.

## 6. Near-star asymptotics: entropy reweighting reduces a power loss to a logarithm

Let

`r=r_C=2eps^2/Z2`, `L=log(1/r)`.

If `L>=32`, choose the admissible first-branch point

`ell=8/L`, `q=2-16/L`.

Because `ell<=1/4<ell0` for sufficiently small eps,

`D_Ber(ell||r)
 <= ell log(ell/r)
 <= ell L=8`;

the omitted Bernoulli term is nonpositive. Hence

`B_vol(8/L)
 <= 2^(5/4) e^(3/2) (L/8)(1-8/L)^(-1/4) Z2^(-1/8).`

So the optimized two-volume certificate is only

`O(log(1/r))=O(log(1/eps))`,

whereas keeping the partner's first `k=3` / `q=4/3` gate forces the rare class to mass `1/3` and gives a power cost `eps^(-1/12)`.

This is the useful mathematical lesson: a near-star should not be paid at a fixed fractional exponent. The Fourier exponent itself must move toward the endpoint `q=2` at a rate inverse-logarithmic in the rare volume.

## 7. Concrete target-valid stress point and designated-partner application

Take

`eps=10^(-12)`

and

`Q_eps=Z^2+2 X^T M_eps Y`.

The matrix `M_eps` is symmetric positive definite by Sylvester's criterion: its leading principal minors are `2`, `1`, `eps`. Also

`M_eps=M0+eps e_3e_3^T`,

so its largest eigenvalue is at least `2+sqrt(2)>1`. Therefore the full symmetric coefficient matrix of `Q_eps` has the eigenvalues `1` and `+/-` the three eigenvalues of `M_eps`; in particular it is indefinite and has at least the three target-scale eigenvalues

`1`, `+lambda_max(M_eps)`, `-lambda_max(M_eps)`.

All nine cross entries are nonzero.

At this eps,

`Z2=4.000000000004...`,
`r_C=4.999999999995... x 10^(-25)`,
`L=55.955189412418044...`,
`ell0=0.3333333333331111...`.

The unique zero of the first-branch derivative is

`ell*=0.14163448612643018...`,
`q*=1.7167310277471396...`,

and the globally optimized all-weight certificate is

`boxed:
 ||p_Qeps||_infinity <= 61.89826829192555... .
}`

For comparison, the fixed `q=4/3` optimum is

`104.06624845711598...`.

Now apply the completed **designated partner** fleet03/B04 r26 theorem directly. For the triangle of row-pair types with probabilities `r_A,r_B,r_C`, the common intersection of `k` sampled pairs is empty iff all three pair types appear. Hence

`delta_k
 =1-(r_A+r_B)^k-(r_A+r_C)^k-(r_B+r_C)^k
   +r_A^k+r_B^k+r_C^k.`

At `eps=10^(-12)`, its `k=7` inequality gives

`delta_7=3.390624999996609375... x 10^(-24)`

and therefore

`boxed:
 ||p_Qeps||_infinity <= 62.96716222831744... .
}`

This is an actual equation-level application of the partner theorem. It lies within about `1.8%` of the globally optimized continuous-q/all-weight certificate; the discrete partner choice `q_7=12/7` is close to `q*`. Asymptotically the partner family has the same mechanism: choosing `k` of order `L/8` turns the rare-edge power penalty into a logarithmic one.

## 8. Ridge and physical-rank-two comparisons on the identical near-star matrix

### Direct ridge

For every ridge matrix on a three-row physical bank, if

`max_i K_ii<=q/2`,

then

`theta=tr K<=3q/2<2q`.

Thus the direct ridge density theorem's condition `theta>2q` is impossible on this three-row realization at every regularization scale.

### A valid square-assisted ridge certificate

For `M_eps`, write `g=gamma^2`. Exact algebra gives

`D0=e^2 g^2+7e^2 g+e^2+2e g^2+4e g+g^3+12g^2+4g`,

where here `e` denotes `eps`, and

`K_11=(5e^2g+e^2+4eg+6g^2+4g)/D0`,

`theta=(e^2g^2+14e^2g+3e^2+2eg^2+8eg+12g^2+8g)/D0`,

`D=det(I+M_eps M_eps^T/g)=D0/g^3`.

For `0<eps<1`, `K_11` is the largest physical diagonal. At the concrete scale

`gamma=eps/4`, `g=eps^2/16`, `q=2K_11`,

the square-assisted ridge hypotheses hold. At `eps=10^(-12)`:

`K_11=0.99999999999999999999999988125...`,
`theta=2.7999999999998399999999996845...`,
`q=1.9999999999999999999999997625...`,

and the completed ridge formula gives the valid but much weaker estimate

`||p_Qeps||_infinity <= 1236.0028842696313... .`

No claim is made that this chosen ridge scale is globally optimal; it is an actual same-matrix certificate. The direct ridge route has no certificate at all, while optimized volume weighting is already below 62.

### Physical rank-two excision

This stress family also proves that even the logarithmic optimized-volume cost is not intrinsic. Condition on the second original left coordinate and retain rows 1 and 3. The resulting physical `2 x 3` cross packet has exact rank two and aggregate two-volume

`det(C_eps C_eps^T)=2+4eps+5eps^2`.

Thus the nonzero singular-value product is

`Delta2=sqrt(2+4eps+5eps^2)`.

The r22 exact-rank-two theorem, with the same untouched outer scalar `Z`, permits all affine contamination generated by the conditioned coordinate and yields

`boxed:
 ||p_Qeps||_infinity
 <= [8 sqrt(e)/3^(1/4)] (2+4eps+5eps^2)^(-1/8).
}`

At `eps=10^(-12)` this is

`boxed: ||p_Qeps||_infinity <= 9.190267759834622... .`

Hence on the identical genuinely rotated indefinite target form:

- globally optimized admissible two-volume weights: `61.8983`;
- designated partner k-sample weight (`k=7`): `62.9672`;
- one valid square-assisted ridge scale: `1236.003`;
- direct ridge: impossible on this 3-row bank;
- robust original-coordinate aggregate rank-two excision: `9.1903`.

The last line is why the next unpaid implication must be a structural near-star-to-aggregate-rank-two/hub theorem, rather than further optimization of the same full-block volume certificate.

## 9. What changed in the proof map

1. The partner's exact-star alternative is now analytically closed by the exact-rank-two joint Fourier theorem whenever an untouched original scalar square is available.
2. For a quantitative near-star, the full entropy optimization can be solved exactly. The optimal Fourier exponent approaches `2` and converts a fixed-exponent power loss into a logarithm.
3. The partner's general `k`-sample construction nearly realizes the global optimum automatically; at the explicit stress point its `k=7` bound is within 1.8% of the exact all-weight optimum.
4. Nevertheless a product-preserving physical rank-two excision can be uniformly much better. Therefore an exhaustive proof should route the near-star geometry to aggregate rank-two/hub structure before paying even the logarithmic full-block penalty.

This is a supporting result, not a proof of the unrestricted conjecture. Independent review of the new KL projection and near-star algebra is pending.
