# fleet01/B11 — two-sided shear absorption for the rank-two mixed endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control revision:** `2026-09-22.5`  
**Run:** `QFORM-B11-20260922T144348Z-r11`  
**Assignment:** indefinite signatures  
**Outcome:** `ESSENTIAL_STEP_APPLIED / TARGET_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Exact target and conditional end-to-end architecture

The full target is unchanged: for every dimension, every independent real input vector with one-dimensional probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal bound for the density of `Q=X^TAX`, or give a genuine target counterexample. Continuity is a separate stronger requested conclusion.

The present run attacks the local indefinite endpoint that remained after the completed mixed-Hessian and heavy-row arguments. The compact conditional architecture is:

1. completed diffuse/full-range branches pay geometrically diffuse matrices;
2. the assigned partner `fleet02/B11` pays an exact-rank-three heavy coordinate when its spectral Rayleigh quotient has the minority sign and stays away from the null cone;
3. the completed `fleet01/B19` one-sided mixed theorem pays a physical `1 self + 2 cross` packet when the scalar coordinate couples to only one side of the rank-two mixed block;
4. the new theorem below pays **two-sided scalar coupling** whenever one of two explicit shear curvatures is nonzero, without pretending that the shear preserves coordinate independence.

Thus the first local analytic debt is no longer generic two-sided coupling. The residual is a simultaneous double-null shear geometry together with the global problem of extracting/aggregating a quantitatively useful packet without dividing by one tiny physical minor.

No pointwise law-uniform Fresnel decay, post-rotation independence, bounded-diameter localization, conditional-cap-as-independence replacement, or single-good-minor dichotomy is used.

## 2. Immutable peer inputs actually used

### 2.1 Assigned partner `fleet02/B11`

Canonical source: `yspennstate/math-open-problems@245a4e2a4414294fbb20b9dd4f292f6b001e5aa2`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260922T135203Z-b11-qform-6080e0b3/REPORT.md`.

For exact rank three, if a physical spectral row has leverage `c>=1/2`, is rotated only inside the three-dimensional spectral representation to `sqrt(c)e_1`, and its Rayleigh coefficient `a` has the minority sign, the partner proves

`||p_Q||_infinity <= 2 sqrt(2*pi*e) delta^(-1/4)` whenever `|a|>=delta`.

Applying the result at `delta=1/4` gives the actual branch inequality

`||p_Q||_infinity <= 4 sqrt(pi*e) < 11.690`.                 (2.1)

The same report proves the one-dimensional projection cap `sqrt(e)` and the two-dimensional isotropic projection cap `e`; both keep the original product-coordinate provenance.

### 2.2 Mixed-Hessian Plancherel endpoint

The exact mixed-Hessian estimate is from `yspennstate/math-open-problems@446d0a33ef626b11ed5da529f2cec821732e97e9`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260922T130227Z-fleet03-B09-QFORM-r11/REPORT.md`.

For arbitrary square-integrable amplitudes `F,G` on `R^2` and invertible `2x2` physical cross block `B`, the same Plancherel calculation gives

`|int F(u) exp(i2t u^T Bv) G(v) du dv|
 <= pi |t|^(-1) |det B|^(-1/2) ||F||_2 ||G||_2`.           (2.2)

At mixed dimension two this is the exact logarithmic Fourier endpoint.

### 2.3 One-sided scalar-curvature repair

The completed `fleet01/B19` source is `yspennstate/math-open-problems@1620f286923bde59e02467ff11ed662d2a18514f`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B19/20260922T141737Z-b19-qform-r11/REPORT.md`.

It proves the one-sided theorem with constant

`C_* = 5 * 3^(3/5) * 2^(-2/5) < 7.326`,                    (2.3)

using a shifted-square `L^4(dt)` gain. The new argument below keeps the same endpoint constant but removes the one-sided coupling assumption by a product-aware shear calculation.

## 3. A subprobability shifted-square lemma

### Lemma 3.1 — mass-sensitive shifted-square transform

Let `h:R->[0,1]` be integrable, with mass `m=integral h(x)dx<infinity`. For `a!=0`, `b in R`, define

`K_b(t)= integral h(x) exp(i t(a x^2+2b x)) dx`.

Then

`||K_b||_4 <= 2 sqrt(2) (2*pi)^(1/4) m^(1/2)|a|^(-1/4)`.      (3.1)

The estimate is uniform in `b`, and `m` need not be at most one.

### Proof

Complete the square and translate `h`. It suffices first to take `a=1,b=0`. Let `g` be the pushforward mass density under `x->x^2`. For `y>0`,

`g(y)=[h(sqrt(y))+h(-sqrt(y))]/(2sqrt(y)) <= y^(-1/2)`,

and `integral g=m`. If `m=0` there is nothing to prove. Split at `y=m^2`:

`integral_0^{m^2} g^(4/3) <= integral_0^{m^2} y^(-2/3)dy=3m^(2/3)`.

For `y>=m^2`, `g(y)<=1/m`, hence

`integral_{m^2}^infinity g^(4/3) <= m^(-1/3) integral g <=m^(2/3)`.

Thus `||g||_(4/3)<=2sqrt(2)m^(1/2)`. Scaling by `a` gives `|a|^(-1/4)`, and Hausdorff--Young for `hat g(t)=integral exp(ity)g(y)dy` gives the extra factor `(2*pi)^(1/4)`. QED.

## 4. Main theorem: two-sided coupling can be sheared onto one side

Let `x,u_1,u_2,v_1,v_2` be five distinct original coordinates, all independent, each with density at most one. Write `u=(u_1,u_2)` and `v=(v_1,v_2)`. After conditioning all other original coordinates, suppose

`q(x,u,v)=a x^2+2x(beta+r^T u+s^T v)
          +u^T C u+2 gamma^T u+2u^T Bv
          +v^T Dv+2 delta^T v+c_0`,                            (4.1)

where `C,D` are symmetric `2x2` matrices and `B` is invertible.

Define

`kappa=B^(-T)s`,
`a_L=a-2r^T kappa+kappa^T C kappa`,                            (4.2)

and

`lambda=B^(-1)r`,
`a_R=a-2s^T lambda+lambda^T D lambda`.                         (4.3)

### Theorem 4.1 — `QFORM-TWOSIDED-SHEAR-MIXED-v1`

If `a_L!=0`, then the conditional and unconditional laws of `Q` have bounded continuous densities vanishing at infinity and

`||p_Q||_infinity <= C_* |a_L|^(-1/5)|det B|^(-2/5)`.         (4.4)

If instead `a_R!=0`, the same conclusion holds with `a_R` in place of `a_L`. Thus generic two-sided scalar coupling costs no new exponent and no new constant relative to the one-sided endpoint.

### Proof: left shear

Make the volume-preserving change `u'=u+kappa x`, i.e. `u=u'-kappa x`. This is only a change of integration variables: it does **not** preserve independence between `x` and `u'`, and no such claim is made.

Because `kappa^T B=s^T`, the term `2u^TBv` becomes `2u'^TBv-2x s^Tv`, exactly cancelling the original `2x s^Tv`. Expansion gives

`q=a_Lx^2+2x(beta_L+r_L^Tu')+F_L(u')+2u'^TBv+G(v)+c_0`,       (4.5)

where `r_L=r-Ckappa`, `beta_L=beta-gamma^Tkappa`.

The transformed left density is

`rho(x,u')=f_x(x) f_{u_1}(u'_1-kappa_1x) f_{u_2}(u'_2-kappa_2x)`.   (4.6)

Although nonproduct in `(x,u')`, it satisfies `0<=rho<=1`, `integral rho=1`, and if

`m(u')=integral rho(x,u')dx`,

then `integral m(u')du'=1`. The right variable `v` remains independent of the entire transformed left block.

For each `u'` define

`K_t(u')=integral rho(x,u') exp(it[a_Lx^2+2x(beta_L+r_L^Tu')])dx`,

`H(t)^2=integral |K_t(u')|^2du'`.                              (4.7)

Lemma 3.1 on each slice gives, with `C_0=2sqrt(2)(2*pi)^(1/4)`,

`||K_.(u')||_4^2 <= C_0^2 |a_L|^(-1/2)m(u')`.

Minkowski on `H^2` therefore yields

`||H||_4^2 <= integral ||K_.(u')||_4^2du'
            <=C_0^2|a_L|^(-1/2)`,

so

`||H||_4 <= C_0|a_L|^(-1/4)`.                                 (4.8)

This is the product-aware shear step: the shear destroys independence internally, but the mass-sensitive square estimate integrates the slice masses back to one.

Apply the mixed-Hessian estimate (2.2) to the `u'` and `v` amplitudes. The right amplitude has `L^2` norm at most one, hence

`|phi_Q(t)| <= pi |t|^(-1)|det B|^(-1/2)H(t)`, `t!=0`.        (4.9)

Together with `|phi_Q(t)|<=1`, for any `T>0`, Holder gives

`integral |phi_Q(t)|dt
 <=2T+D T^(-1/4)`,                                             (4.10)

where

`D=pi|det B|^(-1/2) C_0 |a_L|^(-1/4)6^(3/4)`.

Optimizing at `T=(D/8)^(4/5)` yields `10(D/8)^(4/5)`. Fourier inversion gives exactly

`||p_Q||_infinity
 <=5*3^(3/5)*2^(-2/5)|a_L|^(-1/5)|det B|^(-2/5)`.            (4.11)

The characteristic function is in `L^1`, so the density is continuous and tends to zero at infinity. The estimate is uniform in all conditioned outside coordinates, so averaging preserves it. QED.

### Right shear

Set `v'=v+lambda x`. Since `B lambda=r`, the mixed term cancels the original `2x r^Tu`. The identical argument with the two sides reversed yields (4.4) with `a_R`.

## 5. Exact double-null obstruction to the strongest shortcut

It is false that one of the two shear curvatures must always be nonzero. Take

`C=D=0`, `B=I_2`, `r=s=e_1`, `a=2`,

with zero affine terms. Then `a_L=a_R=0`. The coefficient matrix on `(x,u_1,u_2,v_1,v_2)` is

`M=[[2,1,0,1,0],
    [1,0,0,1,0],
    [0,0,0,0,1],
    [1,1,0,0,0],
    [0,0,1,0,0]]`.

Its characteristic polynomial is

`lambda(lambda-3)(lambda-1)(lambda+1)^2`,                      (5.1)

so the spectrum is `{3,1,-1,-1,0}`: a literal target-class matrix. The form factors as

`q=2x^2+2x(u_1+v_1)+2u_1v_1+2u_2v_2
  =2(u_1+x)(v_1+x)+2u_2v_2`.                                  (5.2)

This is not a QFORM counterexample. Conditioning on `x` makes `u_1+x` and `v_1+x` independent translations and leaves a zero-self rank-two mixed packet. It is a rigorous counterexample only to the structural shortcut `a!=0 => a_L!=0 or a_R!=0`.

## 6. Partner-based finite-p diagnostic for the canonical near-null chart

The assigned partner's first unpaid chart is

`Q=2Z_1Z_3+Z_2^2`,                                             (6.1)

where an original coordinate `X_0` contributes leverage `c>=1/2` only to `Z_1`. Write `Z_1=sqrt(c)X_0+L(Y)`. Conditional on the remaining original coordinates `Y`, `Z_1` is a translate of `sqrt(c)X_0`, so its density cap is `c^(-1/2)`. The partner's one-dimensional projection theorem gives

`||p_{Z_3}||_infinity<=sqrt(e)`.                               (6.2)

For finite `p>1`, put `alpha=1-1/p`. Conditional on `Y` with `Z_3!=0`, the density of `Q` has `L^1` norm one and `L^infinity` norm at most

`M(Y)=(2sqrt(c)|Z_3|)^(-1)`.

Interpolation and Minkowski give

`||p_Q||_p <=(2sqrt(c))^(-alpha) E|Z_3|^(-alpha)`.             (6.3)

Using (6.2) and splitting at `|z|=1`,

`E|Z_3|^(-alpha) <=1+2sqrt(e)/(1-alpha)=1+2sqrt(e)p`.          (6.4)

Therefore

`||p_Q||_p <=(2sqrt(c))^(-(1-1/p))(1+2sqrt(e)p)
            <=1+2sqrt(e)p`.                                    (6.5)

This does not prove `L^infinity`; it shows that the canonical null chart is an endpoint problem, consistent with logarithmic rank-two singularity.

## 7. How the third direction removes the logarithmic singularity

The mandatory opposite-sign rank-two control remains: products/saddles such as `XY` or `X^2-Y^2` can have logarithmically unbounded density. The valid third-direction mechanism is not law-uniform pointwise Fresnel decay. In a physical triple, the completed indefinite-binary theorem controls a one-sided half-order potential and a third square consumes it through an Abel kernel. In the mixed chart here, two mixed directions give the borderline `|t|^-1` factor, while a nonzero shear curvature supplies a time-averaged `L^4` resource that makes the Fourier tail integrable. The third direction need not be an independent additive square.

## 8. First essential missing implication

Paid here: a physical rank-two mixed packet plus a scalar coordinate coupled to **both** sides, with arbitrary same-side curvature and arbitrary outside affine terms, whenever `a_L!=0` or `a_R!=0`. This directly removes the generic two-sided scalar-coupling item from the `fleet01/B19` residual.

The first unpaid interface is

`QFORM-DOUBLE-NULL-SHEAR-OR-AGGREGATION-v1`:

Starting from the heavy near-null / balanced mixed geometry, prove with universal quantitative constants either

1. an aggregated rank-two packet `B` with paid `|det B|` and at least one quantitatively nonzero `|a_L|,|a_R|`; or
2. in the simultaneous double-null chamber `a_L=a_R=0`, an endpoint `L^infinity` estimate from the remaining product-coordinate structure, extra spectrum, or a rectangular multi-pivot packet, without dividing by a vanishing individual minor.

The exact target-class matrix (5.1) proves that branch (2) is real. The partner estimate (6.5) shows its canonical rank-three manifestation already has every finite `L^p` norm uniformly controlled; the unpaid step is the endpoint upgrade and dimension-free aggregation with arbitrary extra spectrum.

## 9. Scope, continuity, and corrections

Theorem 4.1 is an arbitrary-law original-coordinate theorem, stable under arbitrary outside conditioning. It proves a **continuous** density for its branch because it obtains an actual `L^1` characteristic function. The finite-`p` chart proves only finite-`p` density control. The full conjecture remains open.

Immediately before publication, fresh control remained owner revision `2026-09-22.5`. The live corrections consumed included `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`, and `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`. None of their refuted implications is used.
