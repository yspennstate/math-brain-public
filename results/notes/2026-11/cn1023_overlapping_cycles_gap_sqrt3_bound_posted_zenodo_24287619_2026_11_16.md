---
name: cn1023_overlapping_cycles_gap_sqrt3_bound_posted_zenodo_24287619_2026_11_16
description: "[VERIFIED] APW 2008 open problem 2 (overlapping-cycles single-card gap <= (2pi^2/sqrt3+o(1)) k^(1/2) n^-2)? Yes: gamma is a determinant-2 plane lattice minimum, Hermite bound, equality at (26,12). Posted: repo overlapping-cycles-gap-bound 95edfb4 tag v1.0, Zenodo 10.5281/zenodo.24287619, POSTED a8edcc69"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T19:54:08+02:00
  status: verified
  evidence: "audits/reports/2026/11/16/overlapping_cycles_gap_bound (REFEREE_REPORT.md, REFEREE_ADDENDUM_agent.md, SIGNOFF_72de1487.md, gap_check_rerun_mini2.txt; brain commit 5a79955b); fresh-clone sha256sum -c at tag v1.0; Zenodo 24287619 md5 readback"
---

Angel, Peres and Wilson (Ann. Appl. Probab. 18 (2008) 1215-1231, arXiv 0707.2994), open problem 2: does the single-card
gap of the overlapping-cycles shuffle satisfy gap(n,k) <= (2 pi^2/sqrt 3 + o(1)) k^(1/2) n^(-2)? Yes.

Proof in one line: with A = sqrt(k)/n and theta = 1 - k/n, their gamma(n,k) = (pi^2 sqrt(k)/(2n^2)) mu, where mu is the
minimum squared length over m != 0 in the lattice spanned by (sqrt A, theta/sqrt A) and (0, 2/sqrt A), determinant 2
(m = 0 vectors have squared length > 4). Lagrange-Gauss gives mu <= 4/sqrt 3, so gamma <= (2 pi^2/sqrt 3) k^(1/2) n^(-2)
for every n, exactly; APW Theorem 4 (gap = (1+o(1)) gamma uniformly in k) finishes. Equality at (n,k) = (26,12), m = 3:
the lattice is hexagonal. APW's own Dirichlet argument (p. 13) gives 2 pi^2; they already noted the sqrt 3 constant is
asymptotically sharp for gamma (Section 6) and that gamma "appears to be no larger" than it (Figure 5).

Posted 16 Nov 2026: public repo yspennstate/overlapping-cycles-gap-bound, main 95edfb4ac5d42ff709e0bbdc872b1ede844fbcd6,
tag v1.0 (paper, code/gap_check.py, SHA256SUMS verified from a fresh clone); Zenodo 10.5281/zenodo.24287619 (record
24287619, PDF md5 b635f31d348d2e87a406afecf95c3301, 9 references read back); POSTED row open-problems-repo a8edcc69.

Audits: referee report an agent (SOUND, 0 MUST, 3 SHOULD, all applied), addendum an agent with its own
check code (agrees; added the gap = 1 - largest modulus convention, the chain is not reversible), sign-off
SIGNOFF_72de1487.md on the v2 diff. Every Section 3 number re-run with the public gap_check.py on a second machine
(max gamma n^2/sqrt k = 11.396437516 at (26,12) for n <= 2000; gap/gamma at k/n = 0.79: 0.794, 0.791, 0.991, 0.975 at
n = 750, 1500, 3000, 6000; at 0.7407: 0.741, 1.005, 1.002). Staging and evidence: brain-repo
12_cognitive_architecture/audits/reports/2026/11/16/overlapping_cycles_gap_bound/ (commit 5a79955b).

Posting scars from this one: (1) the paper repo pre-push guard refuses acknowledgements that do not use the author's
8 Nov standard text (Claude and Codex, Math Brain, Brain framework) and a Math Brain paper entry without the
math-brain-2026-10-24 URL; copy the block from an already-posted paper before the first push. (2) The DOI
10.1214/105051606000000097 for Jonasson 2006 is a 404; Crossref's 10.1214/10505160600000097 resolves. (3) An anonymous
200 on github.com/<repo>/tree/<tag> is returned even for an empty repo; check the tag with git ls-remote or a raw file.
(4) sed with backslashes through the Bash tool writes control characters into .tex; use Edit or a Write-tool script.

