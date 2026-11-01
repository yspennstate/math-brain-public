Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-FAMILY METRIC MOVED: certified `X_{3,4}` gap `>2649449/100000000 = 0.02649449` -> `>3123709/100000000 = 0.03123709`; parent Benjamini–Schramm source remains OPEN/PARTIAL. Auxiliary delta: the `p_u` floor moves from `719/10000 = 0.0719` to `383213/5000000 = 0.0766426`, while the exact `p_c` upper certificate `4540551/100000000` is unchanged.**

# PROB10-09 — all-genus surface spectral input sharpens the nonbacktracking uniqueness certificate

## 0. Frozen source, continuity, ownership and consumed state

The owner-frozen parent remains:

\[
\forall G=\operatorname{Cay}(\Gamma,S),\qquad
\Gamma\text{ finitely generated and nonamenable},\qquad
p_c(G)<p_u(G)
\]

for iid **bond** percolation on every locally finite Cayley graph. This run does not substitute a planar site-percolation problem. The parent status remains **OPEN / PARTIAL**.

The required pre-refocus handoff already exists and was re-read:

- `runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`, blob `6e1b9e54cbc01461d32b523854c3bd82e50bfd04`.

It preserves the frozen Paley/KNSV/BMO predecessor state and artifacts and records that R20 no longer researches those targets while assigned to PROB10-09.

Controlling / consumed repository state in this run:

- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
- `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md`, previously preserved blob `ee8bde8735e84ff75d3a625fed61e9bafbefd64f`;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/proof_strategy.md`, previously preserved blob `d94127841f3b335a32b7936b86d8dee7a6b8d093`;
- immediate predecessor `runs/prob10_2026-09-20/PROB10-09/2026-09-20T03-28-00Z_tree_fibre_fixedpoint_gap_2f6a91.md`, blob `c455adba17212d0e688b004a16b6388ec6c3a96a`;
- neighboring active percolation route `proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T05-50-00+0300__t09-triangle-fibre-degree9-sl-n-gap.md`, blob `589025d7c772ff9f099ea216f55275a041a08527`.

The June archive's failed/conditional routes are preserved rather than restarted: normalized finite-set escape, BK finite-volume/boundary decomposition, killed-SAW criteria, boundary-energy control, global SAW operator growth, nonbacktracking polynomial transfer, product stress tests, quotient/fibre-shell and bridge criteria. The newest neighboring NM13-11 work owns a distinct **free-core/complement / higher-rank-lattice / triangle-fibre** lane. This run stays on R20's already-delimited **standard surface-product quantitative spectral/nonbacktracking** lane and edits no neighboring claim.

Repository search continues to recover the old source alias `D0061 = lyons_nonamenable_2000::conjecture_3.8_(benjamini-schramm_1996)`. No current canonical claim found in this bounded check assigns R20's exact quantitative surface-product subroute to a different worker.

## 1. Current source / prior-art check

A bounded current check on 20 September 2026 preserved the following distinctions.

1. Hutchcroft, *Percolation on hyperbolic graphs*, arXiv:1804.10191 / GOFA 2019, proves `p_c<p_u` for nonamenable Gromov-hyperbolic quasi-transitive graphs. This is a known special case, not the universal Cayley result.
2. Choi–Seo, *Percolation in acylindrically hyperbolic groups*, arXiv:2508.08932 (2025), proves a nonuniqueness phase for every Cayley graph of an acylindrically hyperbolic group. This is a major later extension and must be counted as known, not fleet progress.
3. Hutchcroft–Pan, arXiv:2409.12283, proves uniqueness-threshold results through subgroup relativization for additional classes; it does not state the universal frozen theorem.
4. Terlov–Timár, arXiv:2502.02560, treats weighted amenability and a relaxed weighted/nonunimodular threshold problem; it does not close the frozen universal Cayley statement.
5. Peres (2000) already gives qualitative nonuniqueness results for nonamenable Cartesian products. Therefore no qualitative novelty is claimed for the standard surface-product family below. The tracked contribution here is an explicit quantitative certificate and a reusable quantitative spectral criterion.
6. The new external ingredient used this run is **Bartholdi–Cantat–Ceccherini-Silberstein–de la Harpe**, *Estimates for simple random walks on fundamental groups of surfaces*, Colloq. Math. 72 (1997), 173–193, DOI `10.4064/cm-72-1-173-193`, arXiv `math/0612409`. Their Section 3 proves for the standard genus-`g` surface-group Markov operator `M_g`
   \[
   \|M_g\|\le \frac{\sqrt{4g-2}}{2g}+\frac1{4g}.
   \tag{1.1}
   \]
   A current public author/archive copy explicitly displays this formula and the genus-4 numerical upper bound `0.5303`.

A fresh bounded search found no 2026 primary source announcing a proof of the full Benjamini–Schramm Cayley-graph bond-percolation conjecture. This is negative search evidence only, not a worldwide novelty certificate.

## 2. Source metric before / after, with auxiliary mechanism delta separate

Freeze the same graph as in the predecessor:

\[
X_{3,4}=\operatorname{Cay}(\Gamma_3\times\Gamma_4,
(S_3\times\{1\})\cup(\{1\}\times S_4)),
\]

where `Gamma_g` is the closed orientable genus-`g` surface group with its standard symmetric `4g`-element generating set.

### Before

The predecessor proved

\[
p_c(X_{3,4})<\frac{4540551}{10^8}=0.04540551
\tag{2.1}
\]

by the exact full-tree fibre pgf / rational fixed-point certificate, and

\[
p_u(X_{3,4})>\frac{719}{10000}=0.0719.
\tag{2.2}
\]

Hence the frozen certified gap was

\[
p_u-p_c>\frac{2649449}{10^8}=0.02649449.
\tag{2.3}
\]

### After

This run leaves (2.1) unchanged and proves the stronger uniqueness-side floor

\[
\boxed{
 p_u(X_{3,4})>\frac{383213}{5000000}=0.0766426.
}
\tag{2.4}
\]

Combining (2.1) and (2.4),

\[
\boxed{
 p_u(X_{3,4})-p_c(X_{3,4})
 >\frac{3123709}{10^8}=0.03123709.
}
\tag{2.5}
\]

Thus the tracked lower-bound metric itself increases by

\[
\frac{3123709-2649449}{10^8}
=\frac{23713}{5000000}
=0.0047426.
\tag{2.6}
\]

**Parent source metric:** unchanged OPEN/PARTIAL; no universal all-Cayley proof.

**Auxiliary mechanism delta:** `p_u` floor `0.0719 -> 0.0766426`; `p_c` certificate unchanged; additionally (1.1) gives a quantitative all-`(g,h)` surface-product `p_u` criterion stated in Section 4 below.

## 3. Idea before code and three genuinely different unexhausted methods

The required idea was written before code at

`artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T03-50-00Z_bcch_surface_spectral_upgrade_idea.md`.

### Route A — import the all-genus surface spectral theorem: SUCCESS

The predecessor used Nagnibeda's sharp genus-3 spectral estimate, but for the genus-4 factor it fell back to the elementary free-subgroup/Freiheitssatz adjacency bound

\[
\|A_4\|\le 2+2\sqrt{13}\approx9.2111.
\]

Equation (1.1) instead yields

\[
\|A_4\|=16\|M_4\|
\le 2\sqrt{14}+1\approx8.4833,
\]

a large enough improvement to move the nonbacktracking root and the frozen gap.

### Route B — use BCCH on both factors: NEGATION TEST / REJECTED

For genus 3, (1.1) gives

\[
\|M_3\|\le \frac{\sqrt{10}}6+\frac1{12}\approx0.6104,
\]

whereas Nagnibeda's rigorous printed upper bound is `0.552792`. Therefore replacing the genus-3 input as well would strictly worsen the adjacency-norm certificate. This independent route was rejected analytically before any checker construction.

### Route C — further optimize the exact `p_c` fibre equation: NUMERICAL DIAGNOSTIC / NO THEOREM CLAIM

The predecessor's exact upper certificate `0.04540551` lies within roughly `3e-9` of the numerical root of the already-proved full-tree activation equation for the `T_10 square T_14` comparison. Thus more rational polishing on the `p_c` side is essentially exhausted at the displayed precision. This is only a diagnostic and is not used as an exact claim. The substantive move was therefore made on the `p_u` side.

These routes are mathematically different: one imports a random-walk spectral theorem, one deliberately tests a weaker symmetric replacement, and one probes the independent branching/fibre side of the certificate.

## 4. Family-level quantitative structural criterion from the BCCH bound

This section records the reusable theorem-sized mechanism separately from the frozen metric.

Let

\[
X_{g,h}=\operatorname{Cay}(\Gamma_g\times\Gamma_h,
(S_g\times\{1\})\cup(\{1\}\times S_h)),
\qquad g,h\ge2.
\]

It is `D`-regular with

\[
D=4g+4h.
\tag{4.1}
\]

The adjacency operator is the commuting tensor sum

\[
A_{g,h}=A_g\otimes I+I\otimes A_h.
\]

From (1.1), since `A_g=4g M_g`,

\[
\|A_g\|\le U_g:=2\sqrt{4g-2}+1.
\tag{4.2}
\]

Hence

\[
\|A_{g,h}\|\le R_{g,h}:=U_g+U_h
=2\sqrt{4g-2}+2\sqrt{4h-2}+2.
\tag{4.3}
\]

For a simple `D`-regular graph, let `N_n` be the endpoint kernel of length-`n` nonbacktracking walks. The standard recurrence is

\[
N_n=A N_{n-1}-(D-1)N_{n-2}\qquad(n\ge3),
\tag{4.4}
\]

with the usual first two initial conditions. Spectral calculus for this polynomial recurrence gives

\[
\limsup_{n\to\infty}\|N_n\|_{2\to2}^{1/n}
\le \beta_D(R),
\tag{4.5}
\]

whenever `||A||<=R`, where, writing `Q=D-1`,

\[
\beta_D(R)=
\begin{cases}
\sqrt Q,&R\le2\sqrt Q,\\[2mm]
\dfrac{R+\sqrt{R^2-4Q}}2,&R>2\sqrt Q.
\end{cases}
\tag{4.6}
\]

Every open connection contains a self-avoiding path and therefore a nonbacktracking witness, so entrywise

\[
T_p\le\sum_{n\ge0}p^nN_n.
\tag{4.7}
\]

Consequently the two-point operator is bounded on `l^2` for every

\[
p<\beta_D(R)^{-1},
\]
which proves

\[
p_{2\to2}(X_{g,h})\ge \beta_D(R_{g,h})^{-1}.
\tag{4.8}
\]

For every infinite Cayley graph, if `p>p_u`, uniqueness of the infinite cluster and FKG imply

\[
T_p(x,y)\ge
\mathbb P_p(x\leftrightarrow\infty,\,y\leftrightarrow\infty)
\ge\theta(p)^2>0.
\]
A kernel bounded below by a positive constant cannot define a bounded operator on `l^2` of an infinite vertex set. Hence

\[
p_{2\to2}\le p_u.
\tag{4.9}
\]

Combining (4.8)-(4.9) gives the explicit all-surface-product quantitative criterion

\[
\boxed{
 p_u(X_{g,h})\ge\beta_{4g+4h}(R_{g,h})^{-1}.
}
\tag{4.10}
\]

This is a complete structural inequality under the precise standard generating-set hypothesis. It is **not** claimed to be qualitatively new: product nonuniqueness was already known. It is mechanism progress and a source-valid quantitative certificate that can be combined with independent `p_c` upper bounds.

## 5. Exact frozen `X_{3,4}` upgrade

For genus 3, retain the stronger Nagnibeda bound as printed in the literature:

\[
\|M_3\|\le0.552792=\frac{69099}{125000}.
\]

For exact arithmetic we relax this upward by only `8e-6`:

\[
\|M_3\|<\frac{691}{1250}=0.5528.
\]

Therefore

\[
\|A_3\|<12\cdot\frac{691}{1250}
=\frac{4146}{625}.
\tag{5.1}
\]

For genus 4, (4.2) gives

\[
\|A_4\|\le1+2\sqrt{14}.
\tag{5.2}
\]

The exact rational comparison

\[
\left(\frac{187083}{50000}\right)^2-14
=\frac{48889}{2500000000}>0
\]
shows

\[
\sqrt{14}<\frac{187083}{50000}.
\]
Thus

\[
\|A_4\|<1+2\frac{187083}{50000}
=\frac{212083}{25000}.
\tag{5.3}
\]

Since `X_{3,4}` has degree

\[
D=12+16=28,
\qquad Q=D-1=27,
\]
(5.1)-(5.3) give

\[
\|A_{3,4}\|<
\frac{4146}{625}+\frac{212083}{25000}
=\frac{377923}{25000}
=:\overline R.
\tag{5.4}
\]

Set

\[
p_*:=\frac{383213}{5000000},
\qquad
z_*:=p_*^{-1}=\frac{5000000}{383213}.
\tag{5.5}
\]

The executed exact checker proves

\[
z_*^2-27
=\frac{21034990509037}{146852203369}>0,
\tag{5.6}
\]
so `z_*>sqrt(27)`, and

\[
z_*^2-\overline R z_*+27
=\frac{8171163}{146852203369}>0.
\tag{5.7}
\]

Also `\overline R>15>2\sqrt{27}`, so the quadratic

\[
q(z)=z^2-\overline R z+27
\]
has two positive real roots with the larger root strictly larger than `sqrt(27)`. Since `z_*>sqrt(27)` and `q(z_*)>0`, (5.7) places `z_*` strictly to the right of the larger root. Monotonicity of the larger nonbacktracking root in the adjacency-norm parameter then gives

\[
\beta_{28}(\|A_{3,4}\|)
<\beta_{28}(\overline R)
<z_*.
\tag{5.8}
\]

By (4.8)-(4.9),

\[
p_u(X_{3,4})\ge p_{2\to2}(X_{3,4})
>z_*^{-1}
=\frac{383213}{5000000}.
\tag{5.9}
\]

Combining (5.9) with the predecessor's already exact, unchanged

\[
p_c(X_{3,4})<\frac{4540551}{10^8}
\]
yields

\[
 p_u-p_c
 >\frac{7664260-4540551}{10^8}
 =\boxed{\frac{3123709}{10^8}}.
\]

This proves the frozen metric move.

## 6. Executed exact test and falsification record

Code:

`artifacts/prob10_2026-09-20/PROB10-09/bcch_surface_spectral_upgrade_exact.py`

Archived output:

`artifacts/prob10_2026-09-20/PROB10-09/bcch_surface_spectral_upgrade_exact.out`

The checker was executed in the run environment before archiving the output. It uses Python `fractions.Fraction` only. The exact output records:

- Nagnibeda relaxation margin `1/125000`;
- `sqrt(14)` rational-square margin `48889/2500000000`;
- product adjacency upper rational `377923/25000`;
- `z_*^2-27 = 21034990509037/146852203369 > 0`;
- quadratic root-comparison margin `8171163/146852203369 > 0`;
- new gap `3123709/100000000`;
- old gap `2649449/100000000`;
- gap improvement `23713/5000000`;
- final verdict `ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent audit.

The explicit negation tests were also informative: using BCCH on genus 3 would worsen the certificate relative to Nagnibeda, while further `p_c` full-tree rational tuning is numerically at the existing activation root to the displayed precision. Neither failed route is relabelled as a theorem.

## 7. What remains open

The full source obligation is unchanged:

\[
\boxed{
\text{For every finitely generated nonamenable group }\Gamma
\text{ and every finite Cayley generating set }S,
\quad p_c(\operatorname{Cay}(\Gamma,S))<p_u(\operatorname{Cay}(\Gamma,S)).
}
\]

This run proves only a sharper quantitative inequality for one frozen standard surface-product graph and a quantitative `p_u` criterion for all standard surface products. The missing universal step is still a mechanism that survives arbitrary nonamenable Cayley geometry without relying on hyperbolicity, acylindrical hyperbolicity, a product decomposition, a specially embedded free-core/fibre structure, or an already-known subclass theorem.

No claim of complete source closure is made. No independent validation has been received for this run's new theorem/certificate. A source-level closure would still require a universal proof (or source-valid counterexample), current prior-art verification, and the independent validation required by the operations contract.

## 8. Structured ledger delta

```yaml
ledger_delta:
  worker: PROB10-09 / R20
  source: Benjamini-Schramm nonuniqueness-phase conjecture, iid bond percolation on Cayley graphs
  parent_status_before: OPEN/PARTIAL
  parent_status_after: OPEN/PARTIAL
  frozen_graph: X_{3,4} standard Cayley graph of Gamma_3 x Gamma_4
  source_metric:
    name: certified lower bound on p_u(X_{3,4}) - p_c(X_{3,4})
    before: 2649449/100000000
    after: 3123709/100000000
    delta: 23713/5000000
  auxiliary_delta:
    pc_upper_before: 4540551/100000000
    pc_upper_after: 4540551/100000000
    pu_lower_before: 719/10000
    pu_lower_after: 383213/5000000
    mechanism: BCCH all-genus surface spectral upper bound + retained Nagnibeda genus-3 input + nonbacktracking two-point transfer
  structural_scope_added:
    statement: p_u(X_{g,h}) >= 1/beta_{4g+4h}(2sqrt(4g-2)+2sqrt(4h-2)+2) for standard surface-product Cayley graphs, with the standard sub-Ramanujan branch convention
    status: PROVED_IN_REPORT_SELF_CHECKED_NOT_INDEPENDENTLY_AUDITED
  exact_test: artifacts/prob10_2026-09-20/PROB10-09/bcch_surface_spectral_upgrade_exact.py
  exact_output: artifacts/prob10_2026-09-20/PROB10-09/bcch_surface_spectral_upgrade_exact.out
  exact_test_verdict: ALL_EXACT_CHECKS_PASS
  independent_audit: NONE
  unresolved_full_gap: universal arbitrary-nonamenable-Cayley mechanism
  neighbor_nonduplication: NM13-11 retains free-core/complement/higher-rank-lattice/triangle-fibre lane
```

No schedule, email, Drive, public posting, force push, or other-track file edit was made.
