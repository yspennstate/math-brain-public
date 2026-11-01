All logarithms are in bits. The proof is in POINT_SURGERY.tex; the finite verifier is code/check_surgery.py. Neither floating approximations nor finite exhaustion is used to infer the all-dimensional theorem.

For a point flip, every normalized coefficient ratio is an even integer. Thus the physical selector mismatch mass is exactly the spectral minority mass, including packets created from zero seed coefficients. For two adjacent flips this equality can fail: on the active half-cube ratios are only integers. For example the one-bit constant table, flipped at both vertices, gives opposite constant children: physical disagreement is 1 but the conditional selector entropy and minority mass are zero. This endpoint is included in the exhaustive domain.

The logarithmic bill is exactly J=mu[log2(1/mu)-D2(E||q)] and the remaining binary-entropy term is in [0,mu/ln2]. This KL identity is an existing source interface, specialized here to signed actual point and adjacent surgery. For a point E is uniform on every Fourier label; for adjacent points E is uniform on one half-cube determined by their original relative sign. The adjacency interaction is 2 delta^2 epsilon (-1)^(j in S), and the influence correction to adding independent original-table flips is -4 delta f(v)f(v^j) in coordinate j.

The stage's tensor result is quantitative: for any fixed m-bit Boolean seed, let rho be its Fourier support fraction and lambda the uniform-on-support average log2 absolute integer Walsh sum. Then

|L_t/delta_t - 2(1-rho^t) - rho^t(2t lambda + log2 e)| <= 12(rho/2)^t.

This is uniform for all t>=1 and every flipped tensor vertex. The seed's sign distribution affects the exact answer; the proved error removes that dependence only within its explicit bound. Full support gives a growing selector cost; positive zero fraction gives limit 2. The latter is an assertion about powers of a fixed seed, not arbitrary dimension-dependent seeds. Bent character padding separately has a bound uniform in both parameters, recorded in the TeX proof.

Certified logs use 50 terms of ln(y)=2 sum_(j=0)^49 z^(2j+1)/(2j+1), after exact range reduction 1<=y<2, z=(y-1)/(y+1). The positive omitted remainder is at most 2 z^101/[101(1-z^2)]. Powers of two are added with signed interval endpoints. Division by the independently enclosed positive ln2 uses all four endpoint quotients, so negative numerators are handled correctly. All interval endpoints are Fraction rationals and are saved verbatim in out/EXACT_CHECK.json. Decimal displays are not certificates.

Frozen domain: all 276 truth tables for n=1,2,3; all 2,120 point and 3,140 adjacent surgeries; 96 tensor fixtures; 63 bent fixtures. No symmetry reduction, randomness, dimension escalation, or heavy job. Initial verification: 563,961 assertions, 4.116306 seconds of script runtime. The re-execution after adding exact endpoint persistence supplies the final authoritative runtime in out/EXACT_CHECK.json.

Independent reconstruction requested from A087 and A094 through these saved artifacts. Source receipts and source-inspection limitations are recorded in out/SOURCE_RECEIPTS.json. No independent acceptance or mirror receipt is claimed.
