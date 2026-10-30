# B06 / A027 — proper-block selection for Boolean modulation hierarchies

**Run:** `20261012T004320Z-fleet01-B06-a027-modulation-block`  
**Primary packet:** A027 (Block selection)  
**Attempt:** `A027-PROPER-BLOCK-MODULATION-1`  
**Claim:** `B06-A027-MODULATION-BLOCK-HIERARCHY-v1`  
**Gap:** `G-ADAPTIVE-BLOCK-PAYMENT`  
**Status:** restricted all-dimensional theorem PROVED pending independent
review; packet and full FEI remain OPEN.

## Exact result

For genuine Boolean `g` and genuine Boolean modulators `h_i` on a fresh
physical block `Z`, define

`F(x,z)=g(x_1 h_1(z),...,x_n h_n(z))` and `h_S=product_{i in S} h_i`.

The Fourier coefficients factor exactly:

`Fhat(S,T)=ghat(S) h_Shat(T)`.

Consequently

`H(F)=H(g)+sum_S ghat(S)^2 H(h_S)`,

`I_X(F)=I(g)`, and

`I_Z(F)=sum_S ghat(S)^2 I(h_S)`.

This gives a proper-block rule: query the entire fresh block `Z`, stop at the
physical child, and retain that child's entropy.  Every child is a sign-flip
of `g` and has exactly the squared spectrum of `g`.  In the source-pinned
B04 collision notation,

`B_Z=sum_S ghat(S)^2 H(h_S)` and `M_Z=0`.

Thus the required mixing control is exact,

`0 <= M_Z = 0 <= (2/ln 2) I_Z(F)`,

and the queried-influence telescope is exactly `I_Z(F)`.  If every occupied
auxiliary product obeys `H(h_S)<=C_Z I(h_S)`, the full block decrement is at
most `C_Z I_Z(F)`.  The older variables remain unqueried, so the block is
proper and is never `W=[n]`.

Iterating this construction with fresh disjoint blocks and always querying
the newest block yields an arbitrary-depth complete physical stopping tree.
All block budgets are disjoint, and the final leaf is a sign-flipped copy of
the base `f_0`; its entropy is retained.  If the base has constant `C_0` and
the levelwise auxiliary-product constants are `C_l`, then

`H(f_L) <= max_l C_l I(f_L)`.

This is a genuine growing-class theorem, not a universal existence result.

## Nonlinear family and quantified payment

Let `q_m` be the Boolean point defect that is `-1` at one input of the
`m`-cube and `+1` elsewhere, and take every modulator on a level equal to
`q_m`.  Products are either `1` or `q_m`.  If `p_odd` is the core spectral
mass on odd sets, then the exact level payment is

`Delta H=p_odd H(q_m)` and `Delta I=p_odd I(q_m)`.

Writing `N=2^m` and `delta=4(N-1)/N^2`,

`I(q_m)=2m/N` and `H(q_m)=h2(delta)+delta log2(N-1)`.

The elementary entropy bound in `ADAPTIVE_BLOCK_SELECTION.tex` proves
`H(q_m)/I(q_m)<=9/2` for every `m` (the exact ratio tends to `4`).  Hence
this nonlinear hierarchy has a dimension- and depth-independent constant
`max(C_0,9/2)`, with every added influence counted.

## Plateau and obstruction tests

- **Coded plateau:** when the modulators are characters, every auxiliary
  product is a character.  Every partial coordinate restriction preserves
  entropy, while the whole block has `B_Z=M_Z=0`.  The block rule crosses an
  arbitrarily long plateau but leaves all core entropy in the terminal.
- **Bent splice:** its branches do not have a common squared spectrum, so it
  is outside the theorem.  The accepted ratio
  `Delta_sel H/I_sel >= m-1` remains an obstruction to universal selection.
- **Rare defects:** the point-defect logarithmic entropy is included exactly;
  it is not hidden in a local refund.
- **Addressing and near tensors:** either can be a base only with its already
  established constant.  No shared-variable product inequality is used.
- **Shared signed dictator:** making the auxiliary-product premise
  unrestricted would be FEI itself, so no circular universalization is made.
- **Fixed-root telescope:** the terminal is explicit and no coefficient equal
  to the unknown root ratio is assumed.

## Verification

Command:

`python3 verify_modulation_blocks.py`

The deterministic audit checked 4,368 one-step Boolean instances, 256
two-level hierarchies, and 1,792 nodes on character-coded plateaux.  It made
177,376 assertions.  Walsh factorization, squared spectral laws, physical
child laws, influences, and queried-influence telescopes used exact rational
arithmetic.  The maximum displayed entropy residual was `0.000e+00`.
The all-dimensional result is the proof in `ADAPTIVE_BLOCK_SELECTION.tex`,
not an inference from the finite sweep.

## Movement and remaining obstacle

Prior status: A027 had the exact collision identity and the fixed-root signed
tree telescope, but no proved proper-block rule on a growing class.

New status: the modulation hierarchy supplies such a rule with zero mixing
debt, exact block and terminal costs, a nonlinear unbounded-depth subclass,
and explicit plateau/bent-splice boundaries.

The universal A027 gap remains: prove that every Boolean function outside
this sign-modulation class has some proper physical block or compensated
stopping tree with bounded conditional entropy payment.  The common-square
branch condition is sufficient here but is false for bent splices and cannot
be imposed universally.

## Source pins

- B06 compact contract blob: `4fdf4fe492970e589446cc141b90f7b88a81ff2d`.
- Execution protocol blob: `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- Stream index blob: `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.
- B04 collision packet canonical commit:
  `2ae17a5d45294822ac6743aeff1f8ca65e267ff6`.
- B04 original collision proof blob:
  `0c20fb66450849b6b7ddd4a9e955e6c6112c008e`.
- B20 fixed-root tree report blob:
  `b1f1d7e4440033f59d1b047ebb10ab0f84d3a332`, canonical core commit
  `9c670616a0ff2af489a0180445b5ad2bf3a4854b`.
- Source head inspected: `bdd93bb44cd0335a24e42e06dee81a73b5417768`.

No literature novelty claim, independent acceptance, native Brain ingestion,
or full-FEI conclusion is asserted.

## Handoff

A028 should use the hierarchy as a positive stopping-tree control and seek a
compensator when branch squared spectra vary.  A029 should test transport of
the exact terminal deficit across the first level that exits the modulation
class.  Independent reconstruction targets are A087 and A094; consumers are
A065, A087, and A097.
