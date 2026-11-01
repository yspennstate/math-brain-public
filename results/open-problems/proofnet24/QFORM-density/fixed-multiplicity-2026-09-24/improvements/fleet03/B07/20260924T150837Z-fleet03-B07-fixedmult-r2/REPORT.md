SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B07, 2026-09-24T15:08:37Z.

# fleet03/B07 r2 — the two-high leverage collar is impossible; candidate multiplicity eight

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution label: **WITHOUT_VERIFIED_BRAIN**.  
Status: **NEW CANDIDATE FIXED-MULTIPLICITY-8 THEOREM / REQUIRES TWO INDEPENDENT END-TO-END REVIEWS / FULL THREE-EIGENVALUE QFORM OPEN**.

## 1. Fresh source boundary

This run used the current fixed-multiplicity objective and the following source-valid dependencies.

1. Complete self-contained multiplicity-nine manuscript and marginal-free `Z_3` / `Z_2` receivers:
   `yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f`,
   `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`.
2. Eight-direction terminal collar:
   `yspennstate/math-open-problems@5dc3b183bf69c8ab69f725c4464d5073f5c803cd`.
3. Robust two-anchor extraction:
   `yspennstate/math-open-problems@0408c579bcda638e72c010ff99892a22b9049796`.
4. Product-safe incident third-volume receiver:
   `yspennstate/math-open-problems@d44d368cd18a2590fc62d0aadd2cf2b7e9d0e83f`.
5. Zero/one-high leverage closure for the robust pair:
   `yspennstate/math-open-problems@74542593cca87e76d83b07f98e2c895f76b90796`.
6. Designated partner fleet04/B07 coordinate-core theorem:
   `yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T161510Z-fleet04-B07-coordinate-core-r2/REPORT.md`.

No post-rotation independence, moment, support, Gaussian, log-concavity, connected-support, arbitrary-joint coarea, or pointwise rough quadratic-phase hypothesis is used below.

## 2. New lemma: two high leverage coordinates are impossible in the robust no-pivot collar

Use the baseline collar parameters
\[
 \eta=10^{-2},\qquad \kappa=80^{-2}.
\]
The robust-anchor reduction supplies two literal original coordinates `H`, complement `L=H^c`, and
\[
 A=\begin{pmatrix}B&C\\C^T&D\end{pmatrix},
 \qquad
 g:=\det(CC^T)\ge d_0:=\frac{\delta_*^2}{2},
\]
where
\[
 \delta_*=\frac{97}{100}-\frac{297\sqrt2+3\sqrt{202}}{4000}
 =0.8543351401911337\ldots .
\]
Let
\[
 Q_C=C^T(CC^T)^{-1}C,
 \qquad q_i=(Q_C)_{ii}.
\]
This is a rank-two orthogonal projection, hence `sum_i q_i=2`. Define
\[
 J=\{i\in L:q_i>2/3\}.
\]
Therefore `|J|<=2`.

For each pair `a<b` in `L`, define the determinantal weight
\[
 w_{ab}=\frac{\det(C_{\{a,b\}})^2}{g}.
\]
Cauchy--Binet and the standard rank-two determinantal inclusion identity give
\[
 \sum_{a<b}w_{ab}=1,
 \qquad q_i=\sum_{b\ne i}w_{ib}.
\]
Suppose for contradiction that `J={i,j}`. Inclusion-exclusion for this probability measure on two-element subsets gives
\[
 w_{ij}\ge q_i+q_j-1>\frac13,
\]
so
\[
 \det(C_{\{i,j\}})^2>\frac g3. \tag{2.1}
\]

But the state is in the no-`eta`-pivot chamber. Hence every off-diagonal physical coefficient obeys
\[
 |A_{uv}|^2<\eta+\eta^2=\frac{101}{10000}.
\]
Every entry of the literal `2 x 2` matrix `C_{\{i,j\}}` is such an off-diagonal coefficient, so
\[
 |\det C_{\{i,j\}}|
 \le 2(\eta+\eta^2)=\frac{101}{5000},
\]
and therefore
\[
 \det(C_{\{i,j\}})^2
 <\frac{10201}{25000000}
 =0.00040804. \tag{2.2}
\]

On the other hand, the robust-anchor constant is enormously larger. Indeed `sqrt(2)<3/2` and `sqrt(202)<15` imply
\[
 \delta_*
 >\frac{97}{100}-\frac{981}{8000}
 =\frac{6779}{8000}
 >\frac45,
\]
so
\[
 \frac g3\ge\frac{\delta_*^2}{6}>\frac8{75}>0.1. \tag{2.3}
\]
Equations (2.1)--(2.3) contradict each other. Thus
\[
 \boxed{|J|\le1.} \tag{2.4}
\]

This spends the exact last geometric branch left open in fleet03/B20. That theorem already proves that every robust-pair state with `|J|<=1` has a bounded continuous density, quantitatively
\[
 \|p_Q\|_\infty<23.48.
\]
Therefore **the robust two-anchor no-pivot collar is completely paid**.

The point is specifically coordinate-minor selection: two leverage-heavy physical columns would force a single `2 x 2` physical cross minor to carry more than one third of the complete rank-two determinant bank, but the no-pivot entry cap makes such a minor smaller by more than two orders of magnitude.

## 3. Candidate theorem at multiplicity eight

### Theorem candidate `QFORM-FIXED-MULTIPLICITY-8-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with densities `0<=f_i<=K`. Let `A=A^T`, `b` arbitrary and `c` arbitrary. If
\[
 s_8(A)\ge s>0,
\]
then `Q=X^TAX+b^TX+c` has an essentially bounded density satisfying the safe universal estimate
\[
 \boxed{\|p_Q\|_\infty<2400\,\frac{K^2}{s}.} \tag{3.1}
\]
Global continuity is **not** claimed.

### Proof in the normalized case `K=s=1`

Split using the older collar pivot threshold `eta=1/100`.

#### Case A: a scalar pivot exists

If `|A_ii|>=eta`, condition on all other coordinates and complete the square. The conditional scalar-square profile gives
\[
 \|p_Q\|_\infty
 \le \eta^{-1/2}\sup_a\mathbb E|R-a|^{-1/2}.
\]
The Schur spectral-count lemma leaves at least seven unit directions, hence at least five. The multiplicity-nine manuscript's proved five-direction full half-potential proposition applies. With its parameters `d=3/40`, `p=1/400`,
\[
 H_5\le\max\{70,16p^{-1/4},1+d^{-1/2}(J_0+2L_0)\}<115,
\]
using `p^{-1/4}<5`, `d^{-1/2}<4`, `J_0+2L_0<142/5`. Therefore
\[
 \|p_Q\|_\infty<10\cdot115=1150<2400. \tag{3.2}
\]

#### Case B: a principal two-coordinate determinant pivot exists

If a principal pair has determinant modulus at least `eta=1/100`, the definite branch has density at most `pi/sqrt(eta)<40`. In the indefinite branch the pair Schur complement retains at least six unit directions, hence a nonzero unit spectral direction. The proved hyperbolic-pair plus quarter-power logarithmic-potential argument from the multiplicity-nine manuscript applies verbatim; at determinant threshold `1/100` its bound is below `197`, in particular below `2400`.

#### Case C: no `eta`-pivot exists

Apply the eight-direction terminal-collar theorem.

If
\[
 V_3(A)\ge\kappa^3,
\]
a fair literal coordinate cut has crossing third volume at least `4^{-3}kappa^3`. The completed marginal-free order-three receiver has front constant `C_3<15`, hence
\[
 \|p_Q\|_\infty
 <15\,(\kappa^3/64)^{-1/6}
 =15\cdot160
 =2400. \tag{3.3}
\]
This branch has a continuous `C_0` density.

If instead `V_3(A)<kappa^3`, the terminal-collar theorem plus the robust-anchor extraction supply the literal two-anchor block with
\[
 g=\det(CC^T)\ge d_0=0.3649442658827020\ldots .
\]
Section 2 above proves that its high-leverage set has size at most one. The completed B20 theorem then forces product-usable incident third volume and gives
\[
 \|p_Q\|_\infty<23.48. \tag{3.4}
\]
This branch is also continuous.

The three cases exhaust the normalized problem and prove the bound `2400`.

### Scaling

For general `K,s`, put `Y=KX` and
\[
 \widetilde Q
 =Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
\]
The coordinates of `Y` have densities at most one, `s_8(A/s)>=1`, and
\[
 Q=(s/K^2)\widetilde Q.
\]
Density scaling gives (3.1).

## 4. Designated partner fleet04/B07 applied to an actual live inequality

The fleet04/B07 coordinate-core theorem says that on `m=r+3` literal coordinates,
\[
 A[I,I]=D+R+E,
\]
with `|D_ii|>=d`, `rank R<=r`, symmetric `E`, and `max|E_ij|<=epsilon`, implies
\[
 s_3(A[I,I])\ge d-(r+3)\epsilon.
\]

Apply it to a good seed in the eight-direction terminal collar. There
\[
 \epsilon_*={3\sqrt2\over80},\qquad c_*=1-\epsilon_*.
\]
On any seven residual coordinates with `|D_ii|>=c_*`, symmetrize the restricted interpolation decomposition:
\[
 A[I,I]
 =D_I+\frac{P_I+P_I^T}{2}+\frac{E_I+E_I^T}{2}.
\]
The middle term has rank at most four and the final symmetric tail has entrywise modulus at most `epsilon_*`. Taking `r=4`, `m=7`, the partner theorem gives the actual physical-core inequality
\[
 s_3(A[I,I])
 \ge c_*-7\epsilon_*
 =1-8\epsilon_*
 =1-\frac{3\sqrt2}{10}
 >0.5757.
\]
Its physical-fiber consequence is
\[
 \|p_Q\|_\infty
 \le\frac{2\sqrt{42\pi}}{1-3\sqrt2/10}
 <40. \tag{4.1}
\]
Thus any such seven-residual-pivot subbranch is independently paid. The multiplicity-eight proof above needs only the stronger two-anchor closure, but (4.1) is a concrete application of the designated partner result inside the same live collar.

## 5. Audit and status discipline

The new step in this report is only the short implication `|J|=2 => contradiction`, together with the explicit stitching of already completed source-valid lemmas into the multiplicity-eight candidate. I independently checked the determinant inclusion identity, the no-pivot coefficient cap, all displayed constants, and the pivot/no-pivot case split. The numerical values used above are not Monte Carlo evidence; every decisive inequality has an exact algebraic proof.

This report does **not** promote multiplicity eight to owner-validated status yet. The owner protocol requires two independent existing-worker end-to-end reviews of a full candidate. Those reviews do not yet exist for this newly assembled `s_8` proof. Until they do, record:

- fixed multiplicity 8: **CANDIDATE PROOF / PENDING TWO INDEPENDENT END-TO-END REVIEWS**;
- fixed multiplicity 9: separately established by the current manuscript/review stream;
- unrestricted three-eigenvalue QFORM: **OPEN / NOT PROVED / NOT DISPROVED**;
- global continuity at multiplicity 8: **NOT CLAIMED**; continuity is proved only on the two no-pivot third-volume branches used above.
