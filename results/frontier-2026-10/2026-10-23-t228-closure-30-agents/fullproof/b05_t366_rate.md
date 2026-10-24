# T366: exact scope and the optimal random-order rate

Date: 2026-10-24. Status: **the original iid problem is already settled by prior literature; no new solution is claimed.** This note independently checks the metric, supplies a short self-contained synthesis and matching historical-loss lower bound, and records the boundary of that synthesis.

## 1. Original quantifiers and current literature

The registry row is broader in informal wording than its source. In [Evron et al. (2022), arXiv:2205.09588v2](https://arxiv.org/html/2205.09588v2), Definition 3 uses

\[
H_k=\frac1k\sum_{t=1}^k\|X_{I_t}w_k-y_{I_t}\|^2,
\]

and Section 6, Theorem 13, explicitly assumes **uniform iid** indices. Repeated occurrences are counted repeatedly. The assumptions are joint realizability, \(X_iw_*=y_i\), \(\|w_*\|\le1\), \(\|X_i\|\le1\), and initialization \(w_0=0\). Individual consistency alone is insufficient. Thus the original source does not require repeated random-reshuffling epochs.

The relevant published ingredients, independently checked at their primary URLs, are:

| Source | Exact dependency / scope |
|---|---|
| [Dereziński–Dong, 2606.29593v1](https://arxiv.org/html/2606.29593v1), Theorem 3.1, Lemma 3.6 | For positive contractions, the operator difference is at most \(3/(k+1)\); the deterministic deletion estimate implies the same rate for an exchangeable sample. |
| [Evron et al., 2504.04579v3](https://arxiv.org/html/2504.04579v3), Definition 4, Lemma B.1 | Occurrence loss is defined with a factor \(1/2\). Exchangeability transfers pre-update residual control to historical loss, for iid and single-pass sampling without replacement. |
| [Schliserman–Koren, 2610.25469v1](https://arxiv.org/html/2610.25469v1), Appendix A.2, Corollary 3 | Explicitly proves \(10R^2\|w_*-w_0\|^2/k\) for halved iid historical linear-regression loss. Therefore the original unhalved problem is directly covered, even without synthesizing the first two sources. |

The local dossier's claim that iid projections still have a gap between \(k^{-1}\) and \(k^{-1/2}\) is stale. Its distinct-seen-set discussion also changes the original metric.

## 2. Theorem with a self-contained proof

Let \(D=\|w_0-w_*\|\), \(R=\max_i\|X_i\|\), and

\[
P_i=I-X_i^+X_i,\quad Q_i=I-P_i,\quad
e_t=w_t-w_*=P_{I_t}e_{t-1}.
\]

For any exchangeable length-\(k\) task sequence and deterministic initialization,

\[
\boxed{\ \mathbb E H_k\le \frac{8R^2D^2}{k}.\ }
\tag{1}
\]

This includes uniform iid sampling for every \(k\), and a uniform permutation prefix for every \(1\le k\le T\). Arbitrary ranks are allowed. The proof is a projector specialization of the published deletion and historical-transfer arguments, not a novelty claim.

**Deterministic calculation.** Fix projectors \(P_1,\ldots,P_k\). Write

\[
W=P_k\cdots P_1,\quad U_j=P_k\cdots P_{j+1}P_{j-1}\cdots P_1,
\quad\Delta_j=U_j-W.
\]

The coefficient of \(z\) in

\[
G(z)=\prod_{j=k}^{1}\bigl(P_j+z(I-P_j)\bigr)
\]

is \(S=\sum_j\Delta_j\). Every factor is unitary on \(|z|=1\); coefficient extraction gives

\[
S=\frac1{2\pi}\int_0^{2\pi}e^{-it}G(e^{it})\,dt,
\qquad\|S\|\le1.
\]

Suffix contraction and the projection energy identity give

\[
\sum_j\|\Delta_je\|^2
\le\sum_j\|(I-P_j)P_{j-1}\cdots P_1e\|^2
=\|e\|^2-\|We\|^2\le\|e\|^2.
\]

Consequently,

\[
\sum_j\bigl(\|U_je\|^2-\|We\|^2\bigr)
=2\langle We,Se\rangle+\sum_j\|\Delta_je\|^2
\le3\|e\|^2.
\tag{2}
\]

**Exchangeability.** Every deleted sequence has the same law as the first \(k-1\) positions. Hence (2) yields

\[
g_k:=\mathbb E\|Q_{I_k}e_{k-1}\|^2
=\mathbb E(\|e_{k-1}\|^2-\|e_k\|^2)
\le3D^2/k.
\tag{3}
\]

Move position \(j\) to the end while retaining all other positions' order. Exchangeability also gives

\[
\mathbb E\|Q_{I_j}U_je_0\|^2=g_k.
\]

Since \(X_i=X_iQ_i\),

\[
\begin{aligned}
\mathbb E H_k
&\le\frac{2R^2}{k}\sum_j
\mathbb E\bigl(\|Q_{I_j}U_je_0\|^2+\|\Delta_je_0\|^2\bigr)\\
&\le2R^2g_k+2R^2D^2/k
\le8R^2D^2/k.
\end{aligned}
\]

All products used above are in their original order; no commutativity, independence after conditioning, or parameter-distance-to-risk equivalence is assumed. The argument only needs exchangeability of the entire length-\(k\) index vector. For iid sampling, it also proves fresh-task residual \(\mathbb E\|Q_Ie_k\|^2\le3D^2/(k+1)\), where \(I\) is an independent draw.

## 3. Matching lower bound for the exact historical metric

Fix \(k\ge2\). In \(\mathbb R^2\), let \(u_+,u_-\) be unit vectors at angles \(\pm\theta/2\) to \(e_1\), where

\[
s=\sin^2\theta=1/k.
\]

Take the two task row matrices to be unit normals to these lines, \(w_*=-e_1\), \(w_0=0\), and \(y_\pm=X_\pm w_*\). Thus \(e_0=e_1\), \(D=R=1\), and the nullspace projectors are \(u_\pm u_\pm^\top\).

For a task sequence, let \(J\) be its number of switches, and \(N\) the number of positions whose task differs from the final task. The final error lies on the final line, and direct multiplication gives the **pathwise historical-loss identity**

\[
\|e_k\|^2=\cos^2(\theta/2)(1-s)^J,
\qquad
H_k=s\cos^2(\theta/2)(1-s)^J\frac Nk.
\tag{4}
\]

For uniform iid sampling of the two tasks, \(\mathbb E N=(k-1)/2\). Since \(J\le k-1\), \(\cos^2(\theta/2)\ge1/2\), and \((1-1/k)^{k-1}\ge e^{-1}\),

\[
\boxed{\ \mathbb E H_k\ge\frac{1}{8ek},\qquad k\ge2.\ }
\tag{5}
\]

No independence between \(N\) and \(J\) is needed: the pathwise lower bound removes \(J\) before expectation. This avoids the common error of substituting the independent-task population risk for historical loss.

For a without-replacement prefix of length \(k\le T\), put \(a=\lfloor T/2\rfloor\) task indices on one line and \(b=\lceil T/2\rceil\) on the other. For any two different positions,

\[
\Pr(I_t\text{ and }I_k\text{ have different types})
=\frac{2ab}{T(T-1)}\ge\frac12.
\]

Thus \(\mathbb E N\ge(k-1)/2\) and the same lower bound follows. Indexed tasks may repeat a linear system; if distinct systems are required, multiply each row and its target by a different scalar arbitrarily close to one. This preserves every projection and changes the loss by an arbitrarily small factor.

It follows that, uniformly over dimension, number of tasks, ranks, and geometry,

\[
\sup\mathbb E H_k=\Theta(k^{-1})\quad(k\ge2)
\]

for iid orderings, and for a single uniform permutation prefix. The constants displayed are not asserted sharp. At \(k=1\), historical forgetting is exactly zero. With one task it is zero at every time; a lower-bound statement must permit at least two tasks. The worst-case task geometry depends on the requested horizon, as is usual for a uniform minimax rate.

## 4. Repeated epochs and the exact remaining boundary

A fresh permutation independently drawn each epoch is not exchangeable across all update positions. Moving or deleting a position across an epoch boundary changes the law. Drawing one permutation and repeating it is another, also nonexchangeable, process. Neither is licensed by (2)–(3) plus exchangeability.

An epoch product need not be symmetric or positive semidefinite, so Theorem 3.1 cannot simply be applied to random epoch products. Conditioning on an epoch's starting iterate yields a bound in the number of updates **within that epoch**, not automatically a bound in total historical updates.

The targeted current search found related random-reshuffling and Kaczmarz work, including [Liu, COLT 2026](https://proceedings.mlr.press/v336/liu26d.html), but its headline alone does not certify the exact full-projection, last-iterate, all-history claim. This note makes **no claim that repeated-epoch \(O(1/k)\) is proved here or globally open**. It is a separate follow-up question, not a surviving obligation of the original 2022 iid theorem.

## 5. Disposition

**Original T366 random-order rate: closed by existing literature, with order \(\Theta(1/k)\).** The full proof above checks the historical metric and a matching lower bound. The single-pass extension is a corollary of published deterministic machinery. Neither is to be reported as a new campaign solution. No existing registry or dossier was modified.
