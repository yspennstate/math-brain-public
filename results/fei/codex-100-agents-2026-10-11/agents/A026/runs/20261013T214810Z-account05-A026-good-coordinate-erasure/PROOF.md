# A026 stage 3: intact-encoder erasure under biased physical history

Bit entropy is used throughout. Define Phi(a,b)=(a+b)log2(a+b)-a log2(a)-b log2(b), continuously at zero. The universal existential erasure target remains open. A003's stage-2 balanced-substitution identities and maximum-influence obstruction are source inputs, not new results here. The new step is a selection bound valid after histories that bias other blocks, and a paid multi-query prefix with explicit terminals.

## 1. Universal intact-block bound

Let f(z,r) be an arbitrary Boolean sign function, with z one input and r any other physical inputs. The rest may already be an actual restricted function; no balance or encoder structure is required there. Write

A(r)=(f(+1,r)+f(-1,r))/2, D(r)=(f(+1,r)-f(-1,r))/2.

Then A,D take values in {-1,0,1}, A D=0 pointwise, and A^2+D^2=1. Put delta=E D^2, the physical influence of outer z. Replace z by a balanced odd Boolean encoder g on a fresh block. Odd means g(-x)=-g(x), so its Fourier support consists only of odd-degree sets. For an inner coordinate i put gamma=ghat({i}) and d=I_i(g). Let F(x,r)=A(r)+g(x)D(r). Direct edge counting gives I_i(F)=delta d.

For an inner remainder V nonempty, adjacent encoder Fourier indices have opposite parities, so at most one coefficient occurs; such packets have zero erasure. At V=empty the inactive/active packets are Ahat(T) and gamma Dhat(T). Thus, **for every actual Boolean rest r**,

B_i(F)=sum_T Phi(Ahat(T)^2,gamma^2 Dhat(T)^2).                 (1)

This is the already known balanced odd-encoder packet formula, now used without requiring the remaining physical rest to be balanced. Concavity and homogeneity of Phi (equivalently the log-sum inequality) imply

sum Phi(a_T,b_T)<=Phi(sum a_T,sum b_T).

Parseval and pointwise orthogonality give sum Ahat^2=1-delta, sum gamma^2 Dhat^2=gamma^2 delta. Since gamma^2<=1, their total is <=1. The elementary bound Phi(a,b)<=b log2(e(a+b)/b) therefore yields the new robust selection majorant

**B_i(F)/(delta d) <= (gamma^2/d) log2(e/(gamma^2 delta)).**     (2)

When delta=0 the coordinate is irrelevant and omitted; when gamma=0 erasure is zero. Formula (2) holds after arbitrary histories outside the intact encoder block. It neither assumes FEI for the rest nor discards its entropy. It cannot be applied as if the encoder stayed balanced after a query inside that block.

For an odd majority encoder on M=2R+1 inputs, gamma=d=rho=binom(2R,R)/4^R. Then (2) becomes rho log2(e/(rho^2 delta)). This is a simpler, slightly weaker scalar bound than A003's root bound, but its actual-rest formulation survives bias in other encoders.

## 2. Biased sliced encoder: exact correction retained

If a fresh inner Boolean encoder h has mean mu, singleton coefficient gamma and influence d, the same expansion gives

B_i(A+hD)=delta[B_i(h)-Phi(mu^2,gamma^2)]
             +sum_T Phi((Ahat(T)+mu Dhat(T))^2,gamma^2 Dhat(T)^2). (3)

This is a specialization of the A056/A057 coherent biased interface, not advertised as a new general composition identity. The inherited inner B_i(h) and the negative empty-row subtraction are both essential. Orthogonality still gives sum(Ahat+mu Dhat)^2=1-delta+mu^2 delta. Parseval for h gives mu^2+gamma^2<=1, so the collision pair's total mass is at most one, and the collision part is at most gamma^2 delta log2(e/(gamma^2 delta)). Consequently a valid but looser upper bound is B_i(h)/d plus the right-hand scalar term divided by delta d. That inherited price is not removed by the intact-block argument.

After one query in odd majority, the two slices are isospectral and each has mean +/-rho. Every other coordinate has influence rho and singleton coefficient rho: the parent's even-degree coefficients vanish. For the small Majority3 validation, each slice has B_i=1, d=1/2, mu=+/-1/2 and gamma=1/2. A later selection cannot silently reuse B_i(g)=0 on such a slice.

## 3. New history-robust prefix calibration on A003's bad-maximum family

Let k>=4 be even, delta0=2^-k, s=sqrt(delta0), p=delta0^2. Use the accepted sparse bent one-point surgery outer function from B05/A003, with m=3k background inputs and retained selector y. Its uniform influences are

alpha_data=p u, u=1/2+delta0;
alpha_control=p A0, A0=1-s+delta0;
alpha_y=p delta0;
I_outer=p[k u+2k A0+delta0].

Every background alpha lies in [p/2,p], and W=u+2A0=5/2-2s+3delta0<=5/2. The selector erasure ratio is at least (1-delta0)(k-2); this is the existing B05 lower bound consumed by A003. We do not re-prove or generalize it at biased nodes.

Use larger odd majority encoders than A003's root calibration:

**R=k^2 2^(2k+2), M=2R+1, rho=binom(2R,R)/4^R.**

The central-binomial recurrence proves rho<=1/sqrt(R+1)<delta0/(2k). Indeed, if rho_(R-1)^2<=1/R, then rho_R^2<=[(2R-1)/(2R)]^2/R<=1/(R+1), since (4R^2-4R+1)(R+1)<=4R^3. Also M rho>=1: the central binomial probability is largest among M binomial probabilities summing to one. M>=64.

Consider any adaptive physical prefix that queries at most one input in each majority block, never queries y, and stops no later than one query in all m blocks. If q blocks have been queried, their encoder means are +/-rho, independently under the actual remaining uniform physical measure. Untouched block outputs are balanced. Thus, for any outer derivative or selector boundary event, the induced product-bias density relative to the original uniform law is bounded between

(1-rho)^q and (1+rho)^q.

For a background j the derivative event does not depend on its own output; the same bounds remain valid even if its own block is touched. Write alpha_j^mu for its actual derivative mass. Every remaining encoder coordinate has inner influence rho (both intact and one-query slices), hence physical influence rho alpha_j^mu. In particular an untouched block obeys

alpha_j^mu >=(1-rho)^q p/2 >=(1-q rho)p/2 >=29p/64>p/4,

because q<=3k and q rho<3delta0/2<=3/32. This lower bound is for the actual induced measure, not a uniform outer spectrum reused at a biased node.

### Cheap intact-coordinate price

For every coordinate in every untouched block, (2) gives

B_i/I_i <=rho log2(4e/(p rho^2)).

The function x log2(C/x^2) increases for 0<x<=delta0/(2k) and C=4e/p: its derivative is log2(C/x^2)-2/ln2>0, since C/x^2>e^2. Evaluate at x=delta0/(2k), use log2(2k)<=k and log2(e)<3/2:

B_i/I_i <delta0/(2k)[4k+2log2(2k)+2+log2 e]
          <=3delta0+7delta0/(4k) <= **55/256** <1.             (4)

The logarithm inequality follows from 2k<=2^k for k>=4; log2 e<3/2 follows from ln2>2/3, already the first term of its positive atanh series plus a positive next term. Thus (4) is analytic for all even k>=4, not inferred from a scan.

### Half-average eligibility at every preterminal node

All background coordinates and y remain relevant: the induced output law has full support, so all positive derivative events retain positive probability. The number of relevant residual inputs is D=mM+1-q. Actual total influence is at most

I_node <=(1+rho)^q p[M rho kW+delta0].

For every untouched bit i,

2D I_i >=D rho p(1-rho)^q.

Therefore it suffices that

(D/M)[(1-rho)/(1+rho)]^q >= kW+delta0/(M rho).

The ratio power is at least 1-2q rho>=1-3delta0, by Bernoulli applied to (1-rho)/(1+rho)>=1-2rho. Also D/M>=3k(1-1/M), and M rho>=1. The difference between the left lower bound and right upper bound is at least

k[3(1-3delta0)-W]-3k/M-delta0
 =k[1/2+2sqrt(delta0)-12delta0]-3k/M-delta0.

On 0<=delta0<=1/16 the bracket is >=1/4 (concavity, endpoint values 1/2 and 1/4). With M>=64 and k>=4 this difference is >=13k/64-delta0>0. Hence **every untouched bit satisfies I_i>I_node/(2D)**. This is the original relevant-dimension G_(1/2) cutoff, including the actual biased history.

### Weak regime and the maximum rule

(1+rho)^q<=1/(1-q rho)<=32/29. The selector influence is between (1-q rho)p delta0 and p delta0/(1-q rho). Every background influence is at most rho p/(1-q rho). Thus background/selector influence is <=[rho/delta0]/(1-q rho)^2 <(1/(2k))(32/29)^2<=128/841<1. The selector remains the unique maximum-influence coordinate throughout this prefix. All coordinates remain below 1/4. Its erasure price is known to diverge at the root; its price at later biased nodes is **not** claimed to retain that lower bound. The policy picks cheap eligible intact-block bits rather than asserting that a maximum-influence bit is cheap.

The source total influence still vanishes. Since M rho<=2sqrt(R)+1/sqrt(R)=4k/delta0+delta0/(2k),

I_root<=10k^2 delta0+(9/4)delta0^3 ->0.

At every prefix node the corresponding upper bound is multiplied by at most 32/29. No huge truth table is needed for these all-k statements.

## 4. Prefix payment, with every terminal retained

The exact baseline entropy decrement is Delta_i H=H(F)-[H(F_+)+H(F_-)]/2=B_i(F)+J_i(F), with 0<=J_i(F)<=(2/ln2)I_i(F). The influence decrement is I(F)-[I(F_+)+I(F_-)]/2=I_i(F). These are B06 R2, consumed at their stated actual-physical-restriction scope, not re-advertised as new identities.

The policy can pick the least-index intact block and any of its bits, or adapt among intact blocks using physical history. It queries one bit from each of the 3k blocks and then stops. At every queried preterminal node, (4) pays true erasure at K0=55/256. The already established physical influence telescope therefore gives

sum_v w_v B_(i_v)(F_v) <=K0 [I(F_root)-E I(F_leaf)],

H(F_root)<=E H(F_leaf)+(K0+2/ln2)[I(F_root)-E I(F_leaf)].       (5)

We use the recovered telescope and JS bound; we do not claim their reconstruction as a new result. Formula (5) leaves actual terminal entropy in full. It is not a complete tree bound or a proof of FEI. Terminal majority slices are biased and all blocks are touched; (1)-(2) no longer offer an intact block. Their inherited inner-erasure terms in (3), and the retained outer-core entropy, are the first unpaid part.

## 5. Relation to the prior pair-entropy experiment

The previous A026 stage computed conditional pair entropy exposed by a zero-erasure query. For recursive majority such queries are genuinely free. In a composition with a positive outer edge, a query inside an odd encoder may already have nonzero erasure from its empty/singleton collision (1). This stage pays those first collisions rather than presuming every such query is free. It shows that the first loss of balance in other blocks need not destroy selection; it does not extend the zero-erasure identity to a nonzero-erasure node.

## 6. Exact first unsupported line

The universal missing step is a common-budget selection/payment on the terminal biased blocks of (5), retaining the inherited B_i(h), signed empty-row corrections and all outer-core entropy, without assuming FEI for that outer core. The scalar majorant (2) is valid for any actual rest but has log(1/delta); no universal bound follows if an unrestricted derivative delta is arbitrarily small. The favorable lower bound and G_(1/2) eligibility are proved only for the specified history/family. Root transitivity and finite passing cases are never promoted to hereditary universal assumptions.

The next action is to derive a signed reserve for a **second query in a previously touched encoder block**, using (3) and the actual terminal entropy. This is the first node where the reusable intact-block payment is unavailable. Testing that reserve against an arbitrary outer Boolean seed, not only the already-paid B05 core, is the shortest step toward C018/C019.
