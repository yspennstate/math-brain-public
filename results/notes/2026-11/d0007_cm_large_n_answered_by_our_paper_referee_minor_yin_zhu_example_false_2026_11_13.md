---
name: d0007_cm_large_n_answered_by_our_paper_referee_minor_yin_zhu_example_false_2026_11_13
description: "D0007 (Wang, Current open questions in complete mixability, arXiv 1411.6190, Open Problem 7: is every absolutely continuous law on a bounded interval n-completely mixable for all large n?) is answered YES by our posted paper github.com/yspennstate/complete-mixability-large-n (public; last commit 4bd67dbd, 11 Nov 2026): a law on a bounded interval whose absolutely continuous part has positive mass is n-CM for all n >= N(F). The independent referee D0007AR (13 Nov) graded it MINOR, for two reproducibility defects in the claim bundle and none in the proofs. It contradicts the negative claim in Yin-Zhu arXiv 1706.05499v4 Example 2.4: their arcsine-type mixture is n-CM for every n >= 388 pi sqrt3 / alpha_1"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T17:51:36.768Z
---

D0007, rank 50 on the 200 list. Source: Ruodu Wang, "Current open questions in complete mixability", arXiv 1411.6190,
Open Problem 7, PDF p.17. Puccetti, Wang and Wang show that a law on [a,b] with density f >= 3/(n(b-a)) is n-CM. Can
the lower bound on the density be dropped?

Status 13 Nov 2026: answered yes, by our own posted paper. Not refereed by a journal.
- Paper: the author, "Absolutely continuous laws on a bounded interval are completely mixable for all large n",
  https://github.com/yspennstate/complete-mixability-large-n (public; commits 8-11 Nov, head 4bd67dbd "Add
  references"). Theorem 1: if F is supported on a bounded interval and its absolutely continuous part has positive
  mass, there is N(F) with F n-CM for every n >= N(F). The proof convolves F with itself so that F*F dominates
  q U[c-H, c+H], then uses a reservoir of uniform coordinates to absorb an arbitrary remainder. The explicit bound is
  n >= (6R/H + 1)/q, where R is the support length.
- Independent referee, referee_reports/2026-11-13/D0007AR/REPORT.md: MINOR. It checked the Wang-Wang 2011 monotone-
  density input against the author manuscript, the reservoir weighting, the weak-limit step and the odd-dimension
  case. Its two required fixes concern the claim bundle, not the paper: run the scripts from claim_files/, and four
  source PDFs listed in the manifest are not bundled. A second run, D0007A, is in the same folder.
- Conflict in print: Yin and Zhu, arXiv 1706.05499v4 (revised 11 May 2023), Example 2.4, claim the mixture
  f = sum alpha_m C_m x^{2m}/sqrt(1-x^2) on (-1,1) fails in every odd dimension, as a counterexample to this question.
  The referee's reconciliation: F >= (alpha_1/(4 pi sqrt3)) U[1/2,3/4], so the theorem gives n-CM for every
  n >= 388 pi sqrt3/alpha_1 (4223 for alpha_m = 2^-m). Their Example 2.1 obstruction needs a central-mass bound that
  fails for any fixed one of these laws as n grows, and the step from "harder examples for each n" to one fixed law is
  missing. The referee also found their Example 2.1 equality case false as stated (a three-variable counterexample is
  in the report).
- My arXiv check on 13 Nov (with D0005): no other paper on this question since 2014.
- Earlier work: the 8 Sep pass D0007-A001 (mixing with a common centre keeps complete mixability; an asymmetric gap
  blocks pairing pieces about the mean), and PROB20-07 (14-17 Sep, a finite-n corrector criterion, proved).
- Not settled by the paper: the smallest threshold N(F) for a given asymmetric density. No threshold is uniform over
  all such laws.

Related: [[d0005_convex_body_complete_mixability_open_no_new_lit_halving_route_2026_11_13]] (previous item, same source).
