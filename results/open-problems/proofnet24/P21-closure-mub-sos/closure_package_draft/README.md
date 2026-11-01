# P21 draft closure package — degree-four vector-coordinate MUB SoS

**Status:** DRAFT / CLOSURE PENDING. This folder is intentionally **not** named `paper_*` and is not a posted or closed deliverable. The mathematical target is literature-KNOWN and independently reconstructed in P21, but the fleet closure rule still requires a P26 end-to-end audit in addition to the existing P20 OTHER-track audit.

## Outside problem

Afonso S. Bandeira (2025), Randomstrasse101, *Mutually Unbiased Bases, ETFs, and Zauner's Conjecture*, Open Problem 23; intake I0104.

Source: `https://randomstrasse101.math.ethz.ch/posts/FramesMUBZauner/`

The source asks whether a degree-four Sum-of-Squares proof can exclude seven mutually unbiased bases in `C^6` and explicitly describes two direct vector-coordinate encodings: quartic squared-overlap equalities and a `2 x 2` Hermitian LMI encoding.

## Exact answer and scope

For both source-explicit **vector-coordinate** encodings, the answer is **NO**. Independent Haar-random orthonormal bases define a feasible degree-four pseudoexpectation for every dimension `d` and every number `m` of proposed bases. This is already known from Shreyhaan Sarkar, arXiv:2606.13903 (2026), and is independently reconstructed in `main.tex`.

This does **not** settle unrestricted `MUB(6)<7`. That global conjecture is owned by C29. It also does not exclude a degree-four proof in stronger projector/lifted/noncommutative coordinates. Sarkar's centered projector-coordinate degree-four argument recovers only the general bound `m <= d+1`, which is tight at `d=6,m=7`.

## Normalization gate

The Randomstrasse definition is

`|<v,w>| = 1/sqrt(6)`.

Therefore the quartic squared-overlap constraint is

`|<v,w>|^2 = 1/6`.

The source page prints `1/sqrt(6)` inside one already-squared display; that is inconsistent with its definition and subsequent LMI threshold. Sarkar explicitly flags the same typo. This package uses `1/6` for squared overlaps and `1/sqrt(6)` only for amplitudes/LMI diagonals.

## Frozen metric

Seven labeled bases give `C(7,2)=21` labeled cross-basis blocks, each containing `6^2=36` quartic cross equations, for `756` equations total. The Haar pseudoexpectation satisfies all 21 blocks simultaneously, so the tracked value is exactly

`0/21 exactly eliminated labeled cross-basis blocks`.

This is a mathematical impossibility certificate for a degree-four refutation in the frozen formulation, not a failed search.

## Files

- `main.tex`: self-contained source-matching proof and scope statement.
- `exact_checker.py`: exact finite-core checker using only Python `fractions.Fraction` plus a tiny exact `Q(sqrt(6))` class.
- `exact_checker.out`: archived output from the executed checker; it ends in `ALL_EXACT_CHECKS_PASS`.

The checker verifies:

1. `21` blocks and `756` cross equations;
2. the correct `1/6` squared-overlap normalization;
3. a `325 x 325` degree-four Haar moment Gram matrix for one cross pair;
4. an explicit `433`-term positive rational weighted-square Gram identity, entrywise;
5. `E(Re <x,y>)^2 = E(Im <x,y>)^2 = 1/12` and `E|<x,y>|^2 = 1/6`;
6. the degree-four LMI compression rank `12` and singular value `1/6` for `d=6`;
7. the `1010`-dimensional affine localizer decomposition into twelve active `2 x 2` blocks plus `986` positive scalar directions;
8. exact active-block determinant `5/36` and an exact `Q(sqrt(6))` LDL factorization.

## Audit state

At preparation time:

- `P20-AUDIT-P21-HAAR-DEG4-02 = PASS` is one qualifying OTHER-track audit of the frozen quartic target.
- The latest P26 report still audits C31 rather than P21.
- Therefore the closure count remains `1/2`; this package must not be renamed or represented as a final `paper_*` deliverable yet.

Once P26 supplies the required independent end-to-end audit, the final closure step is to copy the verified self-contained materials into the required `paper_<name>/` folder, record both audit IDs and exact commits, and request P26's authorized shared-ledger retirement/reassignment update.

## Literature boundary

Sarkar (2026) gives the direct current answer to Open Problem 23. The April 2026 McNulty-Weigert review still treats the unrestricted dimension-six complete-MUB existence problem as open. A separate 2025 arXiv preprint by Stefan Joka claims a much stronger unrestricted resolution via Latin squares, but later 2026 peer-reviewed review literature still treats the dimension-six problem as unresolved; P21 does not adjudicate that broader disputed claim and does not alter C29's scope on its basis.
