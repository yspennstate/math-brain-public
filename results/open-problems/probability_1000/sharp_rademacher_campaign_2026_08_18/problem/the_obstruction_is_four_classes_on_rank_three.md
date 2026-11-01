# The two mechanisms are one: four π-classes spanning three dimensions

> **[CORRECTED IN §6 — read that before using the title claim.]** Two things are wrong with it. The *rank* half ("on rank three") is **forced by minimality**, not measured: every minimal Rado violation has deficiency exactly 1, by a one-line argument. And the *size* half is not universal: 17 of 18 uncovered configurations give size 4, but one gives **6 classes on rank 5**. What survives is the **composition** distinction — all-private (A) versus two-straddling-sharing-a-boundary-part (B) — which is unaffected.

Author: main session c53c1d50, 2026-08-19 ~11:3x. **This corrects `beta_is_the_absorption_threshold.md` §16, which split the uncovered configurations into two mechanisms and said the second was unexplained.** They are the same mechanism.

## 1. What was split

§16 found that the 136 uncovered configurations divide by whether the private part contains a whole constraint:

- **Mechanism A** — a constraint wholly inside `Q`. Four configurations, all at `L = β`. This is what the quarter story explains.
- **Mechanism B** — no constraint wholly inside `Q`; every one straddles `W`. **132 of the 136**, and §16 said plainly that my account did not explain them.

## 2. What the obstruction actually is

Absorbability is a matroid transversal problem, so the exact failure is Rado's condition: some subfamily of π-classes spans less than its own size. Computing the **minimal violating subfamily** on one example of each type — cheap for a single configuration — gives the same answer every time:

> **Four π-classes spanning only rank three.**

| configuration | violation | the four forms |
|---|---|---|
| threshold object, `W=(0,1,4)` | 4 classes, rank 3 | `e₂`, `e₃`, `e₅`, and `e₂+e₃+e₅` — all **private** |
| book `p=4`, `W=(0,2,3)` | 4 classes, rank 3 | `e₀+e₁+e₄`, `e₀+e₁+e₅` (**straddling**), `e₄`, `e₅` (private) |
| candidate `r=5`, `W=(0,4)` | 4 classes, rank 3 | `e₀+e₁+e₃`, `−(e₀+e₂+e₃)` (**straddling**), `e₁`, `e₂` (private) |

**The same count, the same deficiency, from two different-looking causes.**

## 3. Why mechanism B collapses

In both B cases the two straddling forms have **the same boundary part, up to sign**:

- book: `e₀+e₁+e₄` and `e₀+e₁+e₅` restricted to `W = {0,2,3}` are both `(1,0,0)` — identical;
- candidate: `e₀+e₁+e₃` and `−(e₀+e₂+e₃)` restricted to `W = {0,4}` are `(1,0)` and `(−1,0)` — identical up to sign.

So their **difference is purely private** (`e₄−e₅` and `e₁−e₂` respectively), and therefore already lies in the span of the private coordinates that form the other two classes. Four forms, three dimensions.

> **The unified statement: the obstruction is four π-classes on rank three, arising either from a private homogenizer (A) or from two forms sharing a boundary part with differing private parts (B).**

## 4. Why this connects to something the campaign already had

Mechanism B is a dual restatement of a condition the campaign derived months of work ago from the other side. `the_two_clauses_are_in_tension.md` concluded that both clauses hold exactly when **boundary parts are constant on private-sharing clusters**. Here the failure is the mirror image: **forms sharing a boundary part with differing private parts.** Same structure, read on the dual instead of the rows.

That is worth more than the unification itself. It means the obstruction found by this session's absorbability machinery and the obstruction found by the campaign's clause-tension analysis are **the same object approached from opposite sides** — one of the few places where two independent lines here have met.

## 5. Status and limits

**Established:** the minimal Rado violation is 4-classes-on-rank-3 in all three configurations examined, with the forms and their supports printed; and in both B cases the two straddling forms have equal-up-to-sign boundary parts, verified directly.

**Not established:** that 4-on-3 is the *only* violation shape. Rado violations can be any size, and three configurations were examined, not the 136. A violation of size 5-on-4 or larger may well occur elsewhere in the uncovered set — the natural next check, and cheap, since the minimal-violation search is fast per configuration.

**Also unchanged:** everything is NAE-triple fibres at small `r`, and every object remains a known non-member of the residual class.

## 6. Correction: deficiency 1 is forced, and 4-on-3 is not the only size

The cheap check §5 called for — run the minimal-violation search over the whole uncovered set rather than three samples — returns two corrections, and the second is more useful than the original claim.

**First, an exception.** Over 18 uncovered configurations: **17 have a minimal violation of 4 classes on rank 3, and one does not.** The candidate at `W = (1,2,3)` gives **6 classes on rank 5**, with a mixed composition — 2 private forms, 7 straddling, 3 boundary — unlike the clean all-private (A) and two-straddling (B) patterns. So "the obstruction is four classes on rank three" is **false as a universal statement**.

**Second, and more important: half of the original observation was a triviality.** Both shapes are "`k` classes spanning rank `k−1`" — deficiency exactly 1. That is **forced by minimality**, not discovered:

> If a minimal violating subfamily `J` had `rank(union) < |J| − 1`, then dropping any one class leaves `|J| − 1` classes spanning at most `rank(union) < |J| − 1` — still a violation, contradicting minimality. So every minimal Rado violation has deficiency exactly 1. ∎

One line, no computation. **So the deficiency was never evidence of anything**, and the only empirical content in "4 on 3" is the *size* 4 — which the sweep now shows is 17 of 18, not universal.

**What survives, restated at the right strength.**

- Deficiency 1: a theorem about minimal violations, true everywhere, carrying no information about these objects.
- Minimal-violation **size**: 4 in 17 of 18 configurations, 6 in one. An empirical regularity with a known exception, not a law.
- The **composition** distinction is real and is the part worth keeping: the size-4 violations split cleanly into all-private (mechanism A, at `L = β`) and two-straddling-plus-two-private (mechanism B), and in every B case the two straddling forms share a boundary part up to sign so their difference is purely private. That, and its correspondence with the campaign's "boundary parts constant on private-sharing clusters", is unaffected by either correction.

**The pattern in my own error, since it is the second time today.** I read a *structural* observation (four classes, rank three) off cases where one half of it — the rank — was determined by the definition of minimality rather than by the objects. The same shape as reading a bound as a value: a quantity that could not have come out otherwise, treated as though it had been measured. **Before calling a computed pattern a finding, ask what the pattern's degrees of freedom actually were.**
