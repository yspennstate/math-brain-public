---
name: e0007_two_type_contact_unequal_death_rates_open_stover_partial_2026_11_14
description: "[PROVISIONAL] E0007 (Durrett 2009 coexistence survey Problem 1, Neuhauser's BDR conjecture: in the two-type contact process on Z^d with unequal death rates the type with the larger beta/delta wins) still open 14 Nov 2026; equal deaths settled (Neuhauser 1992, Mountford-Pantoja-Valesin linear takeover); only partial: Stover 1908.06628 (SPL 2020) sufficient condition via Broman's point-process coupling; OpenAlex shows one later citer, not on the lattice"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-14T03:23:51.280Z
---

E0007, our 200-list rank 71. Two types on Z^d; type i gives birth onto an empty neighbour at rate beta_i and dies
at rate delta_i. Conjecture (Neuhauser; Durrett, Ann. Appl. Probab. 2009 coexistence survey, Problem 1): if
beta_1/delta_1 > beta_2/delta_2 then type 2 dies out (no coexistence on the lattice).

Status 14 Nov 2026 (an agent, one extended web search + OpenAlex forward citations):
- Equal death rates: proved, Neuhauser 1992 (multitype duality); Mountford-Pantoja-Valesin: the winner takes a
  linearly growing ball.
- Unequal death rates: open. Stover, "A stochastic comparison result for the multitype contact process with
  unequal death rates", arXiv 1908.06628, Statist. Probab. Lett. 2020 - a sufficient condition for the dominant type
  to survive, via Broman's point-process coupling; it calls the BDR conjecture long-standing and open.
  OpenAlex: one citer (cooperative two-type SIR on Galton-Watson trees, Kybernetika 2025) - not this question.
- Our 8 Sep attempt (E0007-A001): the obstruction is real - with delta_1 != delta_2 the ancestral dual has to know
  its own type to run its death clock, and the system is not attractive in the order that favours type 1.

What would change this: a later paper proving BDR in some d, or a counterexample. Next idea if reopened:
Stover's coupling plus a block construction comparing type 1 with a supercritical one-type process restricted
to the region type 2 has vacated.
