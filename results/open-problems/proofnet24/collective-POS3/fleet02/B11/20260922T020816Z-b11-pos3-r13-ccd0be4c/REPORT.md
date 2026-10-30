# POS3 fleet02/B11 — one-step affine chain-module reduction

**Run:** `20260922T020816Z-b11-pos3-r13-ccd0be4c`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent POS3 status:** **OPEN / NOT PROVED**  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

This report stays within the finite-width-three target under the uniform law on all
linear extensions.  No finite census below is treated as arbitrary-size closure.

## 1. Source-bound state consumed

Fresh owner control revision `2026-09-22.2` assigns this slot to POS3 and stops
the older installation/benchmark work.

The mathematical state used here is:

1. fleet02/B11 prior report blob
   `8d7f5b3ea044c9ec4966ae2de35eca5bd6f54411`: a cardinality-minimal
   counterexample may be assumed to have connected incomparability graph; for a
   proper autonomous chain `M` of size `m`, deletion of all of `M` induces the
   exact binomial corridor weight `binom(m+r,m)`.
2. campaign lead fleet04/B10 report blob
   `1e5a9682e4f90f38484a86e7199428de0b0160f8`: in any no-balanced
   width-at-most-three candidate, every element has probability `>1/81` of
   occupying its rank in the common strong-majority order; the corresponding
   three-chain central flux cell satisfies `81 W > E`.
3. named partner fleet03/B19 report blob
   `b32278d17e70387d51be17fd0d0ac912bae48f5e`: an exact connected,
   module-prime width-three example shows that module-primality plus absence of
   extremal balanced pairs does **not** force a light insertion distribution.
   Any post-reduction proof must use global alignment/blocker compatibility.
4. fleet04/B19 report blob
   `f11967a121d6c257ff510714cfb49cf27467198a`: for an autonomous
   chain, the deleted law is controlled by the central neutral-corridor length;
   a minimal counterexample can contain such a chain only in the
   **boundary-active** case.  Its earlier module theorem, recorded there as
   dependency blob `ce30dae79d698103f026d4d871033238489b1fb1`, eliminates
   proper autonomous nonchains from a cardinality-minimal counterexample.

The point of the present run is to use cardinality minimality *one element at a
time*.  This replaces the high-degree direct binomial tilt by an exact affine
size-bias and sharply narrows the remaining chain-module obligation.

## 2. Conditional end-to-end route

Assume POS3 is false and choose a counterexample `P` of minimum cardinality.

- The known width-two theorem gives `width(P)=3`.
- The prior fleet02/B11 ordinal decomposition gives connected
  incomparability graph.
- fleet04/B19 eliminates every proper autonomous nonchain.
- Hence the only proper autonomous subset that can remain is a chain
  `M={c_1<...<c_m}`, `m>=2`, and fleet04/B19 further says it must be
  boundary-active.
- The theorem below deletes only the top member `x=c_m`.  The smaller poset
  `P^- = P-x` **still has width exactly three and connected incomparability
  graph**, while the exact change from the uniform law of `P^-` to that of `P`
  is a one-dimensional affine size-bias.
- Therefore it is enough to prove the one-step migration lemma in Section 6.
  That lemma would rule out every proper autonomous chain and make the minimal
  counterexample fully module-prime.
- The named partner's module-prime certificate then shows that this would not
  finish POS3 by a light-slice shortcut.  The genuinely unresolved core would
  still have to reconcile the common strong-majority alignment, the `>E/3`
  heavy slices, the lead's `>E/81` pinned central cells, and the boundary/blocker
  constraints.

Thus the first unpaid implication in this structural branch is now a
**boundary-active one-step affine migration statement**, not the previous
all-at-once binomial migration statement.

## 3. Deleting one endpoint preserves the hard structural class

Let `M={c_1<...<c_m}`, `m>=2`, be a proper autonomous chain of a
width-three poset `P` whose incomparability graph is connected.  Put
`x=c_m`, `c=c_{m-1}`, and `P^-=P-x`.

Autonomy partitions the elements outside `M` into

- `D`: below every member of `M`;
- `N`: incomparable with every member of `M`;
- `U`: above every member of `M`.

As in the prior corridor theorem, `width(N)<=2`.

### Proposition 3.1

`width(P^-)=3`, the incomparability graph of `P^-` is connected, and
`M^-={c_1<...<c_{m-1}}` remains an autonomous chain.

### Proof

Deleting `x` cannot increase width.  Conversely, take a three-element
antichain of `P`.  If it avoids `x`, it remains in `P^-`.  If it contains
`x`, its other two members must lie in `N`, hence are incomparable with every
member of `M`; replacing `x` by `c` gives a three-element antichain of
`P^-`.  Thus the width stays three.

In the incomparability graph, the members of `M` are pairwise nonadjacent
false twins: they have the same outside neighborhood `N`.  Since the graph of
`P` is connected, `N` is nonempty.  Any path using `x` can replace the segment
through `x` by the surviving twin `c`.  Therefore deleting `x` leaves the
incomparability graph connected.  Autonomy of `M^-` is immediate. `□`

For a cardinality-minimal counterexample, `P^-` is therefore a smaller
nonchain in exactly the same width-three connected class, so it has a balanced
pair.

## 4. Exact one-step affine fiber law

Fix `lambda in L(P^-)`.  Every predecessor of `x` is already before `c`,
and every successor of `x` lies in `U`.  Let

`s(lambda)`

be the number of neutral elements `z in N` that occur after `c` and before the
first element of `U` in `lambda` (with a sentinel after the word if `U` is
empty).

### Theorem 4.1 — one-step fiber

Deleting `x` maps `L(P)` onto `L(P^-)`, and the fiber over `lambda` has
exactly

`1+s(lambda)`

extensions.

### Proof

The new top element `x` must be inserted after `c` and before the first
`U`-element.  Every element strictly between those boundaries is in `N` and is
incomparable with `x`.  Hence there is one legal insertion gap before the first
such neutral element, one between each consecutive pair, and one after the
last: exactly `s+1`.  Every legal lift arises uniquely in this way. `□`

Let `E_-` and `Cov_-` denote expectation and covariance under the **uniform**
law on `L(P^-)`.  For any event `A` depending only on old elements,

`Pr_P(A) = E_-[(s+1) 1_A] / E_-[s+1]`

and therefore

`Pr_P(A)-Pr_-(A) = Cov_-(s,1_A)/(1+E_-[s]).`             (4.1)

This is the exact one-step defect.  It applies equally to an old outside pair
and to a pair involving one of `c_1,...,c_{m-1}`.

### Boundary-covariance localization

For `z in N`, define

`J_z(lambda)=1{ c precedes z and z precedes every u in U in lambda }`,

with the second condition vacuous if `U` is empty.  Then

`s = sum_{z in N} J_z`.

Consequently every old-pair probability defect splits exactly as

`Pr_P(A)-Pr_-(A)
 = [sum_{z in N} Cov_-(J_z,1_A)]/(1+E_-[s]).`          (4.2)

Since `width(N)<=2`, the entire chain-module defect is now localized to
boundary events carried by a width-at-most-two neutral region.

This is the natural point at which to connect the autonomous-chain reduction
to the collective boundary/flux methods: if an old balanced pair is destroyed,
at least one explicit neutral boundary event has the required signed
correlation with its order event.

## 5. Relation to the previous binomial corridor law

Let `Q=P\M`, let `r(tau)` be the active neutral-corridor length in
`tau in L(Q)`, and let `nu_{m-1}` be the law on `L(Q)` induced by a uniform
extension of `P^-`.

The old all-at-once fiber weights are

`w_t(tau)=binom(t+r(tau),t)`.

The ratio between consecutive module lengths is only

`w_m/w_{m-1} = (m+r)/m`.                               (5.1)

Hence, for an event `A` involving only elements of `Q`,

`Pr_P(A)
 = E_{nu_{m-1}}[(m+r)1_A]/E_{nu_{m-1}}[m+r]`

and

`Pr_P(A)-Pr_{P^-}(A)
 = Cov_{nu_{m-1}}(r,1_A)/(m+E_{nu_{m-1}}[r]).`  (5.2)

So cardinality minimality removes the high-degree binomial obstruction:
the last inflation step is an **affine tilt in corridor length**.

As a quantitative byproduct, the total-variation distance between the uniform
law on `L(P^-)` and its projection from the uniform law on `L(P)` is exactly

`TV = E_-|s-E_-s| / (2(1+E_-s))
    <= sqrt(Var_-(s)) / (2(1+E_-s)).`                    (5.3)

Thus any balanced pair of `P^-` lying farther than `TV` from both endpoints
`1/3,2/3` must survive.  A minimal counterexample with an autonomous chain
must therefore put every balanced pair of `P^-` inside this boundary layer.
In particular `s` cannot be constant.

## 6. First missing implication: one-step autonomous inflation

The exact remaining lemma is:

> **One-step autonomous inflation lemma (candidate).**
> In the setup above, if `P^-` has a balanced incomparable pair, then after
> adjoining the new top member `x` either
> 1. some pair already balanced in `P^-` remains balanced in `P`, or
> 2. `x` has a balanced incomparable pair in `P`.

For the minimal-counterexample argument this is sufficient: Proposition 3.1
and cardinality minimality give the antecedent, while either conclusion
contradicts that `P` is a counterexample.

Both alternatives are genuinely necessary.

### 6.1 Old-pair survival alone is false

Let `P^-` be a three-element chain `a_0<a_1<a_2` plus an isolated module
point `c_1`.  It has four linear extensions, and its only balanced
module/outside pair is

`Pr(c_1<a_1)=1/2`.

Inflate `c_1` to `c_1<c_2`.  There are `10` extensions.  The corresponding
middle comparisons become

`Pr(c_1<a_1)=7/10`,  `Pr(c_2<a_1)=3/10`,

so the old balanced comparison is destroyed and neither chain member balances
against `a_1`.  But the new top is rescued elsewhere:

`Pr(c_2<a_2)=3/5`.

Thus one cannot prove the candidate by old-pair preservation only.

### 6.2 A balanced pair involving the new top is not automatic

Start from a two-element antichain and replace one point by the chain
`c_1<c_2`.  The resulting `P^-` has three extensions and both cross
probabilities are boundary-balanced (`1/3` and `2/3`).  Inflate once more to
`c_1<c_2<c_3`.  The new top satisfies

`Pr(c_3<z)=1/4`,

so it has no balanced pair with the only incomparable outside element.
Nevertheless an old pair survives with

`Pr(c_2<z)=1/2`.

Thus the new-top branch alone is also false; the OR in the candidate is
structural, not cosmetic.

## 7. Exact finite stress test of the one-step candidate

The companion standard-library verifier enumerates every naturally labelled
transitively closed poset `R` through `|R|<=6`, every choice of a point to
replace, and module lengths `m=2,3`.  It substitutes that point by chains of
length `m-1` and `m`, retains width at most three, and checks the candidate
exactly using integer linear-extension counts.

The output is:

- naturally labelled posets by size `2,3,4,5,6`:
  `2,7,40,357,4824`;
- substitutions examined: `61,828`;
- width-at-most-three substitutions retained: `43,570`;
- retained cases whose smaller poset has a balanced pair: `43,530`;
- old-pair survival: `43,413`;
- new-top balanced pair: `31,324`;
- both branches: `31,207`;
- old-only: `12,206`;
- new-top-only: `117`;
- failures of both branches: `0`.

The zero is finite adversarial evidence only.  The generated instances are not
claimed independent or nonisomorphic, and this computation is **not** used as
proof for arbitrary size.

Verifier SHA-256:
`60406042d0fc296e12e4b0c328bd8033014a977ffea161476713e5aea498886b`.

Captured output SHA-256:
`cef65a17abb76bab819fc62f927f61d06fef65f9945c43e4ae826c858fd5ef9e`.

Terminal marker:
`POS3_ONE_STEP_AUTONOMOUS_MIGRATION_STRESS_PASS`.

## 8. Named partner applied and genuinely unresolved core

The named partner fleet03/B19 exact certificate is important after this
reduction, not merely background.  Its nine-element example is connected and
module-prime, has no balanced extremal-anchor pair, yet every relevant
insertion distribution has a slice larger than one third; its only balanced
pairs are interior.  Therefore proving the one-step lemma above would
legitimately eliminate the last module branch, but it would **not** justify the
false next step “module-prime implies a light slice.”

The campaign lead's theorem supplies the correct additional surviving
constraint: in a true counterexample every element also carries `>E/81` mass
in its majority-rank central cell.  The first module-side obligation is now the
one-step affine lemma; after it, the first global obligation is an
alignment/conservation inequality coupling the `>E/3` heavy marginals,
`>E/81` pinned cells and the consecutive-boundary blocker data.

## 9. Status and next mathematical action

`ESSENTIAL_STEP_APPLIED`, not a full proof.

The previous direct autonomous-chain deletion left a polynomial binomial tilt
`binom(m+r,m)`.  Cardinality minimality now shows that only the final
single-element inflation needs to be controlled, where the exact Radon-Nikodym
factor is affine (`s+1`, or `m+r` on the outside quotient).

The next proof attempt should attack (4.2) directly: if every old balanced pair
is driven across an endpoint, use `width(N)<=2` and the signs of the finitely
many boundary covariances `Cov(J_z,1_A)` to force a balanced pair involving
the new top `x`.  The finite stress test and the two exact one-sided
counterexamples indicate that a proof must couple the two rescue mechanisms,
not optimize either separately.

No finite census is treated as closure; no benchmark data, credentials,
scheduler identifiers, machine paths, private transcripts, email/Drive,
paid API/model/Codex call, remote workflow, public posting, or permission
change is used.
