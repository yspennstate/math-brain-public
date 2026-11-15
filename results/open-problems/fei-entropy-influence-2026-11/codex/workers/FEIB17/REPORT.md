# FEIB17 report

The referee pass is complete. The core erasure identities are correct, but FLOW needs corrections to its unsmoothed KL claims, steep-edge constant, block-witness simplification and several adjoining quantitative statements. Part 2 produced general reductions and obstruction theorems; it did not prove FEI.

## Requested referee verdicts

| Item | Verdict |
|---|---|
| (a) D_i=E_i+JS_i; JS constant | PROVED. The constant 2/ln 2 is sharp even among real Boolean functions. |
| (b) Paths and both supremum brackets | PROVED, including adaptive orders, the random-order integral and the stated additive constants. |
| (c) G<=H^-<=G+I/ln 2 | PROVED. |
| (d) Edge-law identity | PROVED exactly. Q must be the normalized unoriented toggle-edge law. |
| (e) Pair form | The soft approximation with error (log 3+1/ln 2)delta is PROVED; the raw KL identification is FALSE. A mixture reference repairs it. The approximation constant improves to log((3+sqrt(5))/2)+1/ln 2. |
| (f) Bent-majority example | PROVED. Exact ratios and unique-maximum influence are computed; majority block size depends on the replaced point. |
| (g) Complex unimodular example | PROVED. It violates FEI and the new Boolean weighted edge budget. Both tribes marginal proxies have the claimed width loss. |
| (h) Block witness | Exact two-cell entropy and first bound PROVED. The last bound is FALSE without a hypothesis; the corrected universal bound uses I_N+eta. |

REFEREE.md contains the full arguments and also covers the remaining displayed statements in sections 7, 9 and 10.

The main corrections are these. Raw spectral KL can be infinite while E_i/Inf_i is arbitrarily large; taking a positive part does not fix it. The last block-witness right side is negative in a fully relevant Boolean example. At equal edge masses the proposed steep-edge constant is too small. Majority block influence scales as sqrt(|N|/n), rather than |N|/sqrt(n). Comparable consecutive low-level weights can occur in symmetric Boolean spectra. The small-influence/no-cheap-coordinate conclusion requires a suitable extremizing sequence, not an arbitrary hypothetical FEI counterexample sequence.

For the bent family at the all-zero replaced point, the exact outer block influence is 1/2+2^-m. The minimal odd majority lengths for m=2,4,6 are respectively 7,53,695; E_i/Inf_i is respectively 2.672488983973203, 5.224357932670612, 7.386758947438571 bits per unit influence. At the all-one point the outer influence is 1/2-2^-m and the corresponding lengths are 3,33,613. Thus the suggested m=4, r=41 works at some points but is not point independent. Source: exact_families.json; the composed 15-variable example is independently transformed in final_checks.json.

## Part 2 verdicts

1. General logarithmic/quadratic bound: OPEN. PROVED that a uniform H^- bound only on 1<=I<=9/4 already implies FEI, via a switch to an independent dictator. Consequently the quadratic target for I>=1 remains equivalent to FEI in strength. The unqualified CI^2 target is FALSE at small influence: AND_n has H^-/I tending to 2 while I tends to zero.

2. Simultaneous real Boolean relations: the full unweighted G bound is OPEN. PROVED a weighted edge budget: one chosen edge per direction, or weights totaling at most one per direction, costs at most [2/(e ln 2)]I. This fails for the complex example. Singleton upper endpoints therefore cannot carry an unbounded erasure ratio. Explicit convolutions pass the stated census and samples.

3. Vertex correction: CHECKED the candidate c rho+k I(g)+l Var(g) by an LP on the supplied five-variable representatives. Its fitted integrated constant is 3.226406123311145. PROVED that every fixed-coefficient inequality in that family fails in general, using biased thresholds displaced n^(1/4) from the median. A valid replacement correction remains OPEN.

4. Counterexample structure: PROVED necessary steep-edge tail, edge multiplicity, higher-level, hypercontractive and signed-convolution constraints. No Boolean FEI counterexample was found, and I do not claim the conjecture is false.

Full proofs and precise scopes are in PROOFS.md. LEARNINGS.md holds the durable findings for later publication by the launching session.

## Checks and receipts

The independent checker covers all 65,536 four-variable functions and 3,000 mixed draws at each of n=6,7,8. All corrected identities and inequalities pass. The largest core entropy identity residual is 1.2989609388114332e-14 bits. Two adaptive policies and the exact random-order integral also pass on every four-variable function. The explicit Boolean convolution residuals are zero. Sources: audit_results.json, path_census.json, extra_checks.json; commands are listed in RUNS.md.

The five-variable LP and best-coordinate scan use the read-only file of 616,126 supplied NPN representatives. I checked every listed representative and coordinate subset for the candidate, but did not independently regenerate coverage of the representative file. Its hash is recorded in vertex_lp.json and source_provenance.json. The LP is rejected by independent larger threshold holdouts and by the asymptotic proof.

The stated record lower bound is reproduced: the balanced perfect-matching-plus-coins construction has H/(I-1)=6.521845710923046... . records.json obtains it by the ordinary transform; record_precision.json independently uses an integer transform and 80-digit Decimal logarithms. This verifies the numerical lower bound, not an upper bound on FEI.

final_checks.json says PASS. MANIFEST.json identifies the output receipts. Instrumented runs inherited nice 10 and reached a measured peak of 314,736,640 bytes resident memory, about 0.293 GiB, below the process cap. Numerical libraries were limited to one thread; HiGHS received threads=1. The folder remains below the required disk cap. No subagents, additional model workers, git pushes, production processes or external publishing were used.

Brain recall helped by surfacing the older largest-influence/composition counterexample, which prevented treating that construction as a new discovery. The math store was unavailable. Findings remain in this folder, as the fleet rules require.

Task: “Do the brief fully and carefully” — FEIB17; worker start 10 November 2026, 04:39 +04.
