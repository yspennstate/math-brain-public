# Critical rectangle-interface payment

## Frozen class and conclusion

The source class is genuine Boolean `f:{-1,1}^N->{-1,1}` that is
**descendant-critical for the ordinary Fourier ratio**: every nonconstant
physical restriction `g` has `H(g)/I(g) <= R(f)`.

For a physical cut `A|B`, the independently defined interface is the
multiplicative rectangle-defect probability

`rho_A(f)=Pr[f(x,y)f(x',y)f(x,y')f(x',y')=-1]`.

It is measured directly on the truth table. It is not an entropy remainder,
not a spectral probability law chosen ad hoc, and not qualitative circuit
connectedness.

The anchoring identity proves that some Boolean product `u(x)v(y)` has Hamming
error `epsilon<=rho_A(f)`. Combining this with the A053 near-tensor theorem and
the elementary universal estimate `R(f)<=3N` proves

`R(f) I(u)-H(u) <= E_{N,a}(rho)`,

where

`E_{N,a}(rho)=2 h2(2 sqrt(rho))+(2N-a)2 sqrt(rho)+6aN rho`.

This is the corrected component comparison. If `u` is nonconstant, its ratio
deficit is bounded by `E/I(u)`.

## A noncircular influence-paid subclass

Let `J=I_A(f)>0`, `0<kappa<=1`, and `t=2sqrt(rho_A(f))`. The following three
truth-table/influence conditions are sufficient:

1. `t <= kappa^2 J^2/144`;
2. `t <= kappa J/(6N)`;
3. `t <= sqrt(2 kappa J/(9aN))`.

They imply

`E_{N,a}(rho) <= kappa J`,

`I(u) >= (1-kappa/(9N))J >= 8J/9`, and hence

`R(u) >= R(f)-9kappa/8`.

The three conditions pay, respectively, the binary-entropy continuity term,
the ambient spectral-alphabet term, and the physical influence-transport term.
They do not mention the desired factor-ratio conclusion. This is a complete
payment theorem on the stated subclass. The missing universal step is to prove
that every high-ratio critical source admits such a cut, or to replace this
interface by a stronger one.

## Mandatory component controls

The theorem does not revive either rejected support-component rule.

- The pinned nine-bit indicator has exactly two connected support components
  and violates raw component entropy subadditivity by more than `1/5000`.
  Its support components are not Boolean product factors exposed by a physical
  cut. No raw component entropy inequality is used here.
- The pinned seven-bit indicator has exactly two connected components and
  `R(A union B)>max(R(A),R(B))` by more than `0.0028` in natural-log units.
  It is not descendant-critical: fixing two data coordinates yields an OR2/NAND2
  descendant whose ratio exceeds the union ratio by more than `0.59`. The new
  proof uses descendant-criticality precisely through the A053 block inequality.

Thus the new result is compatible with both exact counterexamples and does not
reinterpret connected truth-table support as a physical descendant.

## Adversarial family checks

- **Exact and near tensors.** At `rho=0`, exact tensor purity is recovered.
  Equal-ratio critical tensors remain allowed. A one-point surgery has
  `rho<=4*2^{-N}` across an original factor cut, so a block with nonnegligible
  influence eventually satisfies the paid-cut criterion; an arbitrary
  fixed low-ratio hidden factor therefore cannot remain inside a high-ratio
  descendant-critical family.
- **Rare restrictions and sparse defects.** When `J` is tiny, the admission
  threshold becomes correspondingly stringent. The theorem makes no universal
  rare-event refund claim and does not conflict with `B05_RARE_REFUNDS`.
- **Addressing and multiplexers.** No fresh-selector or orthogonality endpoint
  is reopened. A cut is useful only after its actual rectangle defect and block
  influence meet the displayed conditions; selector labels are not counted as
  free components.
- **Prime Boolean gates.** A genuinely prime gate with no low-defect physical
  cut simply falls on the other side of the alternative. The result does not
  assert that primitivity alone controls entropy.
- **Arbitrary-core embeddings.** One-point surgery can make a tensor prime
  while keeping `rho` exponentially small. The theorem shows why qualitative
  primitivity is insufficient but true ratio criticality can still reject a
  fixed lower-ratio core. It does not reject equal-ratio core replication.

## Exact finite reproduction

`verify_rectangle_interface.py` exhausts all `65,536` Boolean sign tables on
a `4 x 4` product cube. With exact integer and `Fraction` arithmetic it checks
for every table that the sum of the sixteen anchored product-error counts is
exactly the ordered rectangle-defect count, and that the best anchored Boolean
product error is at most the defect probability. It passed `131,200`
assertions. This finite check reproduces the combinatorial identity only; the
all-dimensional theorem is the analytic proof in `COMPONENT_EXCESS.tex`.

## Status

The rectangle anchoring lemma, controlled-excess inequality, and the stated
influence-paid subclass are **PROVED pending independent review**. Universal
admission of a paid cut is **OPEN**. Full FEI is **OPEN**.
