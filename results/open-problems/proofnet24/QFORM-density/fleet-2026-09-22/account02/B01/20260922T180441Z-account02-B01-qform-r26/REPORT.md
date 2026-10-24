# QFORM account02/B01 r26 — scalar-residual conditioning sup is false; weighted replacement survives

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T180441Z-account02-B01-qform-r26`  
Assignment: Oscillatory replacement  
Status: `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Target and fresh proof boundary

The full target remains OPEN: for every dimension, every independent real input coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of magnitude at least one, prove one universal finite essential bound for the density of `Q=X^T A X`, or give a target-valid counterexample.

Fresh prepublication owner control is QFORM-only, revision `2026-09-22.11`. That correction explicitly retires two stronger Fourier/vector-conditioning routes and proposes as the new high-value implication the scalar conditioning bound

`M = sup_b ||p_{Q3 | Q'=b}||_infinity <= C`,

where `Q3` is a selected rank-three spectral core and `Q'` is the scalar residual quadratic form. This report attacks that implication immediately.

The result is decisive: the displayed scalar-conditioning supremum is FALSE even for four independent uniform inputs and an exact target-valid matrix with eigenvalues `{1,1,-1,epsilon}`. The full QFORM conjecture is NOT refuted: the same four-dimensional form is uniformly bounded by the preceding account02/B01 physical-triple theorem. The failure is the pointwise-in-`b` conditioning interface. A weighted/averaged conditional trace remains finite and is the natural replacement.

## 2. Source-pinned dependencies actually used

1. **account02/B01 r25 physical triple theorem.** At `yspennstate/math-open-problems@bf4ba08b75ab774aef671c62ba4898a371059c0d`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260922T170850Z-account02-B01-qform-r25/REPORT.md`, it proves for every invertible physical symmetric `3 x 3` block `B`, independent cap-one inputs, and arbitrary affine leakage,

   `||p||_infinity <= 216 |det B|^(-1/3)`.

2. **Named partner account03/B01 r15.** At `yspennstate/math-open-problems@76fd4f9ccae2e422498fec6d4156bfd64775c8e4`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T163129Z-r15/REPORT.md`, the arbitrary-orientation rank-two half-Riesz theorem gives the exact-rank-three Schur consequence

   `||p_Q||_infinity <= C_* (|d| c |det Lambda_3|)^(-1/4)`

   for a nonzero physical diagonal `d` and spectral-row leverage `c`, with all original-coordinate product structure retained.

3. The live correction set was refreshed before publication. In particular, uniform pointwise quadratic-phase decay, post-rotation independence, absolute-value ambiguity/Hölder aggregation, and fixed-good-small-minor reductions remain forbidden.

No fixed-potential, raw-U4, unweighted-L2, or fixed-depth-KL route is used.

## 3. A target-valid four-dimensional Hadamard family

Let `X_1,...,X_4` be iid uniform on `[0,1]`. Their densities equal one on their supports. Define orthogonal Hadamard coordinates

`Y1=( X1+X2-X3-X4)/2`,
`Y2=( X1-X2+X3-X4)/2`,
`Y3=( X1-X2-X3+X4)/2`,
`Y4=( X1+X2+X3+X4)/2`.

Let `T` be the corresponding orthogonal matrix and fix `epsilon=1/128`. Put

`A = T^T diag(1,1,-1,epsilon) T`,

so

`Q = X^T A X = Q3 + Q'`,
`Q3=Y1^2+Y2^2-Y3^2`,
`Q'=epsilon Y4^2`.

Because `T` is orthogonal, `A` has eigenvalues exactly `1,1,-1,epsilon`; hence it satisfies every hypothesis of the owner target. No post-rotation independence is asserted: all probability calculations below come directly from the original cube.

## 4. Exact scalar-conditioning blow-up

Since all `X_i` lie in `[0,1]`, `Y4` lies in `[0,2]`. Thus for every `b in (0,4 epsilon)`, conditioning on `Q'=b` is equivalent to conditioning on the unique nonnegative value

`Y4=sqrt(b/epsilon)`.

Write a value near the upper edge as

`Y4=2-delta`, with `0<delta<=1/2`,

and put deficits `u_i=1-X_i`. The condition on `Y4` is then

`u_i>=0`, `u_1+u_2+u_3+u_4=2 delta`.

The conditional law is uniform on this three-dimensional simplex. On it,

`Y1=delta-(u1+u2)`,
`Y2=delta-(u1+u3)`,
`Y3=delta-(u1+u4)`.

In particular each `Yj` lies in `[-delta,delta]`. Therefore

`Q3 | (Y4=2-delta)` is supported inside `[-delta^2,2 delta^2]`,

an interval of length at most `3 delta^2`.

The conditional law is absolutely continuous after applying the nonconstant rank-three quadratic polynomial: the conditional source has a bounded three-dimensional Lebesgue density on the simplex, and the quadratic gradient `(2Y1,2Y2,-2Y3)` vanishes only at one point; the coarea formula gives a density. Consequently every version of that density satisfies

`||p_{Q3 | Y4=2-delta}||_infinity >= 1/(3 delta^2)`.        (4.1)

There is also an exact scaling statement. Set `v_i=u_i/(2 delta)`. The law of `v` is uniform on the fixed unit three-simplex, independent of `delta`, and `(Y1,Y2,Y3)=delta L(v)` for a fixed linear map `L`. Hence

`Q3 | (Y4=2-delta)  =_law  delta^2 W`                        (4.2)

for a fixed nonconstant quadratic random variable `W`. Thus the conditional density norm scales exactly like `delta^-2`.

As `delta downarrow 0`, the corresponding scalar residual value is

`b_delta=epsilon(2-delta)^2`,

and (4.1) proves

`boxed( sup_b ||p_{Q3 | Q'=b}||_infinity = infinity ).`      (4.3)

This is a genuine falsifier of the revision-2026-09-22.11 scalar-conditioning **intermediate implication**. It is not a counterexample to QFORM.

## 5. Why the full form remains harmless

The checker verifies exactly that every physical `3 x 3` principal minor of `A` has determinant

`det A[I,I] = -(1+epsilon)/4 = -129/512`.

One transparent derivation uses Jacobi's complementary-minor identity: `det A=-epsilon`, while every diagonal entry of

`A^{-1}=T^T diag(1,1,-1,epsilon^{-1})T`

is `(1+1-1+epsilon^{-1})/4=(1+epsilon^{-1})/4`. Hence deleting any one coordinate gives determinant `-(1+epsilon)/4`.

Applying account02/B01 r25 to any physical triple therefore yields

`||p_Q||_infinity <= 216 [4/(1+epsilon)]^(1/3) <342`.        (5.1)

So the target-valid form has a bounded density even though the proposed scalar conditional supremum is infinite.

The named partner account03/B01 r15 also applies nontrivially to the rank-three core `H=T^T diag(1,1,-1,0)T`. Each physical row has leverage `c=3/4`, each physical diagonal is `d=1/4`, and `|det Lambda_3|=1`. The partner's exact-rank-three consequence gives

`||p_{Q3}||_infinity <= C_* (3/16)^(-1/4)
                       = C_* (16/3)^(1/4)`.                 (5.2)

Thus both the full form and the unconditional core are controlled; only the supremum over rare scalar residual fibers blows up.

## 6. The averaged replacement survives exactly

The same construction identifies the right correction. Let `h(y)` be the density of `Y4`. For `y=2-delta`, `0<delta<=1/2`, the Irwin-Hall edge formula for the sum of four independent uniforms gives

`h(2-delta) = (8/3) delta^3`.                                (6.1)

The conditional `(Y1,Y2,Y3)` density is uniform on its section and has supremum `h(y)^(-1)`. Applying the source-stated rank-three coarea scaling bound on this three-dimensional conditional density gives

`||p_{Q3 | Y4=y}||_infinity <= K h(y)^(-2/3)`.               (6.2)

Therefore the *weighted* conditional cap obeys near the singular edge

`h(2-delta) ||p_{Q3 | Y4=2-delta}||_infinity
 <= K h(2-delta)^(1/3)
 = (2K/3^(1/3)) delta`,                                      (6.3)

which is integrable even though the pointwise conditional cap diverges like `delta^-2`.

More globally, `Y4` has support of length two and `int h=1`, so Holder gives

`int_0^2 h(y)^(1/3) dy <= 2^(2/3)`.

Combining with (6.2),

`boxed(
 E[ ||p_{Q3 | Y4}||_infinity ] <= K 2^(2/3).
)`                                                            (6.4)

Because `Q'=epsilon Y4^2` is one-to-one on `[0,2]`, the same expectation may be written

`int ||p_{Q3 | Q'=b}||_infinity p_{Q'}(b) db <= K 2^(2/3)`. (6.5)

Finally the exact mixture identity yields the useful interface

`||p_Q||_infinity
 <= E[ ||p_{Q3 | Q'}||_infinity ]`,                           (6.6)

not the false `sup_b` obligation. Equations (6.3)-(6.6) are the distributional replacement relevant to this B01 assignment: rare fibers may be arbitrarily sharp, but their scalar-residual probability weight can compensate exactly.

This report does NOT prove that the expectation in (6.6) is universally bounded for every target matrix; that is now the first unpaid implication.

## 7. Earlier full-vector conditioning dead end, exact formula

Before the revision-2026-09-22.11 refresh, this run also independently quantified the already-retired full-vector conditioning mechanism. For one `m`-cube block and its normalized constant direction, if `ell(z)` is the section length and `R` is the range of `m` iid uniforms, then

`ell=sqrt(m)(1-R)`,
`f_R(r)=m(m-1)r^(m-2)(1-r)`.

For `0<theta<2`,

`J_{m,theta}:=E ell^(-theta)
 = m^(-theta/2) m(m-1) B(m-1,2-theta)
 ~ Gamma(2-theta) m^(theta/2)`.

For three independent blocks the conditional three-dimensional density supremum is the product of the three inverse section lengths. At the coarea exponent `theta=2/3`,

`E M^(2/3) = J_{m,2/3}^3
 ~ Gamma(4/3)^3 m`,                                          (7.1)

with asymptotic coefficient `0.712072942688730...`. Hence full-vector conditioning loses a factor linear in `m`. The committed regression confirms the exact formula numerically through `m=1024`. A first implementation using direct gamma evaluations overflowed at large `m`; it was replaced by the mathematically equivalent log-gamma evaluation, whose output ends `STATUS=PASS`. This is diagnostic evidence only; (7.1) is an analytic beta-integral computation.

## 8. First unpaid universal implication

The owner-proposed `sup_b` scalar-conditioning route is now ruled out. The first unpaid replacement is:

**QFORM-WEIGHTED-SCALAR-TRACE-v1.** Starting only from the full target hypotheses and an admissible choice of three large spectral directions, prove a dimension-free estimate of the form

`E_{Q'} ||p_{Q3 | Q'}||_infinity <= C`,

or an equivalent signed-Fejer / small-ball averaged conditional estimate, while retaining original-coordinate product provenance and all additional spectrum.

The Hadamard cube shows why the expectation is the right scale: the worst conditional fibers can diverge polynomially, but their scalar-residual mass shrinks at exactly an integrable rate. A future proof must exploit that mass/cap tradeoff instead of taking a pointwise conditional supremum.

Full QFORM remains **OPEN**. This is not a full-proof candidate and has not received two end-to-end reviews.

## 9. Exact computations and provenance

Committed checkers in this run directory:

- `check_scalar_conditioning.py` and `.out`: exact Fraction arithmetic verifies orthogonality, `det A=-1/128`, all four physical principal `3 x 3` determinants `=-129/512`, the r25 bound, partner parameters, and edge-section scaling values. Output terminates `STATUS=PASS`.
- `check_conditional_moment.py` and `.out`: evaluates the exact beta/gamma formula for the retired vector-conditioning moment via log-gamma; output terminates `STATUS=PASS`.

These finite computations check algebra/constants only and are not substitutes for the symbolic arguments above.
