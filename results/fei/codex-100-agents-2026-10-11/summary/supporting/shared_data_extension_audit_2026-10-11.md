# Shared-data multiplexer extension: implementation and audit

Date: 11 October 2026.

## Implemented result

The working public manuscript now contains Section 8.2, “Multiplexers with shared data,” immediately before the unrestricted-selector reduction. Proposition 8.6 states and proves the exact collision identity for arbitrary Boolean branches on a common uniform data cube, including unbalanced branches and the empty data Fourier set. It also states the exact data and selector influence identities.

Corollary 8.7 gives FEI closure with constant `max(4,C)` under neighboring-branch orthogonality, and the more general constant `max(2/c,C)` when selector influence is at least `c` times the selector dimension. Corollary 8.8 iterates the result for regular leaves and fresh independent selectors, preserving `C_reg = 8.936474657877582... < 8.937` without any dependence on depth, fan-in or branch-data reuse. The common-data majority example has entropy 3 and influence 2.

The exact hypotheses are retained: each selector introduced at a node occurs in none of that node's branches, and every neighboring pair of branches is orthogonal under the common uniform data law. The extension imposes no branch-balance or Fourier-support-separation assumption. It proves no unrestricted selector-increment inequality.

## Independent derivation

The normalized Walsh transform of the conditional signed coefficient vector is exactly the conditional selector spectral vector. Comparing its squared law with the physical label law through two applications of the entropy chain rule proves the identity. Their alphabet sizes give the `2a` entropy budget. Orthogonality makes each selector bit disagree with probability one half, so that budget is four times selector influence. Induction is legitimate because extending a branch to the common union of data variables adds only irrelevant coordinates.

The stale companion-draft constant 13.415 was replaced by the audited internal Theorem A constant. No undefined reference to the separate bent-splice obstruction was imported. Funding, acknowledgements and declarations were not edited.

## Exact files authored

- `deliverables/fourier-entropy-threshold-functions/paper/main.tex`: new section and a short abstract adjustment.
- `deliverables/fourier-entropy-threshold-functions/README.md`: theorem description and recovery/extension note.
- `deliverables/fourier-entropy-threshold-functions/RESEARCH_STATUS.md`: exact hypotheses and audit scope.

`paper/main.pdf` was rebuilt. TeX also generated `main.aux`, `main.log` and `main.out` as build intermediates.

## Verification

Two successful `pdflatex -interaction=nonstopmode -halt-on-error main.tex` passes produced a 38-page PDF. The abstract remains 126 whitespace-delimited words. The final log has no unresolved citations or references, no rerun request, and no overfull or underfull boxes. Its only actual warning is a nonfatal pdfTeX font-expansion warning at the first bibliography monospace-font use.

The title/abstract page and pages 32–34 containing the new section were rendered with Poppler and visually inspected. They have legible formula spacing and equation numbers, clean margins, and no clipping or overlap. Final whole-document QA and release packaging remain with the root agent.

The exact source SHA-256 at this audit is:

`5cff9d1b91c92883a6d35ec7674ff5953365cadc85299747e4047d9deb150dac`

All four authored/rebuilt deliverable hashes, byte sizes and validation metadata are recorded in `shared_data_extension_source_hashes.json` beside this note. A subsequent source change requires a fresh hash and final compile.

