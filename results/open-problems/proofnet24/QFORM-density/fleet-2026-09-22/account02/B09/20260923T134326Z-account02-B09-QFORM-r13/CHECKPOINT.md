SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T13:43:26Z.
attacking: the high-hub-leverage survivor by splitting off one compulsory physical row inside the determinant-weighted cross-volume measure, while retaining arbitrary same-side curvature.

# Early checkpoint: one compulsory-row three-volume smoothing

Status: supporting theorem proved below; full QFORM remains open.

## First unpaid implication

The prior selected-subvolume q-theorem pays rank-two hub/star aggregate volume whenever the physical hub leverage is <3/4. At the endpoint 3/4 its absolute-value Jensen route gives only |t|^{-1}, so changing q cannot cross that barrier. The next useful implication is therefore: if the selected determinant measure is concentrated on one physical hub row, can that row be spent separately while the other two row marginals remain diffuse?

The answer is yes. The result below keeps the original-coordinate cut, arbitrary quadratic phases on both sides, and gives a direct L1 characteristic-function estimate. It does not assume independence after any rotation.

## Theorem: QFORM-ONE-ANCHOR-THREEVOLUME-HYBRID-v1

Let I,J be disjoint sets of original coordinates and M=A[I,J]. After conditioning on all remaining original coordinates, allow arbitrary symmetric same-side blocks A[I,I], A[J,J] and arbitrary affine terms. Let h in I be distinguished and write a=M[h,:].

Let Omega be a nonempty selected family of actual physical 3x3 minors (R,C) of M such that h belongs to every row triple R. Put

    Z = sum_{(R,C) in Omega} det(M[R,C])^2 > 0

and normalize pi_(R,C)=det(M[R,C])^2/Z. For every i != h let

    alpha_i = P_pi(i in R).

Assume

    max_{i != h} alpha_i <= 1/2.

Then the full quadratic-plus-affine output Q has a continuous density and

    ||p_Q||_infinity
      <= 5 * 2^(4/5) * sqrt(e) * ||a||_2^(1/5) * Z^(-1/5)
      < 14.353 * ||a||_2^(1/5) * Z^(-1/5).

Consequently for every interval L,

    P(Q in L) <= 14.353 ||a||_2^(1/5) Z^(-1/5) |L|.

The quantity ||a|| Z^{-1} has the correct fifth-order scaling: scaling M by s multiplies the displayed density certificate by s^{-1}.

### Proof

Use the standard source-coordinate quadratic decoupling on the I bank. With W=X_J-X'_J, independent coordinates having densities g_j=f_j*tilde(f_j)<=1, and h_i(s)=|psi_i(2ts)|,

    |phi_Q(t)|^2 <= F(t)
      := integral prod_{i in I} h_i(<M[i,:],w>) prod_{j in J} g_j(w_j) dw.

All same-side quadratic terms disappear only under this legitimate Weyl differencing; no spectral-coordinate independence is introduced.

Write H(w)=h_h(<a,w>) and R(w)=prod_{i != h} h_i(<M[i,:],w>). Cauchy-Schwarz under the measure prod_j g_j(w_j)dw gives

    F(t)^2 <= F_2(t) F_0(t),

where

    F_2 = integral H^2 R prod_j g_j,
    F_0 = integral R prod_j g_j.

#### 1. Three-volume bound for F_2

Use exactly the selected family Omega in the Gaussian Brascamp-Lieb determinant expansion. Its row exponent at h is one, while the other row exponents are alpha_i<=1/2; let beta_j be its selected column marginals. Weighted AM-GM gives the determinant lower bound with selected mass Z. For the distinguished row use Plancherel,

    integral h_h(s)^2 ds
      = (2|t|)^(-1) integral |psi_h(u)|^2 du
      <= pi/|t|.

For every other active row, the cap-one characteristic-function estimate at p=1/alpha_i>=2 gives

    (integral h_i(s)^(1/alpha_i) ds)^(alpha_i)
      <= [2pi sqrt(alpha_i)/|t|]^(alpha_i).

The alpha_i factors cancel the row entropy factors of the BL constant. Since sum_{i != h} alpha_i=2 and the column entropy product is at most e^(3/2),

    F_2(t)
      <= 4 pi^3 e^(3/2) Z^(-1/2) |t|^(-3).          (1)

#### 2. A derived two-volume measure for F_0

For a low row pair R0={i,k} define

    z_R0 = sum_{C: ({h} union R0,C) in Omega}
             det M[{h} union R0,C]^2.

Then sum_R0 z_R0=Z. Set pi_R0=z_R0/Z. Its row marginals are exactly the alpha_i.

Let

    Z2_R0 = sum_{|C|=2} det M[R0,C]^2
           = ||M[i,:] wedge M[k,:]||_2^2.

Exterior-product monotonicity gives

    z_R0 <= ||a wedge M[i,:] wedge M[k,:]||^2
           <= ||a||_2^2 Z2_R0,

so

    Z2_R0/pi_R0 >= Z/||a||_2^2.                       (2)

For each R0 distribute its probability pi_R0 over its physical 2x2 minors proportionally to their squared determinants. This produces a genuine determinant weight w on actual physical 2x2 minors, with the same low-row marginals alpha_i. If gamma_j are its column marginals, the weighted geometric determinant mass is

    Z_eff
      = exp(E_w log(det^2/w))
      = exp(sum_R0 pi_R0 log(Z2_R0/pi_R0))
      >= Z/||a||_2^2                                  (3)

by (2).

Apply the two-volume BL calculation to F_0. Again alpha_i<=1/2, sum alpha_i=2, and the row entropy cancels against the L^p factors; the column entropy is at most e. Therefore

    F_0(t)
      <= 4 pi^2 e Z_eff^(-1/2)|t|^(-2)
      <= 4 pi^2 e ||a||_2 Z^(-1/2)|t|^(-2).           (4)

#### 3. Assemble before taking the decoupling square root

From (1) and (4),

    F(t)
      <= 4 pi^(5/2) e^(5/4)
         ||a||_2^(1/2) Z^(-1/2)|t|^(-5/2).

Hence

    |phi_Q(t)|
      <= 2 pi^(5/4) e^(5/8)
         ||a||_2^(1/4) Z^(-1/4)|t|^(-5/4).

The exponent 5/4 is strictly integrable. Combining this with |phi_Q|<=1 and integrating the exact majorant min(1,K|t|^{-5/4}) gives

    ||p_Q||_infinity
      <= (5/pi) K^(4/5)
      = 5*2^(4/5)*sqrt(e)
        ||a||_2^(1/5) Z^(-1/5).

Fourier inversion gives a continuous representative and the same coefficient times |L| for every interval. QED.

## Connection to the rank-two hub/star compiler

For A[H,I]=P C^T with P^TP=I_2, the partner account03/B09 aggregate compiler constructs an actual cut and a selected 3-minor family whose hub-pair factor is det(P[{a,b},:])^2 and whose moved-leaf factor is independent of that hub pair. For a hub row h,

    eta_h=(PP^T)_{hh}=sum_{b != h} det(P[{h,b},:])^2.

Restricting the compiler's selected family to minors that contain h therefore multiplies selected mass by eta_h. The moved-leaf marginal is unchanged. Conditional on h, the other-hub row b has distribution

    delta_b = det(P[{h,b},:])^2 / eta_h.

Thus the new theorem pays even eta_h=1 whenever max_b delta_b<=1/2 and the compiler remains in its diffuse moved-leaf branch. This strictly crosses the previous eta<3/4 barrier. The remaining high-leverage obstruction is now more specific: a high hub h whose two-dimensional Pluecker mass is itself concentrated on one partner row b, together with failure of an already-paid physical/grouped exit.

No claim is made that this last concentrated-pair survivor is impossible under the bare three-eigenvalue hypothesis.
