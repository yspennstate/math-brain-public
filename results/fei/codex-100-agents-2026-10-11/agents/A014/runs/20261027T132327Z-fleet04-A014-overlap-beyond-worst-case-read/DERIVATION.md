# Feasible fractional activities pay the full normalizer; one connected overlap closes

All logarithms are base two unless written ln. Outputs are sign Boolean functions
on the uniform finite cube. Sources are fixed before the Fourier target. No
maximal-read bound, actual spectral entropy, or unpriced core reference is assumed.

## 1. A normalizer theorem for EVERY feasible weighted graph

Let G=(V,E) be ANY finite simple graph, including isolated vertices. Give every
edge a nonnegative activity lambda_e, with d_lambda(v)=sum_(e incident v)lambda_e
<=1. Put W=sum_e lambda_e. For A subset V define F(empty)=1. For nonempty A,
sum over EVERY maximal matching M of G[A] and all attachment choices of its
unmatched vertices. A root e contributes lambda_e/24. An unmatched vertex
attaches to an outside neighbor with weight lambda_e/32 or a matched endpoint
with weight lambda_e/8. A root receiving a,b leaves at its endpoints also
contributes J(a,b)=a!b!/[(a+b+1)^2(a+b+2)]. Let Z=sum_(A nonempty)F(A).
Zeros are allowed in this normalizer lemma; no support positivity is asserted.

THEOREM. The ENTIRE original sum, including its empty structure, satisfies

       1+Z <= exp[(275/2352)W] <= exp(W/8).                    (1)

Proof. J(a,b)<=a!b!. For a fixed root matching with r edges, order each list
of internal leaves at its endpoint. The factorials count precisely those
orders when leaf labels are distinct. Allowing repeated labels and overlap
with roots only enlarges the sum. At endpoint v a list of length t has total
activity weight (sum_u lambda_uv)^t<=1. Summing lengths with leaf factor1/8
gives (1-1/8)^(-2r)=(64/49)^r. This is a geometric series with ratio1/8<1.
External leaves sum independently to at most

       product_v(1+d_lambda(v)/32) <= exp(sum_v d_lambda(v)/32)
                                  = exp(W/16).

Every original structure is counted, possibly more than once in the relaxed
bound; distinctness and matching maximality were relaxed only upward. Weighted
root matchings are bounded by ordered edge tuples divided by r!, giving

 sum_M product_(e in M)[(64/49)lambda_e/24]
       <= exp[(8/147)W].

Multiplication gives (1), since 1/16+8/147=275/2352<1/8. If W=0, Z=0
and equality holds at the empty structure. Everything is nonnegative, so
the countable geometric sums may be rearranged monotonically. The original
sum itself is finite. Feasibility, rather than a global maximum degree, pays
this complete normalizer. For positive Z, log Z<=W/(8 ln2)<W/4.

### The normalizer is universally INFLUENCE-paid on graph edge unions

Let C be the independent-set indicator of this SAME graph G, and f=1-2C.
Let s=EC, v=Var(f). Conditional on C=1, write p_v for the occupation
probability of vertex v and t_v=1-2p_v. Downward closure gives t_v>=0:
removing a selected v injects independent sets containing v into those not
containing v. For any edge uv, condition on all other vertices. The possible
uv patterns are {00,10,01}, {00,10}, {00,01}, or {00}; thus the conditional
mean of x_u+x_v is at most2/3. Averaging gives t_u+t_v>=2/3.
Consequently fractional feasibility implies

 (2/3)W <= sum_(uv in E)lambda_uv(t_u+t_v)
          =sum_v d_lambda(v)t_v <=sum_v t_v.

The EXACT downset boundary identity is I(f)=2s sum_v t_v. It follows by
counting all n|C| incidences and subtracting twice the internal cube edges,
whose number is sum_(X independent)|X|. Therefore

       I(f)>=(4/3)sW,       vW<=3I(f),
       v log2(1+Z) <= [275/(784 ln2)]I(f)
                    <=[3/(8 ln2)]I(f)<(9/16)I(f).           (1a)

For Z>0 this also pays the POSITIVE PART of v log Z, retaining any negative
normalization refund. No support positivity or chosen spectral cover is used
in (1a). If G has no edges then W=Z=I=v=0 and its assertion is zero<=zero.
The factor3 in vW/I is SHARP as a supremum: on m disjoint edges with every
activity1, vW/I=3[1-(3/4)^m] tends to3. This is a matching calibration of
the incidence-to-influence step, not a sharpness assertion for the exponential
normalizer constant. Thus only the atom-cost expectation remains unpaid on
arbitrary connected graph overlaps; the complete normalizer no longer does.

Feasibility is essential to (1): on a star with64 leaves, all activities1,
the full selected atom is64!/[24*8^63*64^2*65]>3^8>exp(W/8), W=64.
Only the hub row is infeasible. This exact boundary counterexample prevents
dropping the row constraints when using ordered endpoint lists.

## 2. Actual connected growing-overlap family and physical influence

Let G_m be the windmill of m triangles, m>=4. There is one hub h and m
disjoint leaf pairs (x_j,y_j); its edges are hx_j,hy_j,x_jy_j. Let C be its
independent-set indicator and f=1-2C. Write

       a=(3/4)^m, b=4^-m, s=(a+b)/2, v=4s(1-s).

At h=0 the event is the product of m independent no-double-one edge events;
at h=1 every leaf is zero. These are actual restrictions on the SAME leaf
cube. Direct physical pivotal counting gives

       I_h=a-b,
       I=(1+2m/3)a+(2m-1)b.                                (2)

Every vertex is relevant. Every edge is an indispensable positive minterm
of the edge union, so maximum read is2m. The incidence graph is connected;
there are no disjoint components or dummy controls. Gates are width2 and
any two distinct gates intersect in at most one variable.

The following all-m estimates will be used only at m>=4:

       (2/3)m a <= I <= m a,
       v/I <= 82/(27m),
       log(48m)<=2m.                                       (3)

For the upper I bound, b/a=3^-m and (2m-1)3^-m<=m/12 at m>=4, so
I/a<=1+3m/4<=m. Also v<=2(a+b)<=164a/81, proving the second bound.
For the last, log48<6 and log m<=m/2 for real m>=4; the latter starts
with equality at4 and has derivative log(e)/m<=1/2 there and thereafter.

## 3. A locally feasible ORIGINAL source and spectral congestion

Set leaf-pair activity alpha=1/2 and every spoke activity beta=1/(2m).
The hub load is exactly1; a leaf load is alpha+beta<=1. Thus (1) applies,
with W=m/2+1. Use the SAME occupation formula, all root and attachment
events, and q(A)=F(A)/Z on nonempty A. Its full calibrated probability is
Q(empty)=1-v, Q(A)=v q(A). Every nonempty atom has positive F, as the
lower bounds below prove. Define the ACTUAL spectral congestion

       kappa_h = Pr_(fhat^2)(h in S) log(48m)/I
               = (a-b)log(48m)/I <=3.                       (4)

This quantity is not defined by CE/I. The last bound follows from (2)-(3).

For a leaf set let u be the number of singleton pairs and d the number of
double pairs. Set B=(alpha/32)^u(alpha/48)^d. If the hub is absent, match
every double pair and attach each singleton to its outside mate. This gives
F>=B. If the hub is present and u>=1, match it to one of the u selected
singletons, match all doubles, and attach the remaining singletons to their
outside mates. These u distinct maximal matchings give

       F >= u(beta/48)(alpha/32)^(u-1)(alpha/48)^d
         = [2u/(3m)] B.

If the hub is present and u=0, match all double pairs and leave the hub
unmatched. Its outside attachments contribute2(m-d)beta/32, while attachments
to matched endpoints contribute2d beta/48, because J(1,0)/J(0,0)=1/6.
Their sum is at least m beta/24=1/48, giving F>=B/48. This also includes
the singleton hub with d=0. Thus, in every case,

       log(1/F(A)) <=7m+1_(h in A)log(48m).                  (5)

Indeed alpha/32=1/64, alpha/48=1/96>1/128 and u+d<=m. Both positive
and negative values of log F are allowed; (5) is only an upper bound.
No matching/attachment mass is discarded from the original source.

The COMPLETE cost is

       CE(f,Q)=h2(v)+sum_(A nonempty)p(A)log(1/F(A))+v log Z. (6)

By (1), log Z < W/4=m/8+1/4<=3m/16. Also v>=a, because s<=1/2 and
v>=2s=a+b. The elementary scalar bound h2(v)<=v log(e/v), with
log e<3/2 and log(4/3)<1/2, gives h2(v)<=(m/2+3/2)v<=7mv/8.
Putting these estimates in (6), retaining the signed normalizer first,

       CE(f,Q) <= (129/16)m v + (a-b)log(48m)
               <= [1763/72+kappa_h] I
               <= (1979/72)I <28I.                         (7)

This is a fully paid ORIGINAL root reference on a connected unbounded-read
family, with a bounded explicit spectral congestion and fractional loads.
By Gibbs, actual H(f)<=CE(f,Q)<28I. No novelty is claimed for FEI on this
special width-two family; the result pays the stated complete source.

## 4. Global scale fails even on this CONNECTED family

Keep G_m but give EVERY edge the globally feasible lambda=1/Delta=1/(2m).
For h absent, exact original mass on the leaf profile is

       F_0(u,d)=(lambda/16)^u(lambda/48)^d.

Let Ahat denote the Fourier coefficient of the no-double-one product on the
leaf cube. For the two hub sectors the actual nonempty sign coefficients
are -(Ahat+b) and -(Ahat-b). Summing the h-absent spectrum gives

       v_0=a+3b-(a+b)^2,
       sum_(h absent) p(S)*(u+d)=(m/4)(a+5b).                (8)

For example the three terms in the second identity are ma/4 from Ahat^2,
mb/2 from2b Ahat, and3mb/4 from b^2. They follow from the four exact
one-pair coefficients(3/4,1/4,1/4,-1/4). The empty set contributes zero
to this moment and is excluded in v_0.

The full Z includes all singleton masses. Their sum is
sum_v d_lambda(v)/32=2W/32=3/32. Hence log Z>-4, not an unpriced
unknown normalizer. All OTHER normalized atom code lengths are nonnegative,
so discarding the hub-present contribution only lowers CE. Therefore

       CE(f,Q_global) >= (m/4)(a+5b)[log(2m)+4]-4v_0.

Using I<=ma, v_0<=a+3b<=28a/27 and I>=2ma/3 yields

       CE(f,Q_global)/I >= (1/4)log(2m)+1-56/(9m) -> infinity. (9)

This refutes global feasible scaling on CONNECTED linear-hypergraph overlap.
It is not a failure of all feasible weights or fixed mixtures: (7) explicitly
repairs the source. It is not an FEI counterfamily, by (7) itself.

## 5. Scope of the universal bridge

The normalizer theorem (1) holds for ALL finite graphs and ALL feasible
fractional activities. The expected atom cost (5) is proved only for the
windmill. Neither (1) nor feasibility bounds that expected cost universally.
The next unpaid line is a locally weighted whole-set atom/attachment bill
on connected overlap with a growing interacting core, not just one hub.
The earlier disconnected counterexample and local repair remain valid.
No auxiliary physical influence or reach probability is removed.

The supplied-source projection/profile history theorem of A012, if used,
has a DIFFERENT inheritance convention from vacuum-calibrated v6: raw
spectral projection of the FULL Q. It retains signed entropy decrements,
all query KL contractions, full profile conversion fees and both complete
terminal laws. Under exactly that interface (7) plus2I/ln2 pays the full
history below31I, with any already funded booking b separately retained.
No true-kernel conversion, mandatory floor, positive-part fee or productive
arbitrary-core stopping policy is supplied for free.
