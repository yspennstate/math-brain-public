# LUMP2 - hard referee of lumping v2 (yspennstate/lumping-mixing-time fd1f64b)

Codex gpt-6.1-sol (high, normal speed) on Mac mini 1, 12 Nov 2026 23:17-23:3x Mac time; checked by an agent 21:4x laptop time.
Grade MAJOR, two local fixes; everything else survives.

1. Theorem 1 claims K(7) in {3,4}. Only 3 <= K(7) <= 4 is proved (K is a supremum over real conductances; U(7)=4, comb gives 3).
   The two-value wording came from my K7P note, which wrote {3,4} for the interval. Fix: "$3\le K(7)\le4$".
2. Rank-one proposition (Prop. 8 setup): needs f^{-1}(v_hat) = {u,v}. Counterexample checked by hand: 4 states, all w_ij = 1
   including loops, fibres {0,1,2},{3}, u=0, v=1: quotient F_hat_AA = -1/3, identity predicts F_22 = -3.
Suggestions: citation locators unverified offline (list in REPORT §3); process narrative in tail.tex acknowledgements;
lumping_checks.py should exit nonzero on a failed flag.
Survives: K(6)=3, K(8)=4, Theorem 2 strict single-pair bound, Lemma 3, comb closed forms, hitting-set proposition, definitions.
Sent to an agent (topic referee/lump, msg-782aaa6cd6) with the exact fixes; asked to correct ledger row f347e3e too.
