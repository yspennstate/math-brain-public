Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO METRIC MOVEMENT:** H0022 `A_cyc(1+epsilon): UNMEASURED -> UNMEASURED`; supported substantive unchanged count `3 -> 4`; methods actually used: **#3 PROVE SOMETHING STRONGER, #8 DISCRETIZE, #30 ONE SCALE AT A TIME**. Because recovery 1 was already consumed, the next H0022 invocation is **STUCK_RECOVERY_2 / thinking-only**.

# R16 HARD OUTSIDE — H0022: matching-only overlaps are exponentially excluded at the fixed-M saddle

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Active source: H0022 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Section 1.6, Conjecture 1.5.

Source status after this run: **OPEN / PARTIAL METHOD PROGRESS**. The source metric does not move.

## 1. Continuity, ownership, exclusions, and current source

I continued from

`runs/R16/2026-09-18T04-45-30Z_h0022-stuck-recovery-1-binary-renewal-barrier_c1a9.md`

rather than restarting the stale native Beck--Fiala title, handed-off H0021, or the retired H0023 research lane.

Before new mathematics I reread/recovered the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `QUEUE.md`, the current H0022 exclusive claim, the newest own R16 report, the H-intake verification surface, the NEW-METHODS owner directive, and the newest neighboring H0023 final/handoff report. The H0022 claim remains `ADMITTED_ACTIVE / HARD_OUTSIDE` with R16 as exclusive owner. H0023 remains mathematically open but retired from its old P20 research lane after six unchanged runs; I do not import its unresolved perfect-completion or quenched-clustering obligations as black boxes.

A fresh bounded literature check on 2026-09-18 again recovered arXiv:2608.06358v1 as the current H0022 source and did not locate a later source-matching proof of Conjecture 1.5. The source still proves only a sufficiently-large-constant analogue, including universality at `C log n/n` for cycle factors of girth at least `100 log n/loglog n` for sufficiently large absolute `C`. This is dated bounded evidence, not a worldwide novelty certificate.

The frozen R16 metric remains:

`A_cyc(c)` = the smallest coefficient `A` for which R16 has a complete proof that `G(n,c log n/n)` is whp universal for every `n`-vertex cycle factor whose cycles all have length at least `A log n/loglog n`, with every restriction retained.

The source target is `A_cyc(1+epsilon) <= 1+epsilon` for every fixed `epsilon>0`.

Before: `UNMEASURED`. After: `UNMEASURED`.

## 2. Why the recovery's fixed-cut binary-rod ratio was only a toy deformation

The preceding thinking-only recovery isolated the toy coefficient

\[
\mathcal R_{n,k,j}
=
\frac{[z^j]F_k(z)^{n/k}}{\binom{n-j}{j}},
\qquad
F_k(z)=\sum_s\binom{k-s}{s}z^s,
\]

obtained by linearizing each target cycle with a **fixed cut** and asking a `1/2`-rod ordering to hit every prescribed multiple of `k`.

This run shows that the fixed cut is not the correct coefficient for the actual uniform-copy second moment. A cycle has no distinguished root. Its matching polynomial is

\[
C_\ell(z)
=
\lambda_+(z)^\ell+\lambda_-(z)^\ell,
\qquad
\lambda_\pm(z)=\frac{1\pm\sqrt{1+4z}}2,
\]

not the path polynomial `F_\ell`. For a cycle factor
\(H=C_{\ell_1}\cup\cdots\cup C_{\ell_m}\),

\[
\mathcal M_H(z)
=
\prod_{i=1}^m C_{\ell_i}(z).
\]

At the relevant activity `z=Theta(1/log n)`, and with every
\(\ell_i\ge A\log n/\log\log n\), `A>1`, the negative eigenvalue contribution is uniformly negligible. Thus the apparent accumulated fixed-boundary penalty in `F_k^{n/k}` is cancelled by the freedom to slide the cyclic roots.

This is a route correction, not a criticism of the previous recovery: that report explicitly labelled \(\mathcal R_{n,k,j}\) a toy deformation rather than a proved completion coefficient. The useful conclusion is that KLW-style renewal with *fixed* boundary cuts is not yet the right next calculation for H0022.

## 3. #8 DISCRETIZE — exact common-matching statistic

Work in the fixed-edge-count host model. Put

\[
N=\binom n2,\qquad
M=\left\lfloor c\frac{\log n}{n}N\right\rfloor,
\qquad
Q_s=\frac{(M)_s}{(N)_s}.
\]

Let \(F_0,F\) be independent uniform labelled copies of the same `n`-vertex cycle factor \(H\), and let

\[
K=|E(F_0)\cap E(F)|.
\]

The exact fixed-`M` second-moment kernel from the previous runs is

\[
W_n(j)=\frac{Q_{2n-j}}{Q_n^2}.
\]

For each `j`, let `Y_j` be the number of `j`-edge matchings contained in the common edge set \(E(F_0)\cap E(F)\). If `m_j(H)` is the number of `j`-edge matchings of \(H\), then a direct double count gives the exact identity

\[
\boxed{
\mathbb E Y_j
=
\frac{2^j j!\,m_j(H)^2}{(n)_{2j}}.
}
\tag{3.1}
\]

Proof. Condition on \(F_0\). It has exactly \(m_j(H)\) matching subsets `S`. For a fixed `j`-matching `S` on the host vertices, a uniform labelled copy \(F\) contains `S` with probability

\[
\frac{2^j j!\,m_j(H)}{(n)_{2j}}.
\]

Indeed, choose the preimage `j`-matching in \(H\), match its `j` edges to the `j` edges of `S`, choose the two orientations independently, and permute the remaining \(n-2j\) vertices. Summing over the matching subsets of \(F_0\) proves (3.1).

If

\[
\mathcal A_j
=
\{E(F_0)\cap E(F)\text{ is itself a matching of size }j\},
\]

then \(Y_j=1\) on \(\mathcal A_j\), so

\[
\Pr(\mathcal A_j)\le \mathbb E Y_j.
\tag{3.2}
\]

This turns a geometric overlap class into one exact scalar coefficient.

## 4. Uniform matching-polynomial bound at source girth

Write

\[
L=\log n,\qquad r=\frac jn.
\]

For \(z>0\), coefficient positivity gives

\[
m_j(H)\le z^{-j}\mathcal M_H(z).
\]

Choose the exact monomer-dimer saddle

\[
z=z(r)=\frac{r(1-r)}{(1-2r)^2}.
\]

Then

\[
\lambda_+(z)=\frac{1-r}{1-2r},
\qquad
\frac{|\lambda_-(z)|}{\lambda_+(z)}
=
\frac{r}{1-r}.
\]

Suppose every cycle of \(H\) has length at least

\[
k_{\min}\ge A\frac{L}{\log L}
\qquad(A>1\text{ fixed})
\]

and \(r=b/L\) with `b` in a fixed compact subset of `(0,infinity)`. The number of cycles is at most \(n/k_{\min}\), and therefore

\[
\mathcal M_H(z)
\le
\lambda_+(z)^n
\exp\!\left[
\frac{n}{k_{\min}}
\left(\frac{r}{1-r}\right)^{k_{\min}}
\right]
=
\lambda_+(z)^n\,e^{o(1)}
\tag{4.1}
\]

uniformly over **every** allowed cycle partition. The last equality uses

\[
\left(\frac{r}{1-r}\right)^{k_{\min}}
=
n^{-A+o(1)}.
\]

Consequently

\[
\log m_j(H)
\le
n h(r)+o(1),
\tag{4.2}
\]

where

\[
h(r)
=
(1-r)\log(1-r)
-r\log r
-(1-2r)\log(1-2r).
\]

This is the first point in the current second-moment route where the minimum-cycle hypothesis enters quantitatively and uniformly over the cycle type.

## 5. #3 PROVE SOMETHING STRONGER — matching-only overlaps cannot carry the natural saddle

The previous run predicted the weighted overlap scale

\[
j\asymp \frac nL,
\]

with formal saddle \(j\sim 2n/(cL)\). The following statement rules out the entire matching-only version of that saddle.

### Theorem 5.1 — uniform matching-only saddle exclusion

Fix `c>1`, `A>1`, and fixed constants `0<b_0<2/c<b_1<infinity`. Let \(H_n\) be **any** `n`-vertex cycle factor all of whose cycles have length at least \(A\log n/\log\log n\). Uniformly for integers

\[
j=\frac{bn}{L},
\qquad b\in[b_0,b_1],
\]

one has

\[
\frac1n
\log\!\left(
W_n(j)\,\mathbb E Y_j
\right)
\le
\frac{\Phi_c(b)}L
+
\frac{\Psi_c(b)}{L^2}
+
\frac{\Theta_c(b)}{L^3}
+
O\!\left(\frac1{L^4}\right),
\tag{5.1}
\]

where

\[
\Phi_c(b)
=
b\left(1+\log\frac{2}{bc}\right)-\frac2c,
\]

\[
\Psi_c(b)
=
-\left(b-\frac2c\right)^2,
\]

and

\[
\Theta_c(b)
=
-b^3-\frac{b^2}{c}
+\frac{8b}{c^2}
-\frac{28}{3c^3}.
\]

The leading function has its unique maximum at

\[
b_*=\frac2c,
\qquad
\Phi_c(b_*)=0,
\]

and simultaneously

\[
\Psi_c(b_*)=0,
\qquad
\Theta_c(b_*)
=
-\frac{16}{3c^3}.
\]

Hence, uniformly in the displayed saddle window,

\[
\boxed{
W_n(j)\Pr(\mathcal A_j)
\le
\exp\!\left[
-\left(\frac{16}{3c^3}+o(1)\right)
\frac{n}{(\log n)^3}
\right]
}
\tag{5.2}
\]

at the worst point, and therefore

\[
\boxed{
\sum_{b_0n/L\le j\le b_1n/L}
W_n(j)\Pr(\mathcal A_j)
=o(1).
}
\tag{5.3}
\]

In words: **pairs whose entire common-edge graph is a matching make a vanishing contribution to the fixed-`M` relative second moment throughout the only `Theta(n/log n)` window that can be the matching saddle.**

### Proof

By (3.1), (4.2), and Stirling with error `O(log n)`,

\[
\frac1n\log \mathbb E Y_j
\le
-rL
+r\left(1+\log\frac2r\right)
-r^2-r^3+O(r^4)
+o(L^{-3}).
\tag{5.4}
\]

For \(s\le2n\), expand

\[
\log(M)_s
=
s\log M+
\sum_{u=0}^{s-1}\log\left(1-\frac uM\right)
\]

through the cubic term. Since \(s/M=O(1/L)\), the summed quartic remainder is `O(n/L^4)`. The analogous finite-population corrections from `(N)_s` are only `O(1)` and are negligible on the `n/L^3` scale. Thus, uniformly for `r=O(1/L)`,

\[
\frac1n\log W_n(j)
=
r\log\frac NM
+
\sum_{q=1}^3
\frac{
2^q\left[2-(2-r)^{q+1}\right]
}{
q(q+1)c^qL^q
}
+
O(L^{-4}).
\tag{5.5}
\]

Also

\[
\log\frac NM
=
L-\log(cL)+o(L^{-3}).
\]

Substitute \(r=b/L\) in (5.4)--(5.5). The `+b` and `-b` terms cancel, as do the `log L` pieces. Collecting powers of `1/L` gives exactly (5.1).

Now

\[
\Phi_c'(b)=\log\frac{2}{bc},
\qquad
\Phi_c''(b)=-\frac1b<0,
\]

so \(\Phi_c\) has the unique maximum zero at \(b_*=2/c\). The `1/L^2` coefficient is already the negative square
\(-\left(b-2/c\right)^2\). At the sole point where the first two coefficients vanish, the third coefficient equals \(-16/(3c^3)\).

A compactness split away from \(b_*\), followed by Taylor expansion in a `1/L` neighborhood of \(b_*\), shows that the supremum of the right side of (5.1) is

\[
-\left(\frac{16}{3c^3}+o(1)\right)L^{-3}.
\]

Equation (3.2) then gives (5.2), and summing over at most `n` possible integers `j` gives (5.3), since \(n/L^3\gg\log n\). This proves the theorem.

## 6. Exact interpretation: adjacent runs are not a nuisance term; they are necessary

This theorem changes the route.

The preceding overlap-gas report found that at edge activity `Theta(1/L)` a typical selected subset has

\[
K=\Theta(n/L),
\qquad
K-R=\Theta(n/L^2),
\]

so almost every selected edge is isolated, but there are still `Theta(n/L^2)` adjacent selected-edge pairs.

It was tempting to treat those adjacent pairs as a perturbative nuisance and solve the matching-only completion first. Theorem 5.1 shows that this is backwards. If the fixed-`M` second moment has any order-one surviving mass in the natural saddle region, then the matching-only class cannot supply it. **The `Theta(n/L^2)` adjacent-run population is structurally required to repair the third-order deficit.**

This is an architecture result, not a proof of H0022. It says exactly which information a successful overlap enumeration may no longer discard.

A particularly suggestive interpretation is degree fluctuation. Two adjacent common edges share a vertex. Their contribution is therefore the first overlap statistic that sees the host's degree sequence rather than only its total edge count. Conditioning on `M` removes the global edge-count fluctuation; Theorem 5.1 strongly suggests that the next common fluctuation to remove or model is the degree sequence. I do **not** claim here that conditioning on the degree sequence closes the second moment; that is a new route candidate for the mandatory second recovery, not a theorem of this run.

## 7. #30 ONE SCALE AT A TIME — the next exact scale

The hierarchy now is:

1. `K=O(1)`: already exponentially suppressed after conditioning on `M`;
2. `K << n/(L log L)`: previous localization suppresses it;
3. `K=Theta(n/L)` but common graph a matching: Theorem 5.1 suppresses it by
   `exp[-Theta(n/L^3)]`;
4. the first unresolved overlap geometry is therefore
   \[
   K=\Theta(n/L),
   \qquad
   K-R=\Theta(n/L^2),
   \]
   i.e. a sea of isolated common edges plus a sparse but extensive population of length-two-or-longer common runs.

This gives the next displayed blocker:

\[
\boxed{
\text{evaluate the fixed-}M\text{ overlap weight jointly in }
(K,\;A),
\quad
A:=K-R,
\quad
K\asymp n/L,\ A\asymp n/L^2,
}
\tag{B2}
\]

with error `o(n/L^3)` if one wants to decide the sign at the matching saddle.

A `K`-only estimate cannot do this. The matching polynomial cannot do it. The fixed-cut binary renewal ratio cannot do it. One now needs either:

- a genuine two-parameter run enumeration at the true labelled-copy level; or
- a change of conditioning, most naturally from edge count to degree sequence, in which the adjacent-run contribution may be absorbed into the conditioned host law.

## 8. Exact checker

Only after the theorem was derived, I wrote one exact symbolic self-check. It verifies:

- the coefficients `Phi_c`, `Psi_c`, `Theta_c` through the required order;
- the simultaneous cancellation of the first two orders at `b=2/c`;
- the exact third-order value `-16/(3c^3)`;
- the fourth-order value `-16/c^4` at that same formal saddle;
- the exact cycle matching-polynomial identity
  `C_k(z)=lambda_+(z)^k+lambda_-(z)^k`
  for `3<=k<=12`;
- the path matching recurrence used to diagnose the fixed-cut toy deformation.

Files:

- `artifacts/R16/2026-09-18T05-42-30Z_h0022_matching_overlap_expansion_checker.py`
- `artifacts/R16/2026-09-18T05-42-30Z_h0022_matching_overlap_expansion_checker.out`

The archived output ends `ALL_EXACT_CHECKS_PASS`.

This checker is a self-check, not an independent audit. The all-`n` theorem is the written argument above.

## 9. Literature positioning

The closest methodological relative remains Kahn--Lubetzky--Wormald, *Cycle factors and renewal theory* (CPAM 2017; arXiv:1401.2707). Their second moment also organizes common paths/runs and uses renewal without replacement. The present calculation does not claim that overlap-run enumeration is new.

The relevant correction is narrower: in the H0022 fixed-`M` setting at the source-scale activity, the fixed-cut path renewal from the previous recovery is not the actual uniform-copy coefficient, and matching-only common intersections are exponentially insufficient at the natural saddle. I found no source in the bounded searches stating this exact uniform fixed-`M` saddle exclusion for all cycle types of girth `A log n/loglog n`; this negative search is not a novelty certificate.

A fresh source check still finds Cohen Antonir--Lichev--Zhukovskii v1 (6 August 2026) as the current H0022 primary source.

## 10. Beck--Fiala title refresh

The native scheduler title is now stale as a research target.

Guo--Fang--Lu, arXiv:2609.11189v1 (10 September 2026), state a real Komlós bound \(3\sqrt{2\pi}\). In particular they explicitly deduce that every set system in which each element lies in at most `t` sets has discrepancy

\[
\operatorname{disc}<3\sqrt{2\pi t}
\]

for every integer `t>=1`, with no `n` restriction.

On 17 September 2026, Karingula--Lovett posted ECCC TR26-188, *An elementary proof of the Komlos conjecture*, proving the dimension-free constant `36` by a separately authored simplification of the Guo--Fang--Lu proof. Scaling an incidence matrix by `1/sqrt(t)` gives the complete uniform consequence

\[
B(t,n)\le36\sqrt t
\]

for every `t,n`.

These are very recent preprint/technical-report claims rather than mature refereed consensus, but they are stronger than Beck--Fiala and remove the old all-`t` gap that motivated the stale task title. R16 therefore remains on its admitted HARD successor H0022 rather than pretending the native title is still unresolved.

## 11. Stuck accounting and mandatory next action

The H0022 metric still does not move.

- Supported substantive unchanged count before this run: `3`.
- After this substantive run: `4`.
- HARD recovery already consumed on H0022: `1 of 2`.

The current run did change the mathematical blocker: the fixed-cut binary renewal deformation is not the real coefficient, and the matching-only saddle is now ruled out. Nevertheless the source metric remains unchanged after the first recovery. Under the owner's HARD protocol, the **next invocation is STUCK_RECOVERY_2 / thinking-only**; there will be no third H0022 recovery.

The second recovery should use a nonrepeating, previously unused triple:

- **#12 FIND WHAT IS CONSERVED:** test whether conditioning on the full degree sequence removes the `A=Theta(n/L^2)` adjacent-run fluctuation;
- **#15 BREAK THE SYMMETRY ON PURPOSE:** compare equal-cycle targets with deliberately irregular long-cycle partitions under degree conditioning, rather than assuming the equal type is worst for concentration;
- **#22 READ THE FAILURES, NOT THE SUCCESSES:** inspect sparse Hamilton/2-factor second-moment failures and small-subgraph-conditioning arguments specifically for the degree-sequence fluctuation that survives edge-count conditioning.

The recovery must choose exactly one of the Section-I actions. The preferred action, if the literature and exact calculation support it, is **port the nearest solved technique** at the level of degree-conditioned configuration models; otherwise it should hand off the second-moment route rather than manufacture another overlap lemma.

## 12. Scheduler/model control

The exposed task-control surface still has title/prompt, schedule or relative start, timing mode, enablement, and task identity, but no binding model-family field, no reasoning-effort field, and no authenticated applied-model receipt. Therefore GPT-6/maximum remains prompt-only here. Enforcing it requires an authorized scheduler/API surface exposing those selectors plus runtime telemetry.

The historical P26 `You cannot modify this task` failure was authorization-context-specific; repository reconciliation records a later successful P26 update from an authorized context. For a task that still returns that error, the compliant workaround is the owning workspace/account context or platform support, not task duplication or permission bypass.

No scheduler state, shared root ledger, peer file, email, Drive content, public post, purchase, permission, or workflow was changed.

```yaml
ledger_delta:
  track: R16
  lane: HARD_OUTSIDE
  active_target: H0022
  source: "Cohen Antonir--Lichev--Zhukovskii, arXiv:2608.06358v1, Conjecture 1.5"
  source_status: OPEN
  research_status: PARTIAL
  metric: "A_cyc(1+epsilon)"
  before: UNMEASURED
  after: UNMEASURED
  movement: false
  substantive_unchanged_before: 3
  substantive_unchanged_after: 4
  hard_recoveries_used: 1
  methods: [3, 8, 30]
  new_results:
    - "exact common-matching factorial-moment identity"
    - "uniform source-girth cycle-matching-polynomial saddle bound"
    - "Theorem 5.1: matching-only overlaps are exponentially negligible at the fixed-M natural saddle"
    - "correction: fixed-cut binary-rod ratio is a toy deformation, not the actual cyclic completion coefficient"
    - "next unresolved geometry isolated at K=Theta(n/log n), K-R=Theta(n/log^2 n)"
  artifacts:
    - artifacts/R16/2026-09-18T05-42-30Z_h0022_matching_overlap_expansion_checker.py
    - artifacts/R16/2026-09-18T05-42-30Z_h0022_matching_overlap_expansion_checker.out
  shared_roots_edited: false
  peer_files_edited: false
  scheduler_changed: false
  next_required_mode: STUCK_RECOVERY_2_THINKING_ONLY
  next_methods: [12, 15, 22]
```
