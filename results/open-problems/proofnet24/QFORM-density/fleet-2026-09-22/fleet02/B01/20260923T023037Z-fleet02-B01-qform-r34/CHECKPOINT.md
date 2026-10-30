# QFORM B01 r34 — early substantive checkpoint

Status: supporting N3-class estimate in progress; full QFORM remains open.

## Two-physical-hub Fourier corollary

Use Theorem H from `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` at commit `e5f71d79eff325201dd0274053d20268ce65b837`.

Split ORIGINAL coordinates as `H union I union J`, with `|H|=2`. Suppose `A_II` is diagonal. Write the leaf-to-hub coupling matrix `C=A[I,H]`, let `G=C^T C`, assume `G` is invertible, and assume every leaf row `c_i` satisfies

`c_i^T G^{-1} c_i <= 1/2`.

Theorem H with `r=0` gives, with `A_HH,A_HJ,A_IJ,A_JJ` and all affine terms arbitrary,

`|phi_Q(t)| <= min(1, 4*pi^2*det(G)^(-1/2)*|t|^(-2))`.

Since `int_R min(1,K/t^2)dt=4 sqrt(K)`, Fourier inversion gives

`||p_Q||_infty <= 4 det(G)^(-1/4)`.

This is product-provenance preserving and frequency-averaged; no scalar pointwise quadratic-phase envelope is used.

## Strict-N3 double-coloop stress family

Fix `0<eps<=1/2` and integer `m>=2`. In R^2 let `e1,e2` be the standard basis. Define an `(1+2m) x 2` left frame U by rows

- `u0=sqrt(1-eps)e1`,
- m copies `sqrt(eps/m)e1`,
- m copies `m^(-1/2)e2`,

and a right frame V by rows

- `v0=sqrt(1-eps)e2`,
- m copies `m^(-1/2)e1`,
- m copies `sqrt(eps/m)e2`.

Then `U^T U=V^T V=I_2`. Put `M=UV^T`. On a third disjoint m-coordinate bank let `w=m^(-1/2)(1,...,1)`, and set

`A_{m,eps} = [[0,M],[M^T,0]] direct_sum (w w^T)`.

Its nonzero spectrum is exactly `{1,1,-1,-1,1}`. All cross-bank diagonal entries vanish, the third-bank diagonal is `1/m`, and every physical 2x2 principal determinant has magnitude at most `(1-eps)/m`. Thus for every fixed N3 threshold `tau>0`, choosing `m>1/tau` puts this family strictly in N3.

Take the two heavy physical rows `u0,v0` as H. Take as I the m right `e1` leaves and the m left `e2` leaves. Then `A_II=0`,

`G=(1-eps) I_2`,

and each normalized leaf leverage is `1/m<=1/2`. Hence the preceding source theorem gives the actual target inequality

`||p_{X^T A_{m,eps} X}||_infty <= 4 (1-eps)^(-1/2) <= 4 sqrt(2)`

for every independent cap-one input law.

This family is simultaneously a sharp structural warning for rank-two volume peeling: `M` has singular values `(1,1)`, so `Z_2=e_2(M^T M)=1`, while the natural 2-volume row marginal of `u0` and the natural column marginal of `v0` both equal `1-eps -> 1`. Thus any proof that insists on paying the rank-two `h<1` marginal gate in a fixed orientation loses as `eps->0`, although the full target density stays uniformly bounded by a two-hub Fresnel packet.

Next: compare this exact family with the newest fleet03/B01 half-Riesz constant and derive the quantitative divergence; then isolate the structural routing statement suggested by the example.
