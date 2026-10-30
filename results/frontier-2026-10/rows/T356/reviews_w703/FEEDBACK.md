Reviewer agent H, acting for agent D (agreed on the mesh 21 Oct 19:2x), 21 Oct 22:5x.

REVIEW: all nine latest claims PASS on their exact versions (T356/AUDITS_FROM_REVIEWER.tsv, one row each with the proof sha):
C008 v1, C004 v2, C002 v3, C005 v2, C007 v1, C003 v2, C009 v1, C001 v3, C006 v2. I redid each proof by hand and read the cited
passages (Fournier-Guillin p.2 examples (a),(b) and the Lipschitz remark; Ambrosio-Stra-Trevisan Thm 1.1). Your bundles may go to
the inbox as they are. Statuses in CLAIMS.jsonl stay yours to update from the audit rows.

Where Target 1 stands after the audit. Unrestricted it is false (C001 two atoms in d=1,2,3; C008 uniform square at h=1/n). It holds
for d>=5 with a q-moment (C004/C005), for Lipschitz-curve laws (C007), and on the bandwidth intervals of C006 for compact support in
d<=4. What is open, and what scores as NARROWED, is small bandwidth for regular laws in d=3 and d=4: there the empirical rate
n^(-2/d) is the truth for the uniform cube, so the target is not contradicted, but the dyadic method cannot see it (its coarse levels
already cost N^(-1/2) even for the uniform law).

NEXT, in this order (F check T356 "<route>" first, open it in ROUTES.jsonl):
1. Extend the label variance of C002 from cells to test functions: for bounded f, E(int f d(L_t-P))^2 <= int f^2 dP / N with the same
   N=n alpha, under each of the three protocols. If the cell proof uses only the indicator structure, say exactly where, and either
   generalize it or give the counterexample. Check it in exact arithmetic on small n for f = a cosine mode.
2. With that bound, run the Fourier argument of Bobkov-Ledoux (arXiv:1909.06193, the AKT matching theorem on the cube with Neumann
   cosines; read their statement and page before using it) on the labels: smoothing at scale eps plus the H^-1 bound against the
   uniform law. The target is E W2^2(L_t,Unif[0,1]^d) <= C N^(-2/d) for d=3,4 (d=4 may carry a log; record it if so). Then the
   triangle step of C006 gives Target 1 for the uniform cube at every bandwidth in d=3, and states exactly what d=4 gets.
3. Literature before claiming: search for recursive or dependent-sample versions of AKT/Bobkov-Ledoux (2019-2026) and record the result.
   The d=2 version only gives log n/n, which is the C008 rate and does not rescue the named target; record it, it scores nothing.
Then STATE: NEEDS_REVIEW with reviewer agent H.
