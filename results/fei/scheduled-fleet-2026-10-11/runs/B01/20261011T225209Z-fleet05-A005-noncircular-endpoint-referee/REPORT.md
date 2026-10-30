# exact target, quantifiers, hypotheses and units

A005, B01, noncircular endpoint referee. Followed the B01 lead's v1 2026-10-11 22:40Z direction: referee low-influence localization. All functions below are finite Boolean signs on uniform independent cubes. Entropy is in bits. Put p(S)=fhat(S)^2, d_i=Inf_i, I=sum d_i, B_i=H(S_i|S_-i), and a=2/ln(2). Constants have H=I=0 and are handled separately.

For 0<tau<1, 0<=lambda<1, K>=0, define L(tau,lambda,K): every nonconstant f with max_i d_i<tau has a relevant coordinate i such that

    B_i(f)/d_i <= lambda H(f)/I(f) + K.

The global version removes the low-influence hypothesis. The questions are (i) whether the low-influence class admits arbitrary seeds with H/I preserved, (ii) whether admission transports this selectable-coordinate criterion with the same lambda,K, and (iii) what constant follows rigorously from localization. This is a source-complete referee artifact, not a full-FEI proof or a new broad conjectural endpoint. The global same-parameter implication remains unproved here.

# sources actually read, revisions and theorem locators

Protocol revision 2026-10-11-execution-v2 was read in full. Campaign README, CURRENT_STATUS, claim/obstruction/packet registries, stream actions, assignment matrix and plan; supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and all twelve source notes were loaded. BOARD and B01 STREAM_NOTES v1 were read at stage start. out/SOURCE_MANIFEST.json pins the 39 local input files by SHA256, size and encoding. Loading a manuscript in full does not certify its unrelated theorems.

Mathematical inspection: threshold_paper_38pp.txt section 8.4, Proposition 8.9/Corollary 8.10 (activation); its earlier 29-page version for scope; ERASURE_REDUCTION.md sections 1-4 (restriction identity, scalar JS bound, B<=H); ERASURE_RIGIDITY.md sections 1-2 (exact independence versus local prices); supplemental block/history/phase notes for unpaid endpoint guards. Percolation 30-page Theorems 1.1-1.2 and the earlier 31-page introduction retain geometric crossing hypotheses and supply no arbitrary-seed admission theorem. No percolation arm estimate is used here. Earlier B05/B09/B19 reports were consumed at their recorded scope: all-coordinate local price failure does not refute existential selection, and the old B09 interval defect is not imported.

A001/A002 reports and A082/A086 review reports were consumed as coordination sources. A002-EXACT-HARDENING-LEDGER@1 contains the prior H/I admission; this stage does not reopen its broad hardening baseline. The new work is the coordinate-level erasure ledger and exact failure of witness transport. The elementary activation algebra below is reconstructed independently. No internet lookup, brain write or external communication was needed.

# complete derivation or exact first unsupported line

## 1. Localization implies FEI, with explicit constants

For every i, B_i<=h2(d_i): conditional entropy is at most marginal entropy. The function h2(d)/d decreases on (0,1), because its derivative is log2(1-d)/d^2<0. Consequently a coordinate with d_i>=tau has B_i/d_i<=c_tau:=h2(tau)/tau. The source's restriction identity is

    Delta_i H = B_i + JS_i, 0<=JS_i<=a d_i,
    I = d_i + (I(f_+)+I(f_-))/2.

Assuming L(tau,lambda,K), set

    C = max{ c_tau+a, (K+a)/(1-lambda) }.

Prove H<=CI by induction in dimension, applying induction to ALL children, whether or not they stay low-influence. If some d_i>=tau, choose that coordinate and use Delta_i<=C d_i. Otherwise choose the localized witness. With r=d_i/I in (0,1], induction gives

    H <= C(I-d_i) + (lambda H/I + K+a)d_i,
    H(1-lambda r) <= CI + (K+a-C)d_i
                          <= CI(1-lambda r).

Since 1-lambda r>0, H<=CI. This supplies a slightly sharper high-influence price than the lead's log2(e/tau)+a, without changing the mechanism. It avoids falsely treating {max d_i<tau} as restriction closed. Conversely FEI(C) implies L(tau,0,C): B=sum B_i<=H<=CI, and influence-weighted averaging gives min_i B_i/d_i<=C. Thus existence of finite localized parameters is equivalent to finiteness of FEI, with the displayed quantitative loss. No assumption that C_FEI is already finite is made.

## 2. Arbitrary-seed H/I admission retains the exact FEI constant

For any nonconstant seed f, put g_m=z product_{j=1}^m f(x^(j)), where z is a fresh fair sign, and activate it at one point of k controls: F=1+A_k(g_m-1), t=2^-k. Tensor independence and balancing give H(g_m)=mH(f), I(g_m)=1+mI(f), and g_m is balanced. Direct Fourier expansion gives

    H(F)=t mH(f)+2kt(2-t)+phi((1-t)^2),
    I(F)=t(mI(f)+1+k),
    d_data=t d_i(f), d_z=t, d_control=t,

where phi(x)=-x log2 x. Take k=ceil(2log2(m+1)). Then I(F)->0, max_i d_i(F)->0, minority probability=t/2->0, and H(F)/I(F)->H(f)/I(f), since k/m->0 and phi((1-t)^2)/t->2/ln2. Therefore the supremum H/I on max d_i<tau is exactly C_FEI as an extended-real supremum, for every tau>0. Any FEI inequality H<=CI on that class transfers with the SAME C. This is the established baseline applied to the specific endpoint, not a second claim of novelty.

That argument does NOT transfer L(tau,lambda,K) with the same lambda,K. Its conclusion is an H/I limit, whereas its premise controls one coordinate selected from an enlarged set. The extra coordinates must be audited.

## 3. Exact control erasure: cheap coordinates introduced by activation

For a balanced core g and k controls, put E(u,v)=phi(u^2)+phi(v^2)-phi(u^2+v^2). Each control has

    B_control(F)=2t-2t^2+E(1-t,t), d_control=t,
    B_control/d_control=2-2t+E(1-t,t)/t -> 2.

The nonempty-data spectrum contributes t: for each retained set the two control-membership amplitudes have equal magnitude. The empty-data pairs other than the exceptional constant pair contribute t-2t^2. The exceptional pair contributes E(1-t,t). Its quotient tends to zero because its small mass is t^2 and E(1-t,t)=O(t^2 log(1/t)). Thus for any K>2 and lambda>=0, sufficiently rare activations have a control witness regardless of the seed. If the seed is balanced, the added z has B_z=0 exactly: all Fourier sets contain z, since the empty spectrum of f^tensor m vanishes. This gives an additional witness unrelated to a useful seed coordinate.

These facts identify the missing inference, but they alone do not disprove any UNIVERSALLY quantified localized endpoint. A criterion holding on all low-influence functions is stronger than its holding on these activated images.

## 4. Unbalanced activation ledger and actual counterexample to same-K witness transport

To eliminate the balancing-coordinate distraction, use G=f^tensor m WITHOUT z. Let mu=Ef, c=mu^m, and for coordinate i of a seed copy let v_i=fhat({i}) mu^(m-1). Let F=1+A_k(G-1). Its Fourier coefficients are t Ghat(T) times the control-character sign for T nonempty; t(c-1) times that sign for T empty and control set nonempty; and 1-t+tc at the constant set. Hence

    d_data=t d_i(f), d_control=t(1-c),
    I(F)=t[mI(f)+k(1-c)],
    H(F)=t[mH(f)-phi(c^2)] + phi((1-t+tc)^2)
         +(t-t^2)phi((1-c)^2)
         +2k[t(1-c^2)+(t-t^2)(1-c)^2].

The DATA erasure is exactly

    B_data(F)=t B_i(f)-t E(c,v_i)
                +(t-t^2)E(c-1,v_i)+E(1-t+tc,t v_i).             (D)

To derive (D), tensor independence first gives B_i(G)=B_i(f). All pairs whose retained data set is nonempty scale to total weight t. Remove the original empty-retained-data pair, of cost t E(c,v_i), and insert its 2^k-1 nonempty-control pairs and its single constant-control pair. Homogeneity E(su,sv)=s^2 E(u,v) yields (D).

For every CONTROL,

    B_control(F)=t(1-c^2)+(t-2t^2)(1-c)^2
                   +E(1-t+tc,t(c-1)).                         (C)

Its three terms come from nonempty data, nonexceptional empty data, and the exceptional constant pair respectively.

Actual Boolean seed: f=-1 at one point of the three-cube and +1 elsewhere. Its empty Fourier coefficient is 3/4; each nonempty coefficient has magnitude 1/4; every d_i=1/4; and

    B_i(f)=3/8+E(3/4,1/4),
    B_i(f)/d_i=3/2+(5/2)h2(1/10)=2.6724889839... .

Take m=16, k=8, giving dimension 56. Every one of its 48 data coordinates and every one of its eight controls is covered by the exact symmetry of (D)/(C). Rational interval certificates establish

    seed min B_i/d_i > 5/2,
    every activated data B_i/d_i > 5/2,
    every activated control B_i/d_i < 5/2,
    max d_i = 4251920575/1099511627776 < 1/256.

Displays only: seed ratio 2.672488984, data ratio 2.673079974, control ratio 2.059787640. Therefore F satisfies the local selectable inequality with lambda=0,K=5/2, and the seed fails the corresponding inequality at the SAME K. The selected witness must be a control. This refutes the precise POINTWISE implication "if this arbitrary-seed activation admits a K-witness, its seed admits a K-witness." It does not assert that L(tau,0,5/2) holds for every low-influence Boolean function, and so does not refute its global implication.

Moreover, with k=ceil(2log2(m+1)) and m->infinity, this unbalanced construction preserves H/I for every nonconstant seed (|mu|<1). Formula (D) gives B_data/t->B_i(f), while (C) gives B_control/[t(1-c)]->2. To justify the first limit, c,v_i decay exponentially; E(c,v_i) and E(c-1,v_i) tend to zero; and E(1-t+tc,t v_i)/t=O(t v_i^2[1+k+log(1/v_i^2)]) tends to zero, with zero v_i interpreted by continuity. The entropy formula has leading term tmH(f) and overhead O(tk)+o(tm). Thus the same obstruction persists in a ratio-preserving family with arbitrarily weak influences, not just in the fixed 56-variable check.

## 5. Precise missing proof and a conditional same-parameter bridge

If one strengthens the activation endpoint by requiring its witness to lie in an ORIGINAL DATA COPY, then (D), H(F)/I(F)->H(f)/I(f), and d_data=t d_i(f) imply the global selectable inequality with the SAME lambda,K. Select a subsequence with the same seed coordinate i (there are finitely many); irrelevant seed coordinates cannot be chosen. Divide by t d_i and pass to the limit. This establishes the exact sufficient transfer hypothesis.

The first unsupported line in an attempted same-parameter proof from the original localization criterion is: "the localized witness can be chosen among the seed data coordinates, or a control witness can be converted into such a data witness without increasing lambda or K." Section 4 proves that assertion false for ordinary activation. No other witness-preserving embedding is proved here. The global logical implication with identical parameters is OPEN; only finiteness and the explicit FEI constant in section 1 are justified. It would be incorrect to claim a theorem that same constants are impossible for every conceivable reduction.

Proof request to B01/A094: either construct a witness-preserving admission map with all auxiliary influence and erasure paid, or prove a nonlocal control-to-data transfer that survives this one-point-defect tensor witness. This is a mathematical request recorded for supervisor routing, not a question requiring user approval.

# executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before the exact checker. Pilot: 80 labelled activation cases from all n=1,2 seeds, m=1,2 and k=1,2, maximum dimension six, 992 assertions, zero failures, 0.184 seconds. Full frozen domain: 600 cases, all n<=3 seeds, m/k choices as specified, maximum dimension eight, 7,800 assertions, zero failures, 1.996 seconds. Integer FWHT and Fraction verify the Boolean spectrum, mean, total/individual influences, entropy identity and EVERY data/control erasure identity. Entropy equalities use rational linear combinations of log2 primes, not floating approximations. No symmetry reduction in this finite domain.

out/WITNESS_FROZEN_SPEC.json precedes the single analytic 56-variable certificate. It does not enumerate 2^56 truth values: formulas (D)/(C), analytically derived above, reduce every coordinate to one of two cases. For r in [1,2], z=(r-1)/(r+1), the logarithm checker sums

    ln(r)=2 sum_{j=0}^{39} z^(2j+1)/(2j+1) + remainder,
    0<=remainder<=2 z^81/[81(1-z^2)].

For arbitrary positive rational x it normalizes x=2^q r, then divides positive intervals for ln(r) and ln(2) with the correct ordered denominators. Interval addition/subtraction retains signs. It rounds final intervals OUTWARD to dyadic denominators 2^40 and verifies containment exactly. out/WITNESS_CERTIFICATE.json contains these small rational enclosures and exact threshold assertions; decimal ratios are display only. The first execution's certificate serialization hit Python's integer-digit limit after all sign assertions passed; serialization was repaired by outward dyadic rounding and rerun successfully. No search was altered in response to the results.

Commands, from A005:

    python -X utf8 runs/20261011T225209Z-fleet05-A005-noncircular-endpoint-referee/code/intake.py
    python -X utf8 runs/20261011T225209Z-fleet05-A005-noncircular-endpoint-referee/code/check.py --nmax 2
    python -X utf8 runs/20261011T225209Z-fleet05-A005-noncircular-endpoint-referee/code/check.py --nmax 3
    python -X utf8 runs/20261011T225209Z-fleet05-A005-noncircular-endpoint-referee/code/witness.py
    python -X utf8 runs/20261011T225209Z-fleet05-A005-noncircular-endpoint-referee/code/finalize.py

All computations are lightweight, below the 300 MB gate and 60-second pilot limit. No GPU, automatic n escalation, heavy/background job, numerical optimization or Lean certification is claimed.

# proof dependencies and changed downstream conclusions

Localization consumes the independently reconstructed scalar JS restriction interface of ERASURE_REDUCTION sections 1-4, Boolean pivotal influence and induction. The arbitrary-seed H/I admission consumes the prior elementary activation interface, reconstructed explicitly here. The coordinate obstruction consumes only direct Fourier expansion, tensor independence and the rational logarithm certificate. It assumes neither FEI nor any B09 tax theorem.

Downstream B01/B20: label low-influence FEI estimates as same-optimal-constant endpoints, but label low-influence selectable criteria as finiteness-equivalent with explicit constants unless witness transfer is proved. A002's H/I admission cannot establish same-parameter selectable admission. A003 should preserve this distinction in the implication graph. A055 should require the exact structural exclusion or control-witness transfer rather than invoking rarity. A064/A026 can treat control witnesses as local payment only; the residual tensor seed entropy remains a terminal/descendant obligation.

This audit narrows a proof inference rather than invalidating the B01 lead's finiteness localization theorem. No direction in STREAM_NOTES was rejected. A005's exact refutation is a scoped referee certificate, not an additional broad candidate opened beyond the B01 unreviewed-candidate cap.

# one next mathematical action and independent reviewer

Next: seek a data-witness-preserving reduction, or prove a nonreusing control-to-data payment on the unbalanced activation tensor family above; either must retain the seed coordinate's B_i/d_i and the entire terminal entropy. Independent reviewer A094 should reconstruct (D)/(C), interval endpoints and the exact quantifier distinction; A087 should independently reconstruct the localization induction. Review assignment is a handoff, not completed independent acceptance.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code/ and out/ are in the assigned A005 run. Rolling STATUS.md is exactly two lines; WORKLOG.md and LEARNED.md are saved in A005. out/ARTIFACT_RECEIPTS.json records SHA256 and sizes after finalization; out/SCHEMA_CHECK.json checks the protocol's exact claim/progress keys, report headings, statement hash and byte-identical compatibility copy. No read-only tree, other agent directory, board, shared registry, git repository, brain database, scheduler or trading workspace was modified. Supervisor copying, mirror verification, downstream adoption and independent review remain unverified external steps.

Universal bridge: This stage moves the lead's low-influence version of C018 by completing its constant-explicit finiteness implication and locating a rigorously certified failure of same-K arbitrary-seed witness transport. H/I admission remains exact; the missing universal payment is an actual good seed/data coordinate or a nonlocal control-to-data transfer, not merely a low-influence activated image. The next step is shortest toward full FEI because it targets the selectable witness at the universal erasure frontier and retains the arbitrary tensor core, rather than closing another isolated structural class.
