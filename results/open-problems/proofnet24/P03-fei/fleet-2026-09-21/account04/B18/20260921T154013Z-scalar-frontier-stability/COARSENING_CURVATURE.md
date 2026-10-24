# B18 addendum — strong-concavity payment inside every spectral coarsening

**Status:** **PROVED quantitative strengthening / full FEI OPEN.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The sibling `REPORT.md` gives the exact coarsened slack identity

\[
H(X_i\mid\mathcal G)-bp_i
=\lambda(\Delta_iH-rp_i)
+\lambda(\bar\Delta_{i,\mathcal G}-\Delta_iH)
+\sum_C\bar y_CG_r(\bar q_C).
\tag{1}
\]

The middle Jensen bank can itself be made quantitative with a universal curvature constant.

## Theorem — coarsening variance is paid explicitly

For every coordinate and every sub-sigma-field `G subset sigma(X_-i)`, let

\[
Q=Pr(X_i=1\mid X_{-i}),
\qquad
\bar Q=E[Q\mid\mathcal G].
\]

Then

\[
\boxed{
\bar\Delta_{i,\mathcal G}-\Delta_iH
\ge {2\over\ln2}\,E[(Q-\bar Q)^2].
}
\tag{2}
\]

Consequently, in a restriction-maximal core,

\[
\boxed{
\begin{aligned}
H(X_i\mid\mathcal G)-bp_i
\ge{}&\lambda(\Delta_iH-rp_i)\\
&+{2\lambda\over\ln2}E[(Q-\bar Q)^2]\\
&+c_r\sum_C\bar y_C(\bar q_C-\tau)^2.
\end{aligned}
}
\tag{3}
\]

### Proof

The inherited scalar analysis gives `j''(q)<0` on `(0,1/2)` and symmetry on `(1/2,1)`. Also

\[
h''(q)=-{1\over(\ln2)q(1-q)}\le-{4\over\ln2}.
\]

Hence on `(0,1)`

\[
\Psi''(q)=h''(q)+j''(q)\le-{4\over\ln2}.
\]

Thus `Psi` is `4/ln2`-strongly concave. Conditional Jensen on each `G`-cell gives

\[
\Psi(E[Q\mid\mathcal G])-E[\Psi(Q)\mid\mathcal G]
\ge {2\over\ln2}\operatorname{Var}(Q\mid\mathcal G).
\]

Average the cells to obtain (2). Insert (2) into the exact decomposition (1), then use `G_r(q)>=c_r(q-tau)^2` from the sibling report to obtain (3). QED.

## Block-chain version

For disjoint `A={i_1,...,i_m}` and `V`, let

\[
\mathcal G_j=\sigma(X_V,X_{i_1},...,X_{i_{j-1}}).
\]

Then the chain residual obeys

\[
\boxed{
\begin{aligned}
H(X_A\mid X_V)-bI_A
\ge{}&\lambda\sum_j(\Delta_{i_j}H-rp_{i_j})\\
&+{2\lambda\over\ln2}\sum_j E[(Q_{i_j}-E[Q_{i_j}\mid\mathcal G_j])^2]\\
&+c_r\sum_j\sum_C\bar y_{j,C}(\bar q_{j,C}-\tau)^2.
\end{aligned}
}
\tag{4}
\]

This is a quantitative version of the coarsening-stable polymatroid floor: block residual pays not only endpoint mismatch but also every loss of fine posterior information under the chosen chain coarsening.

## Why this matters for the next phase step

The scalar tangent defect is size-biased by upper mass and therefore weak on `q very small`. The coarsening-curvature bank is different: it is weighted by the full fibre mass and catches **heterogeneity** between low-posterior and endpoint-like fibres whenever a chosen coarse cell mixes them. This gives the integration step a controllable way to choose phase/block partitions and force a payment without reverting to the refuted every-coordinate selector.

It still does not rule out a coarse cell made almost entirely of uniformly tiny posteriors; that remaining square-root-tail regime is isolated in `PHASE_HANDOFF.md` and its global L2 payment in `L2_PHASE_BANK.md`.
