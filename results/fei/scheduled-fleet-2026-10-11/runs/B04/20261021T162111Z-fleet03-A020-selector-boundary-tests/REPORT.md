# A020 stage 6: all private prefixes paid, with a nonconstant ineligible terminal

Full FEI remains OPEN. The SAME incoming reference survives every remaining private exposure on the A020 rare-query family with a positive signed reserve. The original half-core bank pays the already-booked first insertion, its conversion, all later query code charges, and the final positive terminal deficit, leaving more than 1/32 bit. Local rate-4 eligibility nevertheless fails even for a nonconstant penultimate child when k>=8. This extends and independently reconstructs the fixed-reference continuation in A016; it supplies no arbitrary-core reference.

## exact target, quantifiers, hypotheses and units

For every integer k>=3 put d=2^-k, A=1_(v=0) on k bits, h=chi_u(1-A)+chi_q A, and s a two-bit sign point defect with mean 1/2. Let F=1 at fresh gate x=0 and hs at x=1. All physical bits are independent uniform bits; chi_b=(-1)^b. Entropy, CE, KL and banks are in bits. References cover every positive true spectral atom.

Retain A020 stage5's core reference Q_h=(P_h+point_{q})/2 and exact Q_s=P_s. The full root reference has, at both gate frequencies e,

Q_F(e,T)=[Q_h(T_core)P_s(T_mask)+1_(T=empty)]/4.

Expose q, then v_1,...,v_k. Each child inherits the frequency marginal of this one root Q, identical for both physical outcomes. No exact-spectrum reset or new conditional lift is used. The claim concerns this supplied family/reference only, not all Boolean functions.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2; machine AGENTS.md; BOARD snapshot 2026-10-21 16:22 UTC; B04 STREAM_NOTES v2, 2026-10-11 23:25 UTC; own rolling files and stage5 report/checker. Read canonical README, CURRENT_STATUS, claim/obstruction/packet registries and stream actions, and relevant B04 campaign-plan lines. Read supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING, emphasizing coherent selectors and supplied-reference scope. Inspected all four context text files and threshold 38pp Proposition 8.6, equation (75). Their bytes decode as cp1252, not UTF-8; no source was changed. Prior-stage baseline reading is not represented as a new complete literature review.

New substantive dependency: A016 run 20261014T075009Z-fleet05-A016-addressing-benchmark, REPORT sections 1--5: root reference, marginal CE transport, first conversion, second query and constant-terminal obstruction. Also read A018 run 20261014T051305Z REPORT and A019 run 20261014T055119Z REPORT for the supplied joint reference and zero-row scope. A016 already completed our old NEXT; this stage continues through all remaining queries instead of repeating it. B04's obsolete initial finite-search assignment is superseded in dispatch by this productive continuation, not disputed mathematically. Math recall returned general restriction and Booleanity guards, but no card supplies the new bank theorem; no recalled claim is a proof dependency.

## complete derivation or exact first unsupported line

1. **Fixed-reference transport.** For any supplied finite-cost Q and physical query i, write Q'=sum_e Q(e,T). Parseval applied to the two actual restrictions gives avg_b P_(f_b)(T)=sum_e P_f(e,T). Hence

CE(f,Q)=avg_b CE(f_b,Q')+L_i,
L_i=sum_(e,T) P_f(e,T) log2[Q'(T)/Q(e,T)]>=0.

Support is valid because a positive child atom has positive averaged mass. Q'(T)>=Q(e,T)>0 on each positive summand. Thus no denominator vanishes and the nonnegative code charges telescope. This is the scoped A016 identity, reconstructed from actual Walsh transforms; it is not a universal construction of Q.

2. **All prefixes with the same Q.** After q and t v queries, put z=2^t d^2. On remaining core labels (u followed by k-t v bits), the core reference marginal is

Q_t(empty)=(1+z)/2,
Q_t({u})=(1-2d+z)/2,
Q_t(T)=z/2 otherwise.

It is normalized, strictly positive for k>=3, and the full reference still has the displayed uniform gate conditional and the same mask reference. Exactly one v prefix is active, with probability 2^-t. There h_q=chi_u off the remaining all-zero v event and (-1)^q on it; every inactive prefix is exactly chi_u. This identity, not an approximate symmetry, reduces the full history calculation to the active and inactive cases for both q signs.

Let C_t be the full expected CE after those t v queries, and I_t the full expected remaining physical influence. Direct physical edges give

I_root=(3+kd)/2,
I_t=3/2+(k-t-1)d/2.

The removed influence is (t+1)d/2. If L_[t]=C_root-C_t is the complete cumulative code charge, the signed reserve is exactly

R_t=4I_t-C_t=R_root-[2(t+1)d-L_[t]].

For the common child spectrum P, set c=CE(P,(P+point_empty)/2). Its entropy is H_k=eta((1-d)^2)+(2^(k+1)-1)d^2(2k), and its KL is at most 1. Since H_k<4(k+1)d, C_root=c/2+3 and R_root>5/2-2d. Since L_[t]>=0,

R_t>5/2-(2k+4)d>=5/4

for all k>=3 and 0<=t<=k. The endpoint inequality uses that (2k+4)2^-k decreases for k>=3. No terminal deficit is discarded: if D_t=E(CE-4I)_+ and N_t=E(4I-CE)_+, then N_t-D_t=R_t. The checker retains both separately at every depth. This is an expected signed certificate; it does not assert that every history has its own nonnegative local reserve.

3. **Final terminal costs and positive deficit.** After all v queries, the core marginal is ((1+d)/2,(1-d)/2). At every inactive history the core is chi_u, with complete terminal cost

C_par=5-(1/2)log2[(9+d)(1-d)].

At the two active histories h=+1 and h=-1, both complete terminal costs are

C_con=5-[5log2(9+d)+3log2(1+d)]/8.

Their influences are respectively 3/4 and 5/4; the inactive influence is 3/2. Therefore C_end=(1-d)C_par+d C_con. We have C_par>27/8 and C_con>23/8, by 9^4<2^13, (73/8)^4<2^13 and (9/8)^4<2. Thus C_end>53/16. Also C_con<25/8 because log2(9+d)>3. Only the positive constant history can have a terminal deficit, and its weighted positive deficit satisfies

D_end=(d/2)(C_con-3)_+<d/16<=1/128.

The A016 sign C_con>3 for k>=6 follows from (9+d)^5(1+d)^3<2^16, monotonicity in d, and the exact endpoint 577^5*65^3<2^64. All costs retain the unused ghost atoms in the original reference.

4. **Original half-core bank, no renewal.** The stage5 named reserve is S=2I(h_q)-c/2=2+2(k-1)d-c/2. Let J=C_root-average fresh child CE be the exact already-booked first insertion, and E=C_0-average fresh child CE the conversion to the inherited marginal. As A016 derives, 0<=E<d^2: only the empty-data gate conditional changes, and its conditional KL is bounded by chi-square/ln2 with ln2>1/2. The first debit obeys J<5/8. Carry this exact J forward rather than pretending that the full conservative ceiling was an actual expense.

The sum of subsequent query charges is C_0-C_end. Consequently the total debit, INCLUDING conversion, is

J+(C_0-C_end)=C_root-C_end+E.

The remaining SAME reserve is therefore

S-[J+C_0-C_end]=C_end-[c+1-2(k-1)d]-E.

For a uniform all-k bound, ln2>2/3 gives

H_k<(4k+3)d-(2k+3/2)d^2.

Indeed eta((1-d)^2)<(2d-d^2)/ln2 and the remaining entropy is exactly (4kd-2kd^2). Thus

c+1-2(k-1)d<2+(2k+5)d-(2k+3/2)d^2<=417/128.

At k=3 the last expression is 417/128. At k>=4 its upper bound 2+(2k+5)2^-k is decreasing and at most 45/16<417/128. Combining C_end>424/128 and E<2/128 leaves more than 5/128. Paying D_end<1/128 separately still leaves more than 1/32. This is one explicit allocation of disjoint expenses from the original S; no bank is regenerated at a descendant. It is separate from, and consistent with, the full signed physical-influence reserve R_t.

5. **New nonconstant local-eligibility falsifier.** At the actual history q=0 and v_1=...=v_(k-1)=0, the remaining core is the two-bit point defect chi_u off v_k=0 and +1 on it. It is nonconstant. Its full activation has I=11/8, while its inherited full reference costs

C_near=6+k/4-[17log2(18+d)+3log2(2+d)+4log2(2-3d)]/32.

For k>=8, d<=1/256. The exact integer inequalities (4609/256)^4<2^17 and (513/256)^4<2^5, together with 0<2-3d<2, imply that the bracket is strictly below 80. Hence C_near>7/2+k/4>=11/2=4I. The denominator 2-3d is positive throughout. Thus even keeping both physical branches nonconstant does not guarantee inherited rate-4 eligibility. The history has probability d after q is included. Its cost grows with k but its weighted contribution is of order kd, consistent with the signed reserve. This does not refute FEI or the supplied-reference telescoping identity.

**First unsupported universal line:** an arbitrary Boolean core must admit a constructible initial reference and a conserved source bank that cover these signed profile costs under a proper query, without knowing its Fourier entropy. This stage proves that conservation on the fixed rare-query family; it does not supply the arbitrary-core premise. A local eligibility requirement is now falsified even before the constant endpoint.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the search. Frozen k3..8, six families, maximum dimension13; pilot k3; every q/v prefix represented exactly by active/inactive histories with their physical probabilities. Integer Walsh, direct physical edges and Fraction atoms verify full reference normalization/support, closed costs, every transport identity, signed reserve, positive/negative terminal terms and the original-bank allocation. Canonical rational prime-log forms prove exact cancellation; outward range-reduced rational logarithm intervals certify strict signs. These reuse A020's archived arithmetic helper, not A016's verifier. Every completed k is checkpointed to out/CHECK.json.

Commands: `python -X utf8 code/check.py --pilot` and `python -X utf8 code/check.py` from this run. Final counts and runtime are in out/CHECK.json and final receipt. The first pilot passed. The first full run rejected the unnecessary assertion that every intermediate nonconstant leaf is rate4 eligible. The corrected checker explicitly records signed positive deficits and negative credits; it does not weaken the target reserve assertion. out/FIRST_FAILURE.json records this failure and its mathematical cause. No floating tolerance, dimension escalation or failed sign is accepted. The nonconstant witness above is an analytic consequence, separately checked at k8.

The Lean check of the rational reserve-conservation algebra returned RUNTIME_UNVERIFIED after124.4 seconds; it proves nothing. Mathematical rung: analytic proof with exact finite validation, pending independent review; NOT Lean-checked. No new broad universal candidate is opened. Jobs estimate95MB and cap checker work at60seconds; no job is expected above300MB, so memok admission is inapplicable. Actual peak RAM is not measured. Compute snapshot status was ok with13GB available RAM and8.1GB disk free; slow-state readings showed bulk I/O, not an InventorySvc storm. No running work was stopped. No git, network publication, GPU, detached process, other-agent edit or research-claim write to the brain was used. Required brain-wake and checklist bookkeeping ran under session instructions.

## proof dependencies and changed downstream conclusions

The starting family/reference comes from A020 stage5 and the marginal continuation from A016 stage6. Their formulas are independently reconstructed by our checker from actual Boolean tables and one fixed Q. A016's exact two-query and constant-terminal interface is consumed without altering source claims or asserting independent acceptance of its entire report. The new continuation through every private query and nonconstant penultimate falsifier are self-contained above. No universal FEI bound is a dependency. Arbitrary real spectral measures cannot replace these Boolean truth tables.

A016/A018/A019/B04/A090/A091/A092/A094/B20 should retain signed terminal release instead of insisting on local inherited eligibility. A nonconstant fallback does not repair that eligibility shortcut. No shared claim or packet registry was changed. Source hashes and local evidence are receipts, not independent review or downstream adoption.

## one next mathematical action and independent reviewer

Replace the private point event by one general Boolean activation whose restrictions have unequal spectra, while retaining this root Q, exact prior cost and signed reserve. Derive a sufficient condition on its erased reference marginals for the total terminal positive deficit to be funded once. A016 and A019 should reconstruct the all-prefix bank; A090/A091/A094 should challenge the nonconstant witness and signed terminal accounting. The first unpaid step is a reference-relative potential valid beyond this flat point-event law.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code/, frozen spec and checkpoint outputs are saved inside A020 only. Finalizer checks exact protocol keys, JSON parsing, statement hashes, identical progress/delta, two-line STATUS, file sizes and readback hashes. out/PERSISTENCE_RECEIPTS.json records local persistence. Independent review, supervisor adoption and mirror verification remain pending. No external persistence is claimed.

## Universal bridge

This stage moves C024 history transfer and B04's C019 stopping-tree payment by carrying the SAME reference and the exact original debit through all k remaining private queries, with signed physical reserve>5/4 and a one-use half-core reserve leaving>1/32 after all query charges, conversion and final positive terminal deficit. It also refutes automatic descendant eligibility on a nonconstant penultimate child for every k>=8, strengthening A016's constant-leaf warning. Universal initial-reference construction and signed-bank conservation for arbitrary unequal spectral children remain unpaid. NEXT replaces the flat point event by one nonflat activation while retaining the reference and source bank, because that attacks the exact history invariant needed for full FEI rather than extending a finite census or claiming the supplied-reference identity solves the conjecture.
