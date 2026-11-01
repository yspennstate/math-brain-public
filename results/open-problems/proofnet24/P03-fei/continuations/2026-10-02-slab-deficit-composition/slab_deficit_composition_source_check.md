# Source and status check for deficit, parity and product extensions

Checked 2 October 2026 UTC. The generic identities below are elementary
standard Fourier analysis. Novelty and outside peer review are unverified.
No claim that the full Fourier entropy--influence conjecture is solved is
made. The new mathematical inputs in these applications are the campaign's
already internally audited uniform LTF and parallel-slab estimates.

## Primary sources actually inspected

1. Ryan O'Donnell and Li-Yang Tan, *A composition theorem for the Fourier
   Entropy-Influence conjecture* (ICALP2013), full16-page author manuscript:
   <https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf>.
   Its composition theorem and the influence-minus-variance budget framework
   are established prior work. Its product-law FEI+ formulation excludes
   the empty atom and has coordinate variance corrections. This checkpoint
   bounds the FULL ordinary uniform-input spectral entropy and does not
   silently replace it by uncorrected biased-input entropy. The manuscript
   was reread at the relevant formulation and composition identities.
2. Ryan O'Donnell, *Analysis of Boolean Functions*, May2021 author edition:
   <https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf>.
   Fact1.6 gives the character symmetric-difference identity. Proposition2.21
   gives the monotone singleton-coefficient/influence identity; input sign
   changes give its unate version. Root independently opened and inspected
   both statements, and the parity auditor did the same. These facts are
   credited, not proposed as new results.
3. The full [strong LTF theorem](../2026-10-02-strong-LTF-composition/strong_ltf_and_balanced_composition_proof.md)
   and [parallel-slab theorem](../2026-10-02-parallel-slabs/stripe_extension_parallel_slabs_proof.md)
   are the campaign's mathematical premises. Their complete audits and
   source checks, including Keller--Klein2019 and KOS2004, must be read when
   assessing the consequences here. They are not external acceptance.

## Research-status boundary

The universal signed high-influence split lemma is proved here from the
exact Boolean split entropy identity. Its low-influence conversion keeps
an explicit local-bound premise at every restriction. Ordinary class-wide
FEI alone does not imply that premise. The slab and strict-separated
crossing classes have it from the previous completed proof.

The parity and disjoint-product arguments are elementary consequences of
strong base estimates; no priority claim is made for their identities or
general conditional formulations. Limited searches for parity-modulated
LTF FEI, unate modulation and slab entropy did not locate a matching full
theorem. Some highly constrained fresh searches returned irrelevant pages,
so they provide no evidence of absence. Neither those searches nor the
internal audits certify historical novelty. Recent primary FEI papers
read in the preceding checkpoint still state the unrestricted conjecture
as open; this checkpoint solves only its stated subclasses and implications.

Arbitrary nearby crossings, general Boolean gates, shared-input circuits,
arbitrary unbalanced inputs to nonproduct composition gates, and nonuniform
input laws remain outside these results. A product node can accept biased
CHILD OUTPUTS because its spectrum tensorizes on disjoint uniform leaf
blocks. This does not extend a general LTF/slab node to such inputs.
