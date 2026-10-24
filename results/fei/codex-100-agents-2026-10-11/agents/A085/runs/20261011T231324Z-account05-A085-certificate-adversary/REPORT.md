# A085 / B17 certificate adversary: completed source-bound scope audit

## exact target, quantifiers, hypotheses and units

The lead's v1 handoff names A071's 20,736-case certificate, then A042 and A047. This stage independently resolves those three sources at their stated scopes. It does not audit every future campaign certificate or extend a finite grid to all dimensions. Full uniform-cube FEI remains OPEN.

A071@1: for every actual three-bit Boolean sign, product biases in {1/8,1/4,1/2,3/4,7/8}^3, and nonempty proper physical block A, certify D=M_A+Delta_A-J_A>=0. Here M_A=H(S_A|S_B), J_A=H(S_B)-E_Z H(mu_Z), and Delta_A=sum_{i in A}[h2(p_i)+log2(max(p_i,1-p_i))]. Units are bits. Z is a physical restriction, not spectral conditioning.

A042@1: fixed finite Boolean tables, deterministic-coordinate contraction, and one-coordinate rare-bias expansions with remaining biases fixed and interior. Natural corrected entropy E=(ln2)Hplus and deficit D=I-Var are distinct from A071's defect. No uniform Taylor remainder or bound on all-arity Hplus/D is asserted.

A047@1: fixed finite Boolean child pair in a common fixed interior product basis, independent selector probability p tending to zero. Certify its limiting debt coefficient and support-disjoint identity. The data dimension and biases stay fixed in this limit. This is neither a finite-p half-tax bound nor a uniform remainder under changing data biases.

## sources actually read, revisions and theorem locators

Protocol read completely: fei-execution-protocol/2, revision 2026-10-11-execution-v2. Campaign README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS and the plan were read; the exact A085 contract was read from AGENT_ASSIGNMENTS.json. BOARD.md at stage start was the 2026-10-11 23:09 UTC snapshot. B17 STREAM_NOTES.md v1, 22:40 UTC, supplies this stage's priority; its direction is followed.

Original source runs, read without modifying them:

- A071: 20261011T214639Z-account05-A071-search-space-design, REPORT derivation/domain, code/search.py, code/resolve_zeros.py, frozen specifications and all needed saved results.
- A042: 20261011T220136Z-account05-A042-bias-endpoint-certificates, REPORT sections 1-4, BIASED_ENDPOINT_SERIES.tex, code/check_endpoints.py and out/CHECK_OUTPUT.json.
- A047: 20261011T220210Z-account05-A047-boundary-search, REPORT derivation, BOUNDARY_ASYMPTOTICS.tex, code/boundary.py, code/unequal.py, out/results.json and out/unequal.json.
- Earlier canonical B05/B09/B19 REPORTs, plus supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and source notes. Their results are contextual, not premises for the independent finite checker.
- All four supplied paper text versions were loaded and their theorem/normalization locators inspected. The threshold 38pp corrected-entropy/product-basis definitions, Section 6.1 and Section 7 composition interfaces are relevant context; the 29pp version provides comparison. Percolation 30pp and 31pp Theorems 1.1-1.6 and 3.1-3.2 distinguish spectral influence from pivotal influence and restricted geometry from general Boolean functions. No paper theorem or external uncertainty theorem is assumed by this audit. Loading/hashing a paper is not a complete proof audit of its remaining sections.

out/source_receipts.json records 66 read source files with byte sizes and SHA256; out/source_locators.json records inspection locators. Claims use the original exact statement hashes. The final persistence manifest additionally pins the original numerical outputs and claim files actually reviewed.

## complete derivation or exact first unsupported line

### A071: HOLDS on its complete finite domain

Our transform acts on a value pair u,v in coordinate bias p by replacing it with ((1-p)u+pv,v-u). Iterating coordinates produces coefficients a_S in the unnormalized basis product_{i in S}(x_i-p_i). The squared orthonormal mass is a_S^2 product_{i in S}p_i(1-p_i). This representation is different from A071's direct integer weighted-sum transform. Parseval and physical-mixture identities are checked exactly for every tested parent and block; each child comes from its actual restricted truth table. Therefore its tested defect is exactly H(parent)-2H(residual marginal)+E_Z H(child)+Delta_A.

The symmetry coverage is valid. Output complement negates all Fourier coefficients. Flipping input i and replacing p_i by 1-p_i negates the i-th centered character, preserves every squared mass, and bijects physical children and their probabilities. Reflect all biases into {1/8,1/4,1/2}, then complement the resulting table to make f(000)=+1. We explicitly map all 32,000 raw table/bias pairs onto all 3,456 representative table/bias pairs; retaining six masks covers 192,000 raw cases with 20,736 representatives. Multiplicities are 16 for 1,024 pairs, 8 for 1,536 pairs, 4 for 768 pairs, and 2 for 128 pairs. No coordinate permutation or biased-character multiplication is used.

For x>0 write x=2^k r with 1<=r<2. Set z=(r-1)/(r+1). The logarithm lower sum is 2 sum_{j=0}^{N-1} z^{2j+1}/(2j+1); the positive tail is at most 2z^{2N+1}/[(2N+1)(1-z^2)]. Our grid checker uses N=28 and floors each scaled term at 2^96. Add N units for the discarded fractional parts and a ceiling of the tail for an upper endpoint. Divide the NONNEGATIVE ln(r) interval by the POSITIVE ln2 interval, then add exact integer k. This avoids signed interval division altogether. Every subsequent signed multiplication swaps endpoints when necessary. Powers of two are exact. Zero masses are omitted from entropy, never passed to log.

A071's own signed division was also inspected: it reverses the ln2 endpoints for negative k and takes all four corner quotients. Its entropy coefficient -mass reverses endpoints. Thus the previously repaired B09 signed-division flaw is not present in this source.

Independent exact result: 19,632 strict positives, 1,104 exact zeros. Of the zeros, 504 are immediate exact interval equalities and 600 require symbolic cancellation. For each latter case we write the defect as sum c_x log2(x), factor positive rational x into primes, and verify every resulting prime coefficient is zero using Fraction arithmetic. Their complete parameter set matches A071's saved 600 zero certificates. The minimum-positive case agrees: code 4, biases (1/8,1/8,1/2), mask 4, with a certified lower bound greater than 5/2048 bits. No sign or equality uses floating arithmetic.

Empty blocks have zero defect. Full blocks have J=0 and M+Delta>=0. Dummy-coordinate embeddings cover lower-dimensional grid cases. Biases 0 and 1 are excluded from the interior orthonormal basis; their proper interpretation is contraction, not division by zero. The source does not claim them as part of its numerical grid.

First unsupported extrapolation: 'these 20,736 representatives imply all real product biases and all dimensions.' No such reduction is supplied or claimed. The universal B09 theorem requires its separate analytic proof; the finite certificate alone cannot establish it. Largest directly enumerated dimension is exactly three.

### A042: HOLDS at the fixed-table endpoint interface; finite intervals verified

Independent derivation: integrate selected coordinates in the centered product basis. With w_S=product_{i in S}4p_i(1-p_i), the mixed-difference coefficient c_S=2^{-|S|} E_{outside S} Delta_S f is a polynomial independent of the selected probabilities and bounded in magnitude by one. Consequently P(S)=w_S c_S^2 and E=sum_{S!=empty}w_S c_S^2 ln(1/c_S^2). Deficit is sum_{|S|>=2}(|S|-1)w_S c_S^2. The function t ln(1/t) extends continuously at zero. Terms meeting a deterministic coordinate vanish, and every remaining coefficient is that of the contracted table. This proves continuity of E and D, not continuity of E/D at D=0.

At a rare coordinate e with child coefficients a_T and a_T+b_T, the parent coefficients are a_T+e b_T and sqrt(e(1-e))b_T. Expanding the two degree-weighted sums gives exactly D=D0+eL-e^2Q, Q=sum_{T!=empty}b_T^2. The empty T has degree zero in the selected-coordinate deficit and is correctly excluded from Q.

For corrected entropy, the unselected T!=empty packet contributes (a_T+e b_T)^2 ln[w_T/(a_T+e b_T)^2]. The selected packet, INCLUDING T=empty, contributes e(1-e)b_T^2 ln(4w_T/b_T^2). The selector normalization cancels exactly; omitting its empty residual label would change K. Differentiating u^2 ln(w/u^2) gives 2u[ln(w/u^2)-1]. At a_T=0 the unselected term is e^2b_T^2[2ln(1/e)+ln(w_T/b_T^2)]. Summing yields E=E(g)+eK+2e^2Z ln(1/e)+O(e^2), with precisely A042's K and Z. Finitely many nonzero a_T have a positive minimum magnitude for a fixed table and fixed basis, so the Taylor remainder is valid there. That minimum need not be uniform over moving biases or dimension.

If D0=0 then the typical child is constant or a signed literal: a degree-one Boolean polynomial can have at most one nonzero slope because the pairwise degree-two coefficients in f^2 equal twice products of slopes. If also L=0, nonnegative D(e)=-e^2Q forces Q=0 and no ratio may be formed. Otherwise L>0 and division gives the stated K/(L ln2) limit. A unit spectral atom means a signed normalized product character is Boolean pointwise; varying an occupied coordinate forces equal magnitudes of its two character values, hence that coordinate is fair. Such an atom is a fair-coordinate parity; its D=|S|-1, not always zero.

For analytic paths the first nonzero orders of w and c give the stated atom expansion; zero polynomials contribute zero. Its constants belong to that fixed path/table. A042 correctly treats the exceptional weighted m=1 limit separately. We independently sum the compressed actual weighted Boolean spectrum over cardinality and heavy-coordinate status at m=2,3,4,8,16,32. All 18 certified Hplus/D, physical-TC/I and pivotal-credit/I intervals contain our independently computed tighter intervals. The original floor/ceiling directions, positive denominator checks, signed scaling and four-corner division are correct. These finite ratio checks are separate from the endpoint proof and do not constitute an all-m search or an all-arity theorem.

First unsupported extrapolation: 'a finite fixed-slice limit K/L bounds every simultaneous degenerating-bias, dimension-varying weighted threshold.' Neither continuity of E,D nor a finite collection of ratios proves this. A042 explicitly leaves it open.

### A047: HOLDS for fixed children; all 20 finite interval cases verified

Let G,H be the two normalized child coefficient vectors. Parent fibers are a_T=((1-p)G_T+pH_T)^2 and b_T=p(1-p)(H_T-G_T)^2, and q_T=(1-p)G_T^2+pH_T^2. At a positive limiting atom entropy changes by O(p); an atom p v+O(p^2) contributes v p log2(1/p)+O(p). For G_T=0, q_T and b_T have leading mass pH_T^2, whereas a_T is order p^2. For G_T!=0, only b_T can create a first-order logarithm. Therefore H(q) has coefficient Z=sum_{G_T=0}H_T^2, H(a,b) has coefficient Z+D with D=sum_{G_T!=0}(H_T-G_T)^2, and the averaged child entropy has none. Hence J-M has coefficient Z-D=2Z+2c-2, c=<G,H>=E(gh).

Because G is supported outside the zero set, Cauchy-Schwarz gives c^2<=1-Z. Thus 2Z+2c-2<=2c-2c^2=1/2-2(c-1/2)^2. The constant/quarter-defect pair attains equality; a fresh fair character shifts both spectra and makes both children balanced without changing these quantities. If supports are disjoint the residual spectrum identifies the child, so J=h2(p); each nonzero fiber has selector conditional probability p or 1-p, so M=h2(p) exactly. These proofs need only Parseval, finite entropy expansions and actual physical children.

The finite reviewer constructs the complete parent truth table and transforms it, rather than using A047's two-child fiber formulas. All 15 named-pair joint spectra agree exactly, all M,J,debt saved intervals contain our independent 44-term exact-rational enclosures, and all five unequal-bias AND debt intervals contain our independent enclosures with the stated strict signs. A047's 40-term positive range reduction correctly divides before adding the signed exponent; zero atoms and exact powers of two are handled correctly. The low-dimensional coefficient comparison in our checker is only for FAIR data cubes of dimension zero and one, not arbitrary one-bit biases.

First unsupported extrapolation: 'the fixed-pair coefficient <=1/2 implies a finite-p half-tax inequality or a remainder uniform over moving bases/dimension.' A047 expressly does not assert this. A concrete two-variable support-transition witness shows why the remainder cannot be made uniform without a new estimate: take typical child g(Y)=2Y-1, rare child h(Y)=1, with data bias q. If q!=1/2, G has both coordinates nonzero, so Z=0 and the debt coefficient is 4q-4. At q=1/2 the supports are disjoint and J-M=0 for every selector probability p. Thus lim_{q->1/2} lim_{p->0}(J-M)/(p log2(1/p))=-2, but reversing the limits gives 0. A bound |J-M-(4q-4)p log2(1/p)|<=C p uniform over q near but unequal to 1/2 is impossible: let q tend to 1/2 at fixed p, then let p tend to zero. This is an obstruction to an unsupported uniformization, not a refutation of A047's claim or of FEI.

### Explicit underflow diagnostic and tail payment

For the actual point defect f_n=1-2 1_{x=0}, put p=2^{-n}. Its empty mass is (1-2p)^2, each of 2^n-1 nonempty masses is 4p^2, and I=2np. IEEE binary64 round-to-nearest first rounds the empty AMPLITUDE to one at n=55, the directly converted empty MASS to one at n=56, and every nonempty mass to zero at n=539. Minimality within this exact family follows from binary64's predecessor gap below one (2^-53) and smallest positive subnormal (2^-1074), and is checked over the frozen scalar range n=1..540. No exponential array is allocated.

At n=539, a directly converted compressed spectrum looks like the constant function: empty mass one, all other masses zero. The exact discarded nonempty entropy is 8p(1-p)(n-1), whose ratio to exact I is 4(1-p)(n-1)/n>3.99. This is the requested explicit implementation failure, not a failure of any of the three audited rational sources. Our powers-of-two regressions include exponents +/-1075, for which rational logs remain exact.

More generally, if M atoms of total mass epsilon are dropped without renormalizing, their omitted entropy is at most epsilon log2(M/epsilon) by concavity and at least epsilon log2(1/epsilon). A support bound M<=2^n introduces dimension in the upper error. An absolute small-mass tolerance alone cannot certify H/I when I can approach zero. The point-defect diagnostic makes this ratio issue explicit.

## executed validation with domain, arithmetic, commands and outputs

Run from A085, all with UTF-8, single serial processes, no random sampling:

    python -X utf8 -u runs/20261011T231324Z-account05-A085-certificate-adversary/code/read_sources.py
    python -X utf8 -u runs/20261011T231324Z-account05-A085-certificate-adversary/code/audit.py pilot
    python -X utf8 -u runs/20261011T231324Z-account05-A085-certificate-adversary/code/audit.py grid
    python -X utf8 -u runs/20261011T231324Z-account05-A085-certificate-adversary/code/audit.py finite
    python -X utf8 -u runs/20261011T231324Z-account05-A085-certificate-adversary/code/underflow.py
    python -X utf8 -u runs/20261011T231324Z-account05-A085-certificate-adversary/code/finalize.py

The 768-case pilot completed in 0.246 seconds (1,009 counted checks). Full grid plus coverage completed in 33.747 seconds (62,570 counted checks), within its frozen 180-second cap. Final finite containment run completed in 0.244 seconds (975 counted checks); the initial overlap run passed 1,106 checks and is superseded. A containment refinement first stopped on Python's integer-to-string 4,300-digit serialization guard, not on a mathematical sign or interval failure. The exact output limit was raised to a fixed 100,000 digits and A042 kept its sufficient fixed-scale rational log representation. out/review_attempts.json preserves this history. The 540-scalar underflow diagnostic completed in 0.018 seconds. Tool startup delays are not mathematical compute runtimes.

FROZEN_SPEC.json, FINITE_REFINEMENT_SPEC.json and UNDERFLOW_DIAGNOSTIC_SPEC.json were saved before the relevant jobs. Peak memory was not measured; estimated maximum 150 MB, so no >300 MB job or memok invocation was needed. No heavy parallel job, automatic dimension escalation, GPU, external library-error assumption or floating sign certificate occurred. The serial grid checkpoint was saved after every bias vector.

Outputs: out/pilot.json, out/coverage_audit.json, out/grid_checkpoint.json, out/grid_audit.json, out/finite_scope_audit.json, out/underflow_diagnostic.json and out/review_attempts.json. Original files were never executed in their folders or imported, so no external __pycache__ or output writes occurred.

## proof dependencies and changed downstream conclusions

A071-B09-THREEBIT-GRID-CERTIFICATE@1 receives an independent acceptance at its exact finite scope. A042-BIAS-ENDPOINT-INTERFACE@1 receives independent acceptance of the fixed-table, contracted-basis interface. A047-SHARP-FIXED-CHILD-RARE-SELECTOR@1 receives independent acceptance of the fixed-pair limit and disjoint-support identity. Original statements, versions, hashes and contributor lists are preserved; A085 supplied no substantive repair to those statements or proofs. Review records are carried only in this run's CLAIMS.json; shared indices remain untouched for B20 adoption.

Elementary transform algebra, Parseval, rational arithmetic, the proved positive log-series remainder, finite Taylor expansion, and Cauchy-Schwarz supply the reconstruction. There is no dependency on the universal B09 uncertainty theorem or on a claimed full-FEI endpoint. The underflow and support-transition diagnostics are source-complete scope warnings, not refutations of a registered original claim. No universal constant changes; no invalidation propagation is required. Numerical evidence, mathematical acceptance at scope, supervisor ingestion and downstream use remain separate.

## one next mathematical action and independent reviewer

Audit the next versioned dimension-uniform singleton-tax/stopping-tree transport from A050/A057/A096, including its conditional M term, terminal entropy and nonreused influence ledger. Require a finite-p bound which survives the support-transition witness rather than extracting a uniform remainder from A047. A090 is the independent reviewer for this review artifact; A094 is alternate. B09, B15, B17 and B20 can consume the three scoped acceptance records now. A071's grid is retired as an audit baseline unless its source changes.

## actual persistence receipts or precise save blocker

All requested files are local under the assigned A085 run: REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, CERTIFICATE_ADVERSARY.md, CERTIFICATE_FAILURE.json, frozen specifications, code and exact output. STATUS.md has exactly STATE and NEXT lines; WORKLOG.md is appended and LEARNED.md records durable facts. The finishing checker validates exact protocol field sets, original statement hashes, compatibility bytes, nonempty accepted intervals, file sizes below 20 MB and a SHA256 manifest. out/validation.json and out/manifest.json are the local persistence receipts. Independent review of A085's review, supervisor GitHub copy, brain ingestion and mirror verification remain pending; no external receipt or message is claimed.

## Universal bridge

This stage moves the B17 lead's certificate-scope gate for C019 stopping-tree payment and C025/G-BIASED-LTF by independently accepting one complete 192,000-case finite domain and two correctly quantified endpoint interfaces, with zero unresolved finite signs. It supplies a two-variable obstruction to uniformizing a fixed-pair remainder and a smallest-in-family binary64 underflow witness, so both precision and changing-basis gaps are concrete. What remains is a dimension-uniform finite-p tax/conditional-entropy payment and its nonreusing terminal-corrected tree transport; neither these certificates nor the diagnostics pay that debt. NEXT reviews that precise live transfer, the shortest route to a universal FEI bridge instead of enlarging a census or repeating an isolated class theorem.
