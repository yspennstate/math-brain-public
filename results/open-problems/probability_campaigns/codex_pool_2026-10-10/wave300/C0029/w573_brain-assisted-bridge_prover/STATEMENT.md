# C0029 exact target for independent adversary

Let B_n be an n by n real matrix whose entries are mutually independent and each equals -1 or +1 with probability 1/2. Let s_min(B_n)=min_{||x||_2=1}||B_n x||_2. Seek one constant c in (0,1), independent of n and t, such that for every positive integer n and every t>=0,

P(s_min(B_n)<=t/sqrt(n)) <= t+c^n.

Equivalent eventual-in-n statements with an exponential prefactor can be converted after handling finitely many n; the exact coefficient of t is the issue. Do not replace it by an unspecified C or by 1+o(1).

Primary source recovered: Sah, Sahasrabudhe, Sawhney, On the Spielman-Teng Conjecture, arXiv:2405.20308v2 (2025-01-08), https://arxiv.org/abs/2405.20308 . It resolves the conjecture up to a 1+o(1) factor, not by that description the exact target above. Exact theorem and original ICM source are still being checked. Current exact openness: UNKNOWN; no novelty claim.

Independent adversary: w574. Referee: w575. This file deliberately contains the statement and assumptions before any proof details.
