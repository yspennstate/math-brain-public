# Shared-core exposure criterion (all dimensions)

Let g be Boolean, a=1-Eg, and let C be any indicator independent of g with EC=q. At a node querying a coordinate of a fresh point activation A_l, the two children are

    f0=1+C(g-1),
    f1=1+[C+(1-C)A_(l-1)](g-1).

Put rho=2^-(l-1) and d=a rho(1-q)/2. Fourier labels involving a nonempty subset of the l-1 remaining activation controls have one zero child coefficient, so their parent erasure is twice their mismatch mass. The fraction of squared point-indicator mass on its empty Fourier label is rho. Thus these labels contribute exactly 2(1-rho)d. The other labels have total mismatch rho d and total packet mass at most one, so entropy concavity bounds their contribution by h2(rho d). Therefore

    B/d <=2(1-rho)+rho log2(e/(rho d)).

If a(1-q)>e/8, then rho d>e rho^2/16 and

    B/d <2+2rho[1+log2(1/rho)] <=4.

The last inequality is exact for dyadic rho=2^-j: 2^-j(1+j)<=1 for integers j>=0 (equality j=0,1). This is a measurable conditional exposure criterion on the actual physical node; it does not assume a minority law is signed disagreement.

For two point events with exclusive widths r,t>=1, q=2^-t<=1/2. Every shared bent-selector core with even k>=4 has a>=11/16. Hence a(1-q)>=11/32>e/8, since e<11/4. This proves strict threshold-4 goodness for every first-event control node, uniformly in r,t,k. After the first event fails, querying the second is a constant-child point activation. Common-control queries before the union are also constant-child point activations.

For the latter nodes, at arbitrary conditional deficit d in [0,1], the exact constant-child Fourier packet formula is Jsgn=d-d^2+d^2log2((1-2d+2d^2)/d^2), and B<=Jsgn+c d. Thus B/d<=1+c+2d log2(1/d)<=1+c+2c/e<4. Endpoints d=0 contribute zero. The rational constants c<81/56, e>65/24 prove the strict bound. No A021 remainder sign occurs anywhere.

Every physical control coordinate is queried at most once on a path; common controls have one account, exclusive controls charge only their surviving disagreement, and the shared core has one terminal account. With u=2^-s, beta=p+q-pq, p=2^-r, q=2^-t, the exact partition is

    I_ctrl=u a[s beta+r p(1-q)+t q(1-p)],
    I_leaf=u beta I(g), H_leaf=u beta H(g).

No-control bad-node odd-face credit is EXACTLY zero for this stopping tree. The full entropy/mismatch ledger has

    sum w B <=4 I_ctrl,
    H(F)<= (4+2/ln2) I_ctrl+u beta H(g),
    sum w Jminor+u beta H(g)<=4 I_ctrl+u beta H(g),
    sum w(Jminor+3mu/ln2)+u beta H(g)<9 I_ctrl+u beta H(g).

The mismatch bounds follow from Jminor<=B and mu<=d. The entropy bound uses the exact decrement B+JS with JS<=2d/ln2. Terminal entropy is retained; arbitrary g is not certified merely because a is in the exposed range. For a bent/point-flip selector core, H(g)/I(g)<3 by the elementary support/edge bound, yielding H(F)<7I(F), J+terminal<=4I(F), full sufficient ledger<9I(F).
