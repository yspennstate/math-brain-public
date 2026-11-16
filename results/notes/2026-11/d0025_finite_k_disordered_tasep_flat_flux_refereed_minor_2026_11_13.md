---
name: d0025_finite_k_disordered_tasep_flat_flux_refereed_minor_2026_11_13
description: "[PROVISIONAL] Seppalainen Problem 4 (site-disordered TASEP K-exclusion flat flux at K/2): yes for every finite K, every nonconstant law, after two audits (D0025A + D0025AR MINOR)"
metadata:
  node_type: memory
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T10:27:04+02:00
  status: provisional
  evidence: ""
  modified: 2026-11-13T09:53:53.879Z
---

Seppalainen arXiv:math/9906194 Sec 4 p.9 Problem 4 asks whether the flux f_K of the site-disordered totally asymmetric K-exclusion (generator (3.1) p.8: one departure clock alpha_i per site, independent of occupation) has a flat segment around rho=K/2. Result (D0025A, referee D0025AR verdict MINOR, 13 Nov 2026): for every finite K and every nonconstant iid law on [r,1] with ess inf r>0, f_K(rho)=r M_K whenever |rho-K/2|<=mu r M_K, where M_K is the homogeneous rate-one K-exclusion flux maximum and mu=1/r-E[1/alpha_0]. This is a guaranteed half-width, not the critical one.

How: Sly arXiv:1609.06589 Thm 1 is K=1. His proof adds U=Ber(1-r/alpha)Exp(r) to each disordered exponential, giving Exp(r) totals, and every path must cross the intermediate columns. That argument does not use K=1. Run it on the K-exclusion growth graph T(i,h)=Y+max{T(i,h+1),T(i-1,h),T(i+1,h+K)} (Seppalainen's notes (9.40)-(9.44)). The K=1-specific parts of Sly's proof are only the explicit shape and the value r/4.

Referee correction: Bahadoran-Bodineau arXiv:1602.06718v4 Sec 3.2 p.13 remark that their method extends to K-exclusion. They state no all-laws finite-K theorem, so priority is unverified and a paper must cite that remark. Sly's p.2 typos (EY for EU, the k(v) branches) do not affect the proof. Ring simulations (K=1,2, independent code) support central flattening only. Files: brain 06_math_research/referee_reports/2026-11-13/D0025A and D0025AR; ledger row in probability_1000_intake_D_20260908/problems.jsonl. POSTED 13 Nov 2026 11:50 workstation: paper "A flux plateau for site-disordered finite-capacity exclusion" (11 pp) at github.com/yspennstate/flux-plateau-disordered-k-exclusion, commit 0b4bbd57, after a third fresh-reader referee (D0025PR, MINOR: no mathematical error, all five citations verified, fixes were scope/definitions/filler only). agent confirmed it held nothing on Problem 4. Lesson from the release: the draft's end matter had drifted from the standard (Google-credit-only funding, "no competing interests"); paper_release_guard.py refused it until the full funding list, the equity disclosure and the Math Brain acknowledgment + three bibitems were in - copy the end matter from an already-posted paper (agent_run/arc/repo/paper/main.tex), never write it fresh. Not yet on Zenodo/ResearchGate.

Referee correction: Bahadoran-Bodineau arXiv:1602.06718v4 Sec 3.2 p.13 remark that their method extends to K-exclusion. They state no all-laws finite-K theorem, so priority is unverified and a paper must cite that remark. Sly's p.2 typos (EY for EU, the k(v) branches) do not affect the proof. Ring simulations (K=1,2, independent code) support central flattening only. Files: brain 06_math_research/referee_reports/2026-11-13/D0025A and D0025AR; ledger row in probability_1000_intake_D_20260908/problems.jsonl. Next: a paper. Status provisional until written up.
