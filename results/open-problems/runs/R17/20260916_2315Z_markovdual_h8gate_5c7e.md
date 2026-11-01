Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime and scheduler schema provide no model selector or reasoning-effort selector, so I do not claim otherwise. **NO MOVEMENT: certified interval width `0.033614007999972411... -> 0.033614007999972411...`. Section-B moves tried: 6 (deform to a solvable point), 12 (find what is conserved), 30 (one scale / one direction at a time).**

Problem/source: Václav Chvátal and David Sankoff, “Longest common subsequences of two random sequences,” *Journal of Applied Probability* 12(2) (1975), 306–315, DOI `10.2307/3212444`. Target: determine exactly
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid fair binary strings.

Status of the outside problem: **OPEN**. Status of R17: **PARTIAL**.

Run ID: `20260916_2315Z_markovdual_h8gate_5c7e`.

# 1. Fixed metric — no movement

The retained rigorous interval is
\[
\boxed{
0.792665992\le \gamma_2\le
\frac{173228576586520}{209648759000007}
}
\]
with
\[
U=0.82627999999997241118894483984578\ldots
\]
and
\[
\boxed{
U-L=
\frac{880891882776315417257}
{26206094875000875000000}
=0.03361400799997241118894483984578\ldots .
}
\]

Nothing in this run supplies a new deterministic endpoint, so the fixed metric does not move.

# 2. Required continuity and current-status pass

I read the current repository controls before doing new work rather than restarting from chat memory:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- newest own report `runs/R17/20260916_2214Z_archivara_audit_8c2f.md`;
- newest R18 closure report `runs/R18/2026-09-16_19-25-22_UTC__R18__i0080-closed-packaged-6e4a.md`;
- intake/history search for P0283, the exact binary Chvátal–Sankoff problem.

The current campaign/posted material does not mark this source target settled or posted by another owner. P0283 remains the historical intake entry for the exact binary LCS constant.

Dated external/status checks on 2026-09-16/17 again found the exact constant unresolved. The relevant current sources checked were:

- Alexander Tiskin, arXiv:`2212.01582` v2, whose current revision still describes the exact binary coefficient as unresolved and records the removal of earlier incorrect stochastic-process claims;
- Heineman--Miller--Reichman--Salls--Sárközy--Soiffer, arXiv:`2407.10925` / ISIT 2025, which states the improved binary lower endpoint `0.792665992` while treating the exact constants as open;
- Lember--Sova, DOI `10.1111/sjos.70086`, first published 18 July 2026, which treats a pairwise-Markov strongly-related-string model and explicitly distinguishes it from the iid-independent Chvátal–Sankoff setting;
- Lueker, JACM 56(3) (2009), DOI `10.1145/1516512.1516519`, and the surviving UCI code/Javadocs for the published upper machine.

A bounded negative search is not a proof of worldwide openness. No accessible later source located in this pass claims an exact value or a rigorously narrower ordinary iid binary interval than the endpoints retained above.

# 3. Move 6 — deform the buffered-beam idea to the smallest solvable finite-state control

The preceding run proposed a bounded revealed-buffer beam as a way to convert heuristic beam search into an exact lower-bound algorithm. I first deformed that idea to the simpler one-frontier finite-buffer control before trying to build a much larger beam state.

Fix a lookahead length `h`. A state contains the next `h` revealed bits of each iid stream. An admissible action either

1. chooses equal symbols at positions `(i,j)` in the two buffers, emits that symbol, irrevocably consumes the two prefixes through `(i,j)`, and refills the consumed positions with fresh iid bits; or
2. if desired, irrevocably discards a revealed prefix from one side and refills it.

Every emitted word is pathwise a common subsequence. The state space is finite and every transition probability is dyadic.

At `h=1` this deformation is exactly solvable: when the leading bits match, emit and consume both; when they differ, discard from one side until a match appears. The familiar renewal calculation gives rate `2/3`. More importantly, an exploratory relative-value iteration for this finite-buffer control landed on the same initial numerical sequence printed in the authors' public `Binary-KiwiSotoAlgorithm.py` prototype. I do **not** promote that floating diagnostic to a theorem or endpoint here; it is recorded only as route identification.

The public Kiwi--Soto prototype itself records the first ten values beginning

`0.666666..., 0.727272..., 0.747922..., 0.758576..., ...`

and the current optimized C++ implementation is explicitly described by the authors as a binary feasible-triplet/Kiwi--Soto lower-bound computation. Thus the one-frontier finite-buffer deformation is not a genuinely new source-level route: it is, at minimum, numerically and structurally aligned with the already-exploited Kiwi--Soto/Lueker lower machinery.

**Outcome of move 6:** useful negative result. A bounded buffer alone is not enough novelty. Any finite-state lower attack worth pursuing must enlarge the state beyond a single committed frontier — e.g. a genuinely multi-frontier delayed-commitment beam — or it merely recreates the existing lower-bound sequence at enormous state cost.

No checker was created for this diagnostic because no finite numerical value from the exploratory solver is being claimed as a new mathematical result.

# 4. Move 12 — a conserved Bellman potential gives an exact compiler for finite-state beam policies

The useful piece of the buffered-beam idea is not the particular one-frontier state. It is the existence of an exact finite-state **dual certificate**. The following compiler makes the required certificate explicit.

## R17-C017 — finite-state revealed-tail Bellman certificate

**Status: PROVED as a standard average-reward/occupation-measure compiler; novelty is not claimed.** The Bellman-potential mechanism is standard finite-state average-reward Markov-process duality. The LCS-specific point is the pathwise subsequence interpretation and the use of two separate consumption coordinates.

Consider an admissible finite-state policy on two infinite iid fair binary streams. Its state contains every revealed symbol that the policy may use again. At transition `t`, starting in state `S_t=s`, it

- emits `R_t>=0` new common-subsequence symbols;
- irrevocably consumes `C^X_t>=0` and `C^Y_t>=0` positions from the two streams;
- retains only information represented in the next finite state and obtains every newly exposed symbol from the still-fresh iid tails.

Assume concatenating the emitted segments is pathwise a common subsequence of the consumed prefixes. Let
\[
P(s,s')=\Pr(S_{t+1}=s'\mid S_t=s),
\]
\[
r(s)=\mathbf E[R_t\mid S_t=s],\quad
x(s)=\mathbf E[C^X_t\mid S_t=s],\quad
y(s)=\mathbf E[C^Y_t\mid S_t=s].
\]

Suppose there are a number `c>=0` and bounded potentials `f_X,f_Y` on the finite state space such that for every state `s`,
\[
\boxed{
r(s)-c\,x(s)+(Pf_X)(s)-f_X(s)\ge0,
}
\tag{C017-X}
\]
\[
\boxed{
r(s)-c\,y(s)+(Pf_Y)(s)-f_Y(s)\ge0.
}
\tag{C017-Y}
\]
Assume also that every closed recurrent class reachable from the initial distribution has positive mean consumption on at least one side, and that the policy cannot emit indefinitely without consuming fresh input.

Then
\[
\boxed{\gamma_2\ge c.}
\tag{C017}
\]

### Proof

Fix any closed recurrent class `C` reached by the finite Markov chain and let `pi` be a stationary distribution on that class. Multiply (C017-X) by `pi(s)` and sum over `s`. Since `pi P=pi`, the potential terms cancel exactly:
\[
\sum_s\pi(s)r(s)
\ge
c\sum_s\pi(s)x(s).
\]
Doing the same with (C017-Y) gives
\[
\sum_s\pi(s)r(s)
\ge
c\sum_s\pi(s)y(s).
\]
Write these stationary means as `rho`, `mu_X`, and `mu_Y`. Then
\[
\rho\ge c\max\{\mu_X,\mu_Y\}.
\tag{1}
\]

A finite Markov chain enters a closed recurrent class after a finite transient almost surely. The strong law for additive functionals of a finite recurrent Markov chain gives, along the subsequent trajectory,
\[
\frac1T\sum_{t<T}R_t\to\rho,
\qquad
\frac1T\sum_{t<T}C^X_t\to\mu_X,
\qquad
\frac1T\sum_{t<T}C^Y_t\to\mu_Y.
\]
The finite transient does not affect these limits.

Let `N(n)` be the largest number of completed transitions for which the cumulative consumptions on **both** streams do not exceed `n`. By the preceding limits and the nondegeneracy assumption,
\[
\frac{N(n)}n\to\frac1{\max\{\mu_X,\mu_Y\}}.
\]
Therefore the length `A_n` emitted by the policy inside the two length-`n` prefixes satisfies
\[
\liminf_{n\to\infty}\frac{A_n}{n}
\ge
\frac{\rho}{\max\{\mu_X,\mu_Y\}}
\ge c
\]
almost surely by (1).

Pathwise, `A_n <= LCS(X_1^n,Y_1^n)`. Hence
\[
\liminf_{n\to\infty}\frac{LCS(X_1^n,Y_1^n)}n\ge c
\]
for the lower algorithm's output comparison. Since the ratios are bounded by `1`, Fatou's lemma gives
\[
\liminf_{n\to\infty}\frac{\mathbf E LCS(X_1^n,Y_1^n)}n\ge c.
\]
The Chvátal--Sankoff limit exists, so `gamma_2>=c`. This proves C017.

### Exact-certification consequence

For a bounded revealed-buffer policy, `P,r,x,y` are rational — dyadic when only fair fresh bits are exposed. If `c,f_X,f_Y` are rational, (C017-X)--(C017-Y) are a finite list of exact rational inequalities. Therefore a future numerical search can be **derandomized into a deterministic lower-bound certificate** simply by rounding a candidate Bellman potential to rationals and checking every state.

The metric-moving target is now explicit:
\[
\boxed{
\text{construct one admissible finite multi-frontier policy and exact potentials with }
c>0.792665992.
}
\tag{O018}
\]

C015 from the preceding run is recovered as the regenerative/single-cycle special case. C017 is stronger because successive cycles/states need not be independent; all retained dependence is carried by the finite Markov state.

A quick literature check on average-reward Markov decision processes found the expected occupation-measure/Bellman-duality framework, e.g. Gong--Wang (L4DC 2020) explicitly describes a Bellman saddle-point/duality formulation for finite-state average-reward MDPs. I therefore make **no novelty claim** for the potential argument itself.

**Outcome of move 12:** successful compiler, no endpoint yet. It converts the previous vague instruction “compute an exact beam expectation” into the finite exact feasibility problem (O018).

# 5. Move 30 — isolate one upper-bound scale: the exact public h=8 artifact gate

I separately localized the Lueker upper route to **one history scale, h=8**, instead of proposing another transfer family.

The current UCI `upper/` directory is live and lists only

- `DPTable.java`,
- `Dump.java`,
- `DumpMatrix.java`,
- `GenFn.java`,
- `State.java`,
- `StateTable.java`,
- `Test.java`,
- and `javadoc/`.

There is no precomputed `eigen8.bin` and no posted `data/` transition table in that directory.

The surviving Javadocs make the intended pipeline unusually concrete:

1. `StateTable` constructs the reachable accepting states; its command-line entry point is `java StateTable <history>` and writes the transition data.
2. `GenFn` iterates the nonnegative matrix at a chosen `z` and its `dumpEigen(z)` method writes the current eigenvector approximation to `eigen<h>.bin`.
3. The code overview explains why this eigenvector file is useful: the represented `z` and vector can be treated as exact floating-point data and independently checked as a positive supersolution without rerunning the eigensolver.

A bounded search for `eigen8.bin`, mirrors of the h=8 vector, and a precomputed h=8 transition file found no accessible copy. That is **not** proof that no copy exists anywhere; it identifies the exact missing public artifact in the sources available to this run.

This sharpens the upper-side obstruction. Reconstructing the *definitions* is no longer the issue: the Java/Javadoc source gives the machine generator. The missing high-value object is the actual h=8 positive witness (or a fresh regenerated replacement) with enough certified numerical margin to improve substantially on C010.

I did not execute external Java. The current deployment forbids unreviewed external scripts, and raw `.java` retrieval from the UCI server is rejected by the available reader even though the directory/Javadocs are accessible. No access restriction was bypassed.

**Outcome of move 30:** no endpoint movement, but the next upper computation is reduced to a concrete reproducibility artifact: regenerate and independently certify the h=8 witness rather than invent another transfer-matrix variant.

# 6. Lower-source reproducibility status tightened, but endpoint retained

The previous run found that the published nine-digit Heineman lower endpoint is not reconstructible from the checked-in template parameters alone. This run inspected the public repository/history more narrowly:

- the current `Binary-RAMOnly.cpp` and `Binary-ExtnMem.cpp` both have checked-in `FIXED_POINT_SCALE=25000000`, while comments recommend `2^24` for length at least 19;
- the public root contains source code and supporting documents but no length-21 production-output file;
- the initial archived `Binary-ExtnMem.cpp` copy already used the same `25000000` template scale;
- the available `Binary-ExtnMem.cpp` history consists of the initial copy and a later code update, not a preserved length-21 production configuration/log;
- the source prints the bound to nine decimals from the integer `min_change` through the documented fixed-point formula.

Thus the exact pair `(production FIXED_POINT_SCALE, final min_change)` remains unavailable in the public artifacts I located. This is a reproducibility gap, **not** a refutation of the paper. I therefore continue to retain `0.792665992` as the source-certified lower endpoint rather than weakening or strengthening it by inference.

# 7. R18 audit duty

No fresh R18 mathematical package requires an R17 audit. The newest R18 report is already internally labeled

`PROVED / AUDIT-COMPLETE / PACKAGED`

for Hasebe--Ueda--Wang Problem 4.11, and records both the distinct R17 end-to-end audit and the P26 end-to-end audit. Re-auditing it here would violate the new-methods-first instruction without adding a new independent closure gate.

# 8. Model / scheduler interface status

The model-control situation is still unchanged. The scheduler interface exposed here permits prompt/title, schedule/timing, enablement, and timing mode. It exposes **no model field and no reasoning-effort field**. Consequently `GPT-6 / maximum` is request text only; it is not an enforceable or verified runtime setting in this interface.

Changing that requires product/API support for model/reasoning fields or an owning account/workspace/admin surface that exposes them.

The repository policy records native modification failures such as `You cannot modify this task` for P26 in one context. A later authorized context was able to update P26, so the denial is ownership/context-specific. The legitimate workaround remains the owning account/workspace or platform support — not bypassing access controls and not creating a duplicate schedule.

No scheduler modification was attempted in this run.

# 9. Stagnation / required next run

After C010 reset the streak, the next two reports (`2114Z` and `2214Z`) did not move the fixed interval. This report is a third consecutive no-movement run.

Therefore the next R17 invocation is **mandatory stuck/thinking episode 1** under `operations/NEW_METHODS_2026-09-16.md`. It must make no new theorem claim. It must write the five-part stuck diagnosis and choose exactly one recovery.

The two genuinely metric-relevant blockers are now:

\[
\boxed{
\text{LOWER: find an exact finite-state C017 certificate with }c>0.792665992,
}
\]
or
\[
\boxed{
\text{UPPER: regenerate/certify a Lueker h=8 positive witness strong enough to lower }U.
}
\]

The stuck run should choose **one**, not split effort between both.

# 10. Claim ledger

- `R17-C001` rectangular four-cycle parity obstruction: retained PROVED.
- `R17-C002/C003` fixed-k recent-boundary nonclosure/error-floor family: retained PROVED at stated scope.
- `R17-C004/C005` block composition and annealed-MGF upper compiler: retained PROVED.
- `R17-C006/C007` bounded-span packing/truncation hierarchy: retained PROVED.
- `R17-C008` exact `q_{m,1}=1/m` renewal special case: retained PROVED.
- `R17-C009/C010` source-dependent rigorous sharpening of Lueker's published h=8 error envelope: retained PROVED at stated source-dependent scope.
- `R17-X014` finite Monte Carlo confidence is not a deterministic endpoint certificate: retained PROVED logical obstruction.
- `R17-C015` regenerative fresh-tail lower-bound compiler: retained PROVED.
- **`R17-C017` finite-state revealed-tail Bellman certificate: PROVED as a standard compiler; novelty not claimed.**
- Exact value of `gamma_2`: OPEN.

No exact checker was added this run. C017 has no finite numerical core; its full proof is on the page. The numerical finite-buffer experiment was deliberately left as a route diagnostic and is not promoted to a claim. This follows the owner's instruction not to manufacture a checker merely to prove that a non-moving run executed.

# 11. Structured ledger_delta

```yaml
ledger_delta:
  track: R17
  source:
    authors: "Václav Chvátal; David Sankoff"
    year: 1975
    title: "Longest common subsequences of two random sequences"
    target: "exact binary Chvátal-Sankoff constant gamma_2"
  metric:
    name: "width U-L of the best rigorously certified interval containing gamma_2"
    before_exact: "880891882776315417257/26206094875000875000000"
    before_decimal: "0.03361400799997241118894483984578..."
    after_exact: "880891882776315417257/26206094875000875000000"
    after_decimal: "0.03361400799997241118894483984578..."
    movement: false
  endpoints:
    lower: "0.792665992"
    upper: "173228576586520/209648759000007"
  status: PARTIAL
  source_problem_status: OPEN
  unchanged_count: 3
  methods_this_run: [6, 12, 30]
  new_claims:
    - "R17-C017 finite-state revealed-tail Bellman lower-bound compiler, PROVED; standard mechanism, novelty not claimed"
  exact_evidence:
    - "No new finite numerical certificate this run; full C017 proof is in this immutable report"
  audit_ids:
    - "No fresh R18 package requiring a new audit"
  blockers:
    - "LOWER: exact finite-state C017 certificate with c > 0.792665992"
    - "UPPER: regenerated/certified Lueker h=8 positive witness with materially stronger margin"
  next_protocol_state: "mandatory stuck/thinking episode 1; no new claims"
```

No Gmail, Drive, email, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-file edit was made.