# Independent obstruction for the cumulant route

Saved on 2026-10-10 before reading w456's derivation. The only paired information seen so far is STATUS.md's lane description. All statements below are pending w458's independent check and make no novelty claim.

Let a finite free-boundary FK graph have N vertices, integer q>=3, and component sizes n_C. In the Edwards-Sokal coloring set X_v=1{sigma_v=1}-1/q and S=sum_v X_v. Conditional on the FK configuration, S=sum_C n_C Y_C, where independent Y_C have the centered Bernoulli(1/q) distribution. Write c_j=kappa_j(Y_C). Its first four cumulants are c_1=0,

    c_2=(q-1)/q^2,
    c_3=(q-1)(q-2)/q^3,
    c_4=(q-1)(q^2-6q+6)/q^4.

Conditional independence and E(S|FK)=0 give the exact unconditional identities

    kappa_2(S)=c_2 E sum_C n_C^2,
    kappa_3(S)=c_3 E sum_C n_C^3,
    kappa_4(S)=c_4 E sum_C n_C^4
                  +3*c_2^2 Var(sum_C n_C^2).

For the fourth identity, E(S^4|FK)=c_4 sum_C n_C^4+3*(c_2 sum_C n_C^2)^2; subtract 3(E S^2)^2. Thus averaging conditional fourth cumulants alone omits the variance term. At q=3 this is

    kappa_4(S)=-(2/27) E sum_C n_C^4
                  +(4/27) Var(sum_C n_C^2).

This identity does not by itself determine the sign of kappa_4(S). The third cumulant is strictly positive even at beta=0, where the Potts spins are independent and the field pressure is analytic. Positivity alone therefore cannot certify a thermal transition.

Let P_N(h)=N^(-1)log E exp(hS), chi=P_N''(0)>0, and let I_N be its local Legendre transform using centered magnetization m=P_N'(h). Differentiating the inverse function, with all pressure derivatives evaluated at h=0, gives

    I_N''(0)=1/chi,
    I_N'''(0)=-P_N'''(0)/chi^3,
    I_N''''(0)=3*(P_N'''(0))^2/chi^5 - P_N''''(0)/chi^4.

Consequently a nonzero field cubic is not a uniform nonzero magnetization cubic. Passing to criticality needs bounds for these ratios and a remainder bound on a fixed magnetization interval; finite-volume analyticity does not supply either uniformly.

Here is an explicit S_3-invariant continuous-onset counterexample if that regularity is omitted. For z in C, r=|z|, define

    F_t(z)=-t*r^2+r^(5/2)-Re(z^3)+r^4.

It is invariant under z -> exp(2*pi*i/3)z and z -> conjugate(z), the standard planar action of S_3. It has a fixed nonzero invariant cubic polynomial term. Put c=1-2/(3*sqrt(3))>0. For s=sqrt(r)>=0, min_s(1-s+s^3)=c, so

    F_t(z)>=-t*r^2+c*r^(5/2).

For t<=0 the unique global minimizer is z=0. For t>0, sufficiently small positive real z makes F_t(z)<0, and coercivity supplies a nonzero global minimizer. At every global minimizer its radius r_t obeys F_t<=F_t(0)=0, hence r_t<=(t/c)^2. All global minimizers therefore tend to zero as t decreases to zero, despite the fixed cubic term. For each nonzero radius the minimizing angles are 0,2*pi/3,4*pi/3.

This is a counterexample to the bare invariant-cubic criterion, not a lattice Potts realization and not a counterexample to C0048. The missing premise is a uniform Taylor/Legendre remainder: r^(5/2) is not O(r^4) at zero and dominates the cubic near zero.

The valid conditional contradiction is short. Suppose a constrained potential satisfies F_t(m)-F_t(0)=a_t*m^2-b_t*m^3+R_t(m) on a fixed interval [0,r_0], b_t>=b_0>0, |R_t(m)|<=K*m^4, and a_t ->0. Fix 0<m_0<=r_0 with K*m_0<=b_0/4. For all sufficiently small t, a_t<=b_0*m_0/4, and F_t(m_0)-F_t(0)<=-b_0*m_0^3/2<0. Thus these hypotheses contradict 0 being a global minimizer. If this is used for the Legendre transform of a symmetric pressure, its nonnegativity relative to I(0) makes the contradiction explicit. Establishing the uniform cubic ratio and remainder in the actual nearest-neighbor critical model, especially q=3,d=3, is the still-unproved input.
