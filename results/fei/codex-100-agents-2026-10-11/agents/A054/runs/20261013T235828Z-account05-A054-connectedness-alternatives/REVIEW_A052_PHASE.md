# Independent reconstruction of A052 phase exclusion v1

Source: A052-CRITICAL-BOOLEAN-PHASE-EXCLUSION@1, run
20261013T221539Z-account05-A052-critical-source-structure,
CRITICAL_PHASE_PROOF.md sections 1--3 and CLAIMS.json.
Verdict: ACCEPT_AT_STATED_SCOPE, independent analytic reconstruction;
no substantive repair. Shared adoption remains pending.

The weights q_t sum to one because f is Boolean. For a positive row,
z=w²/q has mean one. Jensen with the probability measure z dUniform
gives E z log2 z<=log2 E z²=log2(1+c). Summing proves the collision bound,
including its zero case. When all c vanish, each row divided by sqrt(q)
is a true Boolean phase on a<n coordinates. Lower-dimensional FEI(K)
applies by minimality among ALL Boolean K-violators; these phases need
not be physical descendants. Their weighted Fourier entropy and
influence are exactly B_A and I_A. Actual children supply the separate
nonpositive terminal deficits. Thus zero collision excludes the root.

For nonzero collision, normalized w/sqrt(q) and its pointwise sign both
have norm one. Parseval and Cauchy--Schwarz give Fourier-squared-law TV
at most their L2 distance. Clipping that distance at one is valid. The
pointwise inequality (sqrt(z)-1)²<=(z-1)² gives tau²<=c; weighting and
Cauchy--Schwarz imply eta<=sqrt(C). The supplied coupling proof controls
entropy difference, and expectations of degree in [0,a] differ by at
most a TV. The capped psi_a is concave and nondecreasing, so Jensen
correctly gives the stated row-averaged approximation error.

Physical-child criticality alone cannot certify the row phases. The
quadratic tensor example has full-factor isospectral cuts and physical
descendant ratios at most two, and therefore correctly prevents the
weaker assertion. No phase approximation, collision or terminal reserve
is silently paid universally. The exact first open selection line is
retained. This review addresses a live B11 source-complete candidate
before the A054 projection generalization is proposed; it is not a replay
of A052's census or acceptance of a full FEI argument.
