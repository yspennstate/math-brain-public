# Review packet: C0120 independent route

Author w495. Mathematical referee w497 (pending). Statement-first adversary w496 (mesh receipt msg-8e4d1b3b89) independently rederived L1-L5 and returned scoped KEEP in ~/brain_workers/w496/AUDIT_W495_PROOF.md; L0/S1 also have KEEP receipts. Review request msg-051c033861. Narrow lemma claim clm-35d79498ec: topic:C0120:bounded-degree-first-chaos-obstruction. Served author/referee identities remain unattested; the audit explicitly does not certify a different-model/login gate. All results remain drafts for integration.

Concrete result: ATTEMPT.md L1-L5 prove an author-only obstruction to a first-chaos/degree-only proof route. The Gaussian common-root graph has first-chaos variance 3-2/m and variance Theta(L/log L). This is a different graph from the source's east/north lattice. C0120 is not solved here; current openness is UNKNOWN.

Source correction to check first: STATEMENT.md and SOURCE_STATUS.json identify Theorem 8.1's ground-state Gaussian 1+1 model. The intake row incorrectly substitutes general-dimension log partition functions. The proposed unified diff will be in patches/01_C0120_source_scope.diff; apply only after source review, to a reviewer-owned checkout.

Check these mathematical obligations independently:

1. L1: Mills bounds, the quantile ratio >=(2/5)exp(-3/2), two-event variance lower bound, and OU hypercontractivity's exact time parameter.
2. L2: graph path length n+r; prefixes are correlated; the Gaussian union bound controls their maximum without independence.
3. L3: the transitive automorphism action preserves the Gaussian law; integration by parts for the Lipschitz maximum gives occupation coefficients.
4. L4: the centered L2 triangle inequality and the condition on prefix error imply both variance bounds; the graph family is outside the source lattice.
5. L5: fixed beta only, deterministic log-sum-exp error, expected Gibbs masses under transitivity, and first-chaos normalization.

The single hardest parent gap is quantified in GAP.md: find delta>0 with R_n(n^-delta)<=C n^(1-delta) on the fixed source lattice. The covariance identity then gives the desired variance gain. Finite checks and hashes validate limited controls and provenance only; no formal theorem check or complete proof certificate is claimed.

Integration: draft concepts only; no theorem promotion or live-store writes by this worker. Prepared, submitted, reviewed, ingested, and retrievable are separate fields. Local hook proposal in hooks/math-w495.jsonl is for the coordinator to place in the shared proposal queue; the worker-folder write restriction remains in force.

NEXT: w497 returns a scoped verdict on S1 and L1-L5; the integrating coordinator applies kept source corrections and draft concepts without setting the parent problem solved.
