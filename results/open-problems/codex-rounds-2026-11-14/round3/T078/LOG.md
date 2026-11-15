# T078 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Session start: 2026-11-15 01:14 +04; exact user-message clock time unavailable.

## Orientation and initial literature check

Read the earlier REPORT.md, LOG.md and SOLVED_ELSEWHERE.md in `~/codex_op_1114/briefs/T078`. Directory listing confirms that there is no earlier PROOF.md or script to read. The earlier result is a scope check of an OpenAI solution preprint, expressly not an audit of its proof.

Read the memory index and compute governor as read-only orientation. The task-specific prohibition on writing outside this directory overrides the general memory/checklist/mesh write commands, so none were invoked. No git, subagents, or external writes. Governor: status `warn`, mode `owner_away_open`, CPU saturated. No heavy computation planned.

Commands: `pwd`, `rg --files`, `ls -la ~/codex_op_1114/briefs/T078`, `date '+%Y-%m-%d %H:%M:%S %z'`; file reads prefixed by `OMP_NUM_THREADS=1 nice -n 15`. Output: timestamp `2026-11-15 01:14:58 +0400`; nice reports `setpriority: Operation not permitted`, but the reads execute. No numerical program was run; no successful priority adjustment is claimed.

Web search queries:

- `"Spontaneous magnetization" "Heisenberg" "September" "2026"`
- `"quantum Heisenberg ferromagnet" proof 2026 OpenAI correction`

Search again locates the September 24 preprint and October companions, but no independently verified later resolution or correction. The previously readable PDF URL currently fails in the web tool. Successfully opened the primary Lean scope note and Main.lean:

- https://raw.githubusercontent.com/openai/math/main/lean/docs/271.md
- https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/Main.lean

Main.lean independently confirms the earlier parameter check: dimension d >= 3, integer ell >= 1, fixed beta >= beta0 > 0, translation-invariant zero-field KMS state, real magnetization >= ell/8. With ell=2S this is S/4, including 1/8 at S=1/2. The earlier narrow scope claim holds; proof correctness remains unverified. Its dependency carrying the ordering estimate is `Selection.field_ordered_cubes`, called on line 31 of Main.lean. Merely finding the same claim again does not establish that the problem is solved.

## Chosen extension, before doing it

Audit the source dependency supplying `Selection.field_ordered_cubes`, down to the first substantive finite-volume ordering inequality. This is the single extension: the previous report explicitly left the analytical proof and Lean dependencies unchecked. A valid source-level audit, or a precisely located missing assumption or false inequality, is more useful than repeating the scope match. No local Lean compilation or whole-proof certification will be claimed.

The comparator was opened independently. Its spin eigenvalues are k-ell/2, its Hamiltonian is minus the nearest-neighbor dot product with each edge once, and its KMS definition has the usual bounded analytic strip. The comparator's terminal `sorry` is a challenge placeholder, not evidence against the separate implementation. `SpinAveragedKMS.lean` imports `SpinAverageBoundary`; subsequent work follows these imports rather than extending the literature search.

## Source access and dependency walk

Following the PDF link from its HTML landing page succeeds, although directly opening the identical PDF URL failed. Opened the 54-page manuscript by OpenAI, dated September 24, 2026. Equation (1.1) and Theorem 1.1 confirm the earlier scope check independently of Lean. The landing page now links a comparator log dated October 26 and labels it accepted; inspect the actual log before relying on this label.

Opened imports: `SpinAveragedKMS -> SpinAverageBoundary -> SpinFieldUniform -> SpinCubeAverage -> FiniteAverage -> SpinBulk -> SpinTranslations`. The first files concern averaging and the KMS limit, rather than the ordering inequality. `Selection.lean` at the guessed flat path returns 404. GitHub directory and API listings fail through the web tool. No missing-file conclusion follows from these access failures.

Literature update stage used well under five minutes; source inspection now serves the chosen proof audit. The PDF's Section 4 is a potentially decisive intermediate check: its conditional first-moment reduction is where loop permutations are compared with a single fresh Markov walk. Check it alongside the ordering dependency.

## Comparator log and exact ordering dependency located

The actual October 26 comparator log is readable in the GitHub HTML page (raw access failed). It reports a successful implementation build and ends with `Lean default kernel accepts the solution` and `Your solution is okay!`. The earlier worker did not establish this. This is an independently read external check report, not a local reproduction, and is no substitute for checking the model's mathematical encoding.

Continued import path: `SpinTranslations -> SpinFieldDynamics -> SpinDeep -> SpinExhaustion -> SpinAverage -> CubeSelection -> PhysicalTilt`. `CubeSelection.lean`, lines 40–97, contains the sought `Selection.field_ordered_cubes`. Its substantive input is `Surface.physical_surface_bound`, called at line 47; the remaining step tilts a surface-cost magnetization tail by a fixed positive field and then sends volume to infinity. Follow that input next.

The paper's Proposition 4.3 was read in full. Its determinant/Schur-complement proof appears internally consistent at this inspection; no counterexample or complete independent verification is claimed. The audit remains focused on the dependency of the ordering estimate.

## Physical surface tail

Opened `PhysicalTilt`, `CubeSurface`, `PhysicalSurface`, `SpinField`, and `MatrixWeights`. `PhysicalSurface.physical_surface_bound` reduces to `symmetrized_surface_bound`; the other steps convert slot traces to physical-spin traces. No source-level error identified yet. The field-tilt constants also check algebraically: below-threshold probability at most 1/11, intermediate threshold 3V/16, minimum magnetization -V/2, so the tilted mean is at least 3V/16-(11V/16)/11=V/8.

Attempted a small directory-list download only: `OMP_NUM_THREADS=1 nice -n 15 /usr/bin/curl --max-time 20 --max-filesize 1500000 -fsSL 'https://api.github.com/repos/openai/math/contents/lean/OAI/MathematicalPhysics/Heisenberg' -o heisenberg_directory.json`. Output: priority change denied; curl exit 6, could not resolve host. No downloaded file or numerical computation resulted. Continue through web-opened imports.

## Audit boundary and concrete quantitative piece

Opened `SymmetrizedSurface`, `CompletionFactor`, and `CompletedSurface`. The ordering dependency reaches `completed_surface_bound`, which calls `mesh_matrix_surface` and passes a finite-mesh inequality to a continuous-time limit. These sources do not yet certify that deep estimate. The full dependency audit would be much larger than one checkable step.

Refine the chosen ordering audit to its explicit finite-volume selection step: independently prove, and sharpen, the implication from a zero-field magnetization tail to a field-induced mean. This is the single mathematical deliverable. The source currently assumes a tail of mass L above V/4 and uses `L^(-1) exp(-bV/16) <= 1/11` to obtain mean >= V/8. Its only probabilistic inputs are support in [-V/2,V/2] and that tail. Determine the optimal universal field threshold from exactly these inputs, with an extremal two-point law to try to break it. This isolates a verified portion of `field_ordered_cubes` without claiming to verify the loop estimate supplying L.

Initial derivation, to be checked independently: put z=bV/8, normalize y=8M/V in [-4,4]. The target is tilted mean y>=1, tail y>=2 of mass at least L. The signed numerator is E[(y-1) exp(z y)]. On the tail it is at least exp(2z). Off the tail its minimum occurs at y=-4 when 0<=z<=1/5, and at y=1-1/z when z>=1/5. Thus the proposed necessary-and-sufficient uniform conditions are `exp(6z) >= 5(1-L)/L` in the first regime and `z exp(z) >= (1-L)/(eL)` in the second. At z=0 the criterion is L>=5/6. Equality should be achieved by mass L at y=2 and mass 1-L at the indicated minimizing point. No computation required.

## Proof and attempts to break it

Wrote PROOF.md with the complete scalar argument, its conditional quantum application, and sharpness witnesses. Every proposed condition survives a second derivation from the explicit tilted mean of a two-point law: maximize `(1-a) exp[z(a-2)]` over the lower atom a in [-4,1). Its logarithmic derivative `z-1/(1-a)` reproduces both optimizer regimes.

Exact equality checks, independently calculated:

- z=0: L=5/6, atoms M=-V/2,V/4, ordinary mean V/8. Also follows from the minimum unweighted mean V(3L/4-1/2).
- z=1/5: both conditions give L=5/(5+exp(6/5)); both optimizers give y=-4.
- z=1: L=1/(1+e^2), atoms M=0,V/4; tilting with bV=8 makes their weights equal, hence mean V/8. This independently checks the factor e.
- L=1: all b>=0 work. V=0 is explicitly excluded; the spin application has V>0. z=0 never enters a formula dividing by z.

A separate convexity calculation gives the simpler sufficient bound `bV >= 8 log(1/L)`: if g(z)=log E exp(zY), then g'(z)>=g(z)/z>=2+log(L)/z. This checks the factor 8 without using the extremal optimization. The earlier source's sufficient condition is `bV >= 16 log(11/L)`. For L=exp(-A)/2, the new sufficient bound is `bV >= 8(A+log 2)`; it strictly improves the old one for every admissible L.

Limits: optimality is over arbitrary scalar distributions with the stated support and tail, not physical spin Gibbs distributions. The surface-order tail, finite-mesh loop estimate, imported Lean dependency chain, and infinite-volume KMS construction remain unaudited. No counterexample to the preprint was found. No numerical computation or Lean build was run.

## Final audit and handoff

Created REPORT.md with first line `VERDICT: PROVED optimal scalar field-selection criterion from a magnetization tail`, and SOLVED_ELSEWHERE.md recording the existing claim and the newly inspected comparator log. Rechecked all normalizations directly: M=(V/8)Y, bM=zY, target V/8 corresponds to Y=1, tail V/4 corresponds to Y=2, lower support -V/2 corresponds to Y=-4. In the quantum application V=ell|Lambda|=2S|Lambda|, so V/8=|Lambda|S/4. The weaker source criterion converts to bV>=16 log(11/L), not 8 log(11/L). These agree with the proof and report.

Final read-only command: `OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c 'head -n 1 REPORT.md; wc -c LOG.md PROOF.md REPORT.md SOLVED_ELSEWHERE.md; ls -1; date "+%Y-%m-%d %H:%M:%S %z"'`. Verified the verdict line and all four deliverables. Priority adjustment remains unavailable. No numerical script exists because the deliverable is a proof, with exact algebraic counterexample and equality checks. Next work is the finite-mesh surface-tail input, not another parameter/scope check.
