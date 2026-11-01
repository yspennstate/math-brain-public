# Composition audit and continuation priced by the actual fee

All spectral entropies include the empty coefficient and use bits. Every core is a Boolean sign on a finite uniform physical cube. All accounts below are expected-resource accounts with explicit conditional-mean-zero transfers; a large child principal need not fit its parent's subtraction-only cash. Full FEI remains OPEN.

## 1. Independent reconstruction of the imported singleton bound

Write p=Inf_i(g), I=I(g), D=H(g)-(H(g_0)+H(g_1))/2 and J=(I(g_0)+I(g_1))/2=I-p. The letter J here denotes remaining influence, not Jensen-Shannon divergence. Set delta=min(p,1-p). The sign u=g_0 g_1 is negative on fraction p, so edge isoperimetry applied to its smaller sign class yields I(u)>=2 delta log2(1/delta). For each remaining physical coordinate, a change of u requires a change of at least one child, hence I(u)<=I(g_0)+I(g_1)=2(I-p). Thus I>=p+delta log2(1/delta). Constants and delta=0 use the continuous convention 0log(1/0)=0.

Independently, the spectral inclusion bit has entropy <=h2(p), and the actual child spectral Jensen-Shannon divergence is <=min(1,2delta/ln2), using the amplitude-pair inequality on every Fourier pair. Therefore D<=h2(p)+min(1,2delta/ln2). The latter bound retains both full child laws. It also gives D>=0 from the exact erasure plus JS identity.

Let ell=log2(3), kappa=3-2/(1+ell). For p<=1/2 replace 2/ln2 by 3, and compare with kappa*p*(1+log2(1/p)). On [0,1/3] the difference from h2(p)+3p is concave and vanishes at both endpoints. On [1/3,1/2] the difference from h2(p)+1 is concave, with values 0 and kappa-2. The second derivative in both intervals is [1/(1-p)-(kappa-1)/p]/ln2<=0, since kappa>2 and p<=1/2. For p>=1/2, I>=p+delta>=1 and D<=2. Hence D<=kappa I. Finally 3^5<2^8 implies ell<8/5 and kappa<29/13=:k. This proves the exact rational account inequality D<=kI used below; it does not improve A060's constant.

## 2. A059's two tickets and geometric policy

The source rate 9/2 splits exactly into 2k+1/26. Split BEFORE first expenditure; this does not repair a previously exhausted owner. Through an already-paid physical core split a pending k t I(g) ticket becomes k t I(g_a) plus release k t p in each child. Their mean equals its parent. Exterior splits preserve its expectation since t is harmonic; genuine tags preserve I. At a selected fee tD consume and close one ticket, leaving k t I-tD>=0. Transport the other ticket through the same query, retaining its own release. This reconstructs TWO adaptively selected queries with the SAME root source and no recreated ticket.

For fresh independent dyadic continuation q<=1/2, the pending rate A=k/(1-q) satisfies A<=2k. After the query the expected surviving principal is qAtJ and the released cash is AtI-tD-qAtJ>=qAtp. The core split reserves qAtI(g_a), and the subsequent independent irrelevant coin assigns AtI(g_a) to survival and zero to stopping, with exactly that mean. Every stopped child retains its full entropy. This verifies the new A059 transaction at its written scope. A091 contributed the older 9/2 source and therefore accepts the NEW transaction independently, not its own source dependency as an independent full-chain review.

The physical wrapper F=K+Cg has exact E=H(F)-tH(g). Its full local decrement is tD+E_parent-E_child_avg. Attach E to the original exterior account, retain its prior debits and both actual exterior/core terminal profiles. Adding the preceding core account transactions then gives the full stopped entropy identity. No independence of overlapping physical cores is inferred: the theorem applies to one actual current g, and never replaces a reused g by independent copies.

## 3. A060's full-terminal law

An AND2 sign negative at a single point has all four squared Fourier coefficients 1/4, so H=2,I=1. Revealing one chosen input makes both children a constant or dictator: H=0, expected remaining influence=1/2. An untouched independent tag z keeps z times every reached product balanced, including after constant factors occur.

For the four-bit paired bent sign b and its all-one point indicator C of density c=1/16, K=b-C has ten squared coefficients 9/256 and six squared coefficients25/256. Balancedness makes the core-empty and core-nonempty sectors disjoint. Direct expansion gives H(K+Cg)=E0+cH(g), E0=8-(45/64)log2(3)-(75/64)log2(5). All four exterior influences are 1/2-c. Thus r AND2 factors give H=E0+r/8, I=7/4+(r+1)/16.

If S_r is the expected number of queried factors, the COMPLETE expected terminal entropy is E0+(r-S_r)/8 and influence is7/4+(r+1-S_r/2)/16. Hence entropy debit is exactly four times removed influence. Fixed independent continuation q<1 gives S_r=(1-q^r)/(1-q)=O(1), leaving terminal/root entropy ratio tending to one. For horizon-dependent constant q_r that ratio tends to zero exactly when r(1-q_r)->0. Sufficiency follows from 1-q^j<=j(1-q); necessity follows from q^j<=(1+j(1-q))^-1 on the last half of the sum. These statements retain any fixed positive old prefix cost. This independently accepts A060's exact terminal formulas and horizon condition.

## 4. New adaptive continuation transaction

Keep the SAME original rate A=9/2, allocated before use, and pending principal AtI(g), plus all existing unused cash and exterior escrow. No uniform additional 1/26 reserve is asserted here. At a selected core query use the actual pre-query D,p,I,J. If J>0 define

    q_star=min(1,(AI-D)/(AJ)).                         (6)

The numerator is nonnegative because D<=kI and k<A. Thus q_star is in[0,1]. Choose ANY dyadic q in[0,q_star], before seeing the core answer, then implement it with fresh independent irrelevant physical bits after the answer. The exact release is

    R=t[AI-D-qAJ]>=0.                                 (7)

In child a reserve qAtI(g_a), and after the coin retain AtI(g_a) only on survival. Both stages have precisely balanced conditional innovations. Close stopped principal once. All old cash stays unused. This is the same resource as in Section2, with an actual-fee decision replacing its uniform worst-case continuation bound. Any finite depth is allowed, and both full terminal functions remain.

If J=0 both children have influence zero and are constant. End the policy without a coin. The fee is paid since D<=kI<=AI; no division by zero occurs. If I=0 the current core is constant, D=p=J=0, and no further query is necessary. A zero-influence queried coordinate has D=0 and q_star=1 when I>0. Such dummy core queries can simply be omitted.

Equation(6) is the MAXIMUM feasible answer-independent continuation at this node for this particular pending potential and nonnegative immediate release: (7) rearranges to q<=q_star when J>0. It is not an optimality claim among other potentials or answer-dependent continuations. It implies q_star>=1-k/A=59/117, strictly larger than1/2. More usefully, q_star=1 exactly when D<=Ap. Thus every affordable physical query continues deterministically; full deterministic paths with this property are paid by actual influence removal, retaining all releases. This condition is NOT asserted universally.

For ideal real-valued independent coins at q=q_star, let O=(D-Ap)_+. Then

    (1-q_star)AJ=O,     R/t=(Ap-D)_+.                (8)

These are algebraic optimal-boundary identities, not an assertion that arbitrary irrational q_star is a finite uniform physical coin. For a b-bit physical coin choose q=floor(2^b q_star)/2^b (or ANY certified lower dyadic approximation). The first identity becomes

    (1-q)AJ=O+A(q_star-q)J.                          (9)

If an enclosure chooses q with q_star-q<=2^-b+epsilon, its excess discarded influence is at most(2^-b+epsilon)J. At q_star=1 choose q=1 EXACTLY, avoiding artificial stopping on affordable queries. Arbitrary bias of the Boolean OUTPUT is allowed; the PHYSICAL core measure here remains uniform. No claim extending (1)--(9) to product-biased physical inputs is made.

Summing(8) on any finite policy, with node physical reach weights w and density t, gives

    A E[t I(g_leaf); forced-stop leaves]
       =sum_selected_nodes w t (D-Ap)_+.             (10)

Cap leaves and already constant leaves are separate; constants have zero influence. Equation(9) gives the exact nonnegative rounding correction for physical dyadic policies. All nodes and outcomes remain in the sum. This identifies precisely where the budget is liquidated: a local excess is paid by discarding future influence principal, not by paying the discarded child's entropy.

On A060's tagged AND2 product, D=2,p=1/2, so D<Ap=9/4. Equation(6) chooses q=1 at EVERY selected factor query, pays deterministic full entropy decrease2r, and leaves the tag with entropy zero. The wrapper debit is r/8, old prefix fees remain booked, and the unused root core reserve is c[(9/2)(r+1)-2r]>0. Thus this rule repairs the actual fixed-q terminal control without an extra source. This is a mechanism refinement, not a new isolated FEI class claim.

## 5. A finite Boolean obstruction to full payment at the fixed 9/2 rate

There is a direct reason not to demand universal complete payment from this particular rate. Let g_0(x)=x, and let g_(d+1)=NAND(g_d(X),g_d(Y)), with independent disjoint copies and NAND(a,b)=-1 exactly at a=b=+1. This defines an actual read-once Boolean sign on2^d variables. If its mean, entropy and influence are m,H,I, the next mean and influence are

    m'=(1-2m-m^2)/2,       I'=(1+m)I.

For general independent means m,n, put a=(1+n)/2,b=(1+m)/2,V=1-m^2,W=1-n^2 and m'=(1-m-n-mn)/2. The constant, first-child-only, second-child-only and both-nonempty Fourier sectors give the exact entropy formula

    H'=eta(m'^2)
       +a^2[H-eta(m^2)]+eta(a^2)V
       +b^2[K-eta(n^2)]+eta(b^2)W
       +(1/4){W[H-eta(m^2)]+V[K-eta(n^2)]}+(1/2)VW.

Here eta(s)=-slog2(s), eta(0)=0. These sectors are disjoint because the physical child supports are disjoint. A known composition identity is independently rederived here, rather than assuming unbiased output gates.

At depth5 this yields a32-variable seed with

    m=1632783679/2147483648,
    I=98620389/67108864,
    H in [266296069353640346422000061583/39614081257132168796771975168,
          532592138707280692844000123203/79228162514264337593543950336].

In particular H-(9/2)I>1/10 EXACTLY. The enclosure uses36 rational atanh terms with an explicit positive geometric tail and outward96-bit dyadic rounding at every operation. code/seed_certificate.py records the complete recurrence and checks its first four depths by actual Boolean truth tables and a separate butterfly spectrum. The floating pilot only selected this seed; the rational interval is the sign certificate. No priority claim about this known type of lower bound is made.

Take N=2048 independent copies of g_5 and multiply their product by one untouched fresh tag z. Its mean is zero, entropy NH, and influence NI+1. Put this core in the actual four-bit wrapper of Section3. Then

    H(F)=E0+(N/16)H,
    I(F)=7/4+(NI+1)/16.

Even granting the COMPLETE wrapper profile E0 for free, the original exterior bank7 and original core bank(9/32)(NI+1) cannot pay this full entropy:

    H(F)-[E0+7+(9/32)(NI+1)]
       =(N/16)[H-(9/2)I]-7-9/32
       >128/10-7-9/32=883/160.

This is an explicit65541-variable Boolean function described by a fixed formula and exact composition certificates, not an alleged exhaustive truth-table computation at that dimension. Any booked old nonnegative fee leaves still less capacity. It follows by telescoping that NO continuation or terminal-payment rearrangement can remove all full terminal entropy from this fixed source on every core. This does not contradict A059's stated partial-payment theorem or FEI. The source RATE must change (a finite larger rate could survive); simply improving continuation while retaining universal9/2 complete-payment aspirations is impossible.

## 6. First unpaid line and review limits

For an arbitrary core, forced-stop leaves may retain an arbitrarily difficult spectral entropy. Equation(10) bounds their discarded INFLUENCE, not their ENTROPY. A dimension-independent inequality pricing their complete entropy by the unused original budget, or a useful different continuation on them, is still unproved. Likewise a finite depth cap retains its complete terminal bill. None of the transaction identities makes the terminal bill disappear.

Section5 supplies an actual complete-entropy budget obstruction, stronger than a local high D/p example. At a chosen larger fixed rate A>=k, Section4 still gives the exact adaptive transaction and liquidation identity, but a useful all-core terminal theorem remains unpaid. The next target is a dimension-independent original rate and entropy-sensitive payment beyond this certified9/2 obstruction, with unchanged old costs and both terminal laws. Proof rung: written proof with exact finite controls and a finite rational interval certificate, external review pending; the attempted Lean scalar check timed out with RUNTIME_UNVERIFIED and supplies no formal certification.
