# fleet03/B18 — nonreused robust-pair forest and a telescoping orientation ledger

**Run:** `20260922T105718Z-fleet03-B18-r11`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Path:** C — nonreused orientation selection  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Exact target and correction state

The assigned target is to select actual physical coordinate pairs or blocks so that opposite-sign derivative overlap is charged only once, while a quantitatively nontrivial part of the robust-row obstruction survives for the critical-core exclusion step. The mechanism must use the exact two-survivor co-pair endpoint, the conditional phase/crossing tax, and a source-derived realizable packing or stopping rule.

This report does **not** use the refuted implication `all-block K=4 terminal + tensor-primitive => U4=O(J)`, does not use the retired raw-`U4` route, and does not use the refuted fixed `Gamma^dagger` / quadratic repairs or the unweighted-convolution-L2 shortcut. The current Path-C object is a genuine minimum-dimensional `F/J` ratio-critical physical descendant; all-block terminality is used only as a consequence of that stronger hypothesis.

The completed partner result consumed substantively is fleet04/B18:

`proofnet24/P03-fei/fleet-2026-09-22/fleet04/B18/20260922T101158Z-robust-trigger-overlap-collapse/REPORT.md`.

Its exact contribution used here is the support/orientation split

\[
h_{ki}:=p_{ki}-2c_{k\leftarrow i}\ge0,
\qquad
\omega_{ki}=h_{ki}+4o_{ki},
\]

and the observation that robust trigger-address overlap belongs to the support-hidden bank, not to the opposite-sign bank. The partner already proved an aggregate address inequality without spending `O4`; the present report changes the mechanism again and constructs an explicit nonreused forest of physical co-pairs.

Other source-exact inputs are:

1. fleet02/B13, `20260922T075416Z-all-block-terminal-core`: on a minimum-dimensional centered critical core with ratio `rho=F/J`, every proper physical descendant has smaller ratio, hence for every physical block `A`, `Delta_A F >= rho D_A`; combined with the restriction upper bound this gives all-block criticality.
2. fleet02/B13, `20260922T093723Z-copair-terminal-tax`: for a physical pair `i,j`,
   \[
   r_{ij}=\Pr(i,j\in X)=p_{ij}/4+o_{ij},
   \]
   and revealing every other coordinate gives the exact endpoint
   \[
   E H(f_z)=2p_{ij},\quad E J(f_z)=p_{ij},\quad E F(f_z)=0.
   \]
3. fleet04/B12, `20260922T094436Z-robust-row-codimension-staircase`: for a relative-`1/16` robust derivative row `i` with trigger set `F_i`, `r_i:=|F_i|>=3`, and every trigger `k in F_i` obeys
   \[
   p_{ik}=p_{ki}\ge {7\over4}q_i.
   \]
4. fleet04/B18's critical-core scalar bound: on `rho>4`, every positive folded influence satisfies `q_k<1/6` and
   \[
   a_k:=\mathfrak j'(q_k)>16/7,
   \qquad w_k:=4+a_k>44/7.
   \]

All quantities below remain attached to original physical coordinates.

## 1. Singleton criticality forces a low-crossing trigger

Let `R` denote the relative-`1/16` robust rows. Fix `i in R`. The singleton block `A={i}` in the genuine `rho>4` critical core gives

\[
h_2(q_i)-\sum_{k\ne i} a_k c_{k\leftarrow i}
\ge
\rho\left(q_i+\sum_{k\ne i}c_{k\leftarrow i}\right).
\]

Therefore

\[
\sum_{k\ne i}(\rho+a_k)c_{k\leftarrow i}
\le h_2(q_i)-\rho q_i
\le \sigma_i,
\qquad
\sigma_i:=h_2(q_i)-4q_i.
\tag{1.1}
\]

Since `rho>4` and `a_k>16/7`,

\[
\boxed{
\sum_{k\in F_i}c_{k\leftarrow i}
< {7\over44}\sigma_i.
}
\tag{1.2}
\]

We next compare `sigma_i` with the dyadic trigger address. Robustness says the derivative support `E_i` is within relative error `1/16` of a codimension-`r_i` physical subcube of measure `2^{-r_i}`. Thus

\[
q_i\ge {16\over17}2^{-r_i}.
\tag{1.3}
\]

For every `0<q<1`,

\[
{h_2(q)\over q}
=
\log_2{1\over q}
+{1-q\over q}\log_2{1\over1-q}
\le
\log_2{1\over q}+{1\over\ln2}.
\tag{1.4}
\]

Indeed `-ln(1-q)<=q/(1-q)`. By (1.3),

\[
\log_2{1\over q_i}\le r_i+\log_2{17\over16}.
\]

The elementary bounds `ln 2>1/2` and `ln(17/16)<1/16` give

\[
\log_2{17\over16}+{1\over\ln2}< {1\over8}+2<4.
\]

Consequently

\[
\boxed{\sigma_i<r_iq_i.}
\tag{1.5}
\]

Averaging (1.2) over the `r_i` actual triggers now produces at least one trigger, denoted `k_i in F_i`, with

\[
\boxed{c_{k_i\leftarrow i}<{7\over44}q_i.}
\tag{1.6}
\]

The robust trigger theorem simultaneously gives

\[
p_{ik_i}=p_{k_i i}\ge {7\over4}q_i.
\tag{1.7}
\]

Hence the support-hidden remainder on this one physical oriented co-pair is

\[
\boxed{
h_{k_i i}
=p_{k_i i}-2c_{k_i\leftarrow i}
>{63\over44}q_i.
}
\tag{1.8}
\]

Multiplying by `w_{k_i}>44/7` gives the particularly clean critical obstruction

\[
\boxed{w_{k_i}h_{k_i i}>9q_i.}
\tag{1.9}
\]

This is the first new inference: full ratio-criticality prevents all triggers of a robust row from hiding their boundary in phase crossings. At least one trigger leaves more than `63/44` of the row influence in the genuine support-hidden channel.

## 2. Realizable packing: break only functional cycles

Choose one `k_i` satisfying (1.6) for every `i in R` and draw the directed physical edge

\[
i\longrightarrow k_i.
\]

Every robust row has out-degree exactly one. Therefore every weak component of this functional digraph contains at most one directed cycle. For each directed cycle delete exactly one arc, choosing an arc whose **tail has minimum `q_i` on that cycle**. Let `T` be the remaining undirected edge set and `R_*` the retained tails.

### Lemma 2.1 — forest packing with half-mass retention

`T` is a forest and

\[
\boxed{
Q_*:=\sum_{i\in R_*}q_i\ge {1\over2}\sum_{i\in R}q_i=: {1\over2}Q_R.
}
\tag{2.1}
\]

**Proof.** Once every directed cycle is broken, an undirected cycle would force every vertex on that cycle to use one outgoing edge along the cycle, recreating a directed cycle; hence the underlying graph is acyclic. On a directed cycle of length `ell>=2`, the deleted minimum tail has weight at most the cycle average, hence at most half the total cycle weight. Acyclic-component tails are untouched. Summing componentwise proves (2.1). QED.

No selector label or synthetic coordinate is introduced: every retained edge is one of the original physical trigger pairs.

## 3. Exact co-pair obstruction survives the packing

For an arbitrary set `E_i` of measure `q_i`, a directional boundary is at most `2q_i`. Thus every retained edge obeys

\[
{7\over4}q_i\le p_{ik_i}\le2q_i.
\tag{3.1}
\]

The exact fleet02/B13 two-survivor theorem says that if all coordinates except this physical pair are revealed, the expected two-bit endpoint has

\[
E H=2p_{ik_i},\qquad E J=p_{ik_i},\qquad E F=0.
\tag{3.2}
\]

Consequently the selected family retains the quantitative endpoint mass

\[
\boxed{
{7\over4}Q_*\le\sum_{i\in R_*}p_{ik_i}\le2Q_*;
}
\tag{3.3}
\]

in particular

\[
\boxed{
\sum_{i\in R_*} E H(\hbox{two-survivor endpoint}_{i,k_i})
\ge {7\over2}Q_*
\ge {7\over4}Q_R.
}
\tag{3.4}
\]

Equation (3.4) is a diagnostic sum of exact physical endpoints, not a claim that all co-pair complements can be queried simultaneously. The realizable object used for nonreuse is the forest `T`; no incompatible restrictions are silently summed.

Define the selected support-hidden bank

\[
H_T:=\sum_{i\in R_*}w_{k_i}h_{k_i i}.
\tag{3.5}
\]

By (1.9) and (2.1),

\[
\boxed{
H_T>9Q_*\ge {9\over2}Q_R.
}
\tag{3.6}
\]

Thus cycle breaking does not erase the robust obstruction: at least half the robust influence remains, and it carries a support-hidden weighted obstruction exceeding `9/2` times the original robust mass.

There is also a dimension-free upper ledger. We next prove the universal scalar bound

\[
0\le \mathfrak j'(q)\le {2\over\ln2},\qquad 0\le q\le1/2.
\tag{3.7}
\]

With `x=sqrt(q/(1-q))`, the source derivative formula is

\[
\mathfrak j'(q)
={2(1-x^2)\over x\ln2}\operatorname{artanh}x.
\]

Since

\[
\operatorname{artanh}x
=\int_0^x{dt\over1-t^2}
\le {x\over1-x^2},
\]

(3.7) follows, including the endpoint by continuity. Set

\[
W:=4+{2\over\ln2}=6.8853900817\ldots .
\tag{3.8}
\]

Because `h_{k_i i}<=p_{ik_i}<=2q_i`,

\[
\boxed{H_T\le2WQ_*\le2WJ.}
\tag{3.9}
\]

The selected support-hidden obstruction is therefore simultaneously nonvanishing and dimension-free; it is not the refuted raw `H4`/`U4` sum.

## 4. Telescoping signed ledger for opposite-sign overlap

For a retained physical pair `e={i,k_i}`, fleet02/B13 gives

\[
r_e:=\Pr(i,k_i\in X)={p_e\over4}+o_e,
\qquad 0\le o_e\le r_e.
\tag{4.1}
\]

Define the selected opposite-sign bank with the original row weight

\[
O_T:=4\sum_{i\in R_*}w_{k_i}o_{ik_i}.
\tag{4.2}
\]

The forest property produces an exact signed telescoping identity. For each realization of the spectral random set `X`, let `T[X]` be the subforest induced on `X cap V(T)`, and let `kappa_T(X)` be its number of nonempty connected components. Since every induced subgraph of a forest is a forest,

\[
|E(T[X])|=|X\cap V(T)|-\kappa_T(X).
\tag{4.3}
\]

Taking expectations gives

\[
\boxed{
\sum_{e\in T}r_e
=
\sum_{v\in V(T)}q_v
- E\,\kappa_T(X)
\le J.
}
\tag{4.4}
\]

The negative component term is a genuine retained credit; it has not been replaced by zero in the exact identity. Combining (3.7), (4.1), and (4.4),

\[
\boxed{
O_T
\le4W\left[
\sum_{v\in V(T)}q_v-E\kappa_T(X)
\right]
\le4WJ.
}
\tag{4.5}
\]

This is the requested **nonreused orientation payment**. Every physical pair is present at most once, and the tensor-style quadratic reuse that made raw `U4/J` diverge is impossible on the selected forest.

For completeness, the selected exact hidden ledger is

\[
U_T^{\rm sel}
:=\sum_{i\in R_*}w_{k_i}
\left[p_{k_i i}-2c_{k_i\leftarrow i}+4o_{k_i i}\right]
=H_T+O_T.
\tag{4.6}
\]

Equations (3.9) and (4.5) give the finite bound

\[
\boxed{
U_T^{\rm sel}\le6WJ
=6\left(4+{2\over\ln2}\right)J
<41.313J.
}
\tag{4.7}
\]

At the same time (3.6) preserves a lower obstruction `H_T>(9/2)Q_R`. Thus the selector pays the opposite-sign overlap once without washing away the robust-row signal needed by the next criticality step.

The visible phase/crossing portion is not double-spent. Since `w_k=4+a_k<rho+a_k`, the selected crossings are a subset of the source critical-core crossing bank:

\[
\sum_{i\in R_*}w_{k_i}c_{k_i\leftarrow i}
\le
\sum_k(\rho+a_k)R_k
\le \mathcal P-\operatorname{DTC}(X).
\tag{4.8}
\]

Thus the signed decomposition `p-2c+4o` keeps the negative crossing refund, the forest ledger keeps the negative component credit, and neither is reused.

## 5. Analytic stress test: exact tensors

Use the source family

\[
F_m=\phi_6^{\otimes m},\qquad N=6m,
\]

where `phi_6` is the six-bit one-point defect and every coordinate has

\[
q_0={1\over32}.
\]

For a pair in different tensor factors, fleet02/B13 proves exactly

\[
p_{ij}=0,\qquad c_{i\leftarrow j}=0,
\qquad o_{ij}=r_{ij}=q_0^2={1\over1024}.
\tag{5.1}
\]

Those cross-factor pairs are precisely the source of the quadratic raw-orientation bank, but they **cannot be trigger edges** of a robust row because a trigger must satisfy `p_{ij}>=7q_i/4>0`. Hence the selector never chooses the spurious tensor-orientation edges.

Even if one deliberately feeds an arbitrary cross-factor forest into the orientation ledger, it remains dimension-free. Since a forest on `N` vertices has at most `N-1` edges,

\[
{O_T\over J}
\le
{4w(q_0)q_0^2(N-1)\over Nq_0}
={w(q_0)\over8}\left(1-{1\over N}\right)
<{W\over8}<0.861.
\tag{5.2}
\]

By contrast, the raw all-pairs `U4/J` of the source family grows linearly in `m`. The forest ledger removes exactly that repeated-spending pathology rather than trying to bound it.

Within each six-bit factor, each derivative support is an exact codimension-five subcube. Its five genuine trigger directions have

\[
p=2q_0={1\over16},\qquad c=0,
\]

so the robust selected edges are factor-local and carry real support obstruction rather than cross-factor tensor orientation.

## 6. Analytic stress test: one-point tensor surgery

Let `G_m` be the fleet02/B13 one-point surgery at `v=1^N`, `N=6m>=18`, which destroys every nontrivial tensor factorization while preserving all-block `K=4` terminality. Write

\[
\delta_N:=2^{1-N}.
\]

The source proves every coordinate influence becomes

\[
q_i=q_0+\delta_N,
\tag{6.1}
\]

and a fixed cross-factor pair statistic changes on only one two-face, hence by at most `2^{2-N}`. In particular

\[
p_{ij}\le2^{2-N},
\qquad
o_{ij}\le q_0^2+2^{2-N}
\tag{6.2}
\]

for cross-factor pairs. Thus for an arbitrary cross-factor forest,

\[
H_T\le W(N-1)2^{2-N}=o(J),
\tag{6.3}
\]

and

\[
O_T\le4W(N-1)(q_0^2+2^{2-N})=O(J),
\qquad
{O_T\over J}\to{W\over8}.
\tag{6.4}
\]

More strongly, the actual robust rows remain close to the **same codimension-five physical subcubes**. The surgery adds one exceptional quotient point to a row support, with relative error

\[
{\delta_N\over q_0}=2^{6-N}\le2^{-12}<1/16.
\tag{6.5}
\]

Hence the source robust trigger set remains the five within-factor coordinates. The selector therefore continues to choose factor-local trigger pairs and ignores the `Theta(m^2)` population of cross-factor orientation pairs. The surgery family that refutes raw `U4=O(J)` consequently does **not** refute the forest selector: its selected orientation ledger is `O(J)` and its selected support obstruction remains of order `J`.

This stress test is a mechanism test, not a claim that `F_m` or `G_m` is a genuine `rho>4` ratio-critical core; the source explicitly uses them to separate terminality/primitivity from full criticality.

## 7. What is proved, and the exact remaining implication

### PROVED — `C-NONREUSED-ROBUST-FOREST-v1`

On every centered minimum-dimensional `F/J` critical core with `rho>4`, for the relative-`1/16` robust rows there is a source-derived forest of original physical trigger pairs such that:

\[
Q_*\ge Q_R/2,
\]

\[
{7\over4}Q_*\le\sum_{e\in T}p_e\le2Q_*,
\]

\[
H_T>9Q_*\ge{9\over2}Q_R,
\qquad H_T\le2WJ,
\]

and

\[
O_T\le4W\left[\sum_{v\in V(T)}q_v-E\kappa_T(X)\right]\le4WJ,
\]

with `W=4+2/ln2`. Every selected pair is physical and occurs once. The exact two-survivor endpoint applies to every selected pair, the singleton criticality phase tax produces the low-crossing trigger, and the signed crossing/component credits are retained rather than discarded.

### NOT PROVED

This is **not** yet a contradiction to `rho>4` and therefore is not full FEI closure. The next unpaid implication is now narrower and is the handoff to fleet01/B19:

> Use the selected forest, not raw `H4` or `U4`, to turn the surviving support-hidden endpoint mass `H_T>(9/2)Q_R` into one affordable physical restriction/block contradiction to ratio-criticality, or prove that `Q_R` is universally small and pass the residual to the nonrobust-row branch.

The useful structural point for B19 is that the opposite-sign overlap is no longer the obstacle on the selected family: it has the exact dimension-free forest payment (4.5). Any remaining failure of the selected-pair criticality contradiction must therefore lie in converting the **support-hidden** co-pair endpoint mass into a single realizable block/restriction debit, or in the nonrobust rows.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.
