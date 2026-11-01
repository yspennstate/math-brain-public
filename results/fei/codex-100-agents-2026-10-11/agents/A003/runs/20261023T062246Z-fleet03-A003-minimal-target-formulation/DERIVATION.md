# Reference-singleton discrepancy funds zero-singleton profile changes

Author proof, independent review pending. All information units are bits. Full FEI remains OPEN. This is a refinement of A096's supplied coherent-reference transaction, not a universally influence-priced source.

## 1. Exact setup and new energy

Let G=a+sigma*b*h be Boolean, sigma in {-1,1}, on disjoint finite uniform controller and seed cubes, with a in {-1,0,1}, b=1-a^2. Write A_U=ahat(U), B_U=bhat(U), beta=sum B_U^2. Supply a complete finite-cost seed reference R calibrated at R(0)=m^2, m=E h. The coherent full reference is

    Q(U,0)=(A_U+sigma*m*B_U)^2,
    Q(U,T)=B_U^2 R(T), T!=0.

All previously executed erasures, old source costs, off-branch terminal references and diminished original bank remain booked. The new argument changes only the local transaction after ONE physical seed query j. Set

The coherent reference is normalized: Parseval gives sum A^2=1-beta, sum AB=E(ab)=0 and sum B^2=beta; its full vacuum mass is1-beta+beta*m^2 and its tail mass is beta*(1-m^2). Every occupied parent atom has positive reference mass by the finite-source hypothesis. Zero reference-only atoms are permitted.

    d=hhat({j}), r=R({j}), delta=r-d^2,
    C=sum A_U^2 B_U^2, D=sum A_U B_U^3, E=sum B_U^4,
    Gamma=C-D^2/E if E>0, else Gamma=0.

Let

    F_m=sum B_U^2(sigma*A_U+m*B_U)^2 >=Gamma,
    x_exact=d^2(F_m+beta^2*m^2)+(delta^2/4)(E+beta^2),
    x=Gamma*d^2+(delta^2/4)(E+beta^2).                 (1)

Both are nonnegative. The new second term depends on the CURRENT reference singleton discrepancy, not on actual singleton energy alone. At d=0 and r>0, x>0 whenever beta>0, even for a seed with every singleton coefficient zero.

## 2. Coarse refund with both its fluctuation and mean terms

The actual child means are m_tau=m+tau*d. Let the coarse partition consist of individual controller-vacuum atoms (U,seed-empty) and one complete nonempty-seed tail. Denote the two actual coarse laws by v_tau and the COMMON inherited marginal coarse reference by q. Direct physical Fourier restriction gives

    v_tau(U)=(A_U+sigma*m_tau*B_U)^2,
    v_tau(tail)=beta*(1-m_tau^2),
    q(U)=(A_U+sigma*m*B_U)^2+B_U^2*r,
    q(tail)=beta*(1-m^2-r).

These are full normalized probabilities, including all reference-only mass. If bar_v=(v_++v_-)/2 and w=(v_+-v_-)/2, then

    bar_v(U)-q(U)=-delta*B_U^2,
    bar_v(tail)-q(tail)=beta*delta,
    w(U)=2d B_U(sigma*A_U+m B_U),
    w(tail)=-2beta*m*d.                               (2)

Therefore the EXACT Euclidean decomposition is

    mean_tau ||v_tau-q||_2^2
      = ||w||_2^2+||bar_v-q||_2^2
      =4d^2(F_m+beta^2*m^2)+delta^2(E+beta^2)
      =4x_exact >=4x.                                 (3)

Coherent child restoration is block calibration of the entire inherited reference. Its refund is k_tau=D_2(v_tau||q). Finite CE propagates under the physical marginal, so every occupied coarse atom has positive reference mass. Pinsker in bits gives k_tau>=||v_tau-q||_2^2/(2 ln2). Applying it separately to the two actual child laws and averaging (no independence assertion) yields

    mean k_tau >=2x_exact/ln2 >=2x/ln2.               (4)

This keeps the mean-offset term discarded by A096's phase-only lower bound. It is also the exact KL centroid decomposition mean D(v_tau||q)=JS(v_+,v_-)+D(bar_v||q), though no separate lower bound on its two KL terms is needed. At d=0 the JS term vanishes but the reference-discrepancy term can remain positive.

For completeness, the Pinsker bound used here needs no new campaign hypothesis: group indices where v>q and apply log-sum; binary KL in bits has second derivative1/[p(1-p)ln2]>=4/ln2 in its first argument and vanishes with zero derivative at p=q. Integrating gives2(p-q)^2/ln2, hence ||v-q||_1^2/(2ln2), which dominates the displayed Euclidean bound. Endpoints follow by limits. Likewise a block calibration multiplies each old atom in block k by v(k)/q(k), so its exact CE decrease is sum_k v(k)log2(v(k)/q(k)); zero actual blocks contribute zero, with complete normalization retained.

## 3. Fund an actual nonempty-profile change

After coherent child restoration, let M_tau be its CURRENT normalized nonempty seed profile and t_tau=beta*(1-m_tau^2) its actual wrapper tail mass. For any prescribed normalized target S_tau on the child's nonempty seed frequencies, set

    eps_tau=x/(t_tau+x),
    M_new_tau=(1-eps_tau)M_tau+eps_tau*S_tau,           (5)

when x>0,t_tau>0. At x=0 make no change. At t_tau=0 no tail is used and the full constant-seed coherent reference is retained. Preserve every actual signed vacuum atom and all B_U^2 factors. Old support stays positive wherever actual mass is positive. The signed tail bill satisfies

    z_tau=t_tau E_actual_tail log2(M_tau/M_new_tau)
         <=t_tau log2(1+x/t_tau)<=x/ln2.              (6)

Let rho be the ACTUAL conditional-occupancy KL refund for this query under the FULL parent reference. The complete local erasure/reference identity, coherent calibration and (4)-(6) give

Explicitly, in each frequency fiber of deleting j, rho is the marginal actual mass times the KL between its actual two-point occupancy and its reference two-point occupancy, summed over fibers. Averaging the two restricted squared Fourier laws equals the parent actual frequency marginal. Expanding CE therefore gives CE(P_G,Q)=B_j(G)+mean CE(P_child,M_j Q)+rho, with rho>=0. Thus the following identity retains BOTH physical children and every complete terminal cost.

    B_j(G)+mean CE(P_child,Q_new_child)-CE(P_G,Q)
       =-rho-mean k_tau+mean z_tau
       <=-rho-x/ln2<=0.                              (7)

Thus no additional ancestor reserve is spent. The same already admitted root rate and every old debit/full complementary terminal are preserved. Any finite adaptive sequence may repeat (7), recomputing r, m, d and the controller from the CURRENT reference and actual restriction, without renewing old credits. Physical controller steps can use paid coherent block restoration as in A079; if intermediate references cease to be coherent, restore the stated invariant before using (1). No unpriced change of nonempty profile is hidden in that restoration.

For the fixed A079/A096 four-bit controller, beta=3/8, C=3/512, D=3/256, E=21/512, Gamma=9/3584. Here

    x=(9/3584)d^2+(93/2048)(R({j})-d^2)^2.            (8)

The coefficient93/2048 is (21/512+9/64)/4, not an improved value of Gamma. A096's9/3584 remains unchanged.

## 4. Scope, sharp zero boundary and first unsupported line

If beta>0, the conservative energy x vanishes precisely when delta=0 and Gamma*d^2=0. In particular at a zero-singleton query d=0, it vanishes exactly when R({j})=0. Thus the zero-singleton sector left by the phase-only rule is narrowed to zero ACTUAL and REFERENCE singleton mass, plus any phase-degenerate controller sector. For references with positive singleton mass every nonconstant zero-singleton query admits a genuinely positive mixture strength in (5). There is no uniform lower bound on that strength: it can go to zero quadratically as reference singleton mass goes to zero.

The parity3/exact-source control R=P_h still has d=r=0 and receives NO free authorization for a prescribed positive reset. It is not refuted or bypassed. Likewise this theorem does not promise any fixed strength such as1/64 and does not construct an influence-priced source for arbitrary h. The first unsupported universal line remains useful quantitatively sufficient source/profile admission from physical influence at one original owner, especially zero-actual/zero-reference singleton sectors. Remaining positive ancestor surplus or other actual occupancy refunds must pay a prescribed conversion there. No full FEI theorem follows from arbitrarily small supplied-reference refreshes alone.
