# A045 stage 4: a quadratic physical-tail reference with an owned energy budget

## exact target, quantifiers, hypotheses and units

Continue G-BIASED-LTF by replacing A041's newly refuted absolute-tail budget with a normalized quadratic reference, and independently review its complete new obstruction claim. For every finite actual two-weight Boolean sign F=2*1{w N_A+N_B>=t}-1, w>0 real, arbitrary threshold and interior independent physical biases (unequal within a group allowed), set v_i=4p_i(1-p_i). Use the orthonormal centered product Fourier basis, squared masses P(U,T), corrected entropy E=sum_nonempty P ln(v_S/P), and Delta=I-Var. All entropy, cross-entropy corrections and KL quantities below are in nats. A and B are disjoint physical coordinate groups.

For nonempty T subset B let h_T(k)=Fhat_B(T;N_A=k)/sqrt(v_T). Write its attained count profile as a constant plus sum_{j=1}^{|A|} alpha_Tj g_j(A), where g_j=2*1{N_A>=j}-1 and alpha_Tj=[h_T(j)-h_T(j-1)]/2. These g_j are genuine physical Boolean gates; the h_T process generally is not Boolean. Freeze deterministic coordinates before forming this basis. Empty groups or zero mixed mass require no reference.

New scoped result: the squared-tail INFLUENCE budget is exactly the actual mixed A-influence and is bounded by the mixed/root deficit. It normalizes a complete mixed reference whose positive mass-normalizer tax costs at most 3Delta/8. This pays energy and normalization only. The remaining complete-reference cross-entropy bound and full FEI are open.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-14 03:25 UTC, B09 STREAM_NOTES.md v2 dated 2026-10-11 23:33 UTC, own STATUS.md, and the execution-v2 protocol in full. The stale lead tax-sum instruction remains excluded by the prior exact AND2 obstruction; follow review/repair dispatch instead.

Read A041 run 20261014T012508Z-account05-A041-weighted-threshold-fei REPORT.md, CLAIMS.json, COFACTOR_REFERENCE.md equations (1)-(10), and REVIEW_A045.md. Its source-bound independent acceptance of A045-MIXED-REFERENCE-ADMISSION-DEGREE-AUDIT@1 at hash71bbc3bef10c23401d07806f2a8b948408858c821e700fce94ee9c7a126bd84a is consumed locally without rewriting the original run. Independently review A041-SIGNED-COFACTOR-VARIATION-ABSOLUTE-BUDGET-OBSTRUCTION@1 at hash46a8f1202df911c49b24b18ae3eddc4e0c106c512fc043db2397ac8533ba4404. Read A044 run20261014T025427Z-account05-A044-non-symmetric-gate-classes REPORT.md: raw shared-guard deficit loss diverges on a near-literal face despite bounded actual coherent entropy. This is context supporting retention of cancellation, not a premise of our theorem.

Prior A045 stage3 supplied the inherited-bias admission and degree/harmonic interface; those closed calculations are not rerun. No web fact or new literature claim is used. Source hashes and exact locators are saved in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

### 1. Independent acceptance of every clause of the new A041 statement

For real score z, h_T(z) jumps at z=(t-l)/w by 2 E_B[1{N_B=l}phi_T]/sqrt(v_T). The level events partition physical B inputs, so the total absolute jump is at most 2 E|phi_T|/sqrt(v_T)=2, since E|phi_i|=sqrt(v_i). For nonempty T both exterior values are zero. Restriction to attained counts cannot increase variation. The canonical tail decomposition follows by discrete telescoping; its absolute coefficients sum to at most one. Integrating its nonempty A Fourier coefficients gives Fhat(U,T)/sqrt(v_T)=sum_j alpha_Tj ghat_j(U). All biases here are physical; spectral conditional marginals need not be Boolean, and none is used.

For A041's actual family take two fair A bits, n=4r+1 fair B bits, w=n+1 and t=w+(n+1)/2. The attained physical branches are -1,g,+1, where g is balanced odd majority. With s_i=2X_i-1,

    F=(s_1+s_2)/2+(1-s_1s_2)g/2.

Thus the canonical coefficients are ghat(T)/2 and -ghat(T)/2; the OR2/AND2 tail deficits are 1/4. Hence B_abs=||ghat||_1/4, Delta(F)=I(g)/2, M=1/4, E_mix=[E(g)+ln4]/4, Delta_m=[I(g)+1]/4 and E(F)=E(g)/2+ln4. The signs of the mixed heavy-pair coefficients are minus ghat(T)/2; the sign has no effect on masses but must be retained in the coherent derivation.

Differentiate majority in one selected bit. The derivative is the indicator that the remaining 4r bits have exactly 2r ones. For 2r further selected bits, its signed level sum is the coefficient of z^(2r) in (1-z)^(2r)(1+z)^(2r)=(1-z^2)^(2r). Therefore every degree2r+1 coefficient has magnitude binom(2r,r)/2^(4r). The maximal central binomial term is at least the binomial sum divided by its number of terms. Applying this to both factors gives ||ghat||_1>=2^(2r)/(2r+1)^2. Since I(g)<=n,

    B_abs/Delta(F)>=2^(2r)/[2(4r+1)(2r+1)^2] -> infinity.

This proves the infinite-family obstruction without extrapolating finite tests. The exact E formulas also show why it is not an FEI counterfamily. No gap is found within A041's complete exact statement. The symmetric-threshold baseline remains its contextual diagnosis, not a dependency of the obstruction. The new downstream quadratic theorem is separate work, not a repair to A041's original version.

### 2. The quadratic influence budget is exact, with arbitrary unequal biases

For a real physical function h(A), define D_i h=[h(X_i=1)-h(X_i=0)]/2. The product Fourier identity is I_A(h)=sum_i v_i E[(D_i h)^2]. At any physical A edge with other-count k,

    D_i g_j=1{k=j-1}.

Distinct count tails have disjoint derivative supports at every edge. Therefore D_i h_T=alpha_T,k+1, and all cross products between different tail derivatives vanish pointwise. This gives the exact diagonal identity

    I_A(h_T)=sum_j alpha_Tj^2 I_A(g_j).

It is valid even though the functions themselves and their spectra are not orthogonal, and even when A-coordinate biases differ. The constant in h_T contributes no influence. Squaring nonempty coefficients and summing over T proves

    B_quad=sum_{T nonempty}v_T sum_j alpha_Tj^2 I_A(g_j)
          =sum_{U,T nonempty}|U|P(U,T).

For each mixed atom |T|>=1, so |U|<=|U|+|T|-1. Consequently

    B_quad<=Delta_mixed<=Delta(F).

This is an exact ownership statement with constant one, not an estimate inferred from a finite grid. It uses influence rather than the false absolute-weight deficit budget. Spending it for both orientations without accounting is invalid: our ledger fixes A as the paid derivative direction. A convex combination of the two orientation budgets is also bounded by Delta_mixed, but their sum is not a second independent reserve.

### 3. A complete normalized quadratic reference and its normalizer cost

Define, on U,T nonempty,

    K(U,T)=v_T sum_j alpha_Tj^2 ghat_j(U)^2,
    Z=sum K=sum_T v_T sum_j alpha_Tj^2 Var(g_j).

Since Var(g_j)<=I_A(g_j), 0<=Z<=B_quad<=Delta. If P(U,T)>0, at least one summand in the coherent amplitude sum is nonzero, so K(U,T)>0. Thus M=sum_mixed P>0 implies Z>0. For M>0, Q=K/Z is a complete normalized reference on the mixed label space; R=P/M is the actual conditional spectral law. Retain possible Q-positive/P-zero labels when normalizing. No Boolean admission of Q is asserted or needed. Each tail g_j is Boolean, but its mixture is a reference law of labels.

Let C_ref=sum_mixed P ln(v_U v_T/K). Direct log expansion gives

    E_mix=C_ref+M ln(Z/M)-M KL(R||Q).

This is an ordinary KL with the original mixed measure, so its negative rebate is genuine. It does not replace spectral TC by a degree-weighted KL. The mass-normalizer cost can be positive because coherent cancellation changes the actual total mass. Nevertheless, for x=M/Z, x ln(1/x)<=1/e (differentiate; the maximum is at x=1/e). Therefore

    [M ln(Z/M)]_+<=Z/e<=3Delta/8.

The final rational bound follows from e>=1+1+1/2+1/6+1/24=65/24>8/3. This normalizer payment is independent of arity and every physical bias. It cannot pay C_ref without another argument.

The bounded-variation representation also shows K<=v_U v_T: every Boolean tail coefficient satisfies |ghat_j(U)|<=sqrt(v_U), and sum alpha_Tj^2<= (sum|alpha_Tj|)^2<=1. Thus C_ref is nonnegative. Nonnegativity is not an upper bound.

To combine with the previous product-marginal reference Q0 without losing its TC rebate, retain the signed conversion exactly:

    TC_spec=KL(R||Q)+E_R ln(Q/Q0).

Either use the new complete identity above or carry that conversion term. It is not free, and the two negative rebates cannot be taken simultaneously. If a degree tilt is introduced later, every ordinary rebate still requires the prior harmonic factor under that tilted measure.

### 4. Exact control on the exponential absolute-mixture obstruction

For the two-heavy majority family, I(OR2)=I(AND2)=1 and Var(OR2)=Var(AND2)=3/4. Parseval for balanced g gives

    B_quad=1/2, Z=3/8, M=1/4

for every r, while B_abs grows exponentially relative to the root deficit. Q gives mass P_g(T)/3 to each of the three nonempty A labels. R gives all mass to U=A, so KL(R||Q)=ln3. The complete reference cross term and actual entropy are

    C_ref=[E(g)+ln8]/4,
    E_mix=C_ref+(ln(3/2))/4-(ln3)/4=[E(g)+ln4]/4.

These are analytic all-r identities, checked from actual full truth tables for r=1,2. They show that the quadratic energy and normalization genuinely avoid the excluded absolute bill. They do not make the arbitrary coefficient-process logarithm disappear.

First unsupported line: C_ref<=C B_quad, or C_ref<=C Delta(F), for one absolute C at every actual two-weight gate and every product bias. No such bound is proved here. Keeping KL(R||Q) may allow a weaker signed inequality even when a separate cross-entropy bound fails. An inequality C_ref+M ln(Z/M)-M KL<=CDelta would suffice; simply restating it is not progress. The energy owner and mass-normalizer payment are now proved, and the remaining logarithmic obligation is explicit.

Deterministic coordinates contract first; then every physical edge and tail is on the inherited remaining product cube. Repeated gate wires do not create disjoint physical coordinates: substitute repetitions into the actual truth table before transforming. Physical restrictions that define h_T are Boolean slices, while their coefficient processes, Q and R are spectral constructions. No physical-tree history, empty coefficient, singleton, child or terminal entropy obligation is removed by the mixed-sector identity.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec out/FROZEN_SPEC.json preceded computation. Independently written code/check.py was run as `python -X utf8 code\check.py --pilot` and `python -X utf8 code\check.py`. No A041/A044 checker was executed. Pilot:54 threshold fixtures,162 profiles,2760 assertions PASS in0.360s. Main:411 threshold fixtures,1365 profiles,14965 assertions PASS in1.917s. Estimated memory80MB, peak unmeasured; no>300MB job, memok requirement, dimension escalation, GPU or background process.

The complete domain is r,s in{1,2,3}, r+s<=5, w in{2,3}, every integer t=0..wr+s+1, and three labeled bias profiles: all fair; A all1/4 with B all3/4; alternating1/4,3/4 across all coordinates. No symmetry reduction. Check Parseval, signed canonical amplitude reconstruction, direct physical-edge energy against an independently transformed coefficient process, diagonal tail energy, B_quad ownership, complete Q normalization/support, exact common-log entropy identity and rigorous mass-tax bound. Streamed per-fixture outputs and checkpoints are saved immediately. There are72 positive-normalizer-tax cases; maximum finite B_quad/Delta=1, which is a check of the proved constant, not its proof.

Independent fair integer Walsh transforms cover the actual obstruction gates with7 and11 inputs. Exact combinatorial signed level sums separately check the central coefficient formula for r=1..8 (up to33 light inputs), using proved majority permutation symmetry rather than a33-bit truth table. These tests support the analytic review; they do not supply the infinite-family bridge.

All spectra and ledgers use Fraction or integer arithmetic. Log enclosures range-reduce x=2^k u,1<=u<2, use24 terms of2sum z^(2j+1)/(2j+1), z=(u-1)/(u+1), and bound the remaining tail by2z^49/[49(1-z^2)]. Signed k reverses interval endpoints when needed; export rounds outward to24 decimal places. Exact entropy identities compare coefficients of identical logarithm arguments, never overlapping numerical intervals. The first pilot had one wrong local expectation for the sign -ghat(T)/2; correcting that sign changed no mathematical source, domain or precision. out/PILOT_REPAIR.json records it.

## proof dependencies and changed downstream conclusions

Independently accept A041-SIGNED-COFACTOR-VARIATION-ABSOLUTE-BUDGET-OBSTRUCTION@1 at its exact original statement/hypotheses hash, source-bound in CLAIMS.json and out/REVIEW_RECORD.json. Consume A041's exact-scope independent acceptance of our prior admission/degree audit. The new scoped quadratic continuation uses physical Fourier/derivative identities and the canonical attained-count tail representation; its proof is reconstructed here and has no conjectural FEI dependency. The source obstruction and new continuation are acyclic downstream results, not mutual assumptions.

B09/A041 can replace the false B_abs budget with the exact B_quad owner and normalized Q. This closes one energy-budget line and pays one complete-reference mass normalizer by an absolute constant. It does not permit Boolean FEI on Q, an upper bound by summing tail entropies without a mixing argument, a free TC conversion, or a second use of root influence. No registered theorem is refuted. The remaining cross-entropy target is not added as a broad claim.

## one next mathematical action and independent reviewer

NEXT: A041/A044 should test the actual signed C_ref-KL remainder of this squared-tail reference, not an absolute or conditional-Boolean mixture. Derive its complete logarithmic bound using the disjoint physical derivative support, and preserve the exact normalizer and reference-conversion terms. A090/A091 or A085 should independently review the quadratic ownership and normalized-reference statement and the full source obstruction acceptance. This is a new quadratic mechanism; previous scalar-tax, mass-only and absolute-tail failures are retained, not renamed as further attempts.

## actual persistence receipts or precise save blocker

All four required protocol files, checker, frozen spec, exact outputs, pilot repair, source receipts, review and validation receipts are saved in this run only. Rolling STATUS.md has two lines; WORKLOG.md and LEARNED.md are appended. Finalizer verifies exact schema field sets, original claim hashes and source-proof hash, identical progress copies, required report headings, final bridge paragraph and file sizes below20MB. Local delivery is complete; independent review of the new quadratic statement, supervisor adoption/copies and remote persistence remain pending. No other agent, shared index, board, lead note or brain was modified.

**Universal bridge:** This stage moves B09's complete signed mixed-set reference toward C020 whole-set witness cost by replacing the exponentially false absolute-tail bill with a quadratic influence budget equal to actual mixed A-energy and bounded by Delta with constant one, and by paying the normalized reference's positive mass tax by3Delta/8 nats. It also independently closes A041's exact scoped obstruction review and consumes the prior admission-audit acceptance. The full complete-reference cross-entropy minus KL charge, remaining sectors and physical-tree child/terminal transfer are still open, so no universal FEI constant is gained. NEXT attacks that remaining logarithmic charge in the same now-normalized, physically owned reference; another isolated gate bound or scalar tax search would not close this missing bridge.
