## exact target, quantifiers, hypotheses and units

Complete packet A072's baseline algebraic engine obligation for the actual family frozen by A071, targeting B09-BIASED-BLOCK-UNCERTAINTY@1. For all 128 output-complement representatives on three bits, every p in {1/8,1/4,1/2}^3, and each physical block mask 1..6, verify the signed spectrum, Parseval, exact Boolean inverse, physical edge influence, child-mixture marginal, and retained-coordinate influence decomposition. This comprises 3456 parent cases, 20736 block cases and 62208 child occurrences. Additionally verify every uniform sign table on n=0,1,2,3 (278 tables). No entropy comparison is performed or claimed.

Assignments x=0..2^n-1 use little-endian bits. The uniform integer Walsh character is (-1)^popcount(x&s), corresponding to cube coordinates 1-2*x_i. The integer transform W has coefficient denominator N=2^n and probability denominator N^2. The biased orthonormal character uses (x_i-p_i)/sqrt(p_i(1-p_i)), corresponding at p=1/2 to the opposite one-bit orientation. Its coefficient differs from W_s/N by (-1)^|s| at uniform bias; squared masses agree. All spectral and pivotal quantities are dimensionless rational probabilities; downstream entropy is in bits. The API separately returns pivotal probabilities and biased spectral influences, rather than conflating their normalizations.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision 2026-10-11-execution-v2. Campaign README, CURRENT_STATUS, CLAIM_REGISTRY and OBSTRUCTION_REGISTRY were read; PACKET_STATUS's B15 records, STREAM_NEXT_ACTIONS and the LaTeX plan's B15 contracts (lines 958-988, A072 lines 966-970) were consulted. BOARD.md was read at stage start, snapshot 2026-10-11 22:05 UTC. The specified Claude B15 STREAM_NOTES.md did not exist; the run records that absence without interpreting it as a mathematical blocker.

A071's REPORT.md, SEARCH_DOMAIN.json and code/search.py were read at runs/20261011T214639Z-fleet05-A071-search-space-design. Its symmetry reduction supplies the chosen family, not an assumed entropy inequality. A016's code/check_addressing.py, lines 14-24, supplies the existing checked integer FWHT, reused verbatim and pinned in source receipts. The new work is the wrapper and rational conversion from its uniform coefficients to the biased centered polynomial; it does not replace the established uniform butterfly engine.

Earlier canonical B05, B09 and B19 run reports were read. B09 sections 2-4 give the biased basis and actual physical mixture definitions. Its section 5(4) tax-necessity inference is flagged in the registry and is not used. Supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were consulted; BLOCK_RESTRICTION_IDENTITY sections 1-3 provide the physical-channel and retained-influence identities. Context papers consulted: threshold_paper_38pp introduction equations (1)-(3), Theorems A/D and product-bias normalization locators; threshold_paper_29pp_earlier_version introduction equations (1)-(3); percolation_spectral_pivotal_entropy_30pp section 1.1 equations (1)-(2), J=sum_i 4p_i(1-p_i)i_i and Theorem 1.1; 31pp earlier version section 1.1 for the same normalization. Their class theorems are context, not proof dependencies. These are scoped consultations, not a claim to have independently reconstructed the papers. out/source_receipts.json pins the local source bytes and consultation scope.

## complete derivation or exact first unsupported line

Let N=2^n and W_u=sum_x f(x)(-1)^popcount(x&u). Orthogonality follows by pairing x with x xor 2^i whenever the character difference contains i. Consequently WHT(W)=N*f, sum_u W_u^2=N^2 for sign f, and the inverse has exactly the input signs. The reused butterfly computes the same character sums; the checker independently compares it with direct character enumeration for every uniform table. If e_i counts each disagreeing undirected i-edge once, the physical influence is 2*e_i/N. Fourier expansion of (f(x)-f(x xor 2^i))/2 retains exactly the characters containing i; Parseval gives Inf_i=sum_{s contains i}W_s^2/N^2. Both sides are computed independently.

For rational interior biases define v_i=p_i(1-p_i). Expanding 1-2*x_i=(1-2*p_i)-2*(x_i-p_i) in the uniform expansion gives the radical-free centered coefficient

    b_s = (-2)^|s| sum_{u superset s} (W_u/N) product_{i in u\s}(1-2*p_i).

Thus f(x)=sum_s b_s product_{i in s}(x_i-p_i), the orthonormal signed coefficient is b_s*sqrt(product_{i in s}v_i), and its squared mass is b_s^2*product_{i in s}v_i. This polynomial expansion follows directly from the finite Walsh inverse and holds for every n and rational interior bias; its general correctness is an elementary identity, not an all-dimensional entropy theorem. The implementation checks all physical inverse evaluations in Fraction arithmetic and their exact membership in {-1,+1}, including every distinct child table. The centered products are orthogonal by independence and centering, so Parseval gives total spectral mass one, also checked exactly.

For coordinate i let Q_i=P_{X_-i}[f(0,X_-i)!=f(1,X_-i)]. The difference d_i=f(1,X_-i)-f(0,X_-i) equals sum_{s contains i}b_s product_{j in s\{i}}(X_j-p_j). Its squared expectation is 4Q_i for sign f. Orthogonality therefore gives

    sum_{s contains i}mu(s) = v_i E[d_i^2] = 4p_i(1-p_i)Q_i.

The engine independently sums the physical edge probabilities over X_-i and compares this result with the spectral marginal. At p_i=1/2 it coincides with ordinary cube influence. All total influences are the sums of their saved coordinate vectors. No biased Fourier coefficient is mislabeled as an integer Walsh coefficient.

For any physical block A, expanding the partial coefficient on B in the centered A-products gives q(t)=sum_{r subset A}mu(r union t)=sum_z P_A(z)mu_z(t). This is orthogonality on A, with the physical branches and inherited biases. All 62208 marginal entries are independently checked via constructed child tables. Averaging the edge pivotal event over the physical assignments in A gives E_z J_i(f_z)=J_i(f) for i in B, where J_i=4p_i(1-p_i)Q_i. This retained-coordinate influence identity is also checked for every block. It is the algebraic input to the nonreusing physical influence ledger; it does not pay the entropy residual.

The A071 spectrum implementation evaluates weighted centered moments directly. Our conversion expands uniform Walsh polynomials and uses physical edge counts. The two methods give exactly identical masses on 3612 distinct parent/child inputs. Extracting only A071's spectrum function for comparison executes no A071 search or logarithm code. This is independent algebraic reproduction by A072; it is not an independent review of A071's logarithm bounds, zero-factor certificates or final entropy verdict.

Named calibration: AND with a dummy third bit and p=(1/8,1/4,1/2) has spectrum (225,7,3,21,0,0,0,0)/256; Q=(1/4,1/8,0); spectral influences (7/64,3/32,0), total 13/64. The A071 minimum-positive witness is +1 except x=3 at p=(1/8,1/8,1/2), block A={2}. Its integer W=(6,2,2,-2,-2,2,2,-2); biased masses (3969,7,7,49,1,7,7,49)/4096; Q=(1/16,1/16,1/64); spectral influences (7/256,7/256,1/64), total 9/128. The two children have spectra (961,7,7,49)/1024 and (1,0,0,0), each with physical weight 1/2. These records allow certified entropy reproduction without guessing phases or branch weights.

No unsupported line is used in the algebraic certificate. The first unsupported global step would be to conclude a dimension-independent entropy payment, a sharper valid endpoint tax, or full FEI from these finite checks. Those implications are not made.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec: FROZEN_SPEC.json was saved before execution. Pilot command, from A072:

    python -X utf8 runs/20261011T220909Z-fleet05-A072-exact-walsh-engine/code/verify.py --pilot

Pilot: 278 uniform tables; 128 biased parents; 768 physical blocks; 2304 child occurrences; 154 distinct spectra matching A071; zero failures; 0.3342712 seconds. Pilot runtime cap 55 seconds.

Full command:

    python -X utf8 runs/20261011T220909Z-fleet05-A072-exact-walsh-engine/code/verify.py

Full: 278 uniform tables; 3456 biased parents; 20736 blocks; 62208 child occurrences and mixture entries; 3612 distinct algebraically checked spectra matching A071; zero failures; 32.7309687 seconds. Full cap 120 seconds, checked after every parent. One serial Python process; estimated RAM below 100 MB, not measured. No job expected above 300 MB, no GPU, no dimension escalation. Arithmetic is Python integers/Fraction throughout the mathematics; perf_counter measures runtime only. Entropy comparisons: zero. Data saved during the run: out/uniform.json, out/grid.jsonl, out/witnesses.json; summary ENGINE_CERTIFICATE.json. Pilot artifacts remain saved separately.

## proof dependencies and changed downstream conclusions

The algebraic certificate is self-contained given Boolean truth tables and integer/Fraction arithmetic. It uses no unreviewed FEI helper or literature entropy theorem. A071's domain and A016's implementation are source artifacts, not accepted mathematical premises. Create one source-complete finite claim A072-EXACT-GRID-ALGEBRA@1, pending independent review. A071's algebraic spectrum layer is independently corroborated; its entropy inequality certification is not accepted by this run. The universal B09 and full FEI statuses remain unchanged. Consumers A073/A074 can use the pinned masses, phases, inverses, edge probabilities and physical branch definitions; A085/A092 can audit the engine without running an entropy search.

## one next mathematical action and independent reviewer

Next: consume a separately versioned sharper singleton tax from B09 and certify its sign on the existing exact grid, preserving the physical-child channel and the factor 4p(1-p). If no revised helper exists, A074 should reconstruct the named minimum-positive witness's entropy margin using these algebraic inputs, rather than enlarge n. Independent reviewers: A085 and A092. A072's baseline engine should be reused after review and reopened only for a changed normalization, concrete error or new family.

## actual persistence receipts or precise save blocker

Saved locally in the requested A072 run directory: REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json with packet_ids=[A072], EXACT_WALSH_INTERFACE.py, ENGINE_CERTIFICATE.json, FROZEN_SPEC.json, code/verify.py, code/finalize.py and out artifacts. Rolling STATUS.md, WORKLOG.md and LEARNED.md updated. out/source_receipts.json pins consulted files; out/manifest.json records run artifact sizes and SHA256 hashes (excluding itself). The finalizer checks the exact protocol field sets, delta equality and the 20 MB limit. Independent review, supervisor copying, mirror verification and adoption are pending, not claimed. All writes are within A072; no shared index or other agent folder was changed.

**Universal bridge:** This stage supports C019 stopping-tree payment by validating its physical spectrum/child-mixture and single-use retained-influence ledger on 20736 actual biased-block cases. It moves no universal entropy bound or constant: the conditional spectral cost and valid bias tax still need a dimension-free, nonreused influence payment, including terminal entropy. The shortest next route is a source-versioned tax/payment candidate on these already certified Boolean inputs, with a rigorous sign or explicit falsifier; repeating the baseline engine or proving another unrelated finite class would not address that missing universal payment.
