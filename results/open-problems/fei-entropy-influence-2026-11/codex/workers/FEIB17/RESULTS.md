# FEIB17 results

The full referee pass and general-case attempts are in REFEREE.md and PROOFS.md. REPORT.md is the handoff. Logs are base 2; entropy and entropy costs are in bits, and influence is dimensionless.

| Result | Status | Receipt |
|---|---|---|
| D_i=E_i+J_i; 0<=J_i<=(2/ln 2)Inf_i, sharp among Boolean functions | PROVED | audit_results.json, exact_families.json |
| Adaptive paths and random-order integral | PROVED, checked on all n=4 functions | path_census.json, reductions.json |
| Both supremum brackets | PROVED | REFEREE.md (b) |
| G<=H^-<=G+I/ln 2 | PROVED | audit_results.json |
| Normalized edge-law identity | PROVED | audit_results.json |
| Pair soft approximation | PROVED; error constant improved to 2.831178868150198 bits per influence | witnesses.json, audit_results.json |
| Unsmoothed KL shortcuts | FALSE, including positive-part repair | singular_examples.json |
| Bent product ratio and unique largest influence | PROVED with point-dependent influence correction | exact_families.json, final_checks.json |
| Complex unimodular obstruction | PROVED | extra_checks.json, exact_families.json |
| Exact two-cell block entropy | PROVED | audit_results.json |
| Last logarithmic block bound without delta<=I_N | FALSE | reductions.json |
| Claimed steep-edge constant | FALSE | final_checks.json |
| Majority block influence proportional to k/sqrt(n) | FALSE in the stated growing-block regime | witnesses.json |
| Consecutive symmetric low levels cannot have comparable mass | FALSE | witnesses.json |
| A bounded H^- theorem on 1<=I<=9/4 implies FEI | PROVED | reductions.json; PROOFS.md 1 |
| H^-<=CI^2 for all influence values | FALSE on AND_n as I tends to zero | exact_families.json |
| Boolean normalized per-direction edge budget | PROVED; fails for complex functions | edge_budget.json, final_checks.json |
| Vertex correction c rho+k I(g)+l Var(g) | Finite LP feasible; every fixed-coefficient general version FALSE | vertex_lp.json; PROOFS.md 4 |
| General unweighted G<=CI or H^-<=CI log(I+2) | OPEN | PROOFS.md |

The bent all-zero-point values at m=2,4,6 are:

| m | least odd r for unique maximum | E_i/Inf_i | D_i/Inf_i |
|---|---:|---:|---:|
| 2 | 7 | 2.672488983973203 | 4.867668746754797 |
| 4 | 53 | 5.224357932670612 | 8.030013847484557 |
| 6 | 695 | 7.386758947438571 | 10.255970235276205 |

Exact rational influences and the failed previous r are in exact_families.json. The alternative all-one point has smaller least odd lengths 3,33,613. The erasure ratio is unchanged. This is a qualification of FLOW's unspecified point, not a claim that r=41 never works at m=4.

The nondegenerate block counterexample has delta=1, I_N=1/8, eta=7/8 and E_i=0. FLOW's last right side is -0.1263823551335972 bits. The exact two-cell expression is zero. Source: reductions.json.

The vertex LP fits c=1.5421769659005276, k=0.8421145787053088, l=0, with integrated objective 3.226406123311145. At the held-out n=256 threshold its left side is 26.81734217721384 and its right side 16.88218195148726. The general negative theorem uses the asymptotics F~sqrt(n)log(n)/8, rho~sqrt(n)/4 and I~sqrt(2/pi)sqrt(n). Source: vertex_lp.json and PROOFS.md.

The core census includes all 65,536 four-variable functions and 3,000 mixed draws at each of n=6,7,8. Its maximum entropy identity residual is 1.2989609388114332e-14 bits. Explicit pair convolution residuals are zero on all four-variable functions and the separate 128-function samples at each of n=6,7,8. The final source and receipt audit passes. Sources: audit_results.json, extra_checks.json, final_checks.json.

The best-coordinate ratio on the supplied five-variable representative file is 4.867668746754797. Tribes 2x7 gives 5.996806000051715. The reconstructed balanced record gives the self-composition lower bound 6.521845710923046... . Sources: records.json, independently record_precision.json for the last value. These are lower bounds/finite checks, not general upper bounds.

All scripts, commands, scopes and source qualifications are listed in RUNS.md. The representative-file coverage is supplied rather than independently regenerated here. Source hashes are in source_provenance.json; output hashes are in MANIFEST.json.
