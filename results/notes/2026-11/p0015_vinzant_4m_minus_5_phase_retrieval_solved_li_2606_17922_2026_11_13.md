---
name: p0015_vinzant_4m_minus_5_phase_retrieval_solved_li_2606_17922_2026_11_13
description: "P0015 (Randomstrasse101 2025 Conjecture 19(a,b), Vinzant: a complex Gaussian (4M-5) x M matrix gives an injective phase retrieval map with probability p_M < 1, and p_M -> 0) is solved in a preprint: Zhangsong Li, arXiv 2606.17922 (16 Jun 2026), p_M < 1 and p_M = O(1/M); AI-generated, human-verified, unrefereed. Its twin P0016 (Gaussian Open Problem 21) is the I0096 memory"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T14:58:28.419Z
---

P0015, rank 32 on the 200 list. Source: Bandeira et al., "Randomstrasse101: Open Problems of 2025" (arXiv 2603.29571),
Entry 10, Conjecture 19(a,b), which restates a conjecture of Cynthia Vinzant. A in C^{N x M}, N = 4M-5, i.i.d. standard
complex Gaussian entries; p_M = probability that x -> (|<a_i, x>|)_i is injective modulo a global phase. 4M-4 generic
measurements always suffice (Conca-Edidin-Hering-Vinzant), so 4M-5 is the first count below the generic threshold.

Solved in a preprint: Zhangsong Li, "Resolution of Vinzant's Conjecture on Phase Retrieval Injectivity", arXiv 2606.17922
(16 Jun 2026, 13 pages). Abstract: p_M < 1 and p_M = O(1/M) as M -> infinity, so both (a) and (b). The abstract says the main
result was obtained with generative AI (GPT6-Astra, GPT 5.6-sol, the Rethlas system); the arXiv comment reads "AI generated,
human verified". Not refereed; only the abstract was read here (13 Nov 2026). The point to check, if it ever matters, is
whether "p_M < 1" covers every M >= 2 or only large M.

Ours: one 6 Sep first pass (codex_20h) settled M = 2 by a Hermitian kernel argument and stopped at M > 2.

P0016 (rank 33, same Entry 10, Open Problem 21: worst square-submatrix conditioning of a (2M-1) x M Gaussian frame) is the
same question as I0096 and is answered for Gaussian entries by the author's own preprint arXiv 2607.06249 (omega = 4^{-M+o(M)})
and by Haggblom 2609.28198: see [[i0096_balan_wang_conj20_open_gaussian_op21_solved_2026_11_13]]. Both entries of Entry 10
on our list are therefore settled in print, and the deterministic Balan-Wang Conjecture 20 stays open.
Lesson again: check MEMORY.md and the author's own arXiv list before a literature search
([[intake_ledger_blind_to_posted_papers_filter_by_repo_readmes_2026_11_13]]).
