# POS3 account01/B10 — common-cover funnel in the majority-late strict corridor

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It uses the actual uniform law on full linear extensions throughout. No deletion law is replaced by a uniform surrogate.

## 1. Source-bound state consumed

The current campaign lead is account04/B10, run `20260922T031005Z-B10-POS3-r11`, report `proofnet24/collective-POS3/account04/B10/20260922T031005Z-B10-POS3-r11/REPORT.md`. Its first-boundary funnel proves that in the strict sibling branch one may relabel incomparable siblings `a,b` so that

`Pred(b) proper_subset Pred(a)`,

`D=Pred(a)\Pred(b)` is a chain, and `d=max D` satisfies `d lessdot a`. In the majority-late orientation `b prec_* a`, absence of span descent forces `d prec_* b` and forces a minimal successor blocker `z` of `b` relative to `a`, with

`b lessdot z`, `z || a`, and `a prec_* z`.

The lead also inherits the exact endpoint identity from account01/B11,

`p_ab = 1-(Q+R)/(2E)`.

The freshest same-mechanism account03/B10 result, run `20260922T031643Z-a03-b10-pos3-r11`, closes the corresponding majority-early conditioning branch but leaves the majority-late side-channel transport unpaid.

The required named **OTHER-account partner result** used here is account02/B11, run `20260922T011526Z-b11-pos3-r12-17156e52`, report blob `8d7f5b3ea044c9ec4966ae2de35eca5bd6f54411`. For any proper autonomous chain `M={c_1<...<c_m}`, it proves the exact quotient-fiber law

`W_M(tau)=binom(m+r(tau),m)`,

so the projected full-extension law is the one-scalar binomial tilt, not a uniform quotient. This gives the correct exit branch if the common cover edge constructed below turns out to be autonomous.

A fresh adversarial input is account02/B19 run `20260922T034025Z-account02-B19-pos3-r11-c4d1b3b8`. Its exact 19-extension witness shows that a balanced equal-predecessor conditioned child need not lift the same pair: balance can migrate to side-corridor pairs. Therefore the present run does not attempt same-pair scalar lifting.

This slot's previous report `20260922T024151Z-b10-pos3-r11b` proved quantitative TP2 for the exact two-coordinate three-chain flux. The present mechanism is different: it analyzes a one-dimensional saturated-chain crossing forced by the newly sharpened majority-late corridor.

## 2. Compact conditional end-to-end route

Assume a cardinality-minimal POS3 counterexample `P` exists. The inherited strong-majority relation is a transitive total order `L_*` extending `P`. The lead's first-boundary funnel and account01/B11 endpoint exchange reduce the first unresolved strict branch to

`d lessdot a`, `b lessdot z`,

`d prec_* b prec_* a prec_* z`,

with `d||b`, `a||b`, `a||z`, and with no shorter extreme incomparable pair between `b,a` unless the argument has already descended.

The first missing transport step splits according to the relation between the incoming and outgoing Hasse endpoints `d,z`.

This run pays the entire **comparable-endpoint geometry**: if `d<z`, then either a shorter extreme pair already occurs along a saturated `d-z` chain, or both `a` and `b` cross one and the same Hasse edge with probability strictly larger than `1/3`. This concentrates the majority-late residue onto a single exact full-extension edge flux.

## 3. New theorem: common-cover funnel

### Theorem 3.1 — double crossing of one cover edge

Let `P` be a hypothetical no-balanced width-at-most-three counterexample in the lead's majority-late strict-corridor state. Thus `a||b`,

`d lessdot a`, `b lessdot z`,

and, in the strong-majority total order,

`d prec_* b prec_* a prec_* z`.

Assume additionally `d<z` in `P`. Choose any saturated chain

`C: c_0=d lessdot c_1 lessdot ... lessdot c_k=z`.

Then exactly one of the following occurs.

1. Some internal `c_i` lies strictly between `b` and `a` in `L_*`; then at least one of `(b,c_i)` or `(c_i,a)` is an incomparable strong-majority pair of strictly smaller `L_*` span than `(b,a)`.

2. There is an index `j` such that, with `l=c_j` and `u=c_{j+1}`,

`l lessdot u`,

and under the original uniform law on all linear extensions,

`Pr(l<b<u) > 1/3`,

`Pr(l<a<u) > 1/3`.

In the no-span-descent subbranch, alternative 2 necessarily holds.

### Proof

Because `L_*` extends `P`, the saturated chain is increasing in `L_*`:

`c_0 prec_* c_1 prec_* ... prec_* c_k`.

Suppose an internal `c_i` satisfies

`b prec_* c_i prec_* a`.

Both relations `b<c_i` and `c_i<a` cannot hold in `P`, because transitivity would imply `b<a`, contradicting `a||b`. Hence at least one of `b||c_i` or `c_i||a` holds. The corresponding incomparable pair is strongly oriented as displayed and has strictly smaller `L_*` span. This proves alternative 1.

Now assume no such internal chain point exists. Since `d prec_* b prec_* a prec_* z` and the chain is increasing, there is a unique adjacent chain edge

`l=c_j lessdot c_{j+1}=u`

such that

`l prec_* b prec_* a prec_* u`.                                      (3.1)

Fix `x in {a,b}`. Set

`q_x(v)=Pr(x<v)`.

Because `l<u` in every linear extension,

`Pr(l<x<u)=Pr(x<u)-Pr(x<l).`                                        (3.2)

The first term is strictly larger than `2/3`: if `x<u` in the poset it equals `1`; otherwise `x||u`, and (3.1) plus no balanced pair gives `Pr(x<u)>2/3`.

The second term is strictly smaller than `1/3`: if `l<x` in the poset it equals `0`; otherwise `l||x`, and (3.1) plus no balanced pair gives `Pr(x<l)<1/3`.

Substituting in (3.2) gives

`Pr(l<x<u)>1/3`.

Applying this once for `x=b` and once for `x=a` proves alternative 2. `square`

### Threshold formulation

Along the same saturated chain define

`q_i=Pr(b<c_i)`, `r_i=Pr(a<c_i)`.

The lead's corridor gives `q_0<1/3`, `r_0=0`, `q_k=1`, `r_k>2/3`. If every relevant chain pair is extreme, each sequence jumps from below `1/3` to above `2/3`. Transitivity of `L_*` forbids the `a`-jump from occurring before the `b`-jump, while a strictly earlier `b`-jump places a chain point between `b,a` and gives span descent. Hence in the no-descent case the two jump indices coincide. If the common jump is across `c_j lessdot c_{j+1}`, then

`q_{j+1}-q_j = Pr(c_j<b<c_{j+1})>1/3`,

`r_{j+1}-r_j = Pr(c_j<a<c_{j+1})>1/3`.

This is the same conclusion expressed directly as an exact one-dimensional lattice-path edge flux.

## 4. Why this is a real narrowing, not closure

The account02/B19 19-extension witness has the side chain

`d<r_1<r_2<u`

and balance appears at `Pr(b<r_1)=9/19` and `Pr(a<r_2)=10/19`. It therefore exits through alternative 1 / a side balanced pair before the common-cover concentration is reached. This is exactly why its failure of same-pair conditioning does not refute Theorem 3.1.

In a true counterexample, where those side pairs are forbidden from being balanced, the comparable-endpoint branch can no longer spread the lost conditioning mass arbitrarily along the corridor: it must concentrate both endpoint insertions onto one Hasse edge.

There is a useful structural dichotomy at that edge. If no outside element distinguishes `l` from `u`, then `M={l<u}` is a proper autonomous chain. The account02/B11 theorem applies with `m=2`, and the exact quotient weight is

`W_M(tau)=binom(r(tau)+2,2)`.

Thus this branch is handed to the partner's exact autonomous-chain migration problem without any uniform-quotient substitution. If `M` is not autonomous, an outside relation-distinguisher is attached to a Hasse edge on which **both** endpoint insertion events have mass `>1/3`; this is a substantially narrower global transport object than the original arbitrary nested corridor.

## 5. Relation to the exact three-chain flux

The previous account01/B10 TP2 theorem says that for any fixed element the full two-chain insertion matrix is TP2 under the genuine uniform extension law. Theorem 3.1 identifies, in the majority-late comparable-endpoint residue, a particular cover transition at which two different endpoint insertions are simultaneously heavy.

What is still missing is not the sign of one element's two-coordinate flux. It is an **inter-element transport inequality** across this doubly crossed cover edge: in the module-prime branch, use width three and the forced external distinguisher(s) to show that two `>E/3` insertion channels cannot coexist without producing either a balanced pair, a shorter extreme pair, or the next corridor state with strictly decreased global potential.

The separate branch `d||z` is also not paid by this theorem.

## 6. Exact finite regression

`verify_common_cover_funnel.py` exhausts all transitively closed naturally labelled posets through `n=6`, filters width at most three, enumerates all linear extensions exactly, and tests every local tuple/saturated path satisfying the theorem's probability and strong-order fragment hypotheses. It does not certify POS3; it checks this local implication only.

Output:

`stats {4: (40, 39, 0, 0, 0), 5: (357, 314, 0, 0, 0), 6: (4824, 3339, 195, 0, 195)}`

`failures 0`

`minimum_verified_common_cover_mass 25/37`

`POS3_COMMON_COVER_FUNNEL_CHECK_PASS`

The tuples for `n=6` give 195 nonvacuous common-cover instances after the exact filters; every one has the required shared cover edge. The observed `25/37` minimum is regression data only, not a claimed universal strengthening of `1/3`.

## 7. First remaining implication

The first essential missing implication after this run is now:

> **Double-crossed-cover transport.** In the module-prime majority-late branch, suppose a Hasse edge `l lessdot u` and incomparable `a,b` satisfy `l prec_* b prec_* a prec_* u` together with `Pr(l<b<u)>1/3` and `Pr(l<a<u)>1/3`, and retain the lead's incoming/outgoing Hasse geometry and all no-balanced width-three constraints. Prove that an external distinguisher of `l,u` forces either a balanced pair or strict descent of a well-founded corridor potential.

Paying that statement would close the `d<z` majority-late residue. The `d||z` residue would still need a separate argument before the parent target is closed.

No claim of a full POS3 proof, finite-frontier improvement, novelty/priority, or verified brain use is made.
