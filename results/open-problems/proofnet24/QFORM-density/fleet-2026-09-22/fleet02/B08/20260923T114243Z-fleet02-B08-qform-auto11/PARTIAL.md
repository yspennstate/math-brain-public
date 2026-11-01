SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-23T11:42:43.340439Z.
attacking: the diffuse k=1 hybrid — aggregate one actual delocalized child square with physical E2/cross currency before scalar-pivot payment, and test the sharp obstruction on the Hadamard family.

# Early substantive checkpoint: the k=1 gate already has universal L^p currency

Programme `QFORM-DENSITY-3EIG-20260922`. Full target OPEN. This checkpoint keeps original-coordinate product laws, arbitrary same-bank curvature, arbitrary complementary spectrum, arbitrary fragmented/unbounded supports, and no post-rotation independence or moment assumption.

## First unpaid implication

At the current actual spectral gate, the k=1 child/cross branch has one ACTUAL child eigenvalue

`|lambda| >= c0 L`,  `c0=(1/2)sqrt(3/5)`,

and its literal physical cross block `B=A[I,J]` has

`s_2(B) > beta0 L`,  `beta0=(3/16)sqrt(3/5)`.

The first genuinely unpaid implication is not existence of analytic currency: it is a provenance-preserving compiler that combines this collective child square with the two-cross currency BEFORE selecting a scalar physical pivot.

## Partner theorem applied to the actual gate

Use fleet03/B08 `QFORM-E2-LP-DENSITY-v1`, source

`yspennstate/math-open-problems@2cb64b71f8aafa0892547dffebcf6af647ea7c64:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T102108Z-fleet03-B08-qform-diffuse-r32/REPORT.md`.

For any `2<=p<5/2`, put `q=p/(p-1)`, so `5/3<q<=2`. The theorem gives for a literal physical cross block `M`

`||p||_p <= C_p E_2(M)^(-1/(4q))`,

with all ambient terms retained. Since

`E_2(B)=e_2(B^T B) >= s_1(B)^2 s_2(B)^2 > (beta0 L)^4`,

we obtain on the entire k=1 branch

`||p_Q||_p < C_p (beta0 L)^(-1/q)`.

If `w` is the actual unit child eigenvector and `V=<w,X_I>`, write the exact peel

`Q=lambda V^2 + R`.

Subtracting `lambda ww^T` changes only the I-I self block, so the same literal cross block `B` remains in `R`. Therefore the SAME partner theorem also gives

`||p_R||_p < C_p (beta0 L)^(-1/q)`.

In particular, at `p=9/4`, `q=9/5`, `C_p<7`,

`boxed:  ||p_Q||_(9/4), ||p_R||_(9/4) < 20.447 L^(-5/9).`

Hence every interval `J` obeys

`boxed:  P(Q in J) < 20.447 (|J|/L)^(5/9).`

This is a full-ambient, target-source-valid estimate for every k=1 actual-gate form. It already improves the previous generic L2/square-root currency.

## Scale-perfect conditional closure and the precise missing input

The partner's dependent-square `L^p -> L^infinity` theorem extends verbatim if the conditional density of `V` given `R=r` is bounded by `K` instead of one: multiply the square kernel by `K`. Thus

`||p_Q||_infinity <= 2(1-q/2)^(-1/2) K |lambda|^(-1/2) ||p_R||_p^(q/2)`.

Insert the actual gate and the partner bound:

`||p_Q||_infinity
 <= [2(1-q/2)^(-1/2) C_p^(q/2) (c0 beta0)^(-1/2)] K/L.`

In the partner theorem's worst diffuse-star case the bracket is minimized at

`q=sqrt(10/3)`, `p=q/(q-1)=2.211032225...`,

because minimizing `q/[(3q-5)(1-q/2)]` gives `q^2=10/3`. The other two partner constants are smaller there. This yields

`boxed: ||p_Q||_infinity < 150.186 K/L.`

Thus a universal conditional-height bound for the COLLECTIVE child projection would close k=1 immediately with the correct `L^{-1}` scaling. But such a bound is not available from delocalization alone, and the live correction against worst conditional projection-density moments forbids assuming it.

## Why one must retain E2 provenance rather than only its L^p consequence

Even for cap-one independent sources, a generic `L^p` residual plus one actual square is not enough when dependence is arbitrary. Let `U_1,U_2` be independent Uniform[0,1], set

`V=(U_1+U_2)/sqrt(2)`,  `c=1/sqrt(2)`,  `R=-2cV+c^2=1/2-(U_1+U_2)`.

Then `p_R` is triangular with `||p_R||_infinity=1`, hence `||p_R||_p<=1` for every `p>=1`; the marginal density of `V` is also bounded (`||p_V||_infinity=sqrt(2)`). Nevertheless

`V^2+R=(V-c)^2=(U_1+U_2-1)^2/2`

has density

`p(y)=sqrt(2)y^(-1/2)-2`,  `0<y<1/2`,

and is unbounded at zero. The peeled residual is affine in the child coordinate (there is no residual `V^2` term), exactly matching the algebraic feature of an eigen-square peel. Therefore a proof cannot throw away the physical E2 mechanism after using it merely to certify `p_R in L^p`; it must combine the E2 provenance jointly with the collective square.

This is a mechanism obstruction, not a QFORM counterexample: the example has only one nonzero quadratic eigenvalue.

## Required fixed-source application

The fixed source `e5f71d79eff325201dd0274053d20268ce65b837` gives D5: for a physical cross block, `||p_Q||_infinity <=5sqrt(2e) e_5(B^TB)^(-1/10)` with no marginal hypothesis. Therefore on the same k=1 gate, if additionally `s_5(B)>=eta L`, then

`e_5(B^TB) >= (beta0 L)^4 (eta L)^6`

and

`boxed: ||p_Q||_infinity <= 5sqrt(2e) beta0^(-2/5) eta^(-3/5) / L.`

At `eta=1/64` this is `<306/L`. Hence the still-unpaid k=1 state can be taken simultaneously to satisfy

`s_2(B)>beta0 L`, `s_5(B)<L/64`,

so it lies within `L/64` in operator norm of rank at most four, while BOTH `Q` and the exact child-peeled residual `R` have the universal `L^p` estimates above. Small operator-norm cross tail is only a structural fact; it is not deleted as a random quadratic perturbation.

Next: test whether the rank-four-tube + E2 provenance admits a mixed Fresnel/decoupling compiler, and use the existing Hadamard k=1 family as the exact-range calibration. No conditional-height assumption will be inserted silently.
