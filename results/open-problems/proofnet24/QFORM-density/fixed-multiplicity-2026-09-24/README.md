# Fixed-multiplicity density: complete self-contained manuscript and audit

## Current owner request: full delivery and real audit work

Read [DELIVERY_STATUS.md](DELIVERY_STATUS.md) on every actual invocation along with the fresh current objective in yspennstate/math-research-brain at scheduled_tasks/CURRENT_OBJECTIVE.md. The owner has renewed the instruction: audit this FULL manuscript, every definition, source line, equation, lemma and proof, then lower the multiplicity as far as rigorously possible. Acknowledge only your own real run and publish substantive mathematics. Keep configured assignments, actual outputs and mathematical validation separate.

## Current candidate

For independent real coordinates with densities at most K, arbitrary real symmetric A with s_17(A)>=s>0, and arbitrary affine b,c, the manuscript gives the candidate bound ||p_(X^T A X+b^T X+c)||_infinity <=10000 K^2/s. The earlier 33-eigenvalue statement is a corollary. Seventeen is not claimed optimal. The full three-eigenvalue conjecture is not claimed solved.

Status: complete written argument and self-audit; independent worker reviews are arriving. The release gate remains under review. A worker PASS is not formal verification or journal peer review. Preserve the pinned baseline and reconcile findings before declaring a new release validated.

## Complete mathematical source and support files

- [manuscript.tex](manuscript.tex): the entire 790-line LaTeX paper. All definitions and specialized lemmas are proved inside this one file. No dependence on or citation to the longer manuscript.
- [AUDIT.md](AUDIT.md): the initial authoring-agent self-report, retained as historical evidence rather than a new verification claim.
- [proof_map.csv](proof_map.csv): exact statement and proof source-line ranges, including the main proof.
- [verify.py](verify.py) and [checks.json](checks.json): newly supplied reproducible finite checks and their actually executed results. This is a new scoped suite, not a reproduction of the different counts historically reported in AUDIT.md.
- [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json): verified source/PDF hashes, environment, delivery state and limitations.
- [DELIVERY_STATUS.md](DELIVERY_STATUS.md): native assignment verification, source-pinned audit-submission snapshot, and renewed work instructions.

Initial source commit: 7c0d6e60946b19423e6400a12d34b473cf0591e2.
Source SHA-256: 9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69.
Git source blob: 183ccd294763214e6a707e8d4749ff9a8cf7006d.

The complete source was matched byte-for-byte to the repository and freshly compiled to a 16-page PDF. The compiled PDF is supplied as a conversation download. This GitHub root contains the full reproducible LaTeX paper, not the compiled binary PDF; do not claim a binary upload without an actual receipt.

## Build and checks

```sh
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape manuscript.tex
python verify.py --output checks.json
```

No external figure, bibliography file, or theorem file is required. The new checker uses Python, numpy and sympy with a fixed seed and no network or remote model calls. Its finite exact and numerical tests do not replace the analytic proof.

## Key improvement to audit

For a sampled disjoint seed of order r, retain the possibly nonsymmetric interpolation P=A[:,T] A[S,T]^{-1} A[S,:]. In A=D+R+E, rank(R)<=3r globally but rank(R[L,L])<=r on the seed complement, and D vanishes on the seed. Therefore 4r+1 large singular values force r+1 large diagonal entries in L, contradicting that restricted rank by diagonal dominance. Orders three and five give nine and seventeen directions. R and E are algebraic auxiliaries, not replacement quadratic forms or independent spectral components.

## Reports and safeguards

Pin the actual source hash; report PASS/GAP/FALSE/UNCHECKED with labels, source ranges, reasoning and downstream consequences. Publish fatal defects promptly, retain unreviewed portions as UNCHECKED, and preserve the original quantifiers in every proposed lower-threshold theorem. Save immutable reviews under audits/<account>/<slot>/<run-id>/ and improvements under improvements/<account>/<slot>/<run-id>/. Two genuinely separate full reviews are required before independent-validation status, and conflicting findings must be reconciled.

Preserve existing hourly tasks, states, quiet delivery, account boundaries, peer artifacts and later owner/platform stops. No invented peer acknowledgments, speculative restarts, email/push notifications, new tasks, cross-account native changes, paid calls, public releases or remote workflows.
