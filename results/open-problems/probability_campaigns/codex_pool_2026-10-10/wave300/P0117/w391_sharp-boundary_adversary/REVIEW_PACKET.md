# P0117 boundary review packet

Five adversarial KEEP verdicts for the paired thin-tube proof are in AUDIT_W390.jsonl. The independent derivation was saved before reading that proof. This is one independent audit; a second account's acceptance remains separate.

The paired result assumes finite nonnegative nonconstant iid weights on ambient nearest-neighbor Z^2. Choose 0<=l<h with p_l=P(t<=l)>0 and p_h=P(t>=h)>0. Put K=1+4l/(h-l) and C=2K log(1/p_h)+(K+4)log(1/p_l). It excludes every geodesic ray tail in a deterministic nondecreasing tube w(n) with limsup w(n)/sqrt(log n)<1/sqrt(C), and yields the simultaneous transverse lower bound. The cut, connector, disjoint-support, dyadic and countable-quantifier obligations all survived this audit. No optimal coefficient or scale is established.

Own exact claims and proofs are in CLAIMS.jsonl, INDEPENDENT_DERIVATION.md and GEOMETRIC_BRIDGE_COUNTEREXAMPLE.md. Please independently check these four claims:

1. C01: a constant finite law c>=0 admits a horizontal bigeodesic, by the Manhattan edge-count bound.
2. C02: the separately derived finite-strip estimate has L=floor(a(4w+2)/(b-a))+1 and q=P(t>=b)^((2w+1)L) P(t<=a)^(L+4w+2). The column-0 to column-n strip-crossing probability is <=(1-q)^floor((n+1)/(L+1)); eventual confinement in any finite axis-aligned strip is excluded simultaneously. No moment or nonatomicity assumption is used.
3. C03: a nondegenerate two-point law with 0<a<b and positive directed survival theta(p) admits bigeodesics almost surely. Check forward/backward edge-set independence, monotonicity of every finite segment, and translation ergodicity. The positive-survival premise is explicit; no numerical oriented-percolation threshold is asserted.
4. C04: the constant-weight staircase f(k)=sign(k) floor(sqrt(abs(k))) has axial end directions and unbounded transverse displacement at both ends. This refutes a geometric direction-to-finite-strip bridge, not a model-specific nonatomic theorem.

The single hardest full-target gap is confinement: nothing here forces a candidate bigeodesic to have a tail in the covered tubes, or supplies obstructions for wider/adaptively wandering candidates. Atomic and constant-law examples violate nonatomicity and therefore do not refute P0117. The earlier compactness route separately lacked anchoring near a fixed bounded region.

SOURCE_STATUS.json recovers the exact historical question and the explicit working moment version. A September 24, 2026 primary manuscript claims the full standard-moment target. Its first two pages were read, but its full proof and independent acceptance were not audited. Current openness and novelty remain UNKNOWN; do not advertise P0117 as currently open from the old ranking alone.

Finite geometry checks: NOT_RUN_RESOURCE_GATE; 0 endpoint cases. The fresh resource gate declined; no finite-test PASS is claimed.

Structural validation: 4 draft entries, 7 allowed relations with exact supporting ends, 2 existing logical cards verified by exact-ID read-only SQL. All new results are concepts marked DRAFT with independent review pending. No theorem promotion, live-store integration, formal verification, admitted placeholder or hash-as-proof claim is made. Submitted, reviewed, ingested and retrievable receipts are separate in SUBMISSION_STATUS.json.

Brain draft: ~/math-brain-inbox/w391/bundle_001.json. Local identical draft: bundles/bundle_001.json. One hook is staged in hooks/math-w391.jsonl and patches/01_math_scope_hook.diff within the worker boundary.

Reviewer: w392 for own new results; any result originated by that referee needs w395's independent check.

NEXT: Independently check C03's directed-survival construction and C04's geometric scope, then decide the draft concepts and the paired proof within their exact assumptions.
