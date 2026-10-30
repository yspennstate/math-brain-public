# B18 FEI proof integration — centered tangent polymatroid and exact correlation/coarsening conservation

**Date:** 21 September 2026  
**Status:** **PARTIAL / PROVED universal structural synthesis. Full uniform-cube Friedgut--Kalai FEI remains OPEN / NOT PROVED.**  
**Route:** APPROACH 11/12 (decision-tree entropy payment / restricted-potential dual).  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval or receiver-context use was available or claimed.  
**Novelty:** no publication-priority claim.

Fresh scientific `master` was resolved during this run, most recently at `7756f52c2081f428df61ca093295af3507d23dd8` before this write. I used the current owner-required FEI packet and the newest compatible exact lemmas, without rerunning the read-once certificate or auditing peer calculations.

The inputs used at their proved scopes are:

1. fleet04/B18's exact scalar tangent-defect/coarsening theorem (`20260921T154013Z-scalar-frontier-stability/REPORT.md`): for a restriction-maximal hard core, every coarsened one-coordinate entropy increment has an exact decomposition into restriction-criticality surplus, `Psi`-Jensen gain, and a nonnegative tangent defect;
2. fleet01/B18's coarsening-stable scalar frontier and endpoint-domination reports: the residual set function `H(X_U)-b I_U` is monotone submodular, and uncentered Bernoulli erasure is endpoint dominated;
3. fleet02/B18's KL-projection/Han identity: `K_q=T-(n/q)\bar T_q` is exactly the spendable fixed-cardinality total-correlation contraction;
4. fleet03/B18's sharp general-law density floor `K_q >= [(n-q)/(q(n-1))]T`;
5. the already-proved top-degree parity theorem ruling out exact simultaneous scalar-frontier endpoints in the currently relevant ratio range. I do not redo that argument here.

The new step is to **center the scalar-frontier polymatroid by the exact physical criticality surplus**. This produces a normalized monotone submodular potential whose singleton, co-singleton, fixed-cardinality, and chain gaps are *exactly* total correlation, dual total correlation, KL projection loss, and coarsening/tangent defect. It gives a source-exact conservation law for APPROACH 11/12 and identifies what an adaptive proof must change rather than merely reorder.

---

## 1. Setup

Let
\[
g:\{-1,1\}^R\to\{-1,1\}
\]
be a nonconstant physical-restriction descendant maximizing
\[
r={H(g)\over I(g)}
\]
among its physical restriction descendants, with `r>4`. Let `X` be its Fourier spectral sample,
\[
\Pr(X=S)=\widehat g(S)^2,
\qquad p_i=\Pr(i\in X)=\operatorname{Inf}_i(g),
\qquad I=\sum_i p_i.
\]

Use the inherited scalar-frontier notation
\[
\tau=\tau(r),\qquad
b=b(r)={h_2(\tau)\over\tau},
\qquad
{\Psi(\tau)\over\tau}=r,
\]
and let `lambda=lambda(r) in (0,1)` be the exact supporting-line slope from the scalar tangent theorem.

For every relevant coordinate define the **physical criticality surplus**
\[
C_i:=\Delta_iH-rp_i\ge0,
\qquad C:=\sum_iC_i.
\tag{1.1}
\]

For a sub-sigma-field `G subseteq sigma(X_{-i})`, put
\[
\bar Q_{i,G}=\Pr(X_i=1\mid G),
\qquad
\bar\Delta_{i,G}=\mathbb E\Psi(\bar Q_{i,G}),
\]
and define the inherited nonnegative coarsening/tangent pieces
\[
J_{i,G}:=\bar\Delta_{i,G}-\Delta_iH\ge0,
\tag{1.2}
\]
\[
S_{i,G}:=\sum_{\text{coarse cells }A}\bar y_A G_r(\bar q_A)\ge0,
\tag{1.3}
\]
where `G_r` is the exact scalar tangent defect and `bar y_A` is the upper spectral mass in the coarse cell.

The inherited exact coarsened identity is
\[
\boxed{
H(X_i\mid G)-bp_i
=\lambda C_i+\lambda J_{i,G}+S_{i,G}.
}
\tag{1.4}
\]
For full conditioning `G=sigma(X_{-i})`, `J=0`; write
\[
S_i^*:=S_{i,\sigma(X_{-i})},
\qquad S^*:=\sum_iS_i^*.
\tag{1.5}
\]
Then
\[
B-bI=\lambda C+S^*,
\qquad B:=\sum_iH(X_i\mid X_{-i}).
\tag{1.6}
\]

---

## 2. PROVED: the centered tangent polymatroid

### Theorem 2.1

Define for every coordinate set `U subseteq R`
\[
\boxed{
\mathcal Q_r(U)
:=H(X_U)-b\sum_{i\in U}p_i
-\lambda\sum_{i\in U}C_i.
}
\tag{2.1}
\]
Then `Q_r` is a normalized, monotone, submodular set function.

More precisely, for `i notin U`,
\[
\boxed{
\mathcal Q_r(U\cup\{i\})-\mathcal Q_r(U)
=\lambda J_{i,U}+S_{i,U}\ge0,
}
\tag{2.2}
\]
where `J_{i,U},S_{i,U}` mean (1.2)--(1.3) with `G=sigma(X_U)`.

### Proof

Normalization is immediate. Submodularity follows because `U -> H(X_U)` is submodular, while the influence and criticality terms in (2.1) are modular.

For monotonicity,
\[
\begin{aligned}
\mathcal Q_r(U+i)-\mathcal Q_r(U)
&=H(X_i\mid X_U)-bp_i-\lambda C_i\\
&=\lambda J_{i,U}+S_{i,U}
\end{aligned}
\]
by the exact inherited coarsening identity (1.4). Both terms are nonnegative. QED.

### Corollary 2.2 — strengthened all-block floor

For all disjoint `A,V subseteq R`,
\[
\boxed{
H(X_A\mid X_V)
\ge b I_A+\lambda\sum_{i\in A}C_i,
\qquad I_A:=\sum_{i\in A}p_i.
}
\tag{2.3}
\]

Indeed this is `Q_r(V union A)-Q_r(V)>=0`. This packages the coordinatewise physical-criticality surplus into every spectral block conditional entropy with the same sharp tangent coefficient `lambda`.

The earlier potential `H(X_U)-bI_U` was already monotone submodular. The new point is that the entire modular bank `lambda sum_{i in U}C_i` can be **refunded exactly** while preserving monotonicity. What remains in every marginal is purely coarsening/tangent defect.

---

## 3. PROVED: total correlation and dual total correlation are the two boundary gaps of the same potential

Write
\[
T:=\operatorname{TC}(X)=\sum_i h_2(p_i)-H(X)
\tag{3.1}
\]
for total correlation, and
\[
D:=\operatorname{DTC}(X)
=H(X)-\sum_iH(X_i\mid X_{-i})
=H-B
\tag{3.2}
\]
for dual total correlation.

### Theorem 3.1

The centered tangent polymatroid satisfies the exact identities
\[
\boxed{
T=\sum_i\mathcal Q_r(\{i\})-\mathcal Q_r(R),
}
\tag{3.3}
\]
\[
\boxed{
D=\mathcal Q_r(R)
-\sum_i\bigl[\mathcal Q_r(R)-\mathcal Q_r(R\setminus\{i\})\bigr].
}
\tag{3.4}
\]
Moreover
\[
\boxed{
\mathcal Q_r(R)=D+S^*.
}
\tag{3.5}
\]

### Proof

For (3.3), all modular terms cancel:
\[
\sum_i\mathcal Q_r(\{i\})-\mathcal Q_r(R)
=\sum_i h_2(p_i)-H=T.
\]

The last marginal in coordinate `i` is, by (2.2) with `U=R\setminus\{i\}`,
\[
\mathcal Q_r(R)-\mathcal Q_r(R-i)=S_i^*,
\tag{3.6}
\]
because no coarsening remains. Hence the second term in (3.4) is `S^*`. On the other hand,
\[
\mathcal Q_r(R)
=H-bI-\lambda C
=(H-B)+(B-bI-\lambda C)
=D+S^*
\]
by (1.6), proving (3.5) and then (3.4). QED.

**Interpretation.** `TC` is the gap between the sum of the *first* marginals and the full value of the centered potential; `DTC` is the gap between the full value and the sum of its *last* marginals. Product-like dependence and co-deterministic dependence are therefore not two unrelated banks in this route: they are the two boundary submodularity gaps of one exact polymatroid.

---

## 4. PROVED: fixed-cardinality Han/KL credit is unchanged by the optimal modular centering

Let
\[
h_q:=\mathbb E_{|U|=q}H(X_U),
\qquad
\bar T_q:=\mathbb E_{|U|=q}\operatorname{TC}(X_U).
\]
The inherited Han/KL credit is
\[
A_q=h_q-{q\over n}H,
\qquad
K_q={n\over q}A_q
=T-{n\over q}\bar T_q.
\tag{4.1}
\]

### Theorem 4.1 — projection conservation

For every `1<=q<=n-1`,
\[
\boxed{
\mathbb E_{|U|=q}\mathcal Q_r(U)
-{q\over n}\mathcal Q_r(R)
=A_q,
}
\tag{4.2}
\]
and equivalently
\[
\boxed{
{n\over q}\mathbb E_{|U|=q}\mathcal Q_r(U)
=\mathcal Q_r(R)+K_q
=D+S^*+K_q.
}
\tag{4.3}
\]

### Proof

In a uniformly random q-subset, every coordinate occurs with probability `q/n`. Therefore both modular terms in (2.1) average to exactly `q/n` of their full values. They cancel from the left side of (4.2), leaving
\[
h_q-(q/n)H=A_q.
\]
Use (3.5) and the definition of `K_q` for (4.3). QED.

Combining with the sharp general-law projection-density theorem already proved by fleet03/B18 gives the immediately usable universal inequality
\[
\boxed{
{n\over q}\mathbb E_{|U|=q}\mathcal Q_r(U)
\ge
D+S^*
+{n-q\over q(n-1)}T.
}
\tag{4.4}
\]
For the Boolean spectral phase/Hellinger bank `t` from the compatible B18 phase theorem, `T>=t/ln 2`, hence also
\[
\boxed{
{n\over q}\mathbb E_{|U|=q}\mathcal Q_r(U)
\ge
D+S^*
+{n-q\over q(n-1)\ln2}\,t.
}
\tag{4.5}
\]
Any stronger certified lower bound on `t` (for example the joint phase-discrepancy packing `t>=Theta(A)`) may be inserted without double counting.

### Route consequence / killed shortcut

The centering in (2.1) is the strongest modular refund supplied by the scalar tangent theorem, but **no modular centering can improve the Han/KL projection credit**: fixed-cardinality averaging annihilates every modular correction exactly. Thus a proof that only replaces the old scalar-frontier potential by a better *modularly centered* one and then repeats the same uniform q-block averaging cannot create a new negative term beyond the already-known `K_q`.

To beat the current fixed-q toll `Rcal_q-K_q`, APPROACH 12 needs a genuinely **nonmodular** spectral/phase/level potential, or APPROACH 11 must use an adaptive physical selection law rather than uniform fixed-cardinality projection. This is a precise route reduction, not a statement that all restricted potentials fail.

---

## 5. PROVED: exact order conservation for every spectral chain

Fix any permutation
\[
\pi=(i_1,\ldots,i_n),
\qquad
\mathcal G_j=\sigma(X_{i_1},\ldots,X_{i_{j-1}}).
\]
Define
\[
J_\pi:=\sum_jJ_{i_j,\mathcal G_j},
\qquad
S_\pi:=\sum_jS_{i_j,\mathcal G_j}.
\tag{5.1}
\]
By telescoping the marginal identity (2.2),
\[
\boxed{
\lambda J_\pi+S_\pi=\mathcal Q_r(R)=D+S^*.
}
\tag{5.2}
\]
Thus the **combined coarsening/tangent bank is exactly invariant under coordinate order**.

This is stronger than merely saying every chain has nonnegative increments. Reordering the spectral coordinates can trade `Psi`-Jensen gain against tangent defect, but it cannot change their combined total.

We can split the Jensen term further. Since `Psi=h_2+j`, define
\[
L_\pi:=\sum_j
\left[
\mathbb E j(\bar Q_{i_j,\mathcal G_j})
-\mathbb E j(Q_{i_j})
\right]\ge0.
\tag{5.3}
\]
Concavity of `j` gives nonnegativity. The entropy part telescopes exactly:
\[
\sum_j
\left[
H(X_{i_j}\mid\mathcal G_j)
-H(X_{i_j}\mid X_{-i_j})
\right]
=H-B=D.
\tag{5.4}
\]
Therefore
\[
J_\pi=D+L_\pi.
\tag{5.5}
\]
Substitute into (5.2):
\[
\boxed{
\lambda L_\pi+S_\pi
=S^*+(1-\lambda)D.
}
\tag{5.6}
\]
Again the right side is independent of the ordering.

### Quantitative sequential stability

The inherited tangent theorem gives the dimension-free scalar curvature
\[
G_r(q)\ge c_r(q-\tau)^2,
\qquad c_r>0.
\]
Let
\[
V_\pi:=\sum_{j,\text{ coarse cells }A}
\bar y_A(\bar q_A-\tau)^2.
\tag{5.7}
\]
Then `S_pi>=c_r V_pi`, so (5.6) yields, **for every permutation**,
\[
\boxed{
V_\pi
\le {S^*+(1-\lambda)D\over c_r},
}
\tag{5.8}
\]
\[
\boxed{
L_\pi
\le {S^*+(1-\lambda)D\over\lambda}.
}
\tag{5.9}
\]

Thus small full tangent defect plus small dual total correlation forces **all fixed spectral prediction orders simultaneously** to stay close, in upper-mass weighted `L^2`, to the scalar endpoint posterior `tau`, while also forcing small accumulated `j`-coarsening gain.

This is the cleanest current bridge to APPROACH 11: an ordering-only spectral predictor cannot make the combined bank disappear. A successful decision-tree argument must exploit the fact that *physical restrictions change the function and its spectral law branch by branch*, or must introduce a nonmodular potential that genuinely refunds one of the conserved quantities. Merely sorting the root spectral coordinates by influence does not change (5.2) or (5.6).

This is **not** a no-go theorem for the owner's influence-greedy physical restriction tree; branch-adaptive physical descendants are different laws. The statement is only about coordinate chains inside one fixed hard-core spectral law.

---

## 6. A calibrated hard-core resource floor

The exact full value can also be written
\[
\mathcal Q_r(R)
=(r-b)I-\lambda C.
\tag{6.1}
\]
The universal singleton recombination estimate gives
\[
C=\sum_i\Delta_iH-H
\le {2\over\ln2}I.
\tag{6.2}
\]
Therefore
\[
\boxed{
\mathcal Q_r(R)
\ge
\left[r-b(r)-{2\lambda(r)\over\ln2}\right]I.
}
\tag{6.3}
\]
Equation (6.3) is exact as a formula; its bracket should only be called useful where it is known positive.

At the currently inherited unrestricted lower-bound calibration
\[
r_0=6.521845710923046575,
\]
the already-used scalar functions give the numerical calibration
\[
\tau(r_0)\approx0.1740316570325050,
\]
\[
b(r_0)\approx3.8317449446243725,
\qquad
\lambda(r_0)\approx0.8738359862443951,
\]
so
\[
r_0-b(r_0)-{2\lambda(r_0)\over\ln2}
\approx0.1687430784884635.
\tag{6.4}
\]
The decimal in (6.4) is **calibration only**, not an interval-certified theorem. The structural identities (2.1)--(6.3) do not depend on this decimal evaluation.

At the old exact arithmetic candidate `tau=1/10`, now already ruled out as a simultaneous Boolean endpoint by the top-degree theorem, the chain conservation law would force the nonzero sequential residual
\[
(1-\lambda)(r-b)I\approx0.1940829054573635\,I
\]
even when the full tangent defect vanished. This explains why exact full-posterior geometricity never meant sequential independence: support constraints reappear under coarsening as a conserved bank.

---

## 7. What changed and the next missing implication

### PROVED in this run

1. The **centered tangent polymatroid** (2.1): subtracting the exact modular criticality bank `lambda C_i` preserves both monotonicity and submodularity.
2. The stronger all-block floor (2.3).
3. Exact boundary-gap identities: `TC` and `DTC` are respectively the first-marginal and last-marginal submodularity gaps of the same centered potential; its full value is `DTC+S^*`.
4. Exact fixed-cardinality projection conservation (4.2)--(4.3): modular tangent centering leaves the Han/KL credit unchanged.
5. The integrated lower bound (4.4), and its phase/Hellinger version (4.5), with no double counting.
6. Exact order conservation (5.2) and the sharper `j`-coarsening conservation (5.6), valid for **every** spectral coordinate order.
7. Quantitative all-order sequential stability (5.8)--(5.9).

### KILLED / narrowed

- **Killed:** trying to obtain a better fixed-q Han credit by only subtracting modular functions of coordinatewise hard-core surpluses. Uniform q-subset averaging cancels such corrections exactly.
- **Killed:** hoping that merely choosing a better fixed ordering of the *root spectral coordinates* makes the combined coarsening/tangent bank smaller. Its total is order invariant.
- **Not killed:** branch-adaptive physical restriction trees, nonuniform selectors coupled to the current restricted function, and genuinely nonmodular spectral/phase/level potentials.

### Exact next target

The current universal obstruction is now concentrated in one place. A useful next theorem would construct a nonnegative **nonmodular** potential `N(U)` with a dimension-free full budget (or a free positive-left-hand-side budget) such that its fixed-q curvature or branch-adaptive physical drop subtracts from the positive recombination term `Rcal_q` without reusing `K_q`, `TC`, `DTC`, or `S^*` twice.

The fresh multi-level Fourier flux direction (`sum c_k W_k`) is structurally compatible because it is genuinely nonmodular and therefore escapes Theorem 4.1's cancellation. A second compatible target is a branch-adaptive selector for which the law itself changes after each physical restriction, escaping the fixed-law order conservation (5.2).

**Full FEI remains OPEN / NOT PROVED.**
