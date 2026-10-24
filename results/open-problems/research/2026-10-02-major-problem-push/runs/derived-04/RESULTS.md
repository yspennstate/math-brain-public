# Deterministic LTF FEI and the fourth forest coefficient

Research checkpoint, 2 October 2026. Full derivations and independent audits
are archived in the problem tracks linked below. Mathematical verification,
finite checks, historical priority and external peer review are distinct.

## 1. FEI for all deterministic linear threshold functions

The complete internally audited theorem is

\[
 H(f)\le C_* I(f)
\]

for every Boolean linear threshold function under uniform cube input, with
arbitrary real weights and arbitrary threshold. More strongly, splitting on
any largest absolute defining weight gives

\[
 H(f)-\tfrac12[H(f^+)+H(f^-)]\le C_* I_i(f),
\]

with a universal constant. The full restriction induction is included.
No regularity or random-weight hypothesis is required.

Track:
[`proofnet24/P03-fei/continuations/2026-10-02-largest-weight/`](../../../../proofnet24/P03-fei/continuations/2026-10-02-largest-weight/).
Read `largest_weight_ltf_fei_proof.md`, all four independent audits,
`largest_weight_ltf_prior_art_checkpoint.md`, and both verification scripts.
The original candidate remains preserved.

The proof combines two established inputs, the KOS biased-noise estimate
and Keller--Klein maximal-influence estimate, with a relative slab-stability
bound retaining the rare-event factor, low-degree separation at the slab's
variance/bias scale, and a dyadic KL bound for the pivot's spectral bit.
Independent audits reproduce the entropy step using a geometric reference,
an exponential test function, and bounded two-sided degree-bin entropy.
They also verify the interference correction in the exact split identity.

The two finite suites passed 1,632 and 1,642 nonconstant LTF cases. The first
includes 13,056 slab-noise checks, 18,022 low-degree checks and 22,814 pair-tail
checks; the second independently uses integer Walsh transforms and rational
spectral identities. Floating-point entropy calculations are sanity checks,
not asymptotic proof certificates. Root reran both successfully.

The preceding arbitrary-bias regular corollary and its L2-nearuniform
consequence are archived separately in
`proofnet24/P03-fei/continuations/2026-10-02-regular-bias/` with their independent
audit and checks. They are now subsumed by the complete LTF theorem, and are
retained as an independent known-results route.

The primary random-LTF paper described general deterministic-LTF FEI as
unknown in 2019. An apparent old 2013 solution was removed in the 2018
revision of ECCC TR13-052; the actual revised manuscript has only the
O(sqrt(n)) LTF entropy bound. No earlier complete solution was located in the
bounded current search, but historical novelty and definitive present-day
priority are not certified. This is internal verification, not external
peer review. Unrestricted Boolean FEI and biased-input-product FEI remain
unproved by this work.

## 2. General fourth-coefficient forest sum of squares

For the weighted forest edge-Rayleigh polynomial, write

\[
 \mathcal R_{ef}(\lambda\mathbf c)
 =H_0\lambda^{2n-4}+H_1\lambda^{2n-5}
   +H_2\lambda^{2n-6}+H_3\lambda^{2n-7}+\cdots.
\]

The new general theorem proves H3>=0 whenever H0=H1=H2=0, with the explicit
electrical shifted-response sum of squares. A positive H3 implies strictly
negative marked-pair correlation for all sufficiently large fugacities.
It extends the already archived H2 theorem by one full degenerate order.

Track:
[`proofnet24/P14-probability-correlation/continuations/2026-10-02-general-H3/`](../../../../proofnet24/P14-probability-correlation/continuations/2026-10-02-general-H3/).
Read `GENERAL_H3_SOS_PROOF.md`, its independent derivations/audits, and
`H3_CHECKS_README.md` for reproducibility.

The key algebra is the local marked-score Ward identity with a valid root
outside the transformed port set, the necessary second-score correction,
and a multiport-current electrical completion. Three independent analytic
audit branches and root's separate derivation pass. Nine exact graph cases,
including positive-off-diagonal response matrices, agree with the formula.
Independent full subset enumeration and frontier-connectivity DP give two
11-vertex H3 values, 83106928972800000 and 42689908537165440000. Root reran
both hard checks and the two response obstructions.

The exact response-space kernel and the H3zero aggregate-support separation
are also proved. Two failed stronger claims are preserved: the response Gram
need not have nonpositive off-diagonal entries, and higher marked scores need
not remain in the exterior algebra of the linear contrast modes. Explicit
rational and symbolic exterior-algebra certificates demonstrate both failures.
Neither obstruction invalidates the proved H2 or H3 formula.

The classical forest/Grassmann and supersymmetry tools are credited, as are
the prior H0/H1 results and equality geometry in arXiv:2610.00549. Specific
historical novelty remains unverified. H0=H1=H2=H3=0 still needs later
coefficients; chains show arbitrarily many leading zeros. No full forest,
all-fugacity, negative-association, or q<1 random-cluster theorem is claimed.

## 3. Next research boundary

The strongest concrete next forest route is recursive regional absorption
of the shifted responses. Geometry, score propagation, finite termination,
and later coefficient identification each require a full audited proof;
matching K4 chains is insufficient. For FEI the general Boolean case is
still open, and the LTF proof's parallel-slab concentration has no automatic
extension to arbitrary monotone functions. Preserve the earlier max-influence
and separator counterexamples as limits on such an extension.

Whitt/MMPP results remain established baselines, not new achievements of
this checkpoint. No email, outside publication, or other campaign changes
are part of this work.
