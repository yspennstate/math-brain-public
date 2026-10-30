# B19 r15 issue ledger

Exact source: math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c; short.tex blob c4f2a997cf336ee974e15409b5bccdd8cca039d8; short.pdf blob 8be3aae36ecad7a9dc9b7c95978aad09499f32d0, SHA-256 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423.

- **C04 — L41 / PDF p1 — FALSE wording.** Abstract omits the no-pivot condition on the random-sign conversion. Counterexample: A=I_5. Body Proposition 6.4 is correctly qualified.
- **C07 — L62 / PDF p1 — UNCHECKED.** Present-day literature-status claim only; not a proof dependency.
- **C05 — L65 / PDF p1 — FALSE wording.** Replace actual-singularity language by square-root/logarithmic upper-envelope language.
- **B19-R15-L148 — L148 / PDF p3 — GAP (new to this B19 pass).** The approximation-number formula is true for padded indices, but the printed converse invokes “the first j right singular vectors” even for j beyond the column dimension. Minimal repair: when j>min(rows,cols), s_j(T)=0 and B=T has rank<j; restrict the printed kernel/SVD proof to in-range j. Downstream uses are in range; no constants change. C06 (“Both” for three assertions) remains editorial only.
- **L222 / PDF p5 — PASS.** Prior B19 cardinality objection remains retracted: “factors ... are at most one” bounds factor values, not the number of zero-beta rows.
- **C02 — L319–321 / PDF p7 — GAP.** Insert |E F|^2 <= E|F|^2 before averaging. Zero loss.
- **B19-R15-L398 — L398 / PDF p9 — GAP (new to this B19 pass).** Density display is undefined at z=v. State it a.e./for z!=v and set p_T(v)=0; P(Y=m)=0. No downstream change.
- **C01 — L412 / PDF p9 — FALSE presentation.** Remove one null ray/use an a.e. elliptic polar chart.
- **C03 — L441 / PDF p10 — GAP.** State the critical indefinite level is two affine lines and hence null under a joint density.
- **External citations/bibliography — UNCHECKED as metadata**, never used as proof premises.

All mathematical repairs above are local and constant-neutral. No fatal theorem obstruction was found in either full pass.
