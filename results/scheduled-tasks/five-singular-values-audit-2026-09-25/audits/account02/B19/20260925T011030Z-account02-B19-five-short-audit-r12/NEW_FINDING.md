# New B19 finding B19-N01

Source: short.tex L222, PDF p5.

Status: FALSE, local and repairable.

The sentence “Factors with beta_i=0 are at most one” is false. Counterexample: n=4 and d=2; let U have columns e1,e2 and choose the orthogonal complement W with columns e3,e4. Then rows w1 and w2 are both zero, so beta1=beta2=0.

Repair: delete “are at most one and” and drop all zero-beta factors. Every zero-beta factor is independent of the integration variable z and is at most 1, so dropping all such factors only increases the density integral. The positive-beta rows still satisfy sum beta_i v_i v_i^T = I. The entropy estimate is unchanged by retaining zero beta terms as 0 log 0 = 0 in the first sum and using sum_i(1-beta_i)=d in the upper bound.

Downstream regression: Lemma 3.2 keeps the same e^(d/2) cap. Lemma 3.3, the grouped Fourier compiler, Corollary 4.4, Proposition 7.1 and Theorem 1.1 therefore keep all constants unchanged.

Independence note: this issue was not listed in the shared CORRECTIONS file and was found during the independent projection-lemma reconstruction.
