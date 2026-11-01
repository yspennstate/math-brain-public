from pathlib import Path
p=Path('~/brain_workers/TRIO_1011/op/F0021')
with p.joinpath('SECOND_ATTEMPT.md').open('a',encoding='utf-8') as f:f.write(r'''

## Corollary 13: the rare-reward theorem permits a slowly growing inverse temperature (proved)
Retain the hypotheses and cutoff kappa of Theorem 11. Let r>=0 with kappa+r<1/3, and let beta_n be any deterministic positive sequence bounded by B_0 n^r for a fixed B_0. Then (11.1), including its total-variation conclusion, still holds with beta_n in place of beta.

Proof. Choose the same fixed envelope exponent 5<q<alpha with q kappa>5/3. In the proof of Theorem 11 replace D by D_n=16 max(1,beta_n), bounded by a constant times n^r. Step 1's condition A/(D_n L)>u_n follows from kappa+r<1/3. Site counts and Step 2 are unchanged.
For the high-layer bound (11.3), the two n-exponents become rq+1-q/3 and rq+(5-q)/3. Since 1/3-r>kappa and q kappa>5/3, these are both strictly negative: they are 1-q(1/3-r) and 5/3-q(1/3-r).
The low-layer bracket (11.4) now has exponents r+2/3-kappa(q-1) and 2r+1-kappa(q-2). The condition r<1/3-kappa makes them strictly less than 1-q kappa and 5/3-q kappa, respectively, which are negative. All logarithmic union bounds therefore still tend to zero. With D_n>=16 beta_n, the allocation inequality (11.5) holds unchanged. The subsequent subset expansion and the bound N log 2<=A/4 are unchanged. This proves all assertions.

## Lemma 14: a finite temperature-comparison identity (proved)
Let P be uniform on the 2^n length-n walk paths, let H be any finite real function on paths, and set F(t)=log E_P exp(tH), t>0. For any p>1,

0 <= F(p beta)/p-F(beta) <= n log 2 (1-1/p).                              (14.1)

Proof. Let mu_t have density exp(tH-F(t)) relative to P. Differentiating the finite sum gives F'(t)=E_{mu_t}H. The relative entropy satisfies
D(mu_t||P)=tF'(t)-F(t)=n log 2 + sum_{paths} mu_t(path) log mu_t(path).
It is nonnegative: Jensen applied to log under mu_t gives E_{mu_t} log(P/mu_t)<=log E_{mu_t}(P/mu_t)=log 1=0. It is at most n log 2 because each mu_t(path)<=1, so every mu_t log mu_t summand is nonpositive. Thus

(d/dt)(F(t)/t)=D(mu_t||P)/t^2 in [0,n log 2/t^2].

Integrate from beta to p beta and multiply by beta. The integral of beta/t^2 is 1-1/p, proving (14.1). All weights are finite for each fixed environment; this requires no exponential moment of the disorder law.

## Theorem 15: unconditional sublinear truncation bound for the ORIGINAL polymer (proved)
Let alpha>5 and beta>0, with the original iid disorder as in Assumption 3. Fix any

0<r<(alpha-5)/(3 alpha).

Choose kappa satisfying 5/(3 alpha)<kappa<1/3-r. Let u_n=n^kappa, c_{i,x}=min(omega_{i,x},u_n), and let F_n(beta)=log Z_n^beta(omega), F_n^cap(beta)=log Z_n^beta(c). Then, with probability tending to one,

0 <= F_n(beta)-F_n^cap(beta)
   <= [n log 2 + exp(-n^{1/3}/4)]/(1+n^r).                               (15.1)

In particular the truncation error is O_P(n^{1-r}), and the difference divided by n tends to zero in probability. This bound is unconditional: it does not assume confinement of either polymer. It applies with exactly the one-sided tail assumption and finite-variance negative side of the question (indeed its proof only needs the right tail).

Proof. The kappa interval is nonempty precisely because r<1/3-5/(3 alpha). Define delta=(omega-u_n)_+ and eta=omega 1{omega>u_n}; then omega=c+delta, 0<=delta<=eta. Put p_n=1+n^{-r} and h_n=p_n/(p_n-1)=1+n^r, so 1/p_n+1/h_n=1. Hölder's inequality in the finite bare-walk expectation gives

Z_n^beta(omega)
 <= [Z_n^{p_n beta}(c)]^{1/p_n} [Z_n^{h_n beta}(delta)]^{1/h_n}
 <= [Z_n^{p_n beta}(c)]^{1/p_n} [Z_n^{h_n beta}(eta)]^{1/h_n}.

The second inequality uses delta<=eta. The inverse temperature h_n beta is at most 2 beta n^r. Corollary 13 applies, because kappa+r<1/3, and shows with probability tending to one that
log Z_n^{h_n beta}(eta)<=Z_n^{h_n beta}(eta)-1<=exp(-n^{1/3}/4).
Subtract log Z_n^beta(c), take logarithms in the Hölder bound, and apply Lemma 14 to the SAME fixed capped environment c. Its temperature-comparison contribution is at most n log 2 (1-1/p_n)=n log 2/(1+n^r). This yields (15.1). The lower bound follows from omega>=c and beta>0. Finally the upper bound divided by n is at most log 2/(1+n^r)+o(1), which tends to zero.

### Where this attempt stops
For 5<alpha<=6 the allowed r is less than or equal to 1/18; hence the obtained scale n^{1-r} remains at least n^{17/18}, much larger than n^{1/3}. Even letting alpha grow, this particular growing-temperature argument allows r<1/3 and thus never reaches an n^{1/3} error through the n^{1-r} entropy comparison. For alpha>6 the first attempt already proves exact equality with a suitable global cap with high probability; Theorem 15 is not an improvement there.
The loss is identifiable: the deterministic comparison (14.1) spends order n(p_n-1) to change temperature. It does not exploit common random fluctuations or a sharply centered free-energy comparison, and bounded deterministic strongly favourable paths can have relative entropy of order n. No estimate proved here reduces this term to the KPZ scale. No KPZ/Airy law for the capped model has been proved either. The theorem proves a truncation bound, not universality and not a counterexample to universality.
''')
with p.joinpath('CLAIMS.jsonl').open('a',encoding='utf-8') as f:
 import json
 for c,l,g in [
 ('The rare-reward polymer theorem remains valid for beta_n=O(n^r) when kappa+r<1/3 and alpha kappa>5/3.','SECOND_ATTEMPT.md, Corollary 13','Zero background, triangular-array rare-reward law only.'),
 ('For any finite energy function on length-n bare-walk paths, 0<=F(p beta)/p-F(beta)<=n log(2)(1-1/p).','SECOND_ATTEMPT.md, Lemma 14','No gap in the finite identity/bound; its order n cost is too large for KPZ comparison.'),
 ('For alpha>5 and every 0<r<(alpha-5)/(3 alpha), a cutoff n^kappa with 5/(3 alpha)<kappa<1/3-r gives an unconditional original-polymer truncation error bounded by (n log 2+exp(-n^(1/3)/4))/(1+n^r) with probability tending to one.','SECOND_ATTEMPT.md, Theorem 15','This is O_P(n^(1-r)), much larger than n^(1/3); capped-model KPZ/Airy universality remains unproved.')]:
  f.write(json.dumps({'problem_id':'F0021','claim':c,'status':'proved','proof_location':l,'remaining_gap':g,'checks':'Complete proof using the independently derived chain bound, temperature entropy identity, and finite Holder inequality; additional finite validation pending.'})+'\n')
print('Saved a genuine unconditional original-polymer truncation bound and the precise loss in the Holder bridge.')
