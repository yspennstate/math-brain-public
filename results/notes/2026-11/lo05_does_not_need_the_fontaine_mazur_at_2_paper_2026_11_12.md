---
name: lo05_does_not_need_the_fontaine_mazur_at_2_paper_2026_11_12
description: "Does H10 over Q (LO05) need the new Fontaine-Mazur-at-2 paper [49]? No: its one use (r_2 of a non-CM QM surface modular) follows from Jacobson-Ohta big image, Khare-Wintenberger and Kisin at one large odd l, then traces"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T16:46:24+02:00
  status: verified
  evidence: "Kisin Ann. Math. 170 (2009) intro theorem read in the Harvard DASH copy; Dieulefait-Rotger arXiv math/0303162 Thm 1.4 read; LO05 Section 4.7 and Lemma 4.6; push 106"
---

LO05 (OpenAI's H10-over-Q preprint, folder 06_math_research/lo05_h10_over_q_agent_2026_11_12) cites [49], a new
unrefereed Fontaine-Mazur-at-2 paper, once: Section 4.7, to make the 2-adic representation r_2 of a non-CM QM
abelian surface (quaternion algebra of discriminant 210, made a G_Q-representation by quasi-isogenies mu_g and a
mu_2m-valued cochain beta) modular.

That use does not need [49]. Route (LO05_49_BYPASS.md, push 106):
1. LO05's Lemma 4.6 works at every l, so the traces of r_l are l-independent (compatible family).
2. Jacobson-Ohta (Dieulefait-Rotger arXiv math/0303162 Thm 1.4; Ohta, J. Fac. Sci. Univ. Tokyo 21 (1974)): the
   l-adic image on the field of definition of the endomorphisms is (O tensor Z_l)^* for almost every l, needing a
   maximal order (reach one by an isogeny; V_l is unchanged). So for a large l the residual image contains
   SL_2(F_l) on Q(zeta_l).
3. Kisin, Ann. of Math. 170 (2009), the theorem of the introduction: p > 2, det = cyclotomic times a finite
   character, residual absolutely irreducible on Q(sqrt(p*)) (weaker than Q(zeta_p)), residually modular, and
   potentially Barsotti-Tate at p imply modular. Residual modularity is Khare-Wintenberger.
4. Chebotarev + Brauer-Nesbitt carry modularity from r_l to r_2.

Equivalently a building block in Ribet's sense, so a factor of a GL_2-type variety over Q.

How to apply: when a paper leans on a new heavy theorem at a small prime (2 here) for a representation that comes
from geometry, check whether the representation sits in a compatible family; then one large odd prime and the
published lifting theorems may do the job, and the new theorem drops out of the dependency list.

Status: verified against the published statements (Kisin read in the Harvard DASH copy of the Annals paper, Ohta
through Dieulefait-Rotger's statement, not Ohta's own paper). LO05 itself stays REPORTED_SOLVED: its second
independent audit has not been done.

