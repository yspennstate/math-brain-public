# Assembly bar: E[X^{-a}] = 1 + o(1) needs only mu1 = o(1)

Verification note, 2026-06-28 (lead-requested rigorous check of the assembly reduction in
`keystone_tail.md` Section 3 / `keystone_synthesis.md` block (A)).

## Setup and the precise claim verified

`X := 1 - |rho|^2 in (0,1]`, `a := d_F/2 > 0`, `mu1 := E[1-X] = E|rho|^2 in [0,1)`.

GIVEN (proven, Section 2, UNCONDITIONAL on mu1): the tail
`P{X<=y} <= (C sqrt y)^{D-1} + 2 e^{-cD}`, tuned `P{X<=y} <= 2 e^{-cD y^{-1/2}} + (C y^{1/4})^{D-1}`,
which yields, for the fixed constant `y1 := 1/(2C') < 1/2`, the singular bound
```
  (S)   E[X^{-a}; X <= y1] = o(1)   as D -> infinity,   and this bound does NOT involve mu1.
```
(S) is mu1-free: Section 3(i) bounds it by `sum_{k>=k1} 2^{(k+1)a}[2 e^{-cD 2^{k/2}} + (C 2^{-k/4})^{D-1}]`,
a function of the tail constants and `D` only. It is `o(1)` once `D > 1 + 2 d_F`. Confirmed mu1-independent.

CLAIM TO VERIFY: `E[X^{-a}] = 1 + o(1)` follows from (S) plus ONLY `mu1 = o(1)` (no `mu1 = O(1/D)`).

## Verification of every inequality

Decompose `E[X^{-a}] = E[X^{-a}; X<=y1] + E[X^{-a}; y1<X<=1/2] + E[X^{-a}; X>1/2]`.

### (band) y1 < X <= 1/2
`X > y1` and `-a < 0` give `X^{-a} < y1^{-a}`. Hence
`E[X^{-a}; y1<X<=1/2] <= y1^{-a} P{X<=1/2}`.
`1-X = |rho|^2 >= 0` (as `X<=1`), so Markov: `P{X<=1/2} = P{1-X >= 1/2} <= mu1/(1/2) = 2 mu1`.
Therefore
```
  E[X^{-a}; y1<X<=1/2] <= 2 y1^{-a} mu1 = O(mu1).      [y1, a are constants -> O(mu1)]   ✓
```
Markov is valid (nonnegative variable, finite mean). No D-dependence beyond mu1 itself.

### (>1/2)
`E[X^{-a}; X>1/2] = P{X>1/2} + E[X^{-a}-1; X>1/2]`, with `X^{-a}-1 >= 0` on `{X<=1}`.
Pick `eta in (0,1/2)` and split `{X>1/2} = {X>1-eta} ∪ {1/2<X<=1-eta}` (disjoint since `1-eta>1/2`).

LEMMA (the (1-eta) bound). For `a>0` and `eta in [0,1/2]`, `(1-eta)^{-a} - 1 <= C_a eta` with
`C_a := a 2^{a+1}`.
PROOF. `f(eta):=(1-eta)^{-a}`, `f(0)=1`, `f'(eta)=a(1-eta)^{-a-1}` is increasing, so on `[0,1/2]`
`f'(eta) <= f'(1/2) = a 2^{a+1}`. MVT: `f(eta)-1 = f'(xi) eta <= a 2^{a+1} eta`. ∎  ✓

- On `{X>1-eta}`: `X>1-eta` and `-a<0` give `X^{-a} < (1-eta)^{-a}`, so `X^{-a}-1 <= (1-eta)^{-a}-1 <= C_a eta`
  (Lemma). Contribution `<= C_a eta * P{X>1-eta} <= C_a eta`.   ✓
- On `{1/2<X<=1-eta}`: `X>1/2` gives `X^{-a} < 2^a`, so `X^{-a}-1 <= 2^a-1`. And
  `{1/2<X<=1-eta} ⊆ {X<=1-eta} = {1-X >= eta}`, Markov `P{1-X>=eta} <= mu1/eta`. Contribution
  `<= (2^a-1) mu1/eta`.   ✓

Hence (using `P{X>1/2} <= 1`)
```
  E[X^{-a}; X>1/2] <= 1 + C_a eta + (2^a-1) mu1/eta.
```

OPTIMIZE over eta. `g(eta) = C_a eta + (2^a-1) mu1/eta` has unconstrained minimizer
`eta* = sqrt((2^a-1)mu1/C_a)`, value `g(eta*) = 2 sqrt(C_a (2^a-1) mu1) = O(sqrt mu1)`.
The note's choice `eta = sqrt(mu1)` is admissible and order-optimal:
`g(sqrt mu1) = (C_a + 2^a - 1) sqrt(mu1) = O(sqrt mu1)`.   ✓
Admissibility `eta = sqrt(mu1) in (0,1/2)` requires `mu1 < 1/4`; since `mu1 = o(1)` this holds for
all large `D`, which is all the asymptotic statement needs.   ✓
```
  E[X^{-a}; X>1/2] <= 1 + O(sqrt mu1).
```

### (total)
```
  E[X^{-a}] <= o(1)   +   O(mu1)   +   1 + O(sqrt mu1)            (S) + band + (>1/2)
            =  1 + O(sqrt mu1) + O(mu1) + o(1).
```
Since `sqrt mu1` dominates `mu1` for small `mu1`, the bound is `1 + O(sqrt mu1) + o(1)`, which is
`1 + o(1)` **iff** `mu1 = o(1)`. The trivial lower bound `E[X^{-a}] >= 1` (as `X<=1`) gives equality:
```
  mu1 = o(1)   ==>   E[X^{-a}] = 1 + o(1).      CLAIM CONFIRMED.   ✓
```

## Sufficiency is sharp: mu1 = o(1) is also NECESSARY
For `t in [0,1)`, `a>0`: `(1-t)^{-a} >= 1 + a t` (let `h(t)=(1-t)^{-a}-1-at`; `h(0)=0`,
`h'(t)=a[(1-t)^{-a-1}-1] >= 0`). With `t = 1-X = |rho|^2 in [0,1)`:
`X^{-a} >= 1 + a(1-X)` pointwise, so `E[X^{-a}] >= 1 + a mu1` (valid even if LHS = +inf).
Thus `E[X^{-a}] = 1 + o(1)` forces `a mu1 = o(1)`, i.e. `mu1 = o(1)`. Necessity uses ONLY `X<=1`
(no tail). Combined with the above:

> Given the tail's mu1-independent singular bound (S),
>     E[X^{-a}] = 1 + o(1)   <==>   mu1 = E|rho|^2 = o(1).

## No hidden dependence on D or on mu1 = O(1/D)
- The band and (>1/2) bounds are functions of `mu1`, `y1`, `a`, `C_a`, `2^a` ONLY — no explicit `D`.
- The ONLY D-dependence in the whole assembly is (i) the singular bound (S) being `o(1)` as `D->infty`
  (needs `D>1+2 d_F`, mu1-free), and (ii) that in the application `mu1 = mu1(D) -> 0`. Both `o(1)`'s
  are the same `D -> infty` limit, so they compose cleanly.
- The specific rate `mu1 = O(1/D)` is NOT used anywhere for the qualitative `1+o(1)`. It only
  SHARPENS the error: `mu1 = O(1/D)` => dominant term `O(sqrt mu1) = O(D^{-1/2})`, recovering
  Section 3's `eta = D^{-1/2}` and its `1 + O(D^{-1/2})` exactly (since `eta=D^{-1/2}=sqrt(mu1)` there).
  Getting the still-sharper `1 + a mu1 + o(mu1) = 1 + O(1/D)` needs a SECOND-MOMENT input
  `E[(1-X)^2]=O(1/D^2)`, as the note already states; the mean alone caps the error at `O(sqrt mu1)`.
- No circularity: the tail (Section 2) is proved from sub-Gaussian + bounded density, never invoking
  mu1; so (S) is genuinely mu1-free and the reduction is not self-referential.

## Conclusion
Every inequality in the chain checks out (band Markov, the `(1-eta)^{-a}-1<=C_a eta` lemma via MVT,
the `{X>1-eta}`/`{1/2<X<=1-eta}` split, the second Markov, the `eta=sqrt(mu1)` optimization, and the
admissibility `mu1<1/4`). The singular part is genuinely mu1-independent. The sufficient condition is
exactly `mu1 = o(1)`, and it is also necessary. The reduction in `keystone_tail.md` Section 3 is
therefore valid under the strictly weaker hypothesis `mu1 = o(1)` in place of `mu1 = O(1/D)`.
```
