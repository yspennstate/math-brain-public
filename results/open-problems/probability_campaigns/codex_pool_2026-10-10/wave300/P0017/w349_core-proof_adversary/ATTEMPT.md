# P0017 adversarial attempt

The exact full target is the universal upper bound C_P(mu)<=C for isotropic
log-concave laws in every dimension, with the variance/Dirichlet normalization.
The original Randomstrasse Entry 13, Conjecture 30 asks equivalently for a
universal Cheeger lower bound in isotropic position. SOURCE_STATUS.json records
the primary statement and the October proof claims. Current openness UNKNOWN;
no full-target novelty or complete independent proof certification is claimed.

The prior live-store attempt proves the Gaussian Hermite special case and
explicitly leaves the general input open. The named H/I targeted searches did
not locate a P0017 proof. The original ledger worktree path is absent. The
source recovery and store read were bounded; private owner work is not certified
exhaustively.

The selected hard input for the independent localization route is (W): universal
T,K control E|Cov_mu_t(f,X)|^2 by K E Var_mu_t(f) for every test function and
every isotropic log-concave law up to time T. WEIGHTED_GAP.md derives the
conditional exp(KT)/T Poincare bound and leaves (W) explicitly unproved.
The reduction uses an actual observation filtration, innovation Brownian
motion, total variance, and Ito isometry; it multiplies no unrelated conditional
expectations. Convex-support strong-convexity and the final approximation are
explicit referee obligations. Smooth strong-convexity itself follows from the
integrated Bochner identity in BKL Section 2: an eigenfunction gives
lambda^2||f||^2>=T||grad f||^2=T lambda||f||^2, hence lambda>=T.

The attempted shortcut to (W) fails even in dimension one for an isotropic
centered exponential law. For f=x and Y_s=sX+sqrt(s)Z, every conditional
variance/covariance factor is the same nonconstant scalar A. The proposed
factorization becomes E A^2<=(E A)^2 and is strictly false. This is w349-C006,
not a counterexample to KLS. The remaining uniform weighted bound is the exact
unfinished mathematical step.

INDEPENDENT.md was saved before paired-prover proof access. It also gives
normalization, raw-moment/cumulant, tilted-covariance and matrix-norm controls.
After reading only w348's challenge, PEER_L1_INDEPENDENT.md supplied an
independent equality witness for the binomial tensor constant and a safe
symmetry-error bound. Then PEER_AUDIT.md checked the actual proof: KEEP L1,
KEEP L2, KEEP L3, FIX only the general finite-fourth-moment Taylor terminology
in L4. The Pareto-tail counterexample and exact minimal repair are recorded
there. The algebraic quadratic-form norm identity remains correct.

For w348's full-target route the unproved universal all-degree Taylor estimate
is the selected hard analytic input. The tensor lemma and centered-exponential
product family do not supply it. No raw moments replace cumulants, no source
hash counts as a proof, and no successful finite computation certifies KLS.

Reproduction:
    python -X utf8 verify_obstructions.py
    python -X utf8 verify_peer.py
Both small runs passed their predeclared gates. The first provides an ordinary
quadrature diagnostic backed by the exact strict-variance argument, and the
second checks exact finite identities. Mathematical evidence and finite checks
are kept separate in CLAIMS.jsonl and the measurement files.

Review: w350 is the independent referee for w349's new results. All such results
remain DRAFT concepts in the inbox until review; account separation and
ingestion are not inferred. w353 independently checks the referee's own results.

NEXT: w350 check C006, the conditional C007 reduction, C009 equality witness and
C010 domain counterexample; then decide whether the universal input (W) or
the published analytic input can be audited without promoting it prematurely.
