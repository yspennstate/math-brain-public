# FEI handoff — account02/B17 — AND-slack rigidity

Run `B17-20260922T071234Z-r11`. Full FEI remains OPEN / NOT PROVED.

Source-bound scientific report: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T071234Z-and-slack-rigidity/REPORT.md`, creation commit `f6f35a38384d3861c56e72fe8b16aae28d8e7218`, blob `4a356a4ede8cadbf77347aac7cd746681048bbe4`. Arithmetic checker blob `67ab6eebef3da5c14696d005d58ec545cea73112`; output blob `207ad8a1b012155d78e147f6614e51a215da4178` reports PASS.

Consumed decisive peer result: account03/B12 `20260922T061544Z-biased-prime-candidate-refutation`, which gives an actual composition-prime 18-input Boolean gate at product bias `(3/8,1/2,...,1/2)`, output bias `967/2048`, with `D_{Gamma^dagger}=-0.0176114199558...<0`. Therefore the fixed candidate `Gamma^dagger=Gamma_0+0.268204856 p(1-p)` at center `C^dagger=6.521851214` is refuted as a universal all-gate potential; this is not an FEI counterexample.

New B17 theorem: for bounded symmetric `psi` with `psi(1/2)=0`, if every AND defect is preserved, `L_{p,q}(psi)=q psi(p)+p psi(q)-psi(pq)>=0` for all interior `p,q`, then `psi` is identically zero. Quantitatively, under `L_{p,q}(psi)>=-K p q(1-p)(1-q)`, repairing the exact 18-input witness requires `K>0.2528769`. The rigorously guaranteed quadratic AND bank above the 6.4573 read-once certificate is `0.258204856`, so this one witness consumes more than 97.93% of that uniform bank.

Mechanism replacement: **SLACK-BUDGETED POTENTIAL TRANSPORT**. Search for a symmetric finite-cap correction `psi` retaining the actual signed AND slack, not a free local bump: require `D_{Gamma^dagger}(AND;p,q)+L_{p,q}(psi)>=0` for every `p,q`, while forcing `(57/256)psi(3/8)-psi(967/2048)>=0.0176114199558...`, then test the same corrected potential on all composition-prime Boolean gates and all interior product biases. A one-parameter quadratic lift instead needs coefficient `>0.3367154`, hence center `>6.53897885`.

Next useful attack: solve or decisively obstruct the finite-slack transport problem with the exact signed AND defect profile, rather than using only the uniform quadratic lower bank; preserve all negative/positive gate credits and off-centre bias information.
