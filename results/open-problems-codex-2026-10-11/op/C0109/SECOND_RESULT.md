# C0109 second-pass result — 2026-10-11

Verdict: PARTIAL. Two genuinely new routes were identified; quantitative
Hermitization/Lindeberg comparison was pursued through a complete
conventional nonoptimal upper-rate proof and hostile referee audit.

For every fixed centered unit-variance complex iid entry law with a
finite (2+eps)-moment, put e=min(eps,1). The new proved bound is

    d_K(mu_n,mu_circ)=O_X,eps(n^(-e/(12+4e)) log n)

almost surely eventually, under any coupling across n. It holds with
failure bounded by every prescribed polynomial power, with constants
depending on that power, and in expectation of the random distance.
Thus every delta<e/(12+4e) is a valid pure-power upper exponent.

The earlier fixed-law lower obstruction says that, when 0<eps<2/3,
no exponent above 2eps/(2+eps) can work for every such law, even with
law-dependent constants. Consequently the exponent sought in the source
lies between the new sufficient bound and that necessary bound (under
the source's almost-sure random rectangle-metric interpretation), but
these bounds do not match. No exact optimal curve or literature solution
is claimed; no novelty claim is made for the derivation.

Full proof: DIRECT_UPPER.md (Sections A–G).
Referee audit: DIRECT_REFEREE.md.
Independent new transfer theorem: SECOND_ATTEMPT.md.
Alternatives considered: SECOND_APPROACHES.md.
Numerical and exact checks: direct_checks.json.
Formal scope and output: FORMAL_CHECK.md.
Both auxiliary Lean files completed with exit code 0; their ten algebraic
lemmas are kernel-checked. The stochastic theorem is not formalized.

The main mathematical inputs used from papers are Tao–Vu's controlled-
moment least-singular-value theorem and Jalowy's expected W_1 rate for
one fixed Gaussian law. The rest, including anisotropic real-Gaussian
projection counts, fractional-moment replacement, row concentration,
bad-set integration, local potential comparison, and rectangle smoothing,
is written out. No moving-law all-moments theorem is invoked.

Remaining gap: matching sharp weak-moment upper and lower exponents.
The upper proof's replacement/regularization and smoothing losses are
not shown necessary; the previous lower construction also need not be
extremal. The full C0109 problem remains unresolved in this work.
