# A045 stage 3: mixed spectral references and Boolean admission

## exact target, quantifiers, hypotheses and units

Referee A041-COHERENT-PURE-SECTOR-PAYMENT@1 and audit its proposed mixed-sector continuation. The existing claim holds at its exact stated scope, conditional on the explicitly cited symmetric-threshold baseline. The new result is a scoped reference/admission audit, not a weighted-threshold or universal FEI theorem.

Let F be an actual Boolean sign on disjoint physical coordinate groups A,B under an independent product law with interior biases p_i. Use X_i in {0,1}, v_i=4p_i(1-p_i), phi_i=(2X_i-1-(2p_i-1))/sqrt(v_i), P(U,T)=Fhat(U,T)^2 and v_U=product_{i in U}v_i. Corrected entropy E=sum_{S nonempty}P(S) ln(v_S/P(S)) is in nats. Delta=I-Var=sum_{S nonempty}(|S|-1)P(S). Zero summands are omitted. This normalized product basis uses actual physical biases, including unequal biases, not biases inferred from a spectral conditional law.

On the mixed sector U,T nonempty put M=sum P, a(U)=sum_T P(U,T), b(T)=sum_U P(U,T), d(U,T)=|U|+|T| and Delta_m=sum(d-1)P. For M>0 define Q0=a b/M^2 and Qd=(d-1)a b/(M Delta_m). Both are normalized reference laws on the FULL mixed label space, including labels of zero actual mass. Neither is asserted to be a Boolean spectrum. Contract deterministic coordinates before using the normalized basis. If M=0, mixed entropy and its obligation vanish; do not form any conditional distribution or divisor.

## sources actually read, revisions and theorem locators

Read the execution-v2 protocol in full, current BOARD snapshot dated 2026-10-14 00:40 UTC, B09 STREAM_NOTES.md v2 dated 2026-10-11 23:33 UTC, and A045 rolling files/previous stage records. The lead's tax-sum direction is superseded by our exact stage-2 obstruction; this stage follows its review/repair-first requirement and the updated dispatch toward a complete signed mixed reference. It creates no additional broad conjecture.

Read A041's run 20261013T215146Z-account05-A041-weighted-threshold-fei: REPORT.md, CLAIMS.json, PURE_SECTOR_PAYMENT.md, especially equations (1)-(8), the equal-weight-group extension, and its exact first unsupported line. The statement hash under review is 8f36fbc86ed36574351e69b9dcb2a18eadad8a8b3b74b5936236a033643eab8b. Read the primary baseline current-threshold-paper.tex at theorem bias:strong, displaying E<=(460+80 ln2)Delta for symmetric thresholds at every product bias. This is a cited source-complete dependency; the underlying paper's proof is not independently re-certified in this stage.

Read A096's run 20261013T220343Z-account05-A096-live-gap-ledger REPORT.md (complete function-specific edge reference retains the arbitrary seed) and A098's run 20261013T235014Z-account05-A098-resource-reallocation REPORT.md (degree/reference audit dispatch; influence-only complete priors fail; universal core KL lower bound open). Read A032's REALIZABILITY_METHOD.md from run 20261011T215947Z-account05-A032-boolean-phase-realizability: uniform phase admission, support-at-most-four classification, and affine support reduction. Its uniform necessary square condition explains our fair examples; the biased admission checks here are independently constructed and do not extrapolate uniform arithmetic to biased bases. Source hashes and locators are in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

### 1. Independent review of the complete A041 claim

For s>0 define psi_s(z)=z^2 ln(s/z^2), continuously extended at zero. The function psi_s(z)+3z^2 has second derivative 2 ln(s/z^2)>=0 on |z|<=sqrt(s), with a continuous first derivative at zero. Jensen gives psi_s(E z)<=E psi_s(z)+3 Var(z) for arbitrary signed amplitudes in this interval. No entropy of the slice labels is needed.

For any actual Boolean physical slice f_x(B), |fhat_x(T)|<=E|phi_T|=sqrt(v_T), since E|phi_i|=sqrt(v_i) and the coordinates are independent. In the signed coefficient process c_T(x)=fhat_x(T), the A-Fourier coefficients are Fhat(U,T). Thus E_A c_T=Fhat(empty,T) and Var_A c_T=sum_{U nonempty}P(U,T). Jensen summed over |T|>=2 proves exactly A041's coherent pure-B bound, and likewise for A. Physical restrictions are Boolean; the averaged function E_A F need not be Boolean, which is why its squared spectrum cannot replace the slice spectra.

Orient each negative weight by flipping its physical coordinate and bias, delete zero weights, and freeze deterministic coordinates. Restrictions to a positive equal-weight group G_j are symmetric thresholds, even with unequal biases. Let a_j(S)=|S intersect G_j| and r(S) count occupied groups. Atomwise, |S|-1=sum_{j:a_j>0}(a_j-1)+(r(S)-1). Therefore Delta=sum_j D_j+R with the claim's definitions. Parseval identifies D_j as the expected physical slice deficit. Every corrected entropy summand is nonnegative by the coefficient bound above. The baseline pays expected slice degree>=2 entropy by c D_j, c=460+80 ln2. Summing Jensen's variance charges costs at most

    3 sum_{S:r(S)>=2} #{j:a_j(S)>=2} P(S)
       <=6 sum_S(r(S)-1)P(S)=6R.

This proves E_pure,ge2<=c sum_j D_j+6R<=cDelta. In two groups R=M. In all-distinct weights the pure higher-degree sector is empty, so this theorem does not pay the mixed sector. No weight ratios, equal biases, or bounded arity were assumed.

For completeness the source's singleton reduction also follows directly: let signed derivative mean a_i and pivotal probability rho_i. Then |a_i|<=rho_i, I_i=v_i rho_i and P({i})=v_i a_i^2. Since x ln(1/x)<=1-x, the singleton contribution is <=2v_i(rho_i-a_i^2). Also sum_i[I_i-P({i})]=sum_{|S|>=2}|S|P(S)<=2Delta. Hence all singleton corrected entropy costs <=4Delta nats. This does not pay mixed entropy or allow Delta to be spent twice without adding the constants.

For the actual fair conjunction on m coordinates in each group, realizable as weights 2 and 1 with threshold 3m, every nonempty mass is P=4^(1-2m). Therefore M=(2^m-1)^2P and E_mix/M=2(2m-1)ln2, divergent. Delta_m/M=2m*2^(m-1)/(2^m-1)-1 grows with m. This verifies the claim's mass-only obstruction without alleging an FEI counterexample.

Direct expansion, with E_A^m=sum_U a ln(v_U/a), gives

    E_mix=E_A^m+E_B^m+M ln M-M TC_spec,
    TC_spec=KL(P/M || Q0)>=0.

This reference is complete on its declared mixed sector and normalized; it is spectral total correlation, not physical total correlation conditioned on a gate event. None of these conclusions requires Q0 or its marginals to be Boolean spectra. All clauses of A041's exact claim are accepted at their stated scope; no strengthening to E_mix<=KDelta is accepted.

### 2. Boolean admission fails after spectral conditioning

At bias p=1/4 the actual one-bit Boolean spectra are only the constant law (1,0) or the literal law (1-v,v)=(1/4,3/4). The normalized law (0,1) is NOT Boolean: its inverse is the normalized centered literal, whose values are -1/sqrt(3), sqrt(3). An actual OR sign with weights 2,1, threshold 1 and two biases 1/4 has M=9/64. Conditioning on its sole mixed Fourier set yields both marginals (0,1). Thus normalization, physical Booleanity of the original gate, and a perfectly valid reference do not license applying a Boolean-gate inequality to either conditional marginal. This example is a physical threshold, not an abstract probability law.

For fair AND4 split into groups of size two, all nonempty P=1/64, M=9/64, both normalized mixed marginals are (0,1/3,1/3,1/3), and Q0 is uniform on nine mixed labels. A two-bit Boolean coefficient is an integer multiple of 1/4, so its squared mass is an integer square divided by 16. Mass 1/3 is impossible. On four fair bits coefficients are integers divided by 16; Q0 mass 1/9 is likewise impossible (256/9 is not even an integer). This proves that a normalized product reference can fail joint Boolean admission.

The converse inference also fails. On four fair physical bits define

    F=(2X0-1)(2X2-1)(-1)^(X1 X3),
    A={0,1}, B={2,3}.

This is an actual Boolean truth table. Its four Fourier masses are 1/4 at (U,T) in {{0},{0,1}} x {{2},{2,3}}, all mixed. Both marginals are (0,1/2,0,1/2), not Boolean on two fair bits, because 16*(1/2)=8 is not an integer square. Nevertheless Q0=P is itself Boolean-realizable and TC_spec=0. The 2x2 signed coefficient matrix has nonzero determinant: phases are coupled across groups. Product squared magnitudes do not force product Boolean functions.

The fair examples are applications of the existing A032 uniform admission and four-point affine-plane classification, not a new phase classification. Their purpose here is to test the mixed-reference interface before importing a Boolean inequality. The catalog addresses inherited biased marginals and does not repeat A032's four-bit enumeration.

Precisely, for arbitrary interior product biases and normalized nonnegative laws q_A,q_B, a joint product law q_A q_B has a Boolean realization with separable coefficient signs iff each marginal has a Boolean realization in its inherited basis. To prove necessity, separable signs reconstruct F(x,y)=a(x)b(y), with each factor's L2 norm one. Full physical support and F in {+1,-1} imply neither factor vanishes and |a(x)| is a constant alpha, |b(y)|=1/alpha. Unit norms force alpha=1. Each factor is Boolean. Conversely tensor any two Boolean realizations on disjoint inputs. A product law may have a Boolean realization with nonseparable signs despite failing marginal admission, as the explicit witness shows. No claim about exhaustive phases in arbitrary dimensions is made.

### 3. Exact degree-weighted reference and the KL distinction

Write R0=P/M on mixed labels. Its two marginals are a/M,b/M. Product Q0 preserves each degree mean, since d-1=(|U|-1)+|T| is additive. Therefore

    Z=sum(d-1)Q0=Delta_m/M,
    Qd=(d-1)Q0/Z=(d-1)a b/(M Delta_m),
    Rd=(d-1)P/Delta_m.

Qd and Rd are normalized, Delta_m>=M>0, and Qd is positive wherever P is positive. Their pointwise likelihood is unchanged:

    Rd/Qd=R0/Q0=M P/(a b).

Their KL averages are NOT unchanged: KL(Rd||Qd) weights that log by (d-1)P/Delta_m, whereas TC_spec weights it by P/M. The mixed entropy identity above must retain TC_spec with its original measure. To rewrite that rebate under Rd one needs the harmonic factor:

    M TC_spec=Delta_m E_Rd[ln(MP/(ab))/(d-1)].

For the actual five-bit threshold 2(X0+X1)+X2+X3+X4>=3 at all biases 1/4, the checker certifies M=60993/262144, Delta_m=122391/262144. TC_spec lies in [3301600245612203/200000000000000000, 2063500153507627/125000000000000000], while KL(Rd||Qd) lies in [825202941607491/50000000000000000, 16504058832149821/1000000000000000000]. Their difference lies in the strictly negative rational interval [-985598977799/250000000000000000,-788479182239/200000000000000000]. Equality of pointwise likelihoods is therefore insufficient for exchanging the rebates. The full exact P and rigorous intervals are saved in out/CHECK_OUTPUT.json.

The exact payment obligation, retaining the actual normalization, is

    E_mix/Delta_m=E_Rd[ln(v_U v_T/P(U,T))/(d-1)].

This stage proves the normalization and interface, NOT a uniform bound on the right-hand side. The first unsupported line is that this expectation is bounded by one absolute K for all actual two-weight thresholds, or that a complete signed reference pays it with a root-Delta budget after including all remaining sectors. The general logarithmic bound is still open; numerical certificates in a frozen finite domain do not prove it.

### 4. Deterministic inputs, reused variables and physical conditioning

At p_i=0 or 1 the normalized phi_i is undefined. Freeze X_i first, obtain the contracted Boolean function and its interior basis, and compute its actual spectrum there. The centered tensor formula has a polynomial extension whose masses containing the frozen coordinate vanish; the eight exact endpoint fixtures compare that extension with the contracted truth table. This is not a definition of a normalized basis on a deterministic input. Limits of ratios and ratios of contracted functions remain different questions.

Every factorization here requires disjoint physical coordinate groups. Reusing a literal in two gate wires gives, for example, XOR(X,X)=0, a constant sign with unit empty mass, whereas independent fair copies have unit mass on the two-coordinate parity label. One must substitute repeated variables into the truth table before taking the Fourier transform; relabeling two occurrences as independent invalidates both product bias and spectral convolution.

Physical conditioning means restricting a truth table at X_A=x with its original remaining product biases; its amplitudes average coherently. Spectral conditioning means renormalizing masses after an event such as U,T nonempty; its marginals are abstract laws of labels. The one-bit example above distinguishes them exactly. Degree tilting is a third change of spectral measure, and requires the harmonic correction just derived. No physical tree, inner-child payment, empty-sector correction or terminal entropy has been eliminated by any of these operations.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec: out/FROZEN_SPEC.json written before computation. Independent helper: code/check_mixed.py. Run commands from this run directory: `python -X utf8 code\check_mixed.py --pilot` and `python -X utf8 code\check_mixed.py`. No source checker was run. Peak memory was estimated below 90 MB; neither job required the >300 MB memok gate. Pilot passed 3,907 assertions in 0.426 seconds. Main passed 40,963 assertions in 81.856 seconds, below the frozen 180-second cap; the pilot and main limits are distinct.

Main exhausts every integer threshold t=0,...,wr+s+1 for r,s in {1,2,3}, r+s<=5, w in {2,3}, and all nine homogeneous-per-group profiles from {1/4,1/2,3/4}^2: 1,233 labeled fixtures including constants. It constructs every truth table on one, two and three bits at each of those biases: 828 tables, with exact normalized product spectra for admission. There are 729 nonzero mixed cases and 717 for which at least one marginal fails exact Boolean admission. These are fixture counts, not counts modulo functional equivalence. It checks 3,816 physical-slice coefficient Jensen instances, 147 scalar Jensen fixtures, 126 occupation patterns, eight deterministic contractions, four compressed conjunction ledgers and two explicit four-bit witnesses. No dimension was raised and no all-functions four-bit census was repeated.

Arithmetic: rational centered tensor coefficients c_S and exact masses c_S^2 v_S, with Parseval checked on every actual transform. Log identities are compared by equal rational coefficients of common log arguments. Inequalities use rational log enclosures: range-reduce x=2^k u with 1<=u<2, use z=(u-1)/(u+1) and 24 terms of 2 sum z^(2j+1)/(2j+1). The nonnegative tail is bounded by 2z^49/[49(1-z^2)]. Apply the same enclosure to ln2, multiply signed k with interval reversal as needed, and round OUTWARD to 24 decimal places. Displayed intervals round outward again to 18 places. Diagnostic floats never decide a claim.

The initial pilot exposed one implementation-only assertion: a formal log dictionary for TC=0 was nonempty because ln(1/4)=2ln(1/2) had not been canonicalized. Replaced dictionary emptiness with the exact rational pointwise likelihood-one condition, which proves TC=0 directly. This did not change the family, domain, arithmetic precision or mathematical statement. The failure and correction are recorded in out/PILOT_FAILURE.json. Passing pilot and main outputs, streamed cases and checkpoints remain on disk.

## proof dependencies and changed downstream conclusions

A041-COHERENT-PURE-SECTOR-PAYMENT@1 independently accepted at its exact hashed statement, using its declared bias:strong source dependency. CLAIMS.json preserves the statement, hypotheses and source hash; it adds a source-bound local review record. Adoption into shared registries is left to the supervisor. The new scoped audit A045-MIXED-REFERENCE-ADMISSION-DEGREE-AUDIT@1 depends only on actual Boolean Fourier/Parseval identities and the explicit truth tables; it does not depend on a conjectural mixed payment.

Downstream correction: Q0 remains a valid normalized reference despite non-Boolean marginals. Applying a Boolean FEI or biased gate theorem to a/M or b/M needs a separate actual Boolean realization and cannot be justified by spectral conditioning. Joint admission cannot be inferred from marginal admission failure without controlling phase separability. Replacing TC_spec by degree-weighted KL silently changes the identity, even though the likelihood ratio agrees pointwise. No universal erasure, history-transfer, stopping-tree or whole-set inequality has been established.

## one next mathematical action and independent reviewer

Next: give A041/A024 the exact Qd normalizer and harmonic factor, and construct a signed physical-cofactor/derivative reference that actually bounds the displayed E_Rd logarithmic charge, retaining its ordinary spectral TC rebate and singleton, empty, inner and terminal accounting. Use the biased one-bit, fair AND4, coupled-phase and unequal-KL fixtures as admission/normalization constraints before any proposed payment. A091 or A085 should independently review this scoped audit; A041 should consume the source-bound acceptance and the correction. Do not repeat scalar-tax or binary endpoint calibration.

## actual persistence receipts or precise save blocker

All writes are under A045. Required REPORT.md, CLAIMS.json, PROGRESS.json and matching PACKET_DELTA.json are present; code/out certificates, frozen spec, review, source receipts and hashes are saved. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated. out/PERSISTENCE_RECEIPTS.json records schema/hash/size validation. No shared registry, board, stream lead file, source tree or brain was modified. Local delivery is complete; supervisor copying and external review are pending, not claimed completed.

**Universal bridge:** This stage moves B09's complete signed mixed-set reference target toward C020 whole-set witness cost by proving its exact degree normalizer, distinguishing admissible Boolean spectra from conditional label laws, and certifying the harmonic correction needed to retain the spectral TC rebate. It also independently closes A041's stated pure-sector payment review. It gains no absolute mixed-payment constant: the displayed normalized logarithmic expectation, other sectors and physical-tree inner/terminal costs remain unpaid. Building one signed coefficient reference that bounds this charge is the shortest remaining route toward the universal bridge; further conjunction, scalar-tax or binary class calculations would not supply the missing complete-set payment.
