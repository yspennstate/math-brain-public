# A016: addressing benchmark and code-cost ledger

## exact target, quantifiers, hypotheses and units

For every integer a >= 0, set N=2^a and let f(x,y)=y_x on a fresh uniform selector block x in {-1,1}^a and N distinct uniform data bits y_u. Reproduce the spectrum, H and I, and compare explicitly defined coordinatewise, complete-set one-root, and conditioned posterior costs as a tends to infinity. Entropy and costs are in bits; I is ordinary total influence. This is a baseline reproduction, not a new FEI theorem. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

The execution protocol was read in full: fei-execution-protocol/2, revision 2026-10-11-execution-v2. Also consulted the campaign README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS and FEI_100_agent_research_plan.tex, especially Endpoint J and A016's acceptance contract. BOARD.md snapshot 2026-10-11 21:38 UTC has no completed B04 baseline. The requested claude/B04/STREAM_NOTES.md did not exist when checked; no lead direction was overridden.

Supplement: CAMPAIGN.md, CLAIMS.md (C008,C009,C020,C035), COUNTEREXAMPLES.md (X012), SEED_LEMMAS.md (complete-reference prior mixture), NATIVE_MAPPING.md, and sources/LOG_ALLOCATION_CURATED.md. Their baseline addressing statements are reused, not presented as novel.

Primary mathematical sources: context/threshold_paper_38pp.txt, Sections 5.2, 5.6 (Proposition 5.5), 5.7 and Section 8's affine-selector addressing example; source_material/reductions/paper/forests.tex, equations forestcost/posteriorforest/outerfractional/addresspressure and Proposition addressforest. The former allows a global scalar root odds parameter lambda=1, while the conditioned forest uses incidence weights lambda_b=1/N. These are different generators and are not silently conflated. The earlier threshold 29-page version's introductory definitions were checked; it is not the source for the later addressing refinement. The percolation 30-page and other 31-page versions' introductory spectral normalization and scope statements were checked; no spatial/percolation theorem is used here. Earlier B05, B19 and B09 run reports were checked for their scopes; none is a proof dependency of this computation. Exact local file hashes are in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

### 1. Exact Boolean spectrum, including a=0

The selector indicator expands as

    1{x=u} = N^{-1} product_j (1+u_j x_j).

Therefore

    f = N^{-1} sum_u sum_{T subset [a]} chi_T(u) chi_T(x) y_u.

The Fourier sets T union {y_u} are distinct because the data coordinates are distinct and disjoint from the selector block. There are N^2 such sets, each coefficient has magnitude 1/N, and all other coefficients vanish. Thus the spectral law is the independent pair U uniform on N labels and T uniform on 2^a selector subsets. Consequently

    H=2a,  |S|=1+Bin(a,1/2),  I=1+a/2,  H=4(I-1).

Each selector has influence 1/2: flipping it selects two independent fair data bits, which disagree with probability 1/2. Each data coordinate has influence 1/N because it matters exactly at its own address. At a=0, f=y_0, H=0, I=1. The ratio H/I=4a/(a+2) increases to 4.

### 2. Actual elementary codes: label sharing is explicit

The codebook, family, dimension and coordinate order are fixed before sampling S. No spectral-law-dependent selection is transmitted. All codewords for a fixed a have known parsing rules.

* Repeated-label complete code: first transmit the a-bit selector-subset mask T, then transmit the a-bit address u once for each coordinate in S, in selector order followed by the data coordinate. The decoder knows s=1+|T| after the mask and checks the labels agree. Its length is a+a*s. The code is prefix-free: different masks have different fixed-length prefixes, and for a fixed mask the remaining length is fixed. The exact expected cost is a(2+a/2), so cost/I = a + 2a/(a+2) = a+2+o(1). Its repeated-label component alone is a*I, with ratio a. Omitting the mask describes only a label charge, not a complete code.
* Complete-set one-root code: transmit u once in a bits and then the a-bit mask T. Length is exactly 2a; its ratio is 4a/(a+2), tending to 4. The uniform reference Q(T union {y_u})=1/N^2 has total mass one. This code achieves H exactly. For a=0 the empty word decodes the unique set {y_0}.
* Posterior version of this elementary code: the latent witness is (u,T). Its posterior given S is a point mass, so H(witness|S)=0. The variational expression E[-log q(witness)]-H(posterior) equals 2a exactly. There is no extra label credit: S itself identifies u.

These definitions show the quadratic-to-linear repair without claiming that an inefficient code is necessary.

### 3. The source's coordinatewise fractional pressure

The canonical DNF has h_b=[x=b and y_b=1], pi_b=1/(2N), and R_b=[a] union {y_b}. For a>=1 the selector incidence constraints are sum_b lambda_b<=1. At a selector j, the unique true endpoint of a pivotal edge forces the witness gate; symmetry gives q_{j,b}=1/N. At data coordinate y_b, its witness is deterministic. In the source's outerfractional bound the nonnegative pressure is

    P(lambda) = (48/5) sum_j Inf_j log2(sum_b sqrt(q_{j,b}) lambda_b^{-11/48}).

Convexity of t^{-11/48} minimizes every selector sum at lambda_b=1/N, and convexity of -log minimizes the sum of data costs at the same weights. Saturation is optimal because increasing a weight decreases these costs. Hence

    P_min=(7/2)a^2+(11/5)a,
    P_min/I=7a-48/5+96/[5(a+2)] ~ 7a.

For a=0 there is one data gate, lambda_0=1, and pressure zero, agreeing with this polynomial. P_min is a term of a complete upper bound, not a Kraft-normalized code length by itself. The full bound (41+P_min/I)*I has the same divergent leading ratio 7a. An additional conditioned log Z term is only linear in a and does not remove this quadratic growth.

### 4. Exact single-run queue cost and its conditioned posterior

Use one common regular-gate order: selectors first, data last. Put d=a+1, gamma=6/5, theta_s(r)=min(1,(s/r)^gamma),

    E_{d,s}=e_s(theta_s(1),...,theta_s(d)),
    W_s(B)=product_{r in B} theta_s(r),  B=T union {d},  s=|B|.

Let L_a=E_T[log2(s(s+1))+log2(E_{d,s})-log2(W_s(B))]. This is a finite exact real expression (algebraic weights and logarithms), not a floating-point identity.

The one-root run chooses only gate u, its entire set B, and no children. With the threshold paper's scalar lambda=1, let Lambda_0=N log2(1+1/(2N)). The actual probability of this run is

    q_0 = 2^{-Lambda_0}/(2N) * W_s(B)/[2 s(s+1) E_{d,s}].

Thus its complete expected negative logarithm is

    C_queue=Lambda_0+a+2+L_a.

For the conditioned forest generator, fix incidence weights lambda_b=1/N and put

    Lambda_f=N log2(1+1/(2N^2)),
    Z_f=1-(1+1/(2N^2))^{-N}.

Its same one-root run, after nonempty-root conditioning, has probability

    q_* = 2^{-Lambda_f}/Z_f * 1/(2N^2) * W_s(B)/[2s(s+1) E_{d,s}],

so

    C_posterior,one-root=Lambda_f+log2 Z_f+2a+2+L_a.

The posterior here is over the specified family of one-root partition runs; exactly one such run outputs each spectral S, so its entropy subtraction is zero. At a=0, L_0=1, C_queue=log2 12 and C_posterior,one-root=2. These positive overheads belong to the queue generator, whereas the optimal elementary code has length zero.

This does NOT claim that the posterior over ALL partition forests is a point mass. When T is nonempty, selector coordinates may be assigned to other gates and produce additional distinct multi-gate partition runs. Optimizing that larger family may improve the reference. The exact finite variational formula is -log2(sum_{r in chosen family} q_*(r)); counting abstract descriptions of the same actual run several times is invalid. No all-partition optimum is claimed here.

### 5. Exact asymptotic constant for these literal queue costs

Define w(t)=1 for 0<=t<=1/2, and w(t)=(2t)^{-gamma} for 1/2<t<=1. There is a unique z>0 satisfying

    integral_0^1 z*w(t)/(1+z*w(t)) dt = 1/2.

Set

    G=integral_0^1 log2(1+z*w(t)) dt - (1/2)log2 z
      - (1/2)integral_0^1 log2 w(t) dt.

Then L_a/a -> G, and both C_queue/I and C_posterior,one-root/I tend to 2+2G. In particular,

    4 <= 2+2G <= 4+gamma*(1-1/(2 ln 2)).

This is an exact integral-defined constant, between 4 and approximately 4.3344; the decimal is illustrative.

Proof of the coefficient limit: on any sequence s/d -> 1/2, choose z_d so sum_r z_d theta_s(r)/(1+z_d theta_s(r))=s. The weights stay in a fixed compact subinterval of (0,1], so z_d stays bounded above and away from zero. Riemann sums converge, giving z_d -> z and

    log2 E_{d,s} = sum_r log2(1+z_d theta_s(r))-s log2 z_d + log2 Pr(K=s),

where K is the sum of independent Bernoulli variables with odds z_d theta_s(r) and mean s. The last term is o(d): Chebyshev gives an atom of probability at least c/sqrt(d) within O(sqrt(d)) of s; adjacent atom ratios are bounded above and below by constants in that central window, because

    min(odds)*(d-k)/(k+1) <= Pr(K=k+1)/Pr(K=k)
                                    <= max(odds)*(d-k)/(k+1).

This inequality follows by counting each (k+1)-subset k+1 times in elementary symmetric sums. Moving from that atom to s costs O(sqrt(d)) bits. This proves the coefficient limit without assuming a local central limit theorem.

Under the uniform selector-subset law, s/d ->1/2 exponentially in probability. Replacing theta_s by theta_{floor(d/2)} changes each log weight by at most gamma*|log2(s/floor(d/2))|, uniformly in r. Thus the expected selected log-weight sum, divided by d, tends to (1/2)integral log2 w; the always-present data coordinate contributes only O(1). The exceptional binomial tails contribute o(d), since every relevant cost is O(d log d). The size-choice logarithm is O(log d). Therefore L_a/a -> G. Finally Lambda_0=O(1), Lambda_f=o(1), and log2 Z_f=-a-1+o(1), proving the stated limits.

For the constant bounds, the uniform distribution on (s-1)-subsets of the a selectors has entropy log2 binom(a,s-1), and Gibbs applied to the subprobability reference B -> W_s(B)/E_{d,s} gives average subset cost at least that entropy. Averaging over s gives a-H(Bin(a,1/2)), hence G>=1. Conversely E_{d,s}<=binom(d,s) since theta<=1, and the preceding selected-weight calculation gives G<=1-(1/2)integral log2 w. Direct integration gives integral log2 w=-gamma*(1-1/(2ln2)).

### 6. The coarse conditioned-posterior theorem cost

For the same one-root assignment, M=1 and s=kappa, so the order-multiplicity and allocation-congestion terms vanish. Write

    R_a=(1/2) sum_{r=1}^a E_{K~Bin(r-1,1/2)} log2(r/(K+1))
           + E_{K~Bin(a,1/2)} log2((a+1)/(K+1)).

The forestcost expression is exactly E B_lambda = 2a+1+gamma R_a. The posterior entropy remains zero. Its residual and full theorem upper bound are

    D_a=Lambda_f+log2 Z_f+2a+1+gamma R_a,
    U_a=K_ref I+D_a,  K_ref=3+2log2 3+log2(6e).

The identity E[1/(1+Bin(r-1,1/2))]=2(1-2^{-r})/r and Jensen give R_a<=I. A binomial concentration argument gives E log2(r/(K+1))->1 (the exponentially small lower tail, with maximum log2 r, is negligible). Cesaro averaging then gives R_a/I->1. Therefore

    D_a/I -> 16/5,
    U_a/I -> K_ref+16/5.

At a=0, R_0=0 and Lambda_f+log2 Z_f=-1, so D_0=0. U_a is a coarsened theorem RHS; it is neither the literal queue cross-entropy nor the entropy of the spectral law. Discarding its K_ref I term would confuse the residual with the complete cost.

The threshold paper's separate complete one-root upper envelope is

    V_a=Lambda_0+a+2+E log2(s(s+1))
             +log2(6e) I+gamma E[s log2(d/s)],

and V_a/I -> log2(6e)+16/5. The source's finite H<10 I estimate uses further uniform inequalities and should not be misreported as an exact asymptotic queue cost.

### 7. Paid prior selection

No scale prior is needed for the fixed references above: they may be assigned weight one. If one instead uses the supplement's dyadic prior w_j=2/[3(|j|+1)(|j|+2)], the charge log2(1/w_j) must be added. For scalar lambda=1, j=0 costs log2 3, whose ratio to I vanishes. A global scalar lambda=1/N corresponds to j=-a and costs log2(3/2)+log2(a+1)+log2(a+2), also o(I). This latter observation applies to the scalar family; vector incidence weights cannot silently be substituted into a different reference family.

There is no unsupported line in the stated addressing derivation. The first unsupported universal extension would be: for every Boolean function, an admissible complete posterior reference of expected cost O(I) exists. Addressing supplies no proof of that extension.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before computation. Executed from the A016 folder:

    python -X utf8 runs/20261011T213934Z-account05-A016-addressing-benchmark/code/check_addressing.py

The checker passed 18,734 assertions, zero failures, measured script runtime 1.0430493 seconds. Integer FWHT on complete actual Boolean truth tables covers a=0,1,2,3 (2,8,64,2048 rows), and compares every Fourier coefficient squared and every edge influence with its expected exact Fraction value. A separate direct spectral/code model covers a=0..6, including decoding and exact expectations. Rational atanh-series intervals (40 terms with a proved geometric remainder and signed exponent handling) certify rank costs at a=0,1,2,4,8,16,32, including the exact reciprocal-binomial identity and R_a<=I. Saved output: out/CHECK.json. Decimal renders are only convenient summaries of those exact intervals. The all-a formulas and limits rest on the proofs above; no finite-to-infinite extrapolation or floating-point certificate is used. No heavy job, GPU or dimension escalation was used.

## proof dependencies and changed downstream conclusions

The Walsh spectrum and elementary-code statements are self-contained. The named pressure and forest cost are evaluated under the exact source definitions in forests.tex; the generator probabilities are reproduced above. No claim registry theorem is required to conclude H and I. These baselines close A016's reproduction target, subject to independent review. They clarify for A006/A008 that the address name is forced by the data coordinate: on this single-root family the repair comes from paying it once, not from subtracting a nonexistent label posterior. A015/A076 should use exact H/I->4, while retaining the distinction between bad coding and an actual FEI counterexample.

## one next mathematical action and independent reviewer

Independent reviewers: A090 and A091, as specified by the packet. Reconstruct the literal queue probability and the coefficient asymptotic, especially root conditioning and the a=0 endpoint. After this baseline is accepted, consume B04's next useful shared-data dependency (A018): compute a fixed reference's genuine multi-run posterior when more than one branch supports the same data Fourier character, retaining coherent interference. Do not restart this baseline without a concrete objection.

## actual persistence receipts or precise save blocker

Saved locally inside the assigned immutable run folder: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, ADDRESSING_BASELINE.tex, ADDRESSING_CONTROL.json, FROZEN_SPEC.json, code/check_addressing.py and out/CHECK.json. out/SOURCE_RECEIPTS.json records read-source SHA256 hashes and out/PERSISTENCE.json records saved artifact hashes and schema checks. The three rolling A016 files are updated. No shared tree, other agent folder, brain store, git repository, external service or public artifact was modified. Supervisor copying, independent review and mirror verification are pending and are not claimed as receipts.
