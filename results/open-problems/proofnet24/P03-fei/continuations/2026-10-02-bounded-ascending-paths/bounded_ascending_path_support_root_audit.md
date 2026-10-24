# Root audit of bounded-path support FEI

2 October 2026 UTC. **PASS within the stated class.** I read the complete
original candidate, final proof, author implementation, independent heat
implementation and full independent analytic audit. I rederived the
argument, supplied the sharper minority-entropy estimate and cotangent
constant, and reran both implementations successfully after the final
changes. This is internal verification; historical novelty and external
review remain unverified. General Boolean FEI remains open.

## Normalization and operator argument

For normalized cube inner product, adjacency A and L=(nI-A)/2 have Walsh
eigenvalues |S|. Consequently physical flip influence equals
<f,Lf>=4<1_E,L1_E>=2[np-<1_E,A1_E>]. Each undirected boundary edge
contributes 2/2^n to physical influence. The scripts verify this against
the exact unnormalized integer Walsh transform.

The raising operator's rank-s block has norm sqrt((s+1)(n-s)), so its
whole norm is at most (n+1)/2. Compression to E retains only paths all of
whose vertices belong to E. A k-vertex path bound therefore means U_E^k=0,
not U_E^(k+1)=0. The restriction concerns contiguous cube-edge paths and
does not assert a bound on arbitrary inclusion chains. Either label can
be used; it need not be the minority.

I checked the full defect-operator dilation independently. For a
contraction T with T^k=0, D=(I-T*T)^(1/2) and
Vh=(Dh,DTh,...,DT^(k-1)h) give V*V=I by telescoping, and VT=BV for the
backward k-shift. No commutation of D with T is needed. Phase-conjugated
Hermitian parts of B have path eigenvalues cos(j*pi/(k+1)). Thus the
credited Haagerup--de la Harpe inequality w(T)<=||T||cos(pi/(k+1)) gives
||A_E||<=(n+1)c, c=cos(pi/(k+1)), and

    I(f)>=2[n-(n+1)c]p.

The primary published operator theorem was checked in the Geneva author
archive. The self-contained dilation is included in the full proof; the
classical operator result is not claimed as new.

## Sharpened entropy and dimension-free constant

For minority density r>0, the nonempty Fourier mass is q=4r(1-r).
Splitting off the empty atom gives H<=h2(q)+qn. Put R=log2(1/r)<=n.
When r<=1/4, h2(q)<=q[log2(1/q)+log2(e)]<=qR<=4rR because
4(1-r)>=3>e. When r>=1/4, use h2(q)<=1<=4r<=4rR.
These estimates include q=1 by continuity and prove H<=8nr.

Poincare gives I>=4r(1-r)>=2r. Write
n_*=(1+c)/(1-c)=cot^2(pi/(2(k+1))). For n<=n_*, H/I<=4n<=4n_*.
For n>=n_*, d_n=n-(n+1)c is positive with d_(n_*)=1, and
H/I<=4n/d_n, whose derivative is -4c/d_n^2<=0. The final bound is

    H(f)<=4 cot^2(pi/(2(k+1))) I(f).

This continuous maximization is a valid upper bound for integer n. For
k=1, c=0 and the exact energy is I=2np, giving H<=4I. A singleton has
nonempty spectral masses 4*2^(-2n), and its entropy/influence ratio tends
to 4. Thus the constant 4 is optimal for edge-free label supports.
This does not assert optimality of the general cotangent constant.

## Scope and checks

Every k-Sperner family satisfies the path condition, but the theorem also
covers thinned even-rank families with arbitrarily long skipped-rank
chains. A closed score band of width D with every weight at least a>0
allows at most floor(D/(2a))+1 vertices on any ascending path. Arbitrary
internal deletions preserve that bound. Signed nonzero weights can be
flipped; zero weights with arbitrary internal decisions are excluded.
No strong I-Var estimate or unrestricted composition theorem follows.

The author rerun passed 65,814 exhaustive supports, 368 further families,
172 explicit nilpotency checks, 128 band rounding checks and singleton
dimensions through 512. The independent heat rerun passed 66,060
supports, 74 compressed-matrix checks and 27 general nonnormal dilations.
Both use exact integer Parseval/influence/path identities. Fourier
entropy, eigenvalues and dilation numerical tests are supplements with
declared tolerances, not exact arithmetic proof of logarithmic statements.
The full analytic argument establishes the unbounded theorem.

The entire primary Shalev extremal-classes introduction and theorem
statements were checked at arXiv:1806.03646v2 (24 January 2019); those
small-influence, high-entropy and spectral-norm subclasses do not by
themselves verify this exact bounded-path assertion. That limited
comparison is not a novelty certificate. The June 2026 primary FEI
continuation and Han's December 2024 article still formulate general FEI
as a conjecture; this result leaves it unresolved.
