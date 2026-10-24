Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# F0106 — exact six-cycle shared-mass dual and a complete C6 witness theorem

Date: 2026-09-18  
Slot: `R7-04`  
Target: `F0106` — Michel Talagrand, *Are Many Small Sets Explicitly Small?*, canonical Conjecture 7.9 / author-preprint Conjecture 7.8, with canonical dual Conjecture 7.12 / author-preprint Conjecture 7.11.  
Methods: **B11 dualize / B16 exact small cases / B19 constructive algorithm**.

This artifact continues the already-admitted outside source. It proves a new restricted theorem for the complete six-cycle minimal-witness class and exactly solves the selected rational recovery LP. It does **not** prove the universal Talagrand conjecture, so the source status remains PARTIAL / OPEN.

## 1. Setup

Let the ground set be `S={0,1,2,3,4,5}` with indices modulo 6, and let

`E_i={i,i+1}`

be the six edges of the cycle `C6`. Define the up-class

`A_6 = {K subseteq S : E_i subseteq K for at least one i}.`

For `0<alpha,p<1`, put

`r=alpha p`

and

`m(p)=mu_p(A_6).`

For a deterministic `J subseteq S`, write

`theta_J = theta_{J,alpha}(A_6)`

for the probability that the `alpha`-thinning of `J` contains at least one cycle edge.

Talagrand's dual asks for a probability law `eta` on `2^S` such that for every `J`

`theta_J <= m(p) * sum_I eta(I) h(I,J),`

where

`h(empty,J)=1`

and, for nonempty `I`,

`h(I,J)=r^(-|I|) 1_{I subseteq J}.`

A subprobability satisfying the same inequalities may be padded at the empty set, because extra empty-set mass only increases the right-hand side.

The exact Bernoulli probability is

`m(p)=p^2 M(p),`

where

`M(p)=6-6p-3p^2+6p^3-2p^4.`

This follows by subtracting the independent-set polynomial of `C6` from 1; the independent-set counts are `1,6,9,2`.

---

# 2. B11 — solve the selected shared-mass dual rather than the witness cover

The STUCK1 report selected the exact stress point

`alpha=37/50, p=73/100, r=2701/5000`

because the simple six-edge principal-cover certificate has mass strictly above one there.

The full dual LP at fixed `(alpha,p,A_6)` can be written as the minimum total nonnegative mass

`min sum_I w_I`

subject to

`sum_{I subseteq J} r^(-|I|) w_I >= theta_J/m(p)`

for every `J subseteq S`.

If the optimum is at most one, padding at the empty set gives a Talagrand dual probability measure.

## 2.1 D6 reduction

The objective, the constraints, and `A_6` are invariant under the dihedral group `D6`. Averaging any feasible `w` over `D6` preserves feasibility and objective value. Therefore an optimum exists with constant weight on each subset orbit.

There are exactly 13 `D6`-orbits of subsets of `S`. The exact finite checker accompanying this artifact constructs them directly and verifies the full 64-constraint LP through this reduction.

## 2.2 The shared-mass primal certificate

Let

`Q_0={0,1,3,4},`
`Q_1={1,2,4,5},`
`Q_2={2,3,5,0}.`

Each `Q_j` is the union of a pair of opposite cycle edges.

Define the following nonzero subprobability masses:

`w_empty = alpha^3/m(p),`

`w_E = alpha^4 p^2(1-alpha)/m(p)` for each of the six cycle edges `E`,

`w_Q = alpha^7 p^4(1-alpha)/m(p)` for each of `Q_0,Q_1,Q_2`.

The total mass is

`T(alpha,p)
 = [alpha^3
    +6 alpha^4 p^2(1-alpha)
    +3 alpha^7 p^4(1-alpha)]/m(p).`                  (2.1)

For a set `J`, let

`e(J)=# {cycle edges E: E subseteq J}`

and

`q(J)=# {Q_0,Q_1,Q_2 subseteq J}.`

Multiplying the Talagrand dual right-hand side by `m(p)`, the unpadded subprobability gives exactly

`R(J)
 = alpha^3
   + e(J) alpha^2(1-alpha)
   + q(J) alpha^3(1-alpha).`                         (2.2)

Indeed

`r^(-2) w_E m(p)=alpha^2(1-alpha)`

and

`r^(-4) w_Q m(p)=alpha^3(1-alpha).`

Thus feasibility is independent of `p`; only the total-mass test (2.1) depends on `p`.

---

# 3. B16 — every one of the 64 inequalities, exactly

Up to `D6`, the 64 ambient sets have 13 types. The following table gives a representative, the pair `(e(J),q(J))`, the exact thinning probability, and the slack `R(J)-theta_J`.

| type | representative | `e(J)` | `q(J)` | `theta_J` | exact slack |
|---|---|---:|---:|---|---|
| 0 | `empty` | 0 | 0 | `0` | `alpha^3` |
| 1 | `{0}` | 0 | 0 | `0` | `alpha^3` |
| 2 | `{0,1}` | 1 | 0 | `alpha^2` | `0` |
| 3 | `{0,2}` | 0 | 0 | `0` | `alpha^3` |
| 4 | `{0,1,2}` | 2 | 0 | `alpha^2(2-alpha)` | `0` |
| 5 | `{0,3}` | 0 | 0 | `0` | `alpha^3` |
| 6 | `{0,1,3}` | 1 | 0 | `alpha^2` | `0` |
| 7 | `{0,1,2,3}` | 3 | 0 | `alpha^2(3-2alpha)` | `0` |
| 8 | `{0,2,4}` | 0 | 0 | `0` | `alpha^3` |
| 9 | `{0,1,2,4}` | 2 | 0 | `alpha^2(2-alpha)` | `0` |
| 10 | `{0,1,3,4}` | 2 | 1 | `2alpha^2-alpha^4` | `0` |
| 11 | `{0,1,2,3,4}` | 4 | 1 | `alpha^2(alpha^3-alpha^2-3alpha+4)` | `alpha^3(1-alpha)(1+alpha)` |
| 12 | `S` | 6 | 3 | `alpha^2(6-6alpha-3alpha^2+6alpha^3-2alpha^4)` | `2alpha^3(1-alpha)(2+2alpha-alpha^2)` |

Every slack is nonnegative for `0<alpha<1`. Hence:

### Lemma 3.1 — shared-mass pointwise majorant

For every `0<alpha<1`, every `0<p<1`, and every `J subseteq S`, the masses in Section 2 satisfy all Talagrand dual inequalities. Therefore, whenever `T(alpha,p)<=1`, the source domination inequality holds on the six-cycle up-class `A_6` against **every** `alpha p`-spread law.

The exact checker independently enumerates all 64 constraints with rational arithmetic at the selected stress point.

---

# 4. Exact optimum at the selected rational stress point

At

`alpha=37/50, p=73/100`

we have

`m(p)=476262636611/500000000000`

and the shared masses give

`T
 =2661818171668307599067
  /3720801848523437500000`

`=0.7153883168287027... < 1.`

Thus the former cover-resistant instance is not close to violating the full Talagrand dual: the exact margin to total mass one is

`1058983676855129900933
 /3720801848523437500000`

`=0.2846116831712973... .`

The exact checker also proves this value is the **full LP optimum**, not merely the value of one feasible construction.

For the 13-orbit reduced primal, a dual optimum is supported on only three constraint orbits:

1. adjacent pairs,
2. consecutive triples,
3. opposite-edge-union four-sets.

With `r=2701/5000`, set

`y_2 = 2-6r^2
     =3113797/12500000,`

`y_4 = 6r^2-3r^4-1
     =309641522747597/625000000000000,`

`y_10=3r^4
     =159668627252403/625000000000000.`

They are nonnegative and sum to one. Direct exact orbit-incidence verification gives every reduced dual constraint, and its objective equals the primal value `T` above. By `D6` averaging, the reduced and full LP optima coincide.

So the selected recovery model is decided exactly:

### Proposition 4.1 — exact stress-point LP value

For `A_6`, `alpha=37/50`, `p=73/100`,

`C_{alpha p,A_6}
 =2661818171668307599067
  /3720801848523437500000
 <1.`

In particular this exact finite model cannot refute F0106.

---

# 5. B19 — a two-certificate algorithm closes the entire C6 witness class through alpha=3/4

The exact stress point suggests a general constructive rule:

1. try the simple edge-supported principal-cover certificate;
2. only when that runs out of mass, switch to the shared empty/edge/opposite-edge-union certificate of Section 2.

This dichotomy completely resolves `A_6` for every `alpha<=3/4`.

## 5.1 First certificate: the six-edge cover

Using the six cycle edges as the cover, the preceding cover theorem gives a valid dual certificate whenever

`6 alpha^4 p^2 <= m(p).`                             (5.1)

Since `m(p)=p^2 M(p)`, condition (5.1) is

`6 alpha^4 <= M(p).`                                 (5.2)

## 5.2 If the cover fails, p is already large

Assume

`0<alpha<=3/4, p<alpha`

and the cover fails. Then

`M(p)<6alpha^4 <= 6(3/4)^4 =243/128.`                (5.3)

Now

`M'(p)=-2(4p^3-9p^2+3p+3).`

The cubic in parentheses has the useful decomposition

`4p^3-9p^2+3p+3
 =1+(1-p)(-4p^2+5p+2).`

The quadratic `-4p^2+5p+2` is concave and is at least `2` on `[0,1]`, so the cubic is at least `1`. Hence `M` is strictly decreasing on `[0,1]`.

At `p=7/10`,

`M(7/10)=9539/5000`

and

`9539/5000 -243/128 =749/80000 >0.`

Therefore (5.3) forces

`p>7/10.`                                             (5.4)

## 5.3 In that large-p regime the shared certificate has huge slack

Because `A_6` is increasing,

`m(p)>m(7/10)`

whenever `p>7/10`, and exactly

`m(7/10)=467411/500000.`                              (5.5)

For the shared certificate numerator in (2.1), use `p<alpha`:

`N(alpha,p)
 :=alpha^3
   +6alpha^4p^2(1-alpha)
   +3alpha^7p^4(1-alpha)`

`<= g(alpha)
 :=alpha^3+6alpha^6(1-alpha)+3alpha^11(1-alpha).`      (5.6)

For `0<alpha<=3/4`,

`g'(alpha)
 =3alpha^2[
    1
    +alpha^3(12-14alpha)
    +alpha^8(11-12alpha)
   ] >0,`

because `12-14alpha>=3/2` and `11-12alpha>=2`. Hence

`g(alpha)<=g(3/4)
 =12088305/16777216.`                                 (5.7)

Finally,

`467411/500000
 -12088305/16777216
 =56178212743/262144000000
 >0.`                                                  (5.8)

Combining (5.4)--(5.8),

`N(alpha,p)<m(p),`

so `T(alpha,p)<1`, and the shared certificate works whenever the simple cover fails.

## 5.4 The p>=alpha regime

If `p>=alpha`, then for every up-class `A` and every deterministic `J`,

`theta_{J,alpha}(A)
 <= theta_{S,alpha}(A)
 =mu_alpha(A)
 <=mu_p(A).`

Thus the single dual measure `eta=delta_empty` already proves the desired inequality.

Putting the three cases together gives the main restricted theorem.

### Theorem 5.1 — complete six-cycle witness theorem

Let `A_6` be the up-class on six coordinates whose minimal witnesses are the six edges of a cycle. For every

`0<alpha<=3/4,`

every

`0<p<1,`

and every `alpha p`-spread probability law `nu` on `2^S`,

`W_alpha(nu)(A_6) <= mu_p(A_6).`

### Proof

If `p>=alpha`, use Section 5.4.

Assume `p<alpha`. If (5.1) holds, the six-edge principal-cover certificate proves the claim. If (5.1) fails, Sections 5.2--5.3 imply `T(alpha,p)<1`, and Lemma 3.1 supplies a shared-mass dual certificate. These cases exhaust all parameters. `QED`

---

# 6. Consequence for the source search

The first F0106 run proved the universal singleton-family obstruction

`alpha_dom <= alpha_*`

where `alpha_*` is the unique root of

`-alpha log(1-alpha)=1`.

Elementary monotonicity and

`(3/4) log 4 = (3/2) log 2 >1`

show `alpha_*<3/4` (for example, `log 2>2/3` follows from `log x>2(x-1)/(x+1)` at `x=2`).

Therefore Theorem 5.1 excludes the entire six-cycle minimal-witness class as a counterexample throughout **every alpha that remains viable for the universal conjecture**.

This is substantially stronger than merely solving the rational stress point. The simple cover really does fail there, but full dual sharing restores a large margin. Any genuine obstruction must use a witness geometry whose shared-mass requirements cannot be represented by this empty/edge/opposite-edge-union mechanism.

The frozen universal metric remains unchanged:

`0 <= alpha_dom <= alpha_*=0.740753643351695... .`

No positive universal lower bound is proved here.

---

# 7. What the three methods contributed

## B11 — dualize

The full finite obstruction norm was attacked directly. `D6` averaging reduced the stress LP to 13 subset orbits, and an exact primal/dual pair determined its optimum. The key reusable output is the explicit shared subprobability on the empty set, six edges, and three opposite-edge unions.

## B16 — exact small cases

All 64 deterministic ambient sets were checked exactly. More importantly, the 13 orbit slacks factor into manifestly nonnegative polynomials, turning the stress-point discovery into a theorem valid for all `alpha,p` whenever the total mass is at most one.

## B19 — constructive algorithm

The recovery became a parameter-uniform two-certificate procedure: edge cover first, shared dual second. A simple monotonicity argument shows one of the two always works for `alpha<=3/4`, with the trivial empty-set certificate handling `p>=alpha`.

---

# 8. Exact verification artifact

Companion checker:

`research7_2026-09-17/R7-04/artifacts/2026-09-18/2026-09-18T094600Z__F0106_C6_shared_dual_exact.py`

It uses Python `Fraction` arithmetic only and verifies:

- the 13 `D6` subset orbits;
- all 64 stress-point primal inequalities;
- the exact primal mass and margin;
- all reduced-dual constraints;
- exact equality of primal and dual objectives;
- the rational constants `749/80000` and `56178212743/262144000000` used in the global `alpha<=3/4` dichotomy.

Executed output is archived beside it and ends `ALL_EXACT_CHECKS_PASS`.

---

# 9. Remaining gap

This does **not** move the full-source quantity `alpha_dom`, because `A_6` is only one six-coordinate up-class. The source still quantifies over every finite ground set and every up-class.

The new obstruction is sharper, however: a future counterexample cannot merely be “the first dense overlap cycle where the principal cover costs more than one.” The six-cycle has now been ruled out throughout the entire source-relevant alpha range by an explicit shared-mass dual.

A productive next direction is to identify the first witness hypergraph for which every low-order shared-mass basis analogous to `{empty, witnesses, structured witness unions}` fails, rather than increasing cycle length mechanically.
