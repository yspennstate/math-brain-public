# account02/B09 — partner-sync addendum: exact hierarchy event-chain nonreuse

**Run:** `20260922T104425Z-account02-B09-fei-packet-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED` (partner-derived strengthening); full unrestricted FEI remains **OPEN**.

After the immutable base report was created, the named partner `account03/B09` published a compatible FEI result:

- account03/B09 run `20260922T104916Z-account03-B09-fei`, scientific commit `776473d56cb62e062f2df8dc776c5ccd720efe90`, theorem family `B-ORBIT-CARDINALITY-SUFFICIENCY-v1` / `B-NESTED-CARDINALITY-EVENT-BANK-v1`.
- It proves exact cardinality sufficiency for permutation-symmetric spectral laws and an exact nested Bernoulli-event decomposition of the resulting KL; on the genuine sparse suspension it recovers the full rare-log `K_occ=Theta(m I)` with zero loss.
- Its explicit next implication is to extend exact event coding to the genuine disjoint-composition hierarchy, including `C_hier`, in a way that survives recursive ternary majority.

This addendum consumes that named partner result and closes that specific representation implication.

## 1. Universal finite nested-event KL identity

Let `P,Q` be probability laws on a finite set `Omega={omega_1,...,omega_M}` with `P << Q`. For `1 <= j <= M`, put

\[
A_j=\{\omega_j,\ldots,\omega_M\},
\quad p_j={P(\omega_j)\over P(A_j)},
\quad q_j={Q(\omega_j)\over Q(A_j)}
\]

whenever `P(A_j)>0` (zero-mass stages contribute zero), and let `d_2` denote Bernoulli KL in bits.

### Theorem A — `FEI-FINITE-NESTED-EVENT-CHAIN-v1`

\[
\boxed{
D_{\rm KL,2}(P\Vert Q)
=\sum_{j=1}^{M-1}P(A_j)d_2(p_j\Vert q_j).
}
\tag{A.1}
\]

### Proof

Reveal the atom by the deterministic sequential code: conditional on membership in `A_j`, ask whether the atom equals `omega_j` or lies in `A_{j+1}`. Under `P` and `Q` this stage has Bernoulli laws `(p_j,1-p_j)` and `(q_j,1-q_j)`. Applying the KL chain rule to the complete deterministic code gives (A.1). Equivalently, expanding the right-hand side telescopes the survival-ratio logarithms to `sum_j P(omega_j) log_2(P(omega_j)/Q(omega_j))`. `QED`.

This is account03/B09's nested-cardinality identity with cardinality bins replaced by arbitrary source atoms; no symmetry is required for the identity itself. Symmetry is required only when one wants cardinality to be a sufficient statistic rather than using the full local atom space.

## 2. Exact binary-event representation of every hierarchy credit

Use account04/B15's exact disjoint-composition identity at a node `v`:

\[
C_v
=D(Q_{\alpha_v}\Vert Q_{A_v})
+\sum_i\alpha_{v,i}D(Q_{r_{v,i}}\Vert Q_{v,i}^{(\zeta_v)}).
\tag{A.2}
\]

Every law in (A.2) lives on a finite nonempty-subset space. Choose once and for all any deterministic ordering of the atoms in each such space and apply Theorem A to each divergence. If `e_{v,0,j}` denotes the resulting Bernoulli KL contribution for the outer mismatch and `e_{v,i,j}` that for child `i`'s tilt mismatch, then

\[
\boxed{
C_v=
\sum_j e_{v,0,j}
+\sum_i\alpha_{v,i}\sum_j e_{v,i,j},
\qquad e_{v,*,j}\ge0.
}
\tag{A.3}
\]

There is no information reuse: (A.3) is an exact KL chain rule, not a union bound or a sum of separately priced inequalities.

## 3. Full-tree event ledger

Let `beta_root=1` and `beta_child=beta_v alpha_{v,i}`. The base B09 theorem already proved

\[
K_{\rm occ}(F_{\rm root})
=\sum_{v\,\mathrm{internal}}\beta_vK_{\rm occ}(G_v)
 +\sum_{v\,\mathrm{internal}}\beta_vC_v
 +\sum_{\ell\,\mathrm{leaf}}\beta_\ell K_{\rm occ}(F_\ell).
\tag{A.4}
\]

Insert (A.3). If desired, apply Theorem A once more to each local `K_occ(G_v)=D(P_v||Q_v)` and each leaf KL. Therefore:

### Theorem B — `FEI-HIERARCHY-EVENT-CHAIN-NONREUSE-v1`

**For every finite disjoint Boolean composition tree, the entire global `K_occ` is an exact activation-weighted sum of nonnegative binary-event KLs attached to actual node-local source/reference laws, with every local dependence term and every hierarchy mismatch term appearing exactly once.**

No fixed-depth truncation, merged tail, or repeated charge is present.

This proves the representation step explicitly requested as the next implication in the named partner's report. It does **not** prove that an arbitrary small subfamily of those events pays the FEI Bellman deficit; that remains the quantitative problem.

## 4. Recursive-majority barrier is passed exactly

For depth-`m` recursive ternary majority, the base report calculated that the weighted hierarchy-credit sum obeys

\[
\sum_v\beta_vC_v
\ge \mu_m(m-4-2\kappa_3)+2+2\kappa_3,
\qquad
\mu_m=(3/2)^m,
\quad \kappa_3=K_{\rm occ}(\mathrm{Maj}_3)\approx0.735604784076543.
\tag{A.5}
\]

By (A.3), the left side of (A.5) is itself exactly a sum of the hierarchy binary-event KLs. Thus a `Theta(mu_m m)` high-scale information bank is explicitly represented by events across the full recursion tree. The account03/B18 fixed/sub-half-depth barrier is not evaded: **all levels are retained**.

Moreover, every local `Maj_3` gate is permutation symmetric, so the named partner's cardinality-sufficiency theorem gives a particularly compact exact nested-cardinality event code for each local `K_occ(Maj_3)`. Hence recursive majority has an exact hybrid event ledger: compact local cardinality events plus full hierarchy-mismatch events.

## 5. Consequence for the packet assignment

The base B09 packet theorem gives any source-valid signed packet lower bound `L_v <= K_occ(G_v)` without double charging inside a node. Theorem B now shows how to retain **all unused local KL plus every hierarchy credit** as an exact binary-event ledger across the composition tree.

Thus the packet-cover problem no longer has a bookkeeping/nonreuse obstruction on decomposable sources. The remaining essential implication is quantitative and prime-local:

`FEI-PRIME-LOG-PACKET-NONREUSE-v2`: on a composition-prime Boolean source, prove a support-conditioned nonlinear signed-convolution packet payment at the rare-event logarithmic scale (the sparse calibration forces leading coefficient `1/4` for the current all-shift tariff), while retaining the exact residual KL/event bank. Then insert it into (A.4) without any information reuse. Alternatively construct a genuine composition-prime Boolean+bias falsifier.

No unrestricted FEI conclusion is claimed.
