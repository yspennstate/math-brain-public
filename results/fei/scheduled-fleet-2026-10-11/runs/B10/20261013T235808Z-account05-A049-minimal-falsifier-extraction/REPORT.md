# exact target, quantifiers, hypotheses and units

A049 / B10, resumed stage 20261013T235808Z. Full uniform-cube FEI remains OPEN. Follow B10 STREAM_NOTES v2's uncompleted A049 direction: test the conditional block sharp-tax claim

    J_A-M_A <= tau*(p1)+tau*(p2),  |A|=2,
    tau*(p)=h2(p)-min_t[h2(sin^2 t)+h2(sin^2(t-beta))], sin^2 beta=p.

The frozen domain is every actual Boolean sign on two revealed bits and m=0,1,2 fair residual bits; revealed biases p1,p2 independently range over {1/8,1/4,3/8,1/2}. There are 1,052,928 truth-table/bias cases. M_A=H(S_A|S_res), and J_A=H(S_res)-sum_z mu_A(z)H(child spectrum), using the product-biased orthonormal Fourier basis, actual physical child probabilities, and normalized Boolean child spectra. All entropies are bits and include the empty atom.

Result: no violation in this entire frozen domain. Every nonuniform bias pair has actual debt below explicit, rigorously certified lower bounds on tau*(p1)+tau*(p2), with a common certified gap greater than 7/1000 bit. The uniform pair has maximum debt exactly zero. The global maximum of (J_A-M_A)/(Delta_A/2), excluding its zero-denominator uniform pair, is certified in (0.68132470,0.68132471). An essential four-bit circuit attains it. These statements are finite verification, not all-dimensional additivity or FEI.

# sources actually read, revisions and theorem locators

Read own STATUS and WORKLOG, BOARD.md snapshot 2026-10-13 23:49 UTC, B10 STREAM_NOTES v2 dated 2026-10-11 23:31Z, and the full execution protocol revision 2026-10-11-execution-v2. The earlier A049 packet is complete; an intervening stage directory contains no report and supplies no mathematical claim. This run does not repeat the retired tax-free falsification.

Read B10 lead REPORT in claude/B10/runs/20261011T230400Z-claude-B10-onebit-half-tax: exact angle reduction and conditional Claim 2. Its cited block-additivity theorem was not re-read by the lead; this run neither assumes it nor promotes it to acceptance. Read A047 stage-2 REPORT and DERIVATION, run 20261012T003641Z-account05-A047-boundary-search, especially explicit rational real witnesses and the exact singleton Boolean census. The chosen real witness abscissae are credited to that source, with their lower-bound calculation reconstructed here.

Read A047 stage-3 REPORT, run 20261013T221434Z, for the newer root-compatible bank-conversion result and its actual half-I/future-conditioning controls. Read A050 stage-2 REPORT, run 20261013T212442Z, including its conditional block scope and first unpaid reference-bank line. These newer transcript results do not complete A049's block census. Earlier required manuscript/context readings retain the accurately stated scope in the first A049 report; no manuscript theorem is used here. Source hashes and locators are saved in out/SOURCE_RECEIPTS.json; repository mirror equivalence is not asserted.

# complete derivation or exact first unsupported line

## Actual Boolean enumeration and exact transform

Fix m and N=2^m. Each truth table supplies four children indexed z=z1+2z2, with integer residual Walsh vectors W_z(T). Each normalized child coefficient is W_z(T)/N. Global output negation changes every coefficient's sign and leaves M,J and all squared spectra fixed. Fix the all-zero input output to +1: exactly half the tables remain, with no fixed points under negation. No variable, bias or input-complement quotient is used.

Write p1=a/8, p2=b/8, a,b in {1,2,3,4}. For each residual label T put

    L=(8-a)(8-b)W00+a(8-b)W10+(8-a)b W01+ab W11,
    D1=(8-b)(W10-W00)+b(W11-W01),
    D2=(8-a)(W01-W00)+a(W11-W10),
    D12=W11-W01-W10+W00.

The squared parent masses, indexed by the two block frequency bits, are exactly

    [L^2, a(8-a)D1^2, b(8-b)D2^2,
     a(8-a)b(8-b)D12^2] / (4096 N^2).

These formulas follow by expanding each centered selector basis and averaging the independent physical selectors. The residual marginal Q_T is the sum of those four masses. Independently, Q_T=sum_z mu_A(z)W_z(T)^2/N^2, with physical child weights

    [(8-a)(8-b),a(8-b),(8-a)b,ab]/64.

Let P be the entire parent law and C_z the normalized child law. Then the chain-rule definitions give the exact debt

    E=J_A-M_A=2H(Q)-H(P)-sum_z mu_A(z)H(C_z).

Every transformed table is checked for nonnegative masses and exact normalization by integer array comparisons. The 48 attaining records are independently reconstructed by direct weighted truth-table centered-basis moments, divided by rational squared basis norms; their child marginal identities are checked as Fractions.

## Certifying the target without assuming additivity

For any single-qubit angle with x=sin^2 t,

    y=sin^2(t-beta)=p+(1-2p)x-2sqrt(p(1-p)x(1-x)).

The definition of tau* immediately implies

    tau*(p) >= h2(p)-h2(x)-h2(y).

Use x=1/32,1/16,1/256 at p=1/8,1/4,3/8, respectively. Rational square-root brackets from integer isqrt at scale 2^100 enclose y, which lies in [0,1/2]. Binary entropy is increasing there, so rational entropy endpoint bounds enclose each witness debt. At p=1/2, a basis vector gives tau*>=0. No minimizer characterization, real-child attainment theorem, half-Delta theorem or tensor-additivity theorem is assumed by this comparison.

Each enumerated E is bounded above by the sum of these explicit lower witnesses. Therefore it is bounded above by the sum of the true tau* values. The weakest strictly positive certified gap over every nonuniform bias pair, every m and every table exceeds 7/1000 bit; its exact rational value is in out/INDEPENDENT_RECONSTRUCTION.json. The pair (1/2,1/2) is certified separately by its exactly zero finite maximum.

## Exact finite maxima and ties

Each rational entropy contribution is rounded outwards to a common 2^-40 lattice. The maximum lower endpoint and maximum upper endpoint enclose the finite supremum. Choose a witness attaining the greatest lower endpoint; every candidate whose upper endpoint overlaps it is expanded into a rational prime-log coefficient vector. Every such vector equals the witness's vector exactly. All other candidates have upper endpoint strictly below that witness's lower endpoint. This proves exact finite maximality and exact tie counts. Equality of coefficient vectors is sufficient; no independence or converse theorem for prime logarithms is asserted.

For m=0,1, the exact maximum is zero at every bias pair. For m=2 let E1,E2,E3 denote the exact two-fair-residual singleton maxima at selector biases 1/8,1/4,3/8, respectively, and E4=0. This block census gives maximum E_min(a,b). Exact prime-log vectors and all counts are in out/CENSUS.json; approximate displays are E1=0.1195450160, E2=0.0827281513, E3=0.0094404728. Those decimals are descriptive, not the sign certificate. The equality with the already completed A047 singleton census is an observed and exactly checked finite identity, not a theorem for more residual bits.

The zero-denominator pair p1=p2=1/2 is excluded from the ratio. Among the other pairs, the global ratio maximum occurs at m=2 and bias pair (1/8,1/2), or its selector-coordinate interchange. Bounds on all other pairs are strictly smaller. Exact symmetry and the prime-log expressions identify the two attaining bias pairs, rather than relying on displayed decimal equality.

## Minimal attaining certificate with both revealed bits essential

Let X1 have probability 1/8 of being 1, and let X2,U,V be fair independent bits. Reveal A={X1,X2} and set

    f(X1,X2,U,V)=(-1)^X2 (1-2X1UV).

All four coordinates are essential. Its complete truth table, indexed X1+2X2+4U+8V, has mask 37683; the actual 16 sign values and the exact circuit/spectra are stored in out/EXTREMAL_CERTIFICATE.json. Multiplication by the fair revealed character (-1)^X2 translates the block spectral label; its squared child spectra are unchanged by the physical X2 sign. Thus the actual block debt equals that of the rare-selector quarter-defect singleton without silently treating X2 as an irrelevant physical input.

The exact debt E satisfies

    128 E=224+225 log2(3)+225 log2(5)+14 log2(7)-232 log2(29).

Its positive sign is certified by the modest-denominator integer comparison

    2^224 * 3^225 * 5^225 * 7^14 > 29^232.

Here Delta_A/2=(log2 7)/16. Consequently the exact global ratio is

    R=[224+225 log2(3)+225 log2(5)+14 log2(7)-232 log2(29)]
      /[8 log2(7)].

Sign-correct rational log bounds certify

    68132470/100000000 < R < 68132471/100000000.

The entire frozen grid with m<=1 has maximum zero. This attaining positive-debt circuit therefore has the minimum possible four total bits inside the searched domain, including the requirement that both revealed bits be essential. No minimality outside the frozen bias grid/fair residual assumptions is claimed. It is an extremal stress certificate, not a violation of the target bound.

## Logarithm error proof and arithmetic limits

For positive rational u, write u=2^k y with 1<=y<2, and z=(y-1)/(y+1) in [0,1/3). The 32-term rational sum

    L(y)=2 sum_{j=0}^{31} z^(2j+1)/(2j+1)

has nonnegative remainder at most 2z^65/[65(1-z^2)]. The same expansion at y=2, z=1/3, gives strictly positive rational bounds on ln2. Divide the nonnegative ln(y) endpoints by opposite ln2 endpoints and add k. Multiplication by -u reverses endpoints before dyadic rounding. All cached mass evaluations and integer array aggregations preserve outward containment. NumPy arrays contain only small integers: counts, mass numerators, and fixed-lattice entropy sums; no floating-point spectrum, entropy, search selection or sign enters a certificate.

The initial verifier mistakenly required an exactly zero debt's rounded upper endpoint to be zero; it failed before any expensive ratio calculation. That assertion was repaired to use the already certified empty prime-log vector. A potential oversized integer exponentiation for fine ratio bounds was also removed before execution; a process-stop check found no matching live process. Only the entropy sign with denominator 128 uses integer powers. Fine ratio signs use the rational log bounds above. out/VERIFIER_REPAIR.md records these facts. There was no oversized job or artifact and the census was unaffected.

First unsupported line: extending this restricted verification to arbitrary residual dimension or residual product biases, or funding the valid tax and conditional M plus terminal entropy in a universal nonreusing C019 ledger. No passing finite census proves either line, and no FEI falsifier was found.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the pilot and full run. Pilot m<=1: 4,352 full cases / 2,176 representatives, 2,514 exact assertions, PASS in 2.712464 seconds. Main m<=2: 1,052,928 full cases / 526,464 representatives, 20,473 recorded exact assertions and vectorized whole-domain mass checks, PASS in 48.831366 seconds. Direct independent implementation of the 48 attaining spectra and exact ratio signs: 543 assertions, PASS in 2.223789 seconds. This implementation is a second representation by A049, not independent-agent acceptance.

Commands from A049:

    python -X utf8 runs/20261013T235808Z-account05-A049-minimal-falsifier-extraction/code/census.py --max-m 1
    python -X utf8 runs/20261013T235808Z-account05-A049-minimal-falsifier-extraction/code/census.py --max-m 2
    python -X utf8 runs/20261013T235808Z-account05-A049-minimal-falsifier-extraction/code/verify.py

Domain by residual size: m=0 has 16 tables, m=1 has 256, m=2 has 65,536; each is tested at all 16 ordered bias pairs. Only output-negation symmetry halves computation. Estimated memory 120 MB; peak RSS was not measured. No >300 MB job was expected or launched, no heavy job, no automatic dimension increase, no GPU or background helper. The main stayed under its frozen 1,200-second cap; the pilot stayed under 60 seconds. The spec's proposed pre-pilot hash-receipt timing was not implemented: final SHA256 receipts bind the saved code but do not prove a pre-pilot hash timestamp; out/SPEC_NOTES.md states that limit. The mathematical domain and arithmetic were frozen before execution.

# proof dependencies and changed downstream conclusions

No external mathematical claim is assumed. The exact transform, chain rule, explicit scalar tau* lower witnesses, rational error bound and witness signs are reconstructed. B10's lead theorem and cited block-additivity result remain outside the proof dependency list; A047 is credited for the already supplied scalar witness choices and singleton maxima.

Changed conclusion: the lead's specified two-block finite domain is now closed without a violation, including exact maxima and a minimal actual essential-coordinate stress fixture. All nonuniform points pass a stronger comparison than their true sharp-tax upper allowance. This verifies an existing candidate at finite scope; no new broad universal candidate is opened under the pending-claim cap. The ratio maximum and truth table are ready for A074; no external message, registry adoption or independent acceptance is claimed.

# one next mathematical action and independent reviewer

A074 should reproduce the full block census or its maximality certificate using a distinct truth-table transform. A092 is primary reviewer; A074/A085 are reconstruction alternatives. Do not expand this bias grid or dimension without a newly versioned target. A049's next mathematical action is to minimize the newer actual descendant-reference injection failure of A048/A047 to the smallest essential tree and exact channel/reset comparison, retaining the root witness, terminal entropy and one removed-influence account. That directly addresses the first unpaid universal payment line after this finite local check.

# actual persistence receipts or precise save blocker

The four protocol files, frozen spec, code, incremental/full census, direct verification, all scalar tax lower witnesses, exact extrema, source receipts, repair notes and A074 handoff are saved inside this run. STATUS has exactly two lines; WORKLOG and LEARNED record this stage and the arithmetic lesson. Finalization checks exact protocol fields, statement hashes, equal progress copies and the 20 MB file limit, then writes out/PERSISTENCE.json. All writes stayed inside A049. No git, Brain write, other-agent mutation, publication or external message occurred. Supervisor copying, mirror verification, downstream use and independent acceptance remain pending; there is no local save blocker.

**Universal bridge:** This stage moves the B10 block-tax interface feeding C019 stopping-tree payment by closing all 1,052,928 specified finite cases, certifying a half-tax ratio below 0.68132471 and a sharp-tax-lower-witness gap above 7/1000 at every nonuniform grid pair. It supplies no universal additivity or FEI constant. What remains is to fund conditional M, a valid tax and all terminal entropy with one physical influence account and correctly charge descendant-reference injections. NEXT minimizes the new actual injection failure rather than increasing an isolated census, because the updated board places the unpaid universal cost in reference/conditioning transport.
