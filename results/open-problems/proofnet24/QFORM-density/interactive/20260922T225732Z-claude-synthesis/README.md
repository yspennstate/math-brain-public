# Quadratic-form density: newest-Claude synthesis

This package supplies complete supporting arguments, not a proof of the unrestricted universal conjecture. Independent end-to-end review of the new synthesis remains pending.

Start with `GEOMETRIC_SYNTHESIS.md`. It combines Claude's newest two-dimensional hyperbola estimate with the existing arbitrary-rank small-ball estimate to give a determinant-only physical-pair bound. It proves the logarithmic auxiliary bound globally and reduces the full conjecture to a single no-pivot three-eigenvalue density statement. That remaining statement is explicitly unproved. The Gaussian padding in the reduction introduces auxiliary variables; it does not assume that the original variables are Gaussian.

`REPORT.md` proves a general O(sqrt(n)) projected-gradient estimate, a uniform finite-core estimate allowing dense perturbations and arbitrary outside couplings, and a rigorous rough-input transfer of Claude's one-sheet ruling bound. It also restores the already-proved semidefinite rank-three theorem to the shared proof map; that old theorem is not presented as new.

## Source commits

The two newest Claude inputs consumed are `e5f71d79eff325201dd0274053d20268ce65b837` and `2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926`, in `yspennstate/math-open-problems`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. A final path-specific history read still showed the latter as the latest commit in that directory.

The six proof/check files in this package are committed together by `6dc1ce3ee7dba3621f83b49c961182fa2c4ab2ab`, directory `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/`. Their Git blob hashes were read back and match the local files exactly. `LOCAL_MANIFEST.json` records SHA-256, Git blob hashes, sizes, and the limited scan scope. The manifest itself was committed at `4098649c3810c9c525c6d357b3d2c5417a333f6b`.

## Reproduce finite checks

Requires Python 3.10+, NumPy, SciPy, and SymPy:

    python checks.py
    python geometric_checks.py

These bounded scripts check scalar identities, finite matrix examples, the ruling Jacobian, and Gaussian-padding preservation of the no-pivot class. Their executed outputs are included. They are not universal proof certificates, independent mathematical reviews, or evidence that the remaining no-pivot hypothesis holds. No Monte Carlo histogram is used as a proof.

## Worker continuation

The existing shared directive is `scheduled_tasks/work/shared/qform-density-2026-09-22/requests/QFORM-CLAUDE-LATEST-20260922T225732Z.md` in `yspennstate/math-research-brain`. All twenty native prompts accessible in account04 were updated successfully to require that directive and newer source commits; the other three accounts' coordinators were directed to perform their own local rollout. Configuration, actual adoption, mathematical results, and successful delivery remain separate evidence classes. No claim is made that all eighty native schedules were directly modified from this account.
