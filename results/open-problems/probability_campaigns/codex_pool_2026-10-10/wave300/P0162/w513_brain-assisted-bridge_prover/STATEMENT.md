# P0162: exact statement for an independent first attempt

For n >= 1 equip {-1,1}^n with uniform product probability. For a Boolean f:{-1,1}^n -> {-1,1}, define chi_S(x)=product_{i in S} x_i and fhat(S)=E[f chi_S]. Parseval gives sum_S fhat(S)^2=1. Use logarithms to base two, with 0 log2(1/0)=0.

H(f)=sum_{S subset [n]} fhat(S)^2 log2(1/fhat(S)^2).
I(f)=sum_{S subset [n]} |S| fhat(S)^2=sum_i Pr[f(x) != f(x with bit i flipped)].

Target: Does an absolute finite constant C exist such that H(f) <= C I(f) simultaneously for all n and all such Boolean f?

No monotonicity, balance, symmetry, degree, formula-size, or coordinate-independence hypothesis is part of the target. A bound whose C depends on n or a complexity parameter is a special case, not the full target. Constant functions have H=I=0. This packet contains the statement only; no proposed route or proof is supplied to the adversary.

Primary statement checked: Gonzalez, MacManus and Pereyra, arXiv:2606.00246v1, Introduction, definitions and FEI Conjecture, https://arxiv.org/html/2606.00246v1 . Historical originating citation: Friedgut and Kalai (1996), DOI 10.1090/S0002-9939-96-03732-X; original PDF access not yet recovered.

Current openness: UNKNOWN pending completion of owner solved/retired and current primary-source checks. No novelty claim.
