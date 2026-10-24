# FEI worker handoff: compute-assisted bounded-potential search

20 September 2026. This handoff preserves the owner's request to save the preceding compute-strategy discussion for ongoing research. It is not a full-FEI proof, a computation executed in this archival action, or a scheduler/resource change.

## Full archive

Read [Compute strategy for FEI and the open-problem portfolio](../../../operations/COMPUTE_STRATEGY_2026-09-20.md), creation commit `db625968048e0388519db6e039929e4fe4f64760`, blob `958806b6a9ec6a6ee1dbd67c550e95cee694744e`.

**Link convention:** the canonical file is at repository root-relative path `operations/COMPUTE_STRATEGY_2026-09-20.md`; from this handoff's directory use [this relative link](../../../operations/COMPUTE_STRATEGY_2026-09-20.md).

Relevant existing pair: P03 and NM13-02 under the current LIVE20 mapping. No new owner or native task is assigned here. Read the [current FEI index](../README.md) and only the full proof dependencies actually needed; newer continuations supersede older state descriptions without erasing historical evidence.

## Proposed universal proof-search target — unproved

Find explicit fixed constants `C,K>=0` and a noncircular potential `Psi` such that, for every Boolean function on every finite uniform cube,

\[
0\le\Psi(f)\le K I(f),
\]

and for every nonconstant `f` there exists a physical coordinate `i` with

\[
H(f)-\tfrac12(H(f_0)+H(f_1))
\le C\operatorname{Inf}_i(f)+\Psi(f)-\tfrac12(\Psi(f_0)+\Psi(f_1)).
\]

The exact identity `I(f)=Inf_i(f)+(I(f_0)+I(f_1))/2` then yields, by induction to constant leaves,

\[
H(f)\le C I(f)+\Psi(f)\le(C+K)I(f).
\]

The induction is elementary; finding and universally certifying the potential is the unresolved mathematical content. The archive does not claim that a finite state system sufficient for this purpose already exists.

## Suggested computational attack

1. Search adversarially for functions violating the proposed restriction inequality at **every** coordinate, and check the global potential bound separately. A counterexample to a template is not a counterexample to FEI.
2. Fit an inspectable potential, for example `Psi=I*psi(s)` with a proved bounded range and explicitly defined spectral-matching/derivative statistics. Avoid opaque predictors and definitions that already assume the FEI conclusion.
3. Extract a universal certificate from the candidate using valid algebraic or interval inequalities. Prove Boolean realizability and restriction coverage of any relaxation. Passing a sample or a fixed-dimensional atlas is insufficient.

Preserve exact difficult functions, failed templates, computations actually executed, and the all-dimensional gap. Do not optimize weighted tree totals that already telescope identically to `H(f)` and `I(f)`.

## Required safeguards and newer inputs

- A finite high `H/I` witness only refutes its tested constant. Disjoint products preserve the ratio as a weighted average and do not amplify it to infinity.
- Keep enough of Booleanity `f^2=1`; arbitrary spectral probability distributions permit entropy `log n` at influence one.
- The old fixed-coefficient affine-drift route and absolute-overlap selector have recorded obstructions. Read their precise scope before proposing a variant. The recovery notice is not the entire raw recovered patch.
- The archive-time FEI index, blob `be66b9115a00b721b72b262dd595fbebd49f5ff3`, includes affine-fibre gluing and quadratic-symmetry stopping classes. Their full REPORT/HANDOFF files and local hypotheses must be recovered before use. They do not justify arbitrary fresh-tag removal, arbitrary overlapping high-degree cores, or an unrestricted hereditary bound.
- The affine-fibre handoff separates failure of a coefficientwise endpoint payment from the still-unresolved whole-function selector. Do not discard the surviving aggregate target on the strength of a fibre-level obstruction.

## Compute and reporting limits

Profile a reproducible pilot before assuming CPU is the bottleneck: record actual CPU/wall time, memory, arithmetic precision, exact success implication, proof dependencies, and a source-level stop/pivot criterion. The owner has requested archival delivery only; no paid compute, remote execution, schedule modification, or performance claim is authorized or asserted by this handoff.

Other tracks' compute priorities and concrete certificates are preserved in Sections 6-14 of the full archive. Delivery into the repository does not prove that a subsequent worker has already consumed it. Use the material inside substantive research, not as a reason for acknowledgment-only runs.

**End of FEI compute-strategy handoff.**
