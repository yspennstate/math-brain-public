---
name: i0003_manhattan_orientation_fields_recurrence_partial_two_audits_2026_11_13
description: "I0003 Bou-Rabee-Peres Problem 3 (which Manhattan orientation fields are recurrent): partial A-E (bounded-primitive invariance, dyadic criterion, eventually-constant classification, iid+bounded transient) passed claim + referee ACCEPT; Pene 2020 and Bremont 2016 unread; Problem 3 open"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T20:20:01+02:00
  status: verified
  evidence: "mini1 agent_run/I0003A/REPORT.md (claim) and I0003AR/REPORT.md first line ACCEPT 13 Nov 21:52 Mac; local copy agent_run/i0003ar_out/REPORT.md"
---

I0003 (Bou-Rabee and Peres, "The randomly oriented Manhattan lattice in 2D is transient", arXiv:2609.07621v1, Sec 7 p.14, Problem 3: which orientation fields give a recurrent walk?) has a partial answer that passed two audits; Problem 3 itself stays open.

With two-sided primitives S,T of the row/column signs and M(r)^2 = max_{|k|<=r}|S(k)|^2 + max_{|k|<=r}|T(k)|^2:
A. fields whose primitives differ by a bounded amount have the same type;
B. sum_m 1/(1+M(2^m)^2) = infinity => recurrent (e.g. |S|+|T| = O(sqrt(log|k|))); convergence is not sufficient (the circulating field is recurrent with a convergent series);
C. eventually-constant tails: recurrent iff e_-=-e_+, f_-=-f_+, e_+f_+=-1 (two circulating arrangements); so (g(y),-g(x)) recurrent but (g(y),g(x)) transient;
D. iid horizontal signs + any bounded-primitive vertical field: transient a.s., simultaneously for all such fields;
E. classes S=O(|k|^a), T=O(|k|^b): every member recurrent iff a=b=0 (elementary from Bosi).
Method: continuous-time generator L=S+A, A antisymmetric on l^2 (counting measure invariant), resolvent symmetric part (H - A H^{-1} A)^{-1}, variational formula for the diagonal resolvent. Predecessors: Gaudilliere-Landim Lemma 5.5, Bosi Thm 9(i).

Referee I0003AR (13 Nov, ACCEPT): no error in A-E; one recurrent site forces irreducible recurrence (P^T is stochastic). Novelty is a bounded search only: Pene's 2020 survey and Bremont's 2016 paper were not read by either run; read them before any paper. Ledger row PARTIAL 2026-11-13T20:15. Local copies agent_run/i0003ar_out/.

