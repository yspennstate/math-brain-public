VERDICT: PROVED a linear-in-group-size Lipschitz obstruction for the fixed one-ReLU-per-group interpolant

For uniform sphere data, the equal-label grouping construction with threshold 1/2 has sphere Lipschitz constant at least m/4 with high probability, where m is the maximum group size. The theorem assumes m>=8, sufficiently many full groups, and explicit dimension bounds; it includes the ordinary grouping of independent binary labels with remainder groups. With width K approximately n/m, this is order n/K, exceeding the desired square-root scale by an unbounded factor as m grows. Thus a sharper analysis of this fixed construction cannot establish the full conjecture in the covered regime.

`PROOF.md` contains the complete proof and explicit failure probability. It also proves the exact orthogonal-data unit-ball constant `2 sqrt(m min(K,4m-1))`, with sphere bounds between `sqrt(3)m` and `4m` when K>=2m.

Run from this folder:

```powershell
$env:OMP_NUM_THREADS='1'; $env:OPENBLAS_NUM_THREADS='1'; $env:MKL_NUM_THREADS='1'; $env:PYTHONDONTWRITEBYTECODE='1'; [System.Diagnostics.Process]::GetCurrentProcess().PriorityClass='BelowNormal'; python -B verify.py
```

Validation passed: exact rational constant checks, 35 orthogonal cases, 17,667 label-count cases, three random instances, and direct network chord secants agreeing with tangent derivatives. Maximum interpolation error was 4.88e-15. Runtime was 7.926 seconds; peak working set 344,895,488 bytes. Reproducible seeds and numerical data are in `verification_data.json`; exact output and the adversarial audit are in `LOG.md`.

The attempted route that fails is improving the square-root scaling merely by tightening the original grouping construction's gradient estimate: there are actual high-gradient sphere points. This does not exclude other biases, position-dependent grouping, or other interpolants. No training was performed; gradient descent from standard initialization is unresolved here. Novelty of this obstruction has not been established.

Resource exception: an optional full-store memory recall exceeded the 1 GB cap (observed 1,954,091,008 bytes). A command was issued to stop that session-owned process; it supplied no mathematical result. This was a resource-control error. The proof's verification run stayed below 345 MB. Details and termination outcome are in `LOG.md`.

`SOLVED_ELSEWHERE.md` records the bounded literature check, including a 2026 arbitrary-weight lower-bound claim. The inspected sources do not settle the whole problem. The original upper conjecture permits a choice of activation and uses sphere Lipschitz constants, so the question's ReLU-specific/global formulation needs care.

Next worker: seek an interpolation construction that changes the activation geometry, rather than re-estimating the fixed group-cap sum. Any proposed improvement should control tangential gradients at the common-sign multi-group witnesses exhibited here. A separate, precisely specified initialization and training theorem is needed for the gradient-descent question.

Task: Open problem T343 — two-layer robustness achievability and gradient descent; one checkable piece.
