# Referee report: polynomial components in spectrally subcritical percolation on near-regular graphs

Paper: yspennstate/near-regular-percolation-components at a133570 (paper/main.tex, 449 lines, 9 pages). Referee:
an agent, 14 Nov 2026.
Claim (answers the near-regular special case of Christoph-Morawski-Wigderson Question 5.2, arXiv:2608.19145): at
p = (1-eps)/lambda on graphs with Delta <= (1+delta) lambda, the largest component is O(log n) when
(1-eps)(1+delta) < 1 (a maximum-degree argument, special case of DEKK Theorem 2), O((log n)^3) when it equals 1
(resolvent-weighted multitype branching process), and there are connected graphs (clique K_{k+1} bridged to a b-ary
tree, blown up by blocks of size m_h) with L_1 >= n^c whp when it exceeds 1, with lambda of any order n^a, 0 <= a < 1.
Plus a refinement of CMW's resolvent bound: L_1 = O(B^{log(qR)/log R + zeta} log n) for fixed R = Delta/lambda,
B = sqrt(n Delta)/lambda. The optimal exponent in the polynomial regime stays open; the paper says so.

## Verdict

SOUND. Commit fa9fa06 ("Fix a reference"), PDF rebuilt (9 pages, no undefined references):

1. Paley-Zygmund was cited as [LP16, Section 5.1]; in Lyons-Peres it is stated in Section 5.5 (the book's own
   pointer at the end of 5.3 says so; Proposition 5.11 in 5.3 is only the t = 0 case). Now Section 5.5.
2. Remark 6.2 listed slopes for six of the seven simulated families and omitted the star with a clique (0.52,
   data/fits.csv); added.
3. SHA256SUMS regenerated for main.tex and main.pdf; a clean clone with core.autocrlf=false passes all 15.

No change to any statement or proof.

## Proofs checked (re-derived)

- Lemma 2.1: lambda(T_{b,h}) <= 2 sqrt b by the weighted AM-GM bound; Weyl for the bridge; degrees; Kronecker blow-up.
- Parameters (2.1): b = floor(rk), mu = b(1 - e^{-q/(k+1)}) -> rq > 1; Delta(G_h) < (1+delta) lambda(G_h);
  log n_h = (1+tau) h log b + O(1); tau = a/(1-a) gives lambda = Theta(n^a).
- Exploration (2.2): 1 - (1-p)^m >= 1 - e^{-mp}, mp = q/lambda(H_h) >= q/(k+1); disjoint tested edge sets.
- Lemma 2.3: E Z_{l+1}^2 = mu^2 E Z_l^2 + sigma^2 mu^l, closed form, Paley-Zygmund with t = 1/2.
- Proposition 2.2: b^j independent subtrees, (1 - s_0)^{b^j} -> 0, the exponent bookkeeping with eta.
- Remark 2.4 numbers: mu = 1.04285, log mu / log 108 = 0.008962 (verify.py: 1.0428532, 0.0089618); the comparison
  mu < q sqrt(b)/2 against B = Theta(n^{1/(2(1+tau))}).
- Proposition 1.2: progeny >= s forces the first s-1 particles to have >= s-1 children; Chernoff with
  e^t = 1/(1-kappa) gives exp(N[kappa + log(1-kappa)]) <= e^{-kappa^2 N/2}; the cycle lower bound.
- Theorem 1.3: p^j W_j(x) <= q^j B and <= 1, U <= 1 + J + 1/eps; the MGF induction with a = 1/(2U^2),
  theta = 1/(4U^2), e^z - 1 <= z + z^2, theta + a^2 U^2 = a; union bound at s = 4U^2(3 log n + 1).
- Theorem 1.5: Aw = a lambda (w - U_a^{-1} 1); the exploration supermartingale; (theta/2)(1 + theta/2)(1 - theta)
  = (theta/2)(1 - theta/2 - theta^2/2) so log M >= theta^2 w(C)/4 - 1; |C| <= U_a w(C).
- Remark 5.1: U_a closed form, the three growth regimes, the choice a >= R^{-zeta}/q giving (1.3).
- Remark 6.1: star and star-plus-clique examples.

## Citations checked against the sources

- CMW arXiv:2608.19145 (19 Aug 2026, Christoph, Morawski, Wigderson): Theorem 1.4(II) is the subcritical bound
  (with K = lambda/sqrt Delta it is (1.1)); Question 5.2 and the "close to regular" special case worded as quoted;
  footnote 7 (d-ary trees, components |G|^{1/2-gamma}) on p. 20.
- DEKK arXiv:2209.03722, Theorem 2: max degree d, p = (1-eps)/d, components <= 9 log n / eps^2.
- BBCR math/0701346, Theorem 3: subcritical C_1 = O(log n) for kernels with ||T_W|| < 1.
- Lyons-Peres book: Paley-Zygmund in Section 5.5 (item 1 above).
- Crossref, all six DOIs (ABS04, BBCR10, DEKK25 RSA 66 e21268, NumPy, LP16, SciPy): authors, journal, volume, pages
  as listed.
- No control characters; 13 entries, all cited.
- Prior-work search (web, two wordings; arXiv abstract search "percolation" AND "spectral radius", newest first): no
  paper after CMW answers Question 5.2 or overlaps these results.

## Numbers checked independently

- data/trials.csv -> least-squares slopes of log median L_1 on log n reproduce data/fits.csv to four digits for all
  seven families (0.2695, 0.4816, 0.4908, 0.5198, 0.1779, 0.1701, 0.1952), matching the rounded values in Remark 6.2.
- hosts.json matches the remark: planted degrees n^{0.6} 2^{-i}; k = 12, b = 16, blocks 2^h; 30 hosts, 40 reps,
  max n 1,118,688.
- Separate script (agent_run/nrpc_refs/indep_nrpc.py: own graph builder, eigsh for lambda, own sampler) on the
  near_regular_tree family h = 1..4: lambda agrees to six digits (12.007254 ... 12.007389), medians 4/6/10/16.5 against
  the paper's 5/6.5/9.5/18, inside each other's q10-q90 bands.
- code/verify.py rerun on Mac mini 2 (NumPy 2.5.4, SciPy 1.18.1): PASS, every field identical except spectral
  roundoff differences of order 1e-14. It does not run on Windows (resource, os.getpriority); the README says
  Linux or macOS.

## Minor (not acted on)

- The letter a is the exponent in Theorem 1.1, the resolvent parameter in Theorem 1.5 and 1/(2U^2) in Section 4;
  theta likewise has two meanings. Each is defined where it is used.
- The abstract is 151 words; the code-availability URL points at the repository root rather than a commit.
