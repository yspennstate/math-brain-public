# C0120 referee packet (2026-10-10)

## Source correction: KEEP, pending Claude statement review

w492-S1.2 is supported by [Chatterjee, *Chaos, concentration, and multiple valleys*, arXiv:0810.4221v2, Section 8 and Section 12(3)](https://arxiv.org/pdf/0810.4221v2). Section 8 defines iid standard Gaussian weights on the positive quadrant and n-vertex up/right paths from the origin; the endpoint is unrestricted. Its random variable M is the maximum path sum. Theorem 8.1 bounds Var(M) by C n/log n. Section 12(3) asks: "Improve the fluctuation exponent in directed polymers." The intake's `Var(log Z_n)` and general-dimension interpretation are unsupported by that theorem. I independently re-read Section 8 and 12, rather than accepting the intake paraphrase. Because this corrects a statement, request Claude review before store promotion. Present openness remains UNKNOWN.

## w493 dependency counterexample: KEEP as abstract special case

Reproduction: let B be Bernoulli(p), 0<p<1, and A_i={B=1} for i=1,...,m, m>=2. With trivial F_i, each P(A_i|F_{i-1})=p while P(intersection A_i)=p>p^m. For the valid sequential bound, previous intersections must be F_{i-1}-measurable. This confirms w493-C0120-001 and does not address polymer overlaps.

## Remaining proof gap

For the Section 8 ground-state model, a power bound on Var(M_n) needs a quantitative power gain in a suitable noise-overlap integral. Neither peer claim supplies it. No parent-problem solution is claimed.

## Full peer packet verdicts and reproductions

- **w492-L1 KEEP.** Distinct Gaussian path sums tie with probability zero. The gradient of M_n is the maximizing path indicator, so its squared norm is n. Hermite differentiation and Parseval give sum k a_k=n; Mehler gives Q_n(t)=sum k a_k exp(-(k-1)t). Integrating exp(-t)Q_n(t) termwise gives Var(M_n)=sum a_k. Finite gradient energy justifies the series interchange.
- **w492-L2 KEEP as a conditional reduction.** Split sum a_k at K, use a_k<=k a_k for k<=K and a_k<=k a_k/(K+1) for k>K. Also D_n(K)<=K sum a_k. The polynomial premise G1 remains unproved.
- **w492-L3 KEEP.** In the nonnegative spectral sum, low-degree terms are bounded below by exp(-(K-1)t)D_n(K) and high-degree terms above by exp(-Kt)n. This yields both inequalities as written.
- **w492-G1 OPEN, no proof verdict.** The existing bound only gives D_n(floor n^a)<=C n^(1+a)/log n, weaker than D_n<=n for large n. This is the load-bearing missing lemma.
- **w492-L4 KEEP for its stated alternate graph.** With m independent Gaussian corridor sums, T=g_0+sqrt(n-1)max_j G_j. I rechecked its quantile lower bound: if Phi(u)^m=1/2 and h=1/u, then u>=1, u^2<=2log(2m), and Mills bounds give P(G>=u+h)>=exp(-3/2)P(G>=u)/5. The two independent copies on opposite sides of u and u+h yield Var(max G_j)>=c/log(2m). Hypercontractivity gives the matching upper O(1/log m). Setting m=n rules out deriving a power gain from small marginals alone. It says nothing against the quadrant target.
- **w493-C0120-002 KEEP with Claude statement gate.** Independently checked against Section 8 and Section 12(3); same mismatch as w492-S1.2.
- **w493-C0120-003 KEEP.** Each path uses one vertex per layer. The layer mean is jointly Gaussian and orthogonal to every residual coordinate; hence independent of the residual vector. The sum of layer means has variance H_n and adds to M_n; at fixed beta it adds as beta times the sum to log Z.
- **w493-C0120-004 KEEP.** At n=2 the root is shared, and the two endpoint choices have equal signs for correlated Gaussian differences with probability 1/2+arcsin(e^{-t})/pi. Thus Q_2(t)=3/2+arcsin(e^{-t})/pi. Direct variance decomposition or integration gives Var(M_2)=2-1/pi.
- **w493-C0120-005 KEEP as a conditional reduction.** Monotonic Q_n and 0<=Q_n<=n allow splitting the variance integral at tau=n^{-a}; the converse uses (1-e^{-tau})Q_n(tau)<=Var(M_n). The polynomial overlap premise remains unproved.

My independent new first-chaos identity and its w497 review gate are in ATTEMPT.md. The older intake C0120-A001 receives **FIX** for model scope and unsupported transfer of an FPP exponent relation.
