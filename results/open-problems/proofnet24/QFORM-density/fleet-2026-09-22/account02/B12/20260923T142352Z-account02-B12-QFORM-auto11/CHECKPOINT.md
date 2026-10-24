SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T14:23:52Z.
attacking: approximate invariant-subspace shielding for arbitrary-magnitude internal spectral updates plus a genuinely dense small tail.

# Early substantive checkpoint

Let A be symmetric on P\oplus Q coordinates in block form A=[[C,F^T],[F,D]], with ||D||op<=b<a and ||F||op<=eps. For Pi_+=1_[a,infty)(A), X=Q Pi_+ satisfies the exact Sylvester equation D X-X A_+=-F P Pi_+, where A_+ is A restricted to ran Pi_+. Since spec(D)\subset[-b,b] and A_+>=a, the separated-spectrum integral gives ||Q Pi_+||op<=eps/(a-b). Applying the same argument to -A gives ||Q Pi_-||op<=eps/(a-b) for Pi_-=1_(-infty,-a](A). Orthogonality of Pi_+,Pi_- then gives

||Q Pi||op <= sqrt(2) eps/(a-b),  Pi=1_{|A|>=a}.

Hence if max_i P_ii<=mu, then sqrt(Pi_ii)<=sqrt(mu)+sqrt(2)eps/(a-b). The P-block C is completely unrestricted: arbitrary rank/sign/norm internal spectral additions cost nothing. For a reference B with ||Q B Q||<=beta, ||Q B P||<=eta, and arbitrary dense T with ||T||op<=delta, apply this to A=B+T with b<=beta+delta and eps<=eta+delta, provided beta+delta<a.

This is the intended new B12 theorem; the remaining work this run is to compile it into an actual QFORM density inequality, give an exact target-class family, and consume the pinned e5f D5 theorem plus the latest account03/B12 eroded-profile theorem at explicit inequalities.
