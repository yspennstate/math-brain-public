# Audit 5: reproducibility, declarations, and document delivery

**Outcome: computational reproduction and manuscript preflight passed.**

## Reproduction

The two earlier exact checkers were copied without modification from their verified repository blobs. The bundled loader checks the predecessor script's SHA-256 before executing it. The uniform-window output reproduced the saved prior output byte-for-byte. A second run of the new stress checker reproduced its output byte-for-byte as well. Python was run without optimization, so its assertion checks were active.

The explicit finite law used for the window illustration is fixed: below mass 120 its positive support is $\{2,3,5,17\}$ with weights $2^{j^2}$ and $w_0=1$, and factorial support points from $5!$ onward extend it to zero radius. All 97 pairs with $20\le m\le22$ and $1/2\le m/n\le2$ are covered. The sharp upper bound is at most $2^{-189}$; the actual worst probability and both insertion bounds agree with the manuscript's rounded table. Span-three checks reproduce the relevant coefficients exactly.

No finite scan is used as a proof of zero radius, the existence of infinitely many favorable records, or an asymptotic limit. The code documentation, manuscript declaration, and review reports all retain this distinction.

## Manuscript and attribution

The final manuscript contains the author's name, Einstein Institute of Mathematics / Hebrew University affiliation, verified correspondence email, standard funding acknowledgement, competing-interest disclosure, and an AI-use declaration adapted to what actually occurred. It does not copy the previous paper's claims about Claude reviewers, Lean formalization, or human approval. No person is thanked for a contribution or discussion that was not established.

The five review passes are explicitly described as work by the same assistant. They are not five independent votes, and no source-resolution registry was promoted on their basis. The grants and competing-interest text match the author's recent standard declaration; independent confirmation of grant applicability was not performed.

## Build and rendering

The article was compiled twice with pdfLaTeX. Its metadata identifies the title and Yitzchak Shmalo. Preflight found 53 unique labels, 52 reference uses, three bibliographic keys, no undefined references, no LaTeX warnings, no overfull boxes, and no text blocks outside the page bounds. It is 11 pages in A4 format. All pages were rendered to images for layout review, with additional full-size inspection of the title page, a proof-heavy page, and the declarations/reference page.

An initial text-extraction assertion looked for mixed-case author text, while the AMS class renders the title author in small capitals. The assertion was made case-insensitive and rerun; the typeset author's name and PDF metadata were already correct. This was a test-harness issue, not a mathematical or author-name correction.

## Package boundary and remaining review

The package includes the paper PDF, root LaTeX source, three standard-library Python checkers, both saved result files, the five reports, and build instructions. Intermediate TeX build files and rendered page images are excluded from the delivered archive. Repository delivery contains the textual source, reports, and runnable checks; the compiled PDFs are also delivered directly and by email.

No unresolved mathematical gap was identified in these five passes. That conclusion remains a self-review assessment. Independent expert review, an exhaustive prior-art assessment, author approval of the final declarations, and any journal refereeing are separate future steps. The manuscript is therefore delivered as a complete research draft, not as an independently certified resolution.
