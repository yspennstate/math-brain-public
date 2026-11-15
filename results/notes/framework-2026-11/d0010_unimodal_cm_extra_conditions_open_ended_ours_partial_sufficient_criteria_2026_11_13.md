---
name: d0010_unimodal_cm_extra_conditions_open_ended_ours_partial_sufficient_criteria_2026_11_13
description: "D0010 (Wang, Current open questions in complete mixability, arXiv 1411.6190, Open Problem 10: extra conditions under which a unimodal law on a bounded interval is n-CM, especially when the mean condition holds with equality) is still open-ended on 13 Nov 2026: no characterization in print and nothing new on arXiv. Ours, self-checked and not refereed: a necessary condition at the boundary (8 Sep A001: a complete mix there is an exchangeable composition of b-a, forcing F(a+x) >= 1 - (b-a)/(n x)), and the P20 successor run's sufficient criteria (16-17 Sep: layer transport, an explicit nonmonotone tight-boundary n-CM family for every n >= 3, a paired-flank criterion for mode = mean). Our D0007 large-n theorem does not reach it: it gives n >= N(F), and the boundary case fixes n"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T17:58:54.690Z
---

D0010, rank 51 on the 200 list. Source: Ruodu Wang, "Current open questions in complete mixability", arXiv 1411.6190,
Open Problem 10, Section 2.8, PDF p.18. The mean condition a + (b-a)/n <= mu <= b - (b-a)/n is known not to suffice
for a unimodal density on [a,b]. Under what extra conditions is such a law n-CM? The case of interest is equality in
one of the two inequalities.

Status 13 Nov 2026: open, and open-ended: the question asks for conditions, so partial sufficient criteria do not close
it.
- My arXiv check on 13 Nov: mixability with unimodal, with bounded support, and the phrase "complete mixability".
  Nothing new since 2014; the hits are Zhang-Li-Yin 1711.05085 (elliptical) and Puccetti-Rigo-Wang-Wang 1704.02660
  (centres without a mean). The arXiv phrase search returns few hits for this field, so a missed journal-only paper is
  possible.
- Our results, none refereed:
  - 8 Sep pass D0010-A001: at mu = a + (b-a)/n, a complete mix is an exchangeable random composition of the fixed total
    b - a into n nonnegative parts, which forces F(a+x) >= 1 - (b-a)/(n x). This necessary condition is not in the
    source.
  - open-problems-repo proofnet24/P20-closure-log-unimodality/successors/D0010 (16-17 Sep, six runs, retired
    PARTIAL): LAYER-TRANSPORT-03 (finite interval-layer sufficient criterion), NONMONOTONE-ALL-N-03 (one formula giving
    nonmonotone, non-symmetric tight-boundary n-CM densities for every n >= 3), PAIRED-FLANK-CM-06 (a sufficient
    criterion for unimodal densities with mode = mean, through flank quantiles). Self-checked, with a P26 audit script.
- Our posted D0007 paper (github.com/yspennstate/complete-mixability-large-n; see
  [[d0007_cm_large_n_answered_by_our_paper_referee_minor_yin_zhu_example_false_2026_11_13]]) proves n-CM for all
  n >= N(F). The tight boundary pins one n for a given law, so that theorem says nothing here.
- There is no Codex report for D0010 in referee_reports/2026-11-13.
- Where an attempt could start: at the boundary the question becomes which unimodal marginals admit an exchangeable
  composition of a fixed total into n parts, which is a transport feasibility problem on the simplex. A clean answer
  for monotone densities at the boundary would be the natural first theorem.

Related: [[d0007_cm_large_n_answered_by_our_paper_referee_minor_yin_zhu_example_false_2026_11_13]] (previous item, same
source).
