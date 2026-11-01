# One logarithmic reserve for a whole point-selector block

Signs, uniform cubes, entropy in bits. G,H are arbitrary Boolean functions on the SAME data cube (dummy coordinates permitted). A_s is a fresh point indicator of width s>=1, alpha=2^-s, F=G+A_s(H-G). Define gamma=P(G!=H), I_S=2s alpha gamma, I_T=(1-alpha)I(G)+alpha I(H), H_T=(1-alpha)H(G)+alpha H(H), c=1/ln2. Query fresh point bits until failure or success, then STOP at the actual G or H. No data query and no terminal entropy is omitted. Failure leaves are disjoint physical histories, all carrying the same G, not independent copies.

If gamma=0, F=G=H and every prefix bill is zero. Assume gamma>0 below. Then

    I(F)=I_S+I_T.

At a live point query with j bits left, l=j-1, rho=2^-l, its physical reach is w=2^{-(s-j)}, d=rho gamma, and w d=2 alpha gamma. The branches G,H and unthinned gamma are unchanged at every live history.

## Exact sector ownership and cumulative erasure

Let Delta_T=(Hhat(T)-Ghat(T))/2, so sum Delta_T^2=gamma. Nonempty residual-selector rows have two equal parent masses, giving exact erasure 2(1-rho)d. Empty residual-selector rows have parent coefficients u_T=Ghat(T)+rho Delta_T and v_T=-rho Delta_T. Their derivative mass is M=rho^2 gamma; their total mass is at most one. With Psi(a,b)=(a+b)h2(b/(a+b)), use Psi(a,b)<=b log2(e(a+b)/b) and log-sum to get

    B_j <= 2(1-rho)d + rho^2 gamma log2(e/(rho^2 gamma)).       (1)

The logarithm bound is valid even when the baseline branches share every data coordinate; it is not a disjoint-support argument. The kernel inequality follows from -(1-t)ln(1-t)<=t. Zero rows are continuous endpoints. M<=1, so replacing the total row mass by one is legitimate.

Let E_B=sum_live w B_j. Sum (1) ONCE over the whole block. Since

    sum_{l=0}^{s-1}2^-l=2(1-alpha),
    sum_{l=0}^{s-1}l2^-l=2[1-(s+1)alpha],

the exact simplified bound is

    E_B <= 2(1-2alpha) I_S
         +4 alpha gamma(1-alpha)[log2(1/gamma)+c].             (2)

In particular the logarithm is paid with coefficient 4 alpha gamma(1-alpha), not I_S times log(1/gamma). Replacing gamma by d at every history, or restarting (2) after every bit, would destroy this calculation. For s=1 the first term vanishes and (2) is the usual h2(gamma) upper bound with its linear remainder.

## Boundary reserve and its physical coordinate owners

Let K=GH. The disagreement set has density gamma. Edge isoperimetry gives gamma log2(1/gamma)<=I(K)/2. One elementary proof: a set of m vertices spans <=m log2(m)/2 edges, by induction splitting its child sizes a<=b and bounding new internal edges by a; h2(a/(a+b))>=2a/(a+b) closes the induction. Its boundary then yields the normalized assertion. This remains valid for gamma>1/2 and at endpoints.

Define the whole-block reserve

    R=2 alpha(1-alpha) I(GH).

Combining with (2),

    E_B <= [2(1-2alpha)+2c(1-alpha)/s] I_S + R.               (3)

For EACH physical data coordinate i, Inf_i(GH)<=Inf_i(G)+Inf_i(H), since the product edge flips iff exactly one branch edge flips. Thus its reserve is at most

    R_i <= 2alpha * [(1-alpha)Inf_i(G)]
         +2(1-alpha) * [alpha Inf_i(H)].                     (4)

The bracketed quantities are the actual terminal coordinate capacities. Mark the indicated fractions once BEFORE querying the selector. Aggregate failure probability is 1-alpha, active terminal probability alpha; no individual failed history receives a fresh full G account. Debit only this block's R_i, delete the marked amounts before any further terminal work. Therefore R<=2 I_T. No reserve is renewed at a live descendant. There is no claim that this reserve can be issued again at each nested point-block ancestor without increasing the rate or proving replenishment.

## Full entropy and genuine minority/KL ledgers

Actual entropy decrement at a split is B+JS. JS<=2c d follows packetwise from [(1+x)ln(1+x)+(1-x)ln(1-x)]/2<=1-sqrt(1-x^2): derivative comparison is artanh(x)<=x/sqrt(1-x^2), with equality at zero; sum the squared-amplitude mismatch and bound it by signed mismatch 4d. Hence

    H(F)-H_T <= A_s I_S+R,
    A_s=2(1-2alpha)+2c+2c(1-alpha)/s <11/2.                 (5)

Here is an exact constant certificate. c<81/56 since ln2>2(1/3+1/81)=56/81. For s=1,2,3,4 substitute alpha=2^-s into A_s and use this rational upper c; each is <11/2. For s>=5, A_s<2+(12/5)c<11/2. Similarly

    b_s=2(1-2alpha)+2c(1-alpha)/s <5/2:                   (6)

check s=1..5 with c<81/56, and for s>=6 use b_s<2+c/3<5/2. These finite rational checks plus the stated all-s inequalities are proofs, not extrapolations from Fourier cases.

For genuine magnitude-minority debt m_T=(|a_T|-|b_T|)^2/4, mu=sum m_T, Q_T=(a_T^2+b_T^2)/2, Jminor=sum m_T log2(Q_T/m_T), one has Jminor<=B and mu<=d. Consequently, on the same physical prefix,

    H(F) < (11/2) I_S + R + H_T,
    J_tree + H_T <= (5/2) I_S + R + H_T,
    J_tree +3c sum w mu +H_T <7 I_S+R+H_T.               (7)

Strictness in the first/third displays applies when I_S>0; zero-cost equality is covered separately. If H(G)<=C_G I(G), H(H)<=C_H I(H), retain their individual rates in (4) to obtain

    H(F)<=max(11/2,C_G+2alpha,C_H+2(1-alpha)) I(F).

In particular certified branches with allowance C yield max(11/2,C+2), independently of width, disagreement, bias, and the amount of shared data. The actual boundary R can be smaller than the sum-bound capacity. An arbitrary-core FEI bound is NOT asserted.

## Explicit nontrivial terminal family and rare influence

Let G=z b_m, H=z b'_m, where b_m is ANY bent sign on even m>=4 bits, b'_m flips it at one vertex, z an independent balancing sign. Their Fourier support has size at most 2^m so H(G),H(H)<=m; I(G)=1+m/2 and I(H)>=1+m/2-2m2^-m. Thus both branches have H/I<2 for every m>=4: 2(1+m/2-2m2^-m)-m=2-4m2^-m>=1. Both terminal certificates are proved and retained. It follows from (7) that the whole shared-data point-switch family has H(F)<(11/2)I(F), retained J+terminal<=4I(F), and full sufficient KL ledger<7I(F), uniformly in m,s, and gamma=2^-m. This is the large-contrast family witnessing the necessary logarithmic local price, not a general terminal certificate.

For an actual vanishing-influence extension, activate the whole switched function under a fresh width-t point event with constant inactive branch. Equation (1) with source disagreement a in [0,1] is insufficient for arbitrary bias, but the constant-child split itself has B/d<3 (sum its nonempty derivative sectors plus Psi(d^2,(1-d)^2), maximizing d[c-2+2log2(1/d)] yields c/sqrt(e)<1). With JS<=2c d<3d its stopping prefix has entropy cost <6 I_control. Retain 2^-t H(F), 2^-t I(F). This gives H(1+A_t(F-1))<6 I(1+A_t(F-1)) on the balanced bent-switch family, with I=2^-t[I(F)+t] because F is balanced. For each fixed m,s, t tends to infinity and I tends to zero; dimensions and all widths are unrestricted. This uses the known constant-child activation interface only, not a newly asserted arbitrary-core result.

## Honest universal boundary

This proves an actual stopping-block entropy/KL payment using a once-issued terminal-coordinate reserve. It does NOT prove Q_bad,4<=constant I for arbitrary shared-data switches: localized odd-face costs can be much larger than the actual signed entropy bill. It does NOT prove that the two units of terminal-coordinate slack persist through many overlapping/nested point blocks. The first unsupported universal line is a history-transfer rule assigning these marked fractions to nested physical data histories without repeated consumption and retaining every terminal entropy. An arbitrary selector remains outside the fresh point-block grammar.
