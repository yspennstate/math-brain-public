# C0029 statement-only packet for w568

Let B_n be n by n with all entries independent and uniform on {-1,+1}; it is neither symmetric nor a 0/1 matrix. Let s_min(B_n)=min_{||x||_2=1}||B_n x||_2. The target is an exact coefficient of one: there exist absolute C,c>0 such that, for every n and every epsilon>=0,

P(s_min(B_n)<=epsilon/sqrt(n)) <= epsilon + C exp(-c n).

This is the exponential-remainder version of the historical conjecture; the original b^n convention and quantifiers will be separately checked. For epsilon>=1 the inequality is trivial. For epsilon=0 it concerns singularity alone. A bound with C'epsilon or (1+o(1))epsilon does not settle this target.

Primary source: Sah, Sahasrabudhe, Sawhney, On the Spielman-Teng Conjecture, arXiv:2405.20308v2 (8 January 2025), Introduction equation (2), Theorem 1.1. https://arxiv.org/html/2405.20308v2

Theorem 1.1 proves an upper bound (1+C_xi(log n)^(-1/16))epsilon + exp(-Omega_xi(n)) for mean-zero variance-one iid real subgaussian entries. This includes Bernoulli, but leaves a coefficient loss. Exact current openness as of 10 October 2026: UNKNOWN pending a targeted check for later primary work and owner's retired results.

This file deliberately contains the target and source boundary only; no proof strategy is included. Please attempt an independent obstruction or adversarial check, then review the later proof packet separately.
