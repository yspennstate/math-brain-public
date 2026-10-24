SOLUTION STATUS: PARTIAL

# HARD10-04 — recovered blocked 18:46 UTC variation/genealogy iteration

Recovery timestamp: 2026-09-15T19:28:00Z.
Original authored run provenance: the immediately preceding HARD10-04 automation response, which attempted to publish `proofnet24/HARD10-04/runs/2026-09-15/2026-09-15T18-46-00Z__report.md` but was blocked by a platform safety check before any GitHub commit existed. This file is a faithful mathematical recovery of that authored work. Original status was PARTIAL and self-reviewed; no independent verification is retroactively claimed.

## Exact target

For standard external site DLA on \(\mathbb Z^2\), started from \(A_1=\{0\}\), with the next exterior-boundary site selected by simple-random-walk harmonic measure from infinity, set
\[
R_n=\max\{|x|:x\in A_n\}.
\]
The full target is existence/determinism/value of \(\lim \log R_n/\log n\), or a rigorous refutation. This recovered iteration did not close that target.

## Verified dependency used by the original run

The latest GitHub predecessor at the time was

`proofnet24/HARD10-04/runs/2026-09-15/2026-09-15T17-22-40Z__report.md`

commit `ccb6b504ed2835c19eaeb635178814ac90043767`.

It proved, for harmonic measure \(\mu_n=\omega(\cdot,\overline A_n)\) and
\[
\delta_{n+1}:=\|\mu_{n+1}-\mu_n\|_{\rm TV},
\]
that one-step logarithmic-capacity growth satisfies
\[
\frac13\delta_{n+1}^2\le C_{n+1}-C_n\le4\delta_{n+1}^2,
\tag{1}
\]
that \(\delta_{n+1}\lesssim R_n^{-1/2}\) by Beurling, and that
\[
C_n=\frac2\pi\log R_n+O(1).
\tag{2}
\]

## 1. Exact total-variation variation index

### Theorem 1 — PROVED

For every \(q>2\) there is a deterministic constant \(C_q\) such that for every sufficiently large deterministic or stopping time \(m\), pathwise after fixing the DLA trajectory,
\[
\boxed{
\sum_{n=m}^{\infty}\delta_{n+1}^{q}
\le
C_qR_m^{-(q-2)/2}.
}
\tag{3}
\]
Conversely,
\[
\sum_n\delta_{n+1}^q=\infty
\qquad(0<q\le2),
\tag{4}
\]
so the exact summability threshold is \(q_c=2\).

### Proof

Let \(r=R_m\) and define radius-doubling times
\[
\tau_j=\inf\{n\ge m:R_n\ge2^jr\}.
\]
On \(\tau_j\le n<\tau_{j+1}\), Beurling plus the one-step comparison from the predecessor gives
\[
\delta_{n+1}\le C(2^jr)^{-1/2}.
\tag{5}
\]
Also (1) gives
\[
\sum_{n=\tau_j}^{\tau_{j+1}-1}\delta_{n+1}^2
\le3\bigl(C_{\tau_{j+1}}-C_{\tau_j}\bigr).
\tag{6}
\]
By (2), a radius doubling changes capacity by a universal constant, so the right side of (6) is bounded uniformly in \(j\). Therefore
\[
\sum_{n=\tau_j}^{\tau_{j+1}-1}\delta_{n+1}^q
\le
\left(C(2^jr)^{-1/2}\right)^{q-2}
\sum_{n=\tau_j}^{\tau_{j+1}-1}\delta_{n+1}^2
\le
C_q(2^jr)^{-(q-2)/2}.
\]
Summing the geometric series in \(j\) proves (3).

For divergence at \(q=2\), (1) gives
\[
\sum_{k<n}\delta_{k+1}^2\ge\frac14(C_n-C_1),
\]
and \(C_n\to\infty\) because \(R_n\to\infty\). Hence \(\sum\delta^2=\infty\). Since \(0\le\delta_n\le1\), for \(0<q\le2\), \(\delta_n^q\ge\delta_n^2\), giving (4). QED.

This is the exact discrete variation exponent of the harmonic-measure path; it is not the DLA radial exponent.

## 2. Canonical backwards harmonic-measure genealogy

Set \(K_n=\overline A_n\), so \(K_n\subset K_{n+1}\). Define the first-hit kernel from \(K_{n+1}\) to \(K_n\) by
\[
\Pi_n(y,z)=
\begin{cases}
\mathbf1_{\{z=y\}},&y\in K_n,\\
\mathbb P^y\{S_{T_{K_n}}=z\},&y\in K_{n+1}\setminus K_n.
\end{cases}
\tag{7}
\]
The pathwise balayage theorem in the predecessor says exactly
\[
\mu_n=\mu_{n+1}\Pi_n.
\tag{8}
\]

For every finite \(N\), define
\[
\mathbb P_N(y_1,\ldots,y_N)
=
\mu_N(y_N)\prod_{n=1}^{N-1}\Pi_n(y_{n+1},y_n).
\tag{9}
\]
Equation (8) makes these finite-dimensional laws projectively consistent. Kolmogorov extension therefore gives, conditional on the fixed DLA trajectory, a process \((Y_n)_{n\ge1}\) with marginal \(Y_n\sim\mu_n\) and backwards transitions \(\Pi_n\). Call it the harmonic-measure lineage.

Define renewal indicators
\[
J_{n+1}=\mathbf1\{Y_{n+1}\in K_{n+1}\setminus K_n\}.
\tag{10}
\]
Because the backwards transition is identity on old sites, this is exactly the event that the lineage changes state at level \(n+1\).

### Proposition 2 — PROVED

Conditional on the DLA trajectory,
\[
\boxed{
\mathbb P(J_{n+1}=1)=\delta_{n+1}.
}
\tag{11}
\]
More generally, for \(m>n\),
\[
\boxed{
\mathbb P\{\text{at least one renewal between }n\text{ and }m\}
=
\|\mu_m-\mu_n\|_{\rm TV}.
}
\tag{12}
\]

### Proof

The first identity follows because the new-shell mass \(\mu_{n+1}(K_{n+1}\setminus K_n)\) equals the one-step TV distance by the predecessor's balayage theorem.

For (12), no renewal between levels \(n\) and \(m\) occurs iff \(Y_m\in K_n\), because old sites are carried backwards identically. Iterated balayage implies \(\mu_n(z)\ge\mu_m(z)\) for \(z\in K_n\). Thus the outside mass \(1-\mu_m(K_n)\) is exactly the total-variation distance between \(\mu_m\) and \(\mu_n\) after zero-extension. QED.

For each fixed \(n\), the lineage renews again almost surely: by Beurling,
\[
\mu_m(K_n)\le |K_n|\max_z\mu_m(z)\lesssim |K_n|R_m^{-1/2}\to0.
\]
Hence a single lineage has infinitely many renewals almost surely under the auxiliary genealogy law.

## 3. q-lineage overlap hierarchy

Take \(q\) conditionally independent copies of the harmonic-measure lineage for the same fixed DLA trajectory, with renewal indicators \(J_{n+1}^{(1)},\ldots,J_{n+1}^{(q)}\). For an index set \(I\), define
\[
L_q(I)=\sum_{n\in I}\prod_{r=1}^qJ_{n+1}^{(r)}.
\tag{13}
\]
Then conditional independence at a fixed time gives
\[
\boxed{
\mathbb E[L_q(I)\mid\text{trajectory}]
=
\sum_{n\in I}\delta_{n+1}^q.
}
\tag{14}
\]
Consequently, Theorem 1 yields, for every integer \(q\ge3\),
\[
\boxed{
\mathbb E[L_q(\{m,m+1,\ldots\})\mid\text{trajectory}]
\le
C_qR_m^{-(q-2)/2}.
}
\tag{15}
\]
Hence
\[
\mathbb P\{\text{any }q\text{-fold simultaneous renewal after }m\mid\text{trajectory}\}
\le C_qR_m^{-(q-2)/2},
\tag{16}
\]
and every \(q\ge3\) has only finitely many simultaneous renewal times almost surely under the auxiliary lineage law.

For \(q=2\), (1) gives
\[
\boxed{
\frac14(C_n-C_1)
\le
\mathbb E[L_2(\{1,\ldots,n-1\})\mid\text{trajectory}]
\le
3(C_n-C_1),
}
\tag{17}
\]
so the expected pair-overlap local time is comparable to \(\log R_n\). This is an expectation statement only; no almost-sure pair recurrence was claimed.

## 4. Exact pair-overlap representation of capacity

The predecessor supplies the exact one-step form
\[
C_{k+1}-C_k=\rho_k\delta_{k+1}^2,
\qquad\frac13\le\rho_k\le4.
\tag{18}
\]
For two independent lineages,
\[
\mathbb E[J_{k+1}^{(1)}J_{k+1}^{(2)}\mid\text{trajectory}]
=
\delta_{k+1}^2.
\]
Therefore
\[
\boxed{
C_n-C_1
=
\mathbb E\!\left[
\sum_{k<n}\rho_kJ_{k+1}^{(1)}J_{k+1}^{(2)}
\middle|\text{trajectory}
\right].
}
\tag{19}
\]
Using (2),
\[
\boxed{
\log R_n
=
\frac\pi2
\mathbb E\!\left[
\sum_{k<n}\rho_kJ_{k+1}^{(1)}J_{k+1}^{(2)}
\middle|\text{trajectory}
\right]
+O(1).
}
\tag{20}
\]
Thus logarithmic capacity is expected weighted pair-renewal local time of two canonical harmonic-measure lineages.

## 5. Exact remaining second-moment target

For a unit-capacity block \(B_j\), define
\[
L_{2,j}=\sum_{k\in B_j}J_{k+1}^{(1)}J_{k+1}^{(2)}.
\]
Its conditional expectation is bounded above and below by universal positive constants. A uniform estimate
\[
\mathbb E[L_{2,j}^2\mid\text{trajectory}]\le C
\tag{21}
\]
would, by Paley–Zygmund, give a uniformly positive probability of a genuine pair common renewal in each capacity block and would create a plausible regenerative clock.

The original run identified the needed two-time estimate
\[
\mathbb P(
J_k^{(1)}J_k^{(2)}=1,
J_\ell^{(1)}J_\ell^{(2)}=1
\mid\text{trajectory})
\lesssim
\delta_k^2\delta_\ell^2+\text{summable error},
\tag{22}
\]
but did not prove it.

## 6. Ledger at original run completion

### PROVED
- exact total-variation summability threshold \(q_c=2\);
- canonical backwards harmonic-measure genealogy;
- one-step and multi-step renewal/TV identities;
- finite total \(q\)-fold overlap for every \(q\ge3\);
- logarithmically divergent expected pair overlap;
- exact weighted pair-overlap representation of logarithmic capacity.

### CONDITIONAL
- a uniform pair-overlap second-moment/decorrelation theorem would provide a genuine regenerative/ergodic capacity clock.

### OPEN
- existence/determinism/value of the DLA radial exponent;
- almost-sure recurrence versus transience of two-lineage common renewals;
- two-time decorrelation of lineage renewals;
- capacity-time stationarity/ergodicity.

### Original checking status
The run separately checked nesting, the directions of the capacity/TV inequalities, radius-annulus summation, projective consistency, and the distinction between divergent expected overlap and almost-sure recurrence. It was self-review only, with novelty unassessed.
