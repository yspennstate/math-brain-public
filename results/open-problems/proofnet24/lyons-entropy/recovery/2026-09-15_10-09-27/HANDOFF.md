# Recovery and continuation handoff — Lyons determinantal entropy concavity

Snapshot: 15 September 2026, approximately 10:09:27 UTC. Canonical destination: `yspennstate/math-open-problems`, private `master` branch. This recovery was requested by the repository owner after a research conversation appeared to freeze. No new proof-search agents were launched by the recovery process.

## What was recovered

The relevant conversation is the Lyons creative campaign, not the separate P03 Fourier Entropy–Influence project. Its original workspace was still receiving writes during this recovery, and the original coordinator also pushed a newer checkpoint during comparison. Therefore the word “frozen” must not be interpreted as proof that all workers had stopped.

The file snapshot contains 599 files from the current creative campaign and 316 from the preceding research session: 915 total, including 80 current C-numbered reports, 61 locally present preceding reports, root derivations, source notes, exact certificates, numerical arrays, scripts, and checkpoint variants. Other preceding reports already in GitHub were retained; absence from this local snapshot does not imply absence from the prior campaign.

[RECOVERY_MANIFEST.json](RECOVERY_MANIFEST.json) accounts for every file. It distinguishes files already in the correct path, identical content elsewhere in GitHub, files pushed by the original coordinator during recovery, missing files, and different local versions. Missing numerical `.npy`/`.npz` artifacts are included. Different historical versions are retained under immutable `variants/` or `concurrent-variants/` paths; they do not replace newer canonical reports.

Three administrative inputs are excluded from verbatim publication: an old directory-tree listing, a redundant upload payload, and mixed-session metadata containing the separate paper-delivery context. The relevant research continuation fields from the latter are retained in [SESSION_STATE_RESEARCH.json](SESSION_STATE_RESEARCH.json). All substantive source files are mapped to their exact Git objects. This is a recovery of accessible saved files, not a claim to have recovered unsaved model state or unavailable conversation messages.

The snapshot was a sequential file copy, not an atomic freeze. Its execution ledger records **75 completed assignments and 81 launched**, with C076–C081 marked running. Its older session-status cache still records 74/80. C072 has a completed manuscript and is completed in the captured ledger; C081 has a launch entry but no saved report in this snapshot. The 19 assignments C082–C100 had not been launched according to that ledger. These are historical recorded statuses, not an independent check of live workers. Preserve both versions rather than silently manufacturing agreement.

## Exact problem

For every finite dimension, Hermitian positive contractions `K0,K1`, and `0<=t<=1`, determine whether

`H(P_((1-t)K0+tK1)) >= (1-t)H(P_K0) + t H(P_K1)`.

Here `P_K` is the determinantal subset law characterized by `P(S subset X)=det K_S`, and entropy uses natural logarithms. The source is [Lyons, Determinantal Probability: Basic Properties and Conjectures, Conjecture 2.6](https://arxiv.org/html/1406.2707v1). [Gu's entropy note](https://sevenkplus.com/data/dpp.pdf) proves prior special cases including rank-one directions; these must not be counted as discoveries of this campaign.

**Universal status: OPEN.** Neither a complete proof nor a certified counterexample to the full assertion was recovered.

## Main mathematical reading order

Paths in this section are relative to `proofnet24/lyons-entropy/creative-2026-09-15/`.

1. `TARGET.md`, `CLAIM_LEDGER.md`, and `PRIOR_FRONTIER.md`: exact scope and the crosswalk preventing rediscovery of prior results.
2. `sources/PRIOR_PARTIAL_RESULTS.md` and `sources/old-097.md`, `old-104.md`, `old-107.md`: prior two-coordinate/block theorems, the three-site criterion, and projection-diamond reductions. Embedded old numbered-agent links refer to the preceding portfolio campaign.
3. `ROOT_RANK_TWO_SUPPORT.md`: arbitrary fixed two-dimensional support, allowing noncommuting active endpoints; `ROOT_DIAMOND_ACTIVE_MATRIX.md`: specified projection-background extensions.
4. `agents/C075.md`, `agents/C074.md`, and `ROOT_ORDERED_CONSTANT_KERNELS.md`: weighted count entropy, exchangeable/count-uniform bases, and explicit constant-upper-entry kernels.
5. `agents/C006.md`, `C022.md`, `C058.md`, `C061.md`, and `C062.md`: diagonal endpoint, block replacement, small borders, and finite-channel constructions.
6. `ROOT_FOUR_SITE_BOUNDARY.md`: the completed fully supported endpoint-vector theorem; distinguish it from C080's unfinished zero-coordinate extension.
7. `agents/C072.md` and its complete `computations/C072/` directory: the newest completed rank-three-support certificate.
8. `agents/C076.md` through `C080.md`, plus their saved computations: current drafts. Consult the manifest for an exact recovered version if the canonical manuscript has advanced.

All reports and computational evidence remain available in full. Recovery verification establishes content preservation. It is not a new independent line-by-line audit of every theorem or an assertion of historical novelty.

## Strongest recorded results and their limits

| Source | Recorded result | Limitation relevant to resuming |
|---|---|---|
| C006 | Concavity along every segment from an arbitrary kernel to a diagonal endpoint, every dimension | Does not cover arbitrary two nondiagonal endpoints |
| ROOT_RANK_TWO_SUPPORT | Concavity of `M -> H(P_(VMV*))` for any fixed isometry `V:C^2 -> C^n`, with full Hermitian active directions | Fixed support of dimension two; no arbitrary full-rank background |
| ROOT_DIAMOND_ACTIVE_MATRIX | Full noncommuting active `2x2` concavity under a certified projection diamond and `min(r,n-r-2)<=4`; rank-one backgrounds included | A general diamond is not proved; arbitrary background mixtures require another argument |
| C075 / C074 | Weighted Poisson-binomial entropy concavity and the full Hermitian Hessian sign at every count-uniform occupation law; strict at nonscalar interior bases | These are special base kernels, not every kernel or every circulant |
| ROOT_ORDERED_CONSTANT_KERNELS | Explicit complex constant-upper-entry family inside C074, with exact atoms and physical domain | Corollary of C074, not a new general theorem |
| C058 / C062 | Small singleton borders of strict cores; fixed coherent satellite blocks coupled to a free two-site core | Large arbitrary borders, moving satellite data, or changing cross orientations remain outside |
| ROOT_FOUR_SITE_BOUNDARY | Full sixteen-dimensional negative-Hessian neighborhood near `(0,p,q,1)` with both endpoint vectors fully supported; independent endpoint rates and zero active minors allowed | Zero endpoint coordinates and arbitrary interior kernels are not settled |
| C072 | Specified six-site odds `diag(1,1/2,...,1/6)+s 11^T`, `2^32<=s<=2^33`, and the explicit support `U`: full nine-real-dimensional Hermitian support gap `1/10000`; exact rational Bernstein certificate | Does not prove arbitrary rank-three directions or arbitrary three-site kernels |
| C076 snapshot | Full saved derivation for a rank-one bridge with three moving reservoir modes on explicit balanced-domain LMIs | The captured report says verifier follows; the captured ledger has no terminal completion. Preserve as a draft pending its later handoff |
| C077 / C078 / C079 / C080 snapshots | Gauge-tangent identity; feasible principal-minor redistribution; independent four-site phase route; grouped singular-atom boundary expansion | Explicitly unfinished; no full theorem should be inferred from these checkpoints |

## Exact obstructions to preserve

The following are failures of proposed methods, not counterexamples to Lyons:

- The full entropy Hessian is `-sum (p'_S)^2/p_S - sum p''_S log p_S`. Dropping either contribution changes the problem.
- Covariance-only Fisher bounds can fail at a kernel with negative full entropy curvature. C072 retains all atom scores and supplies a concrete strict separation from the linear-occupation projection.
- Small trial spaces and pointwise resolvent positivity are not universal. See C010, C011, C005, C046, and C050.
- A classical reset or channel interpretation needs its stated rank and sign conditions. A common invariant law alone does not imply the required Shannon concavity; see C021–C025.
- A nonlinear interpolation of odds or principal-minor invariants is not an affine interpolation of the original kernel.
- Occupation entropy is basis dependent. Arbitrary unitary diagonalization cannot turn a proved coordinate-block theorem into a theorem for arbitrary kernels.
- A proved low-rank boundary neighborhood, a finite numerical scan, or a finite interval certificate does not cover the full interior or all dimensions.

## Concrete continuation priorities

**First milestone: unrestricted three-site concavity.** The prior `old-097` reduction isolates a Schur/Fisher criterion, recorded as `b^T C^-1 b >= 2` with its definitions in that report. Prove it for the complete feasible three-site atom chart, or obtain an exact feasible counterexample. The chart, covariance refinements, phase obstructions, finite replica certificates, and boundary normal forms are already available. Keep all complex phases and singular strata explicit. The full three-site case was not resolved in the recovered record.

**Alternative structural milestone: the unrestricted projection diamond/induction step.** Existing certified six-site families and rank-one backgrounds are useful test cases. Establish the actual Hall/transport condition for arbitrary flags and determine what additional Fisher estimate is needed for general background ranks. Do not assume that a positive coupling in a finite sample or special frame implies the universal coupling.

**Immediate unfinished assignments:** C076 needs its final verification record; C077 seeks the sign beyond the gauge-orbit identity; C078 must control acceleration when returning from invariant coordinates; C079 needs uniform phase estimates and its verifier; C080 needs exact jets, a uniform independent-scale remainder, and an explicit open region. C081 had no saved output in this snapshot. Check subsequent canonical files and execution records before assigning replacements.

The repository-wide choice and resource judgment are in [PORTFOLIO_ASSESSMENT.md](PORTFOLIO_ASSESSMENT.md). More compute can check finite certificates and search for counterexamples; this recovery provides no basis for guaranteeing a solution to the universal conjecture.

## Integrity and reproduction

The manifest provides exact byte lengths, SHA-256 hashes, and Git blob identifiers. [restore_snapshot.py](restore_snapshot.py) reconstructs the substantive source snapshot from those Git objects in a local clone into a new directory, without replacing an existing destination. This also recovers variant files with their original relative layout for reproducible computations.

Publication receipts belong in a subsequent file because this handoff cannot truthfully contain its own future commit hash. No email or outside collaborator notification was sent by this recovery.
