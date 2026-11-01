SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-23T13:29:11Z.
attacking: the true near-null shared-bank endpoint by testing the opposite-sign scalar Schur route; prove whether a positive-definite two-dimensional projected remainder plus genuine product provenance can remove the pivot singularity.

# Checkpoint — definite-Schur logarithmic barrier

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `NEW ROUTE OBSTRUCTION / FULL QFORM OPEN`.

## First unpaid implication

The exact-rank-three near-coloop compiler still needs a mechanism that remains uniform as a physical hub Rayleigh quotient crosses zero while retaining the translating original-coordinate hub factor. The previous B16 logarithmic obstruction covered the sign in which scalar Schur completion leaves an indefinite rank-two remainder. The calculation below shows that choosing the *opposite* sign, so the Schur remainder is positive definite, does not repair scalar square peeling: the exact translation-uniform square envelope still loses a logarithm, even for a genuine dependent two-dimensional product projection.

## Target-valid family

Fix even `m>=4`, balanced signs `epsilon_j in {+1,-1}`, and let

`Y=m^(-1/2) sum_j X_j`,
`Z=m^(-1/2) sum_j epsilon_j X_j`,

for independent original coordinates with densities bounded by one. For `0<eta<=1`, put

`c_eta=sqrt(1+eta)`,
`Q_eta=-eta X_0^2+2 c_eta X_0Y+Z^2`.

On the orthonormal physical-space span `(X_0,Y,Z)`, the coefficient matrix is

`M_eta=[[-eta,c_eta,0],[c_eta,0,0],[0,0,1]]`.

Its characteristic polynomial is `(lambda-1)^2(lambda+1+eta)`, so the nonzero spectrum is exactly

`{1,1,-(1+eta)}`.

Thus this is a strict three-large-eigenvalue target family.

The already completed mixed-Fresnel argument from the required Claude source applies before any Schur completion. Its augmented leaf rows are

`w_j=(c_eta/sqrt(m), epsilon_j/sqrt(m))`,

with Gram `diag(1+eta,1)` and normalized leverage `2/m<=1/2`. Therefore, for arbitrary cap-one source laws,

`||p_(Q_eta)||_infinity <= 3*2^(4/3)*(1+eta)^(-1/3) <= 7.5595263`.

No independence of `(Y,Z)` is used in that estimate.

## Opposite-sign scalar completion

Completing the *negative* hub pivot gives

`Q_eta=-eta (X_0-c_eta Y/eta)^2+R_eta`,

where the rank-two Schur remainder is now positive definite:

`R_eta=((1+eta)/eta)Y^2+Z^2`.

The cap-only conditional square envelope at level zero is

`K_eta(0)=eta^(-1/2) E[R_eta^(-1/2)]`.

This is the exact object produced when one retains only the height bound `f_0<=1` for the translated hub density.

To see the loss on a genuine dependent product projection, take `m=4`, signs `(+,+,-,-)`, and iid `X_1,...,X_4 ~ Unif[-1/2,1/2]`. Put

`A_+=(X_1+X_2)/2`, `A_-=(X_3+X_4)/2`.

Then `Y=A_++A_-`, `Z=A_+-A_-`. If `p(a)=2(1-2|a|)` on `|a|<=1/2` is the density of each `A_+,A_-`, the exact joint density is

`rho(y,z)=(1/2) p((y+z)/2)p((y-z)/2)`.

This pair is dependent: its support is `{|y+z|<=1, |y-z|<=1}`, not the product of its marginal supports. Nevertheless it is a genuine orthogonal projection of the original product law, and the standard product-projection theorem gives `||rho||_infinity<=2`.

On the rectangle `|y|,|z|<=1/8`, one has `rho(y,z)>=9/8`. Let `L=(1+eta)/eta`. Then

`K_eta(0)
 >= eta^(-1/2)*(9/8) int_{|y|,|z|<=1/8}(L y^2+z^2)^(-1/2) dy dz`.

With `u=sqrt(L)y`, and integrating over `1/8<=|u|<=sqrt(L)/8`, `|z|<=1/8`,

`K_eta(0)
 >= [9 sqrt(2)/(64 sqrt(1+eta))] log L`.

Hence

`K_eta(0) -> infinity` as `eta downarrow0`, logarithmically.

So the scalar-Schur / translation-uniform square-peel route fails on *both* sides of the null pivot: an indefinite rank-two remainder is not the source of the earlier logarithm. Even positive-definite rank-two curvature and a valid two-dimensional product marginal do not replace the hub translation weight lost by the peel. The uniformly bounded true density above shows this is a certificate obstruction, not a QFORM counterexample.

Next: pin the sharp half-Riesz formulation, compare directly with fleet03/B16 r28's true near-coloop collar, and publish the immutable report/handoff after a final correction refresh.
