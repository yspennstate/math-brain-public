# account02/B13 r19 audit findings

Source: math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c, short.tex blob c4f2a997cf336ee974e15409b5bccdd8cca039d8, short.pdf blob 8be3aae36ecad7a9dc9b7c95978aad09499f32d0, PDF SHA-256 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423.

Two complete source reconstructions were performed. No theorem-level counterexample was found after the standing local repairs.

New local r19 issue: TeX L628 / PDF p13 is a literal domain/measurability gap. The conditional hyperbolic envelope contains log_+(16 sqrt(D)/|z-v|), while log_+ was defined only for positive finite input, so the dominating profile is not defined on the random critical graph z=v when Lemma 2.4 is invoked. Repair: define the logarithmic envelope to be +infinity at zero before conditioning. Lemma 5.4 makes v atomless for every fixed z; the repair is measurable and has zero constant loss. The <269 indefinite-pair branch is unchanged.

B13 pair checks re-pass: definite chart Jacobian 1/(2 sqrt(det B)); indefinite branch Jacobian 1/(2 sqrt(|det B|)); positive and negative hyperbolic tails require separately chosen original physical coordinates; critical level is two affine lines and planar-null.

PDF byte/blob/hash/page-structure identity was verified. Pixel/formula screenshot comparison remains UNCHECKED because the private PDF was unavailable to the mandated web PDF renderer.

Status: repaired proof chain continues to support the 270 K^2/s density bound under s5(A)>=s and the 77 K/sqrt(s) negative-half-moment bound under s3(A)>=s. AUDIT ONLY; no lower-threshold research.
