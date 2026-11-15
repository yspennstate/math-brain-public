---
name: c0006_dgff_cluster_law_depth_growth_conj_16_6_open_2026_11_13
description: "[PROVISIONAL] C0006 (Biskup PIMS notes arXiv 1712.09972, Conj 16.6: lim e^{-alpha h} E_nu(f_h) in (0,inf) for the DGFF cluster law) still open; companion of Conj 16.5 (deep level set ~ c t e^{alpha t} Z^D(A)); BGL near-maxima 2020 is a different depth"
metadata:
  type: project
status: provisional
---
C0006, rank 7 on the 200 list. Biskup, Extrema of the two-dimensional discrete Gaussian free field (PIMS-CRM notes, arXiv 1712.09972), Conjecture 16.6: for the cluster law nu of Biskup-Louidor and f_h = the number of cluster points within h of the top, e^{-alpha h} E_nu(f_h) converges to a limit in (0,inf), with alpha = 2/sqrt(g).

Context from the notes (text read 13 Nov 2026): Conjecture 16.5 (size of deep extremal level set) states that (1/t) e^{-alpha t} #{x in Gamma_N(t): x/N in A} converges in law, as N then t go to infinity, to c Z^D(A). Theorem 9.1 gives only e^{ct} <= |Gamma_N(t)| <= e^{Ct}, and the notes remark |Gamma_N(t)| = e^{(alpha+o(1))t}. The notes reach 16.6 from 16.5 by the substitution lambda = t^{-1} e^{-alpha t} in the Laplace transform of |Gamma_N(A,t)|, using Theorem 9.2 and truncation of the maximum.

Literature, checked 13 Nov 2026 (three web searches, the near-maxima PDF read in full):
- Biskup-Gufler-Louidor, Near-maxima of the 2D DGFF, arXiv 2010.13939: values about sqrt(log N) below the maximum; limit cLQG x Rayleigh. A different depth scale. Its full text never mentions the cluster law or Conjectures 16.5/16.6, so it does not settle them.
- Biskup-Louidor, Full extremal process, cluster law and freezing (Adv. Math. 2018, arXiv 1606.00510): constructs nu. No growth asymptotics.
- No paper from 2021-2026 found on the depth growth of the cluster law.

Status: open. The natural route goes through 16.5: the t e^{alpha t} level-set count at fixed depth t, combined with the decorated Poisson structure with intensity Z^D(dx) e^{-alpha h} dh. How to apply: a P0xxx-style attempt should start from the Laplace-transform identity in the notes, not from scratch.
