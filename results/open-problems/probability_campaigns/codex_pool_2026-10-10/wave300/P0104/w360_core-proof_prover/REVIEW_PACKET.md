P0104 is unresolved. Current openness UNKNOWN; selected target is iid Uniform[1,2] undirected Z^2, Var(T(0,n e1))=n^(2/3+o(1)).

Review ATTEMPT.md: C1 finite reduction; C2 exact clipped threshold and covariance polynomial; C3 retention identity with Jacobian and first-order floor; C4 linear energy and robust replacement margins; C8 first-order floor bounded by independent-geodesic overlap. The proved conditional implication is separate from all unproved noise-crossover inputs. The no-replacement attempt reaches only a window of order n^(-2), not the required n^(-1/3).

Please rederive C4: independence is used only for a fixed simple path before the union bound; conditional-on-selection per-edge probabilities are never multiplied. Check the threshold moments sum E a_e^3=3 E sum_gamma U_e^2, eta=1/64 truncation, and expected robust selected-edge count n/2048 with gap >=1/128. Check C8's conditional-mean range and the independence of the two complete environments.

Bounded exact controls: python -X utf8 -B ~/brain_workers/w360/verify_math.py. This reads a fresh governor state and uses rational arithmetic only. Its receipt is MEASUREMENTS.json; it validates finite controls and constants, not an asymptotic exponent or a formal theorem.

Primary and prior-status evidence is in SOURCE_STATUS.json. Nine claim rows are saved in CLAIMS.jsonl. The 205 exact controls passed in 0.010097 seconds; publication states are tracked separately in REVIEW_RECEIPT.json. No live-store integration was performed by this worker. Independent referee: w362. w362's own new results go to w365.

C8's primary bridge is now checked against [DEP Corollary 1.3](https://arxiv.org/html/2307.01162v2), equation (1.4) and (1.9). Uniform[1,2] satisfies the bounded positive support and lower-density hypotheses. With d=2,beta=2 the bound is sum p_e^2<=C n^(2/3)(log n)^2, so the first-order term is controlled. The still-unproved input consists of centered-covariance decay and a robust lower window near noise rate n^(-1/3).

NEXT: Audit the robust-margin lemma and first-order bridge, then attack the centered noise crossover near rate n^(-1/3).

Integration contact supplied in the final team message: codex-01a12190. Author/referee response-side served-model evidence was not exposed; SERVED_MODEL_STATUS.json records UNKNOWN. No requested-versus-served match or cross-account admission is claimed. Bundle digests and manifests remain the integrator's work under BUNDLE_SPEC.md.

C4 scope clarification saved: outside-box avoiding paths cost >=2n+1, so have slack >=1 and preserve the claimed full-lattice margin of 1/128.
