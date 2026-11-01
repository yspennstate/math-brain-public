# C0023 independent route, written before opening w423/w424 proof artifacts

2026-10-10, w425. Target: nearest-neighbour independent Bernoulli **bond** percolation on \(\mathbb Z^d\), \(3\le d\le10\). Let \(\theta_d(p)=\mathbb P_p(0\leftrightarrow\infty)\) and \(p_c(d)=\inf\{p:\theta_d(p)>0\}\). The requested conclusion is \(\theta_d(p_c(d))=0\). The 2026-09-07 intake cited Garban--Steif XI.1 p.136; its open-status assertion is now stale or at least seriously contested by the September 2026 formal research artifacts listed in SOURCE_STATUS.json.

## Independent route: stopping-cluster relay

Work first in an arbitrary finite graph with product edge law and vertices \(o,b\), deterministic nonempty relay set \(A\). Explore edges adaptively from \(o\) until a first vertex \(R\in A\) is reached. Aim to prove
\[
\mathbb P(o\leftrightarrow A,\ o\not\leftrightarrow b)\le
\sup_{a\in A}\mathbb P(a\not\leftrightarrow b).
\]
This would yield additive gluing \(\mathbb P(o\leftrightarrow b)\ge\mathbb P(o\leftrightarrow A)-t\) whenever every relay has \(\mathbb P(a\leftrightarrow b)\ge1-t\). Then apply the Kozma--Nitzan reduction (Theorem 6, arXiv:2401.12397) after checking its exact hypotheses.

The naive stopping-time proof fails: the event \(R=a\) is determined by explored edge states, and the event \(a\leftrightarrow b\) may require those very edges. Fresh edges remain independent after exploration, but the full \(a\leftrightarrow b\) event is not independent of \(R=a\). The precise missing step is an exploration rule or inequality that keeps the disconnection cost at most \(t\) after conditioning on the selected relay. I will not infer it from ordinary product independence or multiply per-relay estimates.

## Rigorous baseline and load-bearing gap

For **any** law on finite-graph edge configurations, with deterministic finite \(A\),
\[
\mathbb P(o\leftrightarrow b)\ge\mathbb P(o\leftrightarrow A)-
\sum_{a\in A}\mathbb P(a\not\leftrightarrow b).
\]
Proof: if \(o\leftrightarrow A\) but \(o\not\leftrightarrow b\), choose a reached \(a\in A\); necessarily \(a\not\leftrightarrow b\). Union bound. Thus near-one marginals give a \(|A|t\) loss. The open mathematical burden in this route is removing \(|A|\), not the finite-graph bookkeeping. This lemma is elementary and currently self-checked only; w428 must independently referee it before any theorem promotion.

## Next proof step

Read Kozma--Nitzan Conjecture 3 and Theorem 6 word for word, then test whether a stopping-cluster exploration can give the required conditional bound or whether the recent formalization already settles the target with a different method. No parent-problem proof is claimed here.
