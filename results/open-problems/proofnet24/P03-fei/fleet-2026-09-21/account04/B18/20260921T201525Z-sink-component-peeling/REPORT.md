# B18 FEI proof integration — canonical sink-component survivor block and free peeling

**Run:** `20260921T201525Z-b18-fei-r13`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of full uniform-cube Friedgut--Kalai Fourier entropy--influence conjecture:** **OPEN / NOT PROVED**  
**Claim level:** universal theorem for the doubly robust near-subcube/Palm sector, plus an exact-endpoint elimination theorem. No novelty or publication-priority claim.

## 0. Fresh state and exact missing implication

This run follows the joint four-account FEI order and the account04/B18 interface: integrate mixed-curvature/near-subcube rigidity with the adaptive physical-restriction budget.

The source-exact compatible inputs used substantively are:

1. account04/B12, `20260921T201418Z-scale-separated-palm-trigger-clusters/REPORT.md` (scientific commit `002c2fe97fe9f5bef5d4ee9312037881ed67bb18`). For an epsilon-Palm-robust derivative row, `epsilon<=1/16`, it proves:
   - trigger/nontrigger pair-mass separation;
   - reciprocal robust rows have exactly the same trigger signature
     \[
       T_i=\{i\}\cup F_i;
     \]
   - after reciprocal components are contracted, every cross-component trigger increases influence by at least a factor seven, so the quotient is a DAG;
   - in the simultaneous physical near-subcube regime, each nonreciprocal escape lowers trigger codimension by at least three.

2. account01/B13, `20260921T2020Z-crossing-depth-nearsubcube/REPORT.md`. For a pivotality event of mean `p`, it proves that a near coordinate-subcube support with defining block `F` gives the genuine posterior-majority crossing
   \[
     c(F)\ge p-\mu(E\triangle Q),
   \]
   and the union/Hall form: a family of pivots can be charged simultaneously if no selected pivot lies in the union of the revealed trigger blocks. That report left exactly the combinatorial alternative: construct a substantial survivor family, or use failure to force the dense/cyclic regime into rigidity.

3. account01/B18 and account04/B14/account02/B14, the corrected-entropy critical-core ledger. With
   \[
     \mathfrak j(p)=1-h_2\!\left(\frac12+\sqrt{p(1-p)}\right),
     \qquad
     \Phi=\sum_i\mathfrak j(p_i),
     \qquad
     \mathcal F=H-\Phi,
   \]
   a median-centered `F/J`-critical core of ratio `rho` satisfies for every physical restriction block `A`
   \[
     B_A\ge \rho I_A+\rho C_A+Q_A,
     \tag{0.1}
   \]
   where
   \[
     C_A=\sum_{j\notin A}c_j(A),
     \qquad
     Q_A=G_A+R_A,
     \qquad
     R_A\ge0,
   \]
   and
   \[
     G_A=\sum_{j\notin A}
     \left[\mathfrak j(p_j)-\mathbb E_z\mathfrak j(p_j(z))\right].
     \tag{0.2}
   \]

The previous B18 near-subcube elimination theorem also gives, for a derivative support `E_i` within symmetric-difference mass `e_i` of a coordinate subcube `Q_i` with defining set `F_i`,
\[
   \mathbb E_{x_{F_i}}
   \min\!\left(
     \operatorname{Inf}_i(f_{x_{F_i}}),
     1-\operatorname{Inf}_i(f_{x_{F_i}})
   \right)
   \le e_i.
   \tag{0.3}
\]
At `e_i=0`, exposing `F_i` makes coordinate `i` irrelevant or a pure character on every branch.

The missing implication attacked here is the nonreuse selector: the B13 union theorem needs selected pivots outside the union of all selected trigger blocks. The robust trigger graph now supplies such a family canonically.

---

## 1. Robust trigger components

Let `R_rob` be a collection of coordinates for which both of the following hold.

**Palm robustness.** Row `i` is epsilon-Palm-robust, `epsilon<=1/16`, with trigger set `F_i` in the sense of the account04/B12 theorem.

**Physical near-subcube support.** For
\[
   E_i=\{y:D_i f(y)\ne0\},
   \qquad p_i=\mu(E_i)=\operatorname{Inf}_i(f),
\]
there is a coordinate subcube
\[
   Q_i=\{y_{F_i}=a_i\}
\]
with the same defining coordinate set `F_i` and
\[
   e_i:=\mu(E_i\triangle Q_i).
   \tag{1.1}
\]
The exact endpoint is `e_i=0`; the useful quantitative regime below is `e_i<=p_i/16`.

Join robust rows `i,k` when the trigger relation is reciprocal:
\[
   k\in F_i,\qquad i\in F_k.
\]
By account04/B12 trigger locking, each connected reciprocal component `C` has one exact signature `T_C` satisfying
\[
   T_C=\{i\}\cup F_i\qquad(i\in C).
   \tag{1.2}
\]

Contract these reciprocal components. A directed edge `C -> D` exists if some row in `C` triggers some robust row in `D`. The scale-escape theorem makes this quotient a DAG.

Let `SINK` be its sink components. Choose one arbitrary representative `r_C in C` from every sink and define
\[
   R:=\{r_C:C\in SINK\},
   \qquad
   A:=\bigcup_{r\in R}F_r.
   \tag{1.3}
\]

---

## 2. PROVED: the sink frontier is a canonical Hall survivor family

### Theorem B18-SINK-SURVIVOR-01

With `R,A` as in (1.3),
\[
   \boxed{R\cap A=\varnothing.}
   \tag{2.1}
\]

Moreover, for every sink component `C` with representative `r_C`,
\[
   \boxed{C\setminus\{r_C\}\subseteq F_{r_C}\subseteq A.}
   \tag{2.2}
\]

Thus one physical block restriction on `A` simultaneously:

1. keeps exactly one chosen pivot from every robust sink component alive;
2. physically removes every other robust row in every sink component;
3. satisfies the no-pivot-in-revealed-union hypothesis required by the B13 union/Hall theorem.

### Proof

A representative never belongs to its own trigger set, so only cross-sink collisions could violate (2.1). Suppose representatives `r_C,r_D` of distinct sink components satisfy
\[
   r_D\in F_{r_C}.
\]
Both are robust rows, so this is a cross-component trigger edge `C -> D`, contradicting that `C` is a sink. Hence no selected representative lies in any selected trigger block and (2.1) follows.

For (2.2), trigger locking gives one common signature `T_C`. For any `k in C`, `k != r_C`,
\[
   k\in T_C=\{r_C\}\cup F_{r_C}.
\]
Since `k != r_C`, necessarily `k in F_{r_C}`. QED.

### Significance

The survivor-family existence problem left open in account01/B13 is therefore solved **for the entire sink frontier of the robust quotient DAG**. No matching, random selection, bounded-incidence hypothesis, or pairwise information summation is required.

This is not yet a global FEI selector because nonrobust coordinates and the cost of repeatedly peeling successive sink frontiers remain outside the theorem.

---

## 3. PROVED: larger-block refinement preserves near-free elimination

For a representative `r in R`, the previous B18 theorem (0.3) applies after revealing its own `F_r`. Since
\[
   F_r\subseteq A,
\]
revealing all of `A` is a refinement of that sigma-field.

Put
\[
   U_r(z)=\operatorname{Inf}_r(f_{A=z}),
   \qquad
   q_r(z)=\min(U_r(z),1-U_r(z)).
\]
The function `u -> min(u,1-u)` is concave. Conditional Jensen under refinement therefore gives
\[
   \boxed{\mathbb E_z q_r(z)\le e_r.}
   \tag{3.1}
\]

The raw influence is a martingale under restrictions of other coordinates:
\[
   \mathbb E_z U_r(z)=p_r.
\]
Since
\[
   q_r(z)=U_r(z)-(2U_r(z)-1)_+,
\]
the actual posterior-majority crossing of the representative under the **common union block** is
\[
   c_r(A)
   =p_r-\mathbb E_z q_r(z)
   \ge p_r-e_r.
\]
Hence
\[
   \boxed{c_r(A)\ge p_r-e_r\qquad(r\in R).}
   \tag{3.2}
\]

This is stronger than separately applying the single-row block `F_r`: all sink representatives receive their crossing refunds under one and the same physically realizable noncolliding block `A`.

---

## 4. PROVED: the same block earns an additional concavity rebate

Let
\[
   c_*=\frac{2}{\ln2}.
\]
The inherited scalar cap is
\[
   \mathfrak j(u)\le c_*\min(u,1-u)
   \qquad(0\le u\le1).
   \tag{4.1}
\]

The `r`-summand of the potential Jensen gap (0.2) therefore satisfies
\[
\begin{aligned}
   G_r(A)
   &=
   \mathfrak j(p_r)-\mathbb E_z\mathfrak j(U_r(z))\\
   &\ge
   \mathfrak j(p_r)-c_*\mathbb E_z q_r(z)\\
   &\ge
   \mathfrak j(p_r)-c_*e_r.
\end{aligned}
\]
All other summands in `G_A` are nonnegative, so
\[
   \boxed{
   G_A\ge
   \sum_{r\in R}
   \left[\mathfrak j(p_r)-c_*e_r\right].
   }
   \tag{4.2}
\]

This is the gain that is missed if one keeps only the reflected tangent coefficient `j'(p_r)c_r(A)`.

---

## 5. PROVED: canonical nonreuse sink-frontier budget

Insert (3.2) and (4.2) into the exact critical-core inequality (0.1). Since
\[
   C_A\ge\sum_{r\in R}c_r(A),
   \qquad
   Q_A\ge G_A,
\]
we obtain:

### Theorem B18-SINK-BUDGET-02

On every median-centered corrected-entropy critical core,
\[
   \boxed{
   B_A
   \ge
   \rho I_A
   +
   \sum_{r\in R}
   \left[
      \rho(p_r-e_r)
      +\mathfrak j(p_r)
      -c_*e_r
   \right].
   }
   \tag{5.1}
\]

Since
\[
   B_A=H(X_A\mid X_{A^c})
   \le H(X_A)
   \le\sum_{k\in A}h_2(p_k),
\]
the same statement has the spendable Hall form
\[
   \boxed{
   \sum_{r\in R}
   \left[
      \rho(p_r-e_r)
      +\mathfrak j(p_r)
      -c_*e_r
   \right]
   \le
   \sum_{k\in A}
   \left[h_2(p_k)-\rho p_k\right].
   }
   \tag{5.2}
\]

Every reveal-coordinate slack on the right is counted **once**, regardless of how many sink representatives use it. This is the desired nonreuse feature.

### Comparison with the previous B13 coefficient

For concave `j` with `j(0)=0`,
\[
   \frac{\mathfrak j(p)}p
\]
is decreasing. At the inherited unrestricted lower-bound calibration
\[
   C_0=6.521845710923046575,
   \qquad
   \rho_0=C_0-\frac2{\ln2}
   =3.6364556291451198\ldots,
\]
the critical singleton inequality `h_2(p)>=rho_0 p` gives
\[
   p\le\sigma=0.1966925125514116\ldots,
\]
where `h_2(sigma)/sigma=rho_0`. At this endpoint
\[
   \frac{\mathfrak j(\sigma)}{\sigma}
   =2.6595964009520916\ldots.
\]
If `e_r<=p_r/16`, each representative term in (5.2) is at least
\[
\begin{aligned}
 p_r\left[
   \frac{15}{16}\rho_0
   +\frac{\mathfrak j(\sigma)}{\sigma}
   -\frac1{16}\frac2{\ln2}
 \right]
 &=
 5.888436673164521\ldots\,p_r.
\end{aligned}
\tag{5.3}
\]
Thus the same canonical sink-frontier block obeys
\[
   \boxed{
   5.8884\sum_{r\in R}p_r
   <
   \sum_{k\in A}[h_2(p_k)-\rho_0p_k]
   }
   \tag{5.4}
\]
whenever all selected representatives have relative physical support error at most `1/16`.

The improvement over the earlier tangent-only `5.648410...` coefficient is secondary. The main advance is that `R` is no longer a hypothetical collision-free survivor family: the robust DAG supplies it deterministically as the set of sink representatives.

---

## 6. PROVED: exact endpoint removes every sink component in one step

Suppose now
\[
   e_r=0\qquad(r\in R).
\]
Then (3.1) gives
\[
   \mathbb E_z q_r(z)=0.
\]
Because each `q_r(z)>=0`,
\[
   q_r(z)=0
\]
on every branch. Thus
\[
   U_r(z)\in\{0,1\}.
\]
So after exposing `A`, each surviving representative is either irrelevant or a pure character factor. After the usual character recentering it can be removed with **zero additional squared-spectrum entropy and zero additional folded influence cost**.

Together with (2.2), all nonrepresentatives of the sink component were already physically restricted by `A`. Therefore:

### Corollary B18-EXACT-SINK-PEEL-03

For exact-subcube rows in the robust sink frontier, one common physical restriction block `A` deletes every reciprocal sink component in one step:
- all nonrepresentatives are exposed directly;
- one representative survives per component;
- each surviving representative is free after recentering.

This is the component-level version of the earlier single-row free-elimination theorem and realizes the “one activation per reciprocal trigger block” requested by the fresh account04/B12 cluster handoff.

---

## 7. Exact finite diagnostic

`check_sink_component_peeling.py` exhaustively enumerates Boolean truth tables modulo global output sign through dimension four. It detects every nonempty exact coordinate-subcube derivative support of density at most `1/2`, constructs reciprocal trigger components, contracts them, selects sink representatives, and verifies:

1. `R cap A` is empty;
2. every nonrepresentative sink-component row is exposed by its representative's trigger block;
3. after exposing the common union block `A`, every sink representative has conditional raw influence exactly `0` or `1` on every branch.

Executed results:

| n | functions | functions with exact rows | exact rows | reciprocal components | sink representatives | violations |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 0 | 0 | 0 | 0 | 0 |
| 2 | 8 | 4 | 8 | 4 | 4 | 0 |
| 3 | 128 | 104 | 192 | 128 | 128 | 0 |
| 4 | 32768 | 9280 | 13312 | 11760 | 11760 | 0 |

`TOTAL_VIOLATIONS=0`.

The universal statements above are analytic; the finite enumeration is falsification/implementation evidence only.

The checker process exited zero. The host Python environment emitted an unrelated spreadsheet-runtime warmup diagnostic on stderr after execution; it did not alter the checker result and is not mathematical evidence.

---

## 8. Classification and remaining universal gap

### PROVED

- The sink components of the reciprocal robust trigger DAG admit a **canonical collision-free survivor family**: one representative per sink.
- The union of their trigger blocks physically removes every other robust row in those sink components.
- Under physical near-subcube error `e_r`, the common union block leaves expected folded representative influence at most `e_r` and creates actual crossing at least `p_r-e_r`.
- On a corrected critical core, the same block satisfies the nonreuse budget (5.1)--(5.2), including the full concavity rebate.
- At relative error at most `1/16` and the current calibrated high-ratio scale, the sink representatives force more than `5.8884 sum p_r` of once-counted reveal slack.
- At exact support error zero, the complete sink frontier is removed in one physical restriction step plus free character cleanup.

### CONDITIONAL / SCOPE-LIMITED

The theorem applies to the **doubly robust sector** where the Palm trigger theorem and physical near-subcube approximation use the same trigger sets. It does not assert that every active derivative row is in that sector.

### OPEN

Full FEI remains open. Two nonreuse obligations remain after this run:

1. **Repeated peeling / address entropy.** After deleting one robust sink frontier, prove that the total cost of the sequence of new sink frontiers is `O(J)` rather than accumulating a logarithmic ambient or depth factor.
2. **Nonrobust remainder.** Charge rows outside the doubly robust sector using the existing depth-defect, sign/isoperimetric, curvature, erasure, or Palm-code banks with one globally telescoping budget.

The scale-separated DAG is now more than a structural description: its sink layer supplies the previously missing realizable survivor block. The next run should try to telescope (5.2) over successive sink deletions, using the factor-seven scale increase / codimension-three escape to prevent repeated address charging.
