# w439 review packet: P0043 sharp boundaries

Designated independent referee: w440. w439's source correction and new results are pending that review. Paired prover w438 has received the separate AUDIT_W438.md verdict. Current full openness: UNKNOWN; no novelty or P0043 solution claim.

Target: on every infinite connected locally finite quasi-transitive graph G with p_c(G)<1, iid Bernoulli bond percolation at p_c has no infinite clusters almost surely. Exact quantifiers are verified in Hutchcroft arXiv:1605.05301. The original intake points to Lyons--Peres Conjecture 8.15, printed p.285, 19 August 2026 electronic version; that specific PDF fetch exceeded the browser limit.

Review INDEPENDENT.md and CLAIMS.jsonl 002-003: every uniformly L-subdivided 3-regular tree is quasi-transitive with maximum degree 3, has p_c=2^(-1/L)<1 and critical extinction, but its critical connection probability at distance L is 7/8. For fixed n the supremum over these graphs is 1. Check disjoint coarse edge sets, the finite orbit argument, fixed-n versus fixed-L quantifiers, and the root asymptotic 6L/n. This does not contradict extinction on any fixed graph or a vertex-transitive-only estimate.

Check the source correction (claim 004) against Theorem 6, Lemmas 4-5 and the proof of Theorem 2 in https://arxiv.org/html/1605.05301. The old C0084 attempt says: “His proof uses the growth to show that the susceptibility is finite at p_c in a spherically-averaged sense via a comparison with a branching random walk with killing at rate given by the growth”. The primary proof uses finite susceptibility below p_c, then supermultiplicativity and left continuity of the infimum connectivity rate. The spherical qualifier in the old card is undefined; the correction does not assign it a new theorem. At ordinary critical susceptibility, the 3-regular tree supplies an exact counterexample to finiteness.

AUDIT_W438.md independently checks the reciprocal identity, the polynomial threshold beta=1, the global-versus-root extinction quantifier, and the fixed-p_c local-limit counterexample. The identity uses m_i, not m_(i+1), and is well-defined for 0<p<=1. The broad general-graph comparison is still missing because branches may overlap. This audit is a mathematical check, not a source-hash or formal-axiom receipt.

Verification command: python -X utf8 ~/brain_workers/w439/verify_boundaries.py. Actual run: 30 PASS, 0 FAIL; 584 exact configurations, at most 9 enumerated edges; 0.015625 CPU seconds. Twenty-four checks cover six offspring patterns and four rational parameters, including p=1. A finite 10,000-step illustration has n*a(n)=5.992222306404675; the limit 6 is proved analytically in INDEPENDENT.md, not inferred from that number.

Brain handoff: BRAIN_HANDOFF.json distinguishes prepared, submitted, reviewed, ingested and retrievable. BRAIN_BUNDLE.json has four concept DRAFT entries and two relations; BRAIN_BUNDLE_CORRECTION.json adds one source-audit concept citing the exact existing C0084 logical ID. All remain concept/DRAFT with review pending. The integrator was not run.

Relation endpoints are quoted below for exact support; the cross-bundle citation identifies an existing export node, not a global correction already deployed.

depends_on: nonuniform -> subdivision

FROM: Independent derivation pending w440 review. For every fixed integer n>=1, the supremum of the critical probability of reaching graph distance n, over roots of infinite connected locally finite quasi-transitive graphs of maximum degree at most 3 with p_c<1, is 1. Indeed, for the uniformly L-subdivided 3-regular tree with L>=n, that probability is 1-(1-2^(-n/L))^3 and tends to 1 as L grows. No single f(n) tending to zero can bound the entire class. A degree-only C/n bound fails already at n=L since the probability is 7/8. This does not exclude graph-dependent bounds and does not address the smaller vertex-transitive class. The family has p_c tending to 1, growing orbit count, and volume-growth rate tending to 1.

TO: Independent derivation pending w440 review. Replace every edge of the infinite 3-regular tree with L edges, for a positive integer L, and root at an original vertex. The result T_L is quasi-transitive of maximum degree 3 and has p_c=2^(-1/L)<1. Full subdivided edges are independent coarse bonds of retention p^L, so critical clusters are almost surely finite. For 1<=n<=L the critical probability of reaching graph distance n is 1-(1-2^(-n/L))^3, hence 7/8 at n=L. At radii kL, with u_0=1 and u_(k+1)=u_k-u_k^2/4, the probability is 1-(1-u_(k-1)/2)^3. Reciprocal increments tend to 1/4, so (kL) times this probability tends to 6L. Critical susceptibility is infinite because every original-vertex shell has expected connected count 3/2.

SUPPORT: The exact a_L(n) formula, with fixed n and increasing L, gives the supremum 1 and rules out graph-uniform decay.

specializes: susceptibility -> subdivision

FROM: Independent derivation pending w440 review. On the infinite 3-regular tree, iid Bernoulli bond percolation has p_c=1/2 and almost surely no infinite cluster at p_c, but E_{p_c}|C(o)| is infinite. At distance k>=1 there are 3*2^(k-1) vertices, each connected with probability 2^(-k), giving expected connected shell size 3/2. Below p_c, chi(p)=1+3p/(1-2p), which diverges as p increases to p_c. Thus finiteness of susceptibility for every p<p_c cannot be transferred to p=p_c without a further uniform integrability or domination argument; it cannot be assumed as a bridge to critical extinction.

TO: Independent derivation pending w440 review. Replace every edge of the infinite 3-regular tree with L edges, for a positive integer L, and root at an original vertex. The result T_L is quasi-transitive of maximum degree 3 and has p_c=2^(-1/L)<1. Full subdivided edges are independent coarse bonds of retention p^L, so critical clusters are almost surely finite. For 1<=n<=L the critical probability of reaching graph distance n is 1-(1-2^(-n/L))^3, hence 7/8 at n=L. At radii kL, with u_0=1 and u_(k+1)=u_k-u_k^2/4, the probability is 1-(1-u_(k-1)/2)^3. Reciprocal increments tend to 1/4, so (kL) times this probability tends to 6L. Critical susceptibility is infinite because every original-vertex shell has expected connected count 3/2.

SUPPORT: Set L=1 in the subdivided-tree critical boundary; its original shells show divergent susceptibility despite extinction.

Cross-bundle cites endpoint: math:probability.percolation:attempt-c0084-no-infinite-cluster-at-criticality-on-quasi-transitive-graphs-with-p-c. Exact existing quote and body are preserved in claim 004 and PRIOR_TARGET_ROWS.json. The new endpoint is the complete correction_statement in BRAIN_BUNDLE_CORRECTION.json.

NEXT: w440 returns KEEP/FIX for claims 002-004; coordinator integrates accepted concepts and audits the local hook proposal.

## Review receipt update

w440 independently returned KEEP on w439 boundary claims 001-003, including the subdivision formula, graph-uniformity obstruction, exact 6L asymptotic and susceptibility divergence. See REVIEW_RECEIPT_w440.md. Source correction 004 remains pending. Submitted concept drafts keep their original preparation-time annotations; the receipt and BRAIN_HANDOFF.json record the subsequent review state. Ingestion and retrieval have not been checked.

NEXT: w440 reviews source correction 004; coordinator integrates accepted concept drafts using the receipt and audits the local hook.
