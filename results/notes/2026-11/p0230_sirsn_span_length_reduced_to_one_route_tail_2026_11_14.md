---
name: p0230_sirsn_span_length_reduced_to_one_route_tail_2026_11_14
description: "[PROVISIONAL] P0230 (Aldous SIRSN OP35, E len span of k pts in square area k ~ ell k): reduced via axiom p(1)<inf - exterior up to distance D costs O(sqrt(k) log D + D); OP35 holds if one-route tail h(t)=o(t^-3); unaudited"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T16:52:44+02:00
  status: provisional
  evidence: ""
---

Status: provisional, written once and reread once, needs an independent audit. Key step: a span point at distance d outside the square is at distance >= d from both endpoints, so lies in E(lam,d), whose intensity is <= p(d) = p(1)/d (scaling (30) plus monotonicity in lam); dyadic shells give p(1)(4L log2 D + 6 pi D). The inside is <= ell lam^{1/2} k via Poisson domination (N independent Poisson(lam k), lam = 1 + k^{-1/3}; the N<k correction is k^{5/2} e^{-c k^{1/3}}). Lower bound liminf >= ell is the 6 Sep local truncation (P0230-A001). Far part beyond D by a union bound over k^2 pairs: k^{5/2} h(D/(sqrt2 L)). Hence OP35 iff the far part beyond some D(k)=o(k) is o(k); sufficient h(t)=o(t^-3). Open: the tail in Kendall's Poisson-line SIRSN (Ann. Probab. 2017); a count of distinct far segments instead of k^2. Files: brain-repo/12_cognitive_architecture/math/trio_1011/op/P0230/NOTE.md. Related [[p0175_free_conv_symmetric_unimodal_no_counterexample_fid_subclass_2026_11_14]] (same loop).
