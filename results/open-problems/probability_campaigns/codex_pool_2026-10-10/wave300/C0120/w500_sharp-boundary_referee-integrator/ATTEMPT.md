# C0120 referee attempt and boundary

## Exact source target

The cited Chatterjee paper arXiv:0810.4221 defines independent standard Gaussian vertex weights on the positive quadrant and the maximum M_n of the sums along all n-vertex up/right paths starting at the origin with free endpoint. Its Theorem 8.1 proves Var(M_n) <= C n/log n. Section 12(3) asks to improve the fluctuation exponent but gives no explicit epsilon or quantifier. A precise *operational* power target is: find constants epsilon>0 and C<infinity such that Var(M_n)<=C n^(1-epsilon) for all n>=2. This formulation is mine, not a verbatim source statement. Present-day openness remains UNKNOWN.

The intake's target Var(log Z_n) for general dimensions changes both observable and domain. That source citation cannot support those extensions. Graham, arXiv:0909.1352, proves an O(N/log N) bound for fixed-endpoint Gaussian directed last-passage percolation in arbitrary dimension; it does not establish the requested power improvement for this source model. Basu--Sidoravicius--Sly, arXiv:2604.01214, obtains a power improvement for a rotationally invariant Riemannian FPP class, a distinct model. This bounded source search is not a proof of current openness.

## Independent rederivation of the hardest peer claim

In the width-one strip from (0,0) to (r,r), each diamond has two possible intermediate vertices. Its maximizing path is determined by r independent signs of D_k=(X_k-Y_k)/sqrt(2). Under the source's Ornstein--Uhlenbeck perturbation with time s, each sign pair has correlation rho=e^-s. Writing the perturbed difference as rho D_k+sqrt(1-rho^2)Z_k, the isotropic Gaussian vector (D_k,Z_k) has uniform polar angle. The disagreeing angular sectors total 2 arccos(rho), so q(s)=arccos(e^-s)/pi. Independent diamonds give Bin(r,q) mismatches exactly.

The paths always share the r+1 diagonal junctions. If B diamonds disagree, they share 2r+1-B vertices. For s=r^-alpha, 0<alpha<2, q(s)~sqrt(2)/pi r^(-alpha/2). Thus r q(s)->infinity while q(s)->0. The probability of identical paths, (1-q)^r, tends to zero; their expected shared fraction, 1-rq/(2r+1), tends to one. The path maximum has exact variance (2-1/pi)r+1. Therefore high-probability path *change* alone cannot force a power variance upper bound. This is a counterexample to that auxiliary implication only.

## Hardest open piece

The source's overlap identity needs a polynomial reduction in *expected common-vertex overlap* at a suitable noise scale for the unrestricted planar model, or another route to a power upper bound on Var(M_n). Neither peer establishes this. The Gaussian layer-mean decomposition isolates an H_n variance floor, but provides no upper bound on the centered residual maximum. A fixed-width path family has linear common-mode variance and cannot stand in for the unrestricted family.

No new lemma of mine is asserted. The checked peer results are partial. A KEEP in REVIEW_ROWS.jsonl is a mathematical verdict with served-model identity pending coordinator verification; it is not final promotion or a parent-problem solution.
