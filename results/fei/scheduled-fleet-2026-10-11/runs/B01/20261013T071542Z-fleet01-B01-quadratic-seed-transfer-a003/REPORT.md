# B01 / A003 report: exact quadratic-seed GU' transfer

## Outcome

**AUTHOR-PROVED, PENDING INDEPENDENT REVIEW.** I proved an exact transfer
theorem for the campaign's `GU'` target. If a restriction-closed seed class
obeys

\[
G(g)\le aI(g)+bU(g),\qquad 0\le b<1,
\]

then multiplying every seed by an arbitrary-dimensional quadratic phase on a
disjoint coordinate block preserves `b` exactly and changes `a` only to
`max(3,a)`. The proof uses exact tensor factorization of the upper caps, hence
`U`, `H`, `I`, and the complete restriction charge `G` are all additive.

This gives a concrete expanding restriction-closed class. If the seed is any
Boolean function on at most `k` variables, then

\[
G\le\max\{3,k2^{k-1}\}I,\qquad
U\le2^{k-1}I,\qquad
H\le\max\{2,2^{k-1}\}I.
\]

For example, arbitrary quadratic phases times arbitrary four-bit Boolean
seeds satisfy `G<=32I`, `U<=8I`, and `H<=8I`. This strictly extends the
quadratic class but does not settle FEI because the seed constants grow with
`k`.

## Packet and frozen objective

- Primary packet: **A003 — Minimal target formulation**.
- Gap: **G-UPPER-SET-ASYMMETRY**.
- Attempt: **A003-QUADRATIC-SEED-TRANSFER-5**.
- Objective: use the independently reviewed all-quadratic theorem as a
  transfer mechanism; determine exactly which `GU'(a,b)` estimates survive
  arbitrary quadratic multiplication; instantiate one larger
  restriction-closed class with all parameter dependence explicit.

## Inputs actually used

1. B01 all-quadratic theorem, report blob
   `460a47083324f194bb431650ab912c126f9894f2`, canonical receipt
   `d829fca20536446e9855c0ce13be882b9beaf11a`.
2. B19 independent acceptance of the stronger adaptive quadratic tree theorem,
   report blob `7c15eca2c0b82f3d781c36d8808ffe5722b22866`, canonical receipt
   `04ba7e13af4727f1989b2c1fd8bcbe7ea11685bc`.
3. B01 compact assignment blob
   `ac038a028831d59ad053dd56b2b527e2a71ffdee`.
4. Owner control revision `2026-10-12.1`, commit
   `40210272c19f43fed84f6a67653f9a04b0e11e28`.

Only the reviewed quadratic conclusions `G(q)<=3I(q)`, `U(q)<=I(q)`, and
`H(q)<=2I(q)` are imported. The new tensor transfer and bounded-seed class are
proved in `QUADRATIC_SEED_TRANSFER.md`.

## Mathematical delta

Previously, the accepted class was the quadratic phases themselves. The new
class permits an arbitrary Boolean terminal core of bounded width, independently
of the dimension, rank, and overlap pattern of the quadratic block. More
generally, every future seed-class improvement transfers without worsening its
strict contraction coefficient `b`.

The exact gain and limitation are now separated:

| Item | Previous scope | New scope | Constant |
|---|---|---|---|
| GU' | Quadratic phases | Quadratic phase times any `g` in a seed GU' class | `(max(3,a), b)` |
| Concrete class | All quadratic phases | Quadratic phase times any Boolean `k`-bit seed | `a=max(3,k2^(k-1)), b=0` |
| Upper-set bound | `U(q)<=I(q)` | `U(qg)<=2^(k-1)I(qg)` | grows with `k` |
| FEI bound | `H(q)<=2I(q)` | `H(qg)<=max(2,2^(k-1))I(qg)` | grows with `k` |

The transfer coefficient is dimension-free in the quadratic block. The only
remaining parameter dependence is in the arbitrary seed.

## Verification

The deterministic exact checker passed:

- 32,906 Boolean seeds modulo output sign through dimension four;
- 197,436 bounded-seed inequalities;
- 1,332 seed/quadratic products;
- 5,328 exact tensor identities.

Arithmetic uses integer Walsh transforms, `Fraction` spectral masses, and
exact prime-log coefficient vectors. Floating conversion is used only to print
the observed maxima. No randomness is used.

## Status and remaining universal gap

The two theorems are **AUTHOR_PROVED_PENDING_A086_A094_REVIEW**. They do not
prove full FEI. Disjoint tensor additivity cannot pay upper-set asymmetry
generated inside an arbitrary seed. The explicit bound for seed width `k`
grows exponentially, so taking `k` to infinity is invalid.

The next action is to seek a seed class of unbounded width with a uniform
`GU'(a,b)` estimate, or replace disjoint transfer by a coupled quadratic/seed
payment that makes genuine use of cross-block restriction information. The
exact transfer theorem can then be reused without redoing quadratic accounting.

## Review routing

- Consumers: A005, A021, A023, A063, B20.
- Independent reviewers: A086 and A094.
- Full FEI status: **OPEN**.
- No scheduler, graph, publication, or protected-source action was taken.
