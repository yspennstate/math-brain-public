---
name: lo05_h10_over_q_openai_preprint_section5_checked_2026_11_12
description: "Hilbert's tenth problem over Q claimed undecidable (OpenAI preprint, 62 pages, Oct 2026): finite rational tests, rank-one curve y^2 = x^3 - d^2 x over Q(sqrt 2), five-point odd-contact height estimate via the discriminant-210 Shimura curve. Depends on two other OpenAI preprints (Fontaine-Mazur at 2, pointwise 2-converse). Section 5 checked 17 of 17; 50 pages unread; Sun 2610.20691 builds on it - keep REPORTED_SOLVED"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T04:57:54+02:00
  status: provisional
  evidence: "06_math_research/lo05_h10_over_q_agent_2026_11_12/LO05_CHECK.md, lo05_check.out; push 5554529ee84fd2edff4eaf5219f8684d34c0095a"
---

Row LO05 of the top-200 general list (Hilbert's tenth problem over Q) is claimed solved negatively by one OpenAI preprint (openai/math, 62 pages, versions of 24 Sep and 6 Oct 2026, identical apart from dates) and confirmed by nobody independent as of 12 Nov 2026.

The proof gives no existential definition of Z in Q and no Diophantine model, so Mazur-conjecture obstructions do not apply. For each f it builds finite tests answered by rational-solvability queries with: f has an integer zero iff every test succeeds. Compactness, a rank-one elliptic group (E: y^2 = x^3 - d^2 x over Q(sqrt 2), d = 75 - 53 sqrt 2) carrying additive integer indices, truncated formal logarithms on E and its conjugate, and a height estimate h(s) <= H M(s)^c on the projective line minus five points, M(s) the product of primes of odd contact, proved through the Shimura curve of discriminant 210, quaternionic abelian surfaces and modularity. It depends on two other OpenAI preprints, each a large claim: Fontaine-Mazur modularity at the prime 2 and a pointwise 2-converse. Z.-W. Sun, arXiv 2610.20691, takes the inputs as given and gets 86 unknowns: a second reader of the reduction, not of the inputs. No Lean entry.

Checked by us (lo05_check.py, all pass): Section 5 in full (norm of d, the point Q = (-dw, 2 sqrt 2 d^2), the two-isogeny descent giving rank 1, torsion exactly the two-torsion from 24 point counts, inequality (5.2) on 16.8 million cases); the discriminant-210 Shimura curve has genus 5, no elliptic points, and its Atkin-Lehner quotient has five branch points. Not checked: about 50 pages (Sections 2, 3, 4, 6, 7) and the two cited preprints.

How to apply: do not attack LO05; keep it REPORTED_SOLVED. A result that cites other unrefereed preprints from the same release is no more settled than they are: list the dependencies before weighing the row. Same routine as [[pd08_leray_hopf_nonuniqueness_closing_arithmetic_checked_2026_11_12]] and [[nt02_landau_siegel_zeros_excluded_proof_read_in_full_2026_11_12]].

Evidence: 06_math_research/lo05_h10_over_q_agent_2026_11_12/LO05_CHECK.md, lo05_check.out.

