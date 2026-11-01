Model actually ran: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum. NO MOVEMENT: `C_sub: 0 -> 0`; supported unchanged count `6 -> 7`; methods B16/B5/B26. The selected post-recovery refutation action succeeds against the internal candidate envelope: at an exact critical finite-tree resonance the candidate predicts `Theta(log n)` while the actual largest percolation component is `Omega((log n)^2)` a.a.s.

# G0010 — post-recovery refutation action: critical-window tree area defeats the two-mechanism envelope

## 1. Source / exact target / status

**Native task.** `6aa7eca50c1c8191b3c26254b14d65fd`.

**Target.** G0010, HARD OUTSIDE.

**Primary source.** Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1, submitted 2026-08-19, Question 5.2.

**Exact source target.** For arbitrary finite `G`, with maximum degree `Delta(G)` and adjacency spectral radius `lambda(G)`, determine the tight typical all-regime upper scale of the largest component of Bernoulli bond percolation `G_p` under

\[
p\le \frac{1-\varepsilon}{\lambda(G)}
\]

for fixed `epsilon>0`, preserving the source graph class, probability convention and all `(Delta,lambda)` regimes.

**Frozen metric.** `C_sub in {0,1}`. Before `0`; after `0`. It becomes `1` only after a source-valid matching theorem/counterexample settles the full all-regime Question 5.2.

**Status after this run.** **OPEN / PARTIAL.** This run refutes only the internal two-mechanism candidate proposed by STUCK RECOVERY 2. It does not refute or solve Question 5.2.

## 2. Snapshot / continuity / ownership / repository read

Captured `master` immediately before delivery:

`e9508a3eb5a21ef7959898570283c9753f997866`.

Exclusive claim:

`operations/claims/G0010.md`, blob `b62a5a64b2fde8f44efde5c3350452ebe83be0a2`.

Previous current-target report:

`proofnet24/HARD10-01/rotations/G0010/runs/2026-09-17/2026-09-17T22-20-00Z__report.md`

creation commit

`7b5a7feb4e237fc392acf743cc962ae980346f40`

readback blob

`a3d1cf2773c3c618156c3fc5628caf09a78c3ae1`.

Path-scoped history was re-read and no later G0010 report existed before this write. The required repository entrypoints were also re-read/reconciled at this run: `operations/VISIBLE_FLEET_2026-09-16.md`, root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, the G0010 claim, intake/search material, and same-source neighboring work. Shared roots were not edited.

`HISTORY_GAP`: none material to the current G0010 chain.

## 3. The selected action from STUCK RECOVERY 2

Recovery 2 selected **REFUTE INSTEAD OF PROVE**. The object to attack was the explicitly non-theorem candidate

\[
F_\varepsilon(n,\Delta,\lambda)
=
\frac{\Delta}{\lambda}
\log\!\left(e+\frac{n\lambda^2}{\Delta^2}\right)
+n^\alpha,
\tag{3.1}
\]

where

\[
b=\min\left\{\Delta-1,\frac{\lambda^2}{4}\right\},
\qquad
\alpha=
\left[
\frac{\log((1-\varepsilon)b/\lambda)}{\log b}
\right]_+
\tag{3.2}
\]

when `b>1`.

The two intended pieces were:

1. a hub/multiplicity scale `(Delta/lambda) log(e+n lambda^2/Delta^2)`;
2. a deep-tree polynomial scale `n^alpha`.

This run shows that these two pieces omit a third mechanism: **critical-window finite-depth total progeny**, which produces a `log^2 n` scale exactly where the polynomial exponent clips to zero.

## 4. B16 — compute the small sequence: d=8,9,10 exposes the missing boundary layer

Take the complete rooted `d`-ary tree `T_{d,h}` of height `h`. For `h>=2`,

\[
|T_{d,h}|=n_h=\frac{d^{h+1}-1}{d-1},
\qquad
\Delta(T_{d,h})=d+1,
\tag{4.1}
\]

and the exact adjacency spectral radius is

\[
\lambda_h=2\sqrt d\cos\theta_h,
\qquad
\theta_h=\frac{\pi}{h+2}.
\tag{4.2}
\]

For the diagnostic fixed value

\[
1-\varepsilon=c=\frac23,
\qquad \varepsilon=\frac13,
\tag{4.3}
\]

the source-boundary percolation parameter is

\[
p_h=\frac{c}{\lambda_h}.
\tag{4.4}
\]

The downward offspring mean in a descendant subtree is

\[
m_h(d)=d p_h
=\frac{c\sqrt d}{2\cos\theta_h}.
\tag{4.5}
\]

Hence the three consecutive integer branchings have distinct limiting behavior:

- `d=8`: `m_h(8) -> sqrt(8)/3 < 1`; a fixed subcritical gap eventually appears;
- `d=9`: `m_h(9) = 1/cos(theta_h) = 1+Theta(h^{-2})`; this is the finite-depth critical window;
- `d=10`: `m_h(10) -> sqrt(10)/3 > 1`; finite-depth descendant growth is genuinely supercritical and gives a polynomial mechanism.

The middle integer is the sporadic case the two-mechanism formula misses.

## 5. Exact candidate evaluation on the d=9 resonance

Now fix `d=9`, `epsilon=1/3`. Then

\[
\lambda_h=6\cos\theta_h,
\qquad
\Delta_h=10,
\qquad
p_h=\frac{1}{9\cos\theta_h}.
\tag{5.1}
\]

For the candidate (3.1)-(3.2),

\[
\frac{\lambda_h^2}{4}=9\cos^2\theta_h<9=\Delta_h-1,
\]

so

\[
b_h=9\cos^2\theta_h.
\tag{5.2}
\]

Moreover

\[
\frac{(1-\varepsilon)b_h}{\lambda_h}
=
\frac{(2/3)\,9\cos^2\theta_h}{6\cos\theta_h}
=
\cos\theta_h<1.
\tag{5.3}
\]

Therefore the candidate polynomial exponent is **exactly**

\[
\alpha_h=0
\tag{5.4}
\]

for every finite `h`.

Since `Delta_h/lambda_h` stays bounded above and below by positive constants and `lambda_h^2/Delta_h^2` does as well,

\[
F_{1/3}(n_h,10,\lambda_h)
=
\Theta(\log n_h)
=
\Theta(h).
\tag{5.5}
\]

Thus a lower bound `|C_max| = Omega(h^2)` a.a.s. is enough to falsify (3.1) even as an upper-scale candidate.

## 6. Critical Galton-Watson input

Because

\[
p_h=\frac{1}{9\cos\theta_h}>\frac19,
\tag{6.1}
\]

bond percolation in every descendant `9`-ary subtree at parameter `p_h` stochastically dominates critical percolation with retention

\[
q=\frac19.
\tag{6.2}
\]

Under `q=1/9`, the open descendant cluster of a fixed root is the critical Galton-Watson process with offspring

\[
X\sim \operatorname{Bin}(9,1/9),
\qquad
\mathbb E X=1,
\qquad
\sigma^2=\operatorname{Var}(X)=\frac89.
\tag{6.3}
\]

Let `Z_t` be its generation size, `Z_0=1`, and

\[
S_m=\sum_{t=0}^m Z_t.
\tag{6.4}
\]

I use only the classical finite-variance critical Galton-Watson survival/Yaglom theorem:

\[
\mathbb P(Z_m>0)\sim\frac{2}{\sigma^2m},
\qquad
\frac{Z_m}{m}\,\Big|\,(Z_m>0)
\Rightarrow Y,
\tag{6.5}
\]

where `Y` is nondegenerate exponential. In particular, there are constants `a,c_0>0`, depending only on the fixed offspring law, such that for all sufficiently large `m`,

\[
\mathbb P(Z_m\ge a m)\ge \frac{c_0}{m}.
\tag{6.6}
\]

This is standard branching-process input, not a novelty claim.

## 7. Full second-moment derivation: survival at m gives area of order m^2 with probability order 1/m

For a critical Galton-Watson process with variance `sigma^2`,

\[
\mathbb E Z_t=1,
\qquad
\operatorname{Var}(Z_t)=\sigma^2 t,
\qquad
\mathbb E Z_t^2=1+\sigma^2 t.
\tag{7.1}
\]

For `s<=t`, conditioning on generation `s` gives

\[
\mathbb E[Z_sZ_t]
=\mathbb E\!\left[Z_s\,\mathbb E(Z_t\mid Z_s)\right]
=\mathbb E Z_s^2
=1+\sigma^2s.
\tag{7.2}
\]

Hence

\[
\mathbb E S_m=m+1
\tag{7.3}
\]

and

\[
\begin{aligned}
\mathbb E S_m^2
&=\sum_{s,t=0}^m \bigl(1+\sigma^2\min\{s,t\}\bigr)\\
&=(m+1)^2
+\sigma^2\sum_{r=1}^m (m-r+1)^2\\
&=(m+1)^2
+\sigma^2\frac{m(m+1)(2m+1)}6\\
&=O(m^3).
\end{aligned}
\tag{7.4}
\]

Now condition on `Z_m=N>=a m`. By the branching property, the descendants during the next `m` generations of these `N` particles are independent copies `S_m^{(1)},...,S_m^{(N)}` of `S_m`. Put

\[
Y_N=\sum_{i=1}^N S_m^{(i)}.
\tag{7.5}
\]

Then

\[
\mathbb E(Y_N\mid N)=N(m+1)\ge a m(m+1)
\tag{7.6}
\]

and, using (7.4),

\[
\mathbb E(Y_N^2\mid N)
=N\mathbb E S_m^2+N(N-1)(m+1)^2
\le C N m^3+N^2(m+1)^2.
\tag{7.7}
\]

Because `N>=a m`, the ratio of the right-hand side of (7.7) to `(E[Y_N|N])^2` is bounded by a constant depending only on `a` and the offspring law. Paley-Zygmund therefore gives constants `c_1,c_2>0` such that

\[
\mathbb P\!\left(Y_N\ge c_1m^2\mid Z_m=N\right)\ge c_2
\tag{7.8}
\]

uniformly for `N>=a m` and large `m`.

Since the vertices counted by `Y_N` lie in the same descendant open cluster as the original particle whenever the process reaches generation `m`, (6.6) and (7.8) imply

\[
\boxed{
\mathbb P(S_{2m}\ge c_1m^2)\ge \frac{c_3}{m}
}
\tag{7.9}
\]

for some fixed `c_3>0`.

This is the key critical-area estimate.

## 8. Many independent descendant subtrees force an Omega(h^2) component a.a.s.

Return to `T_{9,h}`. Choose

\[
m=\left\lfloor\frac h4\right\rfloor.
\tag{8.1}
\]

At level `h-2m` there are

\[
M_h=9^{h-2m}
\tag{8.2}
\]

vertices, and their depth-`2m` descendant subtrees are edge-disjoint. Percolation events confined to those subtrees are therefore independent.

Under the auxiliary critical retention `q=1/9`, each such subtree has, by (7.9), probability at least `c_3/m` of containing from its root a descendant open cluster with at least `c_1m^2` vertices. Consequently

\[
\mathbb P_q\!\left(
\text{none of the }M_h\text{ subtrees has such a cluster}
\right)
\le
\left(1-\frac{c_3}{m}\right)^{M_h}
\le
\exp\!\left(-\frac{c_3M_h}{m}\right)
\longrightarrow0.
\tag{8.3}
\]

The actual source-boundary parameter satisfies `p_h>q`, so monotone coupling transfers the same lower event to `p_h`. Therefore

\[
\boxed{
|C_{\max}((T_{9,h})_{p_h})|
\ge c_4 h^2
\quad\text{a.a.s.}
}
\tag{8.4}
\]

for some constant `c_4>0`.

Since `log n_h=Theta(h)`,

\[
|C_{\max}|
=\Omega((\log n_h)^2)
\quad\text{a.a.s.}
\tag{8.5}
\]

Combining (8.5) with (5.5) gives

\[
\frac{|C_{\max}|}{F_{1/3}(n_h,10,\lambda_h)}
\longrightarrow\infty
\quad\text{in probability along this family}.
\tag{8.6}
\]

Hence the candidate (3.1) is **refuted as a universal upper-scale envelope**.

This is not a refutation of the source question; Question 5.2 asks what the correct envelope is.

## 9. B5 — add the branching parameter: the missing mechanism is a singular critical boundary layer

For a fixed `d`-ary tree and fixed `c=1-epsilon`, the limiting descendant mean at the source spectral boundary is

\[
\mu_\infty(d,c)
=\lim_{h\to\infty}d\frac{c}{\lambda_h}
=\frac{c\sqrt d}{2}.
\tag{9.1}
\]

The regular-tree critical surface is therefore

\[
\mu_\infty=1
\quad\Longleftrightarrow\quad
c=\frac{2}{\sqrt d}.
\tag{9.2}
\]

Away from that surface:

- `mu_infty<1`: the descendant branching process has a fixed subcritical gap; logarithmic extremes are natural;
- `mu_infty>1`: depth-`Theta(log n)` transient growth creates the polynomial `n^alpha` mechanism already recovered in earlier G0010 work.

Exactly on (9.2), however, the finite-tree spectral correction gives

\[
\mu_h
=\frac1{\cos\theta_h}
=1+\frac{\pi^2}{2(h+2)^2}+O(h^{-4}),
\tag{9.3}
\]

so the process lies inside the critical finite-size window on a horizon of order `h`: `(mu_h-1)h ->0`. Critical total progeny scales like horizon squared, which is exactly the `h^2` mechanism proved above.

The failure of (3.1) is therefore not a bad constant. The map

\[
\alpha=\left[\frac{\log(cb/\lambda)}{\log b}\right]_+
\]

clips the exponential growth rate to zero and thereby throws away the **critical polynomial-in-depth correction**. A correct all-regime envelope must include a boundary-layer term that survives when the exponential tree exponent vanishes.

## 10. B26 — the “sporadic” case is actually an infinite resonance family

The same argument is not specific to `d=9`. For every integer `d>=5`, define the fixed source parameter

\[
\varepsilon_d=1-\frac2{\sqrt d}\in(0,1).
\tag{10.1}
\]

For `T_{d,h}` and

\[
p_h=\frac{1-\varepsilon_d}{\lambda_h}
=\frac{1}{d\cos\theta_h},
\tag{10.2}
\]

we again have `p_h>1/d`, while

\[
b_h=\frac{\lambda_h^2}{4}=d\cos^2\theta_h
\]

and

\[
\frac{(1-\varepsilon_d)b_h}{\lambda_h}
=\cos\theta_h<1.
\tag{10.3}
\]

Thus the candidate still assigns `alpha_h=0` and `F=Theta(log n_h)`, whereas the same critical Galton-Watson argument gives

\[
|C_{\max}|=\Omega((\log n_h)^2)
\quad\text{a.a.s.}
\tag{10.4}
\]

This produces infinitely many fixed-`epsilon` resonance counterfamilies. The missing third mechanism is therefore structurally real, not a single numerical accident.

## 11. What this changes about the G0010 obstruction

Before this run, the working obstruction was “optimize total progeny over multiscale Perron/degree profiles while capturing hub multiplicity and deep-tree transient growth.” That remains true, but it is now incomplete in an important way.

A source-valid sharp envelope must interpolate at least **three** mechanisms:

1. **hub/multiplicity extremes**, exemplified by complete bipartite hosts and captured in the biregular theorem;
2. **supercritical finite-depth tree growth**, producing polynomial `n^alpha` scales;
3. **critical finite-depth area**, producing at least `Theta((log n)^2)` at resonance surfaces where the exponential transient exponent is zero.

The third mechanism is not visible in a formula containing only a logarithmic hub term plus a clipped polynomial exponent.

The full source obligation is still unchanged:

\[
\boxed{
\text{Determine the matching worst-case typical scale for every feasible }(n,\Delta,\lambda)\text{ regime.}
}
\]

No current route has the matching all-host upper theorem or the complete lower-family phase diagram.

## 12. Failed routes in this selected action

### Three-type monotone path as a new mechanism

A monotone equitable three-type chain with forward degrees of order `D` and reverse degrees of order one can have expected root progeny of order `(Delta/lambda)^2`, but population balance forces the last type population to grow by the corresponding product. In the long-chain limit this is precisely the already-known finite-tree exponent mechanism, not a genuinely new third scale.

### Alternating high/low population chain

Alternating rare/common transitions create a burst followed by a compensating bottleneck. In the simple three/four-type quotients examined algebraically, the expected number of particles reaching the next rare layer is only order one when the preceding burst is order `Delta/lambda`; the next burst then reproduces the hub mechanism rather than multiplying it freely. This did not beat the candidate.

### Forked three-type quotient

For a rare center with two leaf types, if the quotient degrees are `D_i` outward and `d_i` inward, then `lambda^2=sum_i D_i d_i`, and the root total-progeny expectation in the collision-blind multitype process reduces to a denominator `1-c^2` with numerator controlled by the root row sum `<=Delta`. Spectral budget splitting across branches therefore did not produce a new scale.

These failures are why the critical integer resonance is the substantive outcome of B16/B5/B26 rather than another hierarchical-burst formula.

## 13. Dated source / current / later / citing checks

Checks performed 2026-09-17 UTC / 2026-09-18 Asia/Jerusalem:

1. **Primary source reread.** The arXiv HTML for `2608.19145v1` still states in its concluding remarks that Theorem 1.4 gives the general `O(sqrt(n Delta) log n / lambda)` bound, discusses the `K_{s,s^3}`, `lambda~sqrt(Delta)`, constant-`lambda`, and regular regimes, and then asks Question 5.2: for prescribed `Delta(G)` and `lambda(G)`, what is the tight typical largest-component upper bound when `p <= (1-epsilon)/lambda(G)`?
2. **Version/current check.** arXiv still exposes v1 dated 2026-08-19; bounded exact-title/arXiv-ID searches found no later version or source-matching resolution.
3. **Author check.** Current publication pages/searches for the three authors still list this paper and did not expose a later paper resolving Question 5.2. This is negative evidence, not an openness certificate.
4. **Current problem mirror.** A current open-problem mirror still reproduces the same tight-subcritical question as open.
5. **Critical branching prior art.** The only outside input used in the new lower-bound derivation is classical finite-variance critical Galton-Watson survival/Yaglom theory; related literature also studies total progeny and finite-size survival. No novelty claim is made for the `log^2` critical-tree mechanism itself. The research contribution of this run is its use as a direct refutation of the fleet's internal candidate envelope and the consequent correction of the G0010 phase diagram.

Search phrases included the exact title/arXiv ID, authors plus `Question 5.2` / `tight subcritical`, and critical Galton-Watson survival/total-progeny finite-size searches.

## 14. Model / scheduler interface status

The exposed scheduler/task-edit surface still provides prompt/title/schedule/timing/enabled fields but no authenticated model-family selector and no reasoning-effort selector. Therefore `GPT-6 / maximum` remains prompt text only. This report correctly states the actually exposed runtime identity as GPT-5.6 Sol and reasoning level UNVERIFIED.

Changing that requires a product/platform surface exposing owner-authorized model and reasoning selectors, or platform support. Prompt wording cannot authenticate runtime selection.

For a task that returns `You cannot modify this task`, the only valid workaround remains the owning authorized context or platform/admin support. Do not duplicate the schedule, change access, or bypass permission boundaries.

## 15. Artifacts / checker discipline

No new checker or artifact was created. The new claim is theorem-sized and its derivation is on the page. It relies on a standard asymptotic branching-process theorem rather than a finite computation, so manufacturing an exact checker would not certify the relevant step and would violate the research-first directive.

## 16. Next state under the HARD no-recovery-3 rule

Both permitted HARD stuck recoveries have already been consumed. This run is the one selected post-Recovery-2 action, and it leaves `C_sub=0` and the full source obligation unresolved.

Therefore there is **no Recovery 3**. The next qualifying G0010 invocation must be a preserved terminal handoff and in-place successor rotation, not another ordinary G0010 lemma/checker run. The handoff should preserve:

- the exact pointwise finite-horizon nonbacktracking bound and equality families;
- exceptional-root `L^2` budgets and collision profile;
- the arbitrary biregular weighted-branching upper-tail theorem;
- the Perron-profile variational formulation;
- the present critical-resonance refutation of the two-mechanism candidate;
- the corrected three-mechanism phase picture: hub/multiplicity + polynomial tree transient + critical finite-depth area.

Do not self-disable and do not create a new native schedule/ID.

## 17. `ledger_delta`

```yaml
ledger_delta:
  native_task_id: 6aa7eca50c1c8191b3c26254b14d65fd
  target_id: G0010
  report_kind: POST_RECOVERY_2_SELECTED_REFUTATION_ACTION
  input_snapshot_sha: e9508a3eb5a21ef7959898570283c9753f997866
  previous_report_path: proofnet24/HARD10-01/rotations/G0010/runs/2026-09-17/2026-09-17T22-20-00Z__report.md
  previous_report_commit: 7b5a7feb4e237fc392acf743cc962ae980346f40
  exact_source: Christoph-Morawski-Wigderson arXiv:2608.19145v1 Question 5.2
  metric: C_sub
  metric_before: 0
  metric_after: 0
  supported_unchanged_count_before: 6
  supported_unchanged_count_after: 7
  hard_recovery_cycles_consumed: 2_of_2
  methods:
    - B16: d=8,9,10 regular-tree sequence isolates d=9 as the exact critical finite-depth resonance at epsilon=1/3
    - B5: branching parameter mu=c sqrt(d)/2 shows a singular critical boundary layer; alpha clipping loses the horizon-squared total-progeny scale
    - B26: resonance generalizes to every integer d>=5 at fixed epsilon_d=1-2/sqrt(d), refuting the candidate on infinitely many fixed-epsilon families
  candidate_refuted: F_epsilon=(Delta/lambda)log(e+n lambda^2/Delta^2)+n^alpha from STUCK_RECOVERY_2
  rigorous_new_partial: on T_{d,h} with epsilon=1-2/sqrt(d) and p=(1-epsilon)/lambda(T_{d,h}), C_max=Omega((log n)^2) a.a.s. while the candidate gives Theta(log n)
  exact_new_mechanism: critical finite-depth Galton-Watson area at the zero-exponent transition
  mathematical_status: PARTIAL_SOURCE_OPEN
  source_closed: false
  next_state: TERMINAL_HANDOFF_AND_IN_PLACE_ROTATION_ON_NEXT_QUALIFYING_INVOCATION
  audit_refs: []
  artifact_refs: []
  shared_ledgers_edited: false
  email_drive_public_posting: false
  note: No recovery 3; do not continue ordinary G0010 research after this selected action if the same source obligation remains.
```
