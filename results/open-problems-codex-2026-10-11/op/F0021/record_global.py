from pathlib import Path
import json
p=Path('.')
with p.joinpath('ATTEMPT.md').open('a',encoding='utf-8') as f:f.write(r'''

## Proposition 7: full-cone truncation and the two distinct thresholds (proved)
Let C_n={(i,x):1<=i<=n, |x|<=i, x=i mod 2}. Its cardinality is N_n=sum_{i=1}^n(i+1)=n(n+3)/2.

(a) If alpha>6, choose 2/alpha<kappa<1/3. With probability tending to one, all weights in C_n are at most n^kappa, so the ORIGINAL and positively capped full partition functions are exactly equal. No confinement hypothesis is needed for this statement.

Proof. Choose q<alpha with q kappa>2. Lemma 1 and a union bound give P(any capped site)<=N_n C n^{-q kappa}<=2C n^{2-q kappa} for n>=1. The exponent is negative. On the complementary event every accessible site and hence every path weight is unchanged.

(b) If 5<alpha<6, let W_n=max_{(i,x) in C_n} omega_{i,x}. Then W_n/n^{1/3}->+infinity in probability, although M_n/n^{1/3}->0 in L1 by Corollary 6.

Proof. First show the lower power envelope: for q>alpha there exist c,T>0 with Fbar(t)>=c t^{-q} for t>=T. Regular variation gives Fbar(2t)/Fbar(t)>=2^{-q} eventually. Choose T with this property and Fbar(T)>0. For 2^k T<=t<2^{k+1}T, monotonicity and iteration yield
Fbar(t)>=Fbar(2^{k+1}T)>=Fbar(T)2^{-(k+1)q}>=Fbar(T)T^q 2^{-q} t^{-q}.
Choose alpha<q<6 and any fixed A>0. By independence,
P(W_n<=A n^{1/3})=(1-Fbar(A n^{1/3}))^{N_n}
<=exp(-N_n Fbar(A n^{1/3})).
The exponent in absolute value is at least (c/2) A^{-q}n^{2-q/3}->infinity. Thus this probability tends to zero for every A>0, which is the stated divergence. Corollary 6 independently supplies the assertion about M_n.

The number 6 marks when a GLOBAL cap below n^{1/3} can leave the entire reachable cone unchanged. The number 5 marks the single-site, entropy-corrected threshold and allows an unchanged somewhat enlarged KPZ tube. They answer different questions. Neither part establishes a limit for the full random-background polymer free energy.
''')
with p.joinpath('CLAIMS.jsonl').open('a',encoding='utf-8') as f:
 for c,g in [
  ('For alpha>6 a cap n^kappa, 2/alpha<kappa<1/3, leaves the full polymer partition function exactly unchanged with probability tending to one.','A KPZ theorem for the n-dependent capped model is still missing.'),
  ('For 5<alpha<6 the full-cone raw maximum divided by n^(1/3) diverges in probability, while the entropy-corrected single-site maximum divided by n^(1/3) tends to zero in L1.','This distinction does not establish polymer fluctuations or an Airy limit.')]:
  f.write(json.dumps({'problem_id':'F0021','claim':c,'status':'proved','proof_location':'ATTEMPT.md, Proposition 7','remaining_gap':g,'checks':'Full regular-variation envelopes, cone cardinality, union/product probabilities; independently refereed by separating raw and penalized maxima.'})+'\n')
print('Saved full-cone truncation and raw/penalized maximum distinction.')
