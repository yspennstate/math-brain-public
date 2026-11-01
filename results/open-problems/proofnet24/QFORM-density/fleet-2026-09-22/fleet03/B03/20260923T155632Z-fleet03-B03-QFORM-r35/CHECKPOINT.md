SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T15:56:32Z.
attacking: the near-coloop angular-cancellation survivor by squaring the Fresnel representation before absolute values, lifting each physical right-bank row to two maps in R^3, and using the newest twisted L^p input without separating any conjugate sum/difference pair.

# Early substantive checkpoint — lifted two-copy Fresnel geometry

Programme: `QFORM-DENSITY-3EIG-20260922`. Full theorem remains OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

Work in the exact angular packet from fleet03/B03 r32/r34

`Q = a^(-1)(H0 + h.X_R)^2 + 2 sigma U (v.X_R)`,

where the right bank `X_R` is an original-coordinate product bank independent of the background containing `(H0,U)`, `v,q` are orthonormal, and

`h = beta v + m q`, `m>0`, `S^2:=||h||_2^2=beta^2+m^2`, `det([h,v]^T[h,v])=m^2`.

For each right coordinate j put

`eta_j=v_j^2+q_j^2`, `theta_j=h_j^2/S^2`.

The r34 near-coloop survivor has some physical j with `eta_j>2/3`; the new branch below is designed for the deeper angular-cancellation subcollar where the lifted map remains light.

## 1. Squared Fresnel representation

For fixed background, Fresnel linearisation gives

`F_t(H0,U)=c_t int exp(-i a s^2/(4t)+i s H0) prod_j psi_j(h_j s+2t sigma U v_j) ds`,

with `|c_t|^2=|a|/(4 pi |t|)`.

Cauchy-Schwarz is taken ONCE over the whole background, not inside a duplicated coordinate pair:

`|phi_Q(t)|^2 <= E |F_t(H0,U)|^2`.

After expanding the square, taking absolute values only at that stage, and using the true marginal projection cap `||p_U||_infinity<=L`, the change `eta=2t sigma U` yields

`|phi_Q(t)|^2 <= [|a| L/(8 pi |sigma| |t|^2)] I_3`,

where

`I_3=int_{R^3} prod_j |psi_j(h_j s+v_j eta)| |psi_j(h_j s'+v_j eta)| ds ds' d eta`.        (C.1)

No `X-X'` variable has been declared independent of its conjugate sum.

## 2. Exact lifted Gram matrix

Introduce two lifted maps for every physical row:

`A_j=(h_j,0,v_j)`, `B_j=(0,h_j,v_j)` in R^3.

Their Gram sum is

`G_3=sum_j(A_j A_j^T+B_j B_j^T)
    =[[S^2,0,beta],[0,S^2,beta],[beta,beta,2]]`.

A direct determinant computation gives the nondegenerate identity

`det G_3 = 2 S^2 m^2`.                                                   (C.2)

Moreover the leverage of EACH lifted copy of physical coordinate j is

`ell_j=A_j^T G_3^(-1) A_j=B_j^T G_3^(-1) B_j
      = (eta_j+theta_j)/2`.                                             (C.3)

Thus the dangerous physical near-coloop `eta_j ->1` becomes a harmless lifted half-leverage exactly when its angular coefficient obeys `theta_j<=1-eta_j`.

## 3. First integrated consequence

Assume for the moment

`eta_j+theta_j<=1` for every right physical coordinate j.                (C.4)

Then every lifted leverage is at most 1/2. Normalize the lifted frame by `G_3^{-1/2}` and apply geometric rank-one Brascamp-Lieb. The newest Claude twisted Fourier input

`int_R |psi(x)|^p dx <= 4 pi/sqrt(p),  p>=2`

is applied at the actual exponents `p=1/ell_j>=2`. The `sqrt(ell_j)` scaling factors cancel exactly, giving

`I_3 <= (4 pi)^3 / sqrt(det G_3)
     = (4 pi)^3 /(sqrt(2) S m)`.                                      (C.5)

Combining (C.1)-(C.5),

`|phi_Q(t)|^2 <= min{1, A_2 |t|^(-2)}`,

`A_2 = 4 sqrt(2) pi^2 L |a|/(|sigma| S m)`.                         (C.6)

With the completed scalar product-projection cap `L<=sqrt(2)`, this simplifies to

`A_2 <= 8 pi^2 R`, `R:=|a|/(|sigma| S m)`.                          (C.7)

This is the first substantive checkpoint. It is a genuine whole-copy integrated-time mechanism, stable at a physical near-coloop provided the lifted-light gate (C.4) holds. The remaining work in this run is to compute its exact L2/fractional consequences, splice it to a completed receiver that yields one-copy linear small-ball scaling, apply the designated fleet04/B03 collision result, and state precisely what geometry remains when (C.4) fails.
