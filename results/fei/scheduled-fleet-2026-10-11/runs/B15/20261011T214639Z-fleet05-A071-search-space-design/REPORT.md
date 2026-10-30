# A071 / B15: bounded search-space design and exact biased-block grid certificate

## exact target, quantifiers, hypotheses and units

Target: B09-BIASED-BLOCK-UNCERTAINTY@1 in CLAIM_REGISTRY.json. For any actual Boolean sign under independent interior biases and a physical block A with complement B, the live helper asserts 0 <= J_A <= M_A+Delta_A. Here M_A=H(S_A|S_B), J_A=H(S_B)-E_Z H(mu_Z), and Delta_A=sum_i_in_A[h2(p_i)+log2(max(p_i,1-p_i))]. All entropy is in bits. Z is a physical input assignment, not a spectral conditioning event. We test its upper inequality; J>=0 follows from the exact mixture identity and entropy concavity.

Family: all three-bit truth tables, all six nonempty proper physical blocks, and p_i in {1/8,1/4,1/2,3/4,7/8}. Assignments x=0..7 use little-endian bits. Output complement lets f(000)=+1; seven code bits specify the remaining signs, giving 128 tables. Input flips paired with p_i -> 1-p_i preserve every squared coefficient (a sign changes on the flipped basis coordinate) and biject the physical children with unchanged branch weights. Delta also stays fixed. Therefore use ordered p_i in {1/8,1/4,1/2}: 27 bias vectors. This covers the entire raw 256*125*6=192000 grid with 128*27*6=20736 representatives. It is a covering reduction, not a claim that all representatives lie in distinct orbits. No coordinate permutations or multiplication by an input character are quotiented: biased character multiplication does not preserve squared spectra generally.

Dummy coordinates embed all n<=2 proper-block cases. Empty blocks have J=M=Delta=0; full blocks have J=0 and M>=0, Delta>=0. For p<=1/2, delta=p log2((1-p)/p)>=0, and reflection handles p>=1/2. No claim covers off-grid parameters or n>=4. A finite helper falsifier would be sufficient to refute its universal statement, but this search found none.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json read in full: revision 2026-10-11-execution-v2. Read campaign README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS B15 records, STREAM_NEXT_ACTIONS B15, and plan A071-A075 contracts (LaTeX lines 958 onward). Read BOARD.md at stage start: 2026-10-11 21:45 UTC snapshot, no earlier B15 result. B15 STREAM_NOTES.md was absent. Earlier run reports B05/B09/B19 were consulted; B09 sections 2-4 supply the precise target definitions, section 5(4) is flagged in the registry as unsupported tax-necessity reasoning. This stage does not use that reasoning.

Supplement CAMPAIGN, CLAIMS (C005-C007, C022-C025, retired C027-C034), COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and source notes were consulted. BLOCK_RESTRICTION_IDENTITY sections 1-3 were read for physical versus spectral experiment distinctions. ONE_BIT_ENDPOINT and ROUTE_MAP were consulted for the two-address scope; the existential constant there is unsuitable for a single finite falsifier without choosing an additional fixed constant. Hence the named current B09 helper was preferred.

Local context papers were consulted in their text versions: threshold_paper_38pp introduction/Theorems A-D, Fourier preliminaries, product-bias normalization and Section 6.4; threshold_paper_29pp_earlier_version composition/restriction locators; percolation_spectral_pivotal_entropy_30pp introduction, normalized product characters and Theorems 1.1-1.6; 31pp earlier version introduction. Their class results are context, not proof dependencies of this exact certificate. No claim of complete independent reconstruction of these manuscripts or of the Maassen-Uffink theorem is made. Local hashes are persisted in out/source_receipts.json.

## complete derivation or exact first unsupported line

Let m_i=8p_i, w(x)=product_i[m_i if x_i=1 else 8-m_i], and V_S=sum_x f(x)w(x) product_i_in_S(8x_i-m_i). In the orthonormal centered basis phi_i=(x_i-p_i)/sqrt(p_i(1-p_i)), the exact squared coefficient is

    mu(S) = V_S^2 / [8^(2n) product_i_in_S m_i(8-m_i)].

This follows by writing each expectation with its physical probability numerator and cancelling the 8 powers in the variance normalization. All masses are rational, nonnegative and sum to one (checked for every parent and child). Each restricted table is constructed by the actual fixed physical assignment. The code checks q(T)=sum_R mu(R union T)=sum_z P(Z=z)mu_z(T) in Fraction arithmetic for every tested case. Thus the defect is exactly

    D = M+Delta-J = H(mu)-2H(q)+E_Z H(mu_Z)+Delta.

For rational t in [1,2], use y=(t-1)/(t+1), so 0<=y<=1/3. The natural logarithm has positive expansion 2 sum_j>=0 y^(2j+1)/(2j+1). After N=32 terms its remainder is between 0 and 2 y^(2N+1)/[(2N+1)(1-y^2)]. Each retained term is floored at scale 2^80; adding N plus the ceiling of the scaled tail is a rigorous upper enclosure. Range reduction p=2^k t and the separately enclosed ln 2 gives a natural-log interval; multiplication by negative k reverses endpoint order. The base-two division takes extrema of all four rational corner quotients, then floors/ceilings at scale 2^60. Powers of two are evaluated exactly. Multiplying by the negative entropy coefficient -p swaps endpoints. Linear interval arithmetic then encloses D with no floating sign decision.

The initial intervals certified 20136 cases nonnegative, including 504 exact zeros. The other 600 intervals contained zero. A separate frozen follow-up expands each D as a rational linear combination of logarithms of rational masses, factors numerator and denominator integers into primes, and sums each prime's exact coefficient. Every coefficient is zero in all 600 cases, proving D=0 without numerical precision refinement. The follow-up also matches each such parent spectrum using a second algorithm: recursively transform physical value pairs (u,v) to ((1-p)u+pv,v-u), then square the centered-basis coefficients and multiply by product variances. This is a second implementation by the same contributor, not independent review.

Consequently every representative satisfies D>=0; the proved invariances extend this finite certificate to the raw grid. There is no unsupported line within the stated finite claim, subject to independent implementation review. The first unsupported extrapolation would be: grid verification implies the same bound for all real biases and dimensions. We do not make it.

## executed validation with domain, arithmetic, commands and outputs

All commands were run from the A071 workspace, with Python UTF-8 and no randomness:

    python -X utf8 runs/20261011T214639Z-fleet05-A071-search-space-design/code/search.py --pilot
    python -X utf8 runs/20261011T214639Z-fleet05-A071-search-space-design/code/search.py
    python -X utf8 runs/20261011T214639Z-fleet05-A071-search-space-design/code/resolve_zeros.py

Saved outputs: out/pilot.json (768/768 certified), out/search.json (20736 cases, 20136 initial certifications, 600 interval-unresolved, zero certified violations), out/zero_certificates.json (600/600 exact prime-log cancellations and alternate spectra matches, no remaining cases). Original unresolved records are retained. The known AND calibration is embedded with a dummy third bit at p=(1/8,1/4,1/2); the exact spectrum is (225,7,3,21)/256 followed by four zeros. This is a calibration, not a new claim about the retired tax-free helper.

The minimum positive lower-bound case is code 4, p=(1/8,1/8,1/2), A={coordinate 2} (block mask 4). Its sign table is +1 except x=3, i.e. (x0,x1,x2)=(1,1,0). The saved lower bound is (12119843879252555703/4096)/2^60 > 0.00256647677032632 bits. Final exact zero count is 1104 and strictly positive count is 19632.

Computational runtimes: 0.191381 seconds pilot, 22.158842 seconds full grid, 0.411915 seconds equality resolution. Single serial process; RAM estimate <=100 MB, not measured. Resource and batch-timeout qualifications are in SEARCH_BUDGET.md. No heavy computation, automatic dimension escalation or >300 MB job occurred.

## proof dependencies and changed downstream conclusions

The finite proof depends on the explicit Boolean tables, elementary normalized product transform, exact arithmetic and the displayed log remainder. It does not assume the universal B09 theorem. One finite claim created: A071-B09-THREEBIT-GRID-CERTIFICATE@1, pending independent review. Universal B09 status and full FEI stay open in this run; no refutation propagation is needed. The finite completeness domain and alternate transform interface are ready for A072/A073/A074; B09 can test a separately versioned sharper tax on this family.

## one next mathematical action and independent reviewer

A085/A092 should independently reconstruct the symmetry coverage and logarithm error proof, with A074 reproducing the minimum-positive case via a centered tensor transform. The next mathematical target is an explicitly versioned sharper singleton tax on the same frozen grid, as suggested by B09's section 8; no automatic n increase or finite-to-all-bias inference. The broader gap G-BIASED-TAX remains unpaid.

## actual persistence receipts or precise save blocker

All run files, code, frozen specs and outputs saved locally inside A071 only. REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json follow the protocol fields. SEARCH_DOMAIN.json and SEARCH_BUDGET.md fulfill the A071 plan contract. STATUS.md, WORKLOG.md and LEARNED.md updated. out/source_receipts.json pins local source bytes; out/manifest.json records saved artifact hashes and sizes. Independent review, supervisor GitHub copy and mirror verification are pending; none is claimed. No shared indices or other agent folders were modified.
