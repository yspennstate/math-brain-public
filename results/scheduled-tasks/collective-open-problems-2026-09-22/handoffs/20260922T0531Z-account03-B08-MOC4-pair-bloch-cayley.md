# MOC4 source-bound handoff — account03/B08

Run: `20260922T051819Z-account03-B08-MOC4-r11`  
Outcome: `AUXILIARY_ONLY`; parent MOC4 remains **OPEN / not proved / not disproved**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific report: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/account03/B08/20260922T051819Z-account03-B08-MOC4-r11/REPORT.md`, report blob `f39236fa1e63c1af4ebeb89a1f243a49a9aa44a6`; report creation commit `138e4ca0d26691497d4a98ab801e8a08e7feac21`. Exact verifier commit `181d3fbb6cc581f568ced9dd86ac07246017f45f`; captured output commit `5a7bcb3b9580e4669ac21997bb204f9a7ef92512`.

Assigned partner consumed: account04/B09 `MOC4-STANDARD-CHANNEL-CEILING-v1`, source report blob `faaf77b4fcebb8fed6a6c9763251acc1042105ac`. Named other-account result also consumed: account01/B09 phase-family theorem, report blob `9b496cd2cb18df7a577ab0997de1117a8c144c98`, which positively lifts the flat complex-Hadamard phase fiber.

New theorem `MOC4-PAIR-BLOCH-ENVELOPE-v1`: for any true unitary `U`, any row pair `r<s`, and arbitrary complex spectra (including repeated/singular cases), the determinant over the full embedded `SU(2)` row-pair orbit is affine in the Bloch vector `n in S^2`: `D(n)=alpha+beta_x n_x+beta_y n_y+beta_z n_z`. Hence any real support functional is `A0+c dot n`, with exact pair-orbit maximum `A0+||c||`. Every genuine global support maximizer must satisfy `c_x=c_y=0`, `c_z>=0` for all six row pairs. The proof uses only determinant multilinearity and `det(n dot sigma)=-1`; no inverse or genericity assumption is used.

Exact true-unitary adversary: spectra `a=(18-17i,-20+2i,15-22i,-21+2i)`, `b=(-19+4i,25-5i,18-i,-18+i)`; rational skew-Hermitian Cayley seed is recorded in the report/verifier, and `U=(I+K)^-1(I-K)` is checked unitary exactly. All 16 entries are nonzero and `min |U_ij|^2 = 4297768791625000/431850208768934029 > 99/10000`.

For the one common direction `L(z)=-5782 Re z+19099 Im z`, exact enumeration of all 24 target vertices gives `M=-61633500`, `m=-59822291610`, uniquely maximizing at `1234`. The exact true-unitary gap is

`M-L(D)=2774999449515476249040000/431850208768934029 > 0`,

with normalized gap

`92499981650515874968000/860255089365746349873794173 ~= 1.07526224249e-4`.

So the candidate is only about **0.01075% of the full support width inside** the exposed target line, but is not a counterexample. An exact three-vertex Caratheodory certificate places `D` in `conv(v_1234,v_1243,v_1342)`.

Pair `(2,3)` is rigorously improvable in the same support direction: exact squaring proves its genuine `SU(2)` pair-orbit gain exceeds `(M-m)/100000`, but the exact pair optimum still remains below `M`. This is a target-valid stationarity filter, not a negative formal coefficient.

Partner application on this endpoint datum gives `Delta=132071462`, `Kstd=29871989917`, so the standard-channel reserve is large and does not certify the instance. The candidate deliberately probes the required nonflat/pair-strict regime rather than the account01/B09 flat safe family.

Next obligation: `MOC4-PAIR-BLOCH-DESCENT-v1` — iterate the exact six pair envelopes to a pair-stationary true unitary, then either combine the six stationarity conditions with `Kstd/Delta` and subgroup roofs to prove the 24-vertex support bound, or rigorously enclose a strict common-direction violation. Do not count arbitrary bistochastic arrays or negative formal coefficients as target counterexamples.
