# Coverage fallback — fleet03/B05 pass 1

Exact source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`, `short/short.tex` blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`; PDF SHA-256 `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`.

The required JSONL delivery was attempted twice and blocked by the connector safety layer before execution. This compact ledger preserves the line/clause coverage; full derivations are in sibling `report.md`.

| Source lines | PDF | Clause | Status | Check |
|---|---:|---|---|---|
|177–181|4|Theorem 3.1 statement/display|PASS|Frame trace, dimensions and scaling checked.|
|182–183|4|format|NOT_MATHEMATICAL|accounted|
|184–193|4|heat setup/PDE|PASS|Direct differentiation; contraction from WW^T=I.|
|194|4|blank|NOT_MATHEMATICAL|accounted|
|195|4|differentiate/integrate|PASS|Gaussian majorants and derivative bounds checked.|
|196|4|blank|NOT_MATHEMATICAL|accounted|
|197–201|4|large-time limit|PASS|Scaling, frame exponent and Gaussian integral checked.|
|202|4|blank|NOT_MATHEMATICAL|accounted|
|203|4|small-time limit|PASS|Lebesgue-point preimages, Fatou direction, monotonicity checked.|
|204|4|blank|NOT_MATHEMATICAL|accounted|
|205|4|general h_i|PASS|Monotone truncation and zero-factor case checked.|
|206–207|4|format|NOT_MATHEMATICAL|accounted|
|208–215|5|Lemma 3.2 statement|PASS|Original-coordinate scope, dimensions, scalar case checked.|
|216|5|blank|NOT_MATHEMATICAL|accounted|
|217–221|5|orthogonal fiber density|PASS|Unit-Jacobian marginalization; no rotated independence.|
|222|5|beta frame / BL substitution|PASS|beta range/sum/frame and h_i integral checked.|
|223–226|5|entropy bound|PASS|beta log(1/beta)<=1-beta; zero convention; d/2 sum.|
|227|5|blank|NOT_MATHEMATICAL|accounted|
|228|5|SVD transfer|PASS|det Sigma=sqrt(det(BB^T)); Jacobian checked.|
|229–230|5|format|NOT_MATHEMATICAL|accounted|
|231–237|5|Lemma 3.3 statement|PASS|L2 scope, difference density, power claim checked.|
|238|5|blank|NOT_MATHEMATICAL|accounted|
|239–240a|5|difference density|PASS|Convolution cap <=1.|
|240b|5|floor exponent|PASS|m>=p/4 and |fhat|^p<=|fhat|^(2m).|
|240c|5|char function / L1|PASS|Independent-copy characteristic function and Plancherel checked.|
|240d|5|inversion at zero|PASS|Normalization and continuity checked.|
|240e|5|projection application|PASS|Coefficient norm sqrt(2m); reflection harmless.|
|240f|5|version upgrade|PASS|Continuous version inherits a.e. ceiling everywhere.|
|240g|5|constant|PASS|Exact final inequality recomputed.|
|241|5|format|NOT_MATHEMATICAL|accounted|

Every physical source line 177–241 is accounted for. No mathematical GAP/FALSE was found in this range.

Unchecked in pass 1: lines 1–176 and 242–676. First numerically unchecked line: 1. Next forward cursor: 242.

PDF/source rendering: exact PDF blob, byte count, 14 page objects, and named destination mapping were checked. Glyph-by-glyph visual rendering is UNCHECKED because the private PDF could not be opened in the screenshot browser.
