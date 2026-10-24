Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# P13 / T02 — exact Cesaro-block Bellman transfer and a dependence-preserving carry quotient for the next strip width

## 0. Before / after, separated by level

### Source-level binary Chvatal–Sankoff interval

The target remains

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]

for two independent iid uniform binary strings. The match indicators in a column are dependent because the same incoming `Y` letter is reused across that column. The independent Bernoulli matching model is not used.

The latest **completed** P02 companion report available to this run remains

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T10-03-15Z__matched-successor-defect-report.md`,

which proves the repository-internal strict upper endpoint `U_new<U_*`. Thus the completed source-level interval carried into and out of this run is

\[
\boxed{L\le\gamma_2\le U_{new}},\qquad
L=0.792665992=\frac{99083249}{125000000}.
\]

**Source-level before/after in this P13 invocation: unchanged.** Newer P02 artifacts at `2026-09-20T12-18-55Z__type0_successor_dual_checker.*` contain a promising exact dual defect and an endpoint-checker source file, but there is not yet a completed immutable P02 report plus archived endpoint execution in the dependency set read for this run. I therefore do not promote those in-progress companion artifacts to a source-level endpoint claim here.

Fresh source navigation rechecked Alexander Tiskin, `arXiv:2212.01582v2`: the arXiv record says the binary Chvatal–Sankoff coefficient remains unresolved, v2 was last revised 2024-08-13, and claims in the earlier preprint concerning the stochastic process and `gamma` that turned out to be incorrect were removed. The retained rigorous public lower endpoint is `0.792665992` from Heineman–Miller–Reichman–Salls–Sarkozy–Soiffer, `arXiv:2407.10925`.

### P13 mechanism-level movement

The previous P13 report

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T11-19-06Z__bias-extremal-integer-bellman-transfer.md`

proved for the genuine dependent width-six recurrent strip the exact Bellman interval

\[
\frac{6238638445311257066}{8000000000000000000}
\le\gamma_6\le
\frac{6238638445311257073}{8000000000000000000},
\]

of width

\[
\varepsilon_1=\frac7{8\cdot10^{18}}=8.75\cdot10^{-19}.
\]

This run proves a new **Cesaro-block Bellman theorem**. Applying it at block length `k=60` to the same exact integer residual certificate gives a strictly nested interval whose exact width is

\[
\boxed{
\varepsilon_{60}=
\frac{3183344437055150847758447502072126641}
{159507359494189904748456847233641349120000000000000000000}
}
\]

and hence

\[
\boxed{
\varepsilon_{60}=1.9957351479892719\ldots\times10^{-20}<\varepsilon_1.
}
\]

The exact old/new width ratio is

\[
\boxed{
\frac{\varepsilon_1}{\varepsilon_{60}}
=
\frac{139568939557416166654899741329436180480}
{3183344437055150847758447502072126641}
=43.8434930046491\ldots .
}
\]

More importantly, the same smoothing gives a **finite-to-infinite transfer**: for every horizon `N=60J`, a finite computation started at the inherited bias minimizer satisfies

\[
\boxed{\gamma_6\ge A_N(s_-)-\varepsilon_{60}},
\]

with no `1/N` term; the analogous upper inequality holds at the bias maximizer. Thus the asymptotic subtraction in the useful extremal-start finite certificate is strictly smaller by the same factor `43.84349...`.

Status: **PARTIAL / source OPEN / exact internal candidate pending later independent review and public-priority checking.**

## 1. Scope, continuity, exclusions, and handoff

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns P13 to T02 dependence-preserving boundary recursion, complementary to P02's stationary/variational upper route.

Only necessary continuity was read: the previous P13 report above; the latest completed P02 report; root `POSTED.md`; the new exact P13 artifacts listed in section 6; and the current arXiv records. No whole-repository reread was performed.

Short actual pre-LIVE20 successor handoff is preserved: P0342 had already been terminally handed off at frozen `2/2`; the later P0205 screen admitted no successor because its source notation could not be frozen source-faithfully. Retired I0051/clade work remains retired and was not reopened.

No email, Drive, public posting, paid compute, permission, schedule, peer-history, or historical-claim overwrite was performed.

## 2. Genuine dependent strip recursion

Fix half-width `w` and put `m=2w`. A formal strip state is

\[
s=(x,g),\qquad x,g\in\{0,1\}^m.
\]

Set

\[
V_0=0,\qquad V_k=\sum_{i=1}^k g_i.
\]

For one fresh actual source pair `(u,v)`, define

\[
a_i={\bf1}_{\{x_{i+1}=v\}}\quad(0\le i<m),
\qquad a_m={\bf1}_{\{u=v\}}.
\]

The same `v` occurs in every `a_i` in the whole column. The updated profile is

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

Equivalently, with carries `d_i`,

\[
d_i=(1-g_i)\bigl(d_{i-1}\vee {\bf1}_{\{x_i=v\}}\bigr),
\]

and the same `v` is shared down the entire column. Every computation below uses the four equiprobable genuine source pairs `(u,v)` under this recursion.

## 3. New theorem: Cesaro-block residual smoothing is itself a Bellman certificate

Let `R` be a finite closed recurrent class with transition kernel `P`, one-step mean reward `r`, stationary mean `gamma`, and potential `h`. Put

\[
\delta:=r+Ph-h.
\]

For integer `k>=1`, define the `k`-step mean reward

\[
r_k(s):=\frac1k\mathbf E_s R_k,
\]

the block kernel `P_k=P^k`, and block potential

\[
\tilde h:=\frac hk.
\]

### Theorem 3.1 — exact block residual identity

For every state,

\[
\boxed{
r_k+P^k\tilde h-\tilde h
=\frac1k\sum_{t=0}^{k-1}P^t\delta.
}
\tag{3.1}
\]

Therefore, with

\[
\ell_k:=\min_R\frac1k\sum_{t=0}^{k-1}P^t\delta,
\qquad
u_k:=\max_R\frac1k\sum_{t=0}^{k-1}P^t\delta,
\]

one has the stationary certificate

\[
\boxed{\ell_k\le\gamma\le\nu_k.}
\tag{3.2}
\]

If `epsilon_k=nu_k-ell_k`, `s_-` minimizes the original `h`, and `s_+` maximizes it, then for every integer `J>=1`, with `N=kJ`,

\[
\boxed{
\gamma\ge\frac{\mathbf E_{s_-}R_N}{N}-\varepsilon_k,
\qquad
\gamma\le\frac{\mathbf E_{s_+}R_N}{N}+\varepsilon_k.
}
\tag{3.3}
\]

For an arbitrary starting state `s`,

\[
\boxed{
\frac{\mathbf E_sR_N}{N}-\varepsilon_k-\frac{h(s)-h_{\min}}N
\le\gamma\le
\frac{\mathbf E_sR_N}{N}+\varepsilon_k+\frac{h_{\max}-h(s)}N.
}
\tag{3.4}
\]

Thus the residual part of the finite-to-infinite error is replaceable by the strictly smaller block residual span, while the boundary term is unchanged.

### Proof

The telescoping identity for the one-step residual is

\[
\sum_{t=0}^{k-1}P^t\delta
=\sum_{t=0}^{k-1}P^tr+P^kh-h.
\]

Dividing by `k` gives (3.1), because `r_k=(1/k)sum_{t=0}^{k-1}P^tr` and `P^k\tilde h-\tilde h=(P^kh-h)/k`.

The stationary law `pi` obeys `pi P^t=pi`, so

\[
\pi\left(\frac1k\sum_{t=0}^{k-1}P^t\delta\right)=\pi\delta=\gamma,
\]

which proves (3.2).

Now regard `(P^k,r_k)` as a Markov reward chain whose reward is normalized per original time step. Its stationary mean is still `gamma`, and its Bellman potential is `h/k`. Applying the previously proved bias-extremal transfer theorem to this block chain gives (3.3): the minimizers and maximizers of `h/k` are exactly those of `h`, and `J` block rewards average to `E_s R_{kJ}/(kJ)`. For a general start, the block-chain boundary term is

\[
\frac{(h(s)-h_{\min})/k}{J}=\frac{h(s)-h_{\min}}{N},
\]

and similarly on the upper side, yielding (3.4). QED.

### Why this is not finite computation promoted to an asymptotic bound

The transfer uses a globally verified exact Bellman residual and the identity (3.1). A finite expectation by itself is not a bound on `gamma`; the subtraction `epsilon_k` and, away from bias extremizers, the explicit bias boundary term remain logically required.

## 4. Exact width-six `k=60` certificate

The inherited exact width-six potential uses scale

\[
Q=2\cdot10^{18}
\]

and residual integer numerators

\[
D_H(s)=Q\sum_{a=1}^4\rho(s,a)+\sum_{a=1}^4H(T_as)-4H(s).
\]

The exact scan has

\[
d_-=6238638445311257066,
\qquad d_+=6238638445311257073.
\]

Write

\[
e(s)=D_H(s)-d_-\in\{0,1,\ldots,7\}.
\]

Then

\[
\delta(s)=\frac{d_-}{4Q}+\frac{e(s)}{4Q}.
\]

For exact integer propagation define

\[
E_k(s)=4^{k-1}\sum_{t=0}^{k-1}P^te(s).
\]

Because each source letter has probability `1/4`, this obeys the integer recurrence

\[
\boxed{
E_{k+1}(s)=4^k e(s)+\sum_{a=1}^4E_k(T_as),
\qquad E_1=e.
}
\tag{4.1}
\]

No floating arithmetic appears in this propagation.

For `k=60`, the executed exact checker gives

\[
4^{59}=332306998946228968225951765070086144,
\]

\[
E_{60}^{\min}=
41924395640042677859658223559910276214,
\]

\[
E_{60}^{\max}=
45107740077097828707416671061982402855.
\]

Therefore

\[
\boxed{
\ell_{60}=
\frac{6238638445311257066}{8\cdot10^{18}}
+
\frac{41924395640042677859658223559910276214}
{8\cdot10^{18}\cdot60\cdot4^{59}},
}
\tag{4.2}
\]

\[
\boxed{
\nu_{60}=
\frac{6238638445311257066}{8\cdot10^{18}}
+
\frac{45107740077097828707416671061982402855}
{8\cdot10^{18}\cdot60\cdot4^{59}}.
}
\tag{4.3}
\]

The interval is strictly nested in the preceding one: `E_60^min>0`, while

\[
7\cdot60\cdot4^{59}-E_{60}^{\max}
=94461199480318337947483070267453777625>0.
\]

Its width is exactly the `epsilon_60` displayed in section 0. Diagnostic decimal values are

\[
\ell_{60}=0.7798298056639071\ldots,
\qquad
\nu_{60}=0.7798298056639071\ldots,
\]

but the proof uses the exact integer expressions (4.2)–(4.3), not decimal subtraction.

The checker output ends `ALL_EXACT_CHECKS_PASS`.

## 5. New dependence-preserving boundary quotient for lifting from width `w` to `w+1`

The preceding report's next attack was a carry-augmented local lift into width seven. A naive projection is not Markov because the omitted left cell determines the carry entering the retained core. This run identifies the exact missing information.

Consider full half-width `W=w+1`; its raw/gradient vectors have length

\[
M=2W=2w+2.
\]

Delete the leftmost and rightmost coordinates and retain the interior length-`m=2w` vectors

\[
\bar x=(x_2,\ldots,x_{M-1}),
\qquad
\bar g=(g_2,\ldots,g_{M-1}).
\]

The omitted **left** pair `(x_1,g_1)` affects every future interior carry only through the two-bit signature

\[
\boxed{
c=(c_0,c_1),\qquad c_v=(1-g_1){\bf1}_{\{x_1=v\}}.}
\tag{5.1}
\]

Only the three values `(0,0),(1,0),(0,1)` occur. Retain the omitted **right** pair

\[
r=(x_M,g_M)\in\{0,1\}^2.
\]

Thus define the quotient context

\[
q=(\bar x,\bar g,c,r).
\]

### Theorem 5.1 — exact carry-core quotient

For every `w>=1`, the full width-`w+1` reward and the next quotient context are deterministic functions of only `q` and the fresh genuine source pair `(u,v)`. In particular, two full states with the same `q` have identical one-step reward and identical next quotient under each of the four source pairs.

The formal quotient has exactly

\[
\boxed{12\cdot2^{4w}}
\]

contexts, rather than `16*2^(4w)` full formal states.

### Explicit recursion and proof

Write the retained coordinates as `bar x_1,...,bar x_m` and `bar g_1,...,bar g_m`. For the actual incoming `Y` bit `v`, put

\[
e_0=c_v,
\]

\[
e_j=(1-\bar g_j)\left(e_{j-1}\vee{\bf1}_{\{\bar x_j=v\}}\right),
\qquad1\le j\le m,
\]

and, with `r=(x_R,g_R)`,

\[
e_{m+1}=(1-g_R)\left(e_m\vee{\bf1}_{\{x_R=v\}}\right).
\tag{5.2}
\]

The full central reward is

\[
\boxed{\rho=\bar g_{w+1}+e_{w+1}},
\tag{5.3}
\]

with the obvious zero/one-based indexing translation used by the checker.

The new retained raw vector is

\[
\bar x'=(\bar x_2,\ldots,\bar x_m,x_R),
\]

and the new retained gradient vector is

\[
\bar g'_j=\bar g_{j+1}+e_{j+1}-e_j,
\qquad1\le j<m,
\]

\[
\bar g'_m=g_R+e_{m+1}-e_m.
\tag{5.4}
\]

The omitted new left gradient equals

\[
g'_L=\bar g_1+e_1-e_0,
\]

and its raw bit is `x'_L=bar x_1`; hence

\[
c'_z=(1-g'_L){\bf1}_{\{\bar x_1=z\}},\qquad z\in\{0,1\}.
\tag{5.5}
\]

Finally the new right pair is

\[
r'=\left(u,(1-e_{m+1}){\bf1}_{\{u=v\}}\right).
\tag{5.6}
\]

Equations (5.2)–(5.6) are exactly the full carry recursion after deleting the two outer coordinates. The old omitted left pair enters only through `e_0=c_v`, and the old omitted right pair is kept explicitly. This proves the quotient theorem without any independence approximation. QED.

An exhaustive small-width checker verifies the quotient against **every formal full state and all four source pairs** for core widths `w=1,2,3`, totaling `1,024`, `16,384`, and `262,144` transition checks, and ends `ALL_EXACT_CHECKS_PASS`.

For the actual width-seven recurrent class, exact BFS gives

\[
|R_7|=66,008,456.
\]

Mapping every recurrent state through the exact quotient gives only

\[
\boxed{56,219,024}
\]

distinct quotient contexts, collapsing

\[
\boxed{9,789,432}
\]

full recurrent states, i.e. retaining `0.851694273836673...` of them. This is a real exact state reduction, although not yet enough by itself to make a full width-seven Bellman solve attractive.

## 6. Decisive obstruction to the naive width-six projection lift

The right-anchored projection that simply retains twelve raw and twelve gradient bits from a width-seven state is **not** closed on the width-six recurrent class. Exact enumeration gives

- width-seven recurrent states: `66,008,456`;
- distinct projected width-six-sized states: `5,799,288`;
- projected states outside the width-six recurrent class: `64,202`;
- occurrences of such outside projections among width-seven recurrent states: `183,840`.

Under the ordinary width-six transition graph, these `64,202` outsider projections have `231,094` outgoing edges into `R_6`, `25,636` edges to another outsider projection, and `78` edges to states outside both sets. Repeated deterministic peeling of outsiders whose four width-six successors are already safe stalls with exactly

\[
\boxed{2,706}
\]

outsiders after depth nine. Therefore the hoped-for proof “project width seven to `R_6` and use the width-six bias unchanged after finitely many forced steps” is false as stated.

A separate exact classification shows that among the `64,202` outsider projections, `43,818` can be mapped into `R_6` by changing only the first gradient bit, another `17,892` by changing the first two gradient bits, another `2,104` by changing the first two raw bits, but `388` survive all three simple local repairs. This identifies a small but genuine exceptional core rather than a merely administrative state explosion.

This is reported as an obstruction, not as a bound on `gamma_2`.

## 7. Essential executed artifacts

The following artifacts were actually executed and are preserved on `master`:

1. Exact width-six Cesaro residual propagator:
   - code: `proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T12-34-30Z__w6_cesaro_bellman60.cpp`, creation commit `e4bd8847f670e8f8fc59cc6504e2e5ef13dc86f5`;
   - output: same stem `.out`, creation commit `c5ad05099be9395f5b2e6b5ba9441d3810574741`.
   - exact output includes `k=60 ... spread=3183344437055150847758447502072126641` and ends `ALL_EXACT_CHECKS_PASS`.

2. Exact carry-core quotient identity checker:
   - code: `.../2026-09-20T12-35-00Z__carry_core_quotient_small_exact.py`, commit `78b4342655ffb99cebdbca01d825bf63fe51c3b5`;
   - output: same stem `.out`, commit `6efa26baa9bd7ebe936bf2e303613d7f44cd6696`, ending `ALL_EXACT_CHECKS_PASS`.

3. Exact width-seven projection obstruction:
   - code: `.../2026-09-20T12-35-30Z__w7_projection_obstruction.cpp`, commit `9edd3db387a08f007680b65e9b59271b8b7f1938`;
   - output: same stem `.out`, commit `249038f2da3052c474e9c5803c06c81b6c45f4f8`, ending `ALL_EXACT_CHECKS_PASS`.

4. Exact width-seven quotient reachable-count check added in this invocation:
   - code: `.../2026-09-20T13-06-00Z__w7_carry_quotient_reachable_count.cpp`, commit `e478e1d37ef1343a436fdae2fe604757dd9ab9a0`;
   - output: same stem `.out`, commit `24d47569c4a3bd78b83982af764a08257f8f890d`, ending `ALL_EXACT_CHECKS_PASS`.

The quotient-count program was compiled with `g++ -O3 -std=c++17`; local execution reported `ELAPSED=18.27`, `MAXRSS_KB=324864`. Runtime and memory diagnostics are not part of the mathematical proof.

## 8. Failure accounting and residual obstruction

The width-six residual smoothing succeeds decisively at its own task but cannot move the source lower endpoint because the already-certified width-six constant is below `L`. The exact width-six upper endpoint remains separated from `L` by a positive rational margin from the previous report.

The first width-seven lift attempt also has a concrete failure: raw projection to the width-six recurrent class is not a Markov factor and leaves `64,202` outsider projected states; even a deterministic closure peel leaves `2,706` genuinely persistent outsiders. The new carry quotient repairs the Markov-information loss exactly, but the reachable quotient still contains `56,219,024` states, so a full exact Bellman solve would largely reproduce the state explosion rather than exploit the sparse obstruction.

These are mathematical obstructions, not reasons to wait for an auditor or peer.

## 9. Next attack

Use the exact quotient theorem to build a **two-level local Bellman lift**, not a full width-seven value iteration:

- base potential: inherited exact width-six bias on projections in `R_6`;
- correction state: the carry signature `c`, right pair `r`, and only the sparse outsider projection class;
- solve an exact lower residual inequality for the correction on the finite exceptional transition graph, with the `2,706` unpeeled outsider core treated explicitly;
- if the required correction depends on more than this quotient or its residual loss exceeds the width-six-to-seven gain, stop this recovery route and switch to the previously identified event-specific mixed-terminal-suffix coupling rather than another full-state enumeration.

The target is a certified lower Bellman bound for `gamma_7` or a decisive proof that this local-lift architecture cannot beat `L`; either outcome advances the source-lower strategy without conflating finite computation with an asymptotic statement.

## 10. ledger_delta

```text
ledger_delta:
  target: T02 binary Chvatal-Sankoff gamma_2, iid uniform binary strings
  source_before: [L, U_new]
  source_after:  [L, U_new]   # unchanged in this P13 invocation
  source_note: newer P02 type-0 artifacts observed but not promoted without completed companion report/output package
  p13_width6_interval_before: residual span 7/(8e18) = 8.75e-19
  p13_width6_interval_after: exact k=60 Cesaro-block span 3183344437055150847758447502072126641 / 159507359494189904748456847233641349120000000000000000000
  mechanism_gain: exact 43.8434930046491... shrink in residual/asymptotic subtraction for 60-block extremal-start certificates
  new_theorem_1: k-block Bellman residual equals Cesaro average of one-step residual; bias-extremal finite-to-infinite transfer retains zero boundary loss at original bias extremizers
  new_theorem_2: exact width-(w+1) carry-core quotient (interior x,g + 3-valued left carry signature + right pair) preserves transitions and rewards
  w7_full_recurrent: 66008456
  w7_quotient_reachable: 56219024
  w7_projection_outsiders: 64202
  w7_unpeeled_projection_core: 2706
  failed_route: naive direct projection of width 7 into R6 is not closed / not Markov
  next_attack: sparse exceptional-state correction to lift H6 through the exact carry quotient; otherwise event-specific mixed-suffix coupling
  status: PARTIAL / source OPEN / full candidates pending later independent review
```
