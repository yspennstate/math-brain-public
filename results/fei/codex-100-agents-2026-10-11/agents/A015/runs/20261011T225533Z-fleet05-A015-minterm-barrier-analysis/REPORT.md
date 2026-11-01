# A015 / B03: minterm label barrier, with activation normalization

## exact target, quantifiers, hypotheses and units

For every indicated finite Boolean family, quantify the charged label component in the Section 5 queue witness at the **fixed scale lambda=1/k**:

`C_lab(f,D) = sum_{A != empty} fhat(A)^2 min_tau |F_tau(A)| log2 k`.

Here D is a specified DNF, R_l is the physical support of term l, tau assigns every j in A to one term containing j, and F_tau is the set of used terms. Every such assignment has the source-component spanning forest required by Proposition 5.5. Define separately the allocation pressure `P_sub(A,tau)=sum_l s_l log2(|A intersect R_l|/s_l)`, whose coefficient in the proof is 6/5. Empty sets cost zero. All expectations below are **unconditioned** squared-Fourier expectations, and all logarithms are in bits. Conditional expectations given nonempty A must be multiplied by v=Var(f).

Two DNF conventions must be distinguished. FULL CELLS means one full-width signed conjunction for every input in the true event. PRIME means the canonical minimal positive conjunctions for the monotone examples. Calling both 'minterms' hides the tribes contrast.

Main outcome: fixed-scale labels already obstruct a dimension-independent payment for majority, even after optimal whole-set gate assignment. Prime tribes has zero label charge. Sparse activation does not make the majority barrier disappear. These are coding-component obstructions, not FEI counterexamples or lower bounds on every optimized reference. One bundled scoped diagnostic is submitted for review; no new universal representation lemma is asserted.

## sources actually read, revisions and theorem locators

Execution protocol `fei-execution-protocol/2`, revision `2026-10-11-execution-v2`, read in full; README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS and STREAM_NEXT_ACTIONS inspected. Plan source: B03/A015 and its execution contract, plus A016/A021/A076 interfaces. B03 STREAM_NOTES v1 (2026-10-11 22:30Z) and BOARD (2026-10-11 22:57 UTC) direct this work to the three terms (L),(S),(R). No shared files were changed.

The 38-page threshold TXT has SHA256 `36a5953075759ea1085b005cb92352d364693c45a37fc35260d3b39f21cde20c`. Read its regular-function definition, Theorem A, Section 5 (especially equations 31,32,35, Proposition 5.5 and the fixed-scale refinement), and Proposition 8.9 / activation-equivalence corollary; verified these interfaces against supplemental `baseline/current-threshold-paper.tex`. The earlier 29-page TXT (`056e86b12567f3ba766d4aaeb8beb97042151eee3094c1bcd0d27e6ca32a1007`) was inspected for theorem/version differences, not used for joint-witness or activation claims. The percolation 30-page TXT (`d33469ce69f21137a9620927df39c33ff65ef45f54f8be2fec8a55210d46c8b6`) and other 31-page version (`4f09cf6e96559f5c7bbbe67e4f15ba34017770fc498f4bc178c928419189e00b`) were inspected at their theorem/entropy interfaces; no percolation theorem is a proof dependency here. Those papers' spatial hypotheses do not pay arbitrary DNF labels. This is a targeted source intake, not a claim to have independently audited every proof in those papers.

Supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were consulted, particularly C008/C013/C020, the complete-reference prior lemma, and X011/X012. Source collection headings and the overlap-product correction were inspected. Earlier B05/B09/B19 run reports were located and their scopes inspected; no new proof depends on their unreviewed claims. A076's existing report is the threshold/tribes baseline: entropy formulas below are calibration, not another claimed discovery of tribes FEI. The new delta is their comparison with the minterm label/allocation charges. Source hashes and intake locators are retained in `out/SOURCES.json`.

## complete derivation or exact first unsupported line

### 1. The fixed-scale component and why it is not a universal lower bound

At lambda=1/k, each forest root contributes log2 k as part of `log2(1/(lambda*pi_l))`; every child label is bounded above by log2 k. Thus the explicit refined bound charges exactly the formal component `|F| log2 k`, because roots plus edges equals |F|. The actual child contribution is log2 d(j_e), which can be smaller. This report minimizes the formal component over complete assignments. It does not replace it by the weaker coordinatewise `|A| log2 k`.

The complete law also has `h2(v)+v Lambda_lambda`, root rarity, subset normalizers/ranks, size choices, and attachments. It can sum probabilities of different successful witnesses. A lower bound on this **charged expression** is not a lower bound on `log2(1/Q(A))`, on entropy, or on all scales. Changing scale or erasing labels is permissible only in the full cost. The first unsupported line of any proposed universal conclusion would be: 'for every Boolean f there exists a complete normalized representation/reference whose expected total cost is <=K I(f)'. Nothing here proves it.

### 2. Majority: the label obstruction survives whole-set assignment

Let n=2a+1, t=a+1, a>=0; the true event is at least t positive bits. Its prime DNF has one term for each t-subset, each support of size t. The number of terms is N=binom(n,t), and the exact read is k=binom(n-1,t-1). These terms are mandatory in any exact DNF in the following sense: at the input whose positive set is exactly a given t-set, any satisfied implicant must require all t of those positive literals. Otherwise turn every unconstrained positive literal negative and obtain a false input satisfying that term. Distinct t-sets therefore require distinct terms. Each coordinate occurs in at least binom(n-1,t-1) terms in every DNF, even allowing negative literals or redundant terms. Such additions cannot make the formal fixed-scale label component less than log2 k because every nonempty spectral set needs at least one used term.

For the canonical prime DNF, the exact optimal count for a set A of size d is `ceil(d/t)`. The lower bound is support size. For the upper bound, partition A into groups of size at most t and extend each to a t-set; all extended groups are available terms. Since n<2t, this is one for d<=t and two for d>t. Thus, writing W_d=P(|S|=d) and T_n=sum_{d>t} W_d,

`E min |F| = 1+T_n`,

`C_lab(Maj_n,prime) = (1+T_n) log2 binom(n-1,t-1)`.

This is exact, not a bound using E|S|. Only odd levels have mass. A completely explicit spectrum is provided by

`b_d = 2^(-n) sum_{j=0}^n sign(j-t) sum_h (-1)^h binom(d,h) binom(n-d,j-h)`,

where sign(j-t) is +1 for j>=t and -1 otherwise (overall sign/input reversals do not affect W). Then `W_d=binom(n,d)b_d^2`. Equivalently, put `c_j=binom(2j,j)/4^j`; for d=2j+1,

`W_(2j+1) = [n/(2j+1)] c_a c_j c_(a-j)` (0<=j<=a).

One derivation of this last formula: for a chosen coordinate, the majority derivative is the indicator that the other 2a bits have exactly a positives. Its coefficient on 2j chosen bits is `(-1)^j c_a binom(a,j)/binom(2a,2j)`, obtained by taking the coefficient of x^a in `(1-x)^(2j)(1+x)^(2a-2j)` and dividing by 2^(2a). Squaring and multiplying by binom(n,2j+1), followed by factorial cancellation, gives the displayed W. The convolution identity `sum_j c_j c_(a-j)=1` then yields

`I(Maj_n)=n c_a = n binom(n-1,t-1)/2^(n-1)`.

Markov gives `T_n<=I/t=O(n^(-1/2))`. Wallis/Stirling gives `I~sqrt(2n/pi)` and `log2 k=n-1-(1/2)log2 n+O(1)`. Consequently

`C_lab/I ~ sqrt(pi*n/2) -> infinity`.

Actual entropy is exactly `H(W)+sum_d W_d log2 binom(n,d)`, and is Theta(sqrt(n)). The upper bound is baseline Theorem A, H<=C_reg I. For completeness a crude analytic lower bound avoids numerical extrapolation: c_l>=1/(2sqrt(l)) for l>=1 (square and induct using c_(l+1)/c_l=(2l+1)/(2l+2)). For a>=8 and integers ceil(a/4)<=j<=floor((a-1)/2), W_(2j+1)>=1/(8a^(3/2)); there are at least a/8 such j. Their degrees satisfy a/2<=d<=a and log2 binom(n,d)>=d>=a/2, since binom(n,d)>=(n/d)^d and n/d>=2. Therefore H>=sqrt(a)/128. The growing label/influence ratio is a code artifact while H/I stays bounded.

The allocation pressure is not the main obstruction. Among assignments using the minimum number of terms, its minimum is zero for every d<n. For d<=t use a term containing A. For t<d<n, split A into two parts with sizes each at least `d-t+1` and at most t, then fill both terms with coordinates outside A; their intersections with A are exactly their assigned parts. Such a split exists since d<=2t-2. For d=n every support intersection is t. Concavity of `s log2(t/s)` shows the minimum over partitions with s<=t is attained by sizes t,t-1: transferring size toward an endpoint cannot increase the sum. Thus

`E min P_sub = W_n (t-1) log2(t/(t-1)) <= W_n log2 e = O(1/n)`

(n=1 gives zero separately). The subsets giving minimum pressure also have minimum |F|. In contrast the generic bound is I log2 k. Neither allocation nor paying the same name once per whole set removes majority's remaining fixed-scale label bill. The generic (R) estimate still has `(24/5)I log2 k`; this report does not pay that term in this DNF.

The full-cell DNF has N=k=2^(n-1), all supports [n], and a one-gate assignment for every A. Its exact formal label charge is n-1; allocation pressure is zero. A direct n-bit characteristic-vector subset code would add a dimension bill; a size-first uniform code has cost `log2(d(d+1))+log2 binom(n,d)`. Its expected binomial term is already the conditional entropy in the displayed symmetric entropy identity. Full-cell naming is therefore distinct from coding the output set.

### 3. Tribes: prime supports remove the label term

Let T_(w,s) be the OR of s disjoint width-w all-positive tribes, w,s>=1. Put z=2^(-w), q=1-(1-z)^s and choose Boolean sign g=1-2T. Its canonical prime DNF has s disjoint supports and k=1. For a spectral set A, write J(A) for the number of hit tribes. Each hit tribe is mandatory and sufficient, so `min |F|=J(A)`; all gate-owned subsets have `|A intersect R_l|=s_l`. Therefore

`C_lab=0`, `P_sub=0`,

`E J=4s z(1-z)^s`, `I(g)=2sw z(1-z)^(s-1)`.

To verify the expectation, write `g=2 product_l (1-A_l)-1`. Every nonempty coefficient on a set hitting j tribes equals `2(-z)^j(1-z)^(s-j)` up to oriented signs, with multiplicity `binom(s,j)(2^w-1)^j`. Summing its squared mass gives v=4q(1-q); summing hit counts gives E J. The empty coefficient is 1-2q. This proves the normalization and count formulas directly.

The exact entropy is

`H = (1-2q)^2 log2(1/(1-2q)^2) - 2v + 2w E J + 2 log2(1/(1-z)) (s v-E J)`

with 0 log(1/0)=0. In the standard regime w->infinity, sz->lambda in (0,infinity), I~2lambda exp(-lambda)w and H/I->4 (A076 baseline). No entropy asymptotic is needed for the label obstruction.

The full-cell DNF instead has `N=k=2^(ws)-(2^w-1)^s=2^(ws)q` terms, all support [ws]. Consequently `E|F|=v`, `C_lab=v log2 N`, allocation pressure zero. In the same regime, `C_lab/I ~ 2(1-exp(-lambda))s/lambda -> infinity`. This large spurious charge disappears completely on passing to the prime DNF. A whole-set single-name code alone therefore suffices for neither representation: first the right structural supports must be chosen.

### 4. Arbitrary rare activated cores: exact mass, influence and dimension charge

Let g be any Boolean function on m declared data bits, q=P(g=-1)>0, and let A_r be a point indicator on r>=1 fresh controls, p=2^(-r). Define F=1+A_r(g-1). For data B!=empty and arbitrary control U, `Fhat(B,U)=p epsilon_U ghat(B)`. For empty data and U!=empty it is `-2pq epsilon_U`; the empty coefficient is 1-2pq. Thus

`v_F=4pq(1-pq)`, `I(F)=p(I(g)+2rq)`.

The nonempty-data sector has mass p Var(g), not p^2 Var(g): there are 2^r control sets. The control-only nonempty sector has mass `4p q^2(1-p)`. This is the normalization error to avoid when importing sparse-core intuition.

Full-cell terms for the activated event consist of its one fixed control point and one of the `N_-=2^m q` negative core assignments; every support is [r+m], so k=N_-, `min|F|=1` on nonempty A. Exactly

`C_lab(F,full cells)=4pq(1-pq) log2(2^m q)`,

`C_lab/I(F)=4q(1-pq) log2(2^m q)/(I(g)+2rq)`.

For balanced cores this becomes `(2-p)(m-1)/(I(g)+r)`. Allocation pressure is zero. Subset ranks, root rarity `(m+r)` per root, and normalization remain outside this label calculation.

For comparison with the actual target, if balanced,

`H(F)=p H(g)+2rp(2-p)+(1-p)^2 log2(1/(1-p)^2)`.

This is Proposition 8.9, independently checked coefficient by coefficient by the pilot. For general q the direct exact expression is

`H(F)=p H^+(g)+2rp Var(g)+4p q^2(1-p) log2(1/(4p^2 q^2))+(1-2pq)^2 log2(1/(1-2pq)^2)`.

No balanced approximation is used for the 810 arbitrary-core activation cases.

In particular take an m-bit odd majority core and r=ceil(2log2(m+1)). Then p->0, minority probability p/2->0, I(F)->0, but the full-cell charge/influence ratio is Theta(sqrt(m)). Its actual H/I stays bounded by the regular-gate theorem below. If r>>m the displayed label ratio vanishes; r cannot be silently omitted in classifying extreme regimes. Padding a fixed balanced core with dummy data bits increases this full-cell label charge linearly in padding while H(g) and I(g) remain unchanged; this makes the representation dependence unmistakable.

For the prime activated-majority DNF the supports are all r controls plus a t=(m+1)/2-subset of data. Every control occurs in N=binom(m,t) terms, and each data coordinate in binom(m-1,t-1); hence k=N. For a nonempty spectral set `(B,U)`, the exact minimum count is `max(1,ceil(|B|/t))`. Summing the two sectors gives

`E min|F|=2p-p^2+p T_m`,

`C_lab/I(F)=(2-p+T_m) log2 binom(m,t)/(I(Maj_m)+r)`.

Again this diverges as Theta(sqrt(m)) for the sparse choice r=ceil(2log2(m+1)). Assign all U controls to the first of the at most two used terms. Using the preceding majority data partition, pressure is zero for |B|<=t, at most r log2 e for t<|B|<m, and at most (r+1)log2 e at |B|=m. Thus `E P_sub<=p T_m(r+1)log2 e`. This is an upper bound for an explicit minimum-count assignment, not a claim of exact minimum activated pressure. The surviving label obstruction is not created by excessive subset congestion.

For completeness, activate tribes using their prime terms. If J(B)>0 the count is J(B), and if B=empty,U!=empty it is one. Controls have read s, data have read one, so k=s. Exactly

`E min|F|=4p q^2(1-p)+4p s z(1-z)^s`,

`C_lab/I(F)=[4q^2(1-p)+4s z(1-z)^s] log2 s/[2sw z(1-z)^(s-1)+2rq]`.

For sz->lambda, r->infinity and r=o(w), this ratio tends to `2[ (1-exp(-lambda))^2+lambda exp(-lambda)]/[lambda exp(-lambda)]`. More generally if r/w->rho>=0 and p->p_* it tends to `4[(1-exp(-lambda))^2(1-p_*)+lambda exp(-lambda)]/[2lambda exp(-lambda)+2rho(1-exp(-lambda))]`; log2(s)/w->1. Fixed r must retain p_*=2^(-r); rho>0 forces p_*=0. It stays bounded in these regimes, unlike the full-cell representation. Assign controls to one hit tribe. Other hit tribes contribute `b_l log2(1+|U|/b_l)<=|U| log2 e` each, giving `E P_sub<=p r log2(e) E_g J`. This explicit residual bound does not purport to pay all activated-tribes rank/normalization costs for arbitrary parameters.

### 5. Structural grouping repairs majority; a universal grouping lemma is still unpaid

Majority is a single regular gate. Activated majority is also regular: orient the event as increasing, put all controls before all data, and regard coordinates within each group as equivalent. If two inputs differ only by moving a 1 from data to a control, either another control is 0 and both outputs are false, or the input with this control 0 is false while the other is possibly true. Thus every control is at least as desirable as every data bit; data are exchangeable under the threshold. This is a proof of regularity, independently checked in the pilot. A one-gate representation has k=M=1, |F|=1, and zero (L) and allocation pressure. Theorem A pays the remaining complete entropy with C_reg<8.937. These are baseline gate-class consequences, not a new full-FEI case claim.

The precise missing feature in majority's fixed-scale DNF charge is **quotienting interchangeable minterms into a structural gate, or obtaining an equivalent posterior refund with all rarity/normalization bills retained**. The exact unpaid formal bill is `(1+T_n)log2 k`, already Theta(n), while its influence is Theta(sqrt(n)). Merely paying each label once per set improves I log k to this bill and still fails. Tribes shows that smaller physical supports can supply the needed grouping. Arbitrary cores do not come with a regularity order, cheap grouped gates, or a proved posterior refund.

An important algebraic sanity check: if N full-cell terms have the same support, same chosen rank order, and equal pi=2^(-d), the N distinct one-root/no-child runs selecting a fixed output subset have identical non-root factors. Their summed root mass is `N * 2^(-Lambda_lambda) lambda pi`. At lambda=1/N this cancels the explicit log2 N label charge exactly. The remaining factor is pi: the root rarity still costs d, in addition to Lambda and the subset factors. This is a valid finite multiplicity refund, not a universal proof or an assertion that optimal posterior cost must still be >=d. It explains why no raw-label barrier can be promoted to a lower bound on the complete optimized law. A fixed scale prior, root term, subset normalizers and posterior entropy must be assessed together as in C008 and the seed complete-reference lemma.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: `out/FROZEN_SPEC.json`, written before the pilot. Command from A015:

`python -X utf8 runs\20261011T225533Z-fleet05-A015-minterm-barrier-analysis\code\check.py`

Output `out/validation.json`: PASS, **866 cases, 41,726 exact assertions**, maximum dimension 12, observed Python computation time 1.526478 seconds. Full truth tables, integer FWHT, rational Parseval, rational direct-edge influences, every activation coefficient, sector masses, majority Krawtchouk levels, exact minimum cover dynamic programming through n=7, and activated-majority desirability are checked. All nonconstant Boolean cores at m=1,2,3 are included without symmetry reduction; each has r=1,2,3. Majority n=1,3,5,7,9 and tribes w,s=1,2,3 provide the remaining controls. The frozen estimate was 30 MB and 60 seconds; no >300 MB job or heavy search was run.

All logged label costs are rational coefficients times log2 of exact integers. Decimal entropy and label/influence values in output are explicitly diagnostics; no numerical inequality is promoted to proof. Infinite-family conclusions above follow from the displayed analytic formulas and inequalities. A second frozen validation (`out/SYMBOLIC_SPEC.json`) runs `python -X utf8 runs\20261011T225533Z-fleet05-A015-minterm-barrier-analysis\code\symbolic.py`. It passed **5,021 additional exact assertions** in 1.127855 seconds: all 810 activation entropy identities and balanced specializations are checked in a formal log2-prime basis, tribes entropy and majority level entropy are checked exactly, minimum allocation pressure is compared by rational products on all 38 nonempty sets at n=3,5, and closed majority/Wallis identities are checked at all 64 odd dimensions through 127 without truth-table escalation. Total exact assertions: **46,747**. Direct Walsh sums supply a different computational reconstruction from the first FWHT helper; this is author verification, not independent review.

## proof dependencies and changed downstream conclusions

All combinatorial and activation label identities are elementary and proved here. Actual uniform H/I upper comparisons use baseline Theorem A, with the regularity hypothesis proved explicitly for activated majority. Tribes entropy asymptotics are baseline calibration already handled by A076. No A011-A014 candidate or projective-plane result is a premise; that work is not repeated. C013's ratio-preserving arbitrary-core reduction is retained as a scope guard.

Downstream correction for A011/B03: a universal representation lemma cannot infer expected cost O(I) from `|F|<=2`, low influence, or sparse activation. Even unavoidable DNF read and optimal gate count may leave a fixed-scale label bill Theta(sqrt(n)) times influence. Conversely, it cannot infer impossibility of posterior compression from this bill: explicit duplicate-root summation refunds it. A promised code must state its reference scale, output ambiguity/refund, rarity and normalizer together. B03's generic rank charge is a separate unpaid obligation.

## one next mathematical action and independent reviewer

Next: reconstruct A012's complete posterior-erased activated-literal witness (including v Lambda and the remaining root rarity) and check whether its refund extends from a dictator to the grouped activated-majority reference. Use the exact sector masses above; do not restart the majority/tribes baseline or create another broad candidate while B03's review queue is full. Independent reviewers: A086 primary, A094 adversarial. Consumers: A011, A012, B03 lead, B20. The queue/refund extension is a new dependency rather than a second attempt at the same minterm diagnosis.

## actual persistence receipts or precise save blocker

All artifacts are local under the authorized A015 stage directory: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, MINTERM_BARRIERS.tex, COMPRESSION_REQUIREMENTS.md, code/check.py and out files. Rolling STATUS/WORKLOG/LEARNED are current. `out/RECEIPTS.json` records reread hashes and schema checks, excluding its own hash. No GitHub mirror verification, independent acceptance, or supervisor adoption is claimed. There is no local save blocker; copying to shared repositories belongs to the supervisor.

## Universal bridge

This stage moves **C020 whole-set witness cost** by resolving the A015 representation obstruction: exact fixed-scale label bills are computed for majority, tribes and arbitrary sparse activations; majority's bill remains unbounded relative to influence after optimal whole-set assignment, whereas structural regular-gate grouping removes it. The allocation term is separated and the remaining rank, rarity, normalization and posterior bills are explicitly retained. It proves no positive universal constant and excludes no optimized complete reference. The shortest next route to full FEI is to reconstruct A012's proposed posterior refund with these exact activation sectors and test its transfer to grouped references, because that addresses the unpaid universal compression mechanism instead of proving another isolated threshold/tribes case.
