# FEIB12 local handoff

Status: verified proofs and scoped numerical evidence. This file is local because the fleet rules prohibit shared brain/mesh writes. The launching session can decide what to remember.

PROVED: the proposed lower bound F_S(u)>=up(S)u^median is false with a unique median. At n=4, tt=0xaaa9, S mask 1, q=(9,3,3,1)/16, median 0 and F_S(1/2)/up=91/128. See PROOFS.md and unique_median_counterexample.json.

PROVED: separating q(0)=w before applying Jensen gives
F/up >= w+(1-w)u^(E_q k/(1-w)). Its weighted log bound is no larger than either B or the old mean bound, and is strictly smaller than the mean bound when 0<w<1 and u<1. The optimized cumulative-quantile bound also retains the zero-level atom. CHECKED on all four-variable functions and 12,000 six-variable draws. Majority_513 has old mean/I=17.5579699080002, atom bound/I=2.11777614622744, quantile bound/I=1.85056739793155, actual cost/I=1.80460890960402 (families.json). No universal CI theorem follows without controlling B or equivalent data.

PROVED: no fixed nonnegative combination of Ent(g^2), M-||g||_1^2, M log(M/||g||_1^2), M log(1/p), M log(||g||_infinity^2/M) can make the coordinate-independent local B recursion close with finite universal c and a zero Boolean-root potential. AND_n excludes the four logarithmic features; bounded dyadic linear-plus-parity descendants have J/||D||_2^2=log_2(N+1) and defeat the remaining feature. The bounded dyadic descendants embed exactly as averages of Boolean functions. See PROOFS.md section 5 and induction_audit.json. This does not exclude signed features, child slack, selected coordinate orders, or other potentials.

CHECKED: the independently generated n=5 NPN census has 616126 classes, representing all 4294967296 Boolean functions. Its half-noise cost/I maximum is 0.821862628209331 at tt=0x00010117; its cost/(I-Var) maximum is 1.66014999711538 at padded AND_2. Every representative was re-evaluated by a second implementation, with extremizers evaluated by exact rational character sums and 80-digit logs (census_audit.json, exact_extrema.json).

CHECKED: H_nu(S|U)/I is below 2 throughout n<=5, but exceeds 2 already on majority_33 and is 2.716472066717385 at majority_513. This is an example where an apparently small finite-census constant fails on a structured family. The conditional-entropy CI target is equivalent up to constants to FEI.

CHECKED: six families of four-variable fitted recursion potentials all fail on fresh n=5 and n=6 descendants. The best signed fit has coefficient 2.023229343693195, but it is a finite fit, not a universal theorem (induction_lp.json, induction_audit.json).

Already known in FEIB04: read-once AND/OR formulas have Gamma equal to their empty-set bias term, not necessarily zero. The final FEIB02 symmetric B constant is 3.459354, sharper than the 3.462071 version quoted in the brief.
