# Independent reconstruction of A055 singleton reserve

Source claim: A055-SINGLETON-CRITICAL-RESERVE@1; statement SHA256 bfc2c09293d9446e7301b5c562668288de096d6758459530ec93bf1db80c09bf. Source: A055/runs/20261014T004129Z-account05-A055-extremal-obstruction-referee/PROOF.md, SHA256 f2a51364d89525182f1a0cb937d711baf6b1ee13cb4c73cc34028b1a7a09da0a. Reviewer A051 supplies no repair. Verdict: HOLDS at the complete stated analytic scope; the source finite assertion total is not adopted merely by reading its report.

For each paired Fourier row (a,b) define q=a^2+b^2, e=min(a^2,b^2)/q. Directly expanding the two physical amplitudes a+b,a-b gives c=4e(1-e), hence 2e<=c<=4e on [0,1/2]. The one-bit phase has deterministic spectrum; its distance from the spectral pair is exactly e, including ties, whichever phase is selected by the zero convention. Direct character enumeration below independently checks this.

The row channel is relative entropy of the two physical density values 1 plus/minus 2ab/q. Its even power series is j(c)=(1/ln2)sum_(k>=1)c^k/[2k(2k-1)]. The coefficients are nonnegative and sum to 1 at c=1, so j(c)<=c. Concavity of binary entropy, beta<=C/2<=1/2, and monotonicity of h2 on that interval yield B+J<=h2(C/2)+C.

For the sharper row payment, compare the series to 1-sqrt(1-c). The latter coefficient is binom(2k,k)/(4^k(2k-1)); induction gives binom(2k,k)/4^k>=1/(2k). Since 1-sqrt(1-4e(1-e))=2e, j(c)<=2e/ln2. The endpoint is admitted by monotone convergence, not a truncated numeric series.

Keep S=-E D_K(child) as defined even on a noncritical root. Direct restriction averaging gives D+S=L-K Inf_i. Subtract beta from Inf_i and rearrange to D+S+K(Inf_i-beta)=sum q[h2(e)+j(c)-K e]. Thus the orientation is nonnegative but S is nonnegative ONLY after the correct minimality hypothesis. Jensen and the row bound give h2(beta)-(K-2/ln2)beta.

For an independent reconstruction of the last maximization, let p=1/(1+2^t). The exact Gibbs identity is h2(x)-t x=log2(1+2^-t)-D(Bern(x)||Bern(p)). Relative entropy is nonnegative, proving the claimed bound on the enlarged interval [0,1]. This also handles t<0 without accidentally assuming beta can exceed 1/2. Log2(1+u)<=u/ln2 follows by integrating 1/(1+u)<=1. These prove the analytic exponential reserve.

Our independent checker uses direct character sums rather than A055's helper, derives physical child entropies and influences separately, and retains their exact signed deficit. It checks all 276 tables through three bits, 804 singleton cuts, and K=2,4,8,16. The finite exponential comparisons use the proved relaxation 2/ln2<3; the sharp transcendental exponent is established analytically, not by those checks. All 48 singleton cuts of the sixteen three-bit K=2 violations have certified nonpositive smaller-child deficits. No K>=4 violating example is manufactured or claimed.

Downstream: accept the singleton reserve as a real constraint on dimension-minimal witnesses, not as a lower bound on their deficit. The two-bit extension in TWO_BIT_RESERVE.md uses a different phase classification and known two-bit influence margin. Neither theorem supplies a uniformly paid block or permits dropping terminal entropy.
