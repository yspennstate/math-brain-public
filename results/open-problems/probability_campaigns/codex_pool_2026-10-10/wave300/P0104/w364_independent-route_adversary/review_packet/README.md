# Review packet for w365

Target: the P0104 independent boundary-profile/adversary lane. The deliverables are complete for review; the asymptotic open problem is not solved. Current certified openness remains UNKNOWN. All new brain content is staged as concepts/drafts.

Review the actual mathematical claims before deployment:

1. C02: unrestricted-lattice reduction to the two length-two routes, the two incompatible-minimum configurations, the exact distributions, and Cov(L,T-L)=-1/16. Check the argument for all possible other edge configurations, not only the finite-box computations.
2. C05: integer-valued single-edge increments equal membership in every forced-low minimizer, including ties and edges outside the deterministic localization ball. A selected tied geodesic is insufficient.
3. C03: the centered L2 reverse triangle inequality transfers the variance ratio only under both the small-error hypothesis and a two-sided variance bound for L_n. Neither FPP hypothesis has been proved here.
4. C04: the exact source and exponent convention, including the unresolved suitable-law conditions. C01 is only a boundary check on an unqualified shorthand, not a refutation of the primary conjecture.
5. PEER_AUDIT.md: confirm the scoped keeps for the paired L1-L5 argument and its unproved G1; do not treat the exact finite checks as an asymptotic proof.

Reproduce the bounded exact checks with `python -X utf8 check_boundary_profile.py`. It uses 16 assignments, 32 Dijkstra comparisons and 64 forcing checks, all exact arithmetic, no random sampling. Then run `python -X utf8 prepare_drafts.py --validate-only` for artifact/schema consistency. These are author-side reproduction checks, not independent mathematical approval.

The substantive draft bundle is drafts/bundle_001.json. The unified change files in patches/ name the requested shared destinations. The worker's folder-only rule forbids direct shared writes, so submission, review, ingestion and live retrieval are all recorded separately in DELIVERY_STATE.json and start false. The normal validating coordinator publishes only after mathematical review. Do not run a live integrator merely to validate this local draft.

The math claim set uses the accepted owner-own-work source tag. There is no cryptographic source manifest or formal-check receipt. The public mathematical statements contain no home paths, owner names or agent identities.

NEXT: Independently check C02/C05/C03 and return narrow keeps or fixes; the next proof task is centered matching-error control at n^(1/3) scale.
