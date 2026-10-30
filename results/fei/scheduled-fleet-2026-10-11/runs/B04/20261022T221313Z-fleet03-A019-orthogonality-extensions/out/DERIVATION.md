# Opposite means: exact reference discontinuity and a single owned payment

All logarithms are base two. Put E(v)=1[v=0], epsilon=2^-k,
h_+(u,v)=(1-E)u+E and h_-(u,v)=(1-E)u-E. Both children are nonconstant,
have means +/-epsilon, disagree on exactly E, and have the SAME squared spectrum P.
Its coefficient at {u} is (1-epsilon)^2; all other 2^(k+1)-1 atoms have mass epsilon^2.
The physical parent h(q,u,v)=(1-E)u+qE has empty coefficient zero and a positive
q-only squared coefficient epsilon^2. Take Q_b=(P+delta_empty)/2 for both children.
The prescribed parent conditional lift of their average puts the full empty-row
reference mass on q PRESENT; hence Q_h(empty)=0, not a freely assignable zero row.
All other zero true rows are assigned q ABSENT. This convention is fixed before sampling.
KL_parent=KL_child exactly, and D_core=0 (the children have identical P and Q).

For the same nonlinear two-bit mask with mean 1/2 and Q_s=P_s uniform, put t=1/4.
The activation posterior refund for core mean squared m and empty reference a is

 D_t(m,a)=1/2 [t*m*log(m/a)+(1+t*m)*log((1+t*a)/(1+t*m))].

Use continuous zero conventions, so D_t(0,0)=0. Thus parent refund is zero,
the two child refunds coincide, and the exact net reference surcharge is

 Lambda_k=D_(1/4)(epsilon^2,(1+epsilon^2)/2).

It converges to (1/2)log(9/8)>0 while query disagreement epsilon tends to zero.
Indeed it is uniformly greater than 1/32 for k>=2: D increases in its second
argument above the diagonal and decreases in the first below the diagonal,
so Lambda>=D_(1/4)(1/16,1/2)=(-3+65log(72/65))/128>1/32.
The last sign is the exact integer comparison 72^65>2^7*65^65.
The limit uses x log x ->0 and ordinary continuity of positive log arguments.
This rules out any universal Lambda<=K*d for THIS incoming reference hierarchy,
even with both children nonconstant and equal squared spectra. It does not refute FEI.
The old two-balanced-child repair is inapplicable: the folded row now has positive true mass.

Payment: for k>=2, I_b=1+(k-1)epsilon and
H_b=eta((1-epsilon)^2)+2k(2epsilon-epsilon^2).
The inequality eta(z)<= (1-z)/ln2 gives H_b<=2epsilon/ln2+4k*epsilon.
Since ln2>1/2 and epsilon<=1/4, 4I_b-H_b>4-8epsilon>=2.
Q_b>=P_b/2 gives KL_b<=1. Therefore the ORIGINAL supplied core reference cost
c_b=H_b+KL_b has slack s_b=4I_b-c_b>1. No new child source is substituted.

For 0<=m<=a, differentiation of 2D_t in r=tm, with v=ta fixed, gives
log[r(1+v)/(v(1+r))]<=0 on 0<r<=v. Hence
0<=D_t(m,a)<=D_t(0,a)=(1/2)log(1+ta).
Here a<=17/32 and t=1/4, so Lambda_k<1/8, certified by
(145/128)^4<2. The available half-core bank is s_b/2>1/2;
one booking Lambda_k leaves more than 3/8 of that SAME bank unused.
If an incoming booked debit U is already present with 0<=U<=1/8, retiring
that SAME U as well leaves more than 1/4; no bank is renewed.
The mask cost, both complete activation child terminals, and profile curvature remain explicit.
The curvature is bounded by the already established A*d with A=(9/8)log(3)-1,
and physical activation-query influence is d/2. This stage never spends that influence twice.

More generally, with the same exact mask reference (t=sigma^2=1/4), arbitrary
Boolean children and finite complete supplied Q_b satisfying
P_b(empty)<=Q_b(empty), write A0=(Q_0(empty)+Q_1(empty))/2 and sbar=average(KI_b-c_b).
The old exact insertion and D_core,D_parent>=0 imply
Lambda<=average D_b<=1/2 log(1+t*A0).
Thus if the already-booked amount is U>=0 and sbar>=2U+log(1+t*A0),
the ONE remaining half-core bank sbar/2-U pays Lambda_+. Setting U=0 gives
the corresponding unspent-bank criterion; no old booking is silently reused.
This is a conditional reference-transfer lemma, not a construction of eligible references
for arbitrary Boolean cores. Positive core atoms must have positive supplied reference mass;
the incoming parent reference must be the specified conditional lift, rather than reset after querying.

## Removing just one balance assumption

Take h0=u and h1=(1-E)u+E, with means 0 and epsilon and disagreement epsilon/2.
The same Q_b=(P_b+delta_empty)/2 is supplied. Put m=epsilon^2. Now
P_h(empty)=P_h({q})=m/4>0 and Q_h(empty)=(2+m)/8 is FORCED by the true conditional.
Only the empty folded row contributes to the core posterior refund:

 D_core=(m/2)log((2+m)/(1+m)),  0<=D_core<=m/2.

All other rows have reference equal to half their true mass, with identical true/reference
tag posteriors. The exact surcharge is

 Lambda= [D_(1/4)(0,1/2)+D_(1/4)(m,(1+m)/2)]/2
          -D_(1/4)(m/4,(2+m)/8)-D_core/2.

As k tends to infinity this converges to (1/2)log(18/17)>0. Thus no K*d
payment holds even with ONE balanced child, while both children remain nonconstant.
The positive lower limit follows by x log x ->0; no uniform finite-k positivity
is needed for the counterfamily. The finite k1 boundary has NEGATIVE Lambda;
the overstrong blanket sign assertion failed there and is preserved in out/ONE_BIASED_FAILURE.json.
The exact finite k2..8 signs are positive. No extrapolation of those finite signs is used.
The general empty-reference domination lemma bounds Lambda_+<1/8 for k>=2.
The original character core has c0=1,I0=1, hence slack3. The other core has slack>1.
Thus the original half-average core bank is >1; after any old U<=1/8 and the new
Lambda_+ booking, more than 3/4 remains. The actual entropy decrement of the core
and both complete child activation costs stay in the insertion identity.

Universal gap: preserve the remaining original bank through one further data query, for which
the same contaminated references need not satisfy the same eligibility or empty-row domination.
Full FEI remains OPEN. These are author-derived proofs; executed validation and independent-review disposition are recorded separately in REPORT.md.
