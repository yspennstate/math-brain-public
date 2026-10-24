# P0157 — maximal-degree component: a graph-level cycle-defect bound

**Scope.** This is a self-contained route lemma for HARD7-04. It is **not** asserted to be new to the literature and it does **not** solve the source phase-transition problem. Its purpose is to eliminate one concrete obstruction identified in the preceding checkpoint: pairing collisions/cycles in the configuration-model exploration of a maximal-degree vertex.

## Source context

The current source is Remco van der Hofstad, *Stochastic processes on random graphs* (preliminary monograph, 4 Aug 2026), Notes on Section 8.3, printed p. 245 / PDF p. 255. The source explicitly calls the barely-subcritical finite-third-moment configuration-model behavior an open problem and predicts a transition between a hub scale and an Erdos–Renyi scale. With

\[
\nu_n=\frac{\sum_i d_i(d_i-1)}{\ell_n},\qquad
\delta_n:=1-\nu_n>0,\qquad \ell_n:=\sum_i d_i,
\]

the hub prediction is of order \(d_{\max}/\delta_n\), while the Erdos–Renyi barely-subcritical scale is of order
\[
\delta_n^{-2}\log(n\delta_n^3).
\]
The source's prose writes the hub expression with \(\varepsilon_n=\nu_n-1<0\); throughout this track we use the positive parameter \(\delta_n=-\varepsilon_n\).

Current-status check used in this run: van der Hofstad's 4 Aug 2026 monograph still states the phase transition as open; Coulson–Perarnau, *Electron. J. Probab.* 28 (2023), DOI 10.1214/23-EJP921, gives upper bounds in the (barely) subcritical prescribed-degree setting that are asymptotically tight for certain degree sequences, but does not supply the full finite-third-moment crossover claimed by the source. The exploration inequalities below are deliberately not presented as a prior-art novelty claim.

## Assumptions

For each \(n\), let \(\mathrm{CM}_n(\mathbf d)\) be the configuration model with deterministic degree sequence \(\mathbf d=(d_i)_{i\le n}\). Assume

\[
\ell_n\ge c n,\qquad \sum_{i=1}^n d_i^3\le Cn,
\]
for fixed \(c,C>0\), and
\[
\nu_n=1-\delta_n,\qquad \delta_n\downarrow0,\qquad n\delta_n^3\to\infty.
\]
These are the quantitative pieces of the source's finite-third-moment barely-subcritical regime needed below. Let \(v_n\) be a chosen vertex of maximal degree
\[
d_n:=d_{\max}=d(v_n).
\]
Because \(\nu_n\to1\), eventually \(d_n\ge2\).

## Proposition (cycle defect vanishes at a maximal-degree root)

Under the assumptions above,

\[
\mathbb P\bigl(\mathcal C(v_n)\text{ contains a cycle}\bigr)\longrightarrow0.
\]
Moreover
\[
\frac{|\mathcal C(v_n)|}{d_n/\delta_n}
\]
is tight. More quantitatively, there is a constant \(B=B(c,C)\) such that whenever an integer horizon \(T\) satisfies \(T\le \ell_n\delta_n/4\),

\[
\mathbb E[T\wedge\tau]\le \frac{2d_n}{\delta_n},
\tag{1}
\]

\[
\delta_n\,\mathbb E\!\left[\sum_{0\le t<T\wedge\tau} A_t\right]
\le d_n^2+\frac{2Bd_n}{\delta_n},
\tag{2}
\]

and, if \(N_{\mathrm{cyc}}(T)\) counts pairings before \(T\wedge\tau\) whose partner half-edge is already active,

\[
\mathbb P(N_{\mathrm{cyc}}(T)\ge1)
\le
\frac{4d_n^2}{\ell_n\delta_n}
+
\frac{8Bd_n}{\ell_n\delta_n^2}.
\tag{3}
\]
Here \(A_t\) is the active-half-edge queue and \(\tau=\inf\{t:A_t=0\}\).

## Proof

Explore \(\mathcal C(v_n)\) by sequentially pairing active half-edges. After \(t\) pairings let \(A_t\) be the number of active unpaired half-edges. Thus \(A_0=d_n\). For \(t<\tau\), choose one active half-edge. Among the
\[
m_t:=\ell_n-2t-1
\]
possible partners, \(A_t-1\) are other active half-edges. If the partner belongs to an unseen vertex \(i\) of degree \(d_i\), then
\[
\Delta A_t:=A_{t+1}-A_t=d_i-2;
\]
if the partner is active, then \(\Delta A_t=-2\).

Let \(U_t\) be the unseen vertices. The exact conditional drift is
\[
m_t\,\mathbb E[\Delta A_t\mid\mathcal F_t]
=
\sum_{i\in U_t}d_i(d_i-2)-2(A_t-1).
\tag{4}
\]
Since
\[
\sum_i d_i(d_i-2)=\ell_n(\nu_n-1)=-\ell_n\delta_n,
\tag{5}
\]
and every discovered non-root vertex contributes at least \(-1\) to \(d_i(d_i-2)\), while at most \(t\) non-root vertices have been discovered by time \(t\),
\[
\sum_{i\in U_t}d_i(d_i-2)
\le -\ell_n\delta_n+t.
\tag{6}
\]
(The root contribution \(d_n(d_n-2)\) is nonnegative.) Hence, for \(t\le T\le\ell_n\delta_n/4\),
\[
\mathbb E[\Delta A_t\mid\mathcal F_t]
\le -\frac{\delta_n}{2}.
\tag{7}
\]
We intentionally keep slack in the constant.

For the conditional second moment,
\[
m_t\,\mathbb E[(\Delta A_t)^2\mid\mathcal F_t]
=
\sum_{i\in U_t}d_i(d_i-2)^2+4(A_t-1).
\tag{8}
\]
For integer \(d_i\ge0\), \(d_i(d_i-2)^2\le d_i^3\) whenever \(d_i\ge1\), while the degree-zero term is zero. Also \(A_t\le\ell_n-2t\). Since \(T\le\ell_n/4\), for all large \(n\), \(m_t\ge\ell_n/4\). Therefore
\[
\mathbb E[(\Delta A_t)^2\mid\mathcal F_t]\le B,
\qquad B:=\frac{4C}{c}+16.
\tag{9}
\]

Stop the queue at \(\tau\). Summing (7) gives
\[
0\le \mathbb E[A_{T\wedge\tau}]
\le d_n-\frac{\delta_n}{2}\,\mathbb E[T\wedge\tau],
\]
which proves (1).

Next, for \(t<T\wedge\tau\),
\[
\mathbb E[A_{t+1}^2-A_t^2\mid\mathcal F_t]
=2A_t\mathbb E[\Delta A_t\mid\mathcal F_t]
+\mathbb E[(\Delta A_t)^2\mid\mathcal F_t]
\le -\delta_n A_t+B.
\tag{10}
\]
Summing (10), using nonnegativity of the terminal square and then (1), yields
\[
\delta_n\,\mathbb E\!\left[\sum_{0\le t<T\wedge\tau}A_t\right]
\le d_n^2+B\mathbb E[T\wedge\tau]
\le d_n^2+\frac{2Bd_n}{\delta_n},
\]
which is (2).

At time \(t<T\wedge\tau\), the exact conditional probability of a collision/surplus pairing is
\[
\frac{A_t-1}{\ell_n-2t-1}.
\]
Since \(T\le\ell_n/4\), this is at most \(4A_t/\ell_n\) for all large \(n\). Therefore (2) and Markov's inequality give (3).

It remains to choose a legal horizon. The third-moment bound gives
\[
d_n^3\le \sum_i d_i^3\le Cn,
\qquad d_n=O(n^{1/3}),
\tag{11}
\]
while \(n\delta_n^3\to\infty\) is equivalent to
\[
n^{1/3}\delta_n\to\infty.
\tag{12}
\]
Consequently
\[
\frac{d_n^2}{\ell_n\delta_n}
=O\!\left(\frac1{n^{1/3}\delta_n}\right)=o(1),
\qquad
\frac{d_n}{\ell_n\delta_n^2}
=O\!\left(\frac1{(n^{1/3}\delta_n)^2}\right)=o(1).
\tag{13}
\]
Also \(d_n/(\ell_n\delta_n^2)\to0\), so one may choose \(K_n\to\infty\) slowly enough that
\[
K_n\frac{d_n}{\ell_n\delta_n^2}\to0.
\tag{14}
\]
Set
\[
T_n=\left\lceil K_n\frac{d_n}{\delta_n}\right\rceil.
\]
Then (14) ensures \(T_n\le\ell_n\delta_n/4\) eventually. By (1),
\[
\mathbb P(\tau>T_n)
\le \frac{\mathbb E[T_n\wedge\tau]}{T_n}
\le \frac{2}{K_n}.
\tag{15}
\]
Combining (3), (13), and (15) proves that the whole component of \(v_n\) has no surplus pairing with probability \(1-o(1)\). This is exactly acyclicity of \(\mathcal C(v_n)\).

For tightness, instead take any fixed \(M>0\) and \(T=\lceil M d_n/\delta_n\rceil\). The same horizon condition holds eventually, and
\[
\mathbb P\!\left(|\mathcal C(v_n)|>1+T\right)
\le \mathbb P(\tau>T)\le\frac{2}{M},
\]
because each pairing discovers at most one new vertex. Letting \(M\to\infty\) proves tightness. \(\square\)

## What this does and does not buy

The preceding checkpoint had reduced the source's hub side to a branching surrogate with normalized variance defect
\[
Q_n=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]
That quantity is unchanged in this run. The graph-level proposition above instead removes one possible failure mode of transporting the surrogate to the actual configuration model: in the finite-third-moment barely-subcritical regime, a component rooted at a chosen maximal-degree vertex is asymptotically a tree. Thus self-intersections, loops and multiple-edge closures do **not** create the missing hub-scale correction.

The unresolved step is more specific now: control the *finite-population drift/depletion of discovered degrees* sharply enough to upgrade the graph component from tightness on the \(d_{\max}/\delta_n\) scale to the source's predicted \((1+o_{\mathbb P}(1))d_{\max}/\delta_n\) law in the hub-dominated regime, and then compare globally with the Erdos–Renyi extreme scale. Acyclicity alone is not that law.

## Prior-art caution

The active-half-edge exploration, negative-drift estimates, and martingale technology are classical and appear in closely related form in the prescribed-degree literature, including Coulson–Perarnau (2023). The bounded searches in this run used the phrases `barely subcritical configuration model tree/acyclic/cycle largest component`, the 2023 paper, the 2019 barely-supercritical paper, and the 4 Aug 2026 monograph. I did not locate this exact maximal-root estimate stated in this form, but a negative search is **not** evidence of novelty. Treat this as a route lemma until a dedicated prior-art audit says otherwise.
