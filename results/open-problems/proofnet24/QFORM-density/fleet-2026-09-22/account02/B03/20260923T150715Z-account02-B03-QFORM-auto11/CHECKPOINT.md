SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-23T15:07:15Z.
attacking: the nested-heavy deletion-plane endpoint by extracting TWO genuine physical rows before the Fresnel integral and using an unconditional L2 Brascamp--Lieb estimate on the twice-deleted plane.

# Early substantive checkpoint — two physical rows + twice-deleted plane

Programme: `QFORM-DENSITY-3EIG-20260922`.  Full target remains OPEN.  This calculation preserves original-coordinate independence and never splits a coordinate sum from its conjugate difference.

Let `X_1,X_2` and `Y=(Y_j)` be mutually independent cap-one physical variables, and let `Omega` be independent of them.  Let `U=U(Omega)` have density cap `L`; `xi(Omega),F(Omega)` may depend arbitrarily on `U`.  For `A d !=0`, write

`T=A(alpha_1 X_1+alpha_2 X_2+h.Y+xi)^2 + 2d U(b_1X_1+b_2X_2+g.Y)+F`.

Put selected frequency rows `c_i=(alpha_i,b_i)` and

`Delta=|det(c_1,c_2)|>0`,
`r_j=(h_j,g_j)`, `G=sum_j r_j r_j^T`, and assume `det G>0`.

After the pinned e5 damped Fresnel linearisation, setting `eta=2td u`,

`|phi_T(t)| <= (4pi|tA|)^(-1/2)(2|td|)^(-1)
 int p_U(eta/(2td)) |chi_1(c_1.(s,eta)) chi_2(c_2.(s,eta))|
     prod_j |Psi_j(r_j.(s,eta))| ds deta.`

Take Cauchy--Schwarz in the whole `(s,eta)` plane.  For the selected factor, `p_U<=L`, change variables by the two selected rows and use Plancherel:

`||p_U(eta/(2td)) chi_1(c_1.y)chi_2(c_2.y)||_2
 <= 2pi L Delta^(-1/2)`.

For the twice-deleted product factor, normalize the rows by `G^(-1/2)`.  If `ell_j=r_j^T G^(-1)r_j`, geometric rank-one Brascamp--Lieb applied to the SQUARE of the product gives

`||prod_j Psi_j(r_j.y)||_2^2
 <= det(G)^(-1/2)
    prod_j [ell_j^(-1/2) int |Psi_j|^(2/ell_j)]^ell_j`.

Here no leverage restriction is needed because `0<=ell_j<=1`, so `2/ell_j>=2`.  The required pinned e5 estimate

`int |Psi|^p <=4pi/sqrt(p)`

gives each bracket at most `2sqrt(2)pi`.  Since `sum ell_j=2`,

`||prod_j Psi_j(r_j.y)||_2 <=2sqrt(2)pi det(G)^(-1/4)`.

Therefore

`boxed:
 |phi_T(t)| <= min{1,K |t|^(-3/2)},
 K=sqrt(2) pi^(3/2) L |A|^(-1/2)|d|^(-1)
   Delta^(-1/2) det(G)^(-1/4).
}`

and Fourier inversion yields

`boxed:
 ||p_T||_infinity
 <=3*2^(1/3) L^(2/3)|A|^(-1/3)|d|^(-2/3)
   Delta^(-1/3) det(G)^(-1/6).
}`

This strictly removes the `max deletion leverage <=3/4` analytic requirement of account02/B03 r12 whenever a second genuine physical row is extracted and both the selected pair and twice-deleted coefficient plane remain rank two.

For the live one-sided packet `Q=a^(-1)H^2+2 sigma U V`, let `B` be the right-bank row matrix with rows `(h_j,v_j)`, `det(B^TB)=m^2`, and for a physical pair `e={r,s}` define

`p_e=det((h_r,v_r),(h_s,v_s))^2/m^2`,
`q_e=det(B_{-e}^T B_{-e})/m^2`.

Using `m=rho y`, `y^2>1/2`, `gamma=rho^2/|a|`, and the source spectral identity `gamma sigma^2>=s_3(A)^3`, the displayed theorem gives the target-homogeneous inequality

`boxed:
 ||p_Q||_infinity
 <= 3*2^(2/3)e^(1/3) s_3(A)^(-1) (p_e q_e)^(-1/6)
 <6.647 s_3(A)^(-1)(p_e q_e)^(-1/6),
}`

using the valid scalar product-projection cap `L<=sqrt(e)`.  Here `q_e` is exactly the determinant-volume probability that an independent sampled right-plane basis is disjoint from `e`; this is a concrete two-row receiver for the nested-heavy state.  It does not yet pay the simultaneous endpoint `p_e q_e ->0`.
