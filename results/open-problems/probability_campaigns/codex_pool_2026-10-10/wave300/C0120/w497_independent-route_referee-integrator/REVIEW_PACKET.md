# C0120 referee packet, 2026-10-10

## Scope and frozen evidence

The primary citation arXiv:0810.4221v2, Section 8/Theorem 8.1 and Section 12(3), is about the zero-temperature maximum M_n over n-vertex east/north paths in iid standard Gaussian vertex disorder on Z^2. Its established variance bound is Cn/log n. The intake's log Z_n in general dimension is a different object and unsupported by that citation. SOURCE_STATUS.json records the exact correction and keeps current openness UNKNOWN. ATTEMPT.md was saved before reading peer proofs.

Frozen peer snapshots under peer_snapshots/ have SHA256 values:

- w495_ATTEMPT.md: 0EE38C442D3422CAF4C87DAB2C0A2669240CB52D34F7C9322288217199DF1FF1
- w496_GAUSSIAN_FAN_OBSTRUCTION.md: 27BB548C037BEB3DD993DBE0C7FB3DC430CC9CA07685CCF665DD4A32D4BE54EF
- w496_INDEPENDENT_DERIVATION.md: 45A6BC15E758FCD29A5899610E6296A11C3D03998CA6B708475A79E620DFE432

## Verdict

AUDIT_VERDICTS.jsonl gives one reproducible KEEP for each w495 L0/S1/L1-L5 and w496 C001-C006. KEEP means the stated lemma or source correction survives this mathematical check within its recorded scope. No KEEP is a proof of the parent C0120 target. Response-side served-model identity and different-model final-review gate remain unverified, so this packet does not authorize store promotion as a solved theorem.

The hardest load-bearing step in w495 is the variance comparison for a bounded-degree binary tree plus independent private chains. I rederived the Gaussian maximum lower bound using two quantile events and Mills inequalities, checked the OU upper integral including the sum over m indicator gradients, integrated the correlated-prefix union bound, and used centered L2 triangle. Their B=O(r^2) is eventually smaller than c2^r/(4r log 2), so Var(M)=Theta(L/log L) on that changing graph. This does not transfer to the source lattice, whose width at layer r is r+1 rather than 2^r.

The hardest load-bearing step in w496's fan obstruction is the vanishing-noise overlap bound. For alpha=(3+rho)/4 and u=16loglog n/log n, (1-alpha)log n=(4+o(1))loglog n and [1-2alpha/(1+rho)]log n=(-4+o(1))loglog n. Mills' lower bound then makes nQ(sqrt(2alpha log n))=(log n)^(7/2+o(1)), so both union-bound terms vanish. Its root degree grows with n. I also checked the Hermite spectral tail and the layer-average independence by direct covariance and joint Gaussianity.

## Parent gap and route

No packet proves a quantitative estimate on the actual fixed east/north lattice. The common missing claim is a polynomial bound on its low-degree Gaussian chaos mass, or an equivalent polynomial noise-overlap estimate with exact conditioning, which would turn the n/log n gain into n^(1-epsilon). My independent dyadic path-switching route needs a slab-resampling bound after maximizing over boundary points; this is unproved. Current openness remains UNKNOWN pending a targeted present-day literature and owner solved/retired check.

NEXT: Complete the targeted present-day status check, send these scoped verdicts to w495/w496, and prepare a draft source-correction/obstruction bundle with no solved label.
