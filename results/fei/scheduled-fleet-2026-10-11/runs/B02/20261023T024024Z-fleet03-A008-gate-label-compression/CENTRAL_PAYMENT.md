# Compatible root aggregation at the central threshold frontier

All logarithms below are base two. Fix k>=1, m=2k, two disjoint m-bit blocks X,Y, and F=2[|X|>=k][|Y|>=k]-1. Its complete positive prime table consists of the N=binom(m,k)^2 conjunctions of k positive variables in each block. Every width is W=m. Fix lambda=1/N, pi=2^-W, and any one full physical order on each prime, before sampling any spectral set. Packing holds since each coordinate belongs to N/2 primes. Use exactly the conditioned queue in forests.tex, not a retuned reference. Write D=(1+pi/N)^N-1. The conditional probability of exactly a root set R is (lambda*pi)^|R|/D. Since pi<=1/4, pi<=D<=exp(pi)-1<=2pi.

For s selected coordinates at a visit, zero children, and an arbitrary specified subset B, the exact visit probability is

    V_e(B) = prod_{i in B} theta_s^e(i) / [2s(s+1) Z_s^e].

Thus child-count zero is paid, the attachment multiset is uniquely empty, and there are no child names. Every event below visits each named gate once and outputs the union of its explicitly selected subsets.

## Good sets: aggregate names before taking logarithms

For A nonempty put a=|A cap X|, b=|A cap Y|, d=a+b. Call A good if a,b<=k. There are

    G_A=binom(m-a,k-a) binom(m-b,k-b)

compatible prime names. Sum the actual one-root, zero-child event for EVERY such prime, selecting exactly A. These are distinct runs, not multiple descriptions of one run. Their total mass Q_good(A) is

    (lambda*pi/D) sum_{e contains A} V_e(A).

The compatible fraction G_A/N equals binom(k,a)/binom(m,a) times binom(k,b)/binom(m,b), and is at least (2e)^-d. Indeed binom(k,a)>= (k/a)^a and binom(m,a)<= (em/a)^a for a>0, with the a=0 factor equal to one; similarly for b. Since rank<=W, theta_d(i)>=(d/W)^(6/5), while Z_d<=(6e)^d by the original subset-normalizer lemma. Consequently

    Q_good(A) >= (d/W)^(6d/5) / [4d(d+1)(12e^2)^d],
    -log Q_good(A) <= (6/5)d log(W/d)+11d.                 (1)

Here 2+log(d(d+1))<=4d and log(12e^2)<7. All root-name and rarity factors, including absent roots and nonempty conditioning, are present in the sum. Equivalently the posterior on compatible runs is proportional to their original event masses; its entropy refunds interchangeable names. Decoding simply reads the root label and subset and outputs A. The final output ambiguity is exactly the sum over those distinct names, rather than an omitted cost.

## Bad sets: a paid two-root fallback

Fix e0 containing the first k variables in each block and e1 containing the last k in each block. Their supports are disjoint and cover all 2m coordinates. If A is bad, it has more than k coordinates in at least one block, so both B0=A cap e0 and B1=A cap e1 are nonempty. Select exactly roots e0,e1, select these two owned subsets, and select zero children at both visits. This is a genuine partition forest: the ownership graph has two isolated source components. Its exact mass is

    Q_bad(A)=(lambda*pi)^2 V_e0(B0)V_e1(B1)/D.

For every 1<=s<=W, a coarse bound on a specified visit is V_e(B)>=2^-4W. To see this, Z_s<=binom(W,s)<=2^W, prod theta_s>=(s/W)^(6s/5), and log[2s(s+1)]<=1+2s. The inequality s log(W/s)<=log(e)(W-s), together with (6/5)log(e)<2, gives -log V<=W+1+2s+2(W-s)=3W+1<=4W. Therefore

    -log Q_bad(A)<=1+2log N+9W<=1+13m.                  (2)

There is no multiplicity refund in (2): it is one explicit run, both gate names and both root rarities paid. Since bad sets have d>=k+1, for ANY set law P,

    E_P[1_bad (-log Q_bad)] <=26 E_P d.                (3)

This follows pointwise from (1+26k)/(k+1)<26.

The union of good events and bad fallback events is a subcollection of one unchanged conditioned sampler. Events for different output sets are disjoint; one-root and two-root events are disjoint. Thus Q_sel(A), defined by the good sum or bad fallback respectively, is a subprobability, and Q_*(A)>=Q_sel(A) for every nonempty A. No post-observation reference change occurs.

## Exchangeable-law comparison and actual spectral payment

Suppose P is any law on subsets invariant under separate permutations of X and Y, possibly with an empty-set atom. Exact orbit decomposition gives

    H(P)=H(a,b)+E_P[log binom(m,a)+log binom(m,b)].

On good sets, binom(m,a)>=(m/a)^a gives d log(m/d)<=log binom(m,a)+log binom(m,b), including zero counts by continuity. Equations (1)--(3) imply the complete nonempty cross-entropy bound

    C_sel(P):=sum_{A nonempty}P(A)log(1/Q_sel(A))
                <=(6/5)H(P)+37 E_P|A|.               (4)

This is not an absorption argument for arbitrary Boolean functions: the entropy coefficient exceeds one. It is a comparison to an existing entropy payment for this symmetric frontier.

For the actual Fourier law of F, write g=2[|X|>=k]-1, a_k=binom(2k,k)/4^k, q=Pr(g=1)=(1+a_k)/2, and v_g=4q(1-q). Then I(g)=m a_k and I(F)=2q I(g). Splitting the spectrum into empty, left-only, right-only and both-block sectors gives masses (2q^2-1)^2, q^2 v_g, q^2 v_g, v_g^2/4. Within a nonempty block the law is the normalized nonempty spectrum of g; in the joint sector it is the product of two such laws. Hence

    H(F)=H(sector)+2q[H(g)-h2(v_g)]<=2+2q H(g).

The established threshold Theorem A gives H(g)<9 I(g). Moreover I(g)>=1: its initial k=1 value is one, and the adjacent ratio of k a_k is (2k+1)/(2k)>1. Since q>=1/2, I(F)>=1 and H(F)<=11 I(F). Separate exchangeability is automatic from block symmetry. Thus (4) proves

    C_*(F)<=C_sel(F)<=(251/5)I(F)<51I(F)              (5)

for every k>=1, every fixed full physical order per prime, under this same all-prime lambda=1/N queue. If an actual entropy code is desired, supplement the nonempty reference with empty mass 1-v and nonempty mass vQ_sel, v=Var(F); its cross entropy is h2(v)+C_sel(F)<= (261/5)I(F), using the standard h2(v)<=2I(F). This last binary branch is distinct from (5), which prices the original conditioned nonempty sampler.

## Scope and first unsupported line

This closes the central-band actual compatible-prime queue cost left open in A015's FRONTIER.md, with every name, root, subset, count and ambiguity factor retained. It is a coding result for a family whose FEI was already known by threshold composition. It proves neither uniform prime-forest payment for arbitrary f nor an arbitrary nonsymmetric analogue of (4). The first unsupported universal step is replacing exchangeable orbit entropy (and the external threshold entropy payment) by a dimension-free influence payment on arbitrary Boolean spectra, with one fixed original prime reference. No FEI disproof or universal theorem is asserted.
