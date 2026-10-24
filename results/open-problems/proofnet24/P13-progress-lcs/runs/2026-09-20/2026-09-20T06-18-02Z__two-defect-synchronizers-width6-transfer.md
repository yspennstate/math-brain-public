Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. SOURCE-LEVEL BEFORE/AFTER: unchanged at `L <= gamma_2 <= U_W`, where `L=0.792665992` and `U_W` is P02's latest exact coefficient-weighted covering endpoint. CERTIFIED TRANSFER-INTERVAL MOVEMENT: for the true correlated width-6 strip, the finite-to-infinite additive radius drops from `2556527.202...` to the exact certified value `2036624461477/5000000 = 407324.8922954 < 407325`, a factor `>6.276`; this strictly shrinks every finite-horizon certified interval for `gamma_6` and strengthens the lower transfer to `gamma_2`, but does not by itself raise the current source lower endpoint.**

# P13 / T02 — two-defect synchronizers and a six-fold width-6 transfer improvement

## 1. Scope, continuity, and exact model

This run follows `operations/PROGRESS20_2026-09-20.md` and its LIVE20 assignment of P13 to T02, the binary Chvatal--Sankoff constant

\[
\gamma_2=\lim_{n\to\infty}{\mathbf E LCS(X_1^n,Y_1^n)\over n}
\]

for **two independent iid uniform binary strings**. The same fresh `Y` bit is compared against every active `X` bit in a strip column. No independent Bernoulli matching array is substituted.

Necessary dependencies only were recovered:

- controlling policy `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`;
- previous P13 report `proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T05-17-52Z__all-one-defect-sync-overlap-gap-transfer.md`, blob `8b0c3e6c29e361a36e7c97455fb6dd4f1f7bec96`;
- latest available P02 companion report `proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T05-13-00Z__coefficient-weighted-two-step-report.md`, blob `7a7d068e4f35766ec13e09d8d72650c6ed7047c4`;
- the prior exact width obstruction that `gamma_w<L` for every `w<=5`.

Fresh source navigation on 2026-09-20 retained Alexander Tiskin, `arXiv:2212.01582v2`, as the corrected source: its exact binary coefficient remains unresolved, and the earlier incorrect stochastic-process/`gamma` claims were removed in v2. The rigorous public lower endpoint used here remains

\[
L=0.792665992={99083249\over125000000}
\]

from Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`.

Short pre-LIVE20 handoff, preserved without reopening old work: P0342 had already been terminally handed off at frozen metric `2/2`; the later P0205 screen admitted no successor because the source's `tau(infinity)` notation could not be frozen source-faithfully. The retired I0051/clade work remains retired.

## 2. Source-level status versus mechanism-level movement

P02's latest available companion certificate gives

\[
\boxed{L\le\gamma_2\le U_W}
\]

with exact strict separation below its preceding `U_F`; one certified decimal separator from P02 is

\[
U_W<0.826275942762282625015106581537296632823461996193190023880806183312562944430299564492.
\]

No newer P02 report was present when this report was written. Therefore the **source-level metric does not move in this P13 invocation**:

\[
[L,U_W]\longrightarrow[L,U_W].
\]

That is distinct from the substantial lower-side transfer movement proved below. If

\[
\mu_{w,N}(s)={\mathbf E_sR_N\over N}
\]

is any exact finite-horizon width-`w` strip reward average, the previous P13 theorem gave at `w=6`

\[
|\mu_{6,N}(s)-\gamma_6|\le {C_{\rm old}\over N},
\]

where

\[
C_{\rm old}=
{365464514289599436188349306847299150185967435856
\over
142953501131693084676406151816850886136787}
=2556527.2021768987\ldots.
\]

This run proves the strict replacement

\[
\boxed{
|\mu_{6,N}(s)-\gamma_6|
\le {C_{\rm new}\over N},
\qquad
C_{\rm new}={2036624461477\over5000000}=407324.8922954<407325.
}
\]

Hence every already-computed or future exact finite-horizon interval centered at the same `mu_{6,N}(s)` shrinks strictly from radius `C_old/N` to `C_new/N`. Since `gamma_2>=gamma_6`, the source-valid one-sided transfer is

\[
\boxed{
\gamma_2\ge\gamma_6\ge {\mathbf E_sR_N\over N}-{2036624461477\over5000000N}.
}
\]

The previous/new constant ratio is about `6.276383423979046`. This is a demonstrated asymptotic-transfer gain, not a finite computation misreported as a new value of `gamma_2`.

## 3. Exact dependence-preserving boundary recursion

Fix strip half-width `w` and put `m=2w`. A formal boundary state is

\[
S=(x_1,\ldots,x_m;g_1,\ldots,g_m)\in\{0,1\}^{2m}.
\]

For one actual fresh source pair `(u,v)`, define

\[
d_0=0,
\qquad
d_i=(1-g_i)\bigl(d_{i-1}\vee\mathbf 1_{\{x_i=v\}}\bigr),
\quad 1\le i\le m.
\tag{3.1}
\]

Then

\[
x'=(x_2,\ldots,x_m,u),
\tag{3.2}
\]

\[
g'_i=g_{i+1}+d_{i+1}-d_i,\quad 1\le i<m,
\tag{3.3}
\]

\[
g'_m=(1-d_m)\mathbf 1_{\{u=v\}}.
\tag{3.4}
\]

Write the four equiprobable source-pair letters as

\[
A=(0,1),\quad B=(1,0),\quad C=(0,0),\quad D=(1,1).
\]

The dependence is explicit in (3.1): one common bit `v` drives the entire column.

The preceding report proved that every one-defect word

\[
A^rZA^{m-r},\qquad 0\le r\le m,
\]

is synchronizing for every `Z in {A,B,C,D}`, with the bit-complement family for `B` as well. The present run strictly enlarges that reset language.

## 4. A reusable zero-tail lemma

Call a state `k-zero-tailed` if

\[
(x_i,g_i)=(0,0),\qquad m-k+1\le i\le m.
\]

We use one elementary marker fact, reproved here for completeness.

### Lemma 4.1 — localized marker transport

Suppose two states agree except at position `j`, where the reference has `(x_j,g_j)=(0,0)` and the marked state has `(1,b)`, `b in {0,1}`, and all positions to the right are `(0,0)` in both states. Under one common `A=(0,1)` step, if `j>1`, the two outputs again agree except at `j-1`; the reference pair there is `(0,0)` and the marked pair is

\[
(1,1-c),
\]

where `c` is the common carry entering position `j`.

**Proof.** The carry recursions agree up to `j-1`; call their common incoming value `c`. At the reference marker, `x_j=0!=1` and `g_j=0`, so `d_j^0=c`. At the marked marker, `x_j=1=v`, hence

\[
d_j^1=(1-b)(c\vee1)=1-b.
\]

Equation (3.3) therefore gives

\[
g_{j-1}^{0\prime}=0+c-c=0,
\]

\[
g_{j-1}^{1\prime}=b+(1-b)-c=1-c.
\]

The raw marker shifts one place left. To its right both chains see only zero raw bits and zero gradients, so each carry is constant there and the carry differences telescope to zero. QED.

### Lemma 4.2 — arbitrary defect after a zero tail

Let `1<=k<=m`, and let `S` be any `k-zero-tailed state`. For every `Z in {A,B,C,D}`, the word

\[
\boxed{ZA^{m-k}}
\tag{4.1}
\]

maps **all** such `S` to one state depending only on `(k,Z)`, not on the coordinates left of the zero tail.

**Proof.**

- `Z=A`: one `A` step extends the zero tail by one, and each subsequent `A` extends it again, so after at most `m-k` further `A` steps the whole state is zero.
- `Z=C=(0,0)`: on the old zero tail, the first match with `v=0` forces the carry to one and it remains one across that tail; the last `k` output pairs are therefore zero. Thus `C` preserves a zero tail of length at least `k`, after which `A^{m-k}` fills the strip with zeros.
- `Z=B=(1,0)`: `B` and `C` have the same `v=0`, hence the same carry vector. On a nonempty zero tail that carry has reached `d_m=1`, so both terminal gradients are zero. Their outputs differ only by the terminal raw bit, a single localized marker. Compare against the `C` reference and apply Lemma 4.1 through the trailing `A` steps. Before the final marker update, every raw bit to its left is zero: the only surviving old raw bits are precisely the original zero tail, and every appended `A` bit is zero. Hence the final incoming carry is zero, so the marker's terminal gradient is fixed. The reference is already zero; therefore the marked output is fixed as well.
- `Z=D=(1,1)`: compare with `A`, which has the same `v=1` and hence the same carry vector. The post-step difference is again a single terminal marker `(1,b)` versus `(0,0)`, now with possibly state-dependent `b=1-d_m`. Lemma 4.1 erases dependence on that old `b` at the first subsequent `A`. Before the final marker update the `A` reference has raw word `0^m`, so the incoming carry is zero. The final marked state is therefore fixed.

The boundary cases in which no trailing `A` remains are direct because a full zero tail means the starting state itself is the unique zero state. QED.

## 5. New two-defect synchronizer theorem

### Theorem 5.1 — first-`C` family

For every `r,s,t>=0` with

\[
r+s+t=m
\]

and every `Z in {A,B,C,D}`, the word

\[
\boxed{A^r C A^s Z A^t}
\tag{5.1}
\]

is synchronizing on all formal states.

**Proof.** If `r=0`, the suffix `A^s Z A^t` contains exactly `m` copies of `A` and one defect, so it is one of the previously proved one-defect synchronizers. Suppose `r>=1`. After `A^r`, every state has a zero tail of length `r`. A `C` step preserves that zero tail by the argument in Lemma 4.2, and the next `A^s` extends it to length `k=r+s`. Since `t=m-k`, Lemma 4.2 applied to `ZA^t` makes the final state independent of the original state. QED.

### Theorem 5.2 — second-`D` family

For every `r,s,t>=0` with `r+s+t=m` and every `Z in {A,B,C,D}`, the word

\[
\boxed{A^r Z A^s D A^t}
\tag{5.2}
\]

is synchronizing on all formal states.

**Proof.** If `t=0`, the prefix `A^rZA^s` has `r+s=m` and is a one-defect synchronizer; applying the final `D` to its fixed output remains fixed.

Assume `t>=1`. Replace the displayed `D` by `A` and call the resulting reference word `W_0`. Its first `m+1` letters are

\[
A^rZA^{m-r},
\]

so by the one-defect theorem the reference chain is already in a fixed state after those first `m+1` letters.

Up to the `D/A` location, the actual and reference chains coincide. At that location `D=(1,1)` and `A=(0,1)` share the same `v=1`, so they have the same carry vector; their outputs can differ only at the terminal raw/gradient pair. Thus their discrepancy is a localized terminal marker exactly of the type in Lemma 4.1. Every following source letter is `A`, so the marker moves left one position per step and remains the only discrepancy. At the **final** `A` step, the reference chain immediately before the step has processed exactly `m+1` letters of `W_0`, hence is already fixed. Therefore the common carry entering the marker is fixed. Lemma 4.1 makes the final marker gradient `1-c`, independent of the old marker gradient. The actual final state is consequently fixed. QED.

Bit-complement symmetry exchanges

\[
A\leftrightarrow B,\qquad C\leftrightarrow D,
\]

so the complementary `B` families are synchronizing as well.

### Why the theorem is genuinely restricted

The tempting claim that **every** word with `m` copies of `A` and two arbitrary defects synchronizes is false. At `m=3`,

\[
W=ABABA
\]

has three `A` letters and two defects, but exact recursion gives

\[
(000;000)\xrightarrow{W}(010;010),
\]

while

\[
(000;001)\xrightarrow{W}(010;110).
\]

So the restricted defect-type structure in Theorems 5.1--5.2 is doing real work; the run did not promote a false all-two-defect heuristic.

## 6. Exact width-6 reset language

Take `m=12`, i.e. `w=6`. Use the minimal reset language consisting of:

1. `A^12` and `B^12`;
2. every interior one-defect word `A^rZA^{12-r}` and its `B` analogue;
3. every two-defect `A` word of length `14` with two internal defects and either first defect `C` or second defect `D`, plus every bit-complement `B` word.

There are exactly

\[
2+6(11)+2\cdot5\binom{12}{2}
=2+66+660
=\boxed{728}
\]

minimal patterns. For the two-defect count, among the `3^2=9` ordered non-`A` defect-type pairs, exactly

\[
9-(2)(2)=5
\]

satisfy `first=C OR second=D`.

Let `tau` be the first end time of any of these 728 reset patterns in the actual iid source-pair stream. Since every pattern is a constant boundary map, once `tau` occurs any two width-6 strip chains driven by the same future source pairs have coalesced exactly.

## 7. Exact finite automaton certificate for `E tau`

Build the prefix automaton of the 728 reset patterns. After deleting absorbing pattern states it has exactly

\[
\boxed{3279}
\]

nonabsorbing prefix states. Each of the four source letters has probability `1/4`.

The checker first solves the floating linear system only to **propose** a rational super-solution. Floating arithmetic is not used as proof. With denominator

\[
Q=10^7,
\]

it constructs integer values `H(q)` and then checks exactly, for every nonabsorbing automaton state `q`,

\[
\boxed{
4H(q)\ge4Q+\sum_{a\in\{A,B,C,D\}:\delta(q,a)\ {m nonabsorbing}} H(\delta(q,a)).
}
\tag{7.1}
\]

Absorbing successors contribute zero. The minimum exact residual numerator over all 3279 states is

\[
\boxed{9>0}.
\]

For the empty prefix,

\[
H(\varnothing)=4073248922954.
\]

Thus `h=H/Q` obeys `h>=1+Ph` with zero value after absorption. Iterating this inequality up to `tau wedge n` and using monotone convergence gives

\[
\boxed{
\mathbf E\tau\le h(\varnothing)
={4073248922954\over10^7}
={2036624461477\over5000000}
=407324.8922954<407325.
}
\tag{7.2}
\]

The executed checker also exhaustively verifies both new analytic synchronizer families and their bit complements on all formal states for `m<=4`. That enumeration is a self-check only; the proofs above are the general argument.

Artifact:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T06-15-26Z__two_defect_sync_certificate.py`

Executed output:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T06-15-26Z__two_defect_sync_certificate.out`

ending `ALL_EXACT_CHECKS_PASS`.

## 8. Finite-to-infinite theorem

Let `S_t` be the width-6 strip chain started from any formal state `s`, and let `\widetilde S_t` start from stationarity. Drive both by the **same actual source-pair stream**. At time `tau` a synchronizing source word has occurred, so

\[
S_\tau=\widetilde S_\tau
\]

and the two chains remain identical thereafter.

The one-step strip reward is a bit, hence before coupling the two rewards differ by at most one per step. Therefore

\[
\left|\mathbf E_sR_N-\mathbf E_\pi R_N\right|
\le \mathbf E(\tau\wedge N)
\le \mathbf E\tau.
\]

Since `E_pi R_N=N gamma_6`, (7.2) gives

\[
\boxed{
\left|\mathbf E_sR_N-N\gamma_6\right|
\le {2036624461477\over5000000}.
}
\tag{8.1}
\]

Dividing by `N` gives the claimed certified interval, and strip restriction gives

\[
\boxed{
\gamma_2\ge\gamma_6
\ge {\mathbf E_sR_N\over N}
-{2036624461477\over5000000N}.
}
\tag{8.2}
\]

Compared with the preceding P13 constant, the exact checker verifies

\[
C_{\rm old}>6C_{\rm new},
\]

and numerically

\[
C_{\rm old}-C_{\rm new}=2149202.3098814986\ldots.
\]

## 9. Failure / obstruction and next attack

### What did not move

The best source interval remains `[L,U_W]`. Widths `w<=5` are rigorously too small to beat `L`, and this run has not yet produced an exact width-6 finite-horizon reward whose transferred lower endpoint exceeds `L`. Therefore no new numerical lower bound on `gamma_2` is claimed.

The generic width-6 synchronization penalty, although reduced by more than a factor six, is still about `4.07e5/N`. A finite-horizon computation must either be very long with an exact/rigorous expectation engine, or the coupling must be made event-specific so that the relevant error is much smaller than full-state synchronization.

### Decisive failed overgeneralization

The exact `ABABA` counterexample above kills the naive route "m base letters plus any two defects synchronize." The next proof should exploit the actual defect-type algebra, not merely count base letters.

### Next attack

The highest-value continuation is to characterize the still-missing two-defect type `D ... C` family and, more importantly, to couple only the terminal mixed-suffix event from the exact identity

\[
\gamma_w={2\over3}+{1\over3}\pi_w(B_w).
\]

A successful event-specific coupling could replace the full-state `4^{2w}`-scale synchronization penalty by the extinction time of only the suffix/carry information that decides `B_w`. In parallel, P02 remains on the complementary upper variational/covering route; this run does not duplicate it.

## 10. `ledger_delta`

```yaml
ledger_delta:
  slot: P13
  parent: T02-binary-LCS
  model: GPT-5.6-Sol
  reasoning_effort: UNVERIFIED
  source_status_before: "L <= gamma_2 <= U_W"
  source_status_after: "L <= gamma_2 <= U_W"
  source_metric_movement: false
  mechanism:
    object: "true correlated width-6 strip; iid source-pair alphabet A,B,C,D"
    old_additive_constant: "365464514289599436188349306847299150185967435856/142953501131693084676406151816850886136787"
    new_additive_constant: "2036624461477/5000000"
    new_simple_bound: "< 407325"
    strict_gain: true
    gain_factor_previous_over_new: "6.276383423979046..."
  new_proved_scope:
    - "A^r C A^s Z A^t synchronizes for r+s+t=m"
    - "A^r Z A^s D A^t synchronizes for r+s+t=m"
    - "bit-complement B families"
    - "width-6 728-pattern reset automaton has exact Bellman hitting-time super-solution"
    - "|E_s R_N - N gamma_6| <= 2036624461477/5000000"
  rejected_claim:
    statement: "all words with m A letters and two arbitrary defects synchronize"
    counterexample: "m=3, ABABA: (000;000)->(010;010), (000;001)->(010;110)"
  finite_core:
    checker: "proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T06-15-26Z__two_defect_sync_certificate.py"
    output: "proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T06-15-26Z__two_defect_sync_certificate.out"
    verdict: "ALL_EXACT_CHECKS_PASS"
  source_level_claim: "PARTIAL; gamma_2 not determined and source interval unchanged this run"
  next_attack: "event-specific mixed-suffix/carry coupling, after testing/proving the remaining D...C two-defect family"
  previous_successor_handoff: "P0342 terminal handoff preserved; P0205 screen admitted no successor; I0051/clade remains retired"
```
