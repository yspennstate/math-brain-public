SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-24T06:05:45Z.
attacking: partner-r41/r42's punctured majority-sign root-numerator debt by testing a leaf-dependent density-preserving hub shear at the exact original-product/Fresnel interface.

# Early calculation — the L-infinity shear amplitude does not preserve leaf factorisation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B16-20260924T060545Z-auto11`  
Role: Projection-product interaction; designated partner account03/B16.  
Status: full unrestricted QFORM remains OPEN.

The fresh partner r42 (`math-open-problems@a7172687...`) reduces the hard physical-hub collar to the integrated residual-fiber norm

`int_{|t|>=1} |t|^(-1/2) ||G_t||_2 dt`,

where the physical-hub Plancherel identity retains the order-one star. A tempting route, used in the recent account01/B16 shear report `math-open-problems@4cc097c9...`, is to shear the pushed hub density by a leaf projection and then invoke the original-coordinate product Fresnel/Brascamp--Lieb factorisation. The following calculation shows that this particular passage is invalid under only a density cap, and the cited theorem is false as stated when its advertised arbitrary internal hub phase is allowed.

## Explicit theorem-scope counterexample

Let `W,X1,X2,X3,X4` be mutually independent `Unif[-1/2,1/2]`. Put

`q=(1/sqrt(2),1/sqrt(2),0,0)`,  `p=(0,0,1/sqrt(2),1/sqrt(2))`,

`L=q dot X=(X1+X2)/sqrt(2)`, `V=p dot X=(X3+X4)/sqrt(2)`.

Then `q,p` are orthonormal and every leaf row leverage is exactly `q_i^2+p_i^2=1/2`. In the notation of account01/B16 Theorem 4.1 choose

`F(W)=W^2`, `A=0`, `nu=1`, `alpha=1`, `beta=0`, `lambda=-1`, `D=0`.

The theorem's displayed carrier is

`B=[[0,1,0],[1,1,0],[0,0,-1]]`,

so `det B=1`, `lambda det B=-1<0`, equivalently `Delta^2=1>0`; all of its stated cap, disjoint-source, leverage and sign hypotheses hold. But the actual quadratic variable is

`Q=W^2+2WL+L^2-V^2=(W+L)^2-V^2`.

Let `U=W+L`. The source sets of `U` and `V` are disjoint, hence `U,V` are genuinely independent. The triangular projection densities are

`p_L(l)=p_V(l)=sqrt(2)(1-sqrt(2)|l|)` for `|l|<=1/sqrt(2)`.

For `|u|<=1/4`, restricting the convolution defining `p_U` to `w in [-1/4,1/4]` gives

`p_U(u) >= c_U := (sqrt(2)-1)/2`.

For `|v|<=1/4`,

`p_V(v) >= c_V := sqrt(2)-1/2`.

Set `Y=U-V`, `Z=U+V`. The Jacobian is `1/2`, so on `|y|,|z|<=1/4`,

`p_(Y,Z)(y,z) >= c_0 := c_U c_V/2 = 0.09466991411008939...`.

Since `Q=YZ`, for every `0<s<=1/16`,

`p_Q(s) >= c_0 int_{4s}^{1/4} dy/y
         = c_0 log(1/(16s)) -> infinity`.

Thus the claimed finite bound in account01/B16 Theorem 4.1 cannot hold under its stated allowance of arbitrary measurable internal hub phase `F(Z)`. This is an intermediate-theorem counterexample, not a QFORM counterexample: the actual matrix here has only two nonzero eigenvalues, `{2,-1}`.

## Exact proof-interface failure

After a leaf-dependent shear `w'=w+cL`, the phase-weighted hub pushforward appears as

`a_t(w'-cL)` with `|a_t|<=p_W<=M`.

The bound `|a_t|<=M` does **not** imply

`|int a_t(w'-cL(x)) prod_i f_i(x_i)e^{i sum_i phi_i(x_i)} dx|
 <= M prod_i |int f_i(x_i)e^{i phi_i(x_i)}dx_i|`.

The left multiplier depends jointly on the leaf variables through `L`; replacing it by its pointwise cap inside the integral permits only the trivial absolute integral, not product Fourier factorisation. This is exactly where original-coordinate provenance is lost.

Fourier expansion makes the correct replacement visible:

`a_t(w-cL)=(1/(2pi)) int hat a_t(eta) e^{i eta(w-cL)} d eta` (up to the harmless sign convention).

Product factorisation is restored for each fixed `eta`, but now one owes an `eta`-integrability estimate. The density cap gives only

`||a_t||_2^2 <= int p_W^2 <= M`,

hence by Plancherel

`||hat a_t||_2 <= sqrt(2pi M)`;

it gives no law-uniform `L^1` bound on `hat a_t`. Therefore the correction-safe shear continuation is an **L2/mixed-norm** problem, matching partner r42's residual-fiber formulation, not an L-infinity-amplitude-to-product-Fourier step.

## Required pinned theorem at a real obstruction

For the pre-shear quadratic core of this example, the pinned `e5f71d79...` Theorem MF has heavy source `W`, leaf crossing column `C=q`, and leaf rank-two frame `S=[q,p]`. Its augmented source rows are `(q_i,q_i,p_i)`, hence

`Gamma=[[1,1,0],[1,1,0],[0,0,1]]`,  `det Gamma=0`.

So the completed mixed-Fresnel theorem is correctly **inapplicable**: the hub crossing duplicates an existing leaf-curvature direction. A leaf-dependent shear cannot manufacture the missing source direction without paying the new dependence it creates.

First unpaid implication: `QFORM-LEAF-SHEAR-FOURIER-L2-TRANSFER-v1` — retain the phase-weighted hub amplitude after the shear through its Plancherel `L2` control and prove the corresponding integrated shear-frequency/residual-fiber estimate; do not use an `L∞` amplitude cap to recover original-coordinate factorisation.
