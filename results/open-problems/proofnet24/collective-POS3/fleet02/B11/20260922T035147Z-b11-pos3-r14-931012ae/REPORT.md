# POS3 fleet02/B11 — general nested-endpoint reverse-channel compression

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent POS3 status:** `OPEN / NOT PROVED`  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`  
**Run:** `20260922T035147Z-b11-pos3-r14-931012ae`

## 1. Fresh control and source-bound state

Fresh control was resolved from `yspennstate/math-research-brain` main at
revision `2026-09-22.2`; `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
remains active; the later stop on new installation and benchmark work remains
in force. This run did POS3 mathematics only.

The latest complete campaign-lead report consumed is

- fleet04/B10,
  `proofnet24/collective-POS3/fleet04/B10/20260922T034709Z-B10-POS3-r12/REPORT.md`,
  blob `4759a4ecb5f2963a3d190f66fc6728459bb1a46e`.

It proves the crossed-neighborhood union identity and, in the inherited
strict-chain/crossed-successor/no-descent branch, compresses the endpoint
defect to at most three fringe events and forces a fringe minority mass
`>1/9`. Its explicit remaining difficulty is that successor sets need not
continue to satisfy the crossed nesting.

The named OTHER-account result actually consumed is

- fleet03/B19,
  `proofnet24/collective-POS3/fleet03/B19/20260922T0332Z-b19-pos3-r11-reverse-branching/REPORT.md`,
  blob `7da837e669bec270ce633fc9d9612cea0293a2b3`.

For a strict nested endpoint with a **chain** predecessor difference it proves
the exact reverse-remainder decomposition into the unique predecessor channel
plus minimal successor channels; in the majority-late/no-span-descent branch,
the reverse remainder exceeds `E/3`, every atomic channel is individually
below `E/3`, and at least two channels are required.

The endpoint identity used by both reports is fleet01/B11 run
`20260922T021210Z-b11-pos3-exchange-r11`, report blob
`5fdf6f70d35fee1011b67c217b9e177fb197e81a`: for incomparable `(a,b)` with
`Pred(b) subseteq Pred(a)`, if `E=e(P)`, `Q` is its forward common-blocker
count and `R` its reverse nonneutral remainder, then

`Pr(a<b) = 1 - (Q+R)/(2E)`.

The immediately previous fleet02/B11 report, blob
`a8e5e6dc7fc402c714d87da86b4b833a7efa0c38`, proved that every POS3
counterexample has connected comparability graph as well as connected
incomparability graph. Thus a cardinality-minimal counterexample is
series- and parallel-indecomposable.

## 2. Conditional end-to-end route

Assume POS3 is false and choose a cardinality-minimal counterexample `P`.

Inherited reductions give width exactly three, connected comparability and
incomparability graphs, the transitive strong-majority order `L_*`, and the
lead's first-boundary strict nested pair. At that first pair the lower
predecessor discrepancy is a chain, so fleet03/B19 gives a successor
continuation in the majority-late/no-descent direction. The global proof
still needs to continue after moving away from that first special pair.
At a later nested endpoint the predecessor discrepancy need no longer be a
chain, while the lead's crossed successor nesting can also fail.

The first missing implication attacked here is therefore:

> For an arbitrary width-three nested endpoint
> `Pred(b) subseteq Pred(a)`, compress the **entire reverse remainder** to a
> bounded canonical set without assuming that the predecessor discrepancy is a
> chain and without assuming crossed successor nesting.

The theorem below pays this implication. It shows that the arbitrary reverse
remainder is always a union of at most four canonical Hasse-channel events.
Consequently, in the majority-late/no-span-descent branch, either a successor
channel exists or the only possible successor-free obstruction is a
**double-predecessor fan** consisting of two incomparable Hasse predecessors
of `a`. This is the genuinely unresolved local state left by this run.

## 3. General reverse-channel compression

Let `P` be a finite poset of width at most three. Let `a||b` satisfy

`Pred(b) subseteq Pred(a)`.                                   (3.1)

Put

`D = Pred(a) \ Pred(b)`,                                      (3.2)

`T = Max(D)`,                                                  (3.3)

`S = {z : b<z and z||a}`,                                     (3.4)

`U = Min(S)`.                                                  (3.5)

Let `R` be the fleet01/B11 reverse nonneutral remainder: the number of
linear extensions in which `b` precedes `a` and the open interval from `b`
to `a` contains an element comparable with at least one endpoint.

For `t in T` and `u in U`, define full-extension events

`A_t = {L : b precedes t}`,                                   (3.6)

`B_u = {L : u precedes a}`.                                   (3.7)

These events automatically lie in the reverse orientation because `t<a` and
`b<u`.

### Theorem 3.1 — exact reverse-channel compression

Under (3.1),

`R = | union_{t in T} A_t  union  union_{u in U} B_u |`.       (3.8)

Moreover

`|T| <= 2`, `|U| <= 2`,                                      (3.9)

every `t in T` is a Hasse predecessor of `a`, and every `u in U` is a Hasse
successor of `b`.

Hence the reverse nonneutral remainder of **every** width-three nested
endpoint is determined by at most four canonical Hasse-channel events.

#### Proof

First observe that every `d in D` is incomparable with `b`. If `d<b`, then
`d in Pred(b)`, contrary to `d in D`. If `b<d`, then `b<d<a`, contradicting
`a||b`. Therefore `d||b`.

Now take any reverse extension `L` counted by `R`. A nonneutral element `z`
strictly between `b` and `a` can only have one of two forms.

1. `z<a` and `z||b`. Then `z in D`. Choose a maximal `t in D` with
   `z<=t`. Since `b<z<=t<a` in `L`, the event `A_t` occurs.
2. `b<z` and `z||a`. Then `z in S`. Choose a minimal `u in S` with
   `u<=z`. Since `b<u<=z<a` in `L`, the event `B_u` occurs.

Conversely, if `A_t` occurs then `b<t<a`, so `t` is a nonneutral element in
the reverse interval. If `B_u` occurs then `b<u<a`, so `u` is such an
element. This proves the exact union identity (3.8).

Because `T` is an antichain and every member of `T` is incomparable with
`b`, the set `T union {b}` is an antichain. Width at most three gives
`|T|<=2`. Likewise `U` is an antichain and every member is incomparable
with `a`, so `U union {a}` is an antichain and `|U|<=2`.

Finally take `t in T`. If there were `t<c<a`, then relative to `b` there are
three possibilities. `c<b` would imply `t<b`, impossible; `b<c` would imply
`b<a`, impossible; and `c||b` would put `c in D` above the maximal element
`t`, impossible. Therefore `t` is covered by `a`. The dual argument shows
that every `u in U` covers `b`: if `b<c<u`, then `c<a` would imply `b<a`,
`a<c` would imply `a<u`, and `c||a` would contradict minimality of `u` in
`S`. `QED`

### Corollary 3.2 — constant-size endpoint state

Let

`M = Min{z : a<z and z||b}`.

Exactly as above, `M union {b}` is an antichain and every `m in M` covers
`a`, so `|M|<=2`.

Thus the full fleet01/B11 endpoint identity

`Pr(a<b) = 1 - (Q+R)/(2E)`                                   (3.10)

has a constant-size canonical representation in width three:

- `Q` is the event that `b` precedes **all** members of a set `M` of at most
  two Hasse successors of `a`;
- `R` is the union of at most two Hasse-predecessor events `A_t` and at most
  two Hasse-successor events `B_u`.

No chain hypothesis on `D`, no successor-set nesting, no minimality, and no
finite-size bound enter this compression.

## 4. Majority-late/no-span consequence

Now suppose `P` is a hypothetical no-balanced POS3 counterexample and `L_*`
is its transitive strong-majority order. Consider a nested endpoint satisfying
(3.1) with

`b prec_* a`,                                                 (4.1)

equivalently `Pr(a<b)<1/3`.

Assume the current branch has **no strict strong-majority span descent** from
a canonical reverse blocker.

The endpoint identity gives

`Q+R > 4E/3`.                                                 (4.2)

Since `Q<=E`,

`R > E/3`.                                                    (4.3)

For `t in T`, we have `t<a` in the poset, hence `t prec_* a`. If
`b prec_* t`, then `b prec_* t prec_* a`, while `b||t`; this is a strictly
shorter extreme incomparable pair. Under the no-descent hypothesis this
cannot occur, so

`t prec_* b`, and therefore `Pr(b<t)<1/3`.                    (4.4)

Similarly, for `u in U`, the poset relation `b<u` gives `b prec_* u`. If
`u prec_* a`, then `b prec_* u prec_* a` and `u||a` give a shorter extreme
pair. Hence no descent forces

`a prec_* u`, and therefore `Pr(u<a)<1/3`.                    (4.5)

By Theorem 3.1, `R` is a union of at most four events, each individually
smaller than `E/3`, while their union is larger than `E/3`. Hence at least
two canonical reverse channels are active.

### Corollary 4.1 — successor continuation or a double-predecessor fan

In the strict nested case `Pred(b) subsetneq Pred(a)`, `T` is nonempty.
If `U` is empty, then necessarily

`|T|=2`.                                                       (4.6)

The two elements `t_1,t_2` are incomparable Hasse predecessors of `a`, both
incomparable with `b`, so

`{b,t_1,t_2}`

is a three-element antichain. Moreover the two events `{b<t_1}` and
`{b<t_2}` are both indispensable: each has probability below `1/3`, their
union has probability above `1/3`, and neither event contains the other.

Therefore a successor-free majority-late/no-descent nested endpoint does not
leave a diffuse or arbitrarily complicated reverse obstruction. It lands in
one exact local shape: a **double-predecessor Hasse fan**.

If `D` is a chain, then `|T|=1`, so `U` must be nonempty. This recovers the
fleet03/B19 successor-continuation theorem as the chain-discrepancy special
case and explains exactly where that argument can fail after the corridor
leaves the first boundary.

If `Pred(a)=Pred(b)`, then `T` is empty and (4.3) instead forces `|U|=2`.

## 5. Application of the latest lead result

The fleet04/B10 r12 crossed-neighborhood theorem assumes, after orienting
its early/late pair `(x,y)`,

`Pred(x) subseteq Pred(y)` and `Succ(y) subseteq Succ(x)`.

Relabel `(a,b)=(y,x)`. Then the forward blocker set `M` in Corollary 3.2 is
empty, so `Q=E`. Formula (3.10) becomes

`2 Pr(x<y)-1 = R/E`.

Theorem 3.1 identifies this same `R` with the union of maximal lower and
minimal upper fringe events. Thus the lead's crossed-neighborhood union
identity is recovered exactly as the `M=empty` specialization of the present
weak-hypothesis compression.

The new content is what survives when the lead's successor nesting fails:
`Q` may become nontrivial, but `R` **still** has at most four canonical Hasse
channels. Therefore failure of crossed nesting does not restore an
unbounded reverse remainder. The next global branch-merger only has to
control a bounded `2+4` endpoint state.

## 6. Application of the named partner result

Fleet03/B19 r11 assumed the proper predecessor discrepancy `D` was a chain,
so its reverse predecessor contribution was represented by the single top
element `d=max D`. It then proved the exact union

`R = | {b<d} union union_{u in U}{u<a} |`

and, in the majority-late/no-descent branch, forced `U` nonempty.

Theorem 3.1 removes precisely the chain assumption:

`d=max D`

is replaced by the at-most-two-element antichain `T=Max D`, with no change
to the exact union logic. The partner theorem is therefore not merely cited;
its reverse-branching mechanism is extended to every width-three nested
endpoint.

This exposes the first genuinely new obstruction to iterating the partner's
successor corridor: when `U=empty`, width three allows exactly two maximal
predecessor channels to carry the required `R>E/3` mass.

## 7. Decisive local counterexample to a stronger shortcut

The previous B11 run made the minimal hard core connected in both the
comparability and incomparability graphs. A tempting strengthening would be:

> bi-connectivity plus width three rules out the double-predecessor,
> successor-free state.

That strengthening is false.

Take the six-element poset with transitive reduction

`0<1`, `0<5`, `1<3`, `1<4`, `2<3`.                            (7.1)

It has width three, connected comparability graph, and connected
incomparability graph. Let

`a=3`, `b=5`.

Then

`Pred(a)={0,1,2}`, `Pred(b)={0}`,

so

`D={1,2}`, `T={1,2}`, `U=empty`, `M=empty`.

There are exactly `E=33` linear extensions. Exact counts are

`#{a<b}=10`,                                                  (7.2)

`#{b<1}=9`, `#{b<2}=9`,                                      (7.3)

`#{b<1 and b<2}=5`,                                           (7.4)

so

`R=#{b<1 or b<2}=13`.                                         (7.5)

Thus

`Pr(a<b)=10/33<1/3`,

each predecessor atom has probability `9/33<1/3`, but their union has
probability `13/33>1/3`. Since `M=empty`, `Q=E=33`, and the endpoint identity
checks exactly:

`10/33 = 1 - (33+13)/(2*33)`.                                 (7.6)

This poset is **not** a POS3 counterexample; for example `(1,2)` is balanced
with counts `15` and `18`. Its role is narrower and decisive: connectedness
of both complementary graphs does not eliminate the double-predecessor fan.
The no-balanced/strong-majority global constraints must be used.

## 8. Exact finite regression

`verify_pos3_nested_reverse_channels_v1.py` exhaustively enumerates every
distinct transitively closed naturally labelled poset through order six. On
all width-at-most-three cases it checks every oriented incomparable nested
endpoint `Pred(b) subseteq Pred(a)` and verifies:

- `|T|<=2` and `|U|<=2`;
- every canonical element is the claimed Hasse neighbor;
- the direct definition of reverse nonneutral remainder equals the canonical
  union in (3.8).

It then verifies the six-element bi-connected witness above.

Captured counts:

- naturally labelled transitive closures through `n=6`: `5230`;
- width-at-most-three closures: `3701`;
- nested endpoint orientations checked: `33051`;
- strict nested endpoint orientations: `15651`;
- local `|T|=2,U=empty` states: `1581`;
- witness extension count: `33`;
- witness reverse union: `13`;
- zero assertion failures.

Terminal marker:

`POS3_NESTED_REVERSE_CHANNEL_COMPRESSION_V1_PASS`.

SHA-256:

- verifier:
  `e2946e7a40a561ffd07d46894e741adb8e9e57a1f8a8cbbfa82590ce1ef0fcb0`;
- captured stdout:
  `9a71734e334973f15d26fd5963e1a4876535562d7ce7b3895a9afe6090f1c41d`.

The finite regression is a self-check only. Theorem 3.1 and its consequences
are arbitrary-size proofs and do not use finite census as closure.

## 9. Exact remaining obligation

The current conditional end-to-end route is now sharper.

At the inherited first strict boundary the predecessor discrepancy is a
chain, so the majority-late/no-descent direction cannot terminate there:
`|T|=1` forces `U!=empty`, agreeing with fleet03/B19. The lead's crossed
branch additionally has a quantitative `>1/9` outward fringe selector.

After moving to later nested endpoints, however, crossed successor nesting
may fail and `D` may widen. Theorem 3.1 says there are only two ways to avoid
strict span descent:

1. **successor continuation:** `U!=empty`, providing at least one canonical
   Hasse successor channel; or
2. **double-predecessor fan:** `U=empty` and `T={t_1,t_2}`, with two
   indispensable subcritical predecessor atoms whose union has mass `>1/3`.

The first essential unpaid implication is therefore a global branch-merger
statement:

> In the series- and parallel-indecomposable minimal hard core, repeated
> canonical successor continuation cannot terminate in a double-predecessor
> fan without producing either a balanced pair, a strict strong-majority span
> descent, a forbidden width-four antichain, or a previously excluded proper
> autonomous nonchain.

The six-element witness in Section 7 proves that complementary-graph
connectivity alone cannot supply this implication. The next proof has to use
the no-balanced strong-majority order together with the lead's fringe mass
lower bounds / pinned-rank constraints or an equivalent global conservation
law.

POS3 itself remains open.

## 10. Provenance and safety

No installation or benchmark work was performed. No benchmark gold, sealed
labels, credentials, scheduler identifiers, machine paths, raw private
transcripts, email, Drive, public posting, paid model/API/Codex call, remote
workflow, permission change, or brain mutation was used.

Model self-report: `GPT-5.6 Sol`. Requested effort:
`maximum actually supported`. Configured/known effort:
`UNKNOWN / NOT_EXPOSED`. Provider reasoning-token / thinking-time counters:
`null / NOT_EXPOSED`.

The scientific run remained `WITHOUT_VERIFIED_BRAIN`; authenticated GitHub
source retrieval was used, but no authenticated brain retrieval/context was
used.
