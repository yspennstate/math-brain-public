# Rate-continuum obstruction to sequential local-hull admission

All cubes are uniform, entropy is in bits, functions are sign-valued. The allocator matters: at each physical query under the CURRENT admitted coordinate set M, it uses the local stopping hull rho_M to allocate credit

    a_b=a+rho_M(v_b)-mean rho_M(v_children).

Admissions keep credit unchanged. Required solvency includes every positive-probability arrival and every stopping decision. The result below refutes a shortcut for THIS allocator; it does not refute an influence-paid coherent envelope or FEI.

## 1. Generic guard-and-parity construction

Let f on n bits have A_K=H(f)-K I(f)>0. Put

    U_d(s,x)= f(x) when s=0^d, and +1 otherwise,
    G_d(s,x,z)=chi_r(z) U_d(s,x),
    delta=2^-d, mu=E f, a=1-mu, v=1-mu^2.

The selector, seed and parity coordinates are mutually disjoint. These are actual Boolean truth-table definitions for every d. No arbitrary probability spectrum is substituted for a Boolean function.

The integer character expansion of the selector indicator gives the EXACT normalized Walsh coefficients of U_d:

    hat U(empty,empty)=1-delta a;
    hat U(A,empty)=-delta a for nonempty selector A;
    hat U(A,B)=delta hat f(B) for every selector A and nonempty seed B.

The second row has multiplicity 2^d-1, and each nonempty B in the third has multiplicity 2^d. Their inverse is 1+1_{s=0}(f-1). Their squared sum is

    (1-delta a)^2+(delta-delta^2)a^2+delta v=1.

Thus these are the actual spectra, including constant/empty atoms. Exact physical edge counting gives

    I(U_d)=delta[I(f)+d a],  I(G_d)=r+I(U_d),
    H(G_d)=H(U_d).

Multiplication by disjoint parity merely shifts Fourier indices. It changes no squared coefficient or entropy and adds exactly r to influence, at every selector-only restriction.

With eta(t)=-t log2(t), eta(0)=0, the complete entropy formula is

    H(U_d)=eta((1-delta a)^2)
       +(delta-delta^2)[eta(a^2)+2d a^2]
       +delta[H(f)-eta(mu^2)+2d v].                 (1)

The formula also handles a=0, mu=0 and d=0 by the stated convention; coefficients with zero multiplicity are omitted before evaluation.

## 2. Analytic bias faces and uniform bounds

For 0<delta<=1/4, replace d in(1) by log2(1/delta). This defines a continuous auxiliary entropy profile. Its positive weighted multiplicities are 1,1/delta-1 and1/delta per nonempty seed coefficient. The sum of multiplicities is 2^n/delta; all individual squared coefficients lie in[0,1]. Their weighted probabilities sum1 by the identity above, even for nondyadic delta. Weighted log-sum therefore bounds the entropy of all atoms except the main one by their mass times the logarithm of their effective count divided by that mass. This is an analytic auxiliary profile; actual uniform Boolean guards use only dyadic delta.

Let w=1-(1-delta a)^2<=4delta. Separating the main atom and using log-sum gives

    H_delta<=h2(w)+w log2(2^n/delta-1)
           <=1+4delta[n+log2(1/delta)]<=n+3.        (2)

The last step uses delta<=1/4 and delta log2(1/delta)<=1/2, proved by differentiation since ln2>1/2. Physical d=0,1 separately satisfy H(U_d)<=n+d<=n+1 by their finite spectral support. Thus H(U_d)<=n+3 for EVERY integer d>=0; there is no grid gap.

For delta<=1/8, w<=1/2 and h2 is increasing there. The elementary inequality -(1-t)ln(1-t)<=t and 1/ln2<2 imply

    H_delta<=4delta[n+2log2(1/delta)+2].            (3)

At delta=0 set H_0=0. Formula(3), or t log(1/t)->0, proves continuity and its exact zero boundary. At the physical d=0 face use the seed formula, not a rare-bias approximation. The formal weight profile is never claimed to be a Boolean spectrum at nondyadic delta.

## 3. Vanishing global hull versus nonvanishing local-admission capital

For K>=0 define R_K as the full physical stopping hull with payoff (H-KI)_+. Fourier entropy is nonnegative and superharmonic under physical restrictions: write u_T=hat f(T), v_T=hat f(T+i). The parent splits mass M_T=u_T^2+v_T^2 into u_T^2,v_T^2, while the two child spectra have masses(u_T+v_T)^2 and(u_T-v_T)^2 and mixture M. Shannon's chain rule gives

    H(parent)-mean H(children)
      =sum_T M_T h2(u_T^2/M_T)+JS(child spectra)>=0.

Zero-M terms vanish. Therefore H dominates every stopping payoff and every conditional mean, so finite Bellman induction yields R_K(G_d)<=H(G_d)=H(U_d). Also R_K(G_d)>=delta A_K>0: reveal all selectors, then all parity coordinates, and stop at the seed on the all-zero selector branch; other branches are pure parity with zero entropy and nonnegative slack.

Fix a rate interval 0<kappa<=K<=Lambda, and choose integer r with kappa r>=n+3. At ANY selector-only history the full function is either pure parity or chi_r U_t with some t remaining. From(2), K I-H>=kappa r-(n+3)>=0. Every selector-only local stopping hull is therefore EXACTLY0. All its query increments are0, whatever adaptive selector admissions and order are used. Actual inherited credit does not change on the all-zero selector path.

At the end of that path admit the remaining seed and parity coordinates and reveal parity. Each parity outcome is +f or -f and has stop deficit A_K. No conserved-credit allocation with incoming credit<A_K can cover both sign-equivalent children and then stop; mean conservation forbids it. Hence the exact robust local-admission capital T_K(G_d) is at least A_K, independently of d. This argument preserves actual past allocations and needs no fresh outside transfer. Equivalently, the full hull of chi_r f equals R_K(f): tensor subadditivity gives the upper bound and revealing parity first gives the lower bound.

Consequently, whenever A_K has a uniform positive floor over a compact rate interval,

    0<R_K(G_d)<=4*2^-d[n+2d+2] ->0,
    T_K(G_d)>=A_K>0                              (d>=3). (4)

No constant-factor enlargement of a global hull automatically funds all sequential local-hull admissions. This differs from choosing the full-universe hull allocator from the start, which would be coherent but whose initial influence price remains unpaid.

## 4. Certified rate4 interval and actual Boolean family

Use the complete24-bit seed f=J(-1,+1,g,g,g,g), with g negative exactly on{0,1,2} in six bits, h negative on{0,1,2,4,8,16,32,6,17,40}, and J(x)=-h(x xor1). Bit1 means sign-1. The earlier exact source and this run's independently grouped coefficient calculation certify

    A_4=H(f)-4I(f)>7/256,  I(f)<=24.

For EVERY REAL K in the CLOSED interval[4,4097/1024],

    A_K=A_4-(K-4)I(f)>7/256-24/1024=1/256.        (5)

There is no rate sampling in this implication: it is an affine exact endpoint bound. Take r=7, so K r>=28>24+3. The actual family G_d on d+31 physical bits then obeys(4) UNIFORMLY throughout this entire real rate interval. In particular

    T_K(G_d)/R_K(G_d)
       >2^d/[1024(26+2d)] ->infinity.

The seed spectrum is checked again using literal core Walsh coefficient multiplicities and the ordinary outer-character expansion, then compared exactly with the previous independent centered-occupied-sector engine. No24-bit truth array or all-d numerical extrapolation is used.

### Widened certified compact region

The independent seed calculation gives the sharper EXACT influence I(f)=98637/524288. Using that value, rather than I<=24, the endpoint cross-multiplication in RATE_EXTENSION.json certifies

    A_4-I(f)/8>1/256.

Therefore ALL conclusions above extend to the entire CLOSED REAL interval[4,33/8]. This widens the initial conservative[4,4097/1024] certificate by replacing its rough influence bound with the exact same seed's influence; it does not change the seed, accounting convention, or query model. The same r=7 works since the lower endpoint is still4. EXTENSION_SPEC.json froze this single endpoint check before it ran; no rate grid is used.

## 4a. Admission amplification is already equivalent to fixed-rate FEI

Fix ANY real K>0. For a Boolean f let T_K(f) be robust capital starting with no admitted coordinates and allowing every subsequent singleton admission, physical query and stop under the prescribed current-local-hull allocator. Then the following are equivalent:

1. H(f)<=K I(f) for EVERY finite-dimensional uniform Boolean f.
2. There is a finite dimension-independent L>=0 such that T_K(f)<=L R_K(f) for EVERY such f.

If1 holds, it holds at every restriction; every payoff, local hull, increment and robust capital is0, so2 holds. If1 fails, choose its actual finite Boolean witness f with A_K>0. Choose integer r>= (n+3)/K and form the explicit guarded-parity family from Section1. Equations(2)-(4) give R_K(G_d)>0 tending0 and T_K(G_d)>=A_K>0. Hence2 fails for EVERY finite L. The construction uses only Boolean functions and exact physical guards. It includes arbitrary real fixed K>0; K=0 is excluded because the positive parity payment used here is then unavailable. This is a reduction identifying the circularity of a proposed admission shortcut, not a proof of either equivalent universal assertion.

## 5. Initial credits, old labels, and the zero-reach boundary

At any finite DAG, the exact capital for the prescribed local allocator is the maximum over arrival paths of stop deficit minus cumulative allocated-credit increments. This follows by induction over queries and admissions. Equivalently T(v,M) is the maximum of current stop deficit, allowed-admission T values, and T(child,M)-delta_child over BOTH query outcomes. The child maximum is unweighted because actual positive-probability arrivals must each remain solvent. This reconstructs the generic part of A072's rate1 obstruction independently.

Supplying any extra real initial credit b shifts every later actual credit by exactly b, since each local update has coefficient1 on its incoming credit. Thus the sharp requirement covers its entire real half-line including equality; the counterexample takes ANY supplied credit less than A_K, for example L R_K(G_d) for large enough d and any fixed L. Solvent old signed debit labels and nonnegative credit-owner labels can be retained by the conditional kernels in the previous proof; no outside owner, spent donor, parked reserve or sibling terminal is discarded. The obstruction persists even with one owner, so introducing more labels cannot repair it for free.

For every finite d the bad selector path has strictly positive reach2^-d and cannot be erased. At the literal delta=0 boundary it is unreachable: the function is just parity, both hull and robust capital are0. The robust all-arrival requirement can jump at this zero-reach face even though entropy and the global hull tend to0. Extending the positive-capital bound to delta=0 would be false; the analytic boundary is handled separately.

## 6. Hardest audit and first unpaid universal line

Attack the construction by checking whether an intermediate selector restriction can acquire a negative slack and thereby preallocate credit down the rare path. The uniform bound(2), r=7 and the closed rate interval rule this out with a full bit of positive slack. Check separately that parity can really be revealed after admission without altering the seed deficit, and that the rare branch is positive-reach for each finite d. Exact toy augmented-DAG calculations audit this mechanism rather than only the seed entropy.

This is a genuine Boolean counterfamily to a proposed ACCOUNTING implication at rate4 and a real interval above4. Ordinary H/I(G_d) tends0 because H tends0 while I tends7. It is NOT a disproof of FEI. It neither weakens A080/A071's separately verified four-core fixture nor supplies a dimension-independent influence-paid initial envelope. The next unpaid line is to construct and pay a coherent full-universe envelope, or a policy with explicitly priced admission deficits, from the original unused influence resource while retaining all old owners and complete terminals.
