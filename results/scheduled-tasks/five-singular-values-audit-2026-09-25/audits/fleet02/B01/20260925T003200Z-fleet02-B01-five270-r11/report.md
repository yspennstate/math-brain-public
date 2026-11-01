# fleet02/B01 audit pass 1 — exact 14-page source

Run: 20260925T003200Z-fleet02-B01-five270-r11
Objective: QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925
Source commit: ec211ba2d77a4a9850168c6af1574ea651feaa7c
short.tex blob: c4f2a997cf336ee974e15409b5bccdd8cca039d8
short.pdf blob: 8be3aae36ecad7a9dc9b7c95978aad09499f32d0
short.pdf SHA-256 (owner manifest pin): 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423

Independent source read: short.tex lines 1–675 in full. Rendered-PDF visual equivalence was not independently inspected in this run because the authenticated repository connector exposed the source but not a screenshot-capable private PDF object.

Verdict: no theorem-level FALSE statement found. Theorem 1.1 and the three-eigenvalue half-moment result close after local zero-loss repairs. Literal source contains presentation/proof-closure GAPs:
- line 41: abstract omits the no-pivot/small-entry hypothesis from the random-sign conversion; A=I_5 is a counterexample to the unqualified wording.
- line 65: “has a ... singularity” is too strong; definite pair is bounded. Replace by “admits ... upper envelope”.
- lines 319–322: insert |E F|^2 <= E|F|^2 before averaging over X_{I'}.
- line 412: the elliptic polar map on (0,infinity)x[0,2pi) is not literally a global diffeomorphism because of the angular seam; remove a null ray/use the standard a.e. polar change of variables.
- lines 415–442: after treating z>v and z<v, explicitly note {q=v} is a union of two affine lines and hence has probability zero under a joint density.
- line 148: “Both follow” is editorial wording for three assertions.
- line 62 current-open-status claim is UNCHECKED by a complete primary-source literature search.

The exact short source already repairs the negative hyperbolic tail correctly: line 431 chooses separate original coordinates i and i' for u and u'.

Dependency reconstruction PASS highlights: Fourier normalization/half-moment; conditioning domination; singular-value perturbation/compression; Schur loss k; Gram/Cauchy–Binet; heat-flow Brascamp–Lieb; product projection; Fourier power; full hub/mollified-L2/entropy crossing-volume decay (after the Jensen insertion); square/definite/hyperbolic/pair kernels (after local repairs); concentration/log moment; random-sign second moment and Proposition 6.4; all no-pivot/pivot branches; final K^2/s scaling.

Numerical checks independently recomputed from the proof include C3=14.8183376628, C2=12.0950725708, gamma3=0.0900485514653, C3/gamma3=164.559422908, C2/sqrt(gamma2)=24.8257545631, sqrt(12)*77=266.735824366, and the indefinite branch 266.951346330<269. The pinned constants log also reports all 41 checks PASS.

Formal evidence: the pinned run_five3.log ends rc=0 and #print axioms reports only propext, Classical.choice, Quot.sound for the Section-6 formal theorems. This run did not execute Lean, so fresh compilation is UNCHECKED and formal logs are corroboration only.

First remaining obligations: rendered-PDF/source visual comparison; bibliographic/open-status verification; then a second pass in a different reconstruction order.