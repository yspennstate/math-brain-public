# Universal FEI disproof standard — A080, version 1

Throughout, f is an actual sign-valued function on a finite uniform cube, a_S=E[f chi_S], p_S=a_S^2, H=-sum p_S log2 p_S and I=sum |S|p_S. The atom at the empty set is included. Constants have H=I=0 and do not have a defined ratio. Full FEI remains OPEN.

## Acceptance endpoint

A disproof must exhibit a specified sequence f_m:{-1,1}^{n_m}->{-1,1}, with finite n_m and I(f_m)>0, and prove H(f_m)/I(f_m) tends to infinity. An unbounded subsequence suffices after reindexing: for every integer k choose a certified f with H>kI. Equivalently one needs a constructive family and bounds H>=L_m, 0<I<=U_m with L_m/U_m tending to infinity. A finite maximum rho, even exceeding every previously proposed numerical constant, proves only C_FEI>=rho. A bounded limiting ratio proves only that constant lower bound. No threshold such as 4, 6.45 or 100 defines FEI.

For a spectrum supplied without a truth formula, certify real signs a_S, sum a_S^2=1 and sum_S a_S a_(S xor U)=0 for every U!=empty. These identities are precisely the Fourier expansion of f^2=1; inverse Walsh then gives actual sign values. A probability law, random real amplitudes, or separately satisfiable pairwise phase tests are insufficient. A random construction must establish existence of actual finite sign functions and the simultaneous required entropy/influence bounds.

An exact finite certificate consists of a Boolean definition or truth table, integer Walsh coefficients w_S (a_S=w_S/2^n), exact rational Parseval and influence, and rigorously enclosed logarithms. Prove any infinite-parameter transition separately, with an error small relative to I; absolute o(1) errors alone fail when I tends to zero. Floating calculations may locate a candidate but cannot certify the endpoint.

## Tensor, spectator and additive-error tests

For disjoint blocks f(x)g(y), a_(S,T)=a_S(f)a_T(g). Thus p is the product law, H(fg)=H(f)+H(g) and I(fg)=I(f)+I(g). When both influences are positive the ratio is the influence-weighted average of their ratios. A tensor power f^{otimes t} has H=tH(f), I=tI(f) and exactly the same ratio. Tensoring alone does not turn a finite ratio into a disproof.

It does remove fixed additive errors. If every Boolean f obeys H(f)<=CI(f)+A for dimension-independent finite A, apply the inequality to f^{otimes t}, divide by t and let t increase. This gives H(f)<=CI(f). The same holds for an error r(t)=o(t) on these powers; an error proportional to dimension cannot be discarded this way without further estimates.

For F=f(x)g(y) and the proper physical block A=vars(f), H(S_A|S_Ac)=H(f), I_A(F)=I(f), and fixing any spectator assignment leaves a sign multiple of f. Hence H(F)-E_y H(F_y)=H(g) for block vars(g), while the decrement for block A is H(f). The physical-channel mutual information for block A is zero. A proposed universal proper-block bound with constant K must therefore satisfy K>=H(f)/I(f) for every f. Taking a nonconstant spectator makes the block proper. Spectator tensoring embeds the entire optimal FEI constant into a proper-block bound; an isolated lower bound K>=4 is weaker than certified literature bounds.

Balancing by a fresh sign z gives b(x,z)=zf(x), H(b)=H(f), I(b)=I(f)+1. Use z f^{otimes t} to make the additive one negligible. Thus restricting to balanced inputs preserves the supremum C_FEI, though it does not preserve each individual ratio exactly.

## Normalization audit

Natural-log entropy is H_nat=(ln2)H_bits; this fixed factor preserves divergence. With sign convention changes, input permutations and sign flips merely alter Fourier signs or labels and preserve H,I. For b=(1-f)/2, its nonempty coefficients are -a_S/2: the nonempty squared mass is Var(f)/4, not 1. The normalized nonempty law agrees with the sign function's nonempty conditional law, but its entropy alone is not H(f).

Writing v=Var(f)=1-a_empty^2, H(f)=h2(v)+v H(S|S!=empty) and I(f)=v E[|S| | S!=empty]. Therefore H(S|S!=empty)/I(f) is the wrong ratio; conditioning can introduce a factor 1/v. Entropy of the pivotal-set law, size law, or spectral marginals is also a different quantity. The percolation papers compare these laws in specified geometric regimes; singularity of the laws supplies no FEI disproof.

Multiplication by a character preserves H but can change I: I(f chi_A)=sum_(i notin A) Inf_i+sum_(i in A)(1-Inf_i). Its minimum over A is J=sum_i min(Inf_i,1-Inf_i). Therefore universal H<=CI and H<=CJ are equivalent by character centering, but a candidate transformed family must report its new physical I. A general invertible linear coding is not an isometry of total influence.

## Rare activation: exact C013 and the required growth rate

For balanced Boolean g, let A_r indicate one point on r>=1 fresh controls, p=2^-r, F=1+A_r(g-1). This is Boolean; P(F=-1)=p/2. For nonempty data index T and any control index U, a_(T,U)=p sigma_U a_T(g). Empty data with nonempty U has coefficient -p sigma_U; the constant coefficient is 1-p. Hence

H(F)=pH(g)+2rp(2-p)+(1-p)^2 log2(1/(1-p)^2),
I(F)=p(I(g)+r).

The nonempty-data entropy is pH(g)+2rp; the control-only entropy is 2rp(1-p). Each control influence is p and each data influence is scaled by p. These derivations include all atoms and all physical coordinates.

For any seed f with I(f)>0 choose g_t=z f^{otimes t} and r_t=ceil(2 log2(t+1)). Then H(g_t)=tH(f), I(g_t)=tI(f)+1, I(F_t)<= (tI(f)+1+r_t)/(t+1)^2 tends to zero and P(F_t=-1) tends to zero. Divide H(F_t) and I(F_t) by p_t t. Since r_t/t tends to zero and

0 <= (1-p)^2 log2(1/(1-p)^2)/p <= 2/ln2,

the ratios converge to H(f)/I(f). This proves C013: for every epsilon,delta>0, the supremum on these activations with 0<I<=epsilon and P(F=-1)<=delta equals C_FEI, including an infinite supremum.

For a putative unbounded-ratio seed sequence f_m, choose tensor counts t_m with (1+r_m)/(t_m I(f_m)) tending to zero, and choose r_m large enough that p_m(t_m I(f_m)+1+r_m) tends to zero. An explicit choice is to first fix m and choose t until the foregoing fixed-seed activation approximates its ratio within 1/m and both rarity bounds are below 1/m. All tests can be certified from the exact displayed formulas. Arbitrarily choosing huge r without compensating t can destroy seed growth: the denominator contains r and the activation overhead may dominate. Rarity itself is not a disproof mechanism.

## Retained-KL tree payment is FEI-strength

At a node querying physical coordinate i pair the parent's coefficients u_T=a_T, v_T=a_(T+i), set q_T=u_T^2+v_T^2 and m_T=min(u_T^2,v_T^2), and define Q_i=sum_T m_T log2(q_T/m_T), with zero terms zero. This is the minority-mass version of the retained-KL charge, not the unsigned child-difference mass without orienting each packet.

B_i=sum_T q_T h2(m_T/q_T). The omitted part is exactly sum_T (q_T-m_T)log2(q_T/(q_T-m_T)), which lies between zero and sum_T m_T/ln2, since ln(1+x)<=x. Because sum m_T<=Inf_i,

Q_i<=B_i<=Q_i+Inf_i/ln2.

C005 supplies Delta_i H=B_i+JS_i and JS_i<=2 Inf_i/ln2. For completeness its scalar argument sets z=2uv/(u^2+v^2): d(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2 <=1-sqrt(1-z^2), proved by integrating atanh z<=z/sqrt(1-z^2). Thus the JS contribution is at most 2min(u^2,v^2)/ln2.

In every actual stopping restriction tree, w_v is the probability of reaching node v. Influence and entropy telescope:

I_queried=sum_v w_v Inf_(i_v)(f_v)=I(f)-E I(f_leaf),
DeltaH=sum_v w_v Delta_(i_v)H(f_v)=H(f)-E H(f_leaf).

Summing gives, for every such tree and arbitrary Boolean leaves,

sum_v w_v Q_v+E H(f_leaf) <= H(f)
 <= sum_v w_v Q_v+E H(f_leaf)+(3/ln2)I_queried.

For a complete tree the terminal terms vanish. Consequently H/I and the complete-tree Q/I differ by at most 3/ln2. A sequence with Q/I tending to infinity is an FEI disproof, and a uniformly bounded-H/I family cannot refute a complete-tree retained-KL payment. Changing complete tree order cannot change Q by more than (3/ln2)I. For stopping trees, terminal entropy must remain in the endpoint. A divergent upper surrogate, such as Lambda_T in LOG_ALLOCATION equation (8), does not imply divergent Q or H. It may refute that surrogate or the chosen tree policy.

## Balanced recursive composition: genuine amplification, finite ceiling

For a balanced gate g with a=I(g)>1, b=H(g), define f_0=one literal and f_(d+1)=g(f_d^{(1)},...,f_d^{(k)}) on independent blocks. Balance ensures every inner spectrum is supported on nonempty sets. An outer Fourier set identifies exactly which blocks are occupied, so there is no collision. Thus I_(d+1)=a I_d and H_(d+1)=b+a H_d. Solving gives I_d=a^d, H_d=b(a^d-1)/(a-1), and H_d/I_d=[b/(a-1)](1-a^-d). This converges to a finite constant for any fixed gate. Unlike a tensor power it can improve a ratio, but it cannot disprove FEI by itself. A sequence of gates with unbounded b/(a-1), together with depth and finite-gate certificates, would be a valid mechanism. Establishing such gates is the first unpaid line; their existence is not inferred from fixed-gate amplification.

## Literature reproduction and provenance limits

Primary sources: [OWZ, ICALP 2011](https://www.cs.cmu.edu/afs/cs/Web/People/jswright/papers/fei.pdf), Section 1; [O'Donnell–Tan, ICALP 2013](https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf), Section 5; [Hod, arXiv:1711.00762](https://arxiv.org/pdf/1711.00762), Sections 1.2, 2.4, 4.1 and Appendix A.4.

OWZ states the bound 60/13 but supplies no formula for its asserted explicit family in the consulted paper. Reconstruction of that particular historical family is therefore NOT CLOSED; the missing source is recorded instead of inventing an attribution. The later O'Donnell–Tan paper attributes 60/13 to OWZ and proves the 6.278 bound. Hod explicitly corrects the six-bit seed issue. The transcription of O'Donnell–Tan's printed seed has repeated clauses and implies a biased function; do not use it as a balanced seed without checking.

Hod's corrected balanced seed is

g3=(x1 OR x2) AND (x3 OR x4) AND (x1 OR x3 OR x5) AND (x3 OR x5 OR x6).

The signs true=-1,false=+1 do not affect squared spectra. Integer Walsh evaluation, Parseval, pivotal-edge influence, and an independent direct character sum certify balance, I=13/8 and H/(I-1)>6.278944. More generally, g_m=(x1 OR x2) AND [x3 OR (x4 AND (x5 OR (... (x_(2m) AND x1))))]. The frozen checks cover m=2..6 and Hod's modified six/eight-bit clauses. They certify constant lower bounds, recorded as exact rational intervals in out/CERTIFICATES.json. The m=2 seed has H=3,I=3/2 and recursive composition at depth 4 already has ratio 130/27>60/13; this independently validates a stronger lower bound, but is not a reconstruction of OWZ's historical construction.

For Hod's strongest construction put q0=1/2, q_(m+1)=1/(1+q_m), pi0=1, pi_m=product_(j=1)^m q_j. Let R0=0 and

R_(m+1)=R_m+h2(q_m)pi_m/(1-q_m).

Here R_m is H^+(F_m)/I^+(F_m), with H^+=H(S|S!=empty) and I^+=I/Var, not the corrected unnormalized H-plus convention used elsewhere. Hod's disjoint AND/dual limit construction gives these identities. The actual H/I additionally contains h2(Var)/I>=0. Since q_m lies in [1/2,2/3], pi_(m+j)<=pi_m(2/3)^j and the positive series tail beyond R_m is at most 9pi_m. Rational atanh logarithm bounds at m=48 certify

6.4547837159 < R48 <= beta(1/2) < 6.4547837169 < 6.454784.

Thus the rigorous claim is C_FEI>6.4547837; the abstract's display '>6.454784' is too strong at six decimals for this specific construction. No claim about the best current literature bound is made.

The finite-formula implementation replaces each implicit fixed-point step by K0(lambda)=lambda and K_(j+1)(lambda)=dual(lambda AND K_j(lambda)), each occurrence using disjoint copies. Here dual(h)(x)=-h(-x), with every input sign negated. Fresh copies rename all input coordinates disjointly. With a fixed L, F_(0,L)=one literal and F_(m+1,L)=K_L(F_(m,L)) are actual finite monotone Boolean formulas on (L+1)^m coordinates: K_L uses L+1 independent copies of its source. Their scalar triples (p,I,H) use the exact disjoint conjunction identities

p_out=pq, I_out=q I1+p I2,
H_out=q[H1-h2(4p(1-p))]+p[H2-h2(4q(1-q))]
       +h2(4pq(1-pq))+4pq[h2(p)+h2(q)-h2(pq)].

Duality sends p to 1-p and preserves H,I. These identities follow by expanding sign-valued conjunction (1+f+g-fg)/2 for true=-1: nonempty/nonempty coefficients multiply by -1/2, one-block coefficients multiply by the other true probability, and the empty coefficient is 1-2pq. This accounts for all sectors without assuming zero means.

For each fixed m the finite triples converge to Hod's limit triples as L increases. For p bounded away from 0 and 1, the bias iteration q_(j+1)=1-pq_j contracts geometrically; influence is an affine iteration of slope p; entropy is an affine iteration of slope p with a continuous forcing term depending on q_j. The convergence is uniform on compact sets of source triples. Induction in fixed m proves convergence despite the increasing number of physical bits. This supplies the finite-to-limit bridge, rather than treating an infinite function as a finite Boolean witness. The separate finite_hod checker tests the explicitly frozen L=80,m=48 formula directly by scalar interval propagation; its status and output are recorded in REPORT.md. Its 81^48-bit size is symbolic; only 3840 scalar gate recurrences are computed, not a truth table.

## Reproducible interval arithmetic

For rational y in [1,2], set z=(y-1)/(y+1). The positive atanh series has

ln y=2 sum_(j=0)^(K-1) z^(2j+1)/(2j+1)+tail,
0<=tail<=2 z^(2K+1)/[(2K+1)(1-z^2)].

Range-reduce every positive x=2^k y and enclose log2 x=k+ln y/ln2 using positive denominator bounds. Outward dyadic rounding prevents huge rational strings without weakening enclosure. Entropy uses exact masses and positive log weights. For probability intervals, binary entropy's minimum is at an endpoint and its maximum is at 1/2 if included, otherwise an endpoint. The finite formula checker also handles the quadratic 4p(1-p) by its endpoint minima and possible internal maximum. Floating decimal displays are convenience only; all decisive comparisons use rational endpoints.

Review requested from A092 and A088: independently reconstruct the Boolean gate definition, the physical influence ledger, scalar conjunction entropy, retained-KL minority convention, and rational-log tail. No independent acceptance, formal kernel check, mirror save or historical OWZ-family reconstruction is claimed by this artifact.
