# QFORM-PROJECTION-CAP-NONZERO-PIVOT-BARRIER-v1

Status: `RIGOROUS COUNTEREXAMPLE TO AN INTERMEDIATE ABSTRACTION / FULL QFORM OPEN`  
Continuity: the constructed output density is continuous; global QFORM continuity remains open.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target-relevant question

The B16 assignment asks whether the actual bounded-density projection theorem can be combined with nonlinear quadratic integration after the independent product source has been compressed to a bounded joint spectral-plane density. The live corrections already say a bounded projection density alone is not enough for arbitrary indefinite coarea. This run sharpens that warning at the exact nonzero-pivot interface left by the ruled/coloop analysis.

The result below shows that even all of the following data together are insufficient:

- a two-dimensional joint probability density bounded by one;
- both of its coordinate marginal densities bounded by one;
- an independent scalar input with density bounded by one;
- a fixed invertible 3-by-3 quadratic matrix with eigenvalues exactly `{1,1,-1}` and determinant `-1`.

Thus any successful use of the product-projection theorem on the two-sheet/nonzero-pivot side must preserve stronger product provenance, such as the already proved rank-two half-Riesz control, rather than retaining only the projected density height.


## 2. Exact construction

Fix `R >= exp(2)` and put

`L = log R`, `epsilon = 1/(2L)`.

Define

`E_R = {(u,v): 1 <= u <= R, |uv+R| <= epsilon}`

and let `(U,V)` have joint density

`rho_R(u,v) = 1_{E_R}(u,v)`.

For each fixed `u`, the admissible `v` interval has length `2 epsilon/u`. Hence

`|E_R| = integral_1^R 2 epsilon/u du = 2 epsilon log R = 1`.

Therefore `rho_R` is a probability density and

`||rho_R||_infinity = 1`.

Its `U` marginal is

`p_U(u)=2 epsilon/u <= 2 epsilon = 1/L <= 1`.

For the `V` marginal, every support point obeys

`|v|=(R-s)/u >= (R-epsilon)/R = 1-epsilon/R`,

where `s=uv+R` and `|s|<=epsilon`. For fixed `v`, the admissible `u` interval therefore has length at most

`2 epsilon/|v| <= (1/L)/(1-1/(2RL)) <= 1`

because `L>=2`. Thus both coordinate marginal densities are also bounded by one.

## 3. The hyperbolic coordinate is exactly uniform

Set

`S=UV+R`.

Under the change of variables `(u,v) -> (u,s)` with `v=(s-R)/u`, the Jacobian is `1/u`. Hence, for every `|s|<=epsilon`,

`p_S(s)=integral_1^R du/u = L`.

Thus `S` is exactly uniform on `[-epsilon,epsilon]` with density `L`. Consequently

`W:=2UV=2(S-R)`

is uniform on

`[-2R-2epsilon,-2R+2epsilon]`

with density `L/2`.

## 4. Fixed target-normalized quadratic matrix and divergent output peak

Let `X` be independent of `(U,V)` and uniform on `[0,1]`. Its density is bounded by one. Put

`Q_R = X^2 + 2UV`.

The quadratic matrix in variables `(X,U,V)` is the fixed matrix

`B = [[1,0,0],[0,0,1],[0,1,0]]`.

It has

`spec(B)={1,1,-1}`, `det B=-1`.

So the Hessian geometry is completely fixed and satisfies the three-large-eigenvalue normalization. The only missing hypothesis from the full conjecture is that `U` and `V` are dependent.

The density of `Z=X^2` is

`g(z)=1/(2 sqrt(z))`, `0<z<1`.

At `t=-2R`, the density of `Q_R=Z+W` is therefore

`p_Q(-2R)
 = (L/2) integral_0^{min(1,2epsilon)} dz/(2 sqrt(z))`.

Since `R>=e^2`, `2epsilon=1/L<=1`, so

`p_Q(-2R)
 = (L/2) sqrt(1/L)
 = (1/2) sqrt(log R)`.

Hence

`||p_Q||_infinity >= (1/2) sqrt(log R) -> infinity`.

Both `g` and the uniform density of `W` belong to `L^1`, so their convolution has a continuous representative. Thus this is not a pathology caused by a nonexistent or purely singular output density.

## 5. Exact half-Riesz diagnostic

The same construction identifies what information was lost by compressing the product source to a joint density cap. Since `2UV+2R=2S`,

`E |2UV+2R|^{-1/2}
 = L integral_{-epsilon}^{epsilon} |2s|^{-1/2} ds
 = 2 L sqrt(2 epsilon)
 = 2 sqrt(log R)`.

This diverges although the joint density and both coordinate marginal densities remain capped by one.

By contrast, the completed source theorem `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` gives a dimension-free half-Riesz bound for a genuine rank-two quadratic form of the original independent product input. This is exactly a product-provenance invariant destroyed by the cap-only abstraction.

## 6. Actual use of the designated account04/B16 result

The completed account04/B16 ruled/Pluecker endpoint theorem uses the genuine product projection theorem to obtain, on its spectral two-plane,

`||rho_Y||_infinity <= 2`.

Suppose one tried to close its unpaid nonzero-pivot/two-sheet side using only that projected density height, through any inequality of the common scale form

`||p_{aX^2+2X L(Y)+q_2(Y)}||_infinity
 <= C ||rho_Y||_infinity^alpha |det B|^{-beta}`

with finite universal `C,alpha,beta`.

The family above satisfies the stronger data `||rho_R||_infinity=1` and `|det B|=1`, so such an estimate would give `||p_Q||_infinity<=C`, while the exact computation gives

`||p_Q||_infinity >= (1/2)sqrt(log R)`.

This is a contradiction as `R->infinity`. Therefore the partner's valid `<=2` projection-height inequality is useful but cannot be the sole receiver-side datum in the remaining nonlinear integration. The application is quantitative: even replacing the partner's `2` by the strictly stronger `1` does not make the cap-only continuation valid.

The partner's one-sheet bound and its product-provenance proof remain untouched. This construction is not a QFORM counterexample because `(U,V)` are not independent original coordinates and have not been shown to be a linear projection of an independent cap-one product source.

## 7. Consequence for the next mechanism

The exact next implication should retain an invariant that excludes the family above. A natural source-valid candidate is a **product-projection curved half-Riesz transition inequality**: combine the true two-dimensional projection theorem with the already completed rank-two affine half-Riesz estimate before taking the scalar quadratic pushforward. In particular, the receiver must remember more than `||rho_Y||_infinity`; it must retain original-product Fourier/fractional-potential geometry.

A useful diagnostic for any proposed near-null-coloop proof is now immediate: if, after projection, its only hypotheses on `Y` are a bounded joint density and bounded one-dimensional marginals, it cannot be correct, even for the fixed matrix `B` above.

## 8. Scope

- Full QFORM: OPEN.
- This does **not** refute QFORM.
- It refutes a cap-only nonlinear projection-product interface at a fixed normalized nonzero pivot.
- It strengthens the existing warning by preserving cap-one coordinate marginals and a fixed spectrum `{1,1,-1}`.
- Global continuity: OPEN. The constructed dependent test family itself has a continuous output density.
