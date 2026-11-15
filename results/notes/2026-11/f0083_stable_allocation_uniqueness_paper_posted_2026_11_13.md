---
name: f0083_stable_allocation_uniqueness_paper_posted_2026_11_13
description: "[PROVISIONAL] F0083 HHP 2006 open problem (i) (two stable allocations?) answered No for d=1,2, all d under sum 4^k/(1+N(2^k))=inf: paper posted GitHub c349c7b, Zenodo 10.5281/zenodo.24199457; d>=3 open"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T16:10:23+02:00
  status: provisional
  evidence: ""
---

Paper 'Uniqueness of stable allocations in dimensions one and two', repo github.com/yspennstate/stable-allocation-uniqueness commit c349c7b60650b53f5f4a5368b8aec9d6cdd23803 (ls-remote checked), Zenodo 24199457 (md5 1a0526e315fcd7fbab8a889203071b7b, API readback ok). RG folder ~/Downloads/career/researchgate_queue/q4/stable-allocation-uniqueness (final_c349c7b.pdf), queued for the 14 Nov 05:30 retry.

Proof: extremal allocations s (site-optimal, sites apply) and c (centre-optimal) of HHP Lemma 15; disagreement graph q(u,v)=Leb(C_u cap S_v); edges force v sated under c and T_v < T_u (radius of c-territory), so acyclic and q(u,v) <= omega_d(T_u^d - T_v^d); the part H reachable from one edge (rho,v0) has sated vertices with disjoint territories of volume alpha inside B(v,R), R=T_{v0}: packing gives O(r^d) vertices per ball and bounded degree regardless of Xi's density. HHP Prop 13 (transience from capacities, three conditions) makes H transient; Nash-Williams (Lyons-Peres (2.14)) with cutsets r_j=(ell+1)j and Cauchy-Schwarz per dyadic block makes it recurrent when sum 4^k/(1+N_H(2^{k+1}))=inf - always for d<=2. Remark: Xi_0 = union of n points packed in [n, n+1/10] has N(r)~r^2/2 and transient G_2 (unit flow energy 1), so HHP Thm 2 does not apply there while ours does.

Status/doubt: two Codex audits (F0083A claim PARTIAL for d>=3, F0083AR referee MINOR) plus my line-by-line reread against hhp.txt; no fresh-reader paper_audit (relaunch ban until 19 Nov 06:00) - run one then. Priority: literature check (arXiv, 68 OpenAlex forward cites of HHP) found nothing on problem (i); present as extension of HHP's proof. Lint 0 MUST, release guard ok. Related [[e0082_bridge_pattern_constant_paper_posted_2026_11_13]], [[f0083_stable_allocation_uniqueness_d_le_2_two_audits_partial_2026_11_13]].
