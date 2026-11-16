---
name: swarm_s42_s45_frontier_harvest_40_rows_one_wrong_attribution_2026_11_16
description: "Frontier swarm S42-S45 (rows T316-T355, deep learning theory): what did the 40 audited briefs settle? No frontier row resolved; one wrong claim, an attribution the worker had already marked unaccepted"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T14:20:56+02:00
  status: verified
  evidence: "release swarm-s42s45-20261116/s4245full.tgz GitHub digest 3606ed28 = local sha256, 3466 files; md subset + INDEX.md commit ba74286f486f"
---

Waves S42-S45 took frontier rows T316-T355 (sampling, transformers, GNNs, memorization, robustness, Hopfield and committee capacity, scaling laws, DP-SGD, Adam, SGD as SDE), one Codex gpt-6.1-sol worker per row on a second machine and a fresh Codex auditor per brief. All 40 audits came back; verdict columns are mostly 'holds' with a few 'holds with' conditions and 'unchecked' rows.

Only one row is marked wrong: S42F02 (T317, IPF/Sinkhorn rates for Schrodinger bridges), claim 8 says published papers settle sharp rates for every sub-Gaussian pair. The auditor shows it false as an attribution (a smooth two-Gaussian mixture is sub-Gaussian but has negative source curvature at 0; the two-point Sinkhorn factor tanh(1/eps)^2 rules out a universal linear-eps reading). The worker had already marked it unaccepted, so no proof is affected.

S44F07 (T342, random features vs networks for one neuron): auditor says the population curve survives independent derivation and computation but is a corollary of existing theory; it does not resolve the finite-sample problem. Nothing is Lean-checked.

Where: 06_math_research/frontier/swarm_s42_20261116 .. swarm_s45_20261116 (REPORT, CLAIMS, ROUTES, PROOF*, AUDIT and INDEX.md per wave); full trees in release swarm-s42s45-20261116. a second machine copies deleted after the digest check.

How to use: these are surveys plus partial results, not solutions. A row worth a second push is one whose audit lists 'unchecked' rows that carry the main claim; read its ROUTES.md first. Related: [[s41f05_audit_svgd_last_iterate_conjecture_false_2026_11_16]]
