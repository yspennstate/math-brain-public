# Second shared query on an already-paid majority cofactor

Bits, uniform physical inputs, full Boolean spectra. This is a supplied-source continuation theorem, NOT full FEI. Let odd d>=5 shared bits carry central majority, positive at weight<d/2. Edit vertices0,e1 by arbitrary correlated Boolean private profiles V,W on an independent private cube. Allow arbitrary private queries before, between and after at most TWO distinct shared NONSEPARATOR queries (coordinates other than1), chosen adaptively without repeats. Stop anywhere, retaining every sibling and complete core/terminal entropy. No guard-order or profile-mean restriction is imposed.

## 1. Exact biased-cofactor Fourier recurrence

Put n=d-1 even. After a first nonseparator answer0, the unedited carrier c_n is positive at weight<=n/2; answer1 gives its negative complemented counterpart. Write alpha_n=binom(n,n/2)/2^n. It is the physical influence of either carrier at every remaining coordinate, by direct pivotal-edge counting.

The parent odd-majority coefficients vanish at even cardinalities. At odd cardinality2l+1 their value is

 A_(2l+1)=(-1)^l alpha_n binom(n/2,l)/binom(n,2l).

Proof: differentiating parent majority in one physical bit gives exactly the indicator of the tie slice on n other bits. Conditional on a tie, the generating polynomial for elementary sign products is (1+t)^(n/2)(1-t)^(n/2). Its coefficient at2l divided by binom(n,2l) is the conditional product moment, proving the formula. In particular A_(k+2)=-k A_k/(n-k) for odd1<=k<=n-1.

For the answer0 cofactor, coefficients beta_k are A_(k+1) at even k, and A_k at odd k. Hence beta_(2l)=beta_(2l+1); absolute values agree for answer1 as well. For a queried remaining bit, let

 I_even=sum_(k even) binom(n-1,k) A_(k+1)^2 <= I(c_n)=alpha_n.

Using binom(n-1,k)*k/(n-k)=binom(n-1,k-1), the adjacent-level product sum is EXACTLY

 2 sum_(k=0..n-1) binom(n-1,k)|beta_k beta_(k+1)|=4 I_even. (1)

This identity is the replacement for the parity-zero argument, which is unavailable on a biased cofactor. Phi(a^2,b^2)<=2|ab| therefore bounds its unedited shared erasure by4alpha_n. The binary inequality is proved in A076 v8 section3 and is elementary; it includes zero endpoints.

## 2. Complete edited mean sector after the first paid query

On the surviving first answer0, both edited vertices remain adjacent, their mass p=2^-n, and private means mu,nu may be arbitrary in[-1,1]. The COMPLETE empty-private spectrum is

 mhat(S)=beta_|S| -p[(1-mu)+(-1)^(1 in S)(1-nu)].

For a second nonseparator j, the additive translation t_S is identical on paired labels S,S+j and |t_S|<=4p. Thus, by Phi<=2|ab|, triangle inequality and Parseval,

 B_j(m)<=2 sum_pairs |beta_S beta_(S+j)|
           +8p sum_all_labels |beta_S|+32p^2*2^(n-1)
        <=4alpha_n+8*2^(-n/2)+16*2^-n.              (2)

Here the coefficient sum is the FULL carrier Fourier l1 norm, bounded by2^(n/2) since ||c_n||_2=1. This loses no private labels: it concerns the complete empty-private sector only. Both translations and all carrier/edit interference are included.

The two sequences 2^(-n/2)/alpha_n and2^-n/alpha_n decrease along even n>=4: alpha_(n+2)/alpha_n=(n+1)/(n+2), while the respective numerators scale by1/2 and1/4. At n4 the last two terms of(2) total3 and alpha_4=3/8. Therefore, for EVERY even n>=4,

 8*2^(-n/2)+16*2^-n<=8alpha_n, B_j(m)<=12alpha_n. (3)

All edited points AND their j-neighbors have carrier value+1 because n>=4 and their weights are at most2. The first query fixed0, so none of these edges was pivotal in c_n. Direct physical counting gives

 Inf_j(F)=alpha_n+p(2-mu-nu)>=alpha_n.             (4)

On the event-dead first answer1 there are no edits: B_j(m)<=4alpha_n and physical influence is alpha_n. Consequently BOTH actual first children, including the nonconstant event-dead sibling, satisfy B_j(m)<=12Inf_j(F). No fixed positive influence floor is assumed. Alpha_n tends to0, since its recurrence has a divergent harmonic logarithmic decrement; the added4p also tends to0. This is a small-influence result uniform in d, not a fixed-dimensional enumeration.

## 3. Full inherited sector, original R and first shared transaction

At r remaining shared bits, p=2^-r, retain
 U=p[H(V)+H(W)], R=r p[Var(V)+Var(W)]
when both events live, and U=R=0 on event-dead carrier branches. At ANY shared query the nonempty-private squared mass is p[Var(V)+Var(W)]. Partitioning erasure by private Fourier label gives nonempty erasure at most this mass, exactly the ORIGINAL reserve release R-E R_child. U is harmonic. DeltaH=B+JS and JS<=2Inf/ln2<3Inf imply for the SECOND query

 Delta H<=release_R+15Inf.                         (5)

The FIRST query has price5, reconstructed from A076 v9: odd carrier parity makes its even mean-sector squared mass Q=e[(1-mu)^2+(1-nu)^2]/2<=4e, e=2^-d. Concavity of Phi bounds the complete empty erasure by h2(Q)<=h2(4e)<4de. The physical carrier edge alpha_d=binom(d-1,(d-1)/2)/2^(d-1) obeys4de<=2alpha_d for every odd d>=5 (base d5, then recurrence or binomial maximum), and edits add nonnegative influence at the chosen nonseparator. The same existing R release pays all nonempty-private erasure. Hence first DeltaH<=release_R+5Inf, even after arbitrary private prefixes and early guard exposure.

## 4. SAME original signed account through both transactions

The private theorem, reconstructed in A078 v2 section1 from A077 mean curvature, holds for arbitrary Boolean carrier h with h=+1 at both edited points, including each current biased cofactor:

 Delta_private H<=Delta U+release_R+12Inf_private+Delta Xi,
 Xi=p sum_nonempty k(Vhat,What), -4p<=Xi<=0.

No universal input FEI premise is assumed. After all old bookings, at original continuation state o supply B>=4e_o and put C=(B-Xi_o)/e_o. While the two adjacent events live use K=p C+Xi. On event-death set K=0 but retain the actual nonconstant carrier entropy. Each nonseparator doubles p,Xi,K only on its surviving child, so E K_child=K_parent across BOTH shared transactions. Under private queries Delta Xi+E K_child=K_parent. The physical surviving event mass is a martingale. Finite original-reach telescoping therefore gives

 H(F_o)-E H(F_leaf)+E(R_leaf+K_leaf)
 <= U_o-E U_leaf+R_o+B+12P_private+5P_first+15P_second, (6)

 E K_leaf>=B-4e_o.                                (7)

All adaptive orders satisfying the declared at-most-two nonseparator condition are included, with arbitrary private suffixes. No separator or third shared query is silently paid. Input entropy decrements and complete actual terminal entropy remain. The transaction price15 differs from the preceding first-query5 because the biased cofactor no longer has a zero parity sector; (1)-(3) replace that proof. These are continuation prices, not a global FEI constant.

At the ORIGINAL bent source, even k>=4,m>=2,V=y*bent_k,W=y[1-2point(z=0,x1=...=xm=0)], S=e_o(3k/2+5), and5e_o I(V)=e_o H(V)+S. Retain FIRST4e_o collision debit plus any old D0>=0. After BOTH initial x1 answers take B=S-D0-4e_o, admitted when D0<=S-8e_o. Equation(7) leaves S-D0-8e_o without renewing a child certificate. The d5,k4,m2,D0=e_o fixture has S11/32, first4/32, oldD0=1/32, B6/32 and guaranteed2/32 left after both shared payments and early guard queries.

## 5. Honest next line

The THIRD shared query sees a twice-conditioned threshold, whose Fourier coefficients no longer obey the adjacent equality used in(1). A uniform replacement for that exact product-sum identity, together with genuine edit/physical influence ownership, is not proved here. Separators after a biased cofactor, arbitrary carriers, arbitrary-root unused-donor eligibility, full core/terminal FEI certificates and reference conversion also remain unpaid. Full FEI remains OPEN. NEXT is the third distinct nonseparator query after these TWO actually paid transactions, with the same original K and old debits, not a restarted threshold or a new root certificate.
