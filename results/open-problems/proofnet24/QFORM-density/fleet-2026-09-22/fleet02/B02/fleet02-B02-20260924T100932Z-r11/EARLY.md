# fleet02/B02 r11 — early calculation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Integrated Fourier estimate / complementary constructions and source-valid counterexamples  
Target status: full QFORM OPEN.

## Sharp-HY D2 half-potential calculation

Let `I,J` be disjoint ORIGINAL-coordinate banks, `M=A[I,J]`,

`Z2=e2(M^T M)>0`,

and let `alpha_i` be the row marginals of the normalized squared `2x2`-minor law. The completed D2 half-potential theorem in fleet02/B13 used the rough `L^p` Fourier input. Re-running exactly the same physical decoupling/BL argument with the reviewed sharp Hausdorff--Young input from the volume-stability report gives the following improved constant.

For `q>=1` with `alpha_i<=q/2` for every row, the sharp-HY computation at exterior degree two is

`E F_t^q <= e^2 q^(-1) (pi/|t|)^2 Z2^(-1/2)`.

After the one-sided Cauchy--Schwarz decoupling,

`|phi_Q(t)| <= min(1, B_q |t|^(-1/q))`,

`B_q=[e^2 q^(-1) pi^2 Z2^(-1/2)]^(1/(2q))`.

For the half-potential, the pinned fractional-potential formula at `alpha=1/2` has `c_(1/2)=(2pi)^(-1/2)`. Since `q<2` is exactly the high-frequency integrability gate,

`H_(1/2)(Q)`
` <= (2pi)^(-1/2) * [8/(2-q)] * B_q^(q/2)`
` = [4 sqrt(2e) q^(-1/4)/(2-q)] Z2^(-1/8).`

Thus, for every strict marginal gate `h<1`, choosing `q=max(1,2h)` gives

`C2_sharp(h)=4 sqrt(2e)` for `h<=1/2`,

and

`C2_sharp(h)=2 sqrt(2e) (2h)^(-1/4)/(1-h)` for `1/2<h<1`,

with

`H_(1/2)(Q) <= C2_sharp(h) Z2^(-1/8)`.

This improves the completed rough-HY constants `8e^(1/4)` and `4e^(1/4)(2h)^(-1/4)/(1-h)` while preserving arbitrary same-bank quadratic phases, outside couplings and affine terms. No random coordinate is rotated.

## Immediate r47 scalar-pivot specialization

On fleet03/B02 r47's strong physical-diagonal branch, take the literal pivot `d=A_ii` with `|d|>1/228` and let `S` be the exact scalar Schur complement. If a literal physical Schur cross block `M=S[I,J]` has `Z2>0` and its row pair-volume marginals satisfy `alpha_i<=h<1`, the scalar square peel yields

`||p_Q||_infinity <= sqrt(228) C2_sharp(h) Z2^(-1/8).`

At `h=1/2` this is

`||p_Q||_infinity <140.828209 Z2^(-1/8).`

At `h=3/4` it is

`||p_Q||_infinity <254.505303 Z2^(-1/8).`

If both row and column `h=3/4` gates fail, then one physical row and one physical column have pair-volume inclusion probabilities `>3/4`; inclusion-exclusion forces their common incident `2x2`-minor mass to exceed `Z2/2`. Hence the diffuse Schur-E2 part of the previous B02 unpaid implication is paid, and failure produces a single physical bi-star anchor rather than a one-good-minor claim.

## Exact-target diffuse-E2 obstruction to one-minor / D'/D5 closure

For integer `k>=2`, take one isolated physical scalar pivot `W` with `A_WW=1`, two physical center coordinates `V1,V2`, and two leaf banks of size `k`. Join every leaf in bank 1 to `V1` by `1/sqrt(k)` and every leaf in bank 2 to `V2` by `1/sqrt(k)`; all other coefficients vanish.

The nonzero spectrum is exactly `{-1,-1,1,1,1}`, so this is in the exact owner target for every `k`. After pivoting `W`, the literal leaf-to-center Schur cross block `M_k` has singular values `1,1`, hence `Z2=1`. Its `2x2` volume law is uniform over the `k^2` choices of one leaf from each bank, so every leaf row marginal is `1/k<=1/2`. Therefore the new sharp-HY D2 theorem plus the square peel gives the uniform bound

`||p_Q||_infinity <=4 sqrt(2e)=9.326575927...`

for all `k` and all cap-one product input laws.

But every nonzero physical `2x2` minor of `M_k` has determinant modulus `1/k` and second singular value `1/sqrt(k)`: any receiver based on one selected physical `2x2` minor deteriorates with `k`. Moreover the full symmetric matrix is a disjoint union of two stars plus the isolated diagonal pivot, so every disjoint physical cross block has rank at most two. Consequently every such block has `E3=E5=0`: D', the reviewed sharp-HY `E3` density compiler and D5 all have zero currency on this exact-target family. This is a source-valid obstruction to a D'/D5-or-one-good-minor closure, not a QFORM counterexample.

The remaining endpoint is the fixed physical bi-star/near-coloop concentration branch when the Schur `E2` volume marginals approach one.
