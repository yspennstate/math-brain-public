# A036 / B08: normalized collision payment on point-defect tensors

## exact target, quantifiers, hypotheses and units

All logarithms are base two unless written ln. Let C be the class of all finite disjoint tensor products of f_m(x)=1-2*1_{x=x0}, m>=2, allowing arbitrary physical translations, a global output sign, character multiplication, extra character coordinates and irrelevant coordinates. All functions are genuine Boolean signs on the uniform cube. Define P(S)=fhat(S)^2, d_i=P(i in S), I=sum_i d_i, B=sum_i h_2(d_i), and the reference Q(S)=prod_i d_i^{1_{i in S}}(1-d_i)^{1_{i not in S}}. Q is fixed across sampled spectral sets. On its support define b_S=sign(fhat(S))*sqrt(Q(S)), and set b_S=0 off that support. For this class P and Q have identical support, so no sign completion is needed.

Put K=D_2(P||Q), C_b(U)=sum_S b_S b_{S xor U}, v_U=C_b(U)^2, Z=sum_U v_U, L=sum_U v_U log_2(1/v_U), R=v/Z and T=L/Z=H(R)-log_2 Z. Zero summands are zero. The following three inequalities hold on C:

1. **Named excess payment:** K >= [B-4I]_+.
2. **Normalized collision payment:** K >= T/4-8I.
3. **Separate sufficient recovery:** B <= T/4+8I.

Thus collision payment with any constant kappa on this class would imply H(f)=B-K <= (kappa+8)I; the proved kappa=8 yields 16I. Independently, the proof of (1) already gives the stronger H<=4I. The contribution is the explicit divergence/collision ledger and the recovery estimate, not a new FEI class claim or a novelty claim for the known point-defect entropy bound. Constants are conservative.

These estimates are NOT asserted for arbitrary Boolean functions, arbitrary sparse activation of a seed, physical restrictions, overlapping products, or near-tensor surgery. In particular the full-support low-I universal collision premise remains open.

## sources actually read, revisions and theorem locators

Execution protocol: fei-execution-protocol/2, revision 2026-10-11-execution-v2, read in full. Read campaign README/CURRENT_STATUS and inspected the claim, obstruction and packet registries, next-action file and plan, particularly plan normalization paragraph and A036 acceptance contract. BOARD.md was read at stage start; B08 STREAM_NOTES.md was absent at both checks. No earlier local A036 output existed.

Supplement: CAMPAIGN.md, CLAIMS.md, COUNTEREXAMPLES.md, SEED_LEMMAS.md and NATIVE_MAPPING.md were inspected. Most relevant input is SEED_LEMMAS Section 3, the exact point-defect law and fixed-Renyi obstruction. The curated ROUTE_MAP_CURATED.md Sections 1-4 and 9.1 identify the prior normalized convolution/support-loss controls and the still-open KL premise. Its source blob is 216cb662e7b21cfe6d7c2034a6690f3c10b886fa. The referenced unbundled September normalized-convolution and collision-admission reports were NOT retrieved in full, so they are not proof dependencies here. Their scope warnings are retained; all formulas needed below are independently derived.

Read relevant contextual excerpts from threshold_paper_38pp.txt (Theorem A, Proposition 5.5 and Theorem 6.6) and the earlier 29-page threshold version (Theorem A); the current threshold constant differs from the earlier version. Read percolation_spectral_pivotal_entropy_30pp.txt Section 11.2/Corollary 11.3 and the corresponding Section 11.2 in the 31-page version. The latter comparison illustrates the importance of direction and support in relative entropy, and is not a mathematical premise of this proof. Full texts were searched for reference/divergence/composition locators; this report does not claim a full independent audit of these manuscripts. Earlier B05/B09/B19 reports were inspected for prior obstruction/review scope; none supplies a proof premise below. Local hashes of the contextual inputs are recorded in out/source_receipts.json.

## complete derivation or exact first unsupported line

### 1. Exact reference, support and cross entropy

For any law P, its product-marginal Q satisfies E_P log_2(1/Q)=B and H(P)+D_2(P||Q)=B. For a point-defect factor let p=2^-m, d=2p=2^(1-m). Taking x0=all+,

fhat(empty)=1-d, fhat(S)=-d for S nonempty;
P(empty)=(1-d)^2, P(S)=d^2 for S nonempty;
I_i=d, I=md, Q(S)=d^{|S|}(1-d)^{m-|S|}.

All coefficients are nonzero for m>=2. The reference is normalized: sum Q=1. For a disjoint tensor, both P and Q tensorize and b tensorizes. Character/irrelevant coordinates are deterministic under both laws; they add no entropy/divergence. For A=supp P, Q(A)=1. Thus K_supp=-log_2 Q(A)=0 and K_shape=D_2(P||Q(.|A))=K_full=K. This explicitly accounts for support terms rather than discarding them.

Character multiplication permutes spectral indices and sends d_i to 1-d_i on affected coordinates. B, K and squared autocorrelations are unchanged. Since the unshifted factor has d<=1/2, influence weakly increases under character multiplication. Physical translations multiply b_S by a character in S, which multiplies C_b(U) by a sign and leaves v unchanged. Therefore it suffices to prove the estimates for unshifted all+ point defects.

### 2. Exact collision formula and tensor normalization

Write c_S=sqrt(Q(S)); c_empty=(1-d)^(m/2). Then b=-c+2c_empty*delta_empty. For U nonempty of size k,

C_b(U)=(2*sqrt(d(1-d)))^k -4(1-d)^(m-k/2)*d^(k/2)
       =(2*sqrt(d(1-d)))^k [1-2^(2-k)(1-d)^(m-k)].

Let a=4d(1-d). Consequently

v_0=1,
v_k=a^k [1-2^(2-k)(1-d)^(m-k)]^2, k>=1,
Z=1+sum_{k=1}^m binom(m,k)v_k,
L=sum_{k=1}^m binom(m,k)v_k log_2(1/v_k).

For k=1 the bracket lies in [-1,1]; for k>=2 it lies in [0,1]. Thus 0<=v_k<=a^k<=1 and 1<=Z<=(1+a)^m. For tensors v=v1 tensor v2 and Z=Z1 Z2. R tensorizes and

T=T1+T2,
L=L1 Z2+Z1 L2.

These identities use product-compatible actual phases; no independent zero completion is made. The three-bit factor gives exactly Z=319/256, preserving the archived raw-L guard. The proof uses T throughout and does not propose a raw-L influence payment.

### 3. Direct payment of the named entropy excess

For one factor the exact entropy is

H=-(1-d)^2 log_2((1-d)^2)+4d(1-d/2)(m-1).

The empty contribution is at most 2d/ln2: use -ln(1-d)<=d/(1-d). Since ln2>1/2, this contribution is at most 4d. The remaining contribution is at most 4d(m-1). Hence H<=4md=4I. By the exact cross-entropy identity K=B-H and Gibbs' inequality K>=0, K>=[B-4I]_+. This sums over tensors, and the character extension preserves the claim.

### 4. Scalar entropy cap used for upper collision payment

For 0<=x<=y<=1, writing x=yr,

x log_2(1/x)=yr log_2(1/y)+yr log_2(1/r)
            <=y log_2(1/y)+y/(e ln2).

Apply this with x=v_k, y=a^k and sum multiplicities. Since Z>=1,

T<=L<=ma(1+a)^(m-1) log_2(1/a)+[(1+a)^m-1]/(e ln2).   (U)

All losses in (U) are retained; its all-m application requires the scale bounds in the next section.

### 5. Normalized payment K>=T/4-8I

If 2<=m<=6, H(R)<=m and log_2 Z>=0 give T<=m. Thus T/4<=2^(m-3)I<=8I, while K>=0.

If m=7, d=1/64 and a=63/1024. The exact integer comparison 2*1087^6<3*1024^6 proves (1+a)^6<3/2. Also

(1+a)^7-1 <=7a(1+a)^6.

Using log_2(1/a)<=log_2(1/d)=6 in (U) gives T/4<9I+(3/(2e ln2))I<10I. Here e>8/3 and ln2>2/3 imply e ln2>16/9>3/2. Meanwhile B=7h_2(d)>=6I and H<=4I, so K>=2I. Therefore T/4-K<8I.

If m>=8, the sequences m2^(1-m) and m(m-1)2^(1-m) decrease on this range. Hence

ma<=4md<=1/4,
ma log_2(1/d)<=4m(m-1)d<=7/4.

Since (1+a)^m<=e^(ma)<=1/(1-ma)<=4/3 and e^(ma)-1<=(4/3)ma, (U) gives

T/4 <= I log_2(1/d)+(4/3)I*ma log_2(1/d)+(4/(3e ln2))I
     < I log_2(1/d)+(10/3)I
     <= B+4I.

Combine with K=B-H>=B-4I to obtain T/4-K<=8I. Tensor additivity of K,T,I proves the payment on the entire class.

### 6. Separate recovery B<=T/4+8I

For 2<=m<=7, h_2(d)<=d log_2(1/d)+d/ln2 and 1/ln2<2 imply B<=(m+1)I<=8I; T>=0 suffices.

For m>=8 set s=2(1-d)^(m-1)-1. Bernoulli's inequality gives s>=1-2(m-1)d>0. The singleton collision contribution is v_1=a s^2, with log_2(1/v_1)>=log_2(1/a). All raw entropy contributions are nonnegative. Therefore

T/4 >= I W log_2(1/a),
W=(1-d)s^2/Z >=(1-d)[1-4(m-1)d]e^(-ma)
              >=1-(8m-3)d.

The last step uses e^-x>=1-x and the product of nonnegative (1-u) factors being at least one minus their sum. All factors used here are nonnegative for m>=8. Also log_2(1/a)>=log_2(1/d)-2. Consequently

T/4 >= I [log_2(1/d)-2-(8m-3)d log_2(1/d)].

The sequence (8m-3)(m-1)2^(1-m) decreases for m>=8: its next-term ratio is (8m+5)m/[2(8m-3)(m-1)]<1, since 8m^2-27m+6>0. At m=8 it equals 427/128<7/2. Since B<=I[log_2(1/d)+1/ln2],

B-T/4 <=(2+1/ln2+7/2)I<7I<=8I.

This recovers the marginal entropy budget from the normalized collision statistic with a paid error, independently of the lower-divergence payment. Tensor additivity proves the same recovery bound on C.

### 7. Implication and exact open boundary

For any class on which B<=T/4+cI and K>=T/4-kappa I both hold with the SAME product-marginal reference and phase convention, H=B-K<=(c+kappa)I. This is the sufficient recovery implication. Neither inequality follows from the other. On C the above proof gives c=kappa=8, alongside the sharper direct H<=4I.

First unsupported line for a universal extension: asserting either B<=T/4+8I or K>=T/4-8I for an arbitrary Boolean function. The point-defect formula, its low-energy scale estimates and tensor factorization do not justify either assertion. Support conditioning of a different reference is also not covered. The paired-coordinate conditioned under-recovery control in the archive remains applicable to proposed extensions; it is not contradicted.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: out/FROZEN_SPEC.json. Command from this run directory: `python -X utf8 code/check.py`. Domains: individual factors m=2,...,16; independent direct integer Walsh and symbolic rational autocorrelation reconstruction m=2,...,7; one 2-bit x 3-bit tensor normalizer check. No truth-table search, randomness or automatic dimension increase.

Every comparison is exact Fraction arithmetic. Logarithms use 16 terms of ln x=2 sum t^(2j+1)/(2j+1), t=(x-1)/(x+1), after reducing x to [1,2), with remainder bounded by 2t^33/[33(1-t^2)]. Signed log2 intervals are formed with exact range shifts and positive ln2 bounds. Serialized intervals are rounded outward to rational multiples of 10^-18. The initial run exposed Python's large-integer string conversion limit; out/INITIAL_CHECK_FAILURE.txt records the failure and correction. This was an output-format issue, not a mathematical sign failure.

The analytic proof above supplies the all-m bridge; finite validation is not used to infer unbounded dimension. Final execution results and observed runtime are in out/verification.json and out/check_receipt.json. Self-checking direct Walsh reconstruction is not independent external review.

## proof dependencies and changed downstream conclusions

No external unreviewed mathematical claim is a premise. Dependencies are elementary Walsh expansion, Gibbs nonnegativity, entropy on a finite support, the binomial theorem, Bernoulli's inequality, and the displayed rational log remainder. The point-defect FEI bound is recovered baseline. One complete candidate package contains the structural excess bound, normalized payment and recovery; independent acceptance is pending.

A037/A039 must preserve Q across any use of this ledger; physical restrictions generally change Q and do not inherit this theorem. A038 receives a divergence estimate but no occupancy-credit identification. A040/A048 can stress extensions beyond exact tensor products. A066 can use the explicit all-level autocorrelation profile, but no semigroup payment is proved. A088/A094 are the requested independent reviewers. B20 may adopt the source-complete restricted result after review without marking full FEI closed.

## one next mathematical action and independent reviewer

Next: test and prove or refute the two separate inequalities on a single point surgery of a tensor of two nonconstant point-defect factors; retain the actual changed marginals and signs. This leaves exact tensor factorization and directly probes the mechanism's current boundary. Reviewer A088 should reconstruct the singleton recovery and scalar cap bounds; A094 should challenge the sufficient-recovery implication and admission scope.

## actual persistence receipts or precise save blocker

All files are local to the authorized A036 directory. out/save_receipts.json records SHA256 and file sizes after final writes; out/source_receipts.json pins inspected local inputs. REPORT.md, CLAIMS.json, PROGRESS.json and its PACKET_DELTA.json compatibility copy are saved in this run. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. No shared index, other agent folder, brain store, git repository, or external service was modified. Supervisor copying, independent review, mirror verification and downstream use have not been observed and are not claimed.
