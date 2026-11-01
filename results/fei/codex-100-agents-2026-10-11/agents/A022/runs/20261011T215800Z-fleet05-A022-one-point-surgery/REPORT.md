# exact target, quantifiers, hypotheses and units

A022 / B05, run 20261011T215800Z-fleet05-A022-one-point-surgery. For every finite Boolean sign seed on a uniform cube, compute the actual signed Fourier spectrum after one-point or adjacent-point flips and the selector-local logarithmic bill. For every fixed Boolean tensor seed, prove an all-t quantitative formula with a uniform error. All entropies, divergences and logarithms are in bits; ln2 appears only in conversion constants. The cube is encoded as {0,1}^n, equivalently the requested sign cube. Physical influence is the probability of a changed value after reversing a coordinate.

The packet is mathematically resolved at its stated local-formula scope, with independent review pending. Full FEI remains OPEN. Nothing here is an optimized-tree impossibility or an actual unbounded H(f)/I(f) family.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision 2026-10-11-execution-v2. README, CURRENT_STATUS, registries and B05 next action identify the accepted local fixed-price no-go and the unpaid nonlocal bridge. The plan's B05 subsection gives A022's acceptance tests, including signed perturbations and adjacent interaction. PACKET_STATUS contains no adopted A022 artifact. BOARD.md was inspected at stage start. The supplied claude/B05/STREAM_NOTES.md is absent; this is a coordination limitation, not a mathematical dependency.

The original B05 REPORT.md, sections 2--7, and B19 REPORT.md, section 2, were inspected directly. Their archived no-go is used as a control rather than claimed anew. Its source pin is math-open-problems commit 80cc2e5027efa56d79c4ecdf7d4949759ef2068b, independently accepted at 7955d427222392911dc6af2e4ee3aa8aab67ac8c.

Supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were inspected for scope and routing. ISOSPECTRAL_SPLICING_CURATED sections 2--3 give the existing mismatch/minority KL interface; original blob 3421c0cbfd22031554befb962ec92cd0c8bb45b9. LOG_ALLOCATION_CURATED and X003/X009 identify the bent and sparse controls. The supplement is pinned by the protocol to bfb1d10b25cb5cb2e09112357cd24b21b5b1fe5e. No claim of novelty against the literature is made.

The four supplied paper texts were loaded and relevant excerpts inspected, including threshold 38pp Proposition 7.1, Proposition 8.6 and Proposition 8.9 (and earlier composition version), and percolation 30pp/31pp introductions and Lemma 6.1. No percolation theorem is a proof dependency for this stage. out/SOURCE_RECEIPTS.json records 32 exact file hashes and explicitly distinguishes full-file loading from the targeted excerpts inspected in the assistant context; it is not a claim that every line of the unrelated papers was analyzed. One non-UTF8 text required cp1252 decoding; raw hashes are unchanged.

# complete derivation or exact first unsupported line

POINT_SURGERY.tex contains the complete derivation. For D flipped vertices, the actual Boolean function is g=f(1-2 1_D). Its Fourier coefficients are a_S-2t_S, with t_S=2^-n sum_(v in D) f(v)chi_S(v). A fair selector has midpoint mass (a_S-t_S)^2, selector mass e_S=t_S^2, and packet mass q_S=(a_S-t_S)^2+e_S. Therefore

J=sum e_S log2(q_S/e_S)=mu[log2(1/mu)-D2(E||q)],

L=J+R, 0<=R<=mu/ln2, mu=|D|2^-n, E=e/mu.

These are exact signed packets and exact logarithmic terms, including H(parent)=H(q)+L and I(parent)=mu+(I(f)+I(g))/2. The true entropy decrement is L+JS of the child spectral laws.

For a one-point flip, E is uniform on every Fourier label. Every coefficient ratio r_S=a_S/[2^-n f(v)chi_S(v)] is an even integer. Consequently the smaller selector-fiber mass is e_S for every seed; physical mismatch equals spectral minority mass. For adjacent flips, E is uniform on exactly one half-cube, and the essential cross term in e_S is 2 delta^2 epsilon (-1)^(j in S). The change to total influence is the sum over external boundary edges; the internal common edge contributes zero. Simply adding two original-table point-flip influence changes would need a -4 delta f(v)f(v^j) correction in coordinate j. Adjacent coefficient ratios can be odd, so minority and physical mismatch need not agree.

Bent one-point ratios are n+log2(e)+O(2^-n/2); adjacent ratios, divided by their own mismatch mass 2 delta, are n-2+log2(e)+O(2^-n/2). Both follow from exact sign multiplicities and an explicit uniform 12/|r| estimate. This recovers the known bent logarithmic obstruction at the correct local scope.

The quantitative tensor result is: for a fixed m-bit Boolean seed h, let rho be its occupied Fourier-label fraction and lambda the uniform-on-support mean log2 of its absolute integer Walsh sums. After flipping one point of h^(tensor t), with delta_t=2^-mt,

|L_t/delta_t - 2(1-rho^t) - rho^t(2t lambda+log2 e)| <= 12(rho/2)^t.

All nonzero integer Walsh sums are even and have magnitude >=2. Tensor ratios multiply, the occupied fraction is rho^t, and zero packets contribute exactly 2 to the cost/mismatch average. Applying the explicit estimate to occupied ratios proves the formula for every t>=1 and every flipped vertex. Thus positive zero fraction gives L_t/delta_t ->2, whereas full support gives linear growth 2t lambda+log2 e, lambda>=1. The theorem concerns a fixed seed, not an arbitrary dimension-dependent seed sequence. Bent core plus character padding has a separate two-parameter uniform formula in POINT_SURGERY.tex.

First unsupported universal line: there exists a physical stopping policy for arbitrary Boolean input with sum_v pi_v J_v plus all recombination, linear remainders and terminal entropy bounded by K I(input) for one absolute K without reusing ancestral influence. No such inequality is inferred here. The support dichotomy supplies exact stress bills for testing it.

# executed validation with domain, arithmetic, commands and outputs

The complete search specification was frozen before execution in out/FROZEN_SPEC.json. No symmetry reduction: all 276 sign tables in dimensions 1--3, all their 2,120 point and 3,140 adjacent surgeries. Additional declared fixtures: all 16 two-bit seeds at tensor powers 1--6 (96 cases), and quadratic bent dimensions 4,6,8 at three vertices with point and each adjacent flip (63 cases). No dimension escalation or randomness. Integer FWHT and Fraction arithmetic check every signed packet, Parseval, physical mismatch and edge influence change; bent sign multiplicities and tensor factorization are checked independently of the supplied formulas. The tensor error comparison uses outward rational logarithm intervals.

Executed from A022:

`python -X utf8 runs\20261011T215800Z-fleet05-A022-one-point-surgery\code\check_surgery.py`

Result: 563,961 assertions passed, zero failures. The first full pilot took 4.116306 seconds; the final execution, after persisting rational endpoints, is recorded in out/EXACT_CHECK.json. The entire job stayed within its frozen 60-second runtime and conservative 100 MB estimate; no >300 MB job or heavy computation was started. Script process runtime is separate from shell/tool overhead. The interval checker uses 50 atanh-series terms, exact range reduction and all four endpoint quotients for signed division. Exact endpoints are saved; decimal displays are illustrative. Neither the original B05 numerical checker nor the B19 checker was rerun.

# proof dependencies and changed downstream conclusions

The stage's formal dependency chain is self-contained: Walsh linearity, orthogonality/Parseval, elementary entropy expansion, edge counting, parity of integer Walsh sums, and the proved scalar log estimate. Archived no-go and paper identities provide background/provenance, not unreviewed premises. One consolidated source-complete claim is recorded to avoid splitting related formulas into multiple pending candidates.

A020/A021/A053/A077 can now use an actual signed point or adjacent fixture, its influence interaction, and its complete logarithmic bill. A023/A028/A064 should test nonlocal payment against full-support tensors and padding at independent parameters; a blind raw dimension log is too large on seed powers with zeros because the exact KL credit cancels it. This does not establish any proposed primitivity, restricted FEI constant, or global stopping theorem.

# one next mathematical action and independent reviewer

Next: A023 should insert these exact support-dependent bills into a physically specified control-first versus selector-first stopping-tree ledger, keeping the same KL normalization, terminal entropy, and single-use influence budget. Independent review: A087 for physical/mismatch conventions; A094 for the tensor uniform remainder and all quantifiers. A053 can consume the signed near-tensor fixture without recomputing its local spectrum. Handoff is via saved files for supervisor collection; no tool message was sent to other agents.

# actual persistence receipts or precise save blocker

Saved locally in the requested run: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, POINT_SURGERY.tex, SURGERY_LOG_CERTIFICATE.md, code/read_sources.py, code/check_surgery.py, out/FROZEN_SPEC.json, out/SOURCE_RECEIPTS.json, out/EXACT_CHECK.json, and out/PERSISTENCE_RECEIPTS.json. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. The receipt records file sizes and SHA256 hashes and checks protocol field sets. No shared index was modified. No independent review, supervisor adoption, GitHub mirror verification, public release or downstream use is claimed.

**Universal bridge:** This stage moves C019 stopping-tree payment by supplying an exact signed mismatch/KL ledger for point and adjacent surgery, recovering the known bent debt, and proving a uniform tensor support classification that distinguishes surviving logarithms from genuine KL cancellation. It does not bound the complete tree or terminal cost. The remaining universal step is physical, nonreusing transport of these debts using one influence budget. The shortest next step is A023's complete restriction-tree comparison using these reusable formulas, rather than another isolated seed computation or retesting the already refuted fixed-price helper.
