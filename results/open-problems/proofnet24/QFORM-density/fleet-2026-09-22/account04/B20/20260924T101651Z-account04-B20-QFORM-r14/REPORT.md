SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B20, 2026-09-24T10:16:51Z.

# account04/B20 r14 — corrected proof graph after the sectional obstruction

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Run: \`20260924T101651Z-account04-B20-QFORM-r14\`  
Status: **ESSENTIAL_STEP_APPLIED / PROOF-GRAPH CORRECTION / NEW TERMINAL BRANCH / FULL QFORM OPEN**.

The unrestricted theorem remains open. No full candidate is asserted, so end-to-end reviews are not requested. Continuity remains separate.

## 1. New inputs

The newest completed account01/B20 theorem is

\`yspennstate/math-open-problems@e86f9513af59a0efc602e2a3ea69aa364bc36488\`,

\`QFORM-R51-MODERATE-DIAGONAL-OR-PHYSICALSTAR-PAYMENT-v1\`. Under \(s_3(A)\ge1\), it proves that a still-unpaid target state must satisfy

\[
\max_i|A_{ii}|<\frac1{64}
\quad\text{or}\quad
\max_i\|A[i,-i]\|_2>\frac{1007}{4096}.
\tag{1.1}
\]

Its paid side has \(\|p_Q\|_\infty<9763\). This is a literal original-coordinate dichotomy.

The new account04/B10 result is

\`yspennstate/math-open-problems@42498ecbcb68befe182e1958ff49434cc317206a\`,

\`QFORM-PRODUCT-PROJECTION-SECTIONAL-COUNTEREXAMPLE-v1\` and
\`QFORM-FRESH-LONGITUDINAL-PARABOLIC-PAYMENT-v1\`.

It proves two facts:

1. the proposed universal sectional bound \(M_1(\varrho)\le C\) is false even for an orthonormal projection of three independent cap-one variables, with
   \[
   M_1(\varrho_N)\ge2^{5/4}\sqrt N;
   \tag{1.2}
   \]
2. if the longitudinal variable is genuinely on a disjoint fresh bank, then
   \[
   Q=2(sH+aY)L+V^2
   \quad\Longrightarrow\quad
   \|p_Q\|_\infty\le10s^{-4/5},
   \tag{1.3}
   \]
   and hence the live near-coloop scale \(s=\sqrt c\), \(c>63/64\), gives
   \[
   \|p_Q\|_\infty<10(64/63)^{2/5}<10.064.
   \tag{1.4}
   \]

The account01/B10 parabolic receiver used in (1.3) is source-pinned at
\`1439f3ecb30a49b8363552d780159306f4b9c56f\`.

## 2. New proof-graph theorem

### Theorem 2.1 — \`QFORM-R51-CORRECTED-TERMINAL-GRAPH-v1\`

Starting from the current source-pinned r50/r51 proof chamber, every target-valid matrix follows one of the terminal or retained routes below.

1. **Moderate physical diagonal without a large star.**  
   If \(\max_i|A_{ii}|\ge1/64\) and all physical row stars are at most \(1007/4096\), account01/B20 pays the full law:
   \[
   \|p_Q\|_\infty<9763.
   \tag{2.1}
   \]

2. **Large physical star with a surviving pair completion.**  
   The completed distributed-star derivative split at
   \`f324267086411b9725aa0733e108ab6efc2e760a\`
   gives, whenever the effective star persists through a physical-pair completion with \(\kappa\ge L/64\),
   \[
   \|p_Q\|_\infty<6218/L.
   \tag{2.2}
   \]
   Failure is retained as an explicit cancellation/alignment collar; it is not called solved.

3. **Rank-three harmonic near-coloop with fresh longitudinal bank.**  
   The new B10 terminal (1.3) pays this branch. At the live scale:
   \[
   \|p_Q\|_\infty<10.064.
   \tag{2.3}
   \]

4. **Rank-three harmonic near-coloop with shared longitudinal bank.**  
   The one-sided ruled theorem pays only its majority-sign levels. The minority/two-sheet levels remain. The route
   \[
   \text{product projection}\Longrightarrow M_1(\varrho)\le C
   \]
   is now deleted from the proof graph by (1.2). The nonzero modulation \(aZL\) must be retained.

5. **All-tiny-diagonal retained-tail chamber.**  
   When \(\max_i|A_{ii}|<1/64\), the r50/r52 rank-12/rank-11 representation, both incident-volume collapses, and the nonzero retained tail remain exactly present. No perturbative deletion is allowed.

Therefore the first genuinely unpaid nodes are now:

\[
\boxed{
\begin{array}{l}
\text{(A) the star-cancellation/alignment compiler;}\\
\text{(B) the all-tiny-diagonal, two-sided incident-collapse chamber;}\\
\text{(C) the shared-bank nonzero-modulation minority/two-sheet chamber.}
\end{array}}
\tag{2.4}
\]

The full conjecture would follow if these three nodes were paid by source-preserving receivers, together with the already retained no-fixed-anchor aggregate branch.

### Proof

Item 1 is exactly account01/B20 at (1.1). Item 2 is the completed account04/B08 receiver on its stated physical-pair-completion scope. Item 3 is the convolution reduction in account04/B10: \(T=sH+aY\) is independent of \((L,V)\), has density cap at most \(s^{-1}\), and the account01/B10 exact-null theorem gives (2.3). Item 4 follows from the explicit cap-one product-projection construction giving (1.2), so it is a logical deletion, not merely a failed search. Item 5 preserves the r50/r52 coefficients and gates. The routes are noncircular because no terminal is used to establish its own structural hypothesis. QED.

## 3. Why the correction matters

The previous graph could have suggested that the shared-bank harmonic endpoint would close after a dimension-free bound on the sectional mixed norm

\[
M_1(\varrho)
=\int_{0<|\ell|\le1}|\ell|^{-3/4}
  \int dz\,\|\varrho(z,\ell,\cdot)\|_2\,d\ell.
\]

That implication is false under the full source assumptions. The counterexample already has an orthonormal coefficient triple and independent cap-one original variables. Thus ordinary projection-density or Brascamp--Lieb caps cannot repair this endpoint.

The valid replacement must use the actual nonzero modulation \(aZL\). A viable next estimate must either:

- gain cancellation proportional to \(|a\ell|\);
- quotient the fragmented \(Z\)-direction as \(a\to0\) and recover the two-dimensional exact-null theorem;
- or charge \(z\)-fragmentation through a two-copy product-source identity involving the modulation.

## 4. Compact noncircular frontier

The present source-pinned proof graph is:

\[
\begin{array}{c}
s_3(A)\ge1\\
\downarrow\\
\text{D', D5, ridge/window, physical E3, pair-log and finite-core exits}\\
\downarrow\\
\text{r50/r51 pair-free retained chamber}\\
\downarrow\\
\left\{
\begin{array}{ll}
\max|A_{ii}|\ge1/64,\ \text{no large star} &\Rightarrow (2.1),\\
\text{large star + persistent completion} &\Rightarrow (2.2),\\
\text{fresh harmonic longitudinal bank} &\Rightarrow (2.3),\\
\text{otherwise} &\Rightarrow \text{the retained nodes (2.4).}
\end{array}
\right.
\end{array}
\]

Separate surviving global leaves remain the no-fixed-Plücker-anchor aggregate geometry and finite-carrier variants not matching completed exact packets. No scoped theorem is promoted to a full proof.

## 5. Correction boundary

Preserved throughout:

- no independence after rotation;
- no arbitrary-joint coarea theorem;
- no worst conditional-density supremum;
- no pointwise quadratic Fourier decay for arbitrary cap-one laws;
- no deletion of small nonzero coefficients;
- no use of the one-sided ruled estimate on the minority/two-sheet side;
- no inference that one physical star alone supplies the third smoothing resource.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full continuity: **OPEN**.

Source pins: Claude refreshed source \`b0cbc2233369b6a3f366cf569d425f485f123e1c\`; account01/B20 \`e86f9513af59a0efc602e2a3ea69aa364bc36488\`; account04/B10 \`42498ecbcb68befe182e1958ff49434cc317206a\`; account01/B10 \`1439f3ecb30a49b8363552d780159306f4b9c56f\`; brain login \`913ae385f6cb75c1f95f031a4ea656995ea628cf\`.

Repository publication is transport, not verified native ingestion.
