Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding selector is exposed.**

# Scope correction to the H0008 cycle-balance / exit-induction artifact

This is an immutable correction to

`research7_2026-09-17/R7-07/admissions/2026-09-19T181310Z__H0008_cycle_balance_exit_stationarity_and_branch_renewal.md`

created at commit `0835b16fbf6bf52b405b1155e3406835ade1f558`.

The original artifact correctly proves the conditional multinomial law, the transmission-cycle reduction of Altok's reversible criterion, the automatic two-type reversible slice, the exact pipe resolvent/branch-reset identities, and the two-spine hazard identity.  It **overstates the hypotheses of Theorem 2.4 and Corollary 2.5** at one point: ordinary transience alone does not guarantee that the last-exit set has positive intensity under a stationary multitype environment.

## 1. Exact issue

Lyons--Pemantle--Peres induce the stationary path shift on the set `Exit` of last exit points.  In their one-type setting this set has positive stationary measure; indeed their Proposition 8.2 identifies that measure with the speed.

For a general multitype tree, transience need not imply positive speed.  A classical deterministic two-type example is a branching tree decorated by arbitrarily long one-dimensional pipes: simple random walk is transient but can have zero speed.  Therefore the implication

`transience => P(Exit)>0`

used implicitly in Step 4 of Theorem 2.4 is not valid at the stated generality.

## 2. Corrected theorem

### Theorem C.1 (cycle-balanced exit-stationarity, corrected scope)

Retain assumptions 1--3 of Theorem 2.4 and local finiteness/transience.  Add the explicit **positive-exit-intensity** hypothesis

\[
\boxed{
(\mathrm{SRW}\times\mu_A^\infty)(\mathrm{Exit})>0.
}
\tag{C.1}
\]

Equivalently for the LPP induced construction, the stationary reversible walk must be ballistic in the relevant Busemann/radial coordinate, or one must independently prove a finite-mean physical last-exit roof.

Under (C.1), the proof of Theorem 2.4 is valid: inducing the stationary two-sided path shift on `Exit` produces a stationary harmonic-descendant law `mu_H`, and the branching positivity/backbone argument promotes the resulting absolute continuity to equivalence and ergodicity under the same irreducible nonsingular conditions.

### Proof

Steps 1--3 of Theorem 2.4 are unchanged.  Assumption (C.1) makes `Exit` a genuine positive-measure section, so the normalized conditional law and its induced first-return transformation are well defined.  The induced transformation is measure preserving by the standard induced-map theorem.  The tree argument identifying successive last exits with consecutive vertices of the future harmonic ray is unchanged, hence the forward-tree projection is harmonic-stationary.  The absolute-continuity and backbone-ergodicity steps do not use the size of `Exit` beyond its positivity.  QED.

## 3. Corrected dimension-drop consequence

Corollary 2.5 must likewise be read with (C.1) included.  Therefore the rigorous conclusion of the B1 route in this run is:

\[
\boxed{
\text{cycle balance} + \text{positive exit intensity}
\Longrightarrow
\text{equivalent ergodic HARM-stationary law},
}
\]

and, with the already proved R14 PF--KL/rigidity inputs and their moment hypotheses,

\[
\boxed{
\dim_H\mathrm{HARM}<\log\rho(M)
}
\]

outside the deterministic regular no-thinning equality class.

Cycle balance **alone** is not claimed to prove dimension drop.

## 4. What remains valid without correction

The following results from the parent artifact are unaffected:

1. conditional on total transmitted offspring `d`, child types are multinomial with
   \[
   \pi_{ij}=q_jp_{ij}/t_i;
   \]
2. Altok reversibility is equivalent to transmission cycle balance
   \[
   \prod p_{i_si_{s+1}}=\prod p_{i_{s+1}i_s};
   \]
3. every irreducible two-type positive-transmission H0008 law satisfies this reversible criterion;
4. the R14 two-type diagnostic has
   \[
   \Pi=\begin{pmatrix}1/2&1/2\\2/3&1/3\end{pmatrix},\qquad
   \mu=(4/7,3/7);
   \]
5. the exact compactified pipe iterate
   \[
   (\widetilde T_0^nx)_j(u)
   =\left(\frac{u-1}{u+n-1}\right)^2
   \sum_i(J^n)_{ij}x_i(u+n);
   \]
6. the pipe Green resolvent bound and exact branch-renewal factorization;
7. the genuine-branch reset tail;
8. the exact two-spine Feynman--Kac hazard identity and the branch lower bound
   \[
   -\log s\ge \frac{2bR}{(b+R)^2}.
   \]

## 5. Revised mathematical frontier

The cycle-balanced category has now isolated a **new, much smaller scalar/probabilistic gate**:

\[
\boxed{
\text{prove }(\mathrm{SRW}\times\mu_A^\infty)(\mathrm{Exit})>0
\text{ for the H0008 source law,}
}
\tag{C.2}
\]

or construct an exit-stationary law by a zero-intensity/Palm method that does not require positive-speed induction.

This is not the same as the earlier exit-**level** regeneration roof.  Positive `Exit` intensity is a physical-time/Busemann-speed assertion.  The existing R7-07 facts `rho(J)<1`, superexponential small-conductance tails, finite source variance, and exponential exact-pipe tails are natural ingredients, but this correction does **not** claim they have already been assembled into a proof of (C.2).

The bounded literature check on 2026-09-19 is consistent with this caution: multitype trees can exhibit zero-speed transient walks, so no generic transience-to-ballisticity implication may be inserted silently.

Status remains **PENDING_ADMISSION / PARTIAL FEASIBILITY / novelty UNVERIFIED**.
