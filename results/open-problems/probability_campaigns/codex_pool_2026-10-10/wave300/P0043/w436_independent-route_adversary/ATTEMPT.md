# P0043 independent adversary checkpoint

The paired proof has not been read. Exact primary-source verification is pending.

First saved obstruction: on the nearest-neighbor integer line, p_c=1 and percolation occurs at p_c. This checks the recovered p_c<1 assumption and does not refute the intended conjecture.

The completed independent calculation is in INDEPENDENT_DERIVATION.md. It constructs a dyadic-burst tree of maximum degree 9 with p_c=1/2 and critical survival at least 4/5. It uses a conditional offspring second moment on disjoint fresh edges, rather than the recorded homogeneous critical-branching fixed-point extinction argument. Quasi-transitivity is explicitly absent. Exact rational checks covered 4,095 generations in 0.230 seconds with zero failed assertions; the infinite omitted tail is included analytically.

After saving that derivation, I read w435's original proof. AUDIT_w435.md and AUDIT_VERDICTS.jsonl give KEEP for its four auxiliary statements and FIX for its proposed completion. The specific obstruction is noninheritance of host ray energy by a critical component: the host energy is 5/4, but each surviving critical component almost surely has threshold 1, and therefore has no finite I_r for r<1. No conjecture or theorem about all quasi-transitive graphs is refuted by this example.

SOURCE_STATUS.json records a September 24 primary preprint claiming the full result. Its Theorem 1.1 statement is verified, but the proof is not verified here and its linked comparator is a statement stub containing an admitted placeholder. Current openness is UNKNOWN; this packet makes no novelty or solved claim.

Independent route to develop: interpret survival on a rooted tree through generation sizes and a second-moment/energy bound, and test whether critical extinction arguments require a uniformity assumption that quasi-transitivity alone has not supplied. Check recorded local methods before choosing the precise lemma. An arbitrary locally finite tree may have percolation at its critical parameter; any such example must be explicitly separated from the quasi-transitive target.

Hardest unresolved piece of this route: derive from the full quasi-transitive hypotheses, under hypothetical critical survival, a finite-energy ray measure on a surviving critical component for some thinning parameter r<1, and supply a separate argument for recurrent classes. The host graph cannot supply this premise merely by possessing such a measure.
