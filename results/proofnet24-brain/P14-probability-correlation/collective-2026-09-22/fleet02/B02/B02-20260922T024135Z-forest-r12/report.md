# FOREST B02 r12 — exact log-concavity-to-mixture obstruction

Outcome: **ESSENTIAL_STEP_APPLIED**. Parent FOREST target remains **OPEN**. `FULL_PROOF_CANDIDATE=false`. Context: **WITHOUT_VERIFIED_BRAIN**.

Run: `B02-20260922T024135Z-forest-r12`  
Account/slot: `fleet02/B02`  
Fresh control base: `d3aaa92945468cff82b49fbff6d0a488910565cf`  
Owner control revision: `2026-09-22.2`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Role: FOREST — source-valid polynomial/probabilistic comparison for the uniform law on all unrooted forests.

## Exact peer/source state consumed

Lead version consumed: fleet01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, shared-handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`. Its unit-weight complete-graph Hermite subtheorem is not challenged here.

Correction consumed: fleet01/B03 `20260922T014518Z-cocks-gate-refutation`, blob `d992778a8f4d713e3c69304d616c5264d99bd7b0`. This correctly blocks the lead's fixed-graph step `unit pNC on K_n => all-positive-weight pNC on M(K_n)`: Semple–Welsh weighted minor closure cannot be invoked from a unit statement on one fixed graph via the class-level Cocks equivalence.

Named OTHER-account result applied: fleet03/B03 `FOREST-THETA-WEIGHTED-GATE-v1`, blob `05cbe527297b5e78bedc242e165d840f5de17165`. For a simple host `A`, a virtual boundary edge `g` of weight `w`, and marked host edges `e,f`, it writes the exact Rayleigh polynomial
\[
Q_A(w)=D_0+Mw+D_1w^2=\Delta_{A+g}(e,f),
\]
and proves that unit-weight simple theta gadgets realize a dense set of positive responses. Thus a negative `Q_A(w_0)` would compile to a genuine source-valid simple unit counterexample; conversely, a proof of `Q_A(w)>=0` for every host and every `w>0` would close this weighted gate.

Primary source used for log-concavity: N. Anari, K. Liu, S. Oveis Gharan, C. Vinzant, *Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for Independent Sets of Matroids*, arXiv:1811.01600. Their main ingredient is that the homogenization of the generating polynomial of all independent sets of any matroid is completely log-concave. For a graphic matroid, independent sets are exactly forests.

Source-status references: Semple–Welsh, *Negative Correlation in Graphs and Matroids*, CPC 17 (2008), 423–435; Cocks, *Correlated Matroids*, CPC 17 (2008), 511–518.

## 1. Why the log-concavity input is exactly the source law

For a finite simple graph `G`, let
\[
P_G(\mathbf z)=\sum_{F\subseteq E(G):\,F\ {\rm acyclic}}\mathbf z^F.
\]
No root is selected, no connectedness condition is imposed, and no size is fixed: its monomials are exactly **all unrooted forests**, including the empty forest and disconnected forests.

Let `\widetilde P_G(y,\mathbf z)` be the usual homogenization of this independent-set polynomial. ALOV prove that `\widetilde P_G` is completely log-concave. Setting `y=1` is an affine restriction, so
\[
\log P_G(\mathbf z)
\]
is concave on the positive orthant. At `\mathbf z=\mathbf1`, the induced external-field law is exactly the uniform law requested by the source.

More generally, at a positive point `\mathbf z`, let `X_i=1_{\{i\in F\}}`, `p_i=E X_i`, `v_i=p_i(1-p_i)`, and let `C=(\rho_{ij})` be the Pearson correlation matrix. Multiaffinity gives
\[
z_i z_j\,\partial_{ij}\log P_G=\operatorname{Cov}(X_i,X_j)\quad(i\ne j),
\qquad
z_i^2\,\partial_{ii}\log P_G=-p_i^2.
\]
Therefore concavity of `\log P_G` implies
\[
M:=\operatorname{diag}\!\left(\frac{p_i}{1-p_i}\right)
      -(\rho_{ij})_{i\ne j}\succeq0.
\]
Equivalently, if `C` includes diagonal entries `1`,
\[
\operatorname{diag}\!\left(\frac1{1-p_i}\right)-C\succeq0. \tag{1}
\]
At unit weights, deletion of a present edge is a weight-preserving injection from forests containing that edge to forests omitting it, hence `p_i<=1/2`. Thus the actual source law satisfies the unconditional spectral comparison
\[
0\preceq C\preceq2I. \tag{2}
\]
This is spectral negative dependence, not entrywise Rayleigh: ALOV explicitly distinguish the two notions, so (1)–(2) alone do not prove the target sign.

## 2. New exact three-edge mixture theorem

Fix three distinct edges `e,f,g` under any positive external-field forest law. Put
\[
\alpha=P(g\in F),\quad v=\alpha(1-\alpha),
\]
\[
m_e^t=P(e\in F\mid X_g=t),\quad
m_f^t=P(f\in F\mid X_g=t),\quad
\delta_e=m_e^1-m_e^0,\quad \delta_f=m_f^1-m_f^0,
\]
and
\[
c_t=\operatorname{Cov}(X_e,X_f\mid X_g=t).
\]
The law of total covariance is the exact identity
\[
\operatorname{Cov}(X_e,X_f)
=(1-\alpha)c_0+\alpha c_1+v\delta_e\delta_f, \tag{3}
\]
while
\[
\operatorname{Cov}(X_e,X_g)=v\delta_e,\qquad
\operatorname{Cov}(X_f,X_g)=v\delta_f. \tag{4}
\]

Assume both endpoint conditional laws are negatively correlated for the marked pair:
\[
c_0\le0,\qquad c_1\le0, \tag{5}
\]
but suppose the unconditional marked covariance is positive. Write
\[
a=\rho_{ef}>0,\quad b=\rho_{eg},\quad c=\rho_{fg},
\qquad q_i=\frac{p_i}{1-p_i}.
\]
From (3)–(5),
\[
bc\ge a>0. \tag{6}
\]

Apply (1) to the principal triple. We have
\[
\begin{pmatrix}
q_e&-a&-b\\
-a&q_f&-c\\
-b&-c&q_g
\end{pmatrix}\succeq0.
\]
Its determinant is nonnegative:
\[
q_eq_fq_g-q_ec^2-q_fb^2-q_ga^2-2abc\ge0. \tag{7}
\]
Using (6) and AM–GM,
\[
q_ec^2+q_fb^2\ge2\sqrt{q_eq_f}\,bc\ge2\sqrt{q_eq_f}\,a,
\]
and `2abc>=2a^2`. Hence every such violation must obey
\[
(q_g+2)a^2+2\sqrt{q_eq_f}\,a
\le q_eq_fq_g.
\]
The positive root simplifies exactly because
`1+q_g(q_g+2)=(1+q_g)^2`, giving the new bound
\[
\boxed{\rho_{ef}\le
\frac{q_g}{q_g+2}\sqrt{q_eq_f}.} \tag{8}
\]

This is a necessary condition on any positive marked correlation whose two `g`-conditioned endpoint laws already have the desired sign.

## 3. Source-unit and partner-weighted corollaries

For the source unit law, `q_e,q_f,q_g<=1`, so (8) yields
\[
\boxed{\rho_{ef}\le\frac13} \tag{9}
\]
for any hypothetical violation satisfying the two endpoint signs.

There is also an exact counting form. Let `Z` be the forest partition sum and `Z_i` the weighted sum over forests containing edge `i`. Define the Rayleigh difference in the target orientation
\[
\Delta(e,f)=Z_eZ_f-ZZ_{ef}.
\]
A violation has `\Delta<0` and
\[
\rho_{ef}=\frac{-\Delta(e,f)}
{\sqrt{Z_e(Z-Z_e)Z_f(Z-Z_f)}}.
\]
Substituting odds into (8) cancels the square roots and gives
\[
\boxed{
0<-\Delta(e,f)
\le \frac{Z_g}{2Z-Z_g}\,Z_eZ_f.} \tag{10}
\]
At unit weights, the factor is at most `1/3`.

Now apply the named fleet03/B03 one-edge gate. Give only the virtual edge `g` activity `w>0`, leaving host edges unit. Downward closure gives
\[
q_e,q_f\le1,\qquad q_g\le w,
\]
so any interior negative value of its quadratic, provided `D_0,D_1>=0`, must satisfy
\[
\boxed{\rho_{ef}(w)\le\frac{w}{w+2}.} \tag{11}
\]
Writing the partition sum as `Z=A+wB`, this becomes the fully polynomial/counting comparison
\[
\boxed{
0<-Q_A(w)
\le
\frac{wB}{2A+wB}\,
(A_e+wB_e)(A_f+wB_f).} \tag{12}
\]
Thus the partner's weighted gate is now quantitatively constrained at every positive activity, not merely at unit weight.

## 4. Why this does not close the target: sharp mechanism obstruction

The constant `1/3` in (9) cannot be improved using only:
1. the pointwise log-concavity matrix (1), and
2. the endpoint signs (5) plus the exact mixture identities.

Indeed, take an abstract Bernoulli triple with `G~Bernoulli(1/2)`. Conditional on `G=0`, let `E,F` be independent Bernoulli with mean `(1-d)/2`; conditional on `G=1`, let them be independent Bernoulli with mean `(1+d)/2`, where `d=1/sqrt(3)`. Then both conditional covariances are zero and all three marginals are `1/2`, but
\[
\rho_{EF}=1/3,\qquad
\rho_{EG}=\rho_{FG}=1/\sqrt3.
\]
Its correlation matrix has eigenvalues `{1/3,2/3,2}`, so `2I-C` has eigenvalues `{0,4/3,5/3}` and exactly saturates the source spectral constraint.

This law is **not asserted to be forest-realizable**. It is a mechanism-level counterexample showing that the missing implication cannot come from spectral log-concavity plus endpoint negative correlation alone.

## 5. First essential missing implication

The corrected conditional end-to-end route is:

1. Use the source-valid ALOV log-concavity above for the exact all-size unrooted forest measure.
2. Use fleet03/B03 `FOREST-THETA-WEIGHTED-GATE-v1` to reduce source closure to sign control of
   `Q_A(w)=D_0+Mw+D_1w^2` for every simple host and every `w>0`.
3. Endpoint induction/deletion-contraction must supply `D_0,D_1>=0` without the invalid fixed-graph Cocks shortcut; fleet01/B03 identifies `D_1` as the contraction-weight debt because contraction may create positive activities/parallel classes.
4. Once endpoints are known, the remaining sign condition is exactly the graphic-specific cross-term inequality
\[
M\ge-2\sqrt{D_0D_1}
\quad\text{when }M<0, \tag{13}
\]
equivalently nonpositive discriminant for the dangerous quadratic. This would imply `Q_A(w)>=0` for all `w>0`.
5. The theorem (8)–(12) constrains any failure of (13), but the sharp Bernoulli witness proves that pointwise log-concavity alone cannot establish (13).

Therefore the **first essential unpaid implication is now graphic-specific**: prove (13) (together with the contraction endpoint) from forest connectivity/reconnection structure, or exhibit a weighted host violating it. By the partner theta theorem, a genuine negative weighted host would automatically compile to a source-valid finite simple unit counterexample.

## 6. Exact symbolic regression

Executed exact SymPy checker:
`check_spectral_mixture_bound.py`

- source bytes: 1498
- SHA-256: `1c1adc2891c161e7fbe2a5a14506e5da326835881a6583df60010b4950ab4624`
- output bytes: 289
- output SHA-256: `f41bbcecb56f825f5f4fdb8449d2815542667e3daa71ee5ab89689bcdd0c3874`
- verdict: `ALL_CHECKS_PASS`

The checker verifies the determinant identity, the exact positive root, the unit `1/3` corollary, the count-form cancellation, and the sharp abstract witness spectrum. It is regression for the algebra; the theorem proof is the derivation above.

## 7. Status / operations

Scientific status: **ESSENTIAL_STEP_APPLIED**; parent theorem remains OPEN. The lead complete-graph theorem is not promoted to all graphs because the fixed-graph weighted Cocks bridge remains invalid. No random vectors, mock evidence, or unrelated surrogate was used.

Fleet02 managed inventory was inspected only for this account. The twenty managed B01–B20 registrations are enabled, unique, hourly-valid and role-aligned in the exposed inventory; B20 is enabled and quiet delivery is preserved. Scheduler deficit to B20: **none observed**. B02 made **zero** scheduler mutations.

The canonical fleet02/B02 login for the current UTC hour already existed from an earlier actual invocation in that hour and was preserved under create-only semantics; this run has its own unique scientific `start.json` and will have a matching finish. No credentials, scheduler identifiers, machine paths, private transcripts, benchmark gold, email/Drive/public posting, paid model/API, remote workflow, or permission change appears in these artifacts.

Model self-report: `GPT-5.6 Sol`. Requested effort: `maximum supported`. Configured/known effort: `UNKNOWN_NOT_EXPOSED`. Provider usage: `null / NOT_EXPOSED`. Brain context: `WITHOUT_VERIFIED_BRAIN`.
