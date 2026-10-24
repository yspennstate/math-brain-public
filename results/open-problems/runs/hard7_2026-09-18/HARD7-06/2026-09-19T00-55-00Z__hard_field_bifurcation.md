Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** Primary metric **no movement**: `L_6 >= 0 -> L_6 >= 0`; substantive auxiliary movement: the exact unweighted hard-field cavity surrogate has **no nonzero fixed point for every integer d<=6, but at least two nonzero fixed points at d=7**; methods tried: **B4 / B6 / B20**.

# HARD7-06 run 5 — exact hard-field bifurcation at 6/7, and why the finite-warning cluster port is still too small

Status: **PARTIAL / Chang--Kolhe--Sohn k=3 sharpness conjecture remains OPEN under bounded current-literature review.**

Repository / branch: `yspennstate/math-open-problems` / `master`.

Canonical ownership remains `operations/claims/CKS-2024-RREG-HYPER2COL-K3.md`, owner `HARD7-06`. This run executes the first recovery selected in `2026-09-18T23-55-00Z__stuck1_cluster_port.md`: port the cluster/frozen-configuration architecture rather than repair the raw solution count again. The source metric still does not move, so nothing below is presented as a lower bound on the source probability.

## 1. Continuity, ownership, exclusions, and fresh source check

At run start I reread the controlling HARD7 files, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md` and `RANKING.md`, the canonical CKS claim, all preceding HARD7-06 reports, the relevant intake/ownership searches, and neighboring admission material that explicitly recognizes `CKS-2024-RREG-HYPER2COL-K3` as exclusively HARD7-06-owned. No release, collision, posted equivalent, or resolved equivalent was found.

Primary source remains Evan Chang, Neel Kolhe, Youngtak Sohn, *Upper Bounds on the 2-Colorability Threshold of Random d-Regular k-Uniform Hypergraphs for k >= 3*, APPROX/RANDOM 2024, LIPIcs 317, Article 47, DOI `10.4230/LIPIcs.APPROX/RANDOM.2024.47`, full version arXiv:2308.02075. The proceedings abstract says that locating the threshold for small fixed `k>=3` remains open and that the explicit upper threshold `d_*(k)` is conjectured sharp. For `k=3` the admitted lower-side boundary is still the uniformly random simple 6-regular 3-uniform hypergraph.

A bounded fresh web/literature refresh on 2026-09-19 checked the exact CKS title/arXiv id, `random regular NAE-SAT k=3 d=6`, and the cluster/frozen-message literature. I found no source-matching later proof of the exact `k=3,d=6` lower side. This is bounded negative evidence, not a proof of worldwide openness.

The recovery source read most closely was Danny Nam, Allan Sly, Youngtak Sohn, *One-Step Replica Symmetry Breaking of Random Regular NAE-SAT II*, CMP 405 (2024), Article 61, DOI `10.1007/s00220-023-04868-6`. Its frozen configuration uses states `{0,1,f}`; solutions coarsen to frozen configurations but coarsening is not necessarily surjective, and its cluster-size calculation requires message states carrying the structure of free trees. I also checked Allan Sly and Youngtak Sohn, *Local geometry of NAE-SAT solutions in the condensation regime*, PTRF 191 (2025), 979--1033, DOI `10.1007/s00440-024-01337-6`, whose local limit is explicitly built from an infinite spin system / 1RSB belief-propagation fixed point. These results are not small-`k=3,d=6` threshold theorems.

The general warning/survey-propagation mechanism is old CSP folklore/literature; I do **not** claim novelty for the finite hard-field recursion below. The exact `d=6` certificate is a route diagnostic for this track.

## 2. Frozen source metric

The source metric fixed at admission remains

\[
L_6:=\sup\left\{L\in[0,1]:\liminf_{n\to\infty}
\Pr(H_{n,6,3}\text{ is 2-colorable})\ge L\right\},
\]

for the uniformly random **simple** 6-regular 3-uniform hypergraph along source-admissible `n`.

No argument in this run converts the local tree calculation into a source-model probability bound. Therefore

\[
\boxed{L_6\ge0\quad\longrightarrow\quad L_6\ge0.}
\]

This is honest no movement of the frozen source quantity. The useful movement is auxiliary and is kept separate below.

## 3. First exact finite-state port: the hard-field density-evolution surrogate

The first deliberately weaker object keeps only whether a variable-to-clause cavity message is hard `0`, hard `1`, or free `f`. It throws away free-tree shape and cluster-size weights. Assume the incoming variable messages on the local tree are i.i.d. and color-symmetric, with total hard probability `x`, hence probabilities

\[
\Pr(0)=\Pr(1)=x/2,\qquad \Pr(f)=1-x.
\]

For a 3-NAE clause, the clause-to-variable message is a hard warning exactly when the other two cavity variables are both hard and equal. Thus the total warning probability is

\[
u=2(x/2)^2=x^2/2,
\]

and each of the two warning colors has probability `x^2/4`.

At a degree-`d` variable cavity there are `m=d-1` incoming clause warnings. Put

\[
A=1-\frac{x^2}{4},\qquad B=1-\frac{x^2}{2}.
\]

The event of no warning has probability `B^m`. The event that at least one warning of one color is present and none of the opposite color is present has total probability

\[
2(A^m-B^m).
\]

If contradictory two-color warning patterns are discarded and one conditions on local admissibility, the induced total hard probability is therefore

\[
\boxed{
F_d(x)=\frac{2(A^{d-1}-B^{d-1})}{2A^{d-1}-B^{d-1}}.
}
\tag{3.1}
\]

This is an exact recursion for the stated **surrogate ansatz**. It is not asserted to be the full Nam--Sly--Sohn 1RSB recursion and not asserted to characterize source-model clusters.

## 4. Complete auxiliary theorem: the integer bifurcation occurs between d=6 and d=7

### Proposition

For the map (3.1):

1. for every integer `d<=6`, the only fixed point in `[0,1]` is `x=0`;
2. for `d=7`, there are at least two nonzero fixed points, one in `(2/5,1/2)` and another in `(9/10,19/20)`.

### Proof

For fixed `x in (0,1]`, set

\[
r_d(x)=\left(\frac BA\right)^{d-1}.
\]

Here `0<B/A<1`, and

\[
F_d(x)=\frac{2(1-r_d)}{2-r_d}.
\]

The derivative of `2(1-r)/(2-r)` with respect to `r` is `-2/(2-r)^2<0`, while `r_d` strictly decreases in `d`. Hence `F_d(x)` strictly increases in `d`. It therefore suffices for the first assertion to prove `F_6(x)<x` on `(0,1]`.

For `d=6`, direct exact algebra gives

\[
\begin{aligned}
&x(2A^5-B^5)-2(A^5-B^5)\\
&\qquad=\frac{x(2-x)}{512}H(x),
\end{aligned}
\tag{4.1}
\]

where

\[
H(x)=256-512x-256x^2+832x^3+96x^4-512x^5-16x^6+142x^7+x^8-15x^9.
\]

To certify `H>0` globally rather than by sampling, elevate it to the degree-25 Bernstein basis on `[0,1]`. Its exact Bernstein coefficients are

```text
256,
5888/25,
16064/75,
110608/575,
46864/275,
1316848/8855,
5649964/44275,
25824111/240350,
95736109/1081575,
29047472/408595,
22632223/408595,
1544537/37145,
7742247/260015,
5207792/260015,
6872237/557175,
5417161/817190,
5712814/2042975,
724288/1081575,
4914/120175,
29622/44275,
60854/26565,
29296/6325,
4266/575,
1559/150,
333/25,
16.
```

Every coefficient is strictly positive. Since the degree-25 Bernstein basis functions are nonnegative and sum to one on `[0,1]`, `H(x)>0` throughout `[0,1]`. Also `2A^5-B^5>A^5>0`. Equation (4.1) therefore implies

\[
F_6(x)<x\qquad(0<x\le1).
\]

By monotonicity in `d`, `F_d(x)\le F_6(x)<x` for every integer `d<=6`, proving that `x=0` is the only fixed point there.

For `d=7`, exact rational arithmetic gives

\[
F_7(2/5)-2/5=-\frac{37669256}{1170850315}<0,
\]

\[
F_7(1/2)-1/2=\frac{96321}{15251714}>0,
\]

and

\[
F_7(9/10)-9/10=\frac{54169976315169}{9628934500050890}>0,
\]

\[
F_7(19/20)-19/20=-\frac{1192464602770178031}{67772143275429860180}<0.
\]

The denominator of (3.1) is positive on `[0,1]`, so continuity plus the intermediate value theorem gives one fixed point in each of `(2/5,1/2)` and `(9/10,19/20)`. This proves the proposition. `□`

Exact checker:

`artifacts/hard7_2026-09-18/HARD7-06/hard_field_bifurcation_exact.py`

creation commit `d195704aaca8ab22496c60ad01124115ea6a871a`.

Executed exact output:

`artifacts/hard7_2026-09-18/HARD7-06/hard_field_bifurcation_exact.out`

creation commit `de9d18eb82cab24ea7234fa9df2bf1c4f451fe24`, ending `ALL_EXACT_CHECKS_PASS`.

This certificate proves only the finite-state surrogate proposition above.

## 5. B20 exposes the missing variable: free trees carry infinitely many soft likelihood ratios

The fact that the surrogate collapses to `x=0` at `d=6` is not evidence that genuine source clusters are all-free. In the frozen-configuration formalism, coarsening is not surjective in general, and the all-free formal frozen configuration can carry free cycles; the successful large-`k` theory explicitly augments hard/free states with messages encoding free-tree structure and cluster size.

At `k=3` one can see the necessity of this extra information with an elementary exact family. Consider a free-tree path with free variables `v_1,...,v_n`; between `v_i,v_{i+1}` place a NAE clause whose third boundary variable is fixed to `0`. The clause condition becomes simply

\[
(v_i,v_{i+1})\ne(0,0).
\]

Other incident clauses can be viewed as neutral separating boundary factors for this local tree calculation. Let `a_n` be the number of extensions of this path. Then

\[
a_n=a_{n-1}+a_{n-2},\qquad a_1=2,\quad a_2=3,
\]

so

\[
\boxed{a_n=F_{n+2}}
\]

with `F_j` the Fibonacci numbers (`F_1=F_2=1`). More sharply, conditioning the root `v_1` gives

\[
Z_n(v_1=0)=F_n,
\qquad
Z_n(v_1=1)=F_{n+1},
\]

hence the exact cavity likelihood ratio is

\[
R_n=\frac{Z_n(1)}{Z_n(0)}=\frac{F_{n+1}}{F_n},
\qquad
R_{n+1}=1+\frac1{R_n}.
\]

Thus arbitrarily long free trees already generate infinitely many distinct soft cavity messages. A three-state `{0,1,f}` alphabet cannot preserve exact cluster sizes even in this simplest arity-3 free-tree family. This is not a novelty claim; it is the explicit small-`k` obstruction that tells this track what information the next port must keep.

Equivalently, if a child cavity distribution has `p=P(1)` and `q=P(1)` on the two other legs of a NAE-3 factor, the exact factor-to-root likelihood ratio is

\[
\widehat R
 =\frac{1-pq}{p+q-pq}.
\tag{5.1}
\]

Variable nodes multiply incoming likelihood ratios. So the infinite combinatorial message alphabet can at least be viewed dynamically as a distributional recursion on a **continuous projective likelihood ratio plus a log-normalization/cluster-size coordinate**. That is the concrete next reduction, rather than another hard/free scalar.

## 6. The three Section-B moves and what happened

### B4 — prove something weaker, completely

**Succeeded.** Instead of claiming the full 1RSB recursion at `k=3`, I isolated the simplest honest hard-field closure and proved its complete degree statement: no nonzero fixed point through `d=6`, at least two at `d=7`. The proof is global on `x in [0,1]`, not finite sampling.

### B6 — deform to a point / parameter that can be solved

**Succeeded as a route diagnostic.** Treating the degree `d` as the deformation parameter reveals an exact integer bifurcation between the source boundary degrees 6 and 7. This is strikingly aligned with CKS's `ceil(d_*(3))=7`, but it is **not** promoted to a threshold theorem: (3.1) is only a sufficient local surrogate model, not an equivalence with source satisfiability.

### B20 — find why the algorithm fails

**Succeeded in identifying the missing state variable.** At `d=6` the iid finite-warning closure flows only to the all-free state, precisely where cluster size is controlled by free-tree geometry that the closure deleted. The Fibonacci path family proves that exact cluster messages cannot be represented by the hard/free label alone. The next port must retain soft likelihood ratios and their normalization / `size^lambda` tilt, or equivalently the free-tree dynamic-programming data.

## 7. What has *not* been proved

No finite or asymptotic claim about `Pr(H_{n,6,3} is 2-colorable)` follows from the scalar recursion. In particular:

- `L_6` did not improve;
- the d=6/d=7 surrogate bifurcation is not asserted necessary or sufficient for hypergraph colorability;
- no finite-size simulation is used as an infinite-volume theorem;
- the all-free scalar fixed point is not asserted to correspond to a source-model solution cluster;
- no global pair variational inequality, quenched estimate, small-subgraph conditioning statement, or transfer from configuration model to the uniform simple model has been proved;
- no novelty is claimed for warning propagation, belief propagation, Fibonacci path counts, or free-tree dynamic programming.

## 8. Checkpoint for the next bounded recovery iteration

Continue the **same first Section-I recovery** (cluster/frozen architecture); do not go back to the raw overlap polynomial or another one-parameter minority profile.

The next concrete target is to replace (3.1) by a source-matched weighted free-tree recursion at exactly `(k,d)=(3,6)`:

1. carry a variable-to-factor state as a positive pair `(Z_0,Z_1)`, equivalently `(R=Z_1/Z_0, ell=log(Z_0+Z_1))`;
2. use the exact NAE-3 factor update (5.1) and the multiplicative variable update;
3. introduce the cluster-size tilt `exp(lambda ell)` / `size^lambda` in the cavity law rather than discarding normalization;
4. derive a closed distributional fixed-point equation for a tractable first topology class (start with path / one-branch free trees, then branching trees);
5. test whether any `lambda in (0,1]` yields a nondegenerate d=6 fixed point with positive one-replica Bethe exponent before attempting a two-replica/global second moment.

If that weighted/free-tree port also fails to produce a viable d=6 candidate within the allowed recovery cycle, the next Section-I event should use the second and final recovery rather than endlessly refining this same closure. A third stuck episode requires handoff/rotation under `CONTROL.md`.

Reserve a different next method triple: **B1 / B5 / B12** (change category to the distributional operator, vary the cluster tilt `lambda`, identify the conserved/normalization quantity).

## 9. Model / scheduler capability truth

The requested `Model: GPT-6. Reasoning: maximum` remains prompt text only. The exposed scheduler surface available to these tasks provides title, prompt, schedule/timing, enabled state, but **no bindable model-family selector, no reasoning-effort selector, and no authenticated per-run duration guarantee**. This invocation actually identifies as GPT-5.6 Sol; reasoning level is not exposed and is therefore `UNVERIFIED`. Making GPT-6/maximum binding would require an authorized product/workspace/API/admin task surface that exposes persistent model and reasoning fields plus per-run attestation.

The historical P26 `You cannot modify this task` result is an authorization-context failure, not a research or ownership signal. Current root `RESULTS.md` records that a later authorized context did successfully update P26. For a future denied modification, the lawful workaround is to use the owning/otherwise-authorized task context or authorized platform/admin support; do not duplicate the schedule or bypass permissions.

## 10. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: HARD7-06
  category: HARD_OUTSIDE
  source_id: CKS-2024-RREG-HYPER2COL-K3
  claim_id: CKS-2024-RREG-HYPER2COL-K3
  status: PARTIAL
  source_metric_name: L_6
  source_metric_before: ">=0"
  source_metric_after: ">=0"
  source_metric_progress: false
  auxiliary_progress: true
  auxiliary_quantity: unweighted_hard_field_degree_bifurcation
  auxiliary_before: UNMEASURED
  auxiliary_after: "no nonzero fixed point for every integer d<=6; at least two nonzero fixed points for d=7"
  methods_attempted: [4, 6, 20]
  previous_methods: [18, 22, 30]
  stuck_recoveries_started: 1
  recovery_route: cluster_frozen_configuration_port
  checker: artifacts/hard7_2026-09-18/HARD7-06/hard_field_bifurcation_exact.py
  checker_commit: d195704aaca8ab22496c60ad01124115ea6a871a
  output: artifacts/hard7_2026-09-18/HARD7-06/hard_field_bifurcation_exact.out
  output_commit: de9d18eb82cab24ea7234fa9df2bf1c4f451fe24
  exact_checker_result: ALL_EXACT_CHECKS_PASS
  closure: false
  next_methods: [1, 5, 12]
  next_step: derive_lambda_weighted_continuous_free_tree_distributional_recursion_at_k3_d6
```

## 11. Safeguards / write set

This run writes only its own HARD7-06 artifacts and this immutable report. It does not mutate `RESULTS.md`, `POSTED.md`, `QUEUE.md`, another track's files, another claim, any scheduler, Gmail, or Drive. No closure or independent audit is requested or claimed. The artifact output was produced by executed exact rational arithmetic before archival.
