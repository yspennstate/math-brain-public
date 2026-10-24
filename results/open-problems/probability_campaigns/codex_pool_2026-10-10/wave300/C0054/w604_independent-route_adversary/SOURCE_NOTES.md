# C0054 source notes

Recovered exact intake record: problems.jsonl line 54, candidate C0054, Bourgade ICM 2018, Conjecture (0.2) page 2 and Section 2.2 page 7. Its statement combines fixed-W bulk localization with scale exp(W^2) and Poisson local statistics. All three components require separate proof obligations. Intake is unreviewed and current_status is unverified.

The same intake's note says arXiv:2503.07606 addressed W much larger than sqrt(log N). That is unsupported by the cited paper's abstract, which instead assumes W>=N^c for fixed c>0. Correct this parameter range before reusing the intake status note.

Recent primary source: Lai and Yang, https://arxiv.org/html/2609.24426v2, dated 6 October 2026. Equations (1.4)-(1.5) specify independent Gaussian entries up to Hermitian symmetry, real diagonal, circular complex off-diagonal, with variance S_xy=(5W^2)^(-1) within the same or a neighboring block. N=(WL)^2. Theorem 1.2 requires W>=(10+log N)^(27/4)(10+log(10+log N))^13 times the indicated iterated-log square, and gives a simultaneous bulk eigenvector sup-norm-square bound of 2C*m/N with probability >=1-N^(-D); m is the square of that bandwidth threshold. The simpler abstract condition W>=(log N)^7 implies a lower localization-length scale exp(W^(1/7)). This is a delocalization/lower-bound result, not fixed-W localization. Search snippets still report superseded v1 exponent 55. Openness remains UNKNOWN pending the owner-status check; no novelty claim.

Required scar applied: proof_steps_need_derived_joint_structure_2026_09_09. Write the exact conditioning sigma-field when averaging a resolvent factor; deleting one site makes its incident hoppings independent of the minor, but overlapping block resolvents need not be independent.

Required scar applied: perceptron_proof_open_gaps_fleet_2026_07_12. A checked artifact, numerical identity or successful runner is not a proof of the parent's unchecked estimate.
