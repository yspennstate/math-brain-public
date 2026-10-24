# account01/B11 — independent-pair hyperbolic-square smoothing and double-null packet closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control revision at start:** `2026-09-22.5`  
**Run:** `QFORM-B11-20260922T151340Z-r11`  
**Assignment:** indefinite signatures  
**Outcome:** `ESSENTIAL_STEP_APPLIED / TARGET_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Target and conditional end-to-end argument

The full target remains: for every dimension, every vector of independent real coordinates having probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal bound for the density of `Q=X^T A X`, or give a genuine counterexample. Continuity of the density is a separate stronger requested conclusion.

The current indefinite architecture is now:

1. the rank-two opposite-sign saddle is correctly retained as a logarithmic endpoint obstruction;
2. previous B11 work controls a physical rank-two mixed packet plus a scalar third direction whenever one of the two shear curvatures is nonzero;
3. the assigned partner `account02/B11` controls heavy exact-rank-three rows away from the null cone and proves dimension-free density caps for one- and two-dimensional isotropic projections;
4. the partner's newest Walsh-bank construction controls one nontrivial genuinely dependent null-heavy family by aggregating original coordinates before applying a three-variable theorem;
5. this report proves a different endpoint theorem: if one null direction is genuinely independent of the transverse two-dimensional projected pair, then the square in that pair removes the logarithmic saddle singularity with an explicit dimension-free bound. In particular the entire arbitrary Parseval-frame null-heavy chamber at leverage exactly one is now controlled, without any Walsh/sign-bank hypothesis;
6. this report also closes the explicit simultaneous-double-null mechanism witness from the preceding B11 run, and more generally the monomial rank-two mixed packet, by showing that two independent logarithmic product packets convolve to a bounded continuous density.

The first remaining local debt is therefore not the exact `c=1` null-heavy endpoint and not the displayed double-null witness. It is the genuinely overlapping null-heavy chamber `1/2 <= c < 1`, where the residual first-direction coordinates overlap the two transverse directions, together with the global problem of extracting/aggregating such packets without paying a single tiny physical minor. Extra nonzero spectrum remains a separate nonseparable debt.

No pointwise law-uniform Fresnel decay, post-rotation independence, conditional-cap-as-independence replacement, fiberwise trace bound, or best-principal-minor selection is used.

## 2. Assigned partner result actually applied

Newest completed assigned partner source read before this report:

`yspennstate/math-open-problems@047e3c1cb33c6ed605bbc4a014371fa63dd84538`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260922T145132Z-b11-qform-r18-7f3c1a2d/REPORT.md`.

That report supplies the Walsh-bank null-heavy theorem and cites the preceding self-contained projection estimates. The preceding completed partner source

`yspennstate/math-open-problems@245a4e2a4414294fbb20b9dd4f292f6b001e5aa2`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260922T135203Z-b11-qform-6080e0b3/REPORT.md`

proves the estimate used quantitatively below:

> if `(V,W)=sum_i b_i X_i` is a two-dimensional isotropic projection of independent cap-one inputs, i.e. `sum_i b_i b_i^T=I_2`, then `(V,W)` has a joint density `h` with `||h||_infinity <= e`.

It also proves the one-dimensional normalized projection cap `sqrt(e)`. The actual application in Section 4 is `K=e`, yielding the explicit bound `6 e^(2/3)`.

## 3. Main analytic lemma: an independent scalar smooths a bounded transverse pair

### Theorem 3.1 — hyperbolic-square smoothing with dependence inside the pair

Let `S` be independent of the pair `(V,W)`. Suppose `S` has probability density `f_S` with

`||f_S||_infinity <= M`,

and `(V,W)` has a joint probability density `h` with

`||h||_infinity <= K`.

For nonzero real `a,b`, set

`Y = 2 a S W + b V^2`.

Then `Y` has a bounded continuous density vanishing at infinity and

`||p_Y||_infinity <= 6 (M K)^(2/3) |a|^(-2/3) |b|^(-1/3)`.          (3.1)

Crucially, **no independence between `V` and `W` is assumed**. Only the scalar `S` is independent of the whole transverse pair.

### Proof

Let

`m(w)=integral_R h(v,w) dv`.

For almost every `w` with `m(w)>0`, the conditional density of `V|W=w` is

`k_w(v)=h(v,w)/m(w)`,

so

`||k_w||_infinity <= B_w:=K/m(w)`.                              (3.2)

Because `S` is independent of `(V,W)`, conditioning on `W=w` does not change the density of `S`.

Put

`L_w=2 a w S`, `Z_w=b V^2`.

For `w!=0`, `L_w` has a probability density `ell_w` satisfying

`||ell_w||_infinity <= A_w:=M/(2|a w|)`.                       (3.3)

The conditional density `g_w` of `Z_w` obeys, on its one-sided support,

`g_w(z) <= B_w |b|^(-1/2) |z|^(-1/2)`.                        (3.4)

Indeed the two square roots contribute at most `2B_w` and the Jacobian is `2 sqrt(|b z|)`.

Since `g_w` is a probability density,

`||ell_w*g_w||_infinity <= A_w`.                               (3.5)

A second estimate uses a split at distance `r>0`. From (3.4),

`integral_{|z|<=r} g_w(z) dz <= 2 B_w |b|^(-1/2) sqrt(r)`,

while

`sup_{|z|>r} g_w(z) <= B_w |b|^(-1/2) r^(-1/2)`.

Therefore

`||ell_w*g_w||_infinity
 <= B_w |b|^(-1/2) [2 A_w sqrt(r)+r^(-1/2)]`.

Taking `r=(2A_w)^(-1)` gives

`||ell_w*g_w||_infinity
 <= 2 B_w |b|^(-1/2) sqrt(2A_w)`.                              (3.6)

Multiplying by the marginal weight `m(w)`, (3.5)--(3.6) give

`m(w) p_{Y|W=w}(y)
 <= min{ m(w) M/(2|a w|),
          2 K sqrt(M) |a|^(-1/2)|b|^(-1/2)|w|^(-1/2) }`.       (3.7)

For any `R>0`, integrate the second term over `|w|<=R` and the first over `|w|>R`. Since `integral m(w)dw=1`,

`p_Y(y)
 <= 8K sqrt(M)|ab|^(-1/2) sqrt(R) + M/(2|a|R)`.               (3.8)

The optimum is attained at

`sqrt(R)=[ sqrt(M)/(8K) * sqrt(|b|/|a|) ]^(1/3)`,

and substitution yields exactly

`p_Y(y) <= 6(MK)^(2/3)|a|^(-2/3)|b|^(-1/3)`.

This proves the essential bound.

For continuity, for almost every `w!=0`, both `ell_w` and `g_w` are `L^1` densities, hence their convolution is continuous and tends to zero at infinity. For a fixed `R`, the right side of (3.7), using the `|w|^(-1/2)` term on `|w|<=R` and the `m(w)/|w|` term outside, is integrable in `w` and independent of `y`. Dominated convergence therefore shows that the mixture `p_Y` is continuous; the same domination plus the `C_0` property of the conditional convolutions gives vanishing at infinity. QED.

### What this says about the logarithmic rank-two control

For `S,W` independent uniform variables on `[-1/2,1/2]`, the rank-two saddle `2SW` has density

`p_{2SW}(q)=log(1/(2|q|)),  0<|q|<1/2`,                       (3.9)

so it is genuinely unbounded at zero. Theorem 3.1 does not erase this control example. It says that adding the third quadratic direction `bV^2`, when the transverse pair `(V,W)` has bounded joint density and is independent of `S`, converts the logarithmic endpoint into a bounded continuous density. The mechanism is a quantitative split between small `|W|` and large `|W|`: the square-root singularity costs `|W|^(-1/2)` near zero, which is integrable, while away from zero the hyperbolic scalar itself supplies the `1/|W|` cap.

## 4. Direct application to the arbitrary null-heavy Parseval frame at leverage one

Consider the exact-rank-three canonical indefinite form

`Q=2 Z1 Z3 + Z2^2`,                                            (4.1)

whose spectral matrix has eigenvalues `{1,1,-1}`. Write the three spectral coordinates as an original-coordinate Parseval frame. Suppose one physical row is

`r_0=(1,0,0)`.                                                  (4.2)

Because the frame is Parseval, `sum_i r_i r_i^T=I_3`. Equality in the first coordinate of (4.2) forces every residual row to have first component zero. Hence

`Z1=X0`,                                                        (4.3)

while `(Z2,Z3)` depends only on the remaining original coordinates. Therefore `Z1` is genuinely independent of the whole pair `(Z2,Z3)`.

Moreover the two transverse coefficient vectors are orthonormal on the residual original coordinates. Applying the completed `account02/B11` two-dimensional projection theorem gives the **actual partner inequality**

`||p_(Z2,Z3)||_infinity <= e`.                                 (4.4)

Theorem 3.1 with `(S,V,W)=(Z1,Z2,Z3)`, `M=1`, `K=e`, `a=b=1` yields

`boxed: ||p_Q||_infinity <= 6 e^(2/3) < 11.687`.                (4.5)

The density is continuous and vanishes at infinity.

This covers **every** residual Parseval frame at null-heavy leverage exactly one. No sign-pattern banks, finite support, moments, log-concavity, Gaussianity, or independence after a spectral rotation are assumed. Negating the form gives the dual signature `(+,-,-)` with the same bound.

### Support-separated extension for `c>=1/2`

More generally let the heavy row be `r_0=(sqrt(c),0,0)`, `c>=1/2`. Write the residual first-direction coefficient vector as `alpha=(alpha_i)` and the transverse vectors as `beta=(beta_i)`, `gamma=(gamma_i)`. If the support of `alpha` is disjoint from the union of the supports of `beta,gamma`, then

`S=Z1=sqrt(c)X0+sum alpha_i X_i`

is independent of `(V,W)=(Z2,Z3)`. Since the first summand has density cap `c^(-1/2)`, convolution gives

`M<=c^(-1/2)`.                                                  (4.6)

The transverse pair remains isotropic, so the partner theorem again gives `K<=e`. Thus

`||p_Q||_infinity <=6 e^(2/3)c^(-1/3)
                  <=6 e^(2/3) 2^(1/3) <14.724`.                (4.7)

This is an exact support-separation theorem only. No approximation argument is asserted when the supports merely overlap weakly; without moments, a small coefficient does not by itself justify dropping that coordinate.

## 5. A second endpoint identity: two logarithmic packets smooth each other

The preceding B11 run found the simultaneous double-null target-class matrix

`q=2(u1+x)(v1+x)+2u2v2`,                                      (5.1)

with spectrum `{3,1,-1,-1,0}`. It was used only to refute the shortcut that one shear curvature must be nonzero. Here it is controlled uniformly for all admissible input laws.

### Lemma 5.1 — product density has a universal `L^2` bound

If `U,V` are independent real random variables with probability densities bounded by one, then the product `P=UV` satisfies

`||p_P||_2 <= 2 sqrt(2)`.                                      (5.2)

Proof. For almost every `z`,

`p_P(z)=integral f_U(u) |u|^(-1) f_V(z/u) du`.

For fixed `u`, the `L^2(dz)` norm of `|u|^(-1)f_V(z/u)` is `|u|^(-1/2)||f_V||_2<=|u|^(-1/2)`. Minkowski gives

`||p_P||_2 <= integral f_U(u)|u|^(-1/2)du`.

Under `0<=f_U<=1` and total mass one, the bathtub principle maximizes the last integral by taking density one on `[-1/2,1/2]`, where the integral is `2sqrt(2)`. QED.

Hence for any `b!=0`,

`||p_{2bUV}||_2 <= 2/sqrt(|b|)`.                               (5.3)

### Corollary 5.2 — monomial double-null mixed packet

Condition on a scalar coordinate `x`. Suppose the two-sided double-null quadratic part has `C=D=0`, and after merely permuting physical `v` coordinates its mixed block is diagonal

`B=diag(b1,b2)`, `b1 b2!=0`,                                  (5.4)

with simultaneous double-null identity

`a=2 s^T B^(-1) r`.                                            (5.5)

Arbitrary affine terms are allowed. Completing the two bilinear products conditional on `x` writes the conditional form, up to an `x`-dependent additive constant, as

`2b1 U1'(x)V1'(x) + 2b2 U2'(x)V2'(x)`,                         (5.6)

where each primed variable is a translation of one original coordinate. Conditional on `x`, the four primed variables remain independent and each has density cap one.

By (5.3), the two summands have `L^2` density norms at most `2/sqrt(|b1|)` and `2/sqrt(|b2|)`. Young/Cauchy--Schwarz convolution therefore yields

`boxed: ||p_{Q|x}||_infinity <= 4/sqrt(|b1 b2|)
       =4/sqrt(|det B|)`.                                     (5.7)

Averaging over `x` preserves the bound. Each conditional convolution is continuous, and the uniform bound (5.7) gives dominated convergence against the probability law of `x`; hence the unconditional density is continuous.

For the exact witness (5.1), `B=I_2`, so

`boxed: ||p_q||_infinity <=4`.                                 (5.8)

Thus the explicit simultaneous-double-null witness is not merely known not to be a counterexample; it is uniformly controlled for **all** admissible cap-one input densities. This is another precise third/fourth-direction smoothing mechanism: each rank-one opposite-sign product packet can be logarithmically singular, but two independent such packets lie in `L^2` and their convolution is bounded.

## 6. What is paid and what remains

**Paid in this run.**  
- A dimension-free `L^infinity` and continuity theorem for `2aSW+bV^2` when the scalar is independent of a transverse pair with bounded joint density, with explicit bound (3.1).  
- By direct use of the completed `account02/B11` pair-density theorem, the entire arbitrary exact-rank-three null-heavy chamber at leverage `c=1` has `||p||_infinity <=6e^(2/3)<11.687`, continuously.  
- Exact support-separated null-heavy frames with `c>=1/2` have the bound (4.7).  
- The previous simultaneous-double-null `B=I_2` target-class witness is uniformly controlled by `4`; more generally every monomial `2x2` double-null mixed block satisfies (5.7).

**Not paid.** The full conjecture remains open. The first B11 implication is now:

`QFORM-OVERLAPPING-NULL-HEAVY-COMPILER-v2`:

> In the canonical exact-rank-three null-heavy form `2Z1Z3+Z2^2` with physical leverage `1/2<=c<1`, control the case in which the residual first-direction coordinates genuinely overlap the transverse coordinates. Either compile disjoint original-coordinate aggregates so that one scalar is independent of a transverse pair with a universal joint-density cap, or obtain a quantitatively nondegenerate mixed packet covered by the previous two-sided-shear/regularized-determinant mechanisms. The implication must be dimension-free and must not divide by one tiny physical minor.

This residual exactly separates the new theorem from the partner's Walsh-bank compiler: exact sign banks are sufficient but not necessary; leverage one and support separation are now sufficient without banks; arbitrary overlap is the remaining local geometry.

Additional spectrum outside the selected rank-three indefinite part remains a separate nonseparable interface to the full target.

## 7. Corrections and integrity

Live corrections were refreshed before publication. This proof uses none of the refuted claims: no pointwise van-der-Corput envelope, no conditional-density-cap substitute for independence, no local rank-three cut dichotomy, no one-good-principal-triple implication, no fiberwise trace bound, and no finite-fragment localization. The distinction is crucial: Theorem 3.1 assumes **genuine independence of `S` from `(V,W)`**, obtained in Section 4 from disjoint original-coordinate provenance, not from a post-rotation conditional cap.

The opposite-sign rank-two logarithmic example (3.9) is retained explicitly. Continuity is proved for the scoped theorems above; continuity for the full conjecture remains open because the full conjecture itself remains open.
