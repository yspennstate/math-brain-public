---
name: dg06_caratheodory_smooth_counterexample_checked_2026_11_12
description: "Caratheodory and Loewner conjectures false for smooth surfaces (Alpoge; Ando-Umehara 2610.34036): construction checked by hand and numerically; local index 1+k/2 shows only on very small circles; real-analytic case untouched"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:33:26+02:00
  status: verified
  evidence: "06_math_research/dg06_caratheodory_agent_2026_11_12/DG06_CHECK.md, dg06_check.out, dg06_index2.out; push 25bb8bd1f66edc4f1a05533769f3582bf0e8a8fd"
---

Row DG06 (Carathéodory conjecture), 12 Nov 2026.

The smooth Loewner and Carathéodory conjectures are refuted (Alpöge, announced 19 Aug 2026; shorter construction arXiv 2610.34036, Ando and Umehara). Seed F(x+iy) = a(x) - a(y) + sin x sin y, a(t) = sin^4 t + 3 sin^2 t, whose trace-free Hessian never vanishes (4 F_zz = 12 - 16(sin^4 x + sin^4 y) - 2i cos x cos y). Local: H_k(z) = exp(-|z|^(-k/4)) F(z^(-k/2)) has an isolated singularity of index 1 + k/2. Global: support function rho = 1 + eps f/(1+|W|^2), f = exp(-delta (1+|W|^2)^(1/4)) F(W), gives a strictly convex closed C-infinity surface with one umbilic, of index 2.

Checked by hand: Lemma 1.1, Lemma 2.1, the identity rho_WW + (2 conj(W)/D) rho_W = eps f_WW/D, Lemma 1.4, Theorem 2.2. Checked numerically: c = inf|F_zz| = 0.1761; delta = 0.03 satisfies (2.3); min |f_WW|/b = 0.1618 > c/2 on |X|,|Y| <= 45; the umbilic criterion against the surface built in R^3 (19 digits); index 1.5, 2, 2.5, 3 for k = 1..4 on small circles by two routes.

Worth remembering: on circles of ordinary size the index of H_k is NOT 1 + k/2 (k = 1: 0.5 at |z| = 0.35, 2.5 at 0.11). The leading term F_ww w'^2 dominates F_w w'' only when |z|^(-k/2) is large (about 50 for k = 1), and H_k has other singular points further out. A local index claim has to be tested on circles small enough for the asymptotics, with the sampling density stated; my first run at |z| = 0.35 looked like a refutation and was not one.

Conflict: Guilfoyle and Klingenberg (arXiv 0808.0851) claim the conjecture for C^{3,alpha} surfaces; it cannot stand beside this surface. The real-analytic case (Hamburger, Bol, Klotz, Titus, Ivanov; quoted from memory, not re-read) is untouched.

Files: 06_math_research/dg06_caratheodory_agent_2026_11_12/ (DG06_CHECK.md, dg06_check.py, dg06_index.py, dg06_index2.py and outputs). Row proposal: replace, or restate to the real-analytic case with its status. Related: [[ag05_jacobian_dim3_counterexample_recomputed_exactly_2026_11_12]], [[lo01_vaught_infinitary_counterexample_first_order_open_2026_11_12]].

