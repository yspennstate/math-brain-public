# Independent whole-claim review of A006 v1

Verdict: **HOLDS at the stated scope; no repair supplied.** Reviewed statement SHA256: `7e7317fec14ec08f79bad0d58f97d00f9b8f632634d84aca4509375a674ab5c5`. Review concerns A006-SUNFLOWER-POSTERIOR-FOREST-PAYMENT@1, not its later majority result. No author checker was imported or executed. The reconstruction uses generic assignment enumeration, source SCCs, incoming parent choices, attachment choices and chronological queue traces, rather than enumerating the author's already classified stars.

## Source interface and Boolean law

The full source forests.tex was read, particularly eq:forestpacking, eq:forestconditioning, eq:forestcost and thm:posteriorforest. The child-label probability is lambda_child, not uniform neighbor probability in a different queue. Actual partition runs select disjoint nonempty subsets, visit every used gate once, and have one representative root per source SCC. The conditioned root probability for a prescribed nonempty root set is product(lambda_l*pi_l)/D, D=product(1+lambda_l*pi_l)-1. Infinite/failed runs do not enter output mass. The finite posterior identity follows from KL after summing each actual run only once; the B optimizer and actual-probability optimizer need not coincide.

For A006's function, direct expansion f=x0-(1+x0)product_i(1-x_i)/2 gives squared masses P(empty)=4^-m, P({0})=(1-2^-m)^2 and P(T)=P({0}+T)=4^-m for nonempty private T. Edge counts give I0=1-2^-m, Ii=2^-m, I=1+(m-1)2^-m. Thus v=1-4^-m. With lambda=1/m, pi=1/4, a=2^-6/5, D=(1+1/(4m))^m-1, the normalizer is exactly Lambda+log2 Z=log2 D.

## Exhaustion of all actual partition forests

Every private coordinate i can be assigned only to gate i. If 0 is absent, all used gates are isolated source components, all are roots, and exactly one chronological run exists. Its residual B is t(log m+16/5): each gate contributes lambda label log m, root rarity 2, and private rank log2 2 times gamma=6/5.

If A={0}, assigning 0 to a gate r activates one vertex with no edges, giving exactly m distinct root events. Each B=log m+2.

If A={0}+T, the unique gate owning 0 reaches every other used gate. Other gates own private singletons and have no outgoing edges. Thus the unique source vertex must be the root; no alternative parent or attachment is possible. When the owner r lies in T it owns {0,r}; there are t root choices and (t-1)! distinct child-label draws, for t! actual chronological runs. Their B=t log m+2+(6/5)(t-1). When r lies outside T it owns {0}; there are m-t root choices and t! child sequences, for (m-t)t! runs. Their B=(t+1)log m+2+(6/5)t. All children attach at 0. A permutation of the child labels changes the chronological random draws and is a genuinely different event. Root ordering is fixed and supplies no extra factorial.

This exhausts all assignments and all source-SCC forests for every m, not just the finite checked dimensions. Summing formal residual weights gives

    S_B({0})=1/4,
    S_B(T)=a^t/(4m)^t,
    S_B({0}+T)=t!*a^(t-1)/(4m^t)*(1+(1-t/m)*a).

The posterior proportional to these run weights is the exact finite B optimizer.

## Complete 43/10 residual assembly

Insert the preceding sums into v log D+sum_nonempty P(-log S_B). Pair private T and common+T to obtain exactly

    R=v log D+2(1-2^-m)^2
      +4^-m sum_{t=1}^m binom(m,t)
        [2t log m+(22/5)t+4/5-log(t!)-log(1+(1-t/m)*a)].

Product expansion gives D>=1/4. Also D<exp(1/4)-1<1/3; the last inequality follows by comparing the exponential series with the geometric series at 1/4. Hence log D<0. The two posterior correction terms in square brackets are nonpositive. Their removal is used only to obtain an upper bound. Binomial identities give the rare contribution <=2^-m[m log m+(11/5)m+(4/5)(1-2^-m)]. Since log m<=m, it is <=2^-m[m^2+(11/5)m+4/5]. This equals 2 at m=1 and 23/10 at m=2; for P(m)=m^2+(11/5)m+4/5, 2P(m)-P(m+1)=m^2+m/5-12/5>=0 for m>=2. Thus all m have rare contribution <=23/10. The singleton contribution is <=2, proving R<=43/10<=43I/10.

Conversely every deterministic common-singleton witness costs log m+2; every other B is nonnegative. Since log D>=-2, deterministic R is at least (1-2^-m)^2(log m+2)-2v, diverging while I tends to one. This is an obstruction for that fixed representation and point-mass posterior, not FEI or other references.

## Actual conditioned run probabilities and the 23/2 chain

The prescribed root mass is (1/(4m))^k/D. At a singleton subset, local weights are 1 and a with normalizer 1+a and size probability 1/2. At the doubleton, subset probability is one and size probability 1/6. Every leaf additionally chooses child count zero with probability 1/2. A root with t-1 children in the inside case chooses count t-1 with probability 1/[t(t+1)] and the all-0 attachment multiset with probability 1/t, because the selected subset has size two. An outside singleton root has t children, with count probability 1/[(t+1)(t+2)] and only one attachment multiset. Each child draw costs 1/m. Multiplying and summing the already counted distinct chronological traces proves

    W({0})=1/[16(1+a)D],
    W(T)=D^-1*[a/(16m(1+a))]^t,
    W_in({0}+T)=t!/[24D t^2(t+1)m^t]*[a/(4(1+a))]^(t-1),
    W_out({0}+T)=(m-t)t!/[8D m^(t+1)(1+a)(t+1)(t+2)]
                         *[a/(4(1+a))]^t/(1+a).

The code independently verifies these formulas by sequential multiplication. Algebraic a has a^5=1/64 and 2/5<a<1/2 by exact fifth powers; the rational auxiliary evaluations are identities checks, not an assertion that a itself is rational.

For the all-m bound use a<1, 1/a<4 and (1+a)/a<5. The dominant cost is <log(32/3)<4. Private cost is <=t log(80m)<=t(m+7). Inside-root mass alone gives common cost <=5+3m+t(m+5): drop the favorable factorial and negative log D; use log24<5, log20<5 and log(m+1)<=m. Summing the two rare sectors gives <=2^-m(m^2+9m+5). This is <=15/2 for all m: the initial value is 15/2 and 2Q(m)-Q(m+1)=m^2+7m-5>=0 for m>=1. Therefore the complete nonempty run-cost optimum is <=23/2<=23I/2. Entropy inference must still include h2(v).

Finally the stated scale weights 1/[(k+1)(k+2)] telescope to one; every lambda_i=2^-k/m is feasible. Mixing complete conditioned references preserves subprobability. Selecting k=0 pays log(1/w0)=1 bit under each nonempty spectral mass, namely v<=I here. The resulting 53I/10 and 25I/2 bounds follow. Each selected scale retains its own normalizer and all run terms.

## Independently executed exact checks and scope

The frozen checker covers integer Walsh truth tables m=1..8 and all generic partition-forest choices m=1..5. It deduplicates chronological run keys, verifies symbolic residual-weight polynomials in a, and reconstructs actual draw probabilities with Fraction arithmetic at a=2/5 and 1/2. Total actual forest counts for m=1..5 are 3,11,37,143,681. It passed 4,260 recorded assertions in 0.193 seconds; the saved counter excludes the final runtime assertion. out/REVIEW_A006_CHECK.json contains the counts and the independently recomputed source statement hash.

This supplies the whole A006 v1 review requested by the lead, without repair or contribution to the original claim. A094 had independently accepted the same result; this reconstruction is an additional locally saved review, not a shared-registry change. The full universal posterior-cost endpoint remains open, and arbitrary-repeat/overlapping-subset successful runs are outside the exact optimization reviewed here.
