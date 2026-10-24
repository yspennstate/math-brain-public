# Root analytic audit of the rank-one/core-three matching-pair theorem

2 October 2026 UTC. **PASS for the stated family and marked pair types.**
Root read the entire final `forest_rank_one_core3_arbitrary_matching_proof.md`
and its complete exact verifier, independently rederived its sign arguments,
and reran the verifier with exit status zero. This is an internal analytic
audit, separate from historical novelty and outside review. This audit
does not assert negative association; that is a subsequent separate candidate.

The weighted three-core connectivity algebra is exact: pair mergers have
weights b_i b_j and two consecutive mergers have total2BJ, while the
triple merger has weightJ. Thus P²=2BQ, with all other nilpotent products
zero. The exponential Q coefficient gamma+Balpha²=x³/d reconstructs
the complete terminal transfer. Core enumeration gives the claimed S,L,J.
These transfers count every forest; no asymptotic series is being truncated.

For the other matching edges, deletion/contraction is the sum T(a)T(b)+
wT(a+b). Its normalized logarithmic coefficient is the branch average
of gamma plus B theta(1-theta)delta². Root independently calculated this
variance correction; its sign and factor are correct. With s=a+b,
delta=ab(2+Bs)/(da db ds). The bound delta<=a/(B da) reduces exactly
to1+Ba>=0, and similarly for b. The increasing function x/d(x) supplies
the contracted branch margin. Each branch's U/B-Gamma margin is at least
Bdelta², so it absorbs the mixture variance. Products add U,Gamma and
preserve0<=Gamma<=U/B. Nonnegative matching weights and zero unmarked
row activities require no illegal division.

For the selected disjoint pair, contraction replaces row weights a,b by
a+b and multiplies the scalar by c=ds/(da db). The four normalizations
are D,Dc_e,Dc_f,Dc_e c_f. Both Rayleigh terms therefore have the same
factor D²c_e c_f. Their exact difference is

    D²c_e c_f [X_e X_f-2BJ delta_e delta_f F],

where F=S+LU+JGamma+BJU² and
X_i=delta_i(L+2BJU)+Jepsilon_i+BJdelta_i². No negative cross term has
been discarded. Alpha and gamma divided by their positive argument are
strictly increasing, independently proving the positive merge increments.
The author's alternative gamma''=6x/(1+Bx)^4 also checks.

Root independently expanded L²-2BJ S in the primitive core weights.
Writing the columns as u,v,w, its constant is (uv)²+(uw)²+(vw)²;
the p12 coefficient is2w²(u²+uv+v²); its square coefficient is
w²(u+v)²; the p12p13 coefficient is2v²w², with the cyclic analogues.
These agree with every term of the author's displayed certificate and
are positive/nonnegative. Also BL>J. Consequently

    (L+2BJU)²-2BJ F
    >=L²-2BJ S+2J(BL-J)U+2B²J²U²>0.

This supplies the strictly positive Rayleigh bracket for positive marked
endpoint row weights. At zero endpoints the nonnegative limit is valid;
strictness is not claimed. Positive marked activities give strict negative
covariance with the stated sign and factor z_e z_f/Z². Parallel core
activities aggregate because a forest cannot select two parallel edges.

Root read and reran both earlier common-spoke and heterogeneous-row author
and independent scripts as well. The final script's direct uncontracted
subset coefficients, explicit connectivity transfer, and normalized
formula agree. The main final tests include rational weights, absent core
edges, a third matching edge, an unmarked zero row, and frontier checks
through100terminals. Finite tests support the complete algebraic proof;
they do not establish its unbounded scope by extrapolation.

This proves matching/matching pairs only, with rank-one spokes over three
core vertices and all other terminal edges forming a matching. It does
not prove all pair types, arbitrary spoke arrays, arbitrary cores, or the
full forest/random-cluster conjecture. Known series-parallel, two-sum and
small-graph SOS results are prior work and may subsume special cases.
