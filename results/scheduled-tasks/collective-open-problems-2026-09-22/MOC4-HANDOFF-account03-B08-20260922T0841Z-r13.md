# MOC4 handoff — account03/B08 — r13 pair-trap no-margin

Outcome: **AUXILIARY_ONLY**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**. Execution: **WITHOUT_VERIFIED_BRAIN**.

Canonical science: `proofnet24/collective-MOC4/account03/B08/20260922T082441Z-b08-moc4-r13/REPORT.md`, blob `0536c406f1df4f544315001d36db24cad2924b8e`. Exact verifier blob `af095e9a6c763fbe131c5eab50b1713b3502619f`; captured exact output blob `54b507be050c4c26d9780d1dc188df6c18a7624e`.

Assigned OTHER-account partner actually consumed: account04/B09 `MOC4-OPEN-GAP-GENERICIZATION-v1` (`20260922T071523Z`). Its genericization result was applied by staying in simple/nonzero complex spectra rather than singular/repeated limit branches.

New result `MOC4-PAIR-TRAP-NO-MARGIN-v1`:

- spectra: `a=(23+19i,1+17i,25-26i,-35+19i)`, `b=(-21+13i,-1+23i,26-27i,32-21i)`; all spectra are simple/nonzero and all 16 sums `a_i+b_j` are nonzero;
- candidate true unitary is the permutation `p=4321`, with `v_p=-1262976+2125032i`;
- unique global support vertex is `q=3412`, with `v_q=929730+823140i`;
- exact common direction `L(z)=199025 Re(z)+335207 Im(z)` gives `L(v_q)=460961803230`, `L(v_p)=460961803224`, hence target deficit exactly `6`;
- all 24 support values are distinct; total width is `3225656411230`, so normalized deficit is exactly `3/1612828205615 ≈ 1.86008651730892e-12`;
- nevertheless `p` is a **strict maximizer on every one of its six full elementary SU(2) pair orbits**. Exact neighbor losses are `79,221,639,744`, `614,779,338,360`, `487,173,330,150`, `3,225,656,411,224`, `434,225,479,974`, and `36,360,921,450`.

Infinite exact no-margin family: primitive tie normal `n0=(216982,365451)` coexposes exactly `p,q`, with third-vertex margin `39,641,580,000`; Bezout perturbation `d=(-17957,-30244)` satisfies `d·(v_q-v_p)=6`. Thus for every `N>=1`,

`L_N(z)=(216982N-17957) Re(z)+(365451N-30244) Im(z)`

keeps `q` uniquely top and `p` strict second/pair-local with the same absolute deficit `6`, while normalized deficit tends to zero. Therefore strict pair gates alone imply no uniform normalized target slack.

Exact mixed two-root tunnel: `q=(12)(34)p`. If `x=sin^2(theta)` and `y=sin^2(phi)` for disjoint row rotations, then the determinant is the exact convex four-vertex mixture and

`L(D(x,y))-L(v_p) = -A x - B y + (A+B+6)xy`

with `A=79,221,639,744`, `B=36,360,921,450`, `A+B+6=115,582,561,200`. Along `x=y=t`, the path beats the strict pair trap only when

`t > 19263760199/19263760200 ≈ 0.9999999999480891`.

Interpretation for the lead: individual-root strictness can be enormous while a mixed finite-distance term cancels essentially all of it. Any MSQR/cross-reserve proof must retain determinant-specific mixed interactions; there is no uniform-margin shortcut from strict pair gates. This remains target-safe because the whole two-plane family is itself a convex combination of four permitted vertices.

Next B08 mechanism: `MOC4-MIXED-TUNNEL-OFF-MONOMIAL-v1` — perturb the exact tunnel to a genuinely nonmonomial rational-Cayley unitary while preserving a unique common direction and pair strictness, then perform exact all-24 separation/hull certification. No arbitrary bistochastic or negative-formal-coefficient object is called a target counterexample.
