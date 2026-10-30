# B19 / A094 — independent review of aligned-width shielding

## Verdict

**ACCEPTED AT THE FORMAL DECLARED SCOPE, WITH ONE WORDING CORRECTION.**

The following B05 claims survive independent proof reconstruction and an
independent exact implementation:

1. For every full-column-rank physical matrix (M_0) and arbitrary Boolean
   (D(u,z)),
   \[
   H(P)=2r+\mathbb E_uH(D_u),\qquad
   I(P)\ge r+\mathbb E_uI(D_u).
   \]
2. For aligned kernel width (t), every finite adaptive/pruned physical
   restriction tree and one common arbitrary disjoint terminal factor (h)
   satisfy
   \[
   U(Ph)-\sum_\ell w_\ell U(P_\ell h)
   \le \max\{2,C_t\}I(P).
   \]
3. The exact finite Boolean FEI constants through four bits are
   \[
   C_1=0,\quad C_2=2,
   \]
   \[
   C_3=\frac73+\frac34\log_2\frac{16}{9},\qquad
   C_4=\frac{45}{16}+\frac{49}{32}\log_2\frac{64}{49}.
   \]
4. A bound uniform in aligned width would imply full FEI even with shield
   rank one, by applying it to ((-1)^{xu}g^{\otimes N}).

The wording correction is important: (max\{2,C_t\}) is a proved valid
retained-(U) constant built from the exact finite-dimensional FEI constant.
The package does not prove that it is the *optimal* retained-(U) tree
constant.  None of the displayed inequalities requires repair, so reviewer
independence is preserved.

Full FEI remains **OPEN**.

## Review identity and source

- Primary review packet: A094 (proof-chain challenger).
- Target packet: B05/A023.
- Target run: `20261013T132528Z-fleet01-B05-aligned-width-four-a023`.
- Target finalized commit: `09fe8877f0362b6b46361d2e5acbcb10f8dc5dd9`.
- Target proof blob: `484097d7b7634b0fb644d38aee093cdd7d096fe8`.
- Stable gap: `B05_RARE_REFUNDS`.

## Analytic reconstruction

Summation over (x) enforces (M_0u+a=\alpha).  Full column rank leaves a
unique (u), giving

\[
\widehat P(\alpha,\gamma,\delta)
=2^{-r}(-1)^{b\cdot u+d+\gamma\cdot u}\widehat{D_u}(\delta).
\]

The squared spectrum is therefore an exact uniform mixture over (u) and
(\gamma) of the fiber spectra, proving the entropy identity with correct
normalization.

At least (r) nonzero physical (x)-rows each contribute influence (1/2).
Every (u_j) contributes (1/2), since the corresponding nonzero column of
(M_0) balances the derivative over (x).  The (z)-influence is precisely
the mean fiber influence.  This proves the influence lower bound without a
coordinate change.

The tree theorem is an endpoint telescope, not a local credit theorem.  The
weighted signed node sum equals root (U) minus weighted leaf (U); leaf
nonnegativity closes the bound.  Tensor additivity cancels a single common
disjoint factor (h).  Branch-dependent terminal factors or a nodewise
nonnegative payment are not covered.

The complete reconstruction is in `PROOF_RECONSTRUCTION.md`.

## Independent computation

`INDEPENDENT_CHECK.py` shares no code with the target checker.  It uses:

- direct character sums rather than a fast Walsh transform;
- physical edge-disagreement influence rather than the spectral formula;
- a separately written 56-term rational log enclosure;
- all small full-column-rank physical matrices, including nonidentity and
  rectangular matrices, rather than only identity shields.

It passed:

- all 32,768 four-bit truth-table representatives modulo output complement;
- 47 distinct nonconstant four-bit spectrum/influence profiles;
- rigorous (C_4) interval width below (2.07\times10^{-56});
- 16,092 direct shield reconstructions;
- 237,936 reconstructed nonzero Fourier atoms;
- the rank-one tensor-hardness base identity (H(q)=2, I(q)=1).

The exact maximizers through width four have the claimed one-point-defect
spectrum.  The four-bit runner-up is the embedded three-bit maximizer, with a
gap greater than (0.4465).

## Primary-source overlap

Potapov's 18 September 2026 manuscript proves (H\le4I) for plateaued
functions and (H\le2I) for partially bent functions.  It covers the
flat-spectrum endpoint of earlier shield results, but a general aligned
shield here has unequal arbitrary fiber spectra.  It does not state this
upper-set tree endpoint.

O'Donnell--Tan's composition theorem concerns inner functions on disjoint
input blocks with a biased-Fourier outer hypothesis.  The factor (D(u,z))
here shares (u) with the bilinear phase, so that theorem does not directly
supply the reviewed result.  The tensor hardness argument uses ordinary
disjoint additivity and is not presented as a new composition theorem.

No first, best, or literature-priority claim is accepted.  Exact source
comparisons are recorded in `LITERATURE_SCOPE.md`.

## Exact remaining gap

The class is uniform in shield rank, core bias, fiber choice, tree depth,
reveal order, and dyadic leaf rarity, but not in kernel width.  Removing width
is full-FEI-hard.  A separate obstruction also remains when the kernel is not
spanned by physical coordinates: already at nullity two, influence in an
induced kernel basis need not equal physical-coordinate influence.

The productive next move is therefore the dense-nullity-two physical-basis
comparison, not another fixed-width enumeration.

