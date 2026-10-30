# A079 conditional-energy ledger

## Construction

For uniform `a,b in F_2^k`, define

- `U = 1[a=0]`,
- `V = 1[a+b=0]`,
- `f=(-1)^(UV)`.

The encoders share every `a` coordinate.  Their outputs are nevertheless
independent Bernoulli(`2^-k`) because `(a,a+b)` is uniform.

## Spectral dependence

The centered normalized `U` label is `S != empty`; the `V` label is the
diagonal pair `(T,T)`, `T != empty`.  In the product component the physical
label is `(R,T)=(S xor T,T)`.  Hence `R != T` deterministically, so the two
physical label blocks are correlated.

Let `q=2^(k-1)/(2^k-1)`.  Exactly,

- `H(R,T)=2 log2(2^k-1)`;
- `H(R|T)=log2(2^k-1)`;
- `E(|R|+|T|)=2k q(1-q)+kq`.

The map `(S,T)->(S xor T,T)` is injective.  Thus shared variables do not
compress the conditional label in this realization.

## Universal physical payment for the same gate law

For arbitrary deterministic shared-variable encoders with the same output
law, the negative cell has density `delta=2^-2k`.  Edge isoperimetry gives

`I((-1)^(UV)) >= 2 delta log2(1/delta) = 4k 2^-2k`.

For the B09 gain,

`J_k <= 4 2^-2k (k+log2(e))`,

so `J_k/I <= 1+log2(e)/k`.  No conditional-entropy assumption is used; any
additional conditional charge only strengthens the barrier.

## Tensor and normalization guard

Disjoint products add both `H` and `I`, so tensoring this realization cannot
increase its FEI ratio.  The explicit example is a point defect with
`H/I -> 4`.  The bound concerns actual uniform-cube influence, not a biased
surrogate, selector increment, or raw convolution mass.

## Unpaid scope

The result does not rule out a different correlated gate whose gain is not
localized on a rare joint cell.  That is the next A079 search space.
