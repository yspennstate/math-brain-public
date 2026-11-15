# T142 (Waterman: Var L_n = Theta(n) for uniform binary LCS), routes checked 14 Nov 2026

- Upper bound Var L_n <= n: Steele (Efron-Stein). The conjecture is the linear lower bound.
- Known linear lower bounds are all asymmetric: one letter of tiny probability (Lember-Matzinger 2009),
  strongly biased models (Houdre-Ma 2016), one word omitting a letter (Houdre-Liu arXiv:1812.09552).
- Amsalu-Hauser-Matzinger (arXiv:1211.5489), Thm 2.1-2.2: if gamma(S) - gamma(S - eps T) > 0 for some
  eps > 0, where T is the scoring change induced by switching letter a to b, then a random a->b change has a
  biased effect and Var = Theta(n). They check the inequality by simulation (n = 100000) at a confidence
  level for binary 0.2/0.8 and a DNA scoring; for equiprobable letters the difference is 0 by symmetry, which
  the abstract states.
- Rigorous version of their 0.2/0.8 claim (a computer-assisted proof): needs a rigorous lower bound on
  gamma(S) and a rigorous upper bound on gamma(S - eps T) separated. The lower bound E L_m / m for an exactly
  computable m (m ~ 16 by enumeration) is off from gamma by a few hundredths (Alexander's rate
  sqrt(log m / m)), and Lueker-type upper bounds are about 0.04 wide for the uniform constant. Whether the
  separation at 0.2/0.8 exceeds that is not known; it is the first number to compute if this route is taken.
  This would settle a biased case only, not the uniform one.
Row updated (src/rows_12.py): Houdre-Liu and Amsalu-Hauser-Matzinger added to the status field. Still open.
