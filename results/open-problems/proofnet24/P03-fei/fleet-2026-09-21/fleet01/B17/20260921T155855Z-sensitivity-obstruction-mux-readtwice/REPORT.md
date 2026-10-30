# B17 FEI creative attempt: a 4-bit no-subset-coupling obstruction and a constant-6 selector/read-twice theorem

**Status:** full Friedgut--Kalai Fourier entropy--influence conjecture remains **OPEN / NOT PROVED**.  
**Run label:** `WITHOUT_VERIFIED_BRAIN`.  
**Primary routes:** APPROACH 3 / 7 / 14.  
**Novelty:** no literature-priority claim is made. The selector calculation and the sensitivity obstruction are recorded as proof-route mathematics, not as a claim that they are new in the literature.

This run first stress-tested the most literal remaining sensitivity coupling after the previous B17 work. It fails already on four bits. I then pivoted to APPROACH 7 and obtained an analytic FEI closure theorem for a genuine read-twice syntactic class: arbitrary disjoint-branch selector/MUX composition preserves every FEI constant `C >= 6`; consequently every recursive selector tree with literal leaves satisfies `H <= 6 I`.

The general conjecture is not closed by this class theorem. In particular the current full-FEI lower-bound handoff is already above 6.52, so the constant-6 selector class does not contain the known hard construction.

## 1. APPROACH 3 stress test: no universal coupling with `S subset Sens(X)`

Let `f:{0,1}^4->{-1,+1}` be `+1` exactly at the three inputs

`0000, 0001, 0010`

(with coordinate 0 the least significant bit), and `-1` elsewhere. Let `S` be its spectral sample and let `T=Sens(X)` for a uniform input `X`.

Take `A={0,1,2}`. Exact Walsh arithmetic gives

`P(A subset S) = sum_{B superset A} fhat(B)^2 = 1/32`.

Indeed the only supersets are `A` and `A union {3}`, and each corresponding squared coefficient is `1/64`.

On the physical side, the sensitivity masks that occur are

`0, {0,1}, {2}, {3}, {2,3}, {0,2,3}, {1,2,3}`.

No input is simultaneously sensitive in coordinates `0,1,2`, hence

`P(A subset Sens(X)) = 0`.

Therefore there cannot exist any coupling of the spectral sample and a uniform-input sensitivity set satisfying

`S subset Sens(X)` almost surely.

The reason is immediate: such a coupling would force

`P(A subset S) <= P(A subset Sens(X))`

for every `A`, contradicted by `1/32 > 0` above.

This is stronger than merely showing that the two random sets differ in law. It says the natural subset-sampler version of APPROACH 3 is impossible even in dimension four. It is consistent with the known equality of singleton and pair inclusion marginals: the obstruction first appears at order three.

A viable sensitivity route therefore has to use more than one physical point, a random face, or signed derivative information; a single sensitivity set cannot dominate the spectral sample in the containment order.

## 2. Pivot to APPROACH 7: exact selector/MUX composition

Let `a` and `b` be Boolean functions on disjoint variable sets, with

`mu = E a`, `nu = E b`.

Let `z` be one new selector bit, independent of both branches, and define

`f = MUX_z(a,b) = (a+b)/2 + z (a-b)/2`.

Thus one value of `z` chooses `a` and the other chooses `b`.

Write

`phi(t)=-t log2 t`, with `phi(0)=0`.

The Fourier expansion is completely explicit. For every nonempty Fourier atom of `a`, two copies occur in `f`, one without `z` and one with `z`, each with one quarter of the original squared mass; the same is true for `b`. The two special squared masses are

`p_0 = (mu+nu)^2/4`, `p_z=(mu-nu)^2/4`.

Consequently

`I(f) = (I(a)+I(b))/2 + (1-mu*nu)/2`,                                      (2.1)

and

`H(f) = (H(a)+H(b))/2 + Omega(mu,nu)`,                                     (2.2)

where

`Omega(mu,nu)`
` = (1-mu^2)+(1-nu^2)`
`   + phi((mu+nu)^2/4)+phi((mu-nu)^2/4)`
`   - (phi(mu^2)+phi(nu^2))/2`.                                            (2.3)

The final term in (2.1) is exactly the influence of the selector coordinate.

## 3. Main analytic lemma: the selector entropy toll is at most six selector-influences

### Lemma

For all `mu,nu in [-1,1]`,

`Omega(mu,nu) <= 3(1-mu*nu)`.                                              (3.1)

Equivalently, since `Inf_z(f)=(1-mu*nu)/2`,

`Omega(mu,nu) <= 6 Inf_z(f)`.                                              (3.2)

### Proof

The expression `Omega` is unchanged if the sign of either mean is flipped, while

`1-mu*nu >= 1-|mu||nu|`.

It therefore suffices to put `a=|mu|`, `b=|nu|` and prove

`Omega(a,b) <= 3(1-ab)`.

Set

`s=(a^2+b^2)/2`.

If `s=0` the claim is immediate. Otherwise define

`u=ab/s`,
`v=sqrt(1-u^2)=|a^2-b^2|/(a^2+b^2)`,
`g(t)=h_2((1+t)/2)`.

The two transformed special masses have total mass `s` and normalized bias `u`. The two original squared means, after the factor `1/2`, have total mass `s` and normalized bias `v`. A direct entropy grouping gives

`Omega(a,b) = 2(1-s) + s F(u)`,                                             (3.3)

where

`F(u)=1+g(u)-g(v)`.                                                         (3.4)

Use the elementary binary-entropy inequalities, valid for `0<=p<=1`,

`4p(1-p) <= h_2(p) <= 2 sqrt(p(1-p))`.

Applied to `g`, they give

`g(u) <= v`,
`g(v) >= 1-v^2 = u^2`.

Therefore

`F(u) <= 1+v-u^2 <= 3+v-3u`,                                               (3.5)

because the difference between the last two right-hand sides is

`(1-u)(2-u) >= 0`.

Finally observe the exact feasibility identity

`s(1+v)=max(a^2,b^2) <= 1`.                                                 (3.6)

Combining (3.3)--(3.6),

`3(1-su)-Omega`
` = 1 - s(F(u)-2+3u)`
` >= 1-s(1+v)`
` >= 0`.

Since `su=ab`, this is precisely (3.1). QED.

The only scalar inequalities used above are the standard elementary two-sided bounds on binary entropy; each follows by one-variable calculus and is independent of FEI.

## 4. Constant-preserving composition theorem

### Theorem

Let `C >= 6`. Suppose `a` and `b` are Boolean functions on disjoint variable sets satisfying

`H(a) <= C I(a)`, `H(b) <= C I(b)`.

Then their selector composition satisfies the same constant:

`H(MUX_z(a,b)) <= C I(MUX_z(a,b))`.                                        (4.1)

### Proof

By (2.2) and the lemma,

`H(f) <= C(I(a)+I(b))/2 + 3(1-mu*nu)`.

Since `C>=6`,

`3(1-mu*nu) <= C(1-mu*nu)/2`.

Equation (2.1) now gives (4.1). QED.

This theorem does not assume the branches are balanced. The branch biases are exactly what the scalar lemma pays.

## 5. Corollary: a read-twice syntactic class with FEI constant 6

Build a recursive selector tree as follows:

1. leaves are literals or constants;
2. every internal node is `MUX_z(A,B)` with a fresh selector variable `z`;
3. the two branch subtrees use disjoint variable sets, and the selector is used nowhere below them.

A literal has spectral entropy zero and influence one; a constant has both zero. Induction with `C=6` gives

`H(F) <= 6 I(F)`                                                              (5.1)

for every such selector tree.

If a MUX is expanded into AND/OR/NOT syntax as

`(z AND A) OR ((NOT z) AND B)`,

its selector variable occurs twice, once in each polarity. Under the freshness/disjointness conditions above, every internal selector occurs exactly twice and leaf variables occur once. Thus (5.1) is an explicit FEI theorem for this read-twice syntactic subclass.

This is not a theorem for arbitrary read-twice formulas: sharing a variable across two unrelated subcomputations creates Fourier interference not present in the exact MUX decomposition. It is also not claimed that every function in this syntactic class lacks an alternative read-once representation.

## 6. Exact stress tests

`verify_mux_readtwice.py` checks two separate claims.

First, for the four-bit coupling obstruction it obtains exactly

`P({0,1,2} subset S)=1/32`,
`P({0,1,2} subset Sens(X))=0`.

Second, it exhausts all `16 x 16 = 256` ordered pairs of two-bit Boolean branch functions. For every pair it constructs the full five-bit MUX truth table, performs an integer Walsh transform, and verifies:

- the entropy identity (2.2), to zero float discrepancy in this run;
- the influence identity (2.1) exactly as a rational identity;
- `H(MUX)<=6 I(MUX)`.

Among those branch pairs the largest observed selector overhead ratio

`Omega / Inf_z`

is `4.867668746754797`, attained by branch means `-1` and `-1/2`.

As a separate scalar stress test, every dyadic bias pair with denominator `256` satisfies (3.2); the largest observed ratio is

`4.872309369879589`

at means `-1` and `-69/128`. These finite values are not used in the proof; the analytic lemma gives the rigorous constant 6 on the full continuum.

Executed checker SHA-256:

`41a829662a7a06656cb78a64d40d23f5516180007cbd116113d9055ebc65777a`.

Executed stdout SHA-256:

`4beba7e700ed5ca91a906c5475c317f0ff2cf3c54f60b6304f51711499119638`.

## 7. What this changes, and next target

APPROACH 3 now has a sharp local warning: even containment coupling to one physical sensitivity set is impossible, not merely equality in law. A sensitivity proof must be face-based, multi-point, or signed.

APPROACH 7 gains a positive closure operation. Selector reuse is one of the simplest ways a read-once AND/OR/NOT formula becomes read-twice; its entropy toll is universally paid by at most six times the selector influence, with no bias restriction. Hence arbitrary depth and arbitrary branch functions already known to satisfy a constant `C>=6` can be glued by fresh selectors without worsening `C`.

The next nontrivial read-twice step is to allow a physical variable to be shared by two *non-selector* branch computations. The exact MUX proof shows what must be retained: rather than bounding a shared-variable entropy term by itself, one should diagonalize the two branch Fourier fibres and charge the resulting two-by-two mixing entropy to the actual shared-coordinate influence after cancellation. A universal two-fibre inequality of that form would extend this theorem beyond selector-normal-form read-twice formulas and would be a genuinely stronger move toward full FEI.
