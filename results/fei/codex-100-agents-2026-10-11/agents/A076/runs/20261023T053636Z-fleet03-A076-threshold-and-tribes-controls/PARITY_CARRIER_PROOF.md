# Small-influence noncharacter shared query from the original account

All logarithms are base2 unless ln is written. Inputs are independent uniform physical bits. Profiles may be arbitrarily correlated and biased. This is a continuation theorem with retained input and terminal entropy, not full FEI.

## 1. The first genuinely new carrier clause

Let d>=5 be odd, e=2^-d, and h(s)=+1 when |s|<d/2 and -1 otherwise, with bits encoded0,1. On a disjoint private cube take any Boolean V,W, and replace h(0),h(e1), both originally+1, by V,W. Put mu=EV,nu=EW, A=1-mu,C=1-nu, and m(s)=E_private F(s,private). Then

    mhat(S)=hhat(S)-e[A+(-1)^(1 in S) C].            (1)

The remaining exact spectrum is Fhat(S,T)=e[Vhat(T)+(-1)^(1 in S)What(T)] for every NONEMPTY private label T. The carrier coefficients hhat are the usual symmetric threshold Krawtchouk sums retained in A076-STRUCTURED-SPECTRA@8; odd parity follows directly by global complementation, without an asymptotic approximation.

Since h is odd under global bit complementation, hhat(S)=0 at every even cardinality. For d>=2, orthogonality of the two distinct adjacent point characters on this parity half gives EXACTLY

    Q=sum_(|S| even) mhat(S)^2=e(A^2+C^2)/2<=4e.    (2)

No normalized Boolean source is attributed to m. It has total squared mass M=E m^2=1-e[Var V+Var W]<=1. At any shared query j, each paired row contains one even and one odd label. Concavity and homogeneity of Phi(p,q)=(p+q)h2(q/(p+q)) yield

    B_j(m)<=Phi(Q,M-Q)<=Phi(Q,1-Q)=h2(Q).           (3)

The second inequality follows by increasing the second argument; the missing mass is nonnegative. Because Q<=4e<=1/8, h2(Q)<=h2(4e)<=4e log2(Euler/(4e))<4de. Here h2(q)<=q log2(Euler/q) follows from -(1-q)ln(1-q)<=q, and ln2>=2/3 implies log2(Euler)<=3/2<2. All zero masses are included by continuity. Thus the entire empty-private erasure, including the old empty Fourier row, is paid by a small parity leakage, not by assuming a balanced profile or a zero mask.

## 2. Actual influence pays that leakage uniformly in d

Let alpha_d=2^(-(d-1))*binom(d-1,(d-1)/2). Every carrier coordinate has actual influence alpha_d. For d>=5, BOTH edited points and all their neighbors other than the edge joining them lie in the +1 region. Therefore none of the original pivotal carrier edges is removed. Direct physical edge counting gives

    Inf_1(F)=alpha_d+2e Pr(V!=W),
    Inf_j(F)=alpha_d+e(2-mu-nu), j!=1.              (4)

In particular alpha_d<=Inf_j(F)<=alpha_d+4e. To compare (3) with (4), if d=5 then4de=5/8<=2alpha_5=3/4. For odd d>=7 the central binomial term is the largest among d terms summing to1, so alpha_d>=1/d. The sequence4d^2/2^d decreases on odd d>=3, since its successive ratio is(d+2)^2/(4d^2)<1. At d7 it equals49/32<2. Hence for every odd d>=5,

    B_j(m)<=2Inf_j(F).                              (5)

This is not a fixed positive influence floor: alpha_(d+2)=d alpha_d/(d+1), and the divergent sum of1/(d+1) proves alpha_d tends to0. Equation(4) therefore gives arbitrarily small actual query influence.

The restricted carrier children are the two even-dimensional central thresholds. Each has a nonempty proper set of pivotal edges and a nonzero mean of opposite sign, so neither is a signed character. For d>=5 the actual edited children also cannot become characters: at the positive-mean cofactor the mean can decrease by at most8e, while alpha_d>8e; the negative-mean cofactor only decreases. Their unedited positive and negative vertices persist. At d5, alpha_5=3/8>1/4=8e; for d>=7, alpha_d>=1/d>8/2^d. These arguments apply conditionally at every private descendant, including after exposing a common guard.

## 3. Full erasure and the SAME inherited reserve

Retain

    U=e[H(V)+H(W)], R=de[Var V+Var W],
    Xi=e sum_(T nonempty) ([g(v_T+w_T)+g(v_T-w_T)]/2-g(v_T)-g(w_T)),
    g(t)=-t^2 log2(t^2), -4e<=Xi<=0.               (6)

Partition complete erasure fibers by the private label. The empty sector is exactly(3). Every nonempty-private fiber has Phi<=sum of its two masses; their total mass is e[Var V+Var W]. This is EXACTLY the inherited release_R at a shared query, including separator and event-death children. Thus using the two-point channel bound JS_j<=2Inf_j/ln2<3Inf_j,

    Delta_shared H(F)<=release_R+5Inf_j(F).         (7)

At zero influence the non-strict inequality is understood directly. Both actual full child entropies are included in Delta. U is harmonic at this query. No noncharacter cofactor is replaced by a certified constant, literal or a new entropy budget. Equation(7) closes the small-influence noncharacter handoff left open by A078 v2, at the original odd-majority carrier query. It does NOT prove a second shared query after the carrier has become biased.

## 4. Arbitrary private prefix, one shared handoff, arbitrary private suffix

Allow EVERY finite adaptive tree with at most one shared query per path, arbitrary private queries before and after it, and arbitrary stopping. The chosen shared coordinate may depend on the private history. After that shared query retain the actual threshold cofactor, including the generally nonconstant sibling where both edited events died.

The arbitrary-carrier private theorem reconstructed in A078 v2 section1 is applicable at every private node: Delta H<=Delta U+release_R+12Inf_private+Delta Xi in the two-point phase, price11 is available in the one-point phase. Its proof is the same finite mean-row curvature argument as A076 v8 section1; no profile-mean or carrier-balance hypothesis is required. At a pure carrier sibling private influence and decrement are zero.

At the original continuation state o, after ALL old debits, let unused donor B>=4e_o, and chi_o=Xi_o/e_o. Use the SAME account

    K_v=e_v[B/e_o-chi_o]+Xi_v                       (8)

until separation. Private changes are signed: Delta Xi=K_parent-E K_child. A nonseparating shared query doubles e,Xi on its event-surviving child, sets K=0 on the event-dead carrier sibling, and hence preserves the average K. Its actual NONCONSTANT carrier entropy remains at that sibling. A separator freezes K_parent in BOTH children and all later descendants, even constant ones. In the one-point phase Xi=0 and K is frozen. All reaches are original physical probabilities. The inherited event mass, frozen at separation, is a martingale, giving

    E K_leaf>=B-4e_o.                              (9)

Finite telescoping of the exact private account and(7) gives

 H(F_o)-E H(F_leaf)+E(R_leaf+K_leaf)
    <=U_o-E U_leaf+R_o+B+12P_private+5P_shared.     (10)

Every full inherited core entropy and both actual wrapper children remain. No new source admission occurs after the shared query. This is the unchanged maximum continuation price12, not a dimension-independent FEI proof.

## 5. Original donor, first debit, old debit, and early guard

Use the original source V=y*b_k(z), k>=4 even, W=y[1-2 point(z=0,x1=...=xm=0)], m>=2. The same original C5 allocation splits ONCE as5e_o I(V)=e_o H(V)+S, S=e_o(3k/2+5), since H(V)=k,I(V)=k/2+1. Preserve FIRST4e_o and another old debit D0>=0. After both x1 answers take B=S-D0-4e_o. If D0<=S-8e_o, (9)-(10) retain E K>=S-D0-8e_o. At k4,D0=e_o the expected remainder is2e_o. No descendant bent certificate is renewed even when y,z are queried early. The original allocation e_o H(V), its surplus S, actual transaction allowances and all old debits are kept distinct.

## 6. Exact first unsupported line

The parity certificate(2)-(3) requires an odd carrier, and(5) requires its actual influence to dominate the point leakage. After a first shared query the even-dimensional biased majority cofactor has both Fourier parities, so(2) is not a certificate for its next query. The shortest next target is that SECOND genuine shared exposure on the already paid cofactor, with the same diminished account and both complete terminals. Arbitrary odd carriers with influence comparable to point mass, unrestricted original donor eligibility, arbitrary input/terminal FEI certificates and prescribed-reference conversion also remain unpaid. Full FEI remains OPEN. This new analytic clause awaits independent review; finite certificates alone do not prove all d or all private dimensions.
