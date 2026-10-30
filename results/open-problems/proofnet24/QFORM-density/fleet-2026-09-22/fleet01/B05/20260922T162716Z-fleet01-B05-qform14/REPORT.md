# fleet01/B05 — leakage disintegration functional and a product-valid mixed-slice obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control at publication:** revision `2026-09-22.7`  
**Run:** `20260922T162716Z-fleet01-B05-qform14`  
**Assignment:** Quadratic coarea bound  
**Outcome:** `ESSENTIAL_STEP_APPLIED / PRECISE_MISSING_FACTOR_IDENTIFIED / INTERMEDIATE_MECHANISM_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository retrieval occurred; no native learned-memory receiver use was observed.

## 1. Exact target and compact conditional route

The full target remains open: for every dimension, every independent real input vector whose coordinate densities are bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `Q=X^TAX`, or give a valid target counterexample. No moment, support, log-concavity, sign, connected-support, diagonal-basis, or post-rotation-independence assumption is made. Continuity is not proved in this report.

The present run attacks the hidden-leakage part of the exact-rank-three heavy-isotropic branch. In the established normal form one has

`Q = 2 B (sqrt(c) X_0 + T) Y + A_0 Y^2 + tau (Z+kappa Y)^2`,           (1.1)

where `c>1/2`, `X_0` is an original coordinate independent of the residual coordinates generating `(T,Y,Z)`, and

`B^2 |tau| = |det Lambda| >= 1`.                                       (1.2)

The residual coefficient vectors `s,y,z` obey

`||s||^2=1-c`, `||y||=||z||=1`, and `<s,y>=<s,z>=<y,z>=0`.              (1.3)

Assigned partner fleet02/B05 proved the universal aggregate two-dimensional projection bound

`||p_(Y,Z)||_infinity <= e`                                             (1.4)

for exactly this original-product provenance. In the no-leakage branch `T=0`, its completed application with sectional coarea gives `||p_Q||_infinity < 6 e^(2/3)`.

The first essential question is therefore whether one can condition on the genuine leakage projection `T`, apply the same two-dimensional coarea mechanism on each slice, and average back with a universal loss. The answer is **no** if the slice is compressed to its conditional `L^infinity` norm. This report derives the exact functional that such a proof must pay and gives a source-valid target family on which that functional diverges like `N^(2/3)`, although the partner marginal bound (1.4) remains uniform. Thus the remaining factor is an order-of-operations problem: the leakage variable must be integrated jointly with curvature before taking a transverse slice supremum.

## 2. Dependency actually applied

Assigned partner fleet02/B05, canonical source

`yspennstate/math-open-problems@e74a5d8fabe1c914be1ca2d3689a2cd65ba58f5a`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T155206Z-b05-qform-779c4c9b/REPORT.md`,

proved `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1`: if independent cap-one inputs and coefficient rows `a_j in R^2` satisfy `sum a_j a_j^T=I_2`, then their two-dimensional linear projection has joint density at most `e`.

A second completed theorem used as the sectional coarea engine is fleet03/B05 `QFORM-PAIR-SECTIONAL-COAREA-v1`, canonical source

`yspennstate/math-open-problems@332f29e335274f2b3f81ccf92d62443b928c66cd`.

It states that if `U` is independent of a pair `(V,Z)`, `||p_U||_infinity<=M_U`, `||p_(V,Z)||_infinity<=M_2`, and

`W=2aUV+H(V)+b(Z+theta(V))^2`,

then

`||p_W||_infinity <= 3*2^(2/3) M_U^(2/3) M_2^(2/3)
                       |a|^(-2/3)|b|^(-1/3)`.                          (2.1)

No conditional-density surrogate is silently substituted for independence below: after conditioning on `T`, the genuinely independent variable remains the original coordinate `X_0`.

## 3. Exact conditional-coarea reduction to one mixed-slice functional

Assume first `s!=0`. Then `(T,Y,Z)` is a nondegenerate three-dimensional linear projection of the residual product source and has a joint density `g(t,y,z)`. Put

`p_T(t)=int_R2 g(t,y,z) dy dz`,

`m(t)=ess sup_(y,z) g(t,y,z)`.                                          (3.1)

For `p_T(t)>0`, the conditional density of `(Y,Z)` given `T=t` is

`g_t(y,z)=g(t,y,z)/p_T(t)`,

and therefore

`||g_t||_infinity = m(t)/p_T(t)`.                                      (3.2)

Condition on `T=t`. Since `X_0` is independent of the entire residual vector, `U=sqrt(c)X_0` remains independent of `(Y,Z)|{T=t}` and has density cap

`M_U=c^(-1/2)`.                                                         (3.3)

Equation (1.1) becomes

`Q = 2B UY + H_t(Y) + tau(Z+kappa Y)^2`,                               (3.4)

with `H_t(Y)=2B tY+A_0Y^2`. Applying (2.1) to (3.4) gives, for almost every `t`,

`||p_(Q|T=t)||_infinity
 <= C_0 c^(-1/3) |B|^(-2/3)|tau|^(-1/3)
       [m(t)/p_T(t)]^(2/3)`,                                            (3.5)

where `C_0=3*2^(2/3)`.

Averaging the conditional laws yields the exact sufficient bound

`||p_Q||_infinity
 <= C_0 c^(-1/3)|det Lambda|^(-1/3) J(g)`,                              (3.6)

where

`J(g) := int_R p_T(t)^(1/3) m(t)^(2/3) dt`.                             (3.7)

Because `c>1/2` and `|det Lambda|>=1`,

`||p_Q||_infinity < 6 J(g)`.                                           (3.8)

This is `QFORM-LEAKAGE-DISINTEGRATION-FUNCTIONAL-v1`. It is a genuine original-coordinate coarea reduction: the only new quantity is the mixed slice functional `J(g)`.

A crude Hölder step would give

`J(g) <= (int p_T)^(1/3) (int m(t)dt)^(2/3)
      = (int m(t)dt)^(2/3)`.                                           (3.9)

Thus a dimension-free bound on the forward mixed norm `int ||g(t,.,.)||_infinity dt` would finish this exact-rank-three branch. The assigned partner theorem, however, controls the **opposite** order:

`sup_(y,z) int_R g(t,y,z)dt
 = ||p_(Y,Z)||_infinity
 <= e`.                                                                (3.10)

The next section shows that exchanging these two operations cannot be done with a universal constant, even inside a genuine target frame.

## 4. Product-valid target family with unbounded mixed-slice cost

### Proposition `QFORM-LEAKAGE-SLICE-MIXED-NORM-FALSE-v1`

There are exact-rank-three target matrices with nonzero eigenvalues `{1,1,-1}` and independent cap-one input laws for which the partner inequality (3.10) holds uniformly but the conditional-coarea functional `J(g)` in (3.7) grows at least as a constant times `N^(2/3)`.

### Construction of the target frame

Fix

`c=3/4`,

`Lambda = [[0,1,0],[1,0,0],[0,0,1]]`.                                  (4.1)

The eigenvalues of `Lambda` are `1,-1,1`. Let

`o_1=(1,1,1)/sqrt(3)`

and complete it to an orthonormal basis `o_1,o_2,o_3` of `R^3`. Use one heavy physical row

`r_0=(sqrt(3)/2,0,0)`

and three residual physical rows

`r_j=( (1/2)(o_1)_j, (o_2)_j, (o_3)_j )`, `j=1,2,3`.                  (4.2)

Then

`sum_(j=0)^3 r_j r_j^T=I_3`.                                           (4.3)

Consequently, if `R` is the `4x3` matrix with rows `r_j` and `A=R Lambda R^T`, the three nonzero eigenvalues of `A` are exactly `1,-1,1`. This is a valid target matrix. The heavy row is isotropic because its physical diagonal is `r_0^T Lambda r_0=0`.

For the residual coordinates define

`T=(1/2)o_1.X`, `Y=o_2.X`, `Z=o_3.X`.                                  (4.4)

Thus the normalized triple

`(T_0,Y,Z):=(2T,Y,Z)`                                                   (4.5)

is an orthogonal transform of `(X_1,X_2,X_3)`.

### Fragmented cap-one product laws

For an integer `N>=2`, let

`E_1 = union_(k=0)^(N-1) [4k,4k+1/N]`,

`E_2=E_3=[0,1]`,                                                        (4.6)

and take independent residual inputs with densities `1_(E_j)`. Each density is bounded by one and integrates to one. The heavy input `X_0` may be any independent cap-one probability density, for example `1_[0,1]`.

Let `g_0` be the joint density of `(T_0,Y,Z)`. Since (4.5) is orthogonal,

`g_0(t,y,z)` is exactly the indicator of the orthogonal image of
`E_1 x E_2 x E_3`; in particular it only takes the values zero and one. Therefore

`m_0(t):=ess sup_(y,z) g_0(t,y,z)=1`                                   (4.7)

for every `t` in the projection of the product set onto the `T_0` axis.

That projection is

`(E_1+[0,2])/sqrt(3)`,                                                   (4.8)

which is a union of `N` disjoint intervals, each of length

`(2+1/N)/sqrt(3)`.

Hence already

`int m_0(t)dt=(2N+1)/sqrt(3) -> infinity`.                              (4.9)

This proves there is no universal exchange from the partner-controlled reverse mixed norm (3.10) to the forward norm in (3.9).

### The exact coarea functional itself diverges

The obstruction is stronger than (4.9). Let `S=X_1+X_2+X_3`, so `T_0=S/sqrt(3)`. The density of `X_2+X_3` is the triangular density

`h(u)=u` on `[0,1]`, `h(u)=2-u` on `[1,2]`,

and `h(u)>=1/2` on `[1/2,3/2]`. For each fragment

`I_k=[4k,4k+1/N]`,

if

`S in [4k+1/N+1/2, 4k+3/2]`,                                          (4.10)

then `S-x in [1/2,3/2]` for every `x in I_k`. Therefore

`p_S(S) >= int_(I_k) (1/2) dx = 1/(2N)`.                               (4.11)

The intervals in (4.10) are disjoint and each has length `1-1/N`. After the scaling `T_0=S/sqrt(3)`,

`p_(T_0)(t) >= sqrt(3)/(2N)`                                            (4.12)

on `N` disjoint intervals, each of length `(1-1/N)/sqrt(3)`. Together with `m_0=1` there,

`J(g_0)
 >= N*(1-1/N)/sqrt(3) * (sqrt(3)/(2N))^(1/3)
 = (N-1)/(6N)^(1/3).`                                                   (4.13)

Thus

`J(g_0) -> infinity` like `6^(-1/3) N^(2/3)`.                          (4.14)

The functional is invariant under nonzero rescaling of the leakage coordinate: if `T=aT_0`, then both `p_T` and `m_T` acquire the factor `|a|^(-1)` while `dt` acquires `|a|`, so `J` is unchanged. Hence (4.13) applies to the actual leakage `T=T_0/2` in (4.4).

Finally, the assigned partner result still gives, for every `N`,

`sup_(y,z) int g(t,y,z)dt = ||p_(Y,Z)||_infinity <= e`,                 (4.15)

because `y,z` are orthonormal coefficient vectors of the original independent product source. Equations (4.13) and (4.15) together isolate the failure: **the reverse mixed norm is uniformly bounded while the exact slice functional generated by conditioning on leakage is unbounded.**

This is a counterexample to the proposed proof mechanism, not to QFORM itself. The matrix and input laws satisfy every target hypothesis, but no claim is made here that the actual density of their quadratic output is unbounded.

## 5. A positive leakage identity that survives the counterexample

Although conditioning on `T` and taking slice suprema loses a factor, the independent heavy coordinate does erase leakage at the level of the full spectral-vector density. Put

`W=sqrt(c)X_0+T`.                                                       (5.1)

If `g` is the joint density of `(T,Y,Z)`, then

`p_(W,Y,Z)(w,y,z)=int f_(sqrt(c)X_0)(w-t) g(t,y,z)dt`.                  (5.2)

Since `||f_(sqrt(c)X_0)||_infinity<=c^(-1/2)` and the assigned partner gives `p_(Y,Z)<=e`,

`boxed( ||p_(W,Y,Z)||_infinity <= e c^(-1/2) < sqrt(2)e ).`             (5.3)

Equivalently, wherever `p_(Y,Z)>0`,

`||p_(W|Y,Z)||_infinity <= c^(-1/2)`.                                  (5.4)

This is `QFORM-HEAVY-CONVOLUTION-LEAKAGE-CAP-v1`. It is a genuine application of the designated partner theorem to an actual inequality. It does **not** finish the quadratic pushforward: the live corrections already show that a bounded three-dimensional projection density or a bounded conditional scalar density, by itself, does not control an indefinite curved trace. What (5.3) does show is that the remaining difficulty is no longer concentration of the spectral vector; it is the interaction between its product-fiber provenance and the indefinite quadratic level geometry.

## 6. Precise remaining implication

The failed implication is now explicit:

`QFORM-HIDDEN-LEAKAGE-SLICE-SUP-CLOSURE` is false.

A full coarea proof must instead establish a translation-uniform **curved three-projection trace** estimate that keeps the leakage variable inside the curvature integral before any `L^infinity` slice operation. In the heavy-isotropic coordinates this means controlling the pushforward of the genuine product-projection law of `(W,Y,Z)` under

`(w,y,z) -> 2Bwy + A_0 y^2 + tau(z+kappa y)^2`                          (6.1)

using more than the marginal cap `||p_(Y,Z)||_infinity<=e`, more than the full joint cap (5.3), and more than generic X-ray/fiber suprema. The needed extra resource is the weighted affine-fiber/product representation of the spectral density itself, or an equivalent integrated Fourier estimate that preserves the original-coordinate product law.

A concrete successor is `QFORM-CURVED-PRODUCT-FIBER-TRACE-v1`: prove a dimension-free bound for (6.1) directly from the affine-fiber representation of a rank-three orthogonal projection of a cap-one product measure, without disintegrating first in `T`. Any proof that first replaces each `T`-slice by its conditional pair `L^infinity` norm is ruled out by Section 4.

## 7. Status and provenance

- Full QFORM: **OPEN / NOT PROVED**.
- Continuous density for the full target: **NOT PROVED**.
- New positive results: the exact reduction (3.6)-(3.7) and the convolution leakage cap (5.3).
- New negative result: the source-valid target family (4.1)-(4.15) refutes a universal conditional-slice-sup closure and identifies the precise missing mixed factor.
- Assigned partner actually applied: fleet02/B05 `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1`, canonical commit `e74a5d8fabe1c914be1ca2d3689a2cd65ba58f5a`.
- Sectional engine: fleet03/B05 `QFORM-PAIR-SECTIONAL-COAREA-v1`, canonical commit `332f29e335274f2b3f81ccf92d62443b928c66cd`.
- Fresh owner control immediately before publication: `yspennstate/math-research-brain@5cd9bf4e0e52d0177b7e132df4c09ca57b2a0196`, revision `2026-09-22.7`. The target remains unchanged and exclusive.

Changed-file privacy review: this report contains only mathematical statements, public-style theorem references already present in the authorized private research repositories, and nonsecret source commit/path identifiers. No credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive material, benchmark gold, or public-release action are included.
