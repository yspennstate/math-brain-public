# B05 / A023 — retained-difference entropy telescope

**Primary packet:** A023, amortized rarity budget  
**Gap:** `B05_RARE_REFUNDS`  
**Attempt:** `B05-A023-DIFFERENCE-ENTROPY-TELESCOPE-03`  
**Status:** author-proved at stated scope, pending A087/A094 review  
**Full FEI:** **OPEN**.

## Result

The sparse-surgery no-go ruled out every absolute payment of a coherent
one-node charge by selector influence alone.  This run changes the mechanism:
it retains the raw Fourier entropy of the physical child difference and uses
`H-U` as a telescoping potential.

For genuine Boolean children `g,h`, a fresh uniform selector `z`,

`F(z,x)=g(x)` for `z=-1`, `F(z,x)=h(x)` for `z=1`,

put

`d=(g-h)/2`, `q=E d^2=Pr[g!=h]`, `V=H-U`, and

`L(d)=sum_S dhat(S)^2 log2(1/dhat(S)^2)`.

Then

`U(F)-(U(g)+U(h))/2`

`<= -V(F)+(V(g)+V(h))/2 + L(d) + (3/ln 2) q`.          (1)

The coefficient `3/ln 2 = 4.328085...` is absolute.  No spectral flatness,
nonzero-atom, bias, tensor, or disjoint-data assumption is used.

For an arbitrary finite binary restriction tree whose internal nodes use
distinct fresh physical selector coordinates, let `w_v` be the reach
probability, `d_v` the half-difference of the two child subfunctions, and
`g_l` the terminal Boolean cores.  The children and terminal cores may share
all data coordinates.  Summing (1) gives

`U(root)-sum_l w_l U(g_l)`

`<= sum_l w_l[H(g_l)-U(g_l)] - [H(root)-U(root)]`

`   + sum_v w_v L(d_v) + (3/ln 2) I_sel(root)`.          (2)

All internal `H-U` packets cancel.  Each node's difference packet occurs
once, and `I_sel=sum_v w_v q_v` is the actual physical selector influence.
The constants in (2) do not depend on depth, activation probability, terminal
bias, data overlap, or coherent-core shape.  In particular, (2) is an
all-parameter retained-credit bound for nested rare activations with arbitrary
terminal cores.

## Proof mechanism

Write `a=ghat`, `b=hhat`, `u=(a+b)/2`, `v=(a-b)/2`, and
`M=u^2+v^2=(a^2+b^2)/2`.  The selector Fourier spectrum gives the exact
entropy identity

`H(F)-(H(g)+H(h))/2 = JS(a^2,b^2) + sum_S M_S h2(v_S^2/M_S)`.

Two scalar estimates finish the node bound:

- `JS(a^2,b^2) <= 2q/ln 2`.  The proof is pointwise and is included in the
  TeX artifact; opposite coefficient signs only improve the bound.
- `sum M h2(v^2/M) <= L(d)+q/ln 2`, because `M_S<=1` and
  `u^2 log2(1+v^2/u^2)<=v^2/ln 2`.

Thus the entropy increment is at most `L(d)+3q/ln2`.  Substituting `U=H-V`
produces (1).  Weighting (1) by reach probabilities telescopes both `U` and
`V`, proving (2).  This is a regrouping of the complete signed restriction
charge: it does not discard or assign unsupported signs to the
`B-Gamma+KL` terms.

## Exact scope extension

Previous constructive payments covered nested activations with one retained
terminal core, and separated read-once trees under disjoint sibling-variable
hypotheses.  The new statement permits an arbitrary finite hierarchy of
changing coherent terminal cores with fully shared data coordinates.  The
price of that extension is explicit: the raw difference-spectrum entropy
`sum_v w_v L(d_v)` remains in the ledger.

This is stronger than a finite-case survival and weaker than a pure
dimension-free influence bound.  It is restriction closed under pruning or
fixing any fresh selector coordinate.

## Mandatory obstruction checks

- **Sparse bent surgery:** the theorem keeps `L(d)` rather than falsely
  replacing it by `Cq`.  The archived parametric no-go amplifies precisely
  this retained packet, so there is no contradiction or hidden selector-only
  claim.  Direct genuine-Boolean checks for `r=2,...,6` pass.
- **Shared data / coherent cores:** allowed without orthogonality; only the
  selector coordinates must be fresh and node-unique.
- **Near tensors and prime gates:** (1) is pairwise universal and does not use
  factorization.
- **Parity erasure and even-surgery zero atoms:** the proof never divides by a
  Fourier coefficient; zero terms use the standard limiting convention.
- **Nested rarity:** reach weights can be arbitrarily small dyadic numbers;
  the constants remain `1` and `3/ln2`.
- **Reused address variables:** not covered.  For reused physical selectors,
  `sum_v w_v q_v` need not equal actual influence.

## Verification

`CHECK.py` independently evaluates `H`, `U`, the entropy identity, both scalar
bounds, and (1) for all 65,812 ordered pairs of Boolean functions on at most
three data bits.  It also checks 100 depth-four rare chains with fully shared
three-bit terminal data and the small sparse-surgery instances above.  The
largest entropy-identity error was `5.551e-16`, the largest tree-telescope
error was `3.775e-15`, and every inequality passed.  These finite checks test
normalization and implementation; the theorem is analytic.

## Exact remaining obstacle

The universal unpaid term is now isolated as

`R(T)=sum_v w_v L((F_v^- - F_v^+)/2)`.

No dimension-independent bound of `R(T)` by nonreused physical data influence
plus terminal entropy is proved.  The prior sparse-surgery family proves that
`R(T)` cannot be replaced by an absolute multiple of selector influence,
already for one node.  Reused address variables introduce a second problem:
the nodewise `q_v` charges can interfere and cease to be physical-influence
payments.

The next attempt should decompose each `d_v` into martingale differences of
terminal cores in reveal order and test whether their raw spectral entropies
have disjoint physical ownership.  A valid theorem must retain the path
indicator entropy and survive the sparse-surgery, whole-set addressing, near
tensor, and shared-selector controls.

## Sources and delivery state

- Owner control revision `2026-10-12.1`, commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- B05 contract blob `05447e6d999437bb82a266b427bd76a4b37266b6`.
- Sparse-surgery no-go: canonical commit
  `0b84fdeb8b04511228e1cd7d1746317e883e8df6`, report blob
  `d829573f7b290efd412729955a6c5494d819253b`.
- Exact upper-set restriction identity source blob
  `5797e9cc38598cbee391cc99d4b1abcd554b662e`.

No external novelty claim is made.  No subagent, protected source, paid
compute, public release, email, scheduler mutation, or native Brain ingestion
was used.  Independent review is pending.

## Persistence receipts

The nine-file canonical package was committed at
`840f201947ee28ceec6e8f74e9cfb5282bbed6c0`; the byte-identical Brain
handoff was committed at `c17b45e650d1b69d9b460fdd4f8daa7430bed75b`.
All eighteen file readbacks were nonempty and matched their expected Git blob
SHAs.  These receipts establish durable delivery, not independent acceptance
or a solution of full FEI.
