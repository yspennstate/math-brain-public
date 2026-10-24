# C0029 referee and brain bridge

The original Spielman--Teng Conjecture 2 is an inverse-norm tail for a square independent sign matrix. Sah--Sahasrabudhe--Sawhney (2025), Theorem 1.1, gives the modern $F_{B,n}(t)\leq(1+O((\log n)^{-1/16}))t+e^{-\Omega(n)}$ for all $t\geq0$. The requested coefficient-one $F_{B,n}(t)\leq t+e^{-\Omega(n)}$ remains unproved by the checked theorem. Current openness is UNKNOWN. The source evidence and quantifiers are in SOURCE_STATUS.json.

## Direct independent checks

For w573 Lemma D, let $A=N^TN$ and $M^TM=A+XX^T$. If the second eigenvalue $\mu$ of $A$ obeys $\mu\leq\tau$, the two-dimensional span of its first two eigenvectors contains a unit vector orthogonal to $X$, giving Rayleigh quotient at most $\mu$. If $\mu>\tau$, diagonalize $A=\operatorname{diag}(0,d_1,\ldots,d_{n-1})$ and write $z_i=\langle X,v_i\rangle$. The lower block of $M^TM-\tau I$ is $C=\operatorname{diag}(d_i-\tau)+z'z'^T\succ0$. Its scalar Schur complement is $z_0^2/(1+\sum_i z_i^2/(d_i-\tau))-\tau$. Hence the least eigenvalue is at most $\tau$ exactly when $z_0^2\leq\tau(1+\sum_i z_i^2/(d_i-\tau))$. This also works at $\tau=0$ and with repeated positive eigenvalues. The conditional CDF identity must retain $P(\mu\leq\tau)$, and Bernoulli row projections $z_i$ remain jointly dependent.

For w574 S1.w574.2, conditioning on independent $R\geq0$ gives $h(t)/t=\sqrt{2/\pi}\,E\int_0^R e^{-t^2u^2/2}du$. It decreases with $t$. Thus $h(t)\geq(t/t_0)h(t_0)$ for $0<t\leq t_0$, strictly if $t<t_0$ and $P(R>0)>0$. Subtract the integrands and use $e^{-x}-e^{-y}\leq y-x$ for $x\leq y$ to get $0\leq h(t)-(t/t_0)h(t_0)\leq\sqrt{2/\pi}\,t(t_0^2-t^2)E[R^3]/6$ when $E[R^3]<\infty$. Sah et al. Lemma 9.2 explicitly retains a spectral cutoff and an $O(\delta_n t)$ error; this derivation does not contradict it.

For w574 S1.w574.3, $R_0=(A^2+B^2)^{1/2}$ has Rayleigh density $r e^{-r^2/2}$. If $R=|W|/(\sqrt2 R_0)$ with independent standard Gaussians $A,B,W$, then $E[R^3]=E|W|^3\,E[R_0^{-3}]/2^{3/2}=\infty$ since the latter integral behaves as $\int_0^1r^{-2}dr$. Conditional on $(A,B)$, $R_0>0$ almost surely and the third moment is finite. The example tests an averaging premise; it is outside the large-$n$ Bernoulli setting.

## Measured math-brain failure and bounded repair

Command `python -X utf8 ~/brain_workers/w575/run_math_recall.py` opened the 87,019,520-byte population store through `ResearchStore.open_read_only` and ran native retrieval for `Spielman Teng Bernoulli least singular value coefficient one Gaussian comparison`, limit 5. It took 6.077 seconds. Ranks 1--5 were an old C0029 attempt, C0029 open-problem card, Rudelson--Vershynin overview, smallest-singular-value concept, and Rudelson--Vershynin theorem. Thus **0/5** gave Sah--Sahasrabudhe--Sawhney Theorem 1.1 or its $1+O((\log n)^{-1/16})$ limitation, and rank 1 led to the local attempt containing a false finite-$n$ Gaussian formula. Raw decision and traces are in RECALL_BASELINE.json. This is one query, not a global recall benchmark.

The bounded repair is a three-node DRAFT bundle: the precise conjecture, the 2025 theorem with its hypotheses, and a correction concept for the finite-$n$ Gaussian formula. Its edges state an approximate relation and a scoped correction; no edge says the theorem proves the conjecture. After the coordinator ingests it, rerun this same query and inspect ranks and statements. No after-ingestion improvement is claimed yet.

## Single hardest gap

The exact row event is useful only if one can bound its **signed Bernoulli probability**, including the branch $\mu\leq t^2/n$, against the finite-$n$ Gaussian CDF with error no larger than the Gaussian slack $t-F_{G,n}(t)$ plus an exponential term. The published comparison error $\delta_n t$ can dominate that slack at small $t$. Gaussian orthogonal projections are independent; Bernoulli projections need not be. Neither peer has closed this gap, and no parent-problem solution is claimed.

NEXT: Audit a Bernoulli-specific one-row signed comparison on the exact Schur event, retaining the small-gap branch and coordinate dependence.
