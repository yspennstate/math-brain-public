# B03 / A014 — rank-two Boolean collision beyond disjoint support

**Primary packet:** A014 (overlap beyond worst-case read)  
**Attempt:** `A014-RANK-TWO-COLLISION-2`  
**Stable gap:** `FEI-GAP-SHARED-SELECTOR-CIRCULARITY`  
**Claim:** `B03-A014-RANK-TWO-COLLISION-v1`  
**Status:** PROVED RESTRICTED THEOREM, pending independent review. Full FEI remains OPEN.

## Exact target and movement

The preceding A014 theorem handled spectral branch rank one: Booleanity
forces all branches to be signed copies of one core. Its exact remaining
obligation was rank two or controlled distance from rank one without
recovering the arbitrary-controller FEI embedding.

This run proves the exact rank-two Boolean classification and a strict
all-parameter extension with completely coincident branch Fourier supports.
For every balanced rank-two branch family, there are two balanced Boolean
cores `g,h`, and every branch is one of `±g,±h`. This converts a free
rank-two matrix into two Boolean labels: a sign controller and a type
controller.

For the separable-controller subclass, where the type is one fresh bit and
the sign controller uses a disjoint address block, entropy and influence
factor exactly. The explicit family has

```
worst read                  = 2^(t+1),
fractional congestion       = 1,
spectral branch rank        = 2,
rank/type name cost         = 1 bit,
expected controller roots   < 3,
H(F_t)                      = H(s_t)+2,
I(F_t)                      = t*2^(1-t)+2,
H(F_t)                      < 4 I(F_t).
```

The constant four is independent of address count, read, rarity, and the
complete spectral collision.

## Rank-two Boolean compatibility

Let `B(u,R)=|U|^(-1/2) Fourier(g_u)(R)` on nonempty data frequencies. Assume
the branches are balanced Boolean and `rank(B)=2`. Choose two independent
branches `g,h`. Every other branch is `f=a g+b h`. Since `g,h` are
independent, `r=gh` is a nonconstant sign and assumes both values. Dividing
by `g`, Booleanity gives

```
|a+b|=|a-b|=1.
```

Thus `ab=0` and `a^2+b^2=1`, so `f` is exactly one of `±g,±h`. Equivalently

```
F(a,x)=sigma(a)[(1+tau(a))/2 g(x)+(1-tau(a))/2 h(x)].
```

This is an exact all-dimensional theorem. It is not a finite-rank heuristic
and uses genuine Booleanity at the decisive step.

## Fully colliding rank-two family

On three data signs define

```
g=(x1+x2+x3-x1*x2*x3)/2,
h=(x1+x2-x3+x1*x2*x3)/2.
```

Both are balanced Boolean, they are orthogonal, and their Fourier supports
are identical: the three singletons and the triple. Hence this example is
outside any exactly-disjoint-support argument.

With one type bit `b`,

```
M(b,x)=(g+h)/2+b(g-h)/2
      =(x1+x2+b*x3-b*x1*x2*x3)/2.
```

Its four squared Fourier coefficients are all `1/4`, so `H(M)=2` and
`I(M)=2`. Let `s_t` be negative only at the all-minus address and put

```
F_t(c,b,x)=s_t(c) M(b,x).
```

The factors use disjoint physical blocks, so `H` and `I` add. Writing
`delta=2^(1-t)`, one has `I(s_t)=t delta` and

```
H(s_t)=-(1-delta)^2 log2((1-delta)^2)
       +(2^t-1) delta^2 (2t-2) < 4 t delta.
```

Therefore `H(F_t)<4I(F_t)` for every `t>=1`.

## Complete label, rank, rarity, and root accounting

The literal selector has `2^(t+1)` branches and all three data coordinates
are relevant in every branch. Worst-case read therefore diverges, whereas
its activation-weighted congestion is exactly one.

The core has rank two, costing one type bit. The sign controller `s_t` can
be evaluated by querying until the first `+1`, at expected cost
`2-2^(1-t)<2`; querying `b` adds one physical root. The rare exceptional
address has probability `2^(-t)`, and its logarithmic cost is retained in
`H(s_t)` and paid by `I(s_t)=t2^(1-t)`. The fixed core normalizer is exactly
its already-paid entropy `2`. There is no omitted subset-choice cost.

`COLLISION_COST_LEDGER.md` records every term. No `k`-fold Cauchy--Schwarz,
overlapping-product subadditivity, or disjoint-Fourier-support assumption is
used; the four coherent sums are computed before squaring.

## Boundary and universal gap

The general rank-two normal form has two arbitrary, possibly correlated
Boolean controllers `(sigma,tau)`. The present proof pays them only in the
separable case `tau=b`, `sigma=s(c)`. An arbitrary sign controller already
contains the B18 FEI-hard signed-dictator embedding. Therefore the next
unpaid step is not another rank enumeration: it is a joint posterior charge
for correlated `(sigma,tau)`, or a stable structural hypothesis that bounds
that charge without assuming FEI.

Rank larger than two and approximate rank two remain open. The theorem is a
proper class result and does not settle full FEI.

## Verification

Command:

```
python3 verify_rank_two_overlap.py
```

Output: `PASS: 103 assertions`.

The checker uses exact `Fraction` Walsh transforms. It verifies Booleanity,
balance, orthogonality, complete support coincidence, the four-atom core,
rank two, Parseval, exact influence, entropy decomposition, worst read and
fractional congestion for `t=1,...,9`. Floating logarithms are used only for
finite entropy comparisons; the displayed all-parameter proof is analytic.

## Sources actually used

- Owner overlay `FULL-FEI-ONLY-20261012`, control revision `2026-10-12.1`.
- `assignments/B03.json`, blob `02045d5236cbcfaee630469ed54e6022902b3dd9`.
- Prior A014 rank-one report at canonical commit
  `2c424ae1812091ed3620d844e5dc6efb769a7fdb`, report blob
  `b3bfea82cb0f54377d92efdd217c3206e9030e64`.
- Obstruction registry revision `2026-10-12-a096-tree-slack`, including the
  overlapping-product and arbitrary-controller guards.
- Canonical head observed before persistence:
  `d45a3f975a63c578b1338d4a756ad3f28b68fb37`.

The requested B02 summed-witness artifact was not located by repository code
search and is not claimed as a dependency. This proof instead makes the
two-piece joint packet exact, so there is no witness multiplicity or
Cauchy--Schwarz loss to import.

## Handoff

Route the classification and family to A009/A068 for congestion design and
to A086/A094 for independent review. Because this is the second broad A014
candidate awaiting review, the next B03 action should review/falsify the
rank-two normal form or attack its correlated-controller boundary, not open
a third unrelated candidate.
