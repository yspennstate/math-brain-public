# exact target, quantifiers, hypotheses and units

A023/B05 stage4, run 20261014T022245Z-fleet05-A023-amortized-rarity-budget. Actual uniform Boolean signs; bit entropy. For ALL Boolean branches G,H on the same physical data cube, any fresh point-selector width s>=1, alpha=2^-s and gamma=P(G!=H), let F=G+A_s(H-G). No balance, disjoint-data, or lower-disagreement hypothesis is imposed. Query selector controls until the point is resolved, then stop at actual G or H. Retain H_T=(1-alpha)H(G)+alpha H(H), I_T=(1-alpha)I(G)+alpha I(H). Queried influence is I_S=2s alpha gamma.

PROOF.md proves the whole-block erasure sum and once-owned boundary reserve:

    E_B <=2(1-2alpha)I_S+4alpha gamma(1-alpha)[log2(1/gamma)+1/ln2],
    R=2alpha(1-alpha)I(GH)<=2I_T,
    H(F)-H_T <=(11/2)I_S+R.

Genuine minority/KL bill <=(5/2)I_S+R; its separate 3mu/ln2 allowance gives <7I_S+R. These are complete bills with H_T restored. Each physical data reserve has owners 2alpha times the inactive terminal capacity and 2(1-alpha) times the active terminal capacity, marked once before the entire selector block. Failure histories share one aggregate G terminal account; it is never recreated per failed bit. For certified terminal rates C_G,C_H this gives max(11/2,C_G+2alpha,C_H+2(1-alpha))I(F). Arbitrary-core FEI is not assumed.

For arbitrary even-dimensional bent signs and their actual one-vertex flips, both balanced by the same independent z, the branches have H/I<2. The full shared-data switched family has H<(11/2)I, retained J+terminal<=4I, full sufficient KL ledger<7I, uniformly in all even m>=4 and s>=1. Fresh point activation of this family gives H<6I and influence tending to zero as its activation width grows. No localized bad-face bound or universal nested-reserve theorem follows from the actual entropy payment.

# sources actually read, revisions and theorem locators

Read BOARD.md supervisor snapshot 2026-10-14 02:22 UTC, B05 STREAM_NOTES.md v2, own STATUS.md and complete EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2. BOARD output exceeded the display budget, so the inspected mathematical updates are specifically the B05/B06 and nearby shared-data/payment entries; no claim about auditing every board entry is made. Read A025 run20261014T002956Z REPORT.md and full PROOF.md: its multi-bit unfiltered reserve failure and moderate-disagreement policy. Read A021 run20261014T011316Z REPORT.md, DERIVATION.md, CLAIMS.json and REVIEW_A023.md: sharp contrast price and all-width K7 overlap closure. These already did our former NEXT; do not duplicate their multi-bit overlap census or bound.

Read A028 stage3 REPORT.md, which closes rare point selectors for DISJOINT private data, while naming shared data as its unsupported extension. The present branches may share the entire data cube; its disjoint-branch rate is not asserted at this interface. Read own stage3 checker and existing one-separator statements; the original valid reserve and corrected earlier remainder review remain intact. A021 has independently accepted our v2 single-separator entropy/face subtheorem only, as its local review states. Existing lead odd-face direction is followed; actual entropy/KL payment is explicitly distinguished from localized odd-face payment.

Source SHA256 receipts record exact files and scoped reads. No new paper premise, web result, brain query/write, shared registry edit, or external communication.

# complete derivation or exact first unsupported line

Full proof is PROOF.md. At a live selector query put l=j-1, rho=2^-l and d=rho gamma. Nonempty residual-selector Fourier rows contribute exactly 2(1-rho)d. Empty residual-selector packets have derivative mass rho^2 gamma and total mass <=1; the entropy remainder inequality and log-sum give rho^2 gamma log2(e/(rho^2 gamma)). This argument permits complete coherent overlap of core Fourier rows.

Physical reach w satisfies w d=2alpha gamma at every live node. Sum the exact finite geometric identities sum rho=2(1-alpha) and sum l rho=2[1-(s+1)alpha]. Cancellation of the residual-selector terms yields the stated E_B, with one logarithmic coefficient 4alpha gamma(1-alpha), rather than restarting a log(1/d) account at every descendant. Unthinned source gamma remains the same at each query.

Disagreement-set edge isoperimetry pays gamma log2(1/gamma) by I(GH)/2. For each coordinate i, Inf_i(GH)<=Inf_i(G)+Inf_i(H), giving the named fractions of the ACTUAL terminal capacities. Aggregate terminal probability is exactly1-alpha or alpha; stop before data queries and retain all their entropy. The two-unit allowance pays one point block only; unused terminal capacities are not silently replenished.

Entropy telescoping adds JS<=2d/ln2. The resulting coefficient is A_s=2(1-2alpha)+2c+2c(1-alpha)/s. Rational c<81/56 certifies A_s<11/2 for s1..4; for s>=5 use A_s<2+(12/5)c<11/2. Without JS, b_s<5/2 follows by checking s1..5 and using b_s<2+c/3 for s>=6. Minority J<=B and mu<=d give the retained/full KL bills. These finite scalar checks have explicit all-s tails; actual Boolean pilot checks are not the proof of those tails.

The balanced bent-edit branch class has H<=m, I(G)=1+m/2 and I(H)>=1+m/2-2m2^-m; thus H/I<2 for all even m>=4, regardless of bent seed or edited vertex. No unproved terminal FEI is substituted. Constant-child activation is independently bounded by B/d<3 and JS/d<3, so fresh activation gives H<6I and I=2^-t[I(F)+t] for the balanced switched family. All coordinates and widths are independent physical ones.

REVIEW_A021.md independently reconstructs the upper relative-bias point-switch price and strict6/7 sufficient criteria. It accepts ONLY that scope. Its lower supremum asymptotics and entire overlap application are not independently accepted here; no repair contribution is made. It explains the constant Fourier row and the nonempty-core log-sum separately.

First unsupported universal line: give two nested/overlapping point-switch blocks the same physical terminal-coordinate bank without reissuing the fractions already consumed, and retain all actual terminal entropies. Applying max(C+2,11/2) repeatedly merely increases the terminal rate with depth; it is not a universal constant. Also E_B payment does not establish Q_bad,4<=KI: the full child-product face price is a different upper currency. No full FEI theorem or counterexample is claimed.

# executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes execution. Domain1039 cases: all256 ordered labeled two-bit Boolean branch pairs at widths1..4, plus15 balanced bent/flip shared-data fixtures m=4,6,8 at widths1..5. Constants and gamma=0 included. No symmetry quotient, random sampling, domain increase, GPU or background process. Maximum dimension14, memory estimate150MB; no >300MB job was started, so no memok gate applied.

Command: `python -X utf8 runs\20261014T022245Z-fleet05-A023-amortized-rarity-budget\code\check_block.py`.

Initial attempt reached the frozen60-second pilot cap during the bent fixtures, after all1024 two-bit pairs had passed. out/INITIAL_ATTEMPT.json records the persisted case count. No mathematical assertion failed. Before rerunning the EXACT SAME domain, out/SPEC_UPDATE.json froze helperv1.1, memoization of repeated transforms/node metrics, and removal of an exactly representable half-integer float in a validation assertion. All mathematical decisions in the final run are integer/Fraction or certified log intervals. Runtime clocks alone use floating point.

Final PASS: 1,039 cases, 34,734 exact assertions, 386 saved sign certificates, 16.271131299989065 seconds observed compute time. Counts/runtime are saved in out/validation.json. Integer FWHT and independent undirected edge counts check actual influences, source gamma, terminal weights, coordinate reserve ownership, child-product faces, geometric summation, source upper price, signed entropy telescoping and all stated retained ledgers. Prime-log vectors and positive24-term atanh intervals with proved tail and outward100-bit dyadic rounding certify every tested sign;48-term fallback is frozen. Exact zeros are equality. out/rows.jsonl flushes after each completed case; out/results.json retains the structured aggregate, and out/sign_certificates.json retains replayable endpoint certificates.

No broadening or repeated test after a complete passing run is required. code/finalize.py validates metadata, endpoint signs and ownership against saved results; it performs no new Boolean search.

# proof dependencies and changed downstream conclusions

The new whole-block theorem is self-contained: sector kernel/log-sum, finite geometric sums, elementary edge isoperimetry, scalar JS inequality, direct coordinate ownership and exact terminal certificates are proved in PROOF.md. The earlier A023 v2 claim is preserved at its pinned scope as a dependency of the bundled extended v3 only. The new theorem does not depend on an A021 price assumption or a defective remainder sign. Source ideas are credited to A025's selector-sector split and A021's contrast analysis.

The existing A023 overlap/payment claim is extended to version3; no new broad universal candidate is opened. A021's v1 relative-bias claim receives a partial HOLDS review record while whole-claim acceptance remains pending. A021's independent scoped review of A023 v2 is consumed at its actual entropy/face scope, without silently accepting the old bundled KL or biased-core portions. Shared indices are untouched.

Downstream A021/A025 can replace a fresh per-layer logarithmic reserve by the explicit once-owned whole-block budget. A028 can use this shared-data point-selector bound with a two-unit terminal reserve, but cannot substitute its sharper disjoint-branch price. A027/A029/A064 still owe a nested-history ownership rule. Prior unfiltered-face failure and valid one-separator proof remain unchanged.

# one next mathematical action and independent reviewer

Next: take two nested point-selector blocks whose terminal branches use the SAME core data coordinates. Write the physical conditional terminal capacities before the first block, subtract its marked R_i, and ask whether the second block's actual reserve fits the remaining capacity or yields an exact deficit. Preserve original source disagreement for each block; do not duplicate data branches or restart their allowance. This targets the first unproved reuse step, not a larger paid overlap census.

A021/A025 should reconstruct the geometric cancellation and coordinate reserve fractions; A087/A094 should check the scalar all-s bounds, exact terminal support/edge certificates and the distinction from Q_bad. Handoffs are saved artifacts only, not sent messages or observed adoption.

# actual persistence receipts or precise save blocker

Saved required REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json, PROOF.md, REVIEW_A021.md, frozen specs and initial cap record, direct checker, metadata checker, exact results/sign certificates/constants, source hashes and artifact receipts. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. All writes are confined to A023; old runs and shared sources are read-only. Artifact checks verify exact protocol keys, compatibility byte identity, report headings and <20MB file sizes. No local save blocker. Independent acceptance of the new theorem, supervisor copying, remote mirrors and downstream use remain unverified.

**Universal bridge:** This stage moves C019 actual stopping payment and its C024 history interface by paying the logarithmic point-switch cost once over the whole selector block, even with completely shared data and arbitrarily small disagreement. The explicit reserve is2alpha(1-alpha)I(GH), with physical terminal owners; H-H_T<=(11/2)I_S+R and retained/full KL ledgers are paid without repeated complete-face prices. The balanced bent-edit class has H<(11/2)I and fresh rare activation has H<6I with I tending to zero. What remains is nested ownership of the same terminal-coordinate capacity and a universal terminal certificate; localized odd-face credit is not inferred from an actual entropy bill. NEXT checks the first two-block reuse directly, the shortest route to universal amortization because it tests whether the paid block interface composes without a growing terminal surcharge.
