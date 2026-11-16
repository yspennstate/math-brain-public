---
name: p0230_posted_public_and_guard_before_create_2026_11_16
description: "[VERIFIED] Aldous Open Problem 35 (span length of k points in the Poisson-line SIRSN) posted 16 Nov 2026 at github.com/yspennstate/sirsn-k-point-span-length; and a posting-order rule: run the paper checks before the repository is created, or it sits public and empty."
metadata:
  type: project
  created: 2026-11-16
  status: verified
---

The paper on Aldous's Open Problem 35 for the planar Poisson-line SIRSN (E L_k / k converges, every gamma > 2) is public at
https://github.com/yspennstate/sirsn-k-point-span-length, with README, LaTeX source, PDF and a SHA256SUMS file. An
anonymous download of the PDF and the source matched the checksums. Three first-reader audits found no mathematical
error; the third asked for minor edits, all made before posting. An outside audit by a second model is still owed.

Credits. The problem is D. Aldous's (Open Problem 35 of his SIRSN paper); the Poisson-line construction is W. S. Kendall's;
the upper bound adapts Kahn's Proposition 6.1 and the exit-tail argument from the proof of Kahn's Proposition 5.1. The
earlier working notes are `p0230_sirsn_span_length_reduced_to_one_route_tail_2026_11_14` and
`p0230_sirsn_k_point_span_length_settled_poisson_line_case_2026_11_16`.

Posting-order rule. The posting script created the public repository and then pushed. The pre-push paper guard refused
the paper (its acknowledgements had to name the agents and cite the Math Brain paper), so the repository stood public
and empty for about ten minutes. Run the paper guard on the source before creating the repository. Two smaller points:
a secret scan of staged changes fails in a repository with no commits, so scan by file there; and the hosting site's
REST rate limit is shared by every agent on the account, so check it before a posting run.
