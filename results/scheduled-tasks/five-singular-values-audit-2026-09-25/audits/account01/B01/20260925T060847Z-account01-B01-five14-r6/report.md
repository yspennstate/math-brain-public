# account01/B01 pass 6 — exact five-singular-value paper

Run: `20260925T060847Z-account01-B01-five14-r6`

Objective: `QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925`.

Source pins:
- repository: `yspennstate/math-open-problems`
- commit: `ec211ba2d77a4a9850168c6af1574ea651feaa7c`
- `short.tex` blob: `c4f2a997cf336ee974e15409b5bccdd8cca039d8`
- `short.pdf` blob: `8be3aae36ecad7a9dc9b7c95978aad09499f32d0`
- PDF SHA-256: `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`
- source length: 676 physical TeX lines; PDF: 14 pages.

I re-read the fresh owner controls/package, created and read back only the B01 current-hour sign-in and acknowledgement, then independently reconstructed the full TeX proof in a sixth order emphasizing dimensions, exceptional values, null sets, rank thresholds, and dependency propagation. Earlier B01 PASS labels were not premises.

## Verdict

No fatal counterexample to Theorem 1.1 was found. The immutable literal source remains **GAP**, not end-to-end PASS.

The repaired argument still closes with the original hypotheses and the same branch maximum `<269 K^2/s`, hence the stated `270 K^2/s`:
[
s_5(A)ge s>0
Longrightarrow
|p_{X^TAX+b^TX+c}|_{infty,mathrm{ess}}
le270,K^2/s .
]
No support, moment, smoothness, iid, sign, remaining-spectrum, or affine restriction is introduced. The general theorem is essential boundedness; only the integrable-Fourier branch automatically supplies a continuous density.

## Literal-source gaps/errors retained

1. **C04, L41 / p.1 — FALSE exposition.** The abstract random-sign conversion needs the no-pivot/small-entry hypothesis; `A=I_5` is a counterexample to the unqualified summary.
2. **C07, L62 / p.1 — UNCHECKED current literature status.** Targeted current searches found adjacent regularity results (for example Herry–Malicet–Poly under substantially smoother/iid hypotheses) but did not establish exhaustively that the exact arbitrary-density three-eigenvalue question remains open. This is not a proof dependency.
3. **C05, L65 / p.1 — FALSE/overstated prose.** The later proof gives square-root/logarithmic upper envelopes, not an assertion that every conditional law actually has the named singularity.
4. **R5-L148, Lemma 2.5 / p.3 — GAP.** The approximation-number identity is true with zero padding, but the converse proof's “first j right singular vectors” language is undefined if padded `j` exceeds the right-singular-vector dimension. Split off `j>min(rows,cols)` using `s_j(T)=0` and `B=T`; every actual downstream use in this manuscript is in range.
5. **C02, L319–322 / p.7 — GAP.** Insert `|E F|^2 <= E|F|^2` before passing from the conditional Step-2 estimate to the unconditional squared characteristic function.
6. **C08 / R5-L398, Lemma 5.1 / p.9 — GAP at one null point.** The displayed square-pushforward density formula is not literally defined at `z=v`. State it a.e./for `z!=v` and choose any finite representative at `v`; `P(Y=m)=0`.
7. **C01, L412 / p.9 — FALSE local chart claim.** The half-open polar chart is not an ordinary-topology global diffeomorphism. Delete one null seam ray/use an open angular chart; the Jacobian and constant are unchanged.
8. **C03, L441 / p.10 — GAP.** Explicitly state that the hyperbolic critical level is the union of two affine lines and has probability zero under the joint density.
9. **C09, L613 / p.13 — NEW TO B01 THIS RUN, GAP (notation/order).** Lemma 5.5 defines `J(d)` only for `d!=0`, but Proposition 7.2 writes `E J(R-a)` before the next sentence invokes Lemma 5.4 to establish `P(R=a)=0`. Repair by defining `J(0)=+infinity` (then using the null event), or move the no-atoms invocation before the expectation. No numerical change.

C09 was first seen only in the post-reconstruction comparison with separately executed account02/B19 r16; B01 then independently verified it directly against the pinned source. It is not claimed as an independent B01 discovery.

## Fresh dependency reconstruction

- **Theorem 1.1.** Normalize `K=s=1`; split into no pivot, diagonal pivot, or pair pivot with all diagonals small. The last pair is nonsingular and therefore definite or indefinite. No threshold-equality case is lost.
- **No pivot.** Proposition 6.4 creates an order-three crossing volume; Corollary 4.4(a) turns it into an integrable characteristic-function envelope. Literal closure inherits only C02 through Lemma 4.3.
- **Diagonal pivot.** The one-coordinate Schur complement retains at least four threshold directions; Proposition 7.2 uses only three. Its literal chain inherits C02, C01/C03 through the pair-half inputs, and C09's notation order.
- **Definite pair.** Lemma 5.2 plus conditioning pays it; only the local chart repair C01 is needed.
- **Indefinite pair.** The pair Schur complement retains at least three threshold directions. Lemma 5.4 controls the random critical value and Lemma 5.3 supplies the logarithmic density envelope; literal closure needs C02 and C03.
- **Scaling.** For `Y=KX`,
  [
  widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c,qquad Q=(s/K^2)widetilde Q,
  ]
  so `p_Q(z)=(K^2/s)p_{widetilde Q}(K^2 z/s)`.

## Adversarial checks repeated in pass 6

- Lemma 2.6's singular Schur limit preserves equality at the threshold; the `epsilon I` argument does not silently lose a direction.
- Heat-flow Brascamp–Lieb has an integrable large-time dominating function after using the frame identity; small-time passage uses Lebesgue points and Fatou.
- Product projection never rotates the random vector and then asserts independence; the rotation is only a deterministic integration coordinate change.
- The complex measure in Lemma 4.3 is absolutely continuous with modulus bounded by the projected-product density. The mollified `L^2` norms are measurable and converge; C02 is the one missing unconditional Jensen line.
- The hyperbolic positive and negative tails use separate original coordinates `i` and `i'`; the earlier same-coordinate defect is absent from this pinned source.
- Lemma 5.4 excludes atoms via the small-ball estimate; C09 is only the order in which that fact is invoked relative to the definition domain of `J`.
- Rademacher fourth moments retain exactly the ordered pair and its reversal. The bipartite dilation duplicates each crossing singular value.
- Affine terms are uniform throughout all conditional bounds.

## Literature-status check

A targeted current arXiv/web search did not locate a paper settling the exact arbitrary-independent-density, three-large-eigenvalue `L^infty` question. It did locate adjacent work on regularity of quadratic forms under substantially stronger smooth/iid assumptions. This is insufficient to certify “open”, so C07 remains UNCHECKED rather than being promoted to PASS.

## PDF/render status

The exact PDF blob/hash and 14-page map are pinned. A fresh visual screenshot/formula-by-formula comparison of the private PDF binary was not available in this execution surface. Therefore rendered-PDF equivalence remains **UNCHECKED**; provenance is not substituted for a visual audit.

Every physical TeX line 1–676 is accounted for in `coverage.jsonl`, with additional clause rows on mixed lines. Bibliographic metadata/current-priority assertions and fresh visual PDF equivalence remain UNCHECKED where recorded.

Complete B01 TeX passes on this pinned blob after this run: **6**. Fresh B01 visual-PDF passes: **0**.

Model: GPT-5.6 Sol. Configured effort/provider reasoning telemetry: UNKNOWN/not exposed. Native brain status: `WITHOUT_VERIFIED_BRAIN`.
