# Point-controller residual with the retained interleaved reserve

All entropies are bits. At any actual reached cylinder of F=1+A_r(u-1), let s>=1 point controls remain live, q=2^-s, m=Eu for the current Boolean core, a=1-m, V=1-m^2 and z=qa. A failed control kills the activation; no assumption on remaining core bias or exposure order is made. Define U=q[H(u)-eta(m^2)] and R=q log2(1/q)V as in A059. At a controller reveal U has zero expected drift and kappa=R-E R_child=qV, including m=+/-1. Its actual physical influence is z.

Separate the queried-control Fourier pairs by data frequency. Every nonempty core-frequency pair has equal magnitudes q*|uhat(T)|; summing over the 2^(s-1) remaining control frequencies gives exactly qV of erasure. At the empty data frequency, all nonempty remaining-control pairs have equal magnitude qa, contributing (q-2q^2)a^2. The empty remaining-control pair has amplitudes 1-qa and -qa. Thus, with Phi(A,B)=(A+B)h2(B/(A+B)),

    B_control-kappa=(q-2q^2)a^2+Phi((1-z)^2,z^2)
                  =za-2z^2+Phi((1-z)^2,z^2) >=0.

Since a<=2, this is at most b(z)=2z(1-z)+Phi((1-z)^2,z^2). The previously proved A019 scalar b(z)<=3z admits a short independent check. For 1/4<=z<=1/2, Phi(A,B)<=2sqrt(AB) gives b(z)<=4z(1-z)<=3z. For 0<z<=1/4, Phi(A,B)<=B log2(e(A+B)/B) and A+B<=1 give b(z)/z<=2(1-z)+z[2log2(1/z)+1/ln2]. The latter expression increases on that interval and its endpoint is 5/2+1/(4ln2)<3, using ln2>1/2. For z>=1/2, symmetry b(z)=b(1-z) proves b(z)<=3(1-z)<=3z. z=0,1 are direct endpoints. This scalar price is consumed/reconstructed, not a new optimization of A019.

The full physical entropy decrement is D=B+J. The uniform Boolean child-channel estimate 0<=J<=2 Inf_control/ln2 applies to the entire normalized physical child spectra, rather than projected rows. For completeness, a scalar Fourier pair A,B has gap (A^2+B^2)[1-h2(1/2+AB/(A^2+B^2))]. Put x=2|AB|/(A^2+B^2). The natural binary divergence d(x)=[(1+x)ln(1+x)+(1-x)ln(1-x)]/2 obeys d(x)<=1-sqrt(1-x^2), since d'(x)=atanh(x)<=x/sqrt(1-x^2); the latter follows by differentiating the difference from zero. Multiplication and division by ln2 give the pair price 2min(A^2,B^2)/ln2<=2B^2/ln2. Summing normalized actual Fourier pairs yields the queried-influence bound. This reconstructs the closed C005 scalar dependency. Therefore

    0<=D_control-kappa<=(3+2/ln2) Inf_control.             (P)

Every sign and constant-core endpoint is included. At m=+1 all terms vanish. At m=-1, kappa=0 and the controller is an ordinary point-defect sign; it is not discarded as a zero-variance core. (P) holds at every live point-control step even after arbitrary data reveals and history-dependent choices. Once a mismatch occurs all later controls have zero influence/debit. Summing under actual physical reach probabilities gives

    sum_control w(D-kappa)<=(3+2/ln2) Pi_control.

This pays precisely A059's controller residual on the point-activation geometry, with no reuse of its R bank. Combining the reviewed signed DATA bound gives the terminal-inclusive stopped inequality

    H(F_root)<=U_root+R_root+(3/ln2) T_data
                   +(3+2/ln2) Pi_control+E[H_leaf-U_leaf-R_leaf],
    T_data=sum_data w q beta^2 <=Pi_data,
    I(F_root)=Pi_data+Pi_control+E I_leaf.

The remaining signed terminal functional is actual, not the terminal of a control-first or data-first alternative. It has an exact profile factorization for every exclusive independent-core controller, which is useful at the boundary. Put g(z)=sum_j m_j C_j(z), and let gamma_j be the probability law Chat_j(T)^2/q_j for q_j>0. Empty-data Fourier rows are exactly ghat, and a nonempty frequency in core j has coefficient Chat_j(T)*uhat_j(S). Distinct cores have disjoint nonempty data supports, so product homogeneity gives

    H(F)=U+sum_j V_j Eraw(Chat_j^2)+Eraw(ghat^2),
    H(F)-U-R=Eraw(ghat^2)+sum_j q_j V_j H(gamma_j) >=0.

Here Eraw(a^2)=sum_T eta(a_T^2), with no renormalization of the subunit-mass mean profile. Its coefficients have magnitude <=1 because |g|<=1. Each gamma_j is normalized by Parseval. Thus this factorization never turns the terminal into a negative entropy credit and makes its controller profile explicit.

When the ACTUAL controller state is resolved at a leaf, only one q_j=1 remains. Its indicator spectrum is the empty point mass and g is the constant mean m_j. Consequently H_leaf-U_leaf-R_leaf=eta(m_j^2). Since -(1-V)ln(1-V)<=V and Var(u_j)<=I(u_j),

    0<=H_leaf-U_leaf-R_leaf<=I(F_leaf)/ln2.

Unused controller coordinates may remain if its label is already constant; that does not change this boundary price. It does not hold by this argument at an arbitrary unresolved-controller frontier. If an arbitrary controller remains and the cores are constants, the profile can be its full Fourier entropy.

Therefore a point-activation tree stopped with its controller state resolved has the quantitative boundary-complete continuation

    H_root<=U_root+R_root+(3/ln2)T_data
                     +(3+2/ln2)Pi_control+E I_leaf/ln2.

U_root=q E_ne(u) remains an arbitrary-core entropy resource. Funding R_root from root control influence at most 2I_control(root) does not authorize spending that same original control account a second time: in the displayed inequality R_root and residual debits are separately declared charges. No universal FEI constant or arbitrary-core entropy bound follows.

First unsupported extension: general exclusive controllers have no point-indicator pair multiplicities, and their residual may encode an arbitrary Boolean controller even with constant cores. Shared physical data also breaks the independent-core decomposition. The route to a universal policy still requires the actual controller/terminal H-U-R quantity and inherited U to be paid jointly by unspent influence or certified core deficits. This note supplies a scoped residual payment, pending independent A090/A085 review; A091 is a contributor to it.
