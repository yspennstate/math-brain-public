# Independent review of the transported reserve

Verdict: **HOLDS**, for A046-SEPARATOR-LAYER-CUTOFF-RESERVE@1 exactly as
stated. Statement digest c4f09ea5b2a552f438fe64c85737ae4570e03f57453c63683f124dd3a245f2af.
Reviewer A040 supplies no substantive repair and is not a contributor to
that source version. The source's extra root-spectral/output conversion
discussion is outside this claim and outside this independent acceptance.

## 1. Reconstruct the cutoff without source code

For arbitrary signs G,H and a fresh j-bit point switch, put
gamma=Pr(G!=H), rho=2^{-(j-1)}, and d=rho gamma. Parseval gives
sum_T (Hhat(T)-Ghat(T))^2=4gamma. Each nonempty residual-selector label
has a zero amplitude in the first child and amplitude rho(Hhat-Ghat) in
the second. Summing the 2^{j-1}-1 equal parent-pair entropies yields
exactly 2(1-rho)d. The empty residual-selector labels have total
derivative-sector mass rho d and total pair mass at most one. The
inequality E(a,b)<=b log2(euler(a+b)/b), followed by log-sum, gives

    B/d <= 2+2^-k[log2(euler)-2+log2(1/gamma)+2k], k=j-1.

This is a bound on actual Fourier rows, with no Gaussian, biased-mask,
phase-independence or entropy-reference assumption. If gamma>=2^-D,
h0=ceil(log2(D+1)), m=h0+2, then j>m implies k>=h0+2,
D 2^-k<=1/4 and 2k 2^-k<=1. Since ln2>2/3 (the first term of the
positive atanh series is 2/3 and later terms are positive),
log2(euler)-2<0. Thus B/d<=13/4<4. No finite-width extrapolation occurs.

For B=WUV, C=U OR V and Dset=C-B, define q=2^-R,r=2^-T,
eta=2^{-(L+R+T)}, e=q+r-qr-eta. Since eta<=qr/2,

    e>=q+r-(3/2)qr>=max(q,r).

The last inequality uses q,r<=1/2. A balanced independent core makes
the branch disagreement gamma=e/2. Take D=min(R,T)+1, obtaining the
source cutoff m=ceil(log2(min(R,T)+2))+2 in all positive widths.

## 2. Reconstruct physical ownership

Let alpha=2^-s, JB=(L+R+T)eta, JC=R q(1-r)+T r(1-q), JD=JB+JC,
and pi=eta+alpha e. On each U-coordinate, a boundary edge of C requires
V to fail, while a boundary edge of B requires V and W to hold. These
sets are disjoint; similarly on V. W belongs only to B. Hence
J(Dset)=JB+JC, for J(E)=I(1-2E)/2. Conditioning physical edges gives

    I_sep=s alpha e,
    I_other=(1-alpha)JB+alpha JC,
    I_terminal=pi I(g).

Every reached active controller terminal is the SAME g, once per
physical input. Its expected entropy is pi H(g), including rare paths.
At a live separator state j, the actual query influence is 2^-j e.
Its child product is activated by a (j-1)-bit point times Dset. Direct
edge counting, including its remaining separator coordinates, gives

    c_j=2^-j[JD+(j-1)e+e I(g)].

This is an actual face cost, not separately credited event boundaries.

## 3. A different construction of the potential

Define the reserve from distinct eligible future layers first:

    W_j=sum_{ell=1}^{min(j,m)} 2^{-(j-ell)} c_ell.

The factor is the physical probability of reaching layer ell from j.
This nonnegative future-sum definition shows both where the reserve
lives and what it pays. Evaluating the finite arithmetic progression
recovers exactly the source V_j:

    V_j=W_j=2^-j[M_j JD+e M_j(M_j-1)/2+M_j e I(g)],
    M_j=min(j,m), V_0=0.

Failure kills this separator obligation; its remaining B-controller is
priced separately. On success, carry V_(j-1), without reopening a bank.
Subtracting the future sums directly gives

    V_j-E(V_child)=V_j-V_(j-1)/2
       = c_j for j<=m, and 0 for j>m.

The early zero drift is legitimate even if V grows along a success
branch: expected capacity, rather than pathwise monotonicity, is the
stated invariant. The cutoff proves that the actual bad-node cost is
at most this drift at every separator state. Summing actual histories
leaves zero terminal reserve and bounds Q_bad,separator<=V_s.

For M=min(s,m), alpha JD<=I_other because alpha<=1/2;
alpha e I(g)<=I_terminal; M<=s. Therefore

    V_s<=M I_other+(M-1)I_sep/2+M I_terminal<=M I(F).

This is a valid initial M-rate allowance. It does not prove that one
unit of rate pays all future separators, and it never claims that.

The finer physical ownership can also be made explicit. At a W coordinate
the actual influence is (1-alpha)eta, and the envelope debit is M alpha eta.
At a U coordinate they are (1-alpha)eta+alpha q(1-r) and
M alpha[eta+q(1-r)], respectively; exchange q,r for V. At any core
coordinate with native influence t, the actual influence is pi t and
the debit is M alpha e t. For a separator coordinate with ell bits
remaining when queried, the actual influence is alpha e and its debit
as a remaining coordinate in earlier eligible faces is
max(M-ell,0)alpha e. These are each <=M times the actual coordinate's
influence and their sum is exactly V_s. Thus the source is a transported
M-unit account, not transport of the exhausted one-unit account audited
in A040 stage 3. Distinct first-revealed faces can still meet the SAME
physical coordinate; nonreuse of faces alone does not bound this ratio.

## 4. Retained entropy account

After failure, the remaining controller is a point conjunction with
constant-child splits. After success it is the independent two-point
union. A040 stage 3 independently reconstructed their strict K=4
goodness for every width and balanced core. Briefly, constant-child
grouping gives B/d<=1+c+2c/euler<4, c=1/ln2; the two-point rule gives
B/d<=2(1-rho)+rho log2(euler/(rho d))<4 because the residual competing
point probability is at most 1/2. The core is stopped, not queried.

At a bad node, cube edge isoperimetry bounds B<=c_face+c d;
at a good node B<=4d. Exact entropy decrement is B+JS, with
JS<=2c d. Summing the stopping tree and its terminal gives

    H(F)<=(4+2c)(I_sep+I_other)+V_s+pi H(g).

The isoperimetric and scalar JS proofs are fully reconstructed in the
prior A040 stage-3 REVIEW_A023.md; the new cutoff and potential do not
assume FEI. An arbitrary-core entropy estimate has not been supplied.
This accepts the full exact source claim, not its unclaimed universal
extensions or additional witness/reference conversions.

## 5. Executed independent checks and first unpaid line

New code imports no A046 or A025 executable. It uses an A040-owned
exact arithmetic/Walsh prefix, copied into this run, and a new future-sum
potential implementation. Ten explicit Boolean roots include dictator,
balanced bent4, and balanced bent4/vertex-flip selector terminals.
All 694 audit assertions and 368 helper assertions pass, including
direct-edge/Walsh agreement, root and child face prices, control/core
influence partitions, retained entropy, compensated TC and odd-face
telescopes. All finite queried nodes happen to be 4-good; this is not
extrapolated. Another 1,920 rational cases give 10,560 exact drift
identities and 50,880 assertions, including the finer per-coordinate
debit partition above. Formal core-influence parameters in
these account cases are not called additional Boolean truth-table tests.

The first unsupported universal line is a constant influence price for
the ACTUAL bad-node debit, uniformly in growing controller widths, with
arbitrary terminal entropy and any prescribed reference/reset cost paid
on the same account. ENVELOPE_OBSTRUCTION.md proves that the current
V itself cannot have that uniform bound. That is a limitation of its
conservative envelope, not a counterexample to localized payment or FEI.
