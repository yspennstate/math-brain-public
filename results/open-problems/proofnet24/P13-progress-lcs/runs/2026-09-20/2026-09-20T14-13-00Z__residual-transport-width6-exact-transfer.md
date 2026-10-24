Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# P13 / T02 — residual transport: exact semigroup smoothing and every-horizon finite-to-infinite transfer

## 0. Before / after, separated by level

### Source-level binary Chvatal–Sankoff interval

The target is
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. All strip transitions below use the same incoming `Y` bit throughout a column. Independent Bernoulli matching is not used.

The preceding P13 report carried the repository-internal interval
\[
L\le \gamma_2\le U_{new},\qquad L=0.792665992=\frac{99083249}{125000000},
\]
where `U_new` was the endpoint from P02's `2026-09-20T10-03-15Z__matched-successor-defect-report.md`.

The newest completed P02 companion report now visible on `master` is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T13-10-25Z__padic-type01-dual-report.md`, blob `d10e71314c3a2c50612fed3dd660718ebfb870c4`.

That report calls the same 10:03 endpoint `U_prev` and proves a stricter p-adic type-0/type-1 endpoint `U_01<U_prev`, with exact separator
\[
\boxed{
U_{01}<0.82627594276228262501510658153729663282346199619319002388080618331256294443029<U_{new}.
}
\]
Therefore the source-level interval strictly shrinks in the combined P02/P13 program from
\[
[L,U_{new}]\quad\hbox{to}\quad\boxed{[L,U_{01}]}.
\]
This source movement is **P02-derived** and is not attributed to the width-six computation below.

Fresh source navigation rechecked Alexander Tiskin, `arXiv:2212.01582v2`: v2 was revised 2024-08-13; the binary coefficient remains unresolved; the arXiv comments explicitly say erroneous claims in the original preprint about the stochastic process and `gamma` were removed. The retained rigorous public lower endpoint is `0.792665992` from Heineman–Miller–Reichman–Salls–Sarkozy–Soiffer, `arXiv:2407.10925`.

### P13 mechanism-level movement

The previous P13 report proved a 60-block Cesaro Bellman interval for the genuine dependent width-six strip of exact width
\[
\varepsilon^{Ces}_{60}=
\frac{3183344437055150847758447502072126641}
{159507359494189904748456847233641349120000000000000000000}
=1.99573514798927\ldots\times 10^{-20}.
\]

This run switches to a genuinely different semigroup mechanism: **transport the Bellman residual itself by `P^k` and absorb the transport as a coboundary into a new potential.** For `k=62` the exact certified interval width is
\[
\boxed{
\varepsilon^{tr}_{62}=
\frac{213199680345696880030747176466855}
{8000000000000000000\cdot21267647932558653966460912964485513216}
}
\]
\[
=1.25307509921742081569982718974\ldots\times10^{-24}.
\]
It is strictly nested inside the previous 60-block interval. The exact width-improvement factor is
\[
\boxed{
\frac{\varepsilon^{Ces}_{60}}{\varepsilon^{tr}_{62}}
=
\frac{50933510992882413564135160033154026256}
{3197995205185453200461207647002825}
=15926.7002371658\ldots .
}
\]
Relative to the original one-step residual width `7/(8e18)`, the new interval is smaller by a factor `698282.170435...`.

The new finite-to-infinite transfer works for **every horizon `N`**, not only horizons divisible by the smoothing length.

Status: **PARTIAL / source OPEN / exact internal candidate pending later independent review and public-priority checking.**

## 1. Scope, continuity, exclusions, and handoff

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns P13 to T02 dependence-preserving boundary recursion, complementary to P02's stationary/variational upper route.

Necessary continuity only was used: the preceding P13 report

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T13-12-00Z__cesaro-block-transfer-and-carry-quotient.md`, blob `827ea6f66deca092cee69139c9697710c59e0205`,

the newest completed P02 report above, the exact width-six checker dependency, and current source records. No whole-repository reread was performed.

Root `POSTED.md` had already been checked in the immediately preceding T02 companion work; no posting exclusion covers T02. No historical or peer file was overwritten.

Short actual pre-LIVE20 P13 successor handoff is preserved: P0342 had already been terminally handed off at frozen `2/2`; the later P0205 screen admitted no successor because its source notation `tau(infinity)` could not be frozen source-faithfully. Retired I0051/clade work remains retired and was not reopened.

No email, Drive, public posting, paid compute, permission, schedule, or peer-history change was made.

## 2. Genuine dependent strip recursion

Fix half-width `w`, put `m=2w`, and write a formal strip state as
\[
s=(x,g),\qquad x,g\in\{0,1\}^m.
\]
Set `V_0=0`, `V_k=sum_{i<=k} g_i`. For one fresh actual source pair `(u,v)`, define
\[
a_i={\bf1}_{\{x_{i+1}=v\}}\quad(0\le i<m),\qquad a_m={\bf1}_{\{u=v\}}.
\]
The same `v` appears in every `a_i` in the column. The exact DP update is
\[
Q_0=\max\{V_1,V_0+a_0\},
\]
\[
Q_k=\max\{Q_{k-1},V_k+a_k,V_{k+1}\},\qquad1\le k<m,
\]
\[
Q_m=\max\{Q_{m-1},V_m+a_m\},
\]
with
\[
x'=(x_2,\ldots,x_m,u),\qquad g'_k=Q_k-Q_{k-1},
\]
and central reward
\[
\rho(s;u,v)=Q_w-V_w\in\{0,1\}.
\]
Equivalently the carry recursion is
\[
d_i=(1-g_i)\bigl(d_{i-1}\vee {\bf1}_{\{x_i=v\}}\bigr).
\]
This shared-column `v` is retained in the executed checker.

## 3. New theorem: residual transport is an exact Bellman certificate

Let `R` be a finite closed Markov reward class, `P` its transition kernel, `r` its one-step mean reward, `gamma` its stationary mean, and `h` any potential. Define the Bellman residual
\[
\delta_h:=r+Ph-h.
\]
For integer `k>=0`, define the transported potential
\[
\boxed{
 h^{[k]}:=h+\sum_{j=0}^{k-1}P^j\delta_h,
}
\tag{3.1}
\]
where the empty sum is zero.

### Theorem 3.1 — exact residual transport identity

For every `k>=0`,
\[
\boxed{
r+Ph^{[k]}-h^{[k]}=P^k\delta_h.}
\tag{3.2}
\]
Consequently, putting
\[
\ell_k:=\min_R P^k\delta_h,
\qquad
u_k:=\max_R P^k\delta_h,
\qquad
\varepsilon_k:=\nu_k-\ell_k,
\]
we have
\[
\boxed{\ell_k\le\gamma\le\nu_k.}
\tag{3.3}
\]
Moreover for every state `s` and **every** integer horizon `N>=1`, if
\[
A_N(s):=\frac{\mathbf E_sR_N}{N},
\]
then
\[
\boxed{
A_N(s)-\varepsilon_k-
\frac{h^{[k]}(s)-\min h^{[k]}}N
\le\gamma\le
A_N(s)+\varepsilon_k+
\frac{\max h^{[k]}-h^{[k]}(s)}N.
}
\tag{3.4}
\]
In particular, at a minimizer `s_-^{[k]}` and maximizer `s_+^{[k]}` of the transported potential,
\[
\boxed{
\gamma\ge A_N(s_-^{[k]})-\varepsilon_k,
\qquad
\gamma\le A_N(s_+^{[k]})+\varepsilon_k
}
\tag{3.5}
\]
for every `N`, with no `1/N` boundary loss.

### Proof

From (3.1),
\[
\begin{aligned}
r+Ph^{[k]}-h^{[k]}
&=(r+Ph-h)+(P-I)\sum_{j=0}^{k-1}P^j\delta_h\\
&=\delta_h+\sum_{j=1}^{k}P^j\delta_h-
\sum_{j=0}^{k-1}P^j\delta_h\\
&=P^k\delta_h.
\end{aligned}
\]
This proves (3.2). Stationarity gives `pi P^k=pi`, so
\[
\pi(P^k\delta_h)=\pi\delta_h=\pi r=\gamma,
\]
which lies between the minimum and maximum, proving (3.3).

Now apply the already-proved bias-extremal telescoping argument to the one-step Bellman certificate `(h^{[k]},P^k delta_h)`. Summing the inequalities
\[
\ell_k\le r+Ph^{[k]}-h^{[k]}\le\nu_k
\]
along the original chain for `N` steps gives the boundary terms in (3.4). At a potential extremizer the corresponding one-sided boundary term vanishes, giving (3.5). No divisibility condition on `N` appears because this is a one-step coboundary transformation of the original chain, not a `k`-step block chain. QED.

### Corollary 3.2 — monotone span contraction

For every bounded `f`, `span(Pf)<=span(f)`. Hence `epsilon_{k+1}<=epsilon_k`. If a length-`q` actual source word has probability `p` and maps every state to one common state, then
\[
\boxed{\operatorname{span}(P^qf)\le(1-p)\operatorname{span}(f).}
\tag{3.6}
\]
Indeed `P^q(s,\cdot)=p\delta_z+(1-p)K_s` for the common reset state `z`, so the common mass cancels in pairwise expectation differences.

For the width-six strip, the inherited true-source reset word `A^{12}`, `A=(0,1)`, has `p=4^{-12}`. Therefore the exact `k=62` width below implies the all-future analytic tail
\[
\boxed{
\varepsilon_{62+12j}\le
\left(1-4^{-12}\right)^j\varepsilon_{62},\qquad j\ge0.
}
\tag{3.7}
\]
This uses an actual shared-source synchronizer, not independent match entries.

## 4. Exact width-six `k=62` certificate

The inherited exact width-six potential uses integer scale
\[
Q=2\cdot10^{18}
\]
and integer Bellman numerators
\[
D_H(s)=Q\sum_{a=1}^4\rho(s,a)+\sum_{a=1}^4H(T_as)-4H(s).
\]
The exact baseline scan is
\[
d_-=6238638445311257066,
\qquad d_+=6238638445311257073.
\]
Put
\[
e(s)=D_H(s)-d_-\in\{0,\ldots,7\}.
\]
Then
\[
\delta_h(s)=\frac{d_-}{4Q}+\frac{e(s)}{4Q}.
\]

For residual transport define exact integers
\[
\boxed{F_k(s)=4^kP^ke(s).}
\tag{4.1}
\]
Because the four actual source pairs are equiprobable,
\[
\boxed{F_{k+1}(s)=\sum_{a=1}^4F_k(T_as),\qquad F_0=e.}
\tag{4.2}
\]
No floating arithmetic enters (4.2). Floating iteration is used only to reconstruct the already-frozen candidate `H`; the program then re-verifies the inherited exact baseline `d_-,d_+` before using it.

At `k=62`, exact 128-bit propagation over all `5,735,086` recurrent states gives
\[
4^{62}=21267647932558653966460912964485513216,
\]
\[
F_{62}^{\min}=46187259153232832797578610832579588314,
\]
\[
F_{62}^{\max}=46187472352913178494458641579756055169,
\]
and hence
\[
\boxed{
F_{62}^{\max}-F_{62}^{\min}
=213199680345696880030747176466855.
}
\]
Thus
\[
\boxed{
\ell^{tr}_{62}=\frac{d_-}{8\cdot10^{18}}+
\frac{46187259153232832797578610832579588314}
{8\cdot10^{18}\,4^{62}},
}
\tag{4.3}
\]
\[
\boxed{
\nu^{tr}_{62}=\frac{d_-}{8\cdot10^{18}}+
\frac{46187472352913178494458641579756055169}
{8\cdot10^{18}\,4^{62}}.
}
\tag{4.4}
\]
Diagnostic decimals are
\[
\ell^{tr}_{62}=0.779829805663907133521464311072950927\ldots,
\]
\[
\nu^{tr}_{62}=0.779829805663907133521465564148050145\ldots.
\]
The proof uses (4.3)–(4.4), not decimal subtraction.

### Strict nesting inside the preceding 60-block interval

The preceding report had
\[
E_{60}^{\min}=41924395640042677859658223559910276214,
\]
\[
E_{60}^{\max}=45107740077097828707416671061982402855,
\]
with Cesaro denominator `60*4^59`. Since `4^62=64*4^59`, exact cross-multiplication gives
\[
60F_{62}^{\min}-64E_{60}^{\min}
=88074228231238584836590342120517621144>0,
\]
\[
64E_{60}^{\max}-60F_{62}^{\max}
=115647023759470327607148453181510472580>0.
\]
Therefore both endpoints move inward:
\[
\boxed{
\ell^{Ces}_{60}<\ell^{tr}_{62}<\nu^{tr}_{62}<\nu^{Ces}_{60}.
}
\tag{4.5}
\]
This is a strict certified interval shrink, not merely a smaller displayed decimal width.

The exact checker additionally verifies monotone normalized span contraction at every propagated step and ends `ALL_EXACT_CHECKS_PASS`.

## 5. Finite-to-infinite consequence and what it does not prove

Let `h^{[62]}` be (3.1) constructed from the exact width-six residual. For every horizon `N`,
\[
\boxed{
\gamma_6\ge
\frac{\mathbf E_{s_-^{[62]}}R_N}{N}
-\varepsilon^{tr}_{62},
}
\tag{5.1}
\]
where `s_-^{[62]}` minimizes the transported potential. The analogous upper inequality holds from its maximizer. For arbitrary starts, (3.4) supplies the explicit transported-potential boundary term.

This is a proved finite-to-infinite transfer. A finite computation without (3.4)/(5.1) is not promoted to a statement about `gamma_6` or `gamma_2`.

However, the width-six constant itself remains near `0.77982980566`, rigorously below the retained source lower endpoint `L=0.792665992`. Therefore this P13 sharpening does **not** improve the source lower endpoint. Its role is to remove essentially all residual-certification slack from width six and to supply a stronger bias object for the next-width lift.

## 6. Obstruction, failure accounting, and next attack

The preceding raw width-seven projection route remains decisively obstructed: `64,202` projected states lie outside `R_6`, and deterministic peeling leaves a `2,706`-state persistent outsider core. This run deliberately does **not** repeat that failed projection calculation. It executes a different semigroup/coboundary method, as required after repeated work near the same lift obstruction.

Residual transport succeeds strongly at its own target but exposes the remaining source bottleneck more cleanly: interval-certification error at width six is no longer material, while the width-six value itself is too small. Pushing `k` beyond 62 would only polish an already irrelevant width-six endpoint and is not the next research priority.

**Next attack:** lift the *transported* width-six potential/residual, not the raw bias, through the exact width-seven carry quotient from the preceding report. The transported residual has oscillation only `1.2531e-24`; use the carry signature plus the sparse outsider class to ask whether a local correction can preserve a lower residual above `L` without full width-seven value iteration. If the required correction still depends on the large quotient rather than the `2,706` exceptional core, terminate this recovery route and execute the preserved distinct event-specific mixed-terminal-suffix coupling.

## 7. Essential executed artifacts

1. Exact checker source:
   `proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T14-05-30Z__w6_residual_transport62.cpp`
   creation commit `0c449fe745585fad4538c040164556ba74833b05`.

2. Actual checker stdout:
   `proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T14-06-00Z__w6_residual_transport62.out`
   creation commit `3246c620de1c542f1b64e6b4643ee4f1d4251e47`.

The executed output records the exact baseline residual, all selected transport steps through `k=62`, the final exact numerator/denominator, strict one-step nesting margins, and ends `ALL_EXACT_CHECKS_PASS`.

## 8. ledger_delta

```text
ledger_delta:
  slot: P13
  target: T02 binary Chvatal-Sankoff gamma_2, iid uniform binary strings
  source_before: [L, U_new]   # P02 10:03 matched-successor endpoint
  source_after:  [L, U_01]    # P02 13:10 p-adic type-0/type-1 endpoint
  source_gain: strict U_01 < U_new; companion-derived, not attributed to P13 strip computation
  p13_interval_before: width-6 Cesaro-60 Bellman width 1.99573514798927e-20
  p13_interval_after: width-6 residual-transport k=62 width 1.25307509921742e-24
  p13_gain_factor: 15926.7002371658... exact ratio recorded above
  new_theorem: h^[k]=h+sum_{j<k}P^j delta has one-step residual P^k delta; stationary interval and bias-extremal finite-to-infinite transfer hold for every N
  dependence_check: same incoming Y bit reused through each whole strip column; no independent Bernoulli matching
  exact_states: 5735086
  exact_k: 62
  exact_spread_num: 213199680345696880030747176466855
  reset_tail: epsilon_{62+12j} <= (1-4^-12)^j epsilon_62 from actual A^12 synchronizer
  obstruction: gamma_6 itself remains rigorously below L; width-7 raw projection still has 2706 persistent outsiders
  next_attack: carry-quotient lift of transported potential/residual; if nonlocal, switch to event-specific mixed-suffix coupling
  status: PARTIAL / source OPEN / full candidates pending later independent review
```
