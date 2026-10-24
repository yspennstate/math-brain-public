Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but this runtime exposes no authenticated reasoning-effort receipt or model-selector control, so I do not claim otherwise.

**SOURCE-LEVEL MOVEMENT.** For the true Chvátal–Sankoff problem of two independent iid uniform binary strings, the repository-internal certified interval strictly shrinks again. The retained lower endpoint is

\[
L=0.792665992=\frac{99083249}{125000000}.
\]

Let `U_S` be P02's preceding exact support-gap endpoint from `2026-09-20T06-05-32Z__label-support-two-step-report.md`. This run proves a stronger four-band radix support theorem and obtains

\[
\boxed{L\le \gamma_2\le U_R<U_S}.
\]

An exact positive-series logarithm certificate proves

\[
\boxed{U_R<0.8262759427622826250151065815372966328234619961931900238808061833125629444302995503<U_S.}
\]

Thus the tracked metric moves strictly from `U_S-L` to `U_R-L`. Diagnostic high precision, not used as proof, gives `U_S-U_R ≈ 4.69997640726158e-82`. Status remains **PARTIAL / source OPEN**.

# P02 / T02 — four-band radix obstruction for tight C045 rows

## 1. Source, continuity, ownership

The target is
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. The same source letters recur across rows and columns of the LCS dynamic-programming grid; no independent Bernoulli matching array is substituted.

Fresh source navigation on 2026-09-20 recovered Alexander Tiskin, `arXiv:2212.01582v2`, revised 2024-08-13. It still states that the coefficient is unresolved and its comments explicitly say that erroneous claims in the earlier preprint concerning the stochastic process and `gamma` were removed from v2. The retained rigorous lower endpoint `0.792665992` is due to Heineman–Miller–Reichman–Salls–Sárközy–Soiffer. Li–Ren–Wen, published online 2026-03-02, still describe determination of the two-string binary constant as open. The stronger C045/P02 upper endpoints are repository-internal candidates pending later independent review and public-priority checking.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`.

Newest own dependency: `proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T06-05-32Z__label-support-two-step-report.md`, blob `9deebe890c88ce94bde9a0a754dc2ee97a02ba1e`.

Newest P13 companion recovered: `proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T06-18-02Z__two-defect-synchronizers-width6-transfer.md`, blob `1bd0fda6239458a25b70ceddfcc436fc750a047f`. P13 remains on the true-source correlated boundary/reset route; it lowers the width-6 finite-to-infinite transfer radius but does not raise the retained source lower endpoint.

Newest current-history LCS report recovered outside the LIVE20 pair: `runs/prob10_2026-09-20/PROB10-02/20260920T0520Z_r17_secondclass_weighted_dual_9b31.md`, blob `d39e6cf56c1e37a6d21aeefaf899fc17509ebeee`. That route develops a correlated single-defect/Bellman potential and reports no source-endpoint movement. P02 therefore remains nonduplicating on the finite covering/cone variational side.

The essential finite core remains R17 C045, `runs/R17/20260918_0926Z_fullcap6_c045_f7a1.md`, with exact all-row cone output blob `0a00ececfdfe58ec85f5a7e6c29bf2559fd58539`. C033–C035 remain withdrawn after the complement-gauge bug; C036 repaired the cocycle transport; C045 is the retained gauge-correct finite core.

Prior P02 handoff: Aldous–Fill Open Problem 2.34 remains closure-packaged at frozen `11/11`; publication novelty there remained explicitly unverified. It is not reopened. Current `POSTED.md` gives no exclusion for T02.

## 2. Primitive operator and inherited tight-row identity

Put
\[
t=\frac pq=\frac{256717}{800000},\qquad d=q-p=543283,
\]
and write the C045 operator as
\[
A=t^2H,\qquad B=SH,\qquad S=q^6d.
\]
The thirty canonical labels have primitive coefficients
\[
c_k=q^{6-k}dp^k\quad(0\le k\le6),\qquad c_7=p^7,
\]
with multiplicities `(2,4,4,4,4,4,4,4)` and `c_0>c_1>...>c_7>0`.

The inherited positive integer witness satisfies
\[
1\le V_i\le M=5\cdot10^{18},\qquad BV\le\frac abV,
\]
where
\[
a=1995237757733917147310102692686664915858011319606812684127301,
\]
\[
b=4220452010631561279,\qquad \gcd(a,b)=1,\qquad b\le M<2b.
\]
Define integer slack
\[
s_i=aV_i-b(BV)_i\ge0.
\]
If `s_i=0`, then `b|V_i`, hence `V_i=b`; the row is tight and `(BV)_i=a`. The exact two-step identity is
\[
\boxed{a^2V_i-b^2(B^2V)_i=a s_i+b\sum_jB_{ij}s_j.}\tag{2.1}
\]

The preceding P02 theorem proved that a tight row has total coefficient weight to non-tight successors at least
\[
D_S=c_0+c_7=142491860994694633120311956186136958404773.
\]
This run exploits the full radix structure of the geometric coefficient progression.

## 3. Tight-row scalar compression

Fix a tight row. For type `k`, let `n_k` be the number of accepted labels going to non-tight successors and `t_k` the number going to tight successors, so `0<=n_k+t_k<=m_k`. Let
\[
U_k=\sum_{\ell\in N_k}V_{j(\ell)},
\]
with `U_k=0` if `n_k=0` and otherwise the necessary bounds
\[
n_k\le U_k\le n_kM.
\]
Set `z_k=bt_k+U_k`. Since every tight successor has witness value `b`, exact row equality becomes
\[
\boxed{a=\sum_{k=0}^7c_kz_k.}\tag{3.1}
\]
Successor coincidences are deliberately forgotten, so any impossibility derived from this relaxation is valid for the actual C045 row.

## 4. Extreme residues force types 0 and 7

Modulo `p`, every coefficient except `c_0=dq^6` vanishes. If `n_0=0`, then `z_0=bt_0`, `t_0 in {0,1,2}`. The exact residues `(a-c_0bt_0) mod p` are
\[
59337,\ 207469,\ 98884,
\]
all nonzero. Hence
\[
\boxed{n_0>0.}\tag{4.1}
\]

Modulo `d`, every coefficient except `c_7=p^7` vanishes. If `n_7=0`, then `z_7=bt_7`, `t_7 in {0,1,2,3,4}`. The exact residues `(a-c_7bt_7) mod d` are
\[
480116,\ 294585,\ 109054,\ 466806,\ 281275,
\]
all nonzero. Hence
\[
\boxed{n_7>0.}\tag{4.2}
\]

The same congruences force
\[
z_0\equiv r_0=237103\pmod p,
\qquad z_7\equiv r_7=181363\pmod d.
\]
Write
\[
z_0=r_0+pu_0,\qquad z_7=r_7+du_7.
\]
Because `n_0<=2`, `n_7<=4` and every witness coordinate is at most `M`,
\[
0\le u_0\le U_0=38953400047522<p^3=16918579124953813,
\]
\[
0\le u_7\le U_7=36813226255928<q^3=512000000000000000.
\]
Subtracting the fixed extreme residues from (3.1) and dividing by `pd` gives
\[
\mathcal A=q^6u_0+\sum_{k=1}^6q^{6-k}p^{k-1}z_k+p^6u_7,\tag{4.3}
\]
where
\[
\mathcal A=14305858008980776443762461938933765900147651115082.
\]

## 5. A p^3 lift forces one non-tight label among types 1,2,3

Assume for contradiction `n_1=n_2=n_3=0`. Then `z_k=bt_k` for `k=1,2,3`, with `t_k in {0,...,4}`. Reducing (4.3) modulo `p^3` gives
\[
q^6u_0\equiv\mathcal A-b(q^5t_1+q^4pt_2+q^3p^2t_3)\pmod{p^3}.
\]
Since `q` is invertible modulo `p^3`, each of the `5^3=125` triples determines one residue for `u_0`. Exact enumeration gives the minimum possible residue
\[
182722050397201
\]
(attained for `(t_1,t_2,t_3)=(0,3,1)`), but this exceeds the global upper bound `U_0=38953400047522`. Because `u_0<p^3`, no alternative representative exists. Therefore
\[
\boxed{n_1+n_2+n_3>0.}\tag{5.1}
\]

## 6. A q^3 lift forces one non-tight label among types 4,5,6

Assume `n_4=n_5=n_6=0`. Reducing (4.3) modulo `q^3` gives
\[
p^6u_7\equiv\mathcal A-b(q^2p^3t_4+qp^4t_5+p^5t_6)\pmod{q^3}.
\]
Since `p` is invertible modulo `q^3`, the `125` triples determine residues for `u_7`. Their minimum is
\[
276424508039578
\]
(attained for `(t_4,t_5,t_6)=(4,1,0)`), exceeding `U_7=36813226255928`. Hence
\[
\boxed{n_4+n_5+n_6>0.}\tag{6.1}
\]

Combining (4.1), (4.2), (5.1), and (6.1), every tight row has non-tight support in four disjoint coefficient bands
\[
\{0\},\quad\{1,2,3\},\quad\{4,5,6\},\quad\{7\}.
\]
Since the coefficients decrease with `k`, its non-tight coefficient mass obeys
\[
\boxed{W_N\ge D_R:=c_0+c_3+c_6+c_7}
\]
with exact value
\[
\boxed{D_R=147353456536129906925733975506591175200000.}\tag{6.2}
\]
This strictly improves `D_S` by the exact factor `D_R/D_S`, numerically about `1.034118408641012`.

## 7. The scalar relaxation is sharp at D_R

The new checker also exhibits an exact solution of the relaxed scalar equation at support `n=(1,0,0,1,0,0,1,1)` with tight counts
\[
(1,2,3,3,3,4,3,0)
\]
and non-tight witness sums
\[
U_0=4986928951742339517,
\]
\[
U_3=4991857513517926901,
\]
\[
U_6=916813856612861589,
\qquad U_7=181363.
\]
These values satisfy all multiplicity and interval constraints and exactly solve
\[
\sum_kc_k(bt_k+U_k)=a
\]
with support mass `D_R`.

This is **not claimed to be an actual C045 row**. It proves something useful about the route: interval-valued successor sums plus coefficient counts alone cannot force a larger universal threshold. Further progress must use actual successor identities/coincidences, or quantitative slack values at the successors.

## 8. Stronger two-step dual bound

From (2.1): if `s_i>0`, then `s_i>=1`; exact arithmetic verifies
\[
a\ge D_RM,
\]
so the right side of (2.1) is at least `D_RV_i`. If `s_i=0`, then `V_i=b`, every non-tight successor has slack at least one, and (6.2) gives
\[
b\sum_jB_{ij}s_j\ge bD_R=D_RV_i.
\]
Thus for every row
\[
\boxed{B^2V\le\frac{a^2-D_R}{b^2}V.}\tag{8.1}
\]
Hence
\[
\rho(B)\le\sqrt{\frac{a^2-D_R}{b^2}}.
\]
For a rational strict majorant define
\[
\boxed{\beta_R=\frac ab-\frac{D_R}{2ab}.}\tag{8.2}
\]
Because
\[
\beta_R^2=\frac{a^2-D_R}{b^2}+\frac{D_R^2}{4a^2b^2}
>\frac{a^2-D_R}{b^2},
\]
we have `rho(B)<beta_R`. Rescaling,
\[
\boxed{\lambda_R=\frac{t^2}{S}\beta_R,\qquad \rho(A)<\lambda_R<\lambda_S<1.}\tag{8.3}
\]

## 9. Dependence-preserving transfer to the original LCS constant

The C045 covering operator enumerates accepted collations of **actual ordered binary source-string pairs**. Suppose its spectral radius at positive fugacities `(x,y)` is below `z<1`. Finite dimensionality gives a constant `K` such that the total accepted collation weight of order `m` is at most `Kz^m`. Every actual length-`n` source pair with `L_n>=m` has at least one accepted covering collation, and every actual pair has probability exactly `4^{-n}`. Coefficient positivity therefore gives
\[
\Pr\{L_n\ge m\}\le K(4xy)^{-n}z^m.\tag{9.1}
\]
No independent probability is assigned to any match cell.

For any
\[
c>\frac{\log(4xy)}{\log z},
\]
putting `m=floor(cn)` makes (9.1) exponentially small. Summing the upper tail of `L_n`, dividing by `n`, and taking `n->infinity` gives
\[
\boxed{\gamma_2\le\frac{\log(4xy)}{\log z}.}\tag{9.2}
\]
With `x=y=t` and `z=lambda_R`, define
\[
U_R=\frac{\log(4t^2)}{\log\lambda_R}.
\]
Because `z -> log(4t^2)/log(z)` is strictly increasing on `(0,1)`, (8.3) implies
\[
\boxed{U_R<U_S.}
\]
This is the source-level interval movement of the run.

## 10. Exact numerical separation and artifacts

The endpoint checker uses only exact rationals and the positive series
\[
-\log z=2\sum_{j\ge0}\frac{u^{2j+1}}{2j+1},\qquad u=\frac{1-z}{1+z},
\]
truncated after 200 terms with the exact geometric remainder bound. It certifies
\[
U_R<Q<U_S,
\]
where
\[
Q=\frac{8262759427622826250151065815372966328234619961931900238808061833125629444302995503}{10^{82}}.
\]

New exact artifact source:
`proofnet24/P02-progress-lcs/artifacts/2026-09-20T07-09-25Z__radix_support_gap_checker.py`, creation commit `ea074bb78727aacdc43c7a83ad4653fb177ab884`, verified blob `b9f3c635176236d06ef0fae5c36c4045e724aefd`.

Executed output:
`proofnet24/P02-progress-lcs/artifacts/2026-09-20T07-09-25Z__radix_support_gap_checker.out`, creation commit `0f09bf6907bc84e303feb2269f44bb1471c18573`, verified blob `19f1701ebce374227afaa856b9a46cf9bec8fbab`. It ends `EXTREME_RESIDUE_FORCES_N0_N7_PASS`, `P3_LIFT_FORCES_GROUP_123_PASS`, `Q3_LIFT_FORCES_GROUP_456_PASS`, `RELAXED_THRESHOLD_SHARPNESS_PASS`, `TWO_STEP_SPECTRAL_STRICTIFICATION_PASS`, `EXACT_LOG_SEPARATOR_PASS`, `SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS`, `ALL_EXACT_CHECKS_PASS`.

No C045 product or witness was regenerated. The new finite certificate is only 250 radix cases plus one exact relaxed equality witness.

## 11. Residual obstruction and next attack

The four-band theorem exhausts this scalar successor-value abstraction: it is sharp at `D_R`. Repeating larger modular tables on the same variables cannot improve the threshold without adding information. The next P02 attack should therefore use one of two genuinely richer mechanisms:

1. actual C045 successor-identity geometry to show that the relaxed `D_R` witness cannot occur in a genuine tight row; or
2. residue information for successor **slacks** `s_j`, not merely the dichotomy `s_j=0` versus `s_j>=1`, to strengthen `sum B_ij s_j` directly.

This differs from P13's boundary-reset route and R17's correlated single-defect route.

```yaml
ledger_delta:
  track: P02
  parent: T02
  target: "Chvatal-Sankoff gamma_2 for two independent iid uniform binary strings"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: UNVERIFIED
  metric: "certified width U-L"
  lower: "99083249/125000000 = 0.792665992"
  upper_before: "U_S = log(4t^2)/log(lambda_S)"
  upper_after: "U_R = log(4t^2)/log(lambda_R)"
  exact_separator: "U_R < 0.8262759427622826250151065815372966328234619961931900238808061833125629444302995503 < U_S"
  movement: true
  status: PARTIAL
  source_status: OPEN
  new_theorem: "every tight C045 row has non-tight label support in four radix bands {0},{1,2,3},{4,5,6},{7}, hence W_N >= c0+c3+c6+c7"
  old_support_gap: 142491860994694633120311956186136958404773
  new_support_gap: 147353456536129906925733975506591175200000
  dependence: "actual iid source-string pairs; no independent Bernoulli matching"
  p13_scope: "correlated boundary/reset transfer; nonduplicating"
  r17_scope: "correlated single-defect/Bellman route; nonduplicating"
  prior_p02_handoff: "Aldous-Fill OP2.34 closure-packaged at 11/11; not reopened"
  review: "internal exact candidate; independent review and public-priority checking pending"
  next_attack: "actual successor-identity geometry or successor-slack residues"
```
