# account01/B05 r16

Source: yspennstate/math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa, paper.tex blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a.

B05 lens lines 218-226: PASS mathematically. Zero-beta factors are fiber-independent and bounded by one; any number may be dropped. Density representatives are fixed before fiber integration. p(y)=0 is treated before logarithms. No rotated-coordinate independence is used.

Lines 231-241: PASS mathematically. Fresh Lean artifacts now kernel-check the difference-density cap and the Fourier-power argument conditional on Lemma 3.2(a): FiveS3Diff.lean blob 1810def99633232610614122c7e591aeb69d5855 and FiveS3Fpower.lean blob 6509c16245f1994d9ba5080b2e9778ad3d6df6bd. Their stored axiom logs exit successfully and list only propext, Classical.choice, Quot.sound.

Exact formalization note: lemma33 exposes the bound as an ENNReal lower integral, while the paper displays an ordinary real Lebesgue integral. These are equivalent here after integrability, but an explicit ordinary-integral corollary was not found. A local uncompiled helper was prepared for that bridge.

Current formal bottleneck: Lemma 3.2(a). Existing Lean checks its beta/log inequality, f^(1/beta)<=f, rescaling and Jacobian, but not yet the fiber marginal density formula plus zero-beta restriction plus full Brascamp-Lieb application and resulting law domination. Theorem 3.1 also remains partial at the analytic monotonicity/limit/Fatou layer.

Rendered PDF: UNCHECKED.
Native-brain status: WITHOUT_VERIFIED_BRAIN. full_brain_connected:false.
