# Strong LTF/composition source and scope check

Checked 2 October 2026. The underlying primary inputs and current LTF status
search are documented in
[the largest-weight source checkpoint](../2026-10-02-largest-weight/largest_weight_ltf_prior_art_checkpoint.md).
The new complementary split argument is elementary and requires no further
non-elementary analytic input.

The full primary O'Donnell--Tan manuscript, *A composition theorem for the
Fourier Entropy-Influence conjecture*, ICALP 2013, was inspected:
<https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf>,
<https://arxiv.org/abs/1304.1347> (submitted 4 April 2013).
Its Proposition 2 gives exact entropy, influence and variance identities
for disjoint composition. Theorem 1 proves same-constant closure for FEI+;
Theorem 3 treats bounded-arity gates. Generic composition and the I-Var
budget are established prior work, not achievements newly claimed here.

Their FEI+ entropy omits the empty spectral atom, and under biased input
also has a product-variance correction. The present LTF theorem uses the
FULL ordinary uniform-input spectral entropy, including its empty atom:
H(f)<=C[I(f)-Var(f)]. With balanced children, the exact specialization
reproduced in the proof applies without invoking any biased-input theorem.
It permits arbitrary LTF gate fan-in with one constant, while requiring
disjoint leaf blocks and balanced nonroot outputs. The root may be biased.
The distinction in entropy definitions and balance hypotheses is retained.

Targeted source checks also found the previously inspected revised ECCC
TR13-052 manuscript and its AND/OR/XOR/NOT read-once result. The 2013
all-LTF abstract claim was corrected in its 2018 revision and must not be
used as a valid proof of the deterministic LTF target. Read the actual
revised source and the prior checkpoint for the full record.

No earlier complete proof of the precise full-entropy LTF deficit bound
and consequent unrestricted-fan-in balanced subclass was located in the
bounded search. This does not certify priority. Internal proof verification,
exact checks, historical novelty, and external peer review remain distinct.
General Boolean FEI, arbitrary unbalanced children, shared-input circuits,
and uncorrected entropy for arbitrary biased-input products are not solved.
