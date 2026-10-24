from pathlib import Path
import json
head='''# Literature audit for C0133

Audit date: 2026-10-12. Web access used only Python urllib; no built-in web search.

## Exact source
Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, arXiv:1204.1895v2, 8 October 2012, Problem 4.7, printed/PDF p. 19. Downloaded source.pdf; extracted source.txt (37 pages).

> Problem 4.7. (d ≥ 1) Assume (IID), (EL), ℓ ∈ R^d \\ {0}. Does X_n · ℓ/n converge P_0-a.s. on {|X_n| → ∞}^c to 0 as n → ∞? This would generalize [Zer02, Th. 1].

Page 2 defines nearest-neighbor steps, cookie index equal to the number of visits including the current visit, and the annealed law P_0. (IID) means whole cookie stacks are independent and identically distributed across sites, not independence within stacks. Page 3: (EL) means every individual transition probability is strictly positive almost surely. Infinite stacks are allowed; no uniform lower bound, finite-stack hypothesis, or common drift sign occurs in Problem 4.7.

Theorem 4.6 is restricted to A_ℓ = {X_n·ℓ → +∞}; it does not control returning excursions. Theorem 4.8 assumes P_0[A_{ℓ_i} ∪ A_{−ℓ_i}] = 1 for a basis. This implies spatial transience and makes the event in Problem 4.7 null. It therefore cannot answer the question on an event of positive probability.

## Searches (exact URLs and outcomes)
'''
for f in sorted(Path('.').glob('search_log*.json')):
 d=json.loads(f.read_text());head+='\n### '+f.name+' ('+d['date']+')\n'
 for k,u in d['queries'].items():head+='- '+k+': `'+u+'`\n'
 head+='\nOutcomes: `'+json.dumps(d['results'])+'`\n'
head+='''

Rate-limited services are coverage gaps, not negative search results. The first Project Euclid zero-one PDF request returned a 1157-byte HTML response despite HTTP 200; this was not treated as a paper. The arXiv copy was requested separately.

## Read-only prior work
- Intake ledger: probability_1000_intake_claude_20260907/{problems,attempts}.jsonl, C0133 and C0133-A001. Its claimed exponential returning-excursion estimate is not established.
- Git origin/master: probability_campaigns/codex_pool_2026-10-10/team_O/w338/PROOFS.md, C0133 section. Correctly distinguishes an unrestricted spatial tail 1/(2L) from a time-constrained tail. Rechecked independently below; no repository was changed.
- math_recall.py: “excited random walks zero velocity recurrence”; brain.py recall: “excited random walks mistakes” and “C0133 zero velocity non-transient”. No useful problem-specific memory beyond the existing attempt; unrelated memories were not used.

## Status of this audit
No theorem giving the full question under the exact hypotheses has been verified. This is a bounded audit, not a certificate that the problem remains open globally. Later special-case papers are leads; they are not SOLVED_IN_LITERATURE for C0133.
'''
Path('LITERATURE.md').write_text(head,encoding='utf8')
Path('ATTEMPT.md').write_text('''# C0133 mathematical attempt — 2026-10-12

## Statement and conventions
For nearest-neighbor excited random walk X on Z^d, d ≥ 1, with i.i.d. whole cookie stacks satisfying (EL), fix ℓ ≠ 0. Let T = {||X_n|| → ∞}. The target is P_0(T^c ∩ {X_n·ℓ/n does not tend to 0}) = 0. Starting point is 0. We use Euclidean norm; the event is independent of the choice of norm. The event T^c means some finite ball is visited infinitely often, not that all sites are visited infinitely often.

## 1. Exact predictable-drift reduction (proved)
Put L_k(x) = #{0 ≤ j ≤ k: X_j=x}, and
b(x,i) = Σ_{e∈{±e_j}} ω(x,e,i)(e·ℓ).
Let c = max_j |ℓ_j| > 0, a_k = b(X_k,L_k(X_k)), D_n = Σ_{k=0}^{n−1} a_k, and M_n = X_n·ℓ − D_n. In the filtration containing the whole environment and the walk through time n, (M_n) is a martingale, M_0=0, and |M_{n+1}−M_n| ≤ 2c.

Here is a full proof of its strong law. If Z is a conditional mean-zero variable with |Z| ≤ h, convexity on [−h,h] gives E[e^{λZ}|F] ≤ cosh(λh) ≤ exp(λ²h²/2). The last inequality follows by differentiating log cosh t, since tanh t ≤ t for t ≥ 0, and by symmetry for t < 0. Iterating with h=2c gives E exp(λM_n) ≤ exp(2λ²c²n). Markov's inequality and λ=ε/(4c²) yield
P(M_n ≥ εn) ≤ exp(−ε²n/(8c²)). Apply the same argument to −M_n. Summing 2exp(−ε²n/(8c²)) over n and using Borel–Cantelli, for each positive rational ε, proves M_n/n→0 almost surely. This proof applies quenched and annealed; it uses neither IID nor EL.

Consequently the target is equivalent, up to a null set, to D_n/n→0 on T^c. This is a reduction, not a proof that the drift vanishes.

## 2. Balanced projection special case (proved)
If b(x,i)=0 for every x and i almost surely, D_n=0 identically, and Section 1 proves X_n·ℓ/n→0 on the entire probability space. In particular, balanced cookies ω(x,e,i)=ω(x,−e,i) have vector speed 0: apply Section 1 separately to the d coordinate directions, intersect the finitely many full-probability events, and use ||X_n|| ≤ Σ_j |X_n·e_j|. Infinite cookie stacks and lack of uniform ellipticity cause no difficulty in this special case.

## 3. Deterministic return-time reduction (proved)
Let (x_n) be any path with ||x_{n+1}−x_n||≤1. If it visits a ball B(0,R) infinitely often, enumerate its visit times t_1<t_2<… . Then ||x_{t_k}||/t_k≤R/t_k→0. Thus any existing vector or scalar directional speed must be 0 on this event. Existence of a limit is the issue.

If t_{k+1}/t_k→1, then the entire path has zero vector speed. Indeed, for t_k≤n<t_{k+1}, triangle inequality and bounded steps give
||x_n||/n ≤ R/n + (n−t_k)/n ≤ R/t_k + (t_{k+1}−t_k)/t_k,
which tends to 0. This holds for any one finite ball visited infinitely often. Conversely, if ||x_n||≥εn at arbitrarily large n, choose the last ball visit s≤n and next visit t>n. For n large, s exists and ||x_s||,||x_t||≤R. The distance traveled from s to n and from n to t is at least ||x_n||−R, so
n−s≥εn−R, t−n≥εn−R, and t−s≥2εn−2R.
This supplies a necessary condition for a counterexample. IID and EL have not been shown to exclude these large gaps.

## 4. Drift budget versus range (proved conditional criterion)
Let R_n={X_0,…,X_{n−1}}, the set of departure sites by time n, and N_n(x)=#{0≤k<n:X_k=x}. Grouping summands by site gives the exact identity
D_n = Σ_{x∈R_n} Σ_{i=1}^{N_n(x)} b(x,i).
If B(x)=Σ_{i≥1}|b(x,i)| is finite, then
|D_n| ≤ Σ_{x∈R_n} B(x).
Hence any path/event on which the right-hand side is o(n) has zero directional speed almost surely by Section 1. Under a deterministic bound B(x)≤B, it suffices to prove #R_n=o(n). For bounded stacks with at most m non-placebo cookies, B(x)≤mc. This does NOT prove C0133 even under bounded stacks: no sublinear-range estimate on T^c has been established here. For i.i.d. unbounded budgets, integrability alone does not justify replacing the adaptively selected site sum by its expectation.

## 5. Earlier exponential-tail proposal (independently rechecked)
For simple symmetric walk S on Z, τ is the first positive return to 0. For L≥1,
P(max_{0≤n≤τ} S_n ≥ L)=1/(2L).
Proof: a positive first step has probability 1/2. From 1 the probability of hitting L before 0 is 1/L. To prove the latter without unbounded stopping, stop in finite interval [0,L]. Absorption occurs almost surely: in each block of L steps there is conditional probability at least 2^{−L} to take enough steps of one sign to reach a boundary, so survival after k blocks is at most (1−2^{−L})^k. The stopped position is bounded, and the martingale identity followed by dominated convergence gives E S_σ=1; since S_σ∈{0,L}, P(S_σ=L)=1/L. (For L=1 the answer is 1.) A negative first step cannot hit positive L before 0. Return from 1 to 0 is almost sure: the event of staying forever in a finite interval has probability 0 by the same block argument, and P(hit L before 0)=1/L→0 rules out avoiding 0 forever while being unbounded above. Reflect for −1.

This fair-cookie environment satisfies IID, UEL and bounded stacks. For every C,a>0, 1/(2L)>C exp(−aL) for all sufficiently large L, so unrestricted spatial excursions have no exponential upper tail. This does not refute an estimate with an imposed O(L) time budget. Such a time-constrained estimate for arbitrary cookie drifts is also not supplied by ellipticity alone.

## Remaining gap
Prove D_n=o(n) on T^c for general i.i.d. elliptic infinite stacks, or construct an actual IID/EL counterexample. The conditional range and return-time criteria do not close the gap. No full proof or counterexample is claimed.
''',encoding='utf8')
print('saved source audit and initial proved reductions')
