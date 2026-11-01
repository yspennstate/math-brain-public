# Hub-square receivers for product inputs

Status: proved scoped lemmas. These do not prove the unrestricted QFORM/RMT density conjecture.

Let all densities be Lebesgue densities. The caps below may be any positive constants.

## 1. Definite two-hub block

Let H=(H_1,H_2) have independent coordinates with density caps K_1,K_2, and let Y be independent of H. Let B be a definite real symmetric 2 by 2 matrix, b(Y) any measurable vector, and R(Y) any measurable real function. Then

Q=H^T B H+b(Y)^T H+R(Y)

has a density bounded by

pi K_1 K_2 / sqrt(det B).

This includes any quadratic or affine light-only tail, any light-to-hub couplings, and an off-diagonal H_1 H_2 coefficient. There is no light density assumption.

Proof. Condition on Y and complete the square. A translation in H leaves the joint density cap K_1K_2 unchanged. The linear change z=|B|^{1/2}H has Jacobian 1/sqrt(det B). The remaining quadratic is either |z|^2 or -|z|^2. Polar coarea gives the density at every noncritical level as one half the angular integral of the transformed joint density, hence at most pi K_1K_2/sqrt(det B). Conditional mixing preserves the bound.

The signature assumption matters: H_1^2-H_2^2 with independent unit-density uniform hubs has a logarithmic density singularity at zero.

## 2. Mixed square and linear hubs

Let H_1,H_2,Y be mutually independent, with hub density caps K_1,K_2. Let a be nonzero, b(Y),R(Y) arbitrary measurable functions, and d(Y) a real random variable with marginal density cap D. Then

Q=aH_1^2+b(Y)H_1+d(Y)H_2+R(Y)

has a density bounded by

4 K_1 sqrt(2K_2 D/|a|).

In particular, if d(Y)=cL(Y)+u with c nonzero and L density cap M, then D=M/|c| and the bound is 4K_1 sqrt(2K_2M/(|ac|)). The result allows arbitrary correlations between b,d,R through Y. It requires that there be no H_1H_2 product or H_2^2 term.

Proof. Condition on Y. Completing the square in H_1 translates its law, without changing its cap. For every measurable set E of length delta, the conditional probability that aH_1^2+bH_1 lies in E is at most 2K_1 sqrt(delta/|a|). Indeed, after translation and dilation, the preimage of E under x↦x^2 has length at most 2sqrt(delta), by rearrangement of the kernel z^(-1/2) on the positive half-line.

For d nonzero, dH_2 has a probability density bounded by N=K_2/|d|. The bathtub inequality applied to its convolution with the quadratic-hub law gives a density bound

N sup_{|E|≤1/N} P(aH_1^2+bH_1∈E)
 ≤ 2K_1 sqrt(N/|a|)
 = 2K_1 sqrt(K_2/(|ad|)).

Finally, for any probability density bounded by D,

E |d|^(-1/2) ≤ D ∫_{-1/(2D)}^{1/(2D)} |x|^(-1/2)dx = 2sqrt(2D).

Average the conditional bound. Since d has a density, P(d=0)=0.

## 3. Three independent stars with arbitrary hub squares

For j=1,2,3, let (H_j,Y_j) be mutually independent across j, and H_j independent of Y_j. Assume H_j density cap K_j and L_j=L_j(Y_j) density cap M_j. Let c_j be nonzero. For arbitrary real a_j,u_j and arbitrary measurable light-only R_j,

Z_j=a_jH_j^2+c_jH_jL_j+u_jH_j+R_j(Y_j).

Then Z_1+Z_2+Z_3, plus any further independent random summand, has a bounded continuous density with

||p||_infinity ≤ 6 ( product_{j=1}^3 K_j M_j / |c_j| )^(1/3).

Proof. Fix t nonzero and define the complex density
g_{j,t}(l)=f_{L_j}(l) E[e^{itR_j(Y_j)} | L_j=l].
It obeys |g_{j,t}|≤f_{L_j} and ||g_{j,t}||_2^2≤M_j. Fourier transforming g_{j,t} in l and applying Cauchy–Schwarz in h gives, uniformly in a_j and u_j,

|E e^{itZ_j}|
 ≤ ||f_{H_j}||_2 ( ∫ |hat g_{j,t}(c_jth)|^2 dh )^(1/2)
 ≤ sqrt(2pi K_j M_j/(|c_j t|)).

Also |E e^{itZ_j}|≤1. Let D_0 be the product of the three square-root constants. Independence implies that the total characteristic function is bounded by min(1,D_0|t|^(-3/2)), which is integrable. Fourier inversion and the identity
∫_0^infinity min(1,D_0t^(-3/2))dt=3D_0^(2/3)
give the stated constant. Multiplication by the characteristic function of any further independent summand does not increase the bound.

The same argument gives, for n≥3 independent stars,
||p||_infinity ≤ [2n/(n-2)] (product_{j=1}^n K_jM_j/|c_j|)^(1/n).

## 4. Why two arbitrary hub-square stars do not suffice

Take H,L independent uniform on [-1/2,1/2], each with density cap one. With a=1,c=2,u=0,R(L)=L^2, the star is Z=(H+L)^2. Since H+L has triangular density 1-|x| on [-1,1],

p_Z(z)=z^(-1/2)-1, 0<z<1.

Thus Z is not in L^2. For an independent copy Z', the density of Z-Z' is unbounded at zero: formally its value there is ∫_0^1 p_Z(z)^2 dz=infinity, and the essential supremum diverges logarithmically near zero. This quadratic form has rank two, so it does not refute a theorem under s_3(A)≥1. It does disprove any attempt to extend the two-star L^2 convolution lemma uniformly to arbitrary nonzero hub-square coefficients and arbitrary light-only tails.

## Relation to the open theorem

These results provide density receivers when a structural decomposition exposes a definite physical two-hub block, one square hub plus a transverse linear hub with a capped slope, or three independent star blocks. The condition s_3(A)≥1 alone has not been shown to force any of these decompositions. The unrestricted product-input QFORM/RMT density theorem, with arbitrary rank, affine term, and hub-square coefficients, remains open.
