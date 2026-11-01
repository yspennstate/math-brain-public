Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 25000000/291978907 -> 250000000/2919788131`. Methods tried: B6 / B17 / B27.**

# HARD7-03 — the four-step moment is exact after sign-atlas closure

Status: **PARTIAL**. Seppäläinen Problem 4 remains open in its full source scope.

## 1. Continuity, ownership, required reads, and source status

This run resumes the active exclusive claim

`operations/claims/D0025.md`, owner `HARD7-03`, canonical source key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`.

At run start I re-read the required control surfaces

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`,
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`,
- the D0025 claim and repository-wide indexed D0025/intake trail,
- the newest own checkpoint `20260919T2123Z__d0025-central-double-outrunner-local-minimum.md`,
- and the newest visible neighboring HARD7-02 and HARD7-04 commits.

HARD7-02 is still on its distinct non-Hermitian heavy-tail/correlation problem and HARD7-04 on its distinct growing-random-graph/MST line. No canonical collision, release, posted equivalent, or ownership change involving D0025 was found. The very large intake JSONL files are not safely renderable byte-for-byte in one connector response; I used the indexed canonical D0025 trail rather than falsely claiming a literal full dump. Shared root ledgers were not edited; the reconciler delta is recorded below.

The primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1–15, Problem 4, arXiv `math/9906194`, DOI `10.11606/resimeusp.v4i1.74889`. The exact residual tracked here is the finite-capacity `K>=2` iid site-rate disordered nearest-neighbor exclusion plateau question, excluding the now-known ordinary `K=1` site-disorder case.

A fresh bounded literature refresh during this run used the exact source title together with `disordered K-exclusion plateau site disorder flux K=2`, `partial exclusion site disorder asymmetric flux random environment`, and `K-exclusion process random environment asymmetric hydrodynamics`. It recovered the primary source, the broad random-environment hydrodynamics line, and Ayyer–Misra's 2024 exactly-solvable `(q,t)` K-exclusion process, which is a different deformed-rate model. No theorem closing the exact `K>=2` iid site-rate residual surfaced. This remains **OPEN_BY_BOUNDED_SEARCH**, not a claim of exhaustive worldwide openness.

The frozen test case is unchanged:

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

The stable tracked quantity is a rigorous lower bound `L <= Delta_2(Q)`.

## 2. Before/after metric

The preceding checkpoint proved

\[
G_1(0)\le A_{\rm old}:=\frac{291978907}{10^8}=2.91978907
\]

and hence, using the previously proved D0025 transfer,

\[
L_{\rm old}=\frac1{4A_{\rm old}}
=\frac{25000000}{291978907}
=0.085622623417793\ldots .
\]

This run proves

\[
\boxed{G_1(0)\le A_{\rm new}:=\frac{2919788131}{10^9}=2.919788131}
\]

and therefore

\[
\boxed{
L_{\rm new}=\frac1{4A_{\rm new}}
=\frac{250000000}{2919788131}
=0.085622650953916\ldots .}
\]

The exact gain is

\[
\boxed{
L_{\rm new}-L_{\rm old}
=\frac{23475000000}{852516547160952817}>0.}
\]

The numerical movement is small because the important advance of this run is structural: the entire four-layer moment calculation is now exact rather than an upper envelope.

## 3. Idea before code and counterexample-first attack

Before constructing the new checker I committed and read back

`artifacts/hard7_2026-09-18/HARD7-03/20260919T2227Z__idea-four-step-exactness.md`

at commit `00d244f63c7b81bdec2b08d626443f3bda66b65f`.

The preceding run used B5/B19/B24. This run uses the different triple **B6/B17/B27**.

- **B6 — deform to a point already solved.** The purported residual non-local-minimum sectors are deformed to the zero-gap boundary where the kernel has a closed elementary Laplace form. Outcome: successful; the old baseline is exactly equal to the kernel there.
- **B17 — look for the same numbers somewhere else.** The coefficient appearing in those boundary sectors is the same phase-type difference `theta(1/(2-theta)-1/(3-theta))=theta/((2-theta)(3-theta))=kappa`. Outcome: successful; this identifies why no correction exists on the nonpositive zero-gap sectors.
- **B27 — swap the quantifiers.** Instead of asking for a stronger uniform pointwise lower bound for all gaps, partition the complete strict order space first and apply the exact formula on each chamber. Outcome: successful; the `5!` atlas has no uncovered chamber.

The counterexample-first search was exact: enumerate every strict ordering of `(Y_-2,...,Y_2)` and ask whether its predecessor-gap sign pattern belongs neither to a previously exact branch nor to an exact baseline branch. No such ordering exists.

## 4. The exact fresh-layer kernel on the only apparently missing sectors

Retain

\[
a=1-\theta,\qquad b=2-\theta,\qquad c=3-\theta,
\qquad \kappa=\frac{\theta}{bc}.
\]

The fresh-layer triple-slack kernel is

\[
\Phi_\theta(u,v)
=\theta\int_0^\infty e^{\theta t}(1-e^{-t})
 e^{-(t-u)_+-(t-v)_+}\,dt.
\tag{4.1}
\]

If `u<=0` and `v=0`, then for all `t>=0`, `(t-u)_+=t-u` and `(t-v)_+=t`. Therefore

\[
\begin{aligned}
\Phi_\theta(u,0)
&=\theta e^u\int_0^\infty
\left(e^{-(2-\theta)t}-e^{-(3-\theta)t}\right)dt\\
&=\theta e^u\left(\frac1b-\frac1c\right)
=\kappa e^u.
\end{aligned}
\tag{4.2}
\]

By reflection,

\[
\Phi_\theta(0,v)=\kappa e^v\qquad(v\le0),
\tag{4.3}
\]

and in particular `Phi_theta(0,0)=kappa`.

These are exactly the global baseline values already present in the inherited envelope. Hence the sign sectors `(-,0)`, `(0,-)`, and `(0,0)` contain **zero** hidden loss.

This is the B6/B17 mechanism: what looked like an omitted correlation term is actually an identity on the boundary.

## 5. B27: exhaustive sign atlas and exact branch equivalences

Let

\[
S_e=\max\{Y_z:|z-e|\le1,\ -2\le z\le2\}
\]

and at fourth-step endpoint `d` set

\[
(u_d,v_d)=(S_{d-1}-S_d,S_{d+1}-S_d).
\]

Because the five `Y` variables have continuous laws, ties among them have probability zero; structural zero gaps arise only from overlapping maxima. By reflection it is enough to inspect `d=0,1,2`.

The exact `5!` checker gives

\[
\begin{array}{c|l}
d&\text{sign-pattern counts among 120 strict orders}\\ \hline
0&(++)12,(+-)6,(+0)12,(-+)6,(-0)24,(0+)12,(0-)24,(00)24,\\
1&(+-)10,(+0)20,(-0)30,(0-)30,(00)30,\\
2&(+-)20,(+0)20,(0-)40,(00)40.
\end{array}
\tag{5.1}
\]

More importantly, the checker proves exact rank equivalences, not just counts.

### Edge `d=2`

`(+,-)` is exactly

\[
Y_0>Y_1>Y_2,
\]

the strict edge mixed-sign branch integrated exactly in the 12:21Z checkpoint. `(+ ,0)` is exactly

\[
Y_0>Y_2>Y_1,
\]

the structural edge branch integrated exactly in the 19:21Z checkpoint. The remaining `(0,-)` and `(0,0)` sectors are (4.2)–(4.3) baseline identities.

### Near edge `d=1`

Put `M=max(Y_1,Y_2)`. Then `(+,-)` is exactly

\[
Y_{-1}>Y_0>M,
\]

the 13:18Z exact interior mixed-max branch. `(+ ,0)` is exactly

\[
Y_{-1}>M>Y_0,
\]

the 20:21Z structural zero-gap branch. The remaining `(-,0),(0,-),(0,0)` sectors are exact baseline identities.

### Center `d=0`

The strict `(+,-)` sector is exactly

\[
Y_{-2}>Y_{-1}>\max(Y_0,Y_1,Y_2),
\]

and `(-,+)` is its reflection; these are precisely the 13:18Z exact central mixed-max branches.

For `(+ ,0)`, put

\[
M=\max(Y_0,Y_1),\qquad L=\max(Y_{-1},Y_2).
\]

Then the sector is exactly

\[
Y_{-2}>M>L,
\]

with `(0,+)` its reflected orientation. These are the 20:21Z exact central structural branches.

Finally `(+,+)` is exactly

\[
Y_{-2}>\max(Y_{-1},Y_0,Y_1),
\qquad
Y_2>\max(Y_{-1},Y_0,Y_1),
\]

the double-outrunner chamber completed in the 21:23Z checkpoint. The remaining `(-,0),(0,-),(0,0)` sectors are again exact baseline identities.

Therefore every one of the 360 endpoint/order pairs in the `d=0,1,2` atlas belongs to an exact branch. There is no residual triple-slack chamber.

## 6. Exact four-step moment identity

For nonnegative `x,y,z`,

\[
\max(x,y,z)=x+y+z-\min(x,y)-\min(y,z)
-(\min(x,z)-y)_+.
\tag{6.1}
\]

This deterministic identity is exact. The earlier 15:23Z and 17:21Z checkpoints made the nested edge/near-edge and nonnested center adjacent-pair moments exact. The 18:24Z checker promoted those pair formulas to a parameter-uniform four-step expression `U4_allpairs(theta)`. Sections 4–5 above now show that every branch of the only remaining triple term is also exact.

Consequently, for every `0<theta<1` for which the displayed Laplace integrals are finite (in particular throughout this calculation), the quantity obtained by adding the exact 19:21Z, 20:21Z, and 21:23Z corrections to `U4_allpairs(theta)` is not merely an upper bound: it equals the actual four-step exponential-moment sum `A_4(theta)` used by the block Chernoff argument.

As a hard consistency check, the new checker evaluates this parameterized exact identity at the previous

\[
\theta_0=\frac{57343}{100000}
\]

and reconstructs **exactly** the immutable 21:23Z rational

\[
A_4(\theta_0)
=\frac{44104948057835881726074263653049462747385972189701092886716639414717371037400000000000000000000}
{54442695413156570473578553858609910677406260157304013873650482583987300880543061947950013587}
\]

with decimal value `810.116907752835459...`.

This exact reconstruction is important: the new theorem is a closure of the existing branch decomposition, not a numerically patched surrogate.

## 7. Reoptimize only after exactness: new certified theta

Once the four-step quantity is exact, reoptimizing the Chernoff parameter is meaningful. A floating scout was used only to locate a promising rational point; it is not part of the proof. Choose exactly

\[
\theta_*:=\frac{286501}{500000}=0.573002.
\]

The checker evaluates the exact four-step moment as the rational

\[
A_4(\theta_*)=
\frac{1517204019531760324333997345977613444209419763524409954052485300429454952169394531708375000000000000000000000}
{1882210166110178548779321620940661185506706056018518381543077054007807227664534905549104515965797189135667},
\]

numerically

\[
A_4(\theta_*)=806.075775622470019\ldots .
\tag{7.1}
\]

Now set

\[
A_{\rm new}=\frac{2919788131}{10^9}.
\]

With

\[
x=4\theta_*A_{\rm new},\qquad
S_{32}(x)=\sum_{k=0}^{32}\frac{x^k}{k!},
\]

the exact rational checker proves

\[
S_{32}(x)-A_4(\theta_*)>0,
\]

with decimal margin

\[
1.651850018890679\times10^{-6}.
\tag{7.2}
\]

Since every omitted exponential-series term is positive,

\[
A_4(\theta_*)<S_{32}(x)<e^{4\theta_*A_{\rm new}}.
\]

The already proved four-block Chernoff/Borel–Cantelli argument therefore yields the new shape and plateau bounds of Section 2. This is an asymptotic theorem from exact moment identities, not a finite-size simulation.

## 8. Exact artifacts and readback

Idea-before-code:

- `artifacts/hard7_2026-09-18/HARD7-03/20260919T2227Z__idea-four-step-exactness.md`
- commit `00d244f63c7b81bdec2b08d626443f3bda66b65f`

Exact checker:

- `artifacts/hard7_2026-09-18/HARD7-03/four_step_exact_20260919T2227Z.py`
- commit `856a265c7652ac481550524b55b506ff5c0fde10`

Executed exact output:

- `artifacts/hard7_2026-09-18/HARD7-03/four_step_exact_20260919T2227Z.out`
- commit `6f0059bbea21c375fd6db23d2ad835fa4c7b5a36`

The executed output ends `ALL_EXACT_CHECKS_PASS = True`. It verifies the complete 120-order sign atlas, all branch-rank equivalences, the nonpositive-boundary coefficient identity, exact reconstruction of the 21:23Z rational, the new rational `theta`, the positive Taylor margin, and the exact metric gain. This is a **self-check**, not an independent closure audit.

## 9. What this run does and does not establish

The genuinely new structural conclusion is that the **four-step homogeneous exponential-moment calculation is exact** after composing the previous pair and triple branch lemmas. Thus there is no longer any productive route that says “improve the four-step local inequality”: no local four-step inequality remains.

This does **not** solve Seppäläinen Problem 4. It does not determine the exact infinite-time shape constant `G_1(0)`, prove the exact `K=2` binary-disorder plateau width, or cover general `K`, general site-rate laws, particlewise disorder, or every stationary ergodic environment. The four-step Chernoff/block method still loses information by concatenating finite blocks and using one exponential moment.

The correct status remains **PARTIAL**.

## 10. Section-I state and next route

The frozen metric moved, so the unchanged-run streak resets and Section-I stuck rotation is not triggered.

The exactness theorem changes the next obligation qualitatively. The next run should **not** manufacture another four-step chamber correction. The remaining loss is now necessarily outside the exact four-step local recursion: finite block length, scalar exponential tilting, or the block concatenation step.

The best next new-method candidates are:

- **B7:** take the block-length limit and ask whether `m^{-1} log A_m(theta)` has a transfer-operator/subadditive limit that beats the four-block certificate;
- **B18:** recast the exact four-step map as a positive operator on boundary profiles and study its spectral radius instead of scalar block concatenation;
- **B29:** compactify the boundary-profile state space so that the operator extremizer cannot escape through large gap coordinates.

If that operator route fails to move the fixed metric over the next three runs, apply the Section-I stuck protocol rather than returning to local four-step bookkeeping.

## 11. Capability / scheduler statement

The exposed scheduler surface still provides prompt/title, schedule/timing mode and enabled state, but no binding model selector, no reasoning-effort selector, no authenticated reasoning telemetry and no guaranteed run duration. GPT-6/maximum is therefore prompt-requested only. This execution identifies as **GPT-5.6 Sol**, and the reasoning level is **UNVERIFIED**.

Changing the model/effort setting requires a product/backend or authorized scheduler surface that actually exposes those controls; repository prompt text cannot create them. The historical P26 `You cannot modify this task` event is an authorization/context restriction. The compliant workaround is the owning/authorized account or workspace context, or platform support/ownership correction — never a duplicate task or permission bypass. No schedule was created, modified, disabled, or reactivated in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  canonical_claim: D0025
  source_key: disordered_asep_open_1999::problem_4
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  fixed_metric: "rigorous lower bound L <= Delta_2(Q) for K=2, Q=(delta_1/2+delta_1)/2"
  before: 25000000/291978907
  after: 250000000/2919788131
  movement: true
  exact_gain: 23475000000/852516547160952817
  methods: [6, 17, 27]
  new_structural_result: "the complete four-step exponential-moment sum is exact after pair-kernel and sign-atlas closure"
  shape_upper_before: 291978907/100000000
  shape_upper_after: 2919788131/1000000000
  old_theta: 57343/100000
  new_theta: 286501/500000
  exact_checker: artifacts/hard7_2026-09-18/HARD7-03/four_step_exact_20260919T2227Z.py
  exact_output: artifacts/hard7_2026-09-18/HARD7-03/four_step_exact_20260919T2227Z.out
  exact_output_status: ALL_EXACT_CHECKS_PASS
  section_I_state: "metric moved; stagnation reset"
  next_methods: [7, 18, 29]
  posted_changed: false
  results_changed: false
  queue_changed: false
  claim_changed: false
```
