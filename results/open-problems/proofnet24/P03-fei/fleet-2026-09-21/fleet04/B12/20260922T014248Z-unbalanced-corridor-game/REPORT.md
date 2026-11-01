# B12 — the arity-10 gate obstruction has an unbalanced restriction corridor

**Run:** `B12-20260922T014248Z-r44`  
**Outcome:** **CANDIDATE_REFUTED / NEW RESTRICTION OBSTRUCTION.** Full uniform-cube Fourier entropy--influence remains **OPEN / NOT PROVED**.  
**Execution:** **WITHOUT_VERIFIED_BRAIN.** Authenticated repository control and scientific sources were consumed directly; no authenticated cognitive-brain retrieval/runtime entered the proof.

## 0. Live target and mechanism change


\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad
V_u=4u(1-u).
\tag{G}
\]

The source-exact equivalence of a finite-cap symmetric nonnegative \(\Gamma\) satisfying (G) with full FEI is in

`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`,
blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`.

The old read-once potential has already been rigorously falsified as an all-gate candidate by a balanced composition-prime arity-ten gate, so this run does **not** repeat the AND-extremality search. It changes mechanism from my preceding prime one-step safe-split argument to an exact **adaptive restriction game** on that gate. The question is whether the positive balanced obstruction can be discharged by descending until one returns to an easier balanced gate.

It cannot: a completely physical fixed coordinate order avoids every proper nonaffine balanced restriction, and even the best adaptive coordinate policy cannot force a nonaffine balanced return.

## 1. Named peer results consumed

### fleet02/B18 — balanced restriction minimality

I consume

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B18/20260922T0117Z-balanced-restriction-minimal-gate/REPORT.md`,
blob `33b7f8e92df3d37c5499413548a3bfd6c5419b7f`.

Its exact implication used here is the following. For the source-exact ten-input balanced monotone gate \(G_*\),

* no codimension-one or codimension-two coordinate restriction is balanced;
* the first balanced descendants occur at codimension three;
* every proper balanced restriction is a literal after dummy deletion or has at most six essential variables; and
* every proper balanced nonliteral restriction obeys
  \[
  \frac{H}{I-1}
  \le
  \frac{46}{5}-\frac95\log_2 3
  =
  6.3470674987\ldots < 6.4548.
  \tag{1.1}
  \]

Thus the positive balanced-uniform margin of \(G_*\) is not inherited by a smaller balanced child.

### fleet02/B16 — exact restriction-margin martingale

I also consume

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`.

For a coordinate split of a gate \(F\), write

\[
P(F)=\frac{I(F)}4-p_F(1-p_F),
\qquad
Q_i(F)=P(F)-\frac{P(F_0)+P(F_1)}2.
\tag{1.2}
\]

For the base potential \(\Gamma_0=0\) at uniform remaining-input biases, let

\[
L_i(F)=H(F)-\frac{H(F_0)+H(F_1)}2.
\tag{1.3}
\]

Then \(Q_i\ge0\), and on \(Q_i>0\) the local restriction margin is \(c_i=L_i/Q_i\). Along every adaptive physical coordinate-restriction policy stopped at an affine gate,

\[
P(F)=\mathbb E\sum_r Q_r,
\qquad
H(F)=\mathbb E\sum_r Q_r c_r.
\tag{1.4}
\]

This is an exact signed/continuation-preserving identity, not an inequality. It is the tool that converts the finite restriction geometry below into a quantitative entropy obstruction.

## 2. Source gate

The inherited gate is the exact arity-ten witness from fleet03/B12:

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B12/20260922T004418Z-arity10-gate-refutation/REPORT.md`.

Its truth-table SHA-256 is

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`.

It is balanced, monotone, essential in all ten coordinates, and composition-prime. Exactly

\[
I(G_*)=\frac{257}{128},
\qquad
P(G_*)=\frac{I-1}{4}=\frac{129}{512}.
\tag{2.1}
\]

The certified entropy enclosure gives

\[
6.509836127588151479
<
H(G_*)
<
6.509836127588151480.
\tag{2.2}
\]

Therefore the pure entropy/Poincare restriction ratio is

\[
\boxed{
\frac{H(G_*)}{P(G_*)}
>
25.837489126551422.
}
\tag{2.3}
\]

At a balanced root this is \(4H/(I-1)\). Subtracting \(4C_0\) with the old read-once cap \(C_0=6.4548\) recovers the already-known positive read-once margin \(>0.01828912655\); (2.3) is used here only in the exact \(\Gamma_0=0\) restriction ledger.

## 3. New theorem A: balanced return is avoidable, and cannot be forced

Consider a physical restriction state of \(G_*\). A policy may choose the next unrevealed coordinate as an arbitrary function of the already revealed coordinate values; the next bit is then revealed under its correct uniform law. Stop when either

1. a **proper balanced nonaffine** restriction is reached, or
2. the current restriction is affine, equivalently \(P=0\).

Let \(R_\pi\) be the probability of event 1 under policy \(\pi\), and let

\[
X_\pi
=
\mathbb E_\pi\!\left[
P(G_\tau)\mathbf 1_{\{\tau\text{ is balanced nonaffine}\}}
\right].
\tag{3.1}
\]

### Theorem 3.1

For this exact Boolean gate,

\[
\boxed{
\min_\pi R_\pi=0,
\qquad
\max_\pi R_\pi=\frac{19}{32}.
}
\tag{3.2}
\]

Moreover

\[
\boxed{
\min_\pi X_\pi=0,
\qquad
\max_\pi X_\pi=\frac{47}{512}.
}
\tag{3.3}
\]

In particular no adaptive coordinate policy can force a return to a proper nonaffine balanced gate: even the optimal hit-probability policy misses with probability at least \(13/32\).

The minimum in (3.2) has a particularly simple witness. Reveal the original ten live coordinates in the fixed order

\[
0,1,2,3,4,5,6,7,8,9.
\tag{3.4}
\]

For **every** assignment branch, this order encounters no proper balanced nonaffine state at all.

### Proof

The adjacent checker reconstructs \(G_*\) from the inherited source slices and then evaluates all \(3^{10}=59049\) coordinate-restriction states exactly.

For any state \(s\), let \(r_{\min}(s),r_{\max}(s)\) be the minimum and maximum future hit probabilities. A proper balanced nonaffine state has terminal value \(1\); an affine state has terminal value \(0\); otherwise

\[
r_{\min}(s)
=
\min_{i\ {\rm free}}
\frac{r_{\min}(s_{i=0})+r_{\min}(s_{i=1})}{2},
\tag{3.5}
\]

with `min` replaced by `max` for \(r_{\max}\). This is an exact finite dynamic program over rational numbers. The same recursion with terminal value \(P(s)\) instead of \(1\) proves (3.3).

For the explicit fixed order (3.4), the exact counts
`(nonaffine balanced, affine balanced, unbalanced)` after each prefix length are

\[
\begin{array}{c|c}
t & (\#B_{\rm nonaff},\#B_{\rm aff},\#U)\\ \hline
1&(0,0,2)\\
2&(0,0,4)\\
3&(0,0,8)\\
4&(0,0,16)\\
5&(0,4,28)\\
6&(0,21,43)\\
7&(0,28,100)\\
8&(0,57,199)\\
9&(0,2,510)\\
10&(0,0,1024).
\end{array}
\tag{3.6}
\]

The balanced states that do occur are affine and therefore carry zero \(P\)-currency. This proves the fixed-order assertion and the minimum zero. The exact dynamic program gives the maxima in (3.2)--(3.3). \(\square\)

## 4. New theorem B: the missing balanced obstruction reappears as an unbalanced entropy/Poincare spike

Run the fixed order (3.4) all the way to affine termination. For every nonterminal state \(v\), let

\[
Q_v=P(v)-\frac{P(v0)+P(v1)}2,
\qquad
L_v=H(v)-\frac{H(v0)+H(v1)}2.
\tag{4.1}
\]

The checker uses rational atanh-series enclosures for every logarithm and proves:

* exactly `96` prefix states have \(Q_v>0\);
* the root split has
  \[
  \frac{L_{\rm root}}{Q_{\rm root}}
  <22.949201161690351;
  \tag{4.2}
  \]
* every positive-currency local ratio satisfies
  \[
  \frac{L_v}{Q_v}\le32;
  \tag{4.3}
  \]
* exactly `37` **unbalanced** states attain equality \(L_v/Q_v=32\); and
* their branch-probability-weighted \(Q\)-currency is exactly
  \[
  \boxed{\frac{29}{1024}},
  \tag{4.4}
  \]
  which is \(29/258\) of the root currency \(P(G_*)=129/512\).

By the fleet02/B16 martingale (1.4),

\[
\frac{\mathbb E\sum_v Q_v(L_v/Q_v)}
     {\mathbb E\sum_v Q_v}
=
\frac{H(G_*)}{P(G_*)}
>
25.837489126551422.
\tag{4.5}
\]

The root one-step ratio is below \(23\), while every later positive-\(Q\) state in this fixed order is unbalanced by (3.6). Hence the large balanced-root obstruction is **not** confined to a balanced state: it is necessarily transferred into the unbalanced corridor. The explicit equality states in (4.4) show this transfer is not merely existential.

## 5. What this rules out

Fleet02/B18 showed that every proper balanced descendant of \(G_*\) is harmless for the old balanced-uniform margin. The new theorem shows a stronger obstruction to a natural repair:

> **False repair:** descend physically until balance returns, pay the smaller balanced descendant, and treat the unbalanced intermediates as a harmless bridge.

For \(G_*\), balance need not return at all before affine termination, and no adaptive coordinate policy can force nonaffine balanced return with probability one. Along a fixed balance-avoiding order the exact entropy/Poincare ledger still carries the root obstruction, with local unbalanced ratios reaching \(32\).

Therefore any replacement all-gate potential or restriction induction that is intended to prove full FEI must control **off-centre output measures and their signed continuation slack**. A theorem only on the balanced slice, even combined with restriction-minimality, is not a closed induction mechanism.

This is not a counterexample to FEI. It is a finite exact obstruction to a balanced-return proof strategy.

## 6. Relation to the older B12/interface-B work

The earlier fleet04/B18 mixed-curvature identity remains intact:

\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k.
\]

Nothing here assumes \(\sum_k d_k=O(J)\); that implication remains unavailable. The current owner message supersedes the older row-coding assignment for substantive work, so this run does not manufacture a row-stability bridge to the gate problem.

## 7. Verification

`check_unbalanced_corridor_game.py` is source-exact and self-contained. It:

1. reconstructs the inherited arity-ten witness and verifies its truth-table SHA-256;
2. recomputes exact \(I=257/128\) and \(P=129/512\);
3. enumerates the fixed-order prefix restriction lattice and proves (3.6);
4. solves both adaptive finite games exactly over rational numbers;
5. computes Fourier entropies with rigorous rational logarithm intervals; and
6. certifies all statements in section 4.

Executed source SHA-256:

`9983acc24e7d149a87740cf393e6ad1ae6ffb79a38c90fe12785148f88f972bf`.

Recorded output SHA-256:

`53084eedf9e4e5c6e7720d90f66f3afa0914123ea61d4e38f1a4efde9a798fc2`.

The exact execution returned `PASS`.

## 8. Status and next implication

**FULL FEI:** OPEN / NOT PROVED.

**Old missing implication:** after the balanced gate falsifier, hope that ordinary coordinate restrictions quickly return to a smaller balanced gate whose margin is already controlled.

**New result:** that implication is false on the explicit prime arity-ten witness. The restriction lattice has a complete balance-avoiding physical corridor, and even optimal adaptive coordinate choice cannot force a proper nonaffine balanced return.

**Replacement obligation:** a viable finite-cap \(\Gamma\) must pay the unbalanced corridor itself. A concrete next target is to use the exact stopping identity

\[
P(G)c_G
=
\mathbb E\!\left[
\sum_{r<\tau}Q_rc_{R,r}
+
P(G_\tau)c_{G_\tau}
\right]
\]

with an off-centre potential term that bounds the pre-return block margin on every prime gate, rather than requiring balance or a good first coordinate. Any such proposal should be tested first on the 37 exact ratio-\(32\) unbalanced states identified here.

No novelty or publication-priority claim is made.
