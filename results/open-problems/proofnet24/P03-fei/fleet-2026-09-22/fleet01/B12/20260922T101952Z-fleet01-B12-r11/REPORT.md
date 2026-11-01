# fleet01/B12 — pair-selected physical stopping and centered co-pair matching tax

**Run:** `20260922T101952Z-fleet01-B12-r11`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`, Path C  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were consumed, but no separately verified native brain receiver/context was used.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Live assignment and source corrections

The current B12 assignment is **pair-selected physical stopping**: build a realizable rule that spends co-pair information on nonoverlapping blocks of original coordinates. The current state explicitly forbids replacing full ratio-criticality by all-block terminality alone and records the raw `U4=O(J)` tensor-orientation route as refuted.

The exact source inputs used here are:

1. **TERMINAL_CORE** — `yspennstate/math-open-problems`, commit `85ffa60db26997421d980b1f86c03d82259504ca`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`. It supplies the physical block identities and the minimum-dimensional ratio-critical core.
2. **COPAIR_BARRIER** — same repository/commit, path `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T093723Z-copair-terminal-tax/REPORT.md`. It supplies the exact two-survivor pair identities, including `r_ij=p_ij/4+o_ij`, and the tensor-baseline warning.
3. **ROBUST_ROW** — `yspennstate/math-open-problems`, commit `fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md`. It supplies the trigger-boundary lower bound for a relative-`eta` robust derivative row.
4. **CURVATURE** — `yspennstate/math-open-problems`, commit `200e3fd37fe201f78d882ba8809414d201efb829`, path `proofnet24/P03-fei/fleet-2026-09-22/fleet04/B18/20260922T091529Z-surplus-hidden-curvature/REPORT.md`. It supplies, on a genuine ratio-`rho>4` core, the consequence `0<q_k<1/6` for every active coordinate.
5. **Named partner result actually applied:** fleet02/B12 **SELECTOR_DEBIT**, `yspennstate/math-open-problems`, commit `4ccd51ad517f425a529daa52c3352905b86ea69d`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`, Sections 2--4 only. Its exact coordinate restriction recursion uses the actual Boolean children and actual conditional packet probabilities. I use that identity below to serialize a selected physical pair into two genuine singleton reveals with child recomputation. Its Section 5 quadratic candidate is refuted by later work and is not used.

No fixed all-gate potential, raw hidden-curvature bound, unweighted convolution payment, spectral-sample label, or bounded-incidence assumption is used.

## 1. Source notation

At a centered Boolean state `f`, let `X` denote its Fourier spectral random set and write

\[
q_i=\Pr(i\in X)\le\frac12,\qquad
\mathcal J=\sum_i q_i,
\]
\[
\mathfrak j(q)=1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right),\qquad
\mathcal P=\sum_i\mathfrak j(q_i),\qquad
\mathcal F=H-\mathcal P.
\]

For a physical block `A`, TERMINAL_CORE gives

\[
D_A:=\mathcal J(f)-\mathbb E_z\mathcal J(f_{A=z})
=I_A+C_A,
\quad I_A=\sum_{i\in A}q_i,
\tag{1.1}
\]

and

\[
\Delta_A\mathcal F
:=\mathcal F(f)-\mathbb E_z\mathcal F(f_{A=z})
\le B_A-W_A,
\tag{1.2}
\]

where

\[
B_A=H(X_A\mid X_{A^c}),
\qquad
W_A=\sum_{k\notin A}\mathfrak j'(q_k)c_k(A),
\qquad C_A=\sum_{k\notin A}c_k(A).
\tag{1.3}
\]

All restrictions below are on original physical coordinates. After a child is reached it is character-recentered and all quantities are recomputed there.

## 2. New sharp pair-block charge

Fix distinct surviving coordinates `i,j` and set `A={i,j}`. Define

\[
H_{ij}:=H(X_i,X_j),
\qquad
I_{ij}:=I(X_i;X_j)
=h_2(q_i)+h_2(q_j)-H_{ij}.
\tag{2.1}
\]

Because conditioning cannot increase entropy,

\[
B_{\{i,j\}}
=H(X_i,X_j\mid X_{[n]\setminus\{i,j\}})
\le H_{ij}.
\]

Substituting in (1.2) gives the first new lemma.

### Lemma 2.1 — co-pair-rebated physical charge

For every centered Boolean state and every physical pair,

\[
\boxed{
\Delta_{ij}\mathcal F
\le H_{ij}-W_{ij}
=h_2(q_i)+h_2(q_j)-I_{ij}-W_{ij}.
}
\tag{2.2}
\]

Thus the exact pair mutual information is a **real rebate** against the old coordinatewise entropy charge. It comes from one actual source law; no arbitrary joint distribution is substituted.

The pair law itself is fully source-realizable. If

\[
r_{ij}=\Pr(i,j\in X),
\]
then COPAIR_BARRIER proves

\[
\boxed{r_{ij}=\frac14p_{ij}+o_{ij},}
\tag{2.3}
\]

where `p_ij` is physical derivative-support disagreement and `o_ij` is the opposite-sign orientation overlap. Hence

\[
P_{ij}=(1-q_i-q_j+r_{ij},\ q_i-r_{ij},\ q_j-r_{ij},\ r_{ij})
\tag{2.4}
\]

and `I_ij=D_2(P_ij || P_i\otimes P_j)` retains the orientation mode rather than discarding it.

## 3. Realizable pair-selected stopping rule

Fix `K>2`. At each current nonterminal Boolean descendant, inspect its **current** physical pair laws and choose, for example lexicographically among maximizers, any surviving pair `{i,j}` for which

\[
\boxed{
H_{ij}-W_{ij}<K(q_i+q_j+C_{ij}).
}
\tag{3.1}
\]

Equivalently, with

\[
\sigma_i(K):=h_2(q_i)-Kq_i,
\]
condition (3.1) is

\[
\boxed{
I_{ij}+W_{ij}+K C_{ij}>\sigma_i(K)+\sigma_j(K).
}
\tag{3.2}
\]

Reveal the physical block `{i,j}`, recenter the actual child, recompute all pair laws in that child, and continue. If no pair satisfies (3.1), stop.

This is a finite physical rule. It never conditions on a realized spectral label. The selected pair is a deterministic functional of the current Boolean source, and the actual queried object is the original-coordinate block `{i,j}`. Every query removes two coordinates, so along every branch the queried blocks are disjoint and there are at most `floor(n/2)` pair queries.

### Serialization using the named partner result

The fleet02/B12 selector-debit identity, specialized to the uniform selector bias `s=1/2`, is an exact recursion for a genuine physical coordinate using the actual two Boolean restrictions and their actual conditional Fourier packets. Therefore a pair query can be executed as `i` followed by `j`: after the outcome of `i`, recompute the true child and apply the same identity to `j`. The tower property gives exactly the block-restriction expectation in (1.1)--(1.2). No frozen parent packet, invented selector bit, or uncharged coordinate label is introduced. This is the precise use of the named partner result.

### Theorem 3.1 — nonreusing pair telescope

For every tree generated by (3.1),

\[
\boxed{
\mathcal F(f)-\mathbb E\mathcal F(f_L)
<K\bigl(\mathcal J(f)-\mathbb E\mathcal J(f_L)\bigr)
\le K\mathcal J(f).
}
\tag{3.3}
\]

**Proof.** At each queried node, Lemma 2.1 and (3.1) give `Delta_{ij} F < K D_{ij}`. Multiply by the probability of reaching that node and sum. Both `F` and `J` telescope on the same physical restriction tree, while `D_ij` is exactly the folded-influence loss at that node. Since the queried coordinates disappear, the physical block itself cannot be spent again. QED.

This meets the realizability/nonreuse part of the assignment without any bounded-degree hypothesis.

## 4. New terminal exclusion and matching ledger

Every terminal leaf of the pair rule satisfies, for every remaining pair,

\[
\boxed{
I_{ij}+W_{ij}+K C_{ij}
\le\sigma_i(K)+\sigma_j(K).
}
\tag{4.1}
\]

Consequently, for every matching `M` of disjoint surviving coordinate pairs,

\[
\boxed{
\sum_{\{i,j\}\in M} I_{ij}
\le \sum_{v\in V(M)}\sigma_v(K).
}
\tag{4.2}
\]

Equation (4.2) is the requested **co-pair information spent once**: the right side uses each selected physical coordinate at most once. I do not claim that the `W` or `C` terms separately form a matching-additive global bank; they are simply nonnegative terms that may be dropped from (4.1).

A genuine minimum-dimensional ratio-critical obstruction is even more rigid. If `rho=F/J>K`, TERMINAL_CORE gives

\[
\Delta_A F\ge\rho D_A
\]

for every physical block. Combining this with Lemma 2.1 gives, for every pair,

\[
\boxed{
I_{ij}+W_{ij}+\rho C_{ij}
\le\sigma_i(\rho)+\sigma_j(\rho).
}
\tag{4.3}
\]

Thus a true ratio-critical core is automatically terminal for the sharper pair rule. This uses the full extremality hypothesis that the current Path-C correction requires; it is not inferred from all-block terminality alone.

## 5. Centered orientation: tensor-baseline-safe pair payment

Define the centered pair atom

\[
\widetilde r_{ij}:=r_{ij}-q_iq_j
=\frac14p_{ij}+o_{ij}-q_iq_j.
\tag{5.1}
\]

The joint Bernoulli table in (2.4) differs from its product table by

\[
(+\widetilde r,-\widetilde r,-\widetilde r,+\widetilde r).
\]

Hence its total variation distance from the product is exactly `2|tilde r|`. Pinsker's inequality in bits yields

\[
\boxed{
I_{ij}\ge\frac8{\ln2}\,\widetilde r_{ij}^{\,2}.
}
\tag{5.2}
\]

Combining with (4.1), every terminal leaf obeys

\[
\boxed{
\frac8{\ln2}\widetilde r_{ij}^{\,2}
+W_{ij}+KC_{ij}
\le\sigma_i(K)+\sigma_j(K).
}
\tag{5.3}
\]

For any matching,

\[
\boxed{
\sum_{\{i,j\}\in M}\widetilde r_{ij}^{\,2}
\le\frac{\ln2}{8}\sum_{v\in V(M)}\sigma_v(K).
}
\tag{5.4}
\]

This passes the tensor obstruction exactly. For cross-factor pairs of an exact disjoint tensor, COPAIR_BARRIER gives `p_ij=0` and `o_ij=q_iq_j`, so `r_ij=q_iq_j` and therefore `tilde r_ij=0`, even though the raw opposite-sign/hidden-curvature term is positive. The new ledger subtracts the tensor independence baseline before charging anything. It therefore does not repeat the refuted raw-`U4` argument.

## 6. Robust-row consequence on a true ratio-critical K=4 core

Now assume the genuine Path-C obstruction: a centered minimum-dimensional core with

\[
\rho=\mathcal F/\mathcal J>4.
\]

CURVATURE proves that every active coordinate satisfies

\[
0<q_k<\frac16.
\tag{6.1}
\]

Let row `i` be relative-`1/16` robust with trigger set `F_i`. ROBUST_ROW proves for every trigger `k in F_i`

\[
p_{ik}\ge\frac74q_i.
\tag{6.2}
\]

Using the exact signed co-pair identity (2.3),

\[
r_{ik}=\frac14p_{ik}+o_{ik}\ge\frac7{16}q_i.
\]

Together with (6.1),

\[
\boxed{
\widetilde r_{ik}=r_{ik}-q_iq_k
>\left(\frac7{16}-\frac16\right)q_i
=\frac{13}{48}q_i.
}
\tag{6.3}
\]

Pinsker therefore gives the source-valid trigger-by-trigger information tax

\[
\boxed{
I_{ik}
>\frac{169}{288\ln2}\,q_i^2
=0.846581464966093\ldots\,q_i^2.
}
\tag{6.4}
\]

Since the ratio-critical core satisfies the pair terminal inequality, every trigger also obeys

\[
\boxed{
\sigma_i(4)+\sigma_k(4)
>I_{ik}
>\frac{169}{288\ln2}q_i^2,
}
\tag{6.5}
\]

where weakening from `rho` to `4` only enlarges the available surplus.

Finally, let `M` be any matching in the oriented robust-row/trigger graph, with each edge written `(i,k)` using its robust-row orientation. Equations (4.2) and (6.4) give the nonreusing matching payment

\[
\boxed{
\frac{169}{288\ln2}
\sum_{(i,k)\in M}q_i^2
<\sum_{(i,k)\in M}I_{ik}
\le\sum_{v\in V(M)}\sigma_v(4).
}
\tag{6.6}
\]

This is a new terminal exclusion that combines the actual robust trigger geometry with centered co-pair information while avoiding the tensor-baseline failure.

## 7. Obstruction tests and exact remaining implication

- **Tensor products:** passed exactly by `tilde r=r-qq`; cross-factor pairs cost zero.
- **One-point near-tensor surgery:** the rule does not assert raw hidden curvature is small. It charges only the actual deviation from the product pair law, so the published `U4/J -> infinity` counterfamily does not contradict (5.3).
- **Sparse defects:** no false linear-in-influence entropy claim is made. If pair information is tiny, the rule simply stops and the residual remains for another mechanism.
- **Recursive majority:** no fixed-depth or merged-tail KL projection is used. Pair selection is recomputed from the actual descendant after every physical restriction.
- **Addressing/tribes/majority:** no coordinate is assumed individually large and no prescribed coordinate is charged. The theorem is conditional only on an actually favorable pair; a critical core instead satisfies the universal pair exclusion (4.3).

### Old missing implication

The current Path-C state had exact two-survivor identities and robust-row trigger surplus, but no realizable rule that spent co-pair information without reusing coordinate labels; raw hidden curvature was known to fail because of tensor orientation.

### New proved implication

The pair charge (2.2) yields a finite adaptive physical rule with the exact telescope (3.3). Its terminal class satisfies the co-pair inequality (4.1), every true ratio-critical core satisfies the stronger `rho` form (4.3), and centered orientation admits the tensor-safe matching ledger (5.4). On a `rho>4` critical core, each relative-`1/16` robust trigger edge carries the explicit information tax (6.4), hence every disjoint robust-trigger matching is paid once by (6.6).

### New first unpaid implication

Prove a **source-valid matching/cover lemma** for a true ratio-critical core: either extract enough vertex-disjoint robust-row/trigger edges that (6.6) eliminates the medium/heavy robust load, or show from the exact pair/derivative integrability identities that failure of such a matching forces a different affordable physical block. After that, the small/nonrobust rows still require their own multiscale payment. A generic bounded-degree or raw-`U4` assumption is not available.

Therefore this run is `ESSENTIAL_STEP_APPLIED`, not a full proof candidate. **Full FEI remains OPEN.**

## 8. Scope/privacy review

The changed scientific files contain only FEI mathematics, logical account/slot labels and repository-relative/source-pinned identifiers. No credentials, scheduler IDs, machine paths, email/Drive data, public release, paid/remote compute, workflow dispatch, permission changes, benchmark gold or unrelated private data are included. An automated repository secret scanner was not exposed through the connector in this run; this was a narrow manual changed-file review.
