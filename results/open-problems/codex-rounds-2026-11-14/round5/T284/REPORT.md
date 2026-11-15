VERDICT: PARTIAL the general amplification loss has optimal order sqrt(n log n)

The round-4 amplification theorem holds, conditional on its stated published concentration input. Its deterministic repair and sampling transfer were independently re-derived, and its verifier was rerun unchanged from this folder: PASS.

New beyond round 4: the O(sqrt(n log n)) loss cannot be improved to o(sqrt(n log n)) in a theorem covering all fixed rational d>0 and all polynomial-time computable targets, if final failure must be at most n^(-L). This is an independent-set feasibility obstruction, rather than a limitation of arbitrary product-event concentration.

PROOF.md first proves a quantitative statement for every fixed d>0. Set mu_d=(2/3)d^3 exp(-4d). If a target k_n has P(alpha(G(n,d/n))<k_n)>=1/3 eventually, then for every nonnegative integer loss r_n=o(n), eventually

    P(alpha(G(n,d/n))<k_n-r_n)
        >= exp(-320)/16 * exp(-40 r_n^2/(mu_d n)).

Therefore failure n^(-L) requires loss Omega(sqrt(n log n)). The proof conditions on the vertex sets of four-vertex tree components and on the remaining graph. The independence number becomes a fixed shift of Bin(t,1/4), with t linear in n. A change of binomial measure gives the lower tail. The component mechanism is already in Section 5 of Tom Bohman and Jakob Hofstad, *Two-Point Concentration of the Independence Number of the Random Graph*, https://doi.org/10.1017/fms.2024.6 . No novelty claim is made for it.

A concrete example establishes that the hypothesis can coexist with polynomial-time constant success. At d=1/2, choose k_n within O(1) of a n, where a=(beta+beta^2/2)/d and beta exp(beta)=d. This target is polynomial-time computable. A deterministic solver that exhaustively solves components up to logarithmic size has polynomial worst-case time and finds the optimum with probability tending to one. Its success at k_n tends to 1/2, while every algorithm, irrespective of running time, needs the stated loss for failure n^(-L). The Gaussian central-target assertion is imported from Boris Pittel, *On tree census and the giant component in sparse random graphs*, Random Structures & Algorithms 1 (1990), 311--342, https://doi.org/10.1002/rsa.3240010306 . Its publisher abstract states the limit and exact formulas. No moderate-deviation estimate is imported.

Commands, with this folder as cwd:

    env OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T284/verify_rows.py
    env OMP_NUM_THREADS=1 nice -n 15 python3 verify_loss.py

Both pass. The new verifier checks all 33867 labelled graphs up to six vertices; 36 conditional shape fibres; 18 exact component-moment cases; 12 disjoint-component identities; 4368 forest shapes; 5935 exact threshold cases; 24 exact binomial tails through 16384 trials; and 48 likelihood identities. Independent rational bisection and Decimal Newton iteration agree on the central-target constants, and two variance formulas agree. Runtime was 0.949 seconds; peak RSS 157810688 bytes. OMP_NUM_THREADS=1 and inherited nice=20 were checked. The sandbox denies raising priority to the requested 15. Outputs are in LOG.md, row_verification.json and loss_verification.json; the adversarial checks are in AUDIT.md.

What failed or required care: a direct opening of Pittel's DOI failed; the PDF URL redirected to the publisher's abstract, which supplies the statement but not its full proof. No verifier assertion failed. Subtracting the O(1/n) exceptional component-count probability from the final small tail would have been insufficient; the proof selects a fixed positive mass of suitable conditional histories before estimating that tail. A central limit theorem alone would also be insufficient for the polynomial-failure conclusion; the separate binomial change of measure supplies that part.

Limits: T284 remains open. The explicit example uses d=1/2 and a target near the optimum. The all-d bound requires constant infeasibility at the target, a hypothesis not supplied at (1+epsilon)log(d)n/d. This does not prove an obstruction there, establish a named average-case hardness reduction, or construct a barrier-crossing algorithm. The bounded settlement check found none. The finite verifier checks the application, not Pittel's central limit theorem or the imported concentration algorithm. The previous report's source-parameter caveat for computational concentration remains unchanged.

Next worker: do not seek a uniformly smaller loss for the whole round-4 theorem; the example rules that out in order. A more focused amplification question is whether loss can be reduced for targets known to lie a fixed linear distance below the typical optimum, especially at the large-d overlap density. Resolving T284 still requires a separate named average-case reduction or a new algorithm. The feasibility bound here cannot provide that reduction.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 09:03 +04 (Asia/Tbilisi).
