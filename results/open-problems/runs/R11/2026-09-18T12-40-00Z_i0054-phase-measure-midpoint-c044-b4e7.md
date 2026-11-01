Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested in prompt text, but the exposed scheduler/runtime has no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run routing telemetry, so GPT-6 / maximum is not verified or claimed. Metric movement: `43 -> 44` distinct nontrivial discrete model classes with complete author-side proofs of the frozen CTCS(infinity) limit. Actual section-B moves: **#6, #15, #21**.

# R11 / I0054 — U023 phase-measure/collision decomposition and C044 midpoint-quadrature paintbox

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Track: R11, CLOSABLE OUTSIDE.  
Source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, Open Problem 18.  
Source-level campaign status after this run: **PARTIAL, not CLOSED**.  
New author-side claims: `R11-I0054-U023 = PROVED_AUTHOR_SIDE`; `R11-I0054-C044 = PROVED_AUTHOR_SIDE under frozen equivalence`.

## 1. Continuity, source, ownership, prior attempts, neighboring work

I continued from the newest complete R11 report

`runs/R11/2026-09-18T11-40-15Z_i0054-weighted-collision-u022-c043-8c2f.md`

rather than restarting. That report proved U022/C043, moved the fixed metric `42 -> 43`, and prescribed moves `#6/#15/#21`; those are the moves actually used here.

Before new research I reread or recovered the controlling repository state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/I0054.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- the newest R11 report and the nearby C028/C029/C033/C040--C043 reports needed for frozen-equivalence comparisons;
- the current P13 successor report. Its old Aldous--Janson I0051 clade problem remains retired and was not reassigned here;
- repository searches for I0054 prior work and for present-package audit IDs.

The canonical claim still records R11 as provisional exclusive owner and still says `PENDING_ADMISSION, not READY`. The old planar self-avoiding-walk route remains retired with immutable history. I did not edit shared roots or another track's files.

I also rechecked the primary source from the v3 PDF rather than relying on the experimental HTML numbering. The PDF is dated 17 April 2025 / arXiv v3 posted 18 April 2025. Printed page 58 says:

> Open Problem 18. Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately asks whether the source's subordinator approximation can arise in another discrete tree model. The v3 abstract and Part III, arXiv:2412.09655, formalize CTCS(infinity) via consistent exchangeable partition restrictions. I therefore retain R11's frozen strong target: for every fixed `[k]`, convergence of the **complete partition-valued cadlag path** in Skorokhod `J_1`, consistently in `k`, hence convergence in the projective finite-restriction path topology.

Fresh dated literature searches on 2026-09-18 again found:
- Aldous--Janson Part III, arXiv:2412.09655;
- Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320, using homogeneous fragmentations/subordinators for beta-splitting asymptotics;
- Heng Ma, arXiv:2609.14329, which explicitly resolves Aldous--Janson Open Problem 4 on discrete-time height.

Searches combining `midpoint`, `quadrature`, `paintbox`, `fragmentation`, `beta-splitting`, `CTCS`, and `different discrete models` did not locate the construction below or an announced resolution of exact Open Problem 18. This is bounded negative evidence only, **not** a novelty certificate. Hausdorff moment determinacy, polynomial quadrature, paintboxes, and Poisson fragmentation clocks are classical ingredients and are not claimed as new.

A current repository search still does not return a qualifying present-package `P26-AUDIT-R11-I0054` end-to-end PASS or a second complete OTHER-track end-to-end PASS. Search hits are prior R11 reports saying such audits were absent, not new audit verdicts.

## 2. Idea before code and the three new-method moves

U022 fixed the harmonic phase grid and varied the dependence between blocks. The next question is orthogonal:

**Which finite phase measures generate the CTCS beta kernel at all?**

The useful answer is sharper than another construction.

- **#6 — deform to a solvable point.** Replace the harmonic grid by an arbitrary finite set of paintbox biases and rates. The apparently singular CTCS dislocation weights become an ordinary finite measure after one exact transformation.
- **#15 — break symmetry on purpose.** I deliberately allowed an asymmetric phase list. This fails to create new unordered-tree information: complementing every color sends `x` to `1-x` but leaves the unordered split unchanged. The failure exposes the exact `Z_2` orbit measure that the tree actually sees.
- **#21 — ask who else has this shape.** The transformed criterion is precisely a compact Hausdorff moment / quadrature problem on `[0,1]`. This gives an iff theorem rather than a one-sided approximation.

Only after this theorem and C044 were obtained did I write the exact checker.

## 3. General finite phase-paintbox model

For each `N`, let `A_N` be a finite phase set. Phase `a` has

\[
x_{N,a}\in(0,1),\qquad w_{N,a}>0.
\]

In the independent-block version, every current nonsingleton block has independent Poisson clocks, phase `a` ringing at rate `w_{N,a}`. At such a mark, give the leaves of that block iid Bernoulli(`x_{N,a}`) colors. If both colors occur, replace the block by the two nonempty color classes; otherwise do nothing. New child blocks receive fresh independent clocks.

The model is exchangeable in leaf labels. Its restriction to `[k]` is itself exactly Markov: a mark that separates hidden labels but not the visible labels simply transfers the visible block to one child; by Poisson memorylessness/fresh clocks the future visible law is unchanged.

For a particular **unordered** split support with child sizes `i,j`, the exact rate is

\[
q_N(i,j)
=
\sum_{a\in A_N}w_{N,a}
\left[
x_{N,a}^{\,i}(1-x_{N,a})^j
+x_{N,a}^{\,j}(1-x_{N,a})^i
\right].
\tag{3.1}
\]

## 4. Move #15: the exact color-complement quotient

Define the transformed finite measure

\[
\boxed{
\rho_N
=
\sum_{a\in A_N}
w_{N,a}x_{N,a}(1-x_{N,a})
\bigl(\delta_{x_{N,a}}+\delta_{1-x_{N,a}}\bigr).
}
\tag{4.1}
\]

Then (3.1) becomes exactly

\[
\boxed{
q_N(i,j)
=
\int_0^1
x^{\,i-1}(1-x)^{j-1}\,\rho_N(dx).
}
\tag{4.2}
\]

This is not merely an asymptotic representation. It is the exact quotient of the raw phase mechanism by the `Z_2` action exchanging the two Bernoulli colors. Replacing any phase `(x,w)` by `(1-x,w)` leaves the entire unordered partition process unchanged. Thus an asymmetric raw phase list is invisible beyond the symmetrized transformed measure (4.1).

For CTCS the corresponding particular-support rate is

\[
B(i,j)=\int_0^1x^{i-1}(1-x)^{j-1}\,dx.
\tag{4.3}
\]

So the singular-looking paintbox intensity has been reduced to ordinary quadrature against Lebesgue measure.

## 5. U023(A): sharp independent-block phase-measure criterion

**Theorem U023(A).** For the independent-block finite phase-paintbox family above, started from the one-block partition,

\[
\boxed{
\Pi_N\Longrightarrow\Pi_{\operatorname{CTCS}(\infty)}
\text{ in the frozen projective }J_1\text{ topology}
\iff
\rho_N\Rightarrow dx
\text{ weakly on }[0,1].
}
\tag{5.1}
\]

### Sufficiency

Assume `rho_N => dx`. For every fixed `i,j`, the integrand in (4.2) is continuous on the compact interval, hence

\[
q_N(i,j)\to B(i,j).
\tag{5.2}
\]

Fix `k`. The partition set `P_k` is finite. Every off-diagonal generator entry is either zero or one of finitely many rates (4.2), and the diagonal is the negative row sum. Therefore

\[
Q_N^{(k)}\to Q_{\rm CTCS}^{(k)}
\tag{5.3}
\]

entrywise, hence in every finite matrix norm.

Couple holding times at a state `pi` by one `E~Exp(1)` and set
`H_N=E/lambda_N(pi)`, `H=E/lambda(pi)`. Couple the next jump by one uniform random variable using the convergent finite jump distributions. A fragmentation of `[k]` makes at most `k-1` proper jumps, so under this coupling all jump destinations eventually agree and all corresponding jump times converge almost surely. Thus

\[
\boxed{
\Pi_N^{[k]}\Longrightarrow\Pi_{\rm CTCS}^{[k]}
\quad\text{in }J_1
}
\tag{5.4}
\]

for every fixed `k`.

The restrictions are compatible. In the summable projective metric

\[
d_{\rm proj}(\omega,\eta)
=
\sum_{k\ge2}2^{-k}
(1\wedge d_{J_1,k}(\omega^{[k]},\eta^{[k]})),
\]

first take `N -> infinity` at fixed `K` and then `K -> infinity`; the deterministic tail is at most `2^{-K+1}`. Hence the full projective convergence in (5.1).

### Necessity

Assume instead the frozen projective `J_1` convergence to CTCS. Consider the process on `[m+1]` started from its root block. In this pure fragmentation chain, the first holding time is exponential and the first-jump destination probabilities determine each root transition rate. Since the CTCS first jump time is almost surely positive and has no ties, `J_1` convergence implies convergence of the first holding time and first destination law. Therefore, for every `m>=1`,

\[
q_N(m,1)\to B(m,1)=\frac1m.
\tag{5.5}
\]

By (4.2),

\[
q_N(m,1)
=
\int_0^1x^{m-1}\rho_N(dx).
\tag{5.6}
\]

Taking `m=1` gives total mass `rho_N([0,1])->1`; taking all `m` gives convergence of every moment to the Lebesgue moment `1/m`. On the compact interval `[0,1]`, polynomials are uniformly dense in the continuous functions, equivalently the Hausdorff moment problem is determinate. Thus

\[
\rho_N\Rightarrow dx.
\tag{5.7}
\]

This proves necessity and U023(A).

## 6. U023(B): quadrature and common-shock suppression are independent axes

The same transformation combines cleanly with U022.

Consider instead a systematic microcycle of duration `tau_N -> 0`. At each phase `a`, blocks are assigned deterministic channels by `h_{N,a}`; blocks in the same channel share one Bernoulli gate of probability `tau_N w_{N,a}`, while their leaf colorings are independent conditional on that gate. Assume gate legality `tau_N w_{N,a}<=1`.

Let

\[
r_2(x)=2x(1-x)
\]

and define, for fixed `k`,

\[
\boxed{
D_N(k)=
\max_{1\le u<v\le k}
\sum_{a\in A_N}
w_{N,a}r_2(x_{N,a})^2
\mathbf 1\{h_{N,a}(u)=h_{N,a}(v)\}.
}
\tag{6.1}
\]

Then the argument of U022, with the harmonic identity removed, gives

\[
\boxed{
\Pi_N\Longrightarrow\Pi_{\operatorname{CTCS}(\infty)}
\iff
\left[
\rho_N\Rightarrow dx
\ \text{and}\
D_N(k)\to0\ \forall k
\right].
}
\tag{6.2}
\]

Here is the complete reduction.

For one block, the channel map never enters, so (4.2) still gives the exact first-order generator. Thus `rho_N=>dx` gives the CTCS one-block generator and, conversely, root convergence forces the Hausdorff moments as above.

For two visible blocks of sizes `m,n` on a common channel, their same-gate split rate is bounded using

\[
1-x^m-(1-x)^m\le m\,r_2(x)
\tag{6.3}
\]

(and its `n` analogue). Hence on `[k]` the row discrepancy from the independent-block first-order generator is at most

\[
C_kD_N(k).
\tag{6.4}
\]

If both conditions in (6.2) hold, generator convergence follows. Since the limiting fixed-`k` total exit rate is finite, the one-macrocycle total visible hazard is `O_k(tau_N)`; two distinct successful gates in one macrocycle have probability `O_k(tau_N^2)`. The one-cycle kernel is therefore

\[
C_N^{(k)}
=
I+\tau_NQ_N^{(k)}+O_k(\tau_N^2),
\tag{6.5}
\]

and the usual finite-state Euler coupling plus moving a unique intra-cycle jump by at most `tau_N` gives `J_1` convergence.

Conversely, if `D_N(k)` stays above `epsilon>0` along a subsequence, choose two visible pair blocks with the offending minima. Their direct same-gate simultaneous split has rate at least `epsilon`, while CTCS has zero generator mass for a direct simultaneous jump of two different blocks because its block clocks are independent and continuous. The two-pair state is reachable from the root with positive CTCS probability. A short-time two-point distribution therefore contradicts root-start path convergence.

Thus the **quadrature error** (`rho_N-dx`) and the **dependence error** (`D_N`) are genuinely separate structural axes.

## 7. C044 — midpoint-quadrature paintbox hierarchy

Move #6 now chooses a particularly clean point in U023(A).

For each `N>=2`, use `N` phases

\[
x_{N,r}=\frac{2r-1}{2N},
\qquad 1\le r\le N,
\tag{7.1}
\]

with independent blockwise Poisson phase clocks of rates

\[
\boxed{
w_{N,r}
=
\frac{1}{2N\,x_{N,r}(1-x_{N,r})}
=
\frac{2N}{(2r-1)(2N-2r+1)}.
}
\tag{7.2}
\]

At a phase-`r` mark, split by iid Bernoulli(`x_{N,r}`) colors as in Section 3.

Because the midpoint grid is reflection-invariant,

\[
\boxed{
\rho_N
=
\frac1N\sum_{r=1}^N
\delta_{(2r-1)/(2N)}.
}
\tag{7.3}
\]

Indeed each raw phase contributes mass `1/(2N)` at `x` and `1-x`, and reflection permutes the midpoint grid.

Therefore for every specified `i|j` support,

\[
\boxed{
q_{N,044}(i,j)
=
\frac1N\sum_{r=1}^N
x_{N,r}^{\,i-1}(1-x_{N,r})^{j-1}.
}
\tag{7.4}
\]

This is exactly the midpoint quadrature rule for the beta integral. Hence

\[
q_{N,044}(i,j)\to
\int_0^1x^{i-1}(1-x)^{j-1}dx
=B(i,j).
\tag{7.5}
\]

Equation (7.3) also gives `rho_N=>dx` directly, so U023(A) proves the required full limit:

\[
\boxed{
\Pi_{N,044}^{[k]}
\Longrightarrow
\Pi_{\rm CTCS}^{[k]}
\quad\text{in Skorokhod }J_1
\quad\forall k,
}
\tag{7.6}
\]

and

\[
\boxed{
\Pi_{N,044}
\Longrightarrow
\Pi_{\operatorname{CTCS}(\infty)}
}
\tag{7.7}
\]

in the frozen projective finite-restriction topology.

This is the complete partition-valued genealogy convergence, not a root-shape or one-time marginal limit.

## 8. Exact finite identities and frozen non-equivalence

The midpoint rule gives several closed identities:

\[
\boxed{q_{N,044}(1,1)=1},
\qquad
\boxed{q_{N,044}(2,1)=\frac12},
\tag{8.1}
\]

\[
\boxed{
q_{N,044}(2,2)
=
\frac{2N^2+1}{12N^2}
=
\frac16+\frac1{12N^2},
}
\tag{8.2}
\]

and

\[
\boxed{
q_{N,044}(1,3)
=
\frac{4N^2-1}{12N^2}.
}
\tag{8.3}
\]

At `N=4`,

\[
q_{044}(1,3)=\frac{21}{64},
\qquad
q_{044}(2,2)=\frac{11}{64},
\]

so the time-rescaling-invariant ratio of first-root particular-support probabilities is

\[
\boxed{
R_{044}=
\frac{q_{044}(1,3)}{q_{044}(2,2)}
=
\frac{21}{11}.
}
\tag{8.4}
\]

The checker compares `21/11` exactly with the archived binary root-ratio witnesses through C029:

\[
2,\frac75,\frac{2699}{1365},\frac{2273}{1153},
\frac{61381}{43765},
\frac{166094447739}{85563797248},
\frac{33}{17},\frac53,\frac{597}{359},\frac{18}{11},
\frac95,\frac54,\frac{459}{224},
\]

and they are all different. The C030 witness is `>2`, while `21/11<2`; the C032/C033 witnesses are `>11/5`, while `21/11<2<11/5`. The rotor/systematic-scan classes have an atomic periodic microstep timing law, whereas C044 is a homogeneous continuous-time independent-block chain with exponential holding times; deterministic positive time rescaling does not change atomic versus continuous timing.

The nearest homogeneous independent paintbox class is C001, the harmonic-grid model. At `N=4` its exact rates are

\[
q_{001}(1,1)=\frac34,
\qquad
q_{001}(2,2)=\frac5{32},
\]

hence

\[
\frac{q_{001}(2,2)}{q_{001}(1,1)}=\frac5{24},
\qquad
\frac{q_{044}(2,2)}{q_{044}(1,1)}=\frac{11}{64},
\tag{8.5}
\]

which are unequal. This ratio is unchanged by global time rescaling and label relabeling.

C034--C039 have archived finite multifurcation/root-degree witnesses, while C044 is binary at every jump. C040/C042/C043 have a positive direct simultaneous multi-block transition in an appropriate finite state; C044, with independent continuous block clocks, has such direct simultaneous-jump rate exactly zero. These support distinctions survive relabeling and positive global time scaling.

Thus C044 is a new class under the frozen convention:

\[
\boxed{\texttt{R11-I0054-C044 = PROVED\_AUTHOR\_SIDE}.}
\tag{8.6}
\]

## 9. Exact self-check

Only after the route above had produced U023/C044 did I write and execute the exact-arithmetic self-check

`artifacts/R11/2026-09-18T12-40-00Z_c044_midpoint_phase_measure_checker.py`.

It performs **9,042 exact `fractions.Fraction` assertions** and verifies:

1. the transformed phase measure (7.3) exactly through `N=80`;
2. the exact identity (4.2)/(7.4) for all `1<=i,j<=6` over the tested range;
3. the closed identities (8.1)--(8.3) through `N=200`;
4. positive and uniformly controlled finite-block exit rates;
5. the exact `N=4` witness
   \[
   q_{11}=1,\quad q_{13}=21/64,\quad q_{22}=11/64,\quad R=21/11;
   \]
6. the C001 harmonic comparison `5/24 != 11/64`;
7. exact noncollision with every archived binary witness through C029 and the later C030/C032/C033 brackets.

The executed output is archived at

`artifacts/R11/2026-09-18T12-40-00Z_c044_midpoint_phase_measure_checker.out`

and ends

`ALL_EXACT_CHECKS_PASS`.

Local payload hashes recorded in that output:
- checker SHA-256 `b5a565297e8a863048ba109c66237050229ff4dd1820120ae723c6796f4c35b0`;
- stdout SHA-256 `32e6e39a729a7c1b33e24b3a7037a6e51c3dfba9bf45fe40d58bdfaf372782c5`.

This is a **self-check**, not an independent audit.

## 10. Status, audits, model-control limitation

Stable author-side claims from this run are

\[
\boxed{\texttt{R11-I0054-U023 = PROVED\_AUTHOR\_SIDE}},
\qquad
\boxed{\texttt{R11-I0054-C044 = PROVED\_AUTHOR\_SIDE}},
\]

and the frozen metric moves

\[
\boxed{43\to44}.
\]

I am **not** calling Aldous--Janson Open Problem 18 closed. The source-level campaign remains `PARTIAL` because:

1. `operations/claims/I0054.md` remains `PENDING_ADMISSION, not READY`;
2. no qualifying present-package P26 end-to-end PASS was recovered;
3. no second independent OTHER-track current-package PASS was recovered;
4. the source phrase “superficially different” intentionally requires external/source-intent judgment;
5. the literature search is bounded and does not certify publication novelty.

The scheduler/model-control limitation is unchanged in substance. The exposed automation update interface supports prompt/title, schedule, enablement, and timing mode, but not a model-family selector, reasoning-effort selector, guaranteed-duration field, or authenticated per-run routing receipt. `RESULTS.md` now records that P26's **full prompt update later succeeded in another authorized context**, so the old P26 denial is not a universal current failure. However, all 20 R-series IDs were denied edits in the later reconciled context. A task that returns `You cannot modify this task` must be changed from its authorized owning context or through platform support; duplicating or bypassing it is not a valid workaround. Making GPT-6/maximum enforceable requires product/workspace/platform support for persistent model/reasoning fields plus per-run routing attestation.

No scheduler modification, email, Drive write, public posting, workflow execution, permission change, purchase, or peer-file edit was attempted.

## 11. Next route

The next nonrepeating section-B moves are **#4, #17, #27**.

The strongest next question is no longer another ordinary Riemann grid. U023 says the problem is quadrature. The natural sharp test is therefore:

- replace midpoint quadrature by an `m_N`-node Gaussian/Jacobi-type quadrature for Lebesgue measure;
- exploit exact polynomial integration to make the CTCS split generator **exact**, not asymptotic, on every block size up to a growing threshold;
- determine the minimal phase support needed to match all CTCS rates on `[k]`;
- use the resulting finite-law support/timing invariant to decide whether this yields a genuinely new class rather than a reparametrization.

That route would turn the Hausdorff-moment observation into a finite optimality theorem instead of just class 45 by cosmetic variation.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R11
  lane: CLOSABLE_OUTSIDE
  intake: I0054
  source: "Aldous--Janson arXiv:2303.02529v3, Open Problem 18"
  source_status: PARTIAL
  canonical_claim_status: PENDING_ADMISSION
  metric_name: "number of distinct nontrivial discrete model classes with complete author-side CTCS(infinity) projective-J1 proofs under frozen equivalence"
  metric_before: 43
  metric_after: 44
  movement: "+1"
  unchanged_count_after: 0
  methods_used: [6, 15, 21]
  new_claims:
    - "R11-I0054-U023 = PROVED_AUTHOR_SIDE"
    - "R11-I0054-C044 = PROVED_AUTHOR_SIDE under frozen equivalence"
  checker:
    path: "artifacts/R11/2026-09-18T12-40-00Z_c044_midpoint_phase_measure_checker.py"
    assertions: 9042
    result: ALL_EXACT_CHECKS_PASS
  checker_output: "artifacts/R11/2026-09-18T12-40-00Z_c044_midpoint_phase_measure_checker.out"
  closure: false
  next_methods: [4, 17, 27]
  next_target: "minimal-support exact quadrature / exact finite-restriction CTCS generator theorem"
```
