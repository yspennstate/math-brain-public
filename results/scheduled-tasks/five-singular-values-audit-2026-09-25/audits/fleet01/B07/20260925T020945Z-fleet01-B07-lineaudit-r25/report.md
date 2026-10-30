# B07 r25 audit report

Objective: QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925
Source: yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c
TeX blob: c4f2a997cf336ee974e15409b5bccdd8cca039d8
PDF SHA256: 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423
Model: GPT-5.6 Sol; effort telemetry UNKNOWN.
Native-brain status: WITHOUT_VERIFIED_BRAIN.

Fresh controls and the full shared audit package were read. This run covered source L1-162 and L392-676; B07 r24 had independently covered L163-391. Cumulative source-clause coverage is therefore complete once. Direct B07 visual render/source comparison of the private PDF remains UNCHECKED, so strict complete source+PDF pass count is 0.

Literal-source verdict: GAP, locally repairable; no fatal theorem obstruction found. The source is not marked PASS while essential local gaps remain.

Findings:
- L41 p1 FALSE presentation (C04): abstract omits the no-pivot hypothesis on random-sign conversion. A=I5 shows the unqualified sentence false. Add "in the absence of a pivot".
- L65 p1 FALSE presentation (C05): proof establishes square-root/log upper envelopes, not necessary singularities. Repair wording.
- L148 p3 editorial C06: "Both follow" precedes three assertions; mathematics passes.
- L222 p5 FALSE proof sentence: "Factors with beta_i=0 are at most one" is false. Example n=4,d=2 with U=[e1,e2], W=[e3,e4] gives beta=(0,0,1,1). Delete "are at most one and"; all zero-beta factors may be dropped, constants unchanged.
- L319-321 p7 GAP (C02): insert Jensen/Cauchy |E F|^2 <= E|F|^2 before averaging. No constant change.
- L412 p9 FALSE chart wording (C01): the half-open polar chart is not literally a diffeomorphism. Remove a null ray/use an a.e. chart; Jacobian and bound unchanged.
- L441 p10 GAP (C03): explicitly exclude an atom at the critical value; its level set is two affine lines and null. Constants unchanged.
- L62 p1 current-open literature claim and external bibliography remain UNCHECKED; not proof dependencies.

Independent reconstruction checks: Fourier/Gamma/conditioning and Schur count L83-161 pass. One/two-coordinate kernels L395-510 pass after C01/C03. Random-sign moment and compression L515-580 pass. Final branch arithmetic L586-639 passes after C01-C03/C02: gamma3=0.0900485514653, 15/gamma3=166.576805<167; diagonal main branch 266.735824<267; indefinite-pair branch 266.951346<269. Scaling gives K^2/s exactly.

After completing B07's derivation, a separate fleet02/B19 audit was read for comparison only. It independently reports the same L222 defect and C01-C07 classifications. Its decoded pinned-PDF map was used only for page-location metadata; no peer PASS was imported.

Remaining: direct B07 rendered-PDF inspection, external literature metadata, fresh formal build, and a second B07 pass in reverse/adversarial order.
