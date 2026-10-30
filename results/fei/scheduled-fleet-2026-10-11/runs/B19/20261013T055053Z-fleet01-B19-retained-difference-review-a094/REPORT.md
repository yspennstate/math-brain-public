# B19 / A094 — independent review of the retained-difference telescope

**Primary review packet:** A094, proof-chain challenger  
**Target packet:** B05 / A023  
**Target claims:** `B05_A023_RETAINED_DIFFERENCE_NODE_v1` and
`B05_A023_RETAINED_DIFFERENCE_TREE_v1`  
**Verdict:** **ACCEPTED AT DECLARED SCOPE**  
**Full FEI:** **OPEN**.

## Review result

The one-node and all-depth retained-credit inequalities are correct.  I
reconstructed the proof independently from the selector Fourier coefficients,
rather than treating the source checker or its `B-Gamma+KL` description as
evidence.

For Boolean children `g,h`, fresh selector `F`, `d=(g-h)/2`,
`q=Pr[g!=h]`, and `V=H-U`, the accepted node inequality is

`U(F)-[U(g)+U(h)]/2`

`<= -V(F)+[V(g)+V(h)]/2 + L(d) + (3/ln2)q`.             (1)

For every finite fair-bit restriction tree with node-unique fresh selectors,
arbitrary shared data coordinates, and arbitrary Boolean terminal cores,

`U(root)-sum_l w_l U(g_l)`

`<= sum_l w_l V(g_l)-V(root)`

`   +sum_v w_v L(d_v)+(3/ln2)I_sel`,                    (2)

where `I_sel=sum_v w_v q_v` is the actual physical selector influence.
The constants `1` and `3/ln2<4.329` are independent of depth, dimension,
terminal bias, data overlap, and dyadic activation probability.

No proof repair was required, so reviewer independence is preserved.

## Independent proof reconstruction

Writing `a=ghat`, `b=hhat`, `u=(a+b)/2`, `v=(a-b)/2`, and
`M=u^2+v^2`, the parent spectrum consists exactly of the `u` atoms without
the selector and the `v` atoms with it.  This gives

`H(F)-[H(g)+H(h)]/2 = JS(a^2,b^2)+sum M h2(v^2/M)`.

I independently proved the scalar estimate

`JS(a^2,b^2)<=||a-b||_2^2/(2ln2)=2q/ln2`.

The derivative proof is recorded in `REVIEW_PROOF.tex`.  Separately,

`M h2(v^2/M)`

`=v^2 log2(M/v^2)+u^2 log2(1+v^2/u^2)`

`<=v^2 log2(1/v^2)+v^2/ln2`.

Summing yields the entropy increment `L(d)+3q/ln2`; substituting `U=H-V`
gives (1).  Weighting by node reach probabilities cancels every internal `U`
and `V` term, proving (2).

For physical accounting, the ancestors determine whether node `v` is reached
without consulting its fresh selector.  The function ignores that selector
off the reached cylinder; on it the flip probability is `q_v`.  Therefore
`Inf_{z_v}=w_v q_v` exactly.

## Scope correction

The source phrase “single-use” is valid only in this precise algebraic sense:
each node contributes one displayed `w_v L(d_v)` term.  It does **not** prove
single-use ownership of the underlying data coordinates.  With shared cores,
one physical data coordinate can contribute to several different `d_v`
packets.

Accordingly, the following remains open:

`sum_v w_v L(d_v) <= C*(nonreused data influence + terminal entropy)`

with a dimension-independent `C`.  The accepted sparse-surgery obstruction
already forbids replacing this packet by `C I_sel`, even at one node.

Freshness is also essential.  An explicit repeated-selector control has
actual physical influence zero but formal node sum `1/2`, so the identity
`I_sel=sum_v w_v q_v` cannot be extended to reused selectors as written.

Thus the theorem is a correct universal retained ledger for its class, but it
does not prove `U<=KI`, a new pure FEI class bound, or full FEI.

## Independent verification

`REVIEW_CHECK.py` does not import the author checker.  It uses exact rational
Walsh coefficients and upper-set masses, with 70-digit arithmetic only for
logarithms.  It passed:

- 10,200 deterministic rational scalar pairs for the JS inequality;
- 1,300 Boolean selector pairs, including complete enumeration through two
  data bits and a deterministic 32-function phase/bias slice at three bits;
- all 256 depth-two full binary trees whose four leaves are arbitrary Boolean
  functions of one shared data bit;
- the explicit reused-selector falsifier for physical accounting.

Maximum entropy-identity and tree-telescope errors were respectively
`1.2e-69` and `1e-69`.  The author’s separate checker exhausts all 65,812
Boolean child pairs through three data bits; I inspected its implementation
and found its normalization consistent with the proof.

## Literature and dependency scope

The accepted proof is self-contained and makes no novelty or priority claim.
It does not use disjoint composition, read-once FEI, or plateaued-function FEI
as a premise.  Consequently this review accepts no broader composition or
literature claim.  Those results also cannot discharge the retained raw
difference packet in the shared-variable setting.

## Sources

- Target canonical final commit:
  `31e667c3af7f8441f14ab4615c13f21590cf7264`.
- Target report blob: `d484f022e09f80dbe41266b7b078d320511a0e2e`.
- Target proof blob: `fc6aea7e4bd63705a0f305932f4bc1e99eec1bf9`.
- Target checker blob: `47322317d7c8e1b65a3c71a8b46232948de96919`.
- Target Brain final commit:
  `6b69dd99a9c0a8afbb54ebeb51b1a902c72b62e4`.
- Mandatory sparse-surgery obstruction:
  `0b84fdeb8b04511228e1cd7d1746317e883e8df6`.

No subagent, protected source, paid compute, public release, email, scheduler
mutation, or native Brain ingestion was used.

## Persistence receipts

The ten-file canonical review was committed at
`163b1f303aac57452d143f531e14f8aeb402597a`; the byte-identical Brain
handoff was committed at `657974275b36a31aaf9db5891fbc632ce919990c`.
All twenty file readbacks were nonempty and matched the expected Git blob
SHAs.  Delivery does not alter the scoped verdict or the full-FEI status.
