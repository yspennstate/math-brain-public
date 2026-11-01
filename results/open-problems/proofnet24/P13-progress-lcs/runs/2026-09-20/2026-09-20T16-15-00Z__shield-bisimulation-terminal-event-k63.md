Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise.**

# P13 / T02 — leading-one shield bisimulation and strict k=63 terminal-event contraction

## 0. Before / after, separated by level

### Source-level binary Chvátal–Sankoff interval

The target remains
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. Every strip transition below uses one actual incoming `Y` bit across the entire column. Independent Bernoulli matching is not substituted.

The previous P13 report carried the companion-derived source interval
\[
\boxed{L\le \gamma_2\le U_{tail}},\qquad
L=0.792665992=\frac{99083249}{125000000}.
\]
A fresh read of the P02 run directory found no completed companion report later than

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T15-04-28Z__mixed-modulus-exact-tail-dual-report.md`,

which proves `U_tail<U_mm`. Therefore the source-level interval is **unchanged in this invocation**:
\[
\boxed{[L,U_{tail}]\to[L,U_{tail}].}
\]
I do not relabel the width-six computation below as a source improvement, because `gamma_6<L` and `gamma_6<=gamma_2` only yields a weaker lower bound than `L`.

Fresh source navigation also rechecked Alexander Tiskin, `arXiv:2212.01582v2`: the arXiv record still describes the binary coefficient as unresolved; v2 is dated 2024-08-13 and explicitly says the earlier incorrect claims about the stochastic process / `gamma` were removed. The public lower endpoint `0.792665992` is the Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer bound `arXiv:2407.10925`.

### P13 mechanism-level movement

The preceding P13 run introduced the exact terminal-gradient coboundary
\[
r+P\phi-\phi=1-g_m,
\qquad
\phi=\sum_{i=w+1}^{m-1}g_i+2g_m,
\qquad m=2w,
\]
and the event interval
\[
I_k=[1-b_k,1-a_k],\qquad
a_k=\min_sP^kg_m(s),\quad b_k=\max_sP^kg_m(s).
\]
It proposed output-preserving Moore reduction as the next attack.

This run executes that genuinely different automaton route and proves an explicit all-width **shield bisimulation**: if the gradient begins with `ell` ones, the first `ell` raw `X` bits are completely invisible to the entire future terminal-gradient trace. Canonicalizing by deleting exactly those shielded raw bits is a deterministic output bisimulation for the four genuine source-pair transitions.

At width six this quotient reduces the recurrent class from
\[
5,735,086\quad\hbox{to}\quad4,484,525
\]
states, collapsing `1,250,561` states (`21.8054...%`) while preserving every future source-word trace of `g_m` exactly. On that quotient the exact `k=63` event propagation strictly nests inside the preceding `k=62` interval:
\[
\boxed{I_{63}\subsetneq I_{62}}.
\]
The interval width drops from
\[
0.0020643482893085716\ldots
\]
to
\[
\boxed{0.0018993954436775286\ldots},
\]
a `7.990553...%` reduction (old/new factor `1.086844920145574...`).

Status: **PARTIAL / source OPEN / exact internal theorem and computation pending later independent review.**

## 1. Scope, continuity, exclusions, and handoff

Controlling policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns P13 to T02 dependence-preserving boundary recursion, complementary to P02's stationary/variational upper route.

Necessary continuity only was read: the latest P13 report, the latest completed P02 companion report, the governing policy, root `POSTED.md`, and the current Tiskin / lower-bound sources. Root `POSTED.md` contains no T02 posting exclusion. No whole-repository reread was performed.

Short actual pre-LIVE20 P13 successor handoff is preserved: P0342 had already been terminally handed off at frozen `2/2`; the later P0205 screen admitted no successor because its source notation `tau(infinity)` could not be frozen source-faithfully. Retired I0051/clade work remains retired and was not reopened.

No email, Drive, public posting, paid compute, workflow, permission, peer-history, historical-claim, or schedule change was made.

## 2. Genuine dependent strip recursion

Fix half-width `w`, set `m=2w`, and write a formal strip state
\[
s=(x_1,\ldots,x_m;g_1,\ldots,g_m),\qquad x_i,g_i\in\{0,1\}.
\]
For one fresh actual source pair `(u,v)`, define the shared-column carry
\[
d_0^{(v)}=0,
\qquad
d_i^{(v)}=(1-g_i)\left(d_{i-1}^{(v)}\vee {\bf1}_{\{x_i=v\}}\right).
\tag{2.1}
\]
The same `v` is used at every site in the column. The gradient update is
\[
g'_i=g_{i+1}+d_{i+1}^{(v)}-d_i^{(v)},\qquad 1\le i<m,
\tag{2.2}
\]
\[
g'_m=(1-d_m^{(v)}){\bf1}_{\{u=v\}},
\tag{2.3}
\]
and the raw window shifts as
\[
x'=(x_2,\ldots,x_m,u).
\tag{2.4}
\]
The central reward is
\[
\rho(s;u,v)=g_{w+1}+d_{w+1}^{(v)}.
\tag{2.5}
\]
Let `T_a` denote the deterministic transition for one of the four equiprobable source pairs `a=(u,v)` and let `P` be their average.

## 3. New theorem: leading-one raw bits are an exact output shield

For a state `s=(x,g)`, let
\[
\ell(s):=\max\{j\in\{0,\ldots,m\}:g_1=\cdots=g_j=1\}
\]
(the length of the initial run of gradient ones). Define the canonicalization `C` by keeping `g` fixed and replacing
\[
x_1,\ldots,x_{\ell(s)}
\]
by zero, leaving the remaining raw bits unchanged.

### Theorem 3.1 — shield bisimulation

For every `m`, every state `s`, and every source pair `a`,
\[
\boxed{g_m(s)=g_m(C(s))}
\tag{3.1}
\]
and
\[
\boxed{C(T_as)=C(T_aC(s)).}
\tag{3.2}
\]
Consequently `s` and `C(s)` have identical terminal-gradient output traces under **every finite or infinite actual source-pair word**, and therefore
\[
\boxed{P^kg_m(s)=P^kg_m(C(s))\quad\hbox{for all }k\ge0.}
\tag{3.3}
\]

**Proof.** Put `ell=ell(s)` and compare `s` with `t=C(s)`. They have identical gradients and identical raw bits after position `ell`.

If `ell<m`, then for every `i<=ell`, equation (2.1) gives `d_i^{(v)}=0` in both states because `g_i=1`. Starting from the common value `d_ell=0`, the carry recursion for positions `ell+1,...,m` sees identical `x_i,g_i`, hence all later carries agree. Therefore every updated gradient coordinate agrees. For `i<ell`, explicitly,
\[
g'_i=g_{i+1}+0-0=1.
\]
The shifted raw windows can differ only in positions `1,...,ell-1`, because the old differences were confined to `1,...,ell`. But the updated gradient has ones in all those positions, so the next canonicalization deletes every remaining raw difference. Thus (3.2) holds.

If `ell=m`, all old gradients are one, hence every carry in (2.1) is zero. Equations (2.2)--(2.3) give `g'_1=...=g'_{m-1}=1` and `g'_m=1_{u=v}`, independently of all old raw bits. After the shift, all old raw differences lie in positions `1,...,m-1`, again shielded by leading gradient ones and erased by `C`. This proves (3.2) also in the all-one case.

Equation (3.1) is immediate because `C` never changes `g`. Induction on the input word length now gives identical output traces, hence (3.3). QED.

This theorem is dependence-preserving: it is proved directly from the shared-column carry recurrence (2.1), not from independent match indicators.

### Corollary 3.2 — explicit all-formal quotient-size upper bound

For a fixed `ell<m`, there are `2^{m-ell-1}` gradient words whose initial run of ones has exact length `ell`, and after canonicalization only `m-ell` raw bits remain free. Thus the number of canonical formal states is
\[
1+\sum_{\ell=0}^{m-1}2^{m-\ell-1}2^{m-\ell}
=1+\sum_{r=1}^{m}2^{2r-1}
=\boxed{\frac{2\,4^m+1}{3}}.
\tag{3.4}
\]
This is an **upper bound on the minimal Moore quotient size**, not a claim that no further equivalences exist.

The important point operationally is that the canonicalization is closed under all four source-pair transitions, so no iterative partition refinement is required to use it.

## 4. Exact recurrent width-six quotient

The inherited reset argument makes the class reachable from the zero state the unique recurrent width-six class. The new checker regenerates this class using (2.1)--(2.4), obtaining the inherited exact size
\[
|R_6|=5,735,086.
\]
Canonicalizing every recurrent state by Theorem 3.1 gives
\[
\boxed{|C(R_6)|=4,484,525},
\]
so
\[
\boxed{1,250,561}
\]
recurrent states collapse, a fraction
\[
\frac{1,250,561}{5,735,086}=0.2180544459\ldots.
\]
The checker then verifies all
\[
4|R_6|=22,940,344
\]
state/source-pair transitions against the quotient representatives. Every output bit and every canonical successor agrees.

This is a demonstrated exact mechanism gain: terminal-event propagation can be performed on `4,484,525` states rather than `5,735,086`, a state-count speed/memory factor of
\[
\frac{5,735,086}{4,484,525}=1.2788614\ldots.
\]
It is not yet enough by itself to make width seven small; see the obstruction below.

## 5. Finite-to-infinite transfer retained on the quotient

The preceding run proved pointwise on the genuine strip
\[
\boxed{r+P\phi-\phi=1-g_m},
\qquad
\phi=\sum_{i=w+1}^{m-1}g_i+2g_m.
\tag{5.1}
\]
For every `k>=0`, define
\[
\phi^{[k]}:=\phi+\sum_{j=0}^{k-1}P^j(1-g_m).
\]
Then exactly
\[
\boxed{r+P\phi^{[k]}-\phi^{[k]}=1-P^kg_m.}
\tag{5.2}
\]
Because Theorem 3.1 preserves `P^kg_m` exactly, (5.2) may be evaluated on the shield quotient without changing its residual extrema.

Let
\[
a_k=\min_{R_w}P^kg_m,\qquad b_k=\max_{R_w}P^kg_m,
\qquad\varepsilon_k=b_k-a_k.
\]
Stationarity of (5.2) gives the exact finite-computation-to-asymptotic transfer
\[
\boxed{1-b_k\le\gamma_w\le1-a_k.}
\tag{5.3}
\]
No finite enumeration is called a bound on `gamma_w` or `gamma_2` without this coboundary step.

For a finite reward horizon `N`, Bellman telescoping also gives
\[
\boxed{
A_N(s)-\varepsilon_k-
\frac{\phi^{[k]}(s)-\min\phi^{[k]}}N
\le\gamma_w\le
A_N(s)+\varepsilon_k+
\frac{\max\phi^{[k]}-\phi^{[k]}(s)}N,
}
\tag{5.4}
\]
where `A_N(s)=E_s R_N/N`. At a minimizer/maximizer of `phi^[k]`, the corresponding one-sided `1/N` term vanishes. Thus `epsilon_k` is itself a certified finite-to-infinite error at the bias-extremal starts.

## 6. New exact k=63 contraction

The checker propagates
\[
F_k(s):=4^kP^kg_m(s)
\]
on the exact shield quotient by
\[
F_{k+1}(s)=\sum_{a=1}^{4}F_k(T_as).
\tag{6.1}
\]
All proof arithmetic is integer arithmetic.

The inherited `k=62` extrema are reproduced exactly:
\[
4^{62}=21267647932558653966460912964485513216,
\]
\[
F_{62}^{\min}=4663938790599173885795905174720472033,
\]
\[
F_{62}^{\max}=4707842623226368321561270898837713032.
\]

At `k=63` the new exact extrema are
\[
\boxed{4^{63}=85070591730234615865843651857942052864},
\]
\[
\boxed{F_{63}^{\min}=18661685132879679887906041038442426427},
\]
\[
\boxed{F_{63}^{\max}=18823267827203038766451944367208833376}.
\]
Therefore
\[
\boxed{
I_{63}=
\left[
\frac{2070228871969736784355990859085413109}
{2658455991569831745807614120560689152},
\frac{66408906597354935977937610819499626437}
{85070591730234615865843651857942052864}
\right]
}
\tag{6.2}
\]
or diagnostically
\[
I_{63}\approx[0.7787335500510791,\ 0.7806329454947567].
\]
Its exact width is
\[
\boxed{
\varepsilon_{63}=
\frac{161582694323358878545903328766406949}
{85070591730234615865843651857942052864}
=0.0018993954436775286\ldots .
}
\tag{6.3}
\]

Both endpoints move inward strictly. On the common denominator comparison,
\[
4F_{62}^{\max}-F_{63}^{\max}
=\boxed{8102665702434519793139228142018752}>0,
\tag{6.4}
\]
which moves the lower endpoint upward, and
\[
F_{63}^{\min}-4F_{62}^{\min}
=\boxed{5929970482984344722420339560538295}>0,
\tag{6.5}
\]
which moves the upper endpoint downward. The width comparison is
\[
4(F_{62}^{\max}-F_{62}^{\min})-(F_{63}^{\max}-F_{63}^{\min})
=\boxed{14032636185418864515559567702557047}>0.
\tag{6.6}
\]
Hence
\[
\boxed{I_{63}\subsetneq I_{62}}.
\]
The exact old/new width ratio is
\[
\boxed{
\frac{175615330508777743061462896468963996}
{161582694323358878545903328766406949}
=1.086844920145574\ldots .
}
\tag{6.7}
\]

The archived executable output ends `ALL_EXACT_CHECKS_PASS`.

## 7. Failure accounting, obstruction, and next attack

The output-preserving automaton route **succeeds as an exact reduction but not as a width-seven breakthrough**. The shield theorem removes `21.8%` of the width-six recurrent states, not an exponential fraction. Its formal quotient upper bound is asymptotically `(2/3)4^m`, so shield canonicalization alone cannot be expected to collapse a `66,008,456`-state width-seven recurrent class to a tiny object.

I also tested the planned finite-range fallback in a deliberately safe over-approximation: retain a right suffix and let the omitted left block supply an adversarial incoming carry independently at every source step. This preserves dependence inside each actual column but is too permissive across time. At suffix length `8`, the exact dynamic upper envelope remains about `0.233` by step `50` and the lower envelope remains zero, so it cannot approach the source-relevant threshold `1-L=0.207334008`. I do **not** claim a theorem from that diagnostic; it is recorded only as a failed relaxation and is not used in any bound above.

**Next attack:** retain the shield quotient but replace the arbitrary boundary-carry relaxation by a **finite boundary-signal transducer** for the omitted left block. The interface alphabet is the actual carry entering the retained suffix under the shared source bit; the missing task is to prove a small exact automaton for the set of feasible carry histories, not to choose the carry adversarially afresh each time. Compose that transducer with a right suffix and propagate the one-bit terminal observable. This is materially different from the failed raw width-seven projection/bias lift and from the too-loose adversarial suffix relaxation. If its exact interface automaton still grows comparably to the full carry quotient, the preserved next distinct route is a regeneration separator for `g_m` using the already-proved synchronizing source words, not another Moore-refinement pass.

The source-relevant success criterion remains clean: for some wider `w` and finite `k`, prove
\[
\max_sP^kg_m(s)<1-L=0.207334008.
\]
Then (5.3) gives `gamma_w>L`, and strip inclusion gives `gamma_2>=gamma_w>L`.

## 8. Essential executed artifacts

Exact checker source:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T16-10-00Z__w6_shield_quotient_k63.cpp`

creation commit `1966ccd40fa42aff5e987cd611c0b4b1e6a766f4`.

Exact executed output:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T16-10-00Z__w6_shield_quotient_k63.out`

creation commit `7dac7e83ca312bbaedf51ecbcbe493fc3cef8383`.

The executable was built locally with `g++ -O3 -std=c++17`. The output records the recurrent and quotient sizes, all `22,940,344` bisimulation transition checks, the exact `k=62,63` extrema, all strict-nesting cross-products, and `ALL_EXACT_CHECKS_PASS`.

## 9. ledger_delta

```text
ledger_delta:
  slot: P13
  target: T02 binary Chvatal-Sankoff gamma_2, iid uniform binary strings
  source_before: [L, U_tail]
  source_after:  [L, U_tail]
  source_gain: none in this invocation; latest completed P02 companion remains U_tail
  mechanism_before: terminal-gradient event transfer on full recurrent width-6 class; I_62 width 0.0020643482893085716...
  mechanism_after: proved leading-one shield bisimulation; recurrent quotient 5,735,086 -> 4,484,525; exact I_63 width 0.0018993954436775286...
  mechanism_gain: 1,250,561 recurrent states collapsed (21.8054...%); certified event interval shrunk 7.990553...%, strict at both endpoints
  asymptotic_transfer: r+P phi^[k]-phi^[k]=1-P^k g_m; hence 1-max P^k g_m <= gamma_w <= 1-min P^k g_m and finite-horizon Bellman bounds
  model_integrity: one shared fresh Y bit per strip column; independent Bernoulli matching excluded
  failure: arbitrary fresh adversarial boundary carry in a suffix abstraction is too loose; diagnostic lower envelope stayed 0 and upper ~0.233 at ell=8,k=50
  obstruction: shield quotient is exact but only moderate-size reduction; width-7 full/carry state growth remains substantial
  next_attack: exact finite boundary-signal transducer for feasible carry histories, composed with a right-suffix terminal-event automaton
  previous_successor_handoff: P0342 terminal handoff frozen 2/2; P0205 admitted no successor because tau(infinity) could not be frozen source-faithfully
  retired_clade: not reopened
  status: PARTIAL / source OPEN / exact internal candidate pending later independent review
```
