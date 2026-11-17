---
name: fei_li_han_withdrawn_constant_is_kms_claim_4_1_swapped_in_ten_papers_2026_11_16
description: "[VERIFIED] FEI 1/ln2 Han constant: Li-Han 2512.03117 is withdrawn; cite Keller-Mossel-Schlank Claim 4.1 (2012). Swapped in all ten FEI repos 16 Nov"
metadata:
  type: project
  created: 2026-11-17
  created_at: 2026-11-17T00:06:07+02:00
  status: verified
  evidence: "arXiv abs page of 2512.03117 shows withdrawn; KMS PDF Claim 4.1 read; ten repos pushed and fetched in sync 16 Nov"
  supersedes: fei_papers_miss_li_han_sharp_constants_2512_03117_2026_11_12
---

The 1/ln 2 form of Han's FEI bound is not a Li-Han result. arXiv:2512.03117 (Li and Han) is WITHDRAWN on arXiv, and the inequality it claimed already follows from Keller, Mossel and Schlank, "A note on the entropy/influence conjecture", Discrete Math. 312 (2012), no. 22, 3364-3372, doi 10.1016/j.disc.2012.07.031, arXiv:1105.2651, Claim 4.1: Ent(f) <= sum_i h(I_i(f)) by subadditivity of entropy. Since h(t) <= t log2(1/t) + t/ln 2, this gives H(f) <= I(f)/ln 2 + sum_i I_i log2(1/I_i), which is Han's bound with 1/ln 2 in place of 2+3/ln 2, for every real f with sum f^(S)^2 = 1. Claim 4.1 is at line 554 of the text extracted from the KMS PDF.

Done 16 Nov 23:5x (an agent): all ten FEI papers now cite KMS Claim 4.1 in place of LH25, with "sharp" dropped because sharpness of 1/ln 2 was not checked. Heads: fei-equivalent-forms 5546484, fei-filtration-witness 5328f1f, fei-forced-coordinate-bias 2f22882, fei-forced-coordinate 96da1a3, fei-good-coordinates fe5a989, fei-hidden-coordinates 24e81ce, fei-linear-dnf-census b901d30, fei-sparse-linear-dnf b3d3a79, fei-variance-han-bound d1e8f1e, fourier-entropy-influence-one-coordinate 6eab332. Each builds clean (0 undefined, 0 overfull). Zenodo new versions wait on each paper's paper_audit; an agent holds the 11 FEI ResearchGate uploads in q4 until it gets the new ids. Hold file: Downloads/career/researchgate_queue/q4/CITATION_HOLD_FEI.md.

**Why:** the 12 Nov citation hold told agents to add Li-Han as the sharp constant. That premise was wrong: the preprint is withdrawn and the result is ten years older than Han's paper.

**How to apply:** for the 1/ln 2 constant in an FEI paper, cite KMS Claim 4.1, never 2512.03117. Before citing any arXiv preprint as the source of a constant, open its abs page and check for a withdrawal notice. Related: [[t021_fei_dossier_written_li_han_2512_03117_is_withdrawn_2026_11_03]], [[fei_papers_miss_li_han_sharp_constants_2512_03117_2026_11_12]].

