---
name: c0133_cookie_walk_zero_speed_on_non_transience_all_d_resolved_2026_11_13
description: "KZ Problem 4.7 excited random walk Z^d: speed zero on the non-transience event, all d, any iid elliptic stacks: PROVED via consumed-prefix bound + Zerner 2002 Lemma 3"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T03:32:15+02:00
  status: verified
  evidence: "C0133A proof + referee C0133AR ACCEPT + an agent step check"
---

C0133 = Kosygina-Zerner survey (Bull. Inst. Math. Acad. Sin. 8 (2013), arXiv:1204.1895) Problem 4.7: for excited random walk on Z^d with iid elliptic cookie stacks (any stacks, infinite allowed), is X_n/n -> 0 a.s. on the non-transience event N = {|X_n| not -> infinity}? Resolved YES in every dimension, 13 Nov 2026.

Proof shape (Codex C0133A, 20 min): (1) N is the union over x of {x visited i.o.}; KZ Lemma 3.18 rules out paths bounded below in a coordinate that do not go to +infinity. (2) Keep each finite consumption history p (length <= c, ends on the start hyperplane); q_L^p = chance of reaching level L before returning, in the pristine half-space with p's cookies consumed; P(A_e)=0 forces q_inf^p = 0, so a_L(c) = sum_p E q_L^p -> 0. (3) At the first arrival at level m the half-space ahead is pristine, so P(reach m+L with last visit to m within c steps | F_{T_m}) <= a_L(c). (4) Martingale SLLN over levels gives the frequency bound. (5) Zerner 2002 ECP Lemma 3 counting turns positive limsup speed into a contradiction. (6) Kalikow-type zero-one law (KZ Thm 3.16) finishes.

The new ingredient over Zerner's RWRE proof: position alone no longer fixes the future law, so the strong Markov restart is replaced by summing over the finitely many consumed prefixes and bounding their probabilities by 1.

Audits: referee C0133AR ACCEPT (minor: write L > c explicitly; hitting times are the nonnegative levels); my own step-by-step read of steps B-F found no gap. d=1 was already in print (Amir-Berger-Orenshtein 2016, Thm 1.3). Ellipticity alone allows permanent two-site trapping (speed 0, not a counterexample), so recurrence must not be read as visiting every site.

Records: brain 06_math_research/referee_reports/2026-11-13/C0133A (c71b2fd8), C0133AR; ledger intake claude row. Paper to an agent. Related: [[c0134_positive_cookie_ballisticity_resolved_two_audits_2026_11_13]], [[e0018_switching_rate_instability_two_intervals_resolved_unrestricted_2026_11_13]].

