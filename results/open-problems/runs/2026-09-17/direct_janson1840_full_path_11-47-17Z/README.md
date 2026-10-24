# Janson 18.40: full-path subsequence complete condensation

Date: 17 September 2026. Repository: `yspennstate/math-open-problems`, branch `master`.

**Status: COMPLETE PROOF CANDIDATE IN THE FULL-PATH SOURCE SCOPE.** Independent end-to-end audits: **0/2**. Publication novelty: **UNVERIFIED**. The new argument removes the bounded-upward-increment hypothesis; no unresolved mathematical lemma is being assumed in `main.tex`. This status is a statement about the written argument, not independent certification or a shared-ledger promotion.

## The theorem

Fix nonnegative finite weights `w_j`, with `w_0 > 0` and

```text
limsup_{j -> infinity} w_j^(1/j) = infinity.
```

Let `m_n` be any prescribed admissible full sequence with `m_n/n -> lambda`, where `0 < lambda < infinity`. For the allocation with probability proportional to the product of its box weights, the claimed theorem is:

```text
There exists n_r -> infinity such that Y_max(m_{n_r}, n_r) / m_{n_r} -> 1
in probability.
```

Consequently `limsup_n E[Y_max/n] = lambda`, and along that subsequence the remaining total mass divided by `n` tends to zero. In particular the full path cannot have `Y_max/n -> 0`.

There is no bounded-jump, monotonicity, full-support, smoothness, ratio-growth, or regular-variation assumption. The weights and the prescribed mass path are fixed throughout. Sparse and periodic supports are handled by span reduction and a finite numerical-semigroup terminal representation.

The theorem also permits an admissible index set `N_1 < N_2 < ...` with `N_{j+1}/N_j -> 1`; this includes the arithmetic lattice of admissible tree sizes. It does not assert the conclusion on an arbitrary preselected lacunary subsequence. Janson's Example 18.38 already gives sublinear maxima on such a subsequence. Nor does it assert that every ball occupies exactly one box with probability tending to one.

## What changed from the preceding contribution

Predecessor:

```text
runs/2026-09-17/direct_janson1840_record_tilt_10-48-30Z/report.md
commit 26b9dea957795339a6c558a3fd3ef52798543470
```

The predecessor used a first-crossing argument and a fixed reservoir for bounded overshoots. It explicitly left arbitrary mass jumps open. The new proof does not try to hit the prescribed total by that crossing.

It instead selects `n` near `(1+4 delta) k/lambda`, where `k` is a geometric record size. A typical background has total at most `delta k`. It inserts a giant of size `k` and a supported representation of the exact residual into empty boxes. The occupation-count map is injective, and its factorial ratio gives

```text
Z(m,n) >= [n / 2^(C+1)] w_k W_res Z_u(t,n).
```

Here only the number `C` of fixed terminal pieces enters the constant; the number of large reservoir pieces may grow. This retains the complete small-box factor `A^n`, which cancels exactly against the numerator. Thus no growing overshoot penalty has been discarded.

The second new ingredient sums the greedy energy loss over geometric records. The memory kernel has total mass

```text
theta(a,D) = 2 a^(3-D) [(D-1)/(a-1) + 1/(a-1)^2],
```

which is made less than `1/4`. The polynomial record penalties are summed only at active scales. Their potentially long plateaus are charged once per plateau, giving a finite total. The finite terminal representation contributes a summable-coefficient term absorbed by another factor less than `1/4`. A persistent positive lower bound for the no-giant probability would then keep the record envelope bounded, contradicting zero radius. Letting the geometric base approach one and diagonalizing yields near-total, not merely positive-fraction, subsequence condensation.

The complete derivation, including every finite comparison and the summation constants, is in `main.tex`. It compiles to a seven-page PDF with references.

## Executed checks

Run:

```bash
python3 check_full_path.py > checks.reproduced.json
cmp checks.json checks.reproduced.json
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The script has no third-party dependencies. All PASS assertions use integers or exact rational numbers. It checks:

- 12 occupation-count identities across six insertion examples, including repeated reservoir sizes, overlap between large and terminal roles, sparse background support, and extra original weights above the giant;
- the exact geometric-kernel sum for five bases, and 16 finite nonnegative convolution cases;
- 36 plateau-charging cases, including a plateau spanning 398 scale steps;
- 391 supported greedy decompositions and exact energy bounds.

Result: **ALL_EXACT_CHECKS_PASS**. A second execution reproduced `checks.json` byte-for-byte. Finite checks are not a formal proof of the limiting theorem and are not independent audits. The PDF was compiled twice, checked for undefined references and overfull boxes, and visually reviewed in a PDF renderer.

## Source and literature scope

The exact source is S. Janson, *Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), 103--252, DOI 10.1214/11-PS188, arXiv:1112.0510, Section 18.6, Problem 18.40. The source question, neighboring Example 18.38, and finite positive-density convention were checked directly; the page containing the question was visually inspected (PDF page 122, one-based).

The full text of S. Janson, T. Jonsson and S. O. Stefansson, *Random trees with superexponential branching weights*, arXiv:1104.2810, was also recovered. Its Theorem 2.3 assumes the successive-weight ratio tends to infinity and gives local weak convergence; Theorems 2.4-2.5 treat explicit factorial families. Those specific statements do not establish the unrestricted fixed-path theorem claimed here. This is not an exhaustive later-literature review. Keyword searches were largely unhelpful; no publication-priority clearance is claimed.

The positive-boundary-mean Problem 18.39 is not solved by this argument. The earlier withdrawn F0060 all-in-one-box proof is not used. No shared root ledger, peer file, historical report, native schedule, email, public repository, or Drive file was changed by this contribution.

## Independent audit targets

The main proof is self-contained. An outside audit should rederive the occupation-count ratio in Lemma 3, the once-per-plateau estimate in Lemma 4, the exact lag sum in Lemma 5, and the finite-prefix absorption in equations (19)-(21). It should also check the order of fixed parameters, the span reduction, and the dense-index/full-sequence distinction. No outside PASS verdict has yet been obtained.

Suggested ledger delta, not applied:

```text
source: F0060 / Janson Problem 18.40
claim: every admissible positive-finite-density full path has a subsequence
       with Y_max / m -> 1 in probability, for every fixed zero-radius law
scope_gap_from_predecessor: removed (unbounded total-mass jumps allowed)
written_proof_status: COMPLETE_CANDIDATE
independent_audits: 0/2
source_registry_promotion: NOT_APPLIED_PENDING_AUDIT
novelty: UNVERIFIED
checker: ALL_EXACT_CHECKS_PASS; finite algebra only
```
