# C0047: finite-volume critical norm route

Author w552, 2026-10-10. BOND percolation on an infinite connected simple bounded-degree Cayley graph. Independent referee: w554, pending. Parent conjecture remains unproved. This is a self-contained reconstruction of a known operator route, not a novelty claim; Hutchcroft (arXiv:1804.10191v3), Section 2 and Remark 2.5, already give closely related sprinkling estimates.

## Exact target

See STATEMENT.md. The generating set S is arbitrary and fixed before percolation. Neither changing S nor proving a single endpoint is nonunique discharges C0047.

## Load-bearing input, still unproved

Let F run over finite connected subgraphs of G, with free boundary, and let T_p^F(x,y)=P_p^F(x is connected to y). Define

M_c(G) = sup_F ||T_{p_c(G)}^F||_{ell2(F) -> ell2(F)}.

The missing input for THIS route is M_c(G)<infinity for every nonamenable Cayley graph. This is the critical operator boundedness problem, a stronger proposed route to C0047; it is not an established consequence of nonamenability. A constant that depends on F is insufficient. No experiment on finite F can prove this supremum is finite.

## Lemma L1: critical finite-volume supremum equals the full operator norm

For any p in [0,1], extend T_p^F by zero off F. Each T_p^F is positive semidefinite: for a real vector f,

<f,T_p^F f> = E_p[sum over open clusters C in F of (sum_{x in C} f(x))^2] >= 0.

For a finite-support nonnegative f and a finite connected exhaustion F_n of G, every finite connecting open path is eventually inside F_n. Hence each relevant entry T_p^{F_n}(x,y) increases to T_p(x,y), and the quadratic forms converge. If sup_F ||T_p^F|| <= M, it follows that <f,T_p f> <= M||f||_2^2 for every such f. Absolute values extend this to all finite-support f, because T has nonnegative entries; positivity and polarization give a unique bounded positive self-adjoint operator with norm at most M. Conversely, T_p^F <= T_p entrywise, and for arbitrary finite-support f, |<f,T_p^F f>| <= <|f|,T_p|f|> <= ||T_p||||f||_2^2. Thus sup_F ||T_p^F||=||T_p||, allowing infinity on both sides.

Gap: none in the stated lemma. Status: proved special case / author proof, independent check pending.

## Lemma L2: finite-volume differential estimate without an independence shortcut

Fix finite connected F and 0<p<1. Russo's formula for the finite increasing event {x connected to y} gives d/dp T_p^F(x,y)=sum_e P_p(e is pivotal). For e={u,v}, sample all edges other than e. If e is pivotal, removing it leaves x and y in different components with the two endpoint assignments (x connected to u and v connected to y), or their reverse. These connections have edge-disjoint open witnesses. Apply BK on the PRODUCT measure of F with e deleted, then use T_p^{F-e}<=T_p^F. Consequently

d/dp T_p^F(x,y) <= sum_{e={u,v}} [T_p^F(x,u)T_p^F(v,y)+T_p^F(x,v)T_p^F(u,y)] = (T_p^F A_F T_p^F)(x,y).

This does not treat successive cluster explorations as independent. There is no 1/(1-p) factor: pivotality is determined by the other edges, whose law is already a product measure. Entrywise inequalities are used only with nonnegative vectors, never asserted as Loewner inequalities.

For p>0, T_p^F has strictly positive entries (unless F is a singleton, which is trivial). Its Perron eigenvalue m_F(p) is simple and equals its operator norm, since T is positive semidefinite. Let v be its normalized nonnegative Perron vector. Differentiating the simple eigenvalue and using the entrywise bound with v>=0 gives

m_F'(p) = <v,(T_p^F)'v> <= <v,T_p^F A_F T_p^F v> = m_F(p)^2 <v,A_F v> <= alpha m_F(p)^2,

where alpha=||A_G||_2 and ||A_F||_2<=alpha. Integrate (1/m_F)' >= -alpha to obtain, for q>=p_0>0 with alpha m_F(p_0)(q-p_0)<1,

m_F(q) <= m_F(p_0)/(1-alpha m_F(p_0)(q-p_0)).

Gap: none in the stated finite-volume lemma. Status: proved special case / author proof, independent check pending.

## Lemma L3: explicit conditional nonuniqueness interval

Assume p_c(G)<1 and M_c(G)<=M<infinity. Let alpha=||A_G||_2 and eta=min{(1-p_c(G))/2, 1/(2 alpha M)}. Bounded degree and infinitude imply p_c>0 and alpha>0. By L2, every finite F has ||T_{p_c+eta}^F||<=2M. By L1 the full T_q is bounded for every q in [p_c,p_c+eta].

If percolation at any such q had almost surely exactly one infinite cluster, transitivity gives theta(q)=P_q(o belongs to that cluster)>0. Harris-FKG and uniqueness imply T_q(x,y)>=theta(q)^2 for all x,y. For any n distinct vertices, the unit vector equal to 1/sqrt(n) on those vertices has quadratic form at least n theta(q)^2, contradicting boundedness. For q<p_c no infinite cluster exists almost surely. Therefore no parameter below or equal to p_c+eta lies in the a.s. uniqueness set, so

p_u(G)>=p_c(G)+eta>p_c(G).

The conclusion is CONDITIONAL on M_c<infinity; no monotonicity of uniqueness is needed for this infimum argument. A statement about infinitely many infinite clusters additionally invokes the standard 0/1/infinity theorem; it is not needed here.

Gap: prove M_c(G)<infinity from nonamenability alone. Status: proved conditional reduction / author proof, independent check pending.

## Attempt to discharge the missing input

Nonamenability yields alpha<degree d (Kesten's spectral-radius criterion). A path union bound gives T_p <= sum_{n>=0} p^n A_G^n, and hence ||T_p||<=1/(1-p alpha) ONLY for p alpha<1. This proves a useful sufficient regime p_c alpha<1. It does not establish that regime for every nonamenable Cayley graph. Even on a d-regular tree, p_c alpha = 2 sqrt(d-1)/(d-1); at d=3 this is sqrt(2)>1, although the desired critical norm IS finite. Thus the coarse path bound loses enough cancellation/geometry to fail on an elementary solved graph.

The next possible improvement is to remove immediate backtracks and use nonbacktracking path matrices. For a tree, they recover the true two-point kernel p^{distance}; cycles on a general Cayley graph create overlapping witnesses. Summing paths still supplies only an upper bound and needs a uniform operator bound. We cannot multiply conditional exploration probabilities to dispose of those overlaps. The single hardest remaining gap stays M_c(G)<infinity for arbitrary nonamenable G, not a local BK calculation.

This improvement is now carried out, with its precise restricted input, in NONBACKTRACKING_LEMMA.md (L4). It gives ||T_p|| <= (1-p^2)/(1+(d-1)p^2-alpha p) for p beta<1. It verifies the infinite regular-tree critical bound for every d>=3. The sufficient condition p_c beta<1 is still not derived from nonamenability in general, so the parent gap stays open.

NB_ROUTE_OBSTRUCTION.md now shows that the universal shortcut "nonamenability implies p_c beta<1" is FALSE, using the fixed C3*C2 tree-of-triangles Cayley graph. It has p_c>3/5 and beta>5/3, yet p_u=1. This refutes the extra universal spectral input, not L4's conditional bound and not C0047. The general uniform M_c input remains unproved in this packet.

## Measured checks

Command: python -X utf8 ~/brain_workers/w552/validate.py. Fresh Windows commit gate used the existing brain_workers/GATE.json commit_floor_gb=6.0; no worker or resource gate was changed. VALIDATION.json records PASS: 18 exact Russo cases, 294 exact rational entrywise BK checks, 18 numerical norm-bootstrap cases, and 21 exact nonbacktracking recurrence matrix checks. The script used 0.121 seconds of measured run wall time. Evaluation of the analytic tree criteria for d=3,...,10 gives 5/8 certificates for the coarse adjacency-walk criterion and 8/8 for the nonbacktracking criterion. These checks validate finite identities and constants, not the general infinite critical supremum.

## Owner prior work and lane boundary

The owner's named percolation project README.md explicitly says its stronger operator target is unfinished. Its research/proof_strategy.md develops near-critical normalized-kernel escape, interior/boundary alternatives and killed-SAW estimates. Our specific lane is a direct finite-volume Perron/Russo bound plus the regular-graph nonbacktracking resolvent. These conditional tools do not settle the owner's missing uniform near-critical escape bridge. The June source-status note does not certify October openness.

## Latest source-status correction

The public OpenAI math overview now has family 214, a September 24, 2026 manuscript claiming the exact general Bernoulli bond result p_c<p_2to2<=p_u for nonamenable quasi-transitive graphs. Primary source: https://github.com/openai/math/blob/main/overview.tex and https://github.com/openai/math/blob/main/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf. This release claim overrides any use of the August note as a present-openness certificate. Mathematical validity and the actual formal theorem/axioms have not been verified by this worker. A ComparatorChallenges theorem ending in sorry is a challenge statement, not a proof receipt; it says nothing by itself about a separate library proof. Current openness therefore stays UNKNOWN and no novelty is claimed. The paired source lane is already investigating this public claim; this packet preserves the source pointer and works on its own precise conditional statements.

## Validation boundary

The proofs above are mathematical author proofs. Finite exact checks will test L2 and the constants, not certify the infinite uniform supremum. No Lean theorem, admitted placeholder, or formal proof receipt is claimed. Served author model identity is unavailable from this thread; requested model settings are not served-model evidence.
