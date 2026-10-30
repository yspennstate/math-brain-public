# exact target, quantifiers, hypotheses and units

ACCEPT_AT_STATED_SCOPE: A050-OUTPUT-CONDITIONAL-TAX-REPAIR@1, source run 20261013T212442Z-fleet05-A050-repair-with-scope. Its half-output-conditional transcript refund is valid for every finite deterministic physical singleton stopping tree under a fixed independent interior product law, with no repeated coordinate on a path. For actual output Y=f(X), transcript Pi and node weights w_v, define c_v=H(X_i|Y,history=v). Then

    sum_v w_v[tau*(p_i)-c_v/2]_+ <= I(Pi;Y)/2 <= I_phys(f)/2,
    sum_v w_v tau*(p_i) <= I_phys(f)/2+H(Pi|Y)/2.

The sharp scalar tau* is the two-basis angular uncertainty loss defined in the source. The smallest nonnegative bank coefficient lambda in a universal bound A_T<=C I_phys+lambda H(Pi|f), with finite fixed C and essential computing trees, is 1/2. This is a scoped tax/refund theorem; compatible spectral funding and terminal Fourier payment are explicitly unpaid.

New contributed claim, pending independent review: for every such stopping tree on the uniform cube, in the coherent root-spectral/physical coupling, let S0 be the root Fourier set, R=I(f)-E I(f_leaf), and C_T=H(Pi|Y)-H(Pi|S0). Then

    C_T=sum_v w_v J_v-I(Pi;Y),
    -I(Pi;Y)<=C_T<=(2/ln2)R-I(Pi;Y).

In particular [C_T]_+/2<=R/ln2. This gives a quantitative signed conversion price, not a free conditional bank. Entropies are bits, J_v is the actual physical-child/spectral mutual information, and R is consumed uniform physical influence, counted once. The new bound does not cover arbitrary additional reference side information or resets.

# sources actually read, revisions and theorem locators

Read BOARD.md (supervisor snapshot 2026-10-13 22:25 UTC), B19 STREAM_NOTES.md v2 dated 2026-10-11 23:35 UTC, and A092 STATUS.md. The lead's A046/A047@1 targets were completed in the prior two stages. The current board records A050's newer output-bank repair and A046's existing independent review, so the earlier equal-magnitude-only target was updated to this useful new payment dependency. This stage supplies a requested independent challenge and a quantitative next interface; it does not restart the old endpoint census.

Re-read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2. The remaining board stream sections were read to avoid superseded finite census and scalar-tax jobs. Prior campaign and manuscript readings remain the stage-1 source context; no new external theorem, web research or priority claim is used.

Actually read: A050 REPORT.md, PROOF.md sections 1-7, CLAIMS.json, FROZEN_SPEC.json and out/CHECK.json; A048-SHARP-TAX-PAYMENT-SCOPE@1; A046's 20261013T215251Z review CLAIMS.json; A037-PHYSICAL-SPECTRAL-COMMON-LIFT@1 and its finite common-law interface; supplemental sources/ERASURE_REDUCTION.md sections 1-4. Byte hashes are in out/SOURCE_MANIFEST.json. No author's program was replayed as the independent checker.

# complete derivation or exact first unsupported line

First reconstruct the scalar bound independently. Put r=min(p,1-p), beta=arcsin(sqrt(r)), and tau*=h2(p)-min_t[h2(sin^2 t)+h2(sin^2(t-beta))]. For two normalized real two-vector distributions in the rotated bases, let u,w be their smaller probabilities. The maximal-probability basis vectors have overlap modulus at most sqrt(1-r). Their two rank-one projectors have summed largest eigenvalue 1+that modulus; hence u+w>=delta=1-sqrt(1-r). Since each smaller probability is in [0,1/2], entropy monotonicity and concavity give h2(u)+h2(w)>=h2(delta)>=h2(r/2)>=h2(r)/2. Evaluating at a basis vector also shows the minimum is at most h2(r). Therefore 0<=tau*<=h2(p)/2 without a finite interval minimizer or block-additivity assumption.

The exact two-basis connection to actual Boolean children is also reconstructed. If their coefficients are G_T,H_T, normalize the vector (sqrt(1-p)G_T,sqrt(p)H_T) by its norm sqrt(q_T), where q_T=(1-p)G_T^2+pH_T^2. Rotation by beta gives the parent selector-sector coefficients; the two entropies of this vector in the two bases are the physical-child posterior entropy given T and the selector spectral entropy given T. Consequently J-M=h2(p)-sum_T q_T F_p(t_T)<=tau*. For p>1/2 swap physical children first. Zero fibers are unreachable. This proves the uncertainty step used in the bundled A050 ledger without a pending computer-assisted half-Delta result.

For the physical tree define j_v=I(X_i;Y|history=v)=h2(p_i)-c_v and ell_v=h2(p_i)/2-tau*(p_i)>=0. The local net tax equals j_v/2-ell_v, so its positive part is at most j_v/2. The same-tree reserve H(Y|history)/2 has expected drop j_v/2 and leaves the terminal reserve E H(Y|Pi)/2. Its telescope pays sum_v w_v j_v/2=I(Pi;Y)/2 exactly once. Deterministic coordinate choices and stopping create no extra unrecorded entropy. Thus sum_v w_v c_v=H(Pi|Y), proving both claimed refund inequalities.

Root output entropy is bounded by actual physical influence: the product-input chain rule and adding later coordinates give H(Y)<=sum_i I(Y;X_i|X_-i)=sum_i h2(p_i)Inf_i^phys(f)<=I_phys(f). On each other-coordinate fiber the Boolean function is constant or a literal, which proves the equality with weighted pivotal probabilities. This argument pays output information only; it does not replace spectral energy by physical influence in a biased FEI claim.

The bank coefficient is sharp. At the midpoint angle, s=(1-sqrt(1-p))/2=p/4+O(p^2), so tau*(p)>=h2(p)-2h2(s). Combined with the half-entropy upper bound this gives tau*/h2(p)->1/2. If lambda<1/2, fix q with tau*(q)>lambda h2(q). For the actual Boolean point defect f_r=1-2 product_{i=1}^r X_i under bias q, every essential computing tree follows the all-one chain until a zero is seen. Its expected queries equal (1-q^r)/(1-q), its physical influence is r q^(r-1), and H(Pi|f_r)=h2(q)(1-q^r)/(1-q)-h2(q^r). Therefore A_T-lambda H(Pi|f_r) tends to the positive constant [tau*(q)-lambda h2(q)]/(1-q), while physical influence tends to zero. This refutes precisely every fixed-C inequality with lambda<1/2; it is not a uniform-cube FEI counterfamily.

Independent finite sign: use A050's exact original q=1-((2^128-1)/2^128)^2, lambda=49/100 and r=4. Then the midpoint smaller mass is exactly s=2^-129. From the original sixteen-entry table (+1 except at 1111), independently compute all Fourier squares, output probability q^4 and influence 4q^3. A rational log enclosure certifies

    [h2(q)-2h2(s)](1+q+q^2+q^3)
       -(49/100)[h2(q)(1+q+q^2+q^3)-h2(q^4)] >4q^3.

Because the displayed midpoint loss is a lower bound on tau*, this is a rigorous actual tax violation with C=1. The all-C/all-lambda necessity is supplied by the analytic argument, not by extrapolating this one case.

The source's terminal-inclusive spectral identity is correct. Set M_T=sum_v w_v M_v and S_T=sum_v w_v[h2(p_i)/2-(J_v-M_v)]. Chain rules give

    Hhat(f)=E Hhat(f_leaf)+2M_T+H(Pi|Y)/2+I(Pi;Y)/2-S_T.

No optimization of tau* is needed: ell_v+D_v equals the bracket defining S_T. S_T is nonnegative by the angular proof. Its terminal Fourier term is separate from the output reserve. At fair physical bias tau*=0, so the transcript entropy cancels the matching ell term; there is no positive fair-coordinate scalar tax.

New quantitative conversion proof: reconstruct the function-specific coherent coupling. At a uniform node with residual label T, parent fiber mass q_T and physical child coefficient C_b(T), the branch kernel is C_b(T)^2/(2q_T), discarding the queried spectral label. Boolean Parseval gives the actual fair physical branches and actual child squared spectra. The kernel depends only on the retained T; removed root labels have no extra information about that branch conditional on T and history. Thus the root-spectral information release at this node is exactly J_v, and I(S0;Pi)=sum_v w_v J_v. For a partial stopping tree, extend the coupling to a finite computing tree solely to attach the actual Y; its stopped prefix retains the same marginal law and the same information identity.

Subtract the two conditional entropy chain rules:

    H(Pi|Y)-H(Pi|S0)=I(S0;Pi)-I(Y;Pi).

Nonnegativity of J gives the lower bound. At each uniform node the elementary scalar JS inequality d(z)<=1-sqrt(1-z^2), with d'(z)=atanh(z), yields J_v<=(2/ln2)Inf_i(f_v). To verify the scalar inequality, compare derivatives: the derivative of z/sqrt(1-z^2)-atanh(z) is (1-z^2)^(-3/2)-(1-z^2)^(-1)>=0. Integrating twice and using continuity at the endpoints proves it. The physical influence removal identity gives sum_v w_v Inf_i(f_v)=R=I(f)-E I(f_leaf). Summing proves the claimed conversion bound and its positive-half-bank price R/ln2. This is a new quantitative corollary of the reconstructed common lift and the established scalar JS mechanism; independent acceptance of this contributed version is pending.

Two actual fair controls show the signed price cannot be silently dropped: the one-bit character gives conversion -1; the forward essential two-bit AND gives conversion -1+(3/4)log2(3)=1-h2(1/4)>0. A common-space tree can therefore use a bound with its explicit cost, but cannot assume either conditional bank dominates the other.

First unsupported line remains: an actual normalized compatible spectral reference supplies H(Pi|S0) or the needed witness-conditioned bank once, including any reference-reset or additional side-information corrections, and pays the signed M_T/S_T remainder and terminal Fourier entropy from the remaining exclusive influence budget. Our conversion bound does not supply that bank. Substituting its exact signed identity into A050's residual simply recovers Hhat(f)=E Hhat(f_leaf)+M_T+J_T. It cannot be counted as a second independent influence refund. No arbitrary witness label is identified with S0 without a separate compatibility proof.

# executed validation with domain, arithmetic, commands and outputs

SEARCH_SPEC.json was saved before computations. Helper A092-bank-audit-v1 freezes all Boolean tables through n=3 under two product laws (fair and (1/8,1/4,3/8) truncated), four deterministic policies (forward/reverse/maximum-pivotal-influence computing, forward depth-one stopping), three fixed fair priority shared-control functions on n=5, and the original rare n=4 underrefund witness. No symmetry quotient, random sampling, dimension escalation, GPU or heavy job. Memory estimate 100 MB, below the memok threshold. Pilot cap 60 seconds; full watchdog 120 seconds.

Executed `python -X utf8 code/audit.py --pilot` then `python -X utf8 code/audit.py` with the assigned run's absolute path. Pilot passed 44 roots, 176 trees and the rare witness in about 1.46 seconds. Full check passed 556 exhaustive roots, 2,224 exhaustive trees and 12 shared-control trees, with 51,907 exact assertions in about 4.09 seconds. The analytic proofs supply the all-dimensional statements; the finite checks do not establish uniform extrapolation. Code saves each completed census dimension and the rare certificate immediately, and each shared-control fixture as it finishes.

The independent implementation constructs weighted physical tables, a recursive centered-basis transform and actual restrictions, then computes physical transcripts and the root-spectral/transcript joint law directly. It checks exact mixture laws, physical influence removal with partial leaves, output-information release, transcript-bank chain rules, source residual cancellation and common-lift information release. Entropy identities are verified by exact rational coefficient vectors of prime logarithms. A zero coefficient vector is sufficient for equality; no linear independence of prime logarithms is presumed. Original author counts were not falsely claimed as reproduced: this is an independently frozen smaller two-law domain plus the new shared-control fixtures.

Strict signs use a separate rational log engine: for x in [1/2,1), first use log2(x)=-log2(1/x), then reduce the positive reciprocal to [1,2). With z=(r-1)/(r+1), use 96 positive atanh terms and remainder at most 2z^193/[193(1-z^2)]. All division endpoints are nonnegative numerators over positive ln2 bounds; sign-correct multiplication and exact outward dyadic rounding are used. Reciprocal reduction prevents a near-one complement log from subtracting two unrelated ln2 intervals at the extremely rare endpoint. No floating-point sign, numerical tax optimizer or automatic precision increase is used.

For the n=5 fixtures, physical coordinates are z,a,b,u,v. Let F=g if z=a=1, else h if z=b=1, else +1. Frozen core pairs are ((-1)^u,(-1)^v), (-1,(-1)^v), and ((-1)^u,-(-1)^v). Each of the four policies queries every shared physical coordinate at most once. out/SHARED_CONTROL.json retains each exact table, consumed influence, signed conversion and full terminal Fourier entropy vector. No terminal core is declared free. out/UNDERREFUND.json retains the actual table, exact spectrum, influence and rigorously positive tax certificate. out/CONTROLS.json includes both signed-bank controls.

# proof dependencies and changed downstream conclusions

A050@1 receives another independent ACCEPT_AT_STATED_SCOPE review without a mathematical repair. The earlier A046 review is preserved as prior provenance. Its scalar theorem, physical chain rules, bank-coefficient necessity and exact residual were reconstructed directly, including the original extreme rational witness. The source's mathematical hypotheses and statement are unchanged.

The contributed uniform signed-conversion claim depends on the self-contained common-lift reconstruction and scalar JS proof included above. A037@1 and C005 provide credited prior interfaces rather than unreviewed black-box assumptions. This new version is author-proved and pending A087/A085 review. It narrows the C024 side-bank mismatch to an explicit influence-priced quantity in this particular coherent coupling; arbitrary spectral references, resets and additional side information remain separate.

B20/A050/A057/A064 should retain this conversion price and its ownership in the same influence account. Essential scalar-tax payment without a refund remains refuted. Neither that route obstruction nor the rare underrefund witness disproves FEI. This stage does not repeat the retired full small-grid census or scalar half-tax constant search.

# one next mathematical action and independent reviewer

NEXT: place one prescribed source-compatible witness reference on the actual priority shared-control tree and compute H(Pi|S0)-H(Pi|witness,required side information) together with its signed reset cost. Retain the already bounded output-to-S0 conversion and every terminal core entropy in that same ledger. This is the first unmatched conditional bank exposed by the audit, and consumes the A037/A039/A091 reference interfaces rather than repeating scalar-tax payment. A087/A085 should independently review the new conversion corollary and challenge this A050 reconstruction; consumers A050/A057/A064/A037/A039/A091/A095 and B19/B20.

# actual persistence receipts or precise save blocker

All required four protocol artifacts are saved under the assigned A092 run, with code, frozen spec, pilot/main outputs, exact signed controls, underrefund spectrum, source hashes, validation and artifact receipts. PACKET_DELTA.json equals PROGRESS.json and has packet_ids=[A092]. STATUS.md is exactly two lines; WORKLOG.md and LEARNED.md are appended. code/finalize.py checks exact protocol keys, statement hash conventions, required report fields, result counts and files below 20 MB. Local persistence and review verdict are established; supervisor copy, remote mirror, downstream adoption and public release remain unverified. No other agent file, shared index or brain was mutated; no git or external message was used.

Universal bridge: this stage moves C024 history transfer and C019 consumption by independently validating A050's sharp half-output bank repair and the original lambda=0.49 Boolean underrefund certificate, then pricing output-to-root-spectral bank conversion by at most (2/ln2) consumed influence, with 2,236 tree checks retaining terminal Fourier entropy. The unmatched spectral/witness-conditioned bank, signed reference resets and full erasure/terminal payment remain open; no universal FEI constant is reduced. NEXT computes that exact reference-side bank on the existing shared-control tree, the shortest route from a now-explicit conversion price to a complete single-use stopping-tree payment rather than another isolated family bound.
