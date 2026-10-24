Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `53 -> 54` genuinely distinct nonparabolic shape families; Section-B moves actually used: #20 FIND WHY THE ALGORITHM FAILS, #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

# R07 CLOSABLE OUTSIDE — run 54: heterogeneous quadratic-clock portal curtains

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Target: Burdzy--Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Problem 7.8 / intake I0077.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

Overall source status remains **PARTIAL**. New claims T73/T74 below are SELF_CHECK_ONLY pending the required two independent OTHER-track audits. Publication novelty remains **UNVERIFIED**.

## 1. Continuity, admission, ownership, and frozen metric

Before research I recovered the current repository state rather than restarting from the scheduler title:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the current owner directive;
- canonical reservation `operations/claims/I0077.md`;
- the newest own R07 report, `runs/R07/20260918T2126Z_i0077_quadratic_variation_portal_curtains_53_qv53.md`;
- the visible/searchable R07 I0077 chain, including the moving/disconnected/web, gate, occupation, dimension, local-time, and quadratic-variation attempts;
- the newest neighboring R15 report. R15 remains on its distinct retired Burdzy--Scheutzow Problem 7.2 / I0076 handoff and later successor screens; it does not own I0077;
- the old C29 duplicate history and current I0077 exclusive reservation;
- targeted intake searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

`INDEX.md` and `RANKING.md` record Burdzy--Scheutzow Problem 7.5 as settled, not Problem 7.8. `POSTED.md` does not record Problem 7.8 as posted or settled. `operations/claims/I0077.md` still literally says `PENDING_ADMISSION, not READY` and names R07 as exclusive provisional owner; I preserve that shared state while following the owner's explicit assignment of this target.

The old R07 KPZ/FPP route remains preserved by immutable handoff and is not reopened or deleted. The large intake ledgers are too large for a literal byte-for-byte connector rendering; the intake reread is therefore honestly targeted to I0077, its ownership/exclusions, and prior attempts rather than falsely claimed complete over every unrelated row.

Frozen metric:

> number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo Brownian rescaling/reflection/translation and mere parameter changes inside one structural family.

Entering metric: **53**.  
Entering unchanged count: **0**.

The preceding report moved `52 -> 53` using #2/#11/#16 and proved the wrong-total-quadratic-variation gate obstruction T71/T72. Its explicit trace has dyadic quadratic energy diverging, so its total quadratic clock is already incompatible with Brownian time. The present run attacks exactly the boundary that report left open: **total quadratic variation is correct, but its local distribution in time is not**.

## 2. Primary-source benchmark rechecked

The primary arXiv PDF was re-read directly, including Definition 2.1, Theorem 4.3, and the open-problem page.

Definition 2.1 says that an FBM `X` has random witness times tending to `-infinity` such that, for every fixed witness,

\[
B^{(j)}(t)=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\tag{2.1}
\]

is an unconditional standard Brownian motion.

Theorem 4.3 is the three-part parabolic phase theorem in terms of the killed Ornstein--Uhlenbeck exponent `lambda_0(c_1,c_2)`:

1. `lambda_0 >= 1` gives the universal FBM far-past escape alternative;
2. `lambda_0 <= 1` gives a decomposable FBM with the corresponding asymptotic inclusion;
3. when `c_1 <= 0 <= c_2` and `lambda_0 < 1`, there is a decomposable FBM confined pointwise to the exact parabolic strip for all `t<=0`.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

The next sentence, Problem 7.9 on forward Levy processes, is not part of I0077.

## 3. Fresh current-literature / prior-art pass

Fresh bounded searches dated 2026-09-18 included:

- exact title/arXiv ID and exact Problem-7.8 wording;
- `Forward Brownian Motion Theorem 4.3 other space-time shapes`;
- `Burdzy Scheutzow Problem 7.8`;
- `prescribed pathwise quadratic variation Faber Schauder`;
- `generalized Takagi linear pathwise quadratic variation`;
- `quadratic variation quadratic roughness Brownian balanced partitions`;
- recent pathwise quadratic-variation / Ito-calculus papers.

Relevant prior art recovered:

- Alexander Schied, *On a class of generalized Takagi functions with linear pathwise quadratic variation*, arXiv:1501.00837 / JMAA 433 (2016). The deterministic Takagi/Faber--Schauder quadratic-variation mechanism used below is classical territory.
- Yuliya Mishura and Alexander Schied, *Constructing functions with prescribed pathwise quadratic variation*, arXiv:1511.04678 / JMAA 442 (2016), constructs continuous functions with prescribed curved or linear pathwise quadratic variation.
- Rama Cont and Purba Das, *Quadratic variation and quadratic roughness*, arXiv:1907.03115 / Bernoulli 29 (2023), studies robustness of pathwise quadratic variation under balanced partitions and Brownian quadratic roughness.
- Recent adjacent work includes Hove--Zondi--Lochowski--Mhlanga (2025) on partition-dependent quadratic variation/local time for the Peano curve and Ananova--Cont (2026) on pathwise Ito formulae for weakly differentiable functions.

These references mean the deterministic quadratic-variation constructions and Brownian `[B]_t=t` principle are **not** claimed novel. The bounded search did not surface an accessible later paper explicitly resolving exact Burdzy--Scheutzow Problem 7.8 or stating the FBM heterogeneous-clock gate theorem below. That is negative bounded evidence only, not a novelty certificate.

## 4. Counterexample-first / method #20 — why the run-53 algorithm genuinely fails

Run 53's test was the single number

\[
V_N(Q)=\sum_{k=0}^{2^N-1}
\bigl(Q((k+1)2^{-N})-Q(k2^{-N})\bigr)^2.
\tag{4.1}
\]

Brownian motion has `V_N -> 1` on a unit window. A tempting conclusion is that the quadratic-variation route is exhausted once a deterministic gate trace also has total limit `1`.

This run attacks that negation first. The conclusion is false: total mass can be exactly Brownian while the **quadratic clock is distributed incorrectly inside the window**. Thus a scalar checker can return the Brownian answer while a localized checker still separates the trace.

This is a falsification of a proposed extension mechanism, not a refutation of the source's open-ended Problem 7.8.

## 5. Method #5 — add a split parameter and see what the total statistic misses

Let

\[
\phi(x)=\operatorname{dist}(x,\mathbb Z),
\qquad
F(t)=\sum_{n=0}^{\infty}2^{-n/2}\phi(2^nt),\quad 0\le t\le1.
\tag{5.1}
\]

The series converges uniformly, hence `F` is continuous, and `F(0)=F(1)=0`.

On the level-`N` dyadic mesh, for `n<N` the `n`th summand has increment

\[
2^{n/2-N}r_n(k),
\tag{5.2}
\]

where `r_n(k) in {+1,-1}` are the dyadic Rademacher signs. Exact orthogonality gives

\[
\sum_{k=0}^{2^N-1}r_n(k)r_m(k)=2^N\mathbf 1_{n=m}.
\tag{5.3}
\]

Therefore

\[
V_N(F)
=2^{-N}\sum_{n=0}^{N-1}2^n
=1-2^{-N}\longrightarrow1.
\tag{5.4}
\]

Now add a parameter `alpha in (0,1)` and define

\[
Q_\alpha(t)=
\begin{cases}
\sqrt\alpha\,F(2t),&0\le t\le\tfrac12,\\[1mm]
\sqrt{1-\alpha}\,F(2t-1),&\tfrac12\le t\le1.
\end{cases}
\tag{5.5}
\]

Continuity at `1/2` follows from `F(0)=F(1)=0`.

For `N>=1`, define left/right dyadic energies by

\[
L_N(Q)=\sum_{k=0}^{2^{N-1}-1}(\Delta_{k,N}Q)^2,
\qquad
R_N(Q)=\sum_{k=2^{N-1}}^{2^N-1}(\Delta_{k,N}Q)^2.
\tag{5.6}
\]

Then exactly

\[
L_N(Q_\alpha)=\alpha(1-2^{1-N}),
\quad
R_N(Q_\alpha)=(1-\alpha)(1-2^{1-N}),
\tag{5.7}
\]

and hence

\[
V_N(Q_\alpha)=1-2^{1-N}\longrightarrow1
\quad\text{for every }\alpha.
\tag{5.8}
\]

The old scalar statistic has derivative zero in `alpha`, while

\[
\frac{d}{d\alpha}\lim_N L_N(Q_\alpha)=1,
\qquad
\frac{d}{d\alpha}\lim_N R_N(Q_\alpha)=-1.
\tag{5.9}
\]

So the parameter exposes precisely what was invisible: total quadratic mass is conserved, but the local clock moves.

At the canonical value

\[
\boxed{\alpha=\tfrac34,}
\tag{5.10}
\]

we have

\[
V_N(Q_{3/4})\to1,
\qquad
L_N(Q_{3/4})\to\frac34,
\qquad
R_N(Q_{3/4})\to\frac14.
\tag{5.11}
\]

Brownian motion instead allocates `1/2` of its unit quadratic variation to each half.

The balanced point `alpha=1/2` is deliberately **not** claimed solved: the present invariant is silent there even though a deterministic trace is of course far more rigid than a Brownian path. This is the new sharp boundary left for later work.

## 6. Method #30 — localize the quadratic clock

For a dyadic interval

\[
I=[p2^{-r},(p+1)2^{-r}]\subset[0,1]
\tag{6.1}
\]

and `N>=r`, write

\[
V_N(Q;I)
=\sum_{[k2^{-N},(k+1)2^{-N}]\subset I}
\bigl(Q((k+1)2^{-N})-Q(k2^{-N})\bigr)^2.
\tag{6.2}
\]

Run 53 proved the dependence-safe Brownian lemma that on one probability-one event, for every finite `A`,

\[
\sup_{0\le\theta\le A}
\left|
\sum_{k=0}^{2^n-1}
(B_{\theta+(k+1)2^{-n}}-B_{\theta+k2^{-n}})^2-1
\right|\to0.
\tag{6.3}
\]

The new observation is that this immediately localizes to every dyadic subwindow.

### Lemma 6.1 — uniform local Brownian quadratic clock

For standard Brownian motion `B`, almost surely, simultaneously for every dyadic interval `I subset [0,1]` and every finite `A`,

\[
\sup_{0\le\theta\le A}
\left|V_N(B(\theta+\cdot);I)-|I|\right|\longrightarrow0.
\tag{6.4}
\]

#### Proof

Write `|I|=ell=2^{-r}` and let `q` be its left endpoint. The energy over `theta+I` is the energy over a length-`ell` window starting at `theta+q`. Define

\[
\widetilde B_t=\ell^{-1/2}B_{\ell t},
\tag{6.5}
\]

which is standard Brownian motion. At global mesh level `N`, the rescaled window uses level `N-r`, and exactly

\[
V_N(B(\theta+\cdot);I)
=\ell\,V_{N-r}(\widetilde B; (\theta+q)/\ell).
\tag{6.6}
\]

Apply (6.3) to `\widetilde B` on the required compact shift range. This yields (6.4) for one `I,A`. There are only countably many dyadic `I` and integer `A`, so intersect the corresponding probability-one events. QED.

This step is why no conditioning on a random FBM witness phase is needed: all phases are controlled pathwise **before** the witness is introduced.

## 7. New general theorem T73 — non-Lebesgue quadratic-clock gate obstruction

### Theorem T73

Let `Q in C([0,1])`. Suppose there exists a dyadic interval `I subset [0,1]` such that

\[
\limsup_{N\to\infty}
\left|V_N(Q;I)-|I|\right|>0.
\tag{7.1}
\]

Let `a_m -> infinity` be deterministic and let `c_m in R`. Consider any deterministic fiber family `K(u)` such that on every unit gate block

\[
K(a_m+s)\subset\{c_m+Q(s)\},
\qquad 0\le s\le1,
\tag{7.2}
\]

while **no condition whatsoever** is imposed on `K(u)` between the gate blocks.

Then every forward Brownian motion `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ X_{-u}\in K(u)\ \forall u\ge R
\right)=0.
}
\tag{T73}
\]

#### Proof

Let `E_r` be the event that confinement holds for all `u>=r`. It suffices to prove `P(E_r)=0` for each integer `r`.

Fix `r` and choose one deterministic gate index `m` with `a_m>=r`. Enumerate FBM witnesses so that `S_j -> -infinity`. Put

\[
C_j=\{S_j\le-(a_m+1)\}.
\tag{7.3}
\]

Since the witnesses tend to `-infinity`, `\cup_j C_j` has probability one. Hence

\[
E_r\subset\bigcup_j(E_r\cap C_j)
\quad\text{modulo a null set}.
\tag{7.4}
\]

Fix `j`. By Definition 2.1,

\[
B^{(j)}_t=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\tag{7.5}
\]

is an unconditional standard Brownian motion. On `C_j` define the (possibly path-dependent) phase

\[
\theta=-a_m-1-S_j\ge0.
\tag{7.6}
\]

If `E_r` also holds, then for every `0<=s<=1`, physical time `S_j+\theta+s=-a_m-1+s` has age `a_m+1-s`, so (7.2) forces

\[
B^{(j)}_{\theta+s}
=c_m+Q(1-s)-X_{S_j}.
\tag{7.7}
\]

Let `I^*=\{1-s:s\in I\}`, which is again a dyadic interval with `|I^*|=|I|`. Reversal does not change sums of squared increments, so

\[
V_N(B^{(j)}(\theta+\cdot);I^*)=V_N(Q;I).
\tag{7.8}
\]

Lemma 6.1 applied to the Brownian path `B^{(j)}` holds simultaneously for every phase `theta>=0` (intersect over integer compact ranges), and therefore the left side of (7.8) converges to `|I|`. This contradicts (7.1).

Thus `P(E_r cap C_j)=0` for every fixed `j`. Equation (7.4) gives `P(E_r)=0`; finally take the countable union over `r`. QED.

### What T73 adds to T71

T71 is recovered by taking `I=[0,1]`: a wrong total quadratic variation forbids confinement. T73 is strictly useful beyond T71 because it also handles traces whose **total unit-window quadratic variation is exactly Brownian** but whose local quadratic-variation measure is not Lebesgue time.

## 8. Canonical point-54 family and T74

Set

\[
Q=Q_{3/4}
\tag{8.1}
\]

from (5.5). Its total dyadic energy satisfies `V_N(Q)->1`, so T71/run 53 is completely silent. But (5.11) gives the local mismatch on `I=[0,1/2]`.

To make a closed, visibly nonparabolic space-time shape with unrestricted chambers between gate blocks, take

\[
a_m=m!,\qquad m\ge3,
\tag{8.2}
\]

and `I_m=[a_m,a_m+1]`. Define a continuous center `g` by

\[
g(u)=Q(u-a_m)\quad(u\in I_m),
\qquad
g(u)=0\quad\text{between gate blocks}.
\tag{8.3}
\]

This is continuous because `Q(0)=Q(1)=0`.

For each gap `(b_m,a_{m+1})`, where `b_m=a_m+1`, let

\[
p_m=\frac{b_m+a_{m+1}}2.
\tag{8.4}
\]

Define the extended radius

\[
\rho(u)=0\quad\text{on the gate blocks},
\tag{8.5}
\]

and on a gap

\[
\rho(u)=
\begin{cases}
\dfrac{u-b_m}{p_m-u},&b_m<u<p_m,\\[2mm]
+\infty,&u=p_m,\\[2mm]
\dfrac{a_{m+1}-u}{u-p_m},&p_m<u<a_{m+1}.
\end{cases}
\tag{8.6}
\]

For the bounded initial segment before `a_3`, set `g=0,rho=0`. Put

\[
K_*(u)=
\begin{cases}
[g(u)-\rho(u),g(u)+\rho(u)],&\rho(u)<\infty,\\
\mathbb R,&\rho(u)=\infty,
\end{cases}
\tag{8.7}
\]

and

\[
\mathcal C_*
=\{(-u,x):u\ge0,\ x\in K_*(u)\}.
\tag{8.8}
\]

The shape is closed. At every gate endpoint the radius tends to zero and `g` tends to the singleton gate value; at every portal `p_m` the radius tends to infinity and the portal fiber is all of `R`. Thus finite convergent sequences cannot escape the set.

Every gate block has the exact rough trace

\[
K_*(a_m+s)=\{Q(s)\},\qquad0\le s\le1,
\tag{8.9}
\]

whereas every gap contains a literal full-space portal

\[
\boxed{K_*(p_m)=\mathbb R.}
\tag{8.10}
\]

Applying T73 gives:

### Theorem T74

For every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists R:\ (-u,X_{-u})\in\mathcal C_*\ \forall u\ge R
\right)=0.
}
\tag{T74}
\]

This is the canonical **heterogeneous quadratic-clock portal curtain**.

## 9. Frozen-equivalence audit: why point 54 is not a parameter recount

The metric point is assigned to the **unit-total-QV / non-Lebesgue-local-clock family**, not to a new choice of coefficient inside run 53.

- Run 53's canonical exact gate trace has wrong total quadratic variation (indeed it diverges). Here the total quadratic variation converges to exactly the Brownian value `1` on every unit gate.
- The new invariant is the normalized local clock: this trace places asymptotic mass `(3/4,1/4)` on the two equal half-windows instead of Brownian `(1/2,1/2)`.
- Brownian scaling multiplies spatial squared scale and temporal scale compatibly, so the ratio `quadratic-variation mass / elapsed time` is preserved. Reflection and translation do not change squared increments. Time reversal merely swaps the two halves. None of the frozen equivalences turns `(3/4,1/4)` into `(1/2,1/2)` or into the run-53 wrong-total class.
- The parameter `alpha` in (5.5) belongs to this **single** new family; different non-balanced `alpha` values are not separately counted.
- This is not run 47's persistence mechanism: only one fixed-length exact gate is needed after a tail threshold; there is no long cluster of bounded Gaussian increments.
- It is not run 32's moving Cantor lamination/topological leaf conservation: every restrictive fiber here is a singleton and the selected leaf itself has Brownian-scale roughness.
- It is not the occupation/dimension/local-time families 44--52: the obstruction is neither temporal measure nor Hausdorff dimension nor spatial nullity, but the allocation of quadratic energy inside one exact unit trace.

Accordingly the frozen metric moves **53 -> 54 exactly once**.

## 10. Exact finite self-check

The finite Walsh/Rademacher arithmetic was checked with exact rational arithmetic in

`artifacts/R07/20260918T2224Z_qc54_exact_checker.py`

and the executed output was archived as

`artifacts/R07/20260918T2224Z_qc54_exact_checker.out`.

The checker verifies, through level `N=12`, the exact Rademacher orthogonality, the base identity `V_N(F)=1-2^{-N}`, and the composite identities

\[
L_N(Q)=\frac34(1-2^{1-N}),\quad
R_N(Q)=\frac14(1-2^{1-N}),\quad
V_N(Q)=1-2^{1-N}.
\tag{10.1}
\]

It terminates `PASS`. This is explicitly a **SELF-CHECK**, not an independent audit. The all-`N` identities are proved symbolically in Section 5.

## 11. What failed, what succeeded, and the next frontier

### #20 FIND WHY THE ALGORITHM FAILS — success

The run-53 scalar total-energy test returns the Brownian value for the entire `Q_alpha` family. Its failure is exact, not numerical: equation (5.8) is independent of `alpha` in the limit.

### #5 ADD A PARAMETER AND DIFFERENTIATE — success

The split parameter moves left and right quadratic mass with derivatives `+1` and `-1` while leaving total mass fixed. This exposed the missing state variable: the **quadratic-variation measure**, not its total mass.

### #30 DO ONE SCALE / ONE DIRECTION AT A TIME — success

Localizing to one dyadic half-window, then proving the Brownian result uniformly over every phase, closes the random-witness loophole and yields T73/T74.

The next real frontier is now the balanced-clock class, beginning with `Q_{1/2}`:

\[
V_N(Q_{1/2};[0,1/2])\to\frac12,
\qquad
V_N(Q_{1/2};[1/2,1])\to\frac12,
\qquad
V_N(Q_{1/2})\to1.
\tag{11.1}
\]

A finite dyadic split no longer separates that template from Brownian quadratic time. The next route should test a finer invariant that Brownian paths possess simultaneously over all phases but deterministic Faber--Schauder traces can violate: e.g. a full quadratic-variation measure at all scales plus a second-order statistic (signed crossing/local-time profile, Lévy modulus, or a rough-path/iterated statistic). No such stronger claim is made here.

## 12. Closure / audit status

- T73: full proof on this page; **SELF_CHECK_ONLY**; `0/2` required independent OTHER-track audits.
- T74: complete explicit canonical construction and proof via T73; **SELF_CHECK_ONLY**; `0/2` audits.
- finite core: exact checker executed and output archived; this does not substitute for an external audit.
- prior-art search: recorded above; publication novelty **UNVERIFIED**.
- source Problem 7.8: **PARTIAL**, not PROVED/CLOSED.
- canonical claim: still `PENDING_ADMISSION, not READY`; no shared-root or peer-track file was edited.

No paper folder is created because closure requirements have not been met.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  worker: R07
  source: Burdzy-Scheutzow Forward Brownian Motion, Problem 7.8
  intake: I0077
  metric: nonparabolic_shape_families_complete_source_appropriate_theorem
  before: 53
  after: 54
  movement: +1
  unchanged_count_before: 0
  unchanged_count_after: 0
  new_family: unit-total-QV heterogeneous-local-quadratic-clock portal curtains
  claims_added: [T73, T74]
  source_status_before: PARTIAL
  source_status_after: PARTIAL
  independent_other_track_audits: 0/2
  novelty: UNVERIFIED
  admission: PENDING_ADMISSION_not_READY
  next_frontier: balanced local quadratic clock / second-order path invariant
```

## 14. Model / scheduler control report

Actual runtime metadata available to this report says **GPT-5.6 Sol**; the reasoning-effort metadata is **UNVERIFIED**. I therefore do not claim GPT-6 maximum.

The exposed scheduler/action schema still offers task title/prompt, schedule or relative start offset, enabled state, and timing mode. It still exposes **no binding model-family field, no reasoning-effort field, no guaranteed hour-long execution field, and no authenticated completed-run model receipt**. The requested `GPT-6 / maximum` line therefore remains prompt-level only in this interface.

No scheduler modification was attempted, consistent with the owner's prohibition on scheduler changes in this deployment. The repository's current reconciliation records the old P26 `You cannot modify this task` response as authorization-context-specific; a later full P26 update succeeded from an authorized context. For a task that still rejects modification, the legitimate route is the owning/authorized workspace or account, an authorized ownership/admin correction, or platform support -- not a duplicate task or permission bypass.
