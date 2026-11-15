# FEIB26 report

The strongest finite result is an explicit transitive Boolean function with

    4.50504996749762 < min_i E_i/Inf_i < 4.50504996749764.

It has 4,782,969 variables and is seven alternating layers of the nine-edge PM(K33) function and its output complement. All coordinates are equivalent under a wreath-product action. `interval_witness.json` encloses its value with ninety-digit outward interval arithmetic; `periodic_audit.json` independently computes it from two coefficient transforms. This exceeds the brief's 3.7137 benchmark. Already an 81-variable PM self-composition gives 4.048135961762372.

The best retained tower limit is approximately 4.50501525844266655425, for the repeated bottom-to-top period [complemented PM9, PM9]. Its seven-layer finite value is slightly higher because an empty-pair entropy term vanishes in the limit. The ordinary PM9 self-tower limit is approximately 4.474150253077977. These are construction lower bounds; no general optimum or literature novelty is claimed.

I proved the exact balanced and unbalanced composition laws for E_i, H and I, including the interference of amplitudes at empty blocks. A normalized nonempty-pair residual is monotone along a tower. It gives convergence of G for every fixed transitive base, even without convergence of the bias, and a finite-gate truncation bound. The boundedness and tail proof explicitly use the existing O'Donnell–Tan biased composition theorem. `PROOFS.md` writes the arguments and identifies those dependencies.

The numerical work covers every transitive function through seven variables up to relabeling: prime degrees through cyclic actions and the full degree-four/degree-six group catalog. Both output signs are retained for unbalanced towers. All fifty degree-eight actions were surveyed, with 21 exhausted and the rest annealed. The best small-base self-tower limit through seven variables is about 4.137065543117357. Cyclic searches on twelve through twenty variables, graph properties on four and five vertices, translation actions on eight and sixteen coordinates, bent functions and mixed towers are saved with their functions and run counts in `RESULTS.md`.

The 6.278 construction was recovered through Hod's published balanced replacement of the inconsistent DNF displayed in O'Donnell–Tan. It has H=3.924340782942887 bits and I=13/8. Its influences are unequal, so a path-aware dynamic program computes its minimum tower limit as about 3.6848626341. Constant-coordinate paths alone give the wrong minimum. The 6.5218457 helper lift also has unequal influences, 0.00390625 and 0.22265625; it is distinct from the transitive unbalanced nine-variable host.

The proof attempts establish E_1<=12.04 Inf_1 for symmetric functions using the published symmetric FEI theorem, and E_1<=(w+7.94)Inf_1 for ORs of cyclic shifts of a width-w pattern, or (wl+7.94) for a threshold of l shifts. They also give the exact size-biased deletion formula and explain the remaining gap in the Han/convolution approaches. A single absolute constant for every transitive function, the proposed equalities of suprema, and general FEI remain open. `LITERATURE.md` contains the requested neutral clauses and opened primary-source links.

Checks include 401 full small compositions, 262,144 four-variable coordinate checks, an independent reconstruction of every saved search witness, high-precision tower replays, and the separate interval certificate. The largest composition entropy discrepancy was 3.55e-15 bits. The measured verification peak was 377.84 MiB at inherited nice 10 with one math thread. The folder remains below 150 MB. Raw census scratch files were compressed and removed.

Brain recall helped recover earlier cautions; the math store was not installed. No shared state was changed. The launching session can review `LEARNINGS.md` for a durable-memory handoff.

Task: “solve the Fourier Entropy-Influence conjecture” — the author's 9 Nov 2026, 22:20 ask; worker FEIB26.
