# A008 gate-label compression: dictionary-first code

## exact target, quantifiers, hypotheses and units

For every finite fixed gate table with positive rational structural probabilities and supports covering the relevant coordinates, construct a finite prefix code describing each used gate name once and decoding the complete spectral set. Give the full ledger, including dictionary selection, local subsets, roots, attachments, codebook selection, output ambiguity and rounding. All entropy and ideal costs are in bits; Boolean influence is E|S| on the uniform sign cube. WHOLE_SET_CODEC.tex contains the complete proof and precise quantifiers.

One combined candidate is supplied: the general codec, its explicitly distinguished record/output versions, and a quantified dictionary-reference application on f_m=x0-(1+x0)prod_i(1-x_i)/2 for all integers m>=1. Its normalized nonempty output-reference expectation is <(25/4)I(f_m), and the corresponding full-output prefix length is <(33/4)I(f_m). This is a new reference-cost theorem on A006's existing sunflower benchmark, not a new Boolean FEI class. Full FEI remains OPEN. Independent acceptance is pending.

## sources actually read, revisions and theorem locators

The complete execution protocol fei-execution-protocol/2, revision 2026-10-11-execution-v2, governs this run. README, CURRENT_STATUS, the claim/obstruction/packet indices, STREAM_NEXT_ACTIONS and the campaign plan were consulted, together with the A008 contract in AGENT_ASSIGNMENTS. BOARD.md was read at stage start (snapshot 2026-10-11 22:05 UTC). B02/STREAM_NOTES.md was absent at the exact supplied path; no direction was inferred. There was no previous A008 mathematical run.

The supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were consulted, as were the curated source-note scopes. Relevant interfaces are C008/C020 (complete reference cost), X012 (addressing), and SEED_LEMMAS section 2 (paid mixture). No historical erasure, phase, biased-threshold or coherent-product assertion is used as a proof premise.

Context threshold_paper_38pp.txt sections 5.2, 5.3, 5.6, Proposition 5.5 and 5.7 were read for the existing queue and whole-witness scope. The earlier threshold version was inspected for context. Percolation versions were inspected for their introduction and section 2 refinement-code scope; their spatial hypotheses are not imported. Text files use cp1252; hashes bind original bytes rather than recoded copies.

A006's complete report, runs/20261011T210855Z-fleet05-A006-posterior-forest-optimization/REPORT.md, was read. It supplies the nonduplication comparison: its queue already visits each used gate once; posterior entropy is indispensable on its common singleton. Its bounds are R<=43I/10 and complete queue expectation <=23I/2, or <=25I/2 with its selected scale prior. These are contextual comparison targets; this proof derives the Boolean law and the new reference independently and does not import A006 as an accepted theorem. The supplied reports/runs index was inspected; no earlier B02 report exists there. out/SOURCES.json contains byte hashes and specific locators of proof-relevant files.

## complete derivation or exact first unsupported line

The dictionary generator first chooses k, then a set F of k gate names, then one nonempty local subset per named gate. With E_k the elementary symmetric polynomial in the fixed name weights eta, its normalized probability is

    a(r)=kappa_k * prod_{l in F}(eta_l)/E_k(eta) * prod_{l in F}q_l(B_l).

The names are one set in increasing order, not one label per coordinate or per occurrence. The exact ideal cost is -log kappa_k+log E_k-sum log eta_l-sum log q_l(B_l). Finite rational probabilities give computable ceil(-log probability) lengths and a canonical prefix trie, with one total rounding overhead less than one. Normalization follows by summing successive normalized finite choices. All codebooks derive from fixed structural data, without knowledge of the sampled spectral set or a free spectrum-dependent selector.

The decoder unions the subsets and assigns each coordinate to the least containing selected gate. It discards empty owners, builds the directed incidence graph, chooses the least vertex in each source strongly connected component, and builds a breadth-first forest with least available attachment coordinates. Thus roots and attachments are deterministically reconstructed after full decoding. Their conditional cost is zero in this generator. This does NOT remove the root normalizer from the original queue: it replaces the queue by a different finite normalized experiment. CODE_COST_LEDGER.json records every term and this distinction.

For Q(A)=sum_{r:D(r)=A}a(r), the output reference is normalized. Finite Gibbs gives H(P)<=h2(v)+sum_{A!=empty}P(A)(-log Q(A)). A finite output prefix trie also decodes A directly, and may compute its lexicographically first record. It does not decode the random latent record. The identity inf_nu[E_nu c-H(nu)]=-log Q(A) is proved by the explicit finite KL calculation. Consequently posterior entropy is legitimate only as quotient/reference credit; it cannot be subtracted from transmitted witness bits. This is the exact final-output ambiguity accounting.

The addressing table uses one uniformly chosen address gate and one uniform control subset; its decoder receives exactly 2a bits, with H=2a and I=1+a/2. The gate name occurs once. No children, roots requiring choices, subset sizes requiring additional bits, or ambiguity remain in that dedicated table. Choosing it at half-weight in a larger mixture would add one paid selector bit; it is not silently free.

For the sunflower choose eta_i=1, kappa_k=(m+1)/(m*k*(k+1)), and q_i uniform on {0},{i},{0,i}. These size weights sum exactly to one. The complete output formulas in WHOLE_SET_CODEC.tex sum every actual dictionary trace, including those with extra common-only gates. In particular Q({0})=sum_k kappa_k*3^(-k)>=1/6. For every private nonempty T of size t, Q(T)=kappa_t/[binom(m,t)*3^t], and Q({0} union T) is at least this value. Their costs are <=3m+2t.

The exact Boolean law is P(empty)=4^(-m), P({0})=(1-2^(-m))^2, and P(T)=P({0} union T)=4^(-m) for T nonempty; I=1+(m-1)2^(-m)>=1. The total rare-set upper bound is r_m=8m*2^(-m)-6m*4^(-m). It is 5/2 at m=1 and 13/4 at m=2, and decreases thereafter because 4^(m+1)(r_m-r_(m+1))=16(m-1)2^m-18m+6>=46m-58>0. The common singleton costs <3 bits. Thus the full nonempty reference expectation is <25/4<=25I/4. Empty/nonempty entropy and prefix rounding each add at most I, giving expected physical OUTPUT code length <33I/4.

There is a necessary limitation. A raw dictionary record producing {0} has cost >=log m: for k<m, binom(m,k)>=m, and for k=m, 3^m>=m. Its probability is <=1/m. So insisting on revealing a latent witness causes an expected cost >=(1-2^(-m))^2 log m. The bounded result is for the output quotient, not a raw name-transmitting record. This exact distinction prevents a false universal gate-compression claim.

The first unsupported universal line is the existence of a globally fixed structural dictionary table, or a paid normalized mixture, whose ENTIRE output-reference expectation is O(I) for every Boolean f. Local subset costs and dictionary size choices are unpaid in general. The dictionary codec proves decodability and a restricted cost payment, not that line. It is not a bound on the original B_lambda residual and imposes no fractional-incidence condition because it uses a different normalized reference.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the search. V1 passed 17,483 recorded exact assertions in 0.103 seconds. V2 retained exactly the same parameter domain and added canonical source-SCC forest reconstruction checks; it passed 46,331 recorded assertions in 1.100 seconds (the saved count excludes the final runtime assertion). No GPU, background process, heavy job or dimension escalation was used; estimated memory was 50 MB and the pilot cap was 60 seconds.

Command from A008: python -X utf8 runs/20261011T221357Z-fleet05-A008-gate-label-compression/code/check.py

Executed domains: sunflower m=1,...,8, integer FWHT and Fraction squared spectra checked against independent physical edge counts; all 4^m-1 dictionary traces for m=1,...,6, normalized exactly, all output masses checked against independent closed-form aggregation, canonical roots and attachments checked on every trace; record/output canonical prefix codes for m=1,...,4, exact Kraft, length and decoding checks; full ordinary addressing truth tables at a=1,2,3, exactly matching the 2a-bit support and influence benchmark. out/CHECK.json preserves the resulting counts and exact rational masses. No floating-point logarithmic sign is used: the all-m cost proof uses integer powers, binomial identities and the explicit recurrence.

## proof dependencies and changed downstream conclusions

The mathematical proof uses elementary finite normalization, Kraft construction, KL/Gibbs, finite graph reachability and a direct Boolean Fourier expansion, all derived in WHOLE_SET_CODEC.tex. No campaign claim requiring review is assumed. The paid-mixture interface is the source-complete seed argument; the present main bound uses just one fixed table and therefore has no hidden scale selector. Independent reviews: A086 primary, A094 alternate. Neither review has occurred in this run.

Changed conclusion for A006/A011/A069: a set dictionary can remove repeated gate-name occurrences and reconstruct attachments, but explicit latent gate identity can still force a diverging physical transcript cost. A normalized output quotient pays the sunflower whole cost by a different reference, with bound <25I/4. Codebook choice, subset costs and marginalization must be kept separate. This is one combined candidate; with A006's candidate it reaches the two-candidate B02 cap visible in the supplied board snapshot. Further broad candidates should wait for review or consume a concrete objection.

## one next mathematical action and independent reviewer

Next: A086 independently reconstruct the output-fiber quotient, canonical dictionary decoder and latent-name lower bound; after that, lift the dictionary law to the r-variable shared-conjunction family named in A006's next action, retaining the full root-independent dictionary/subset expectation. A094 can reconstruct the all-m recurrence and review scope. This handoff is source-bound via the saved files; no messages were sent or another agent's folder modified.

## actual persistence receipts or precise save blocker

REPORT.md, WHOLE_SET_CODEC.tex, CODE_COST_LEDGER.json, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, FROZEN_SPEC.json, code/check.py, code/finalize.py and out/CHECK.json are saved under the requested immutable run directory. out/RECEIPTS.json records byte sizes and SHA256 of the run files except itself; out/SOURCES.json pins proof-relevant reads. STATUS.md, WORKLOG.md and LEARNED.md are updated within A008 only. No shared tree, Git repository, Brain database or external application was modified. Supervisor upload, mirror verification, adoption and independent review remain unobserved rather than claimed.

## Universal bridge

This stage moves C020 whole-set witness cost / G-J-COST by replacing per-occurrence labels with a normalized set dictionary, proving a complete decoder and exact output-ambiguity quotient, and paying the new sunflower reference expectation by <25I/4. It leaves universal selection of a cheap structural table and payment of all local subset/name-set costs open; the original conditioned-forest residual is not universally bounded. The shortest next route is an independent reconstruction followed by the shared-conjunction stress family, because that tests whether the quotient survives growing shared dimension while every gate-name and subset charge remains in one normalized experiment, rather than reopening an already solved FEI class.
