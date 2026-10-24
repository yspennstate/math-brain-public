# A020 stage 5: a true-positive row defeats the balanced-child reference repair

Full FEI remains OPEN. Nearly identical biased children defeat the extension of A019's balanced-child zero-row repair: an essential query of disagreement 2^-k has net reference surcharge bounded below by1/32 bit. The troublesome row has positive true mass, so the absent-frequency convention cannot repair it. All core and full-function references are rate4 eligible, and the actual query is K1 good. One explicitly unused terminal bank pays this one insertion. No stated A019 theorem or FEI claim is refuted.

## exact target, quantifiers, hypotheses and units

All bits are independent uniform 0/1 bits, chi_b=(-1)^b, outputs Boolean signs, entropy/CE/KL in bits. For every k>=3 let v be k private bits, A=1_{v=0}, delta=2^-k, and define an essential private query q and another private bit u by

h(q,u,v)=chi_u(1-A)+chi_q A.

Its children are h_0=chi_u+(1-chi_u)A and h_1=chi_u-(1+chi_u)A. Let s on two fresh shared bits be a sign point defect with mean1/2, so all four squared Fourier coefficients are1/4. Form F=1 on private gate x0 and h*s on x1. All child/core/activation references below are specified and normalized before spectral sampling.

Supply Q_b=(P_b+delta_empty)/2 to child h_b. Incoming Q_h is the actual queried-frequency conditional lift of average(Q_0,Q_1), with queried frequency absent on ZERO true unqueried rows. Use the SAME Q_s=P_s at all nodes. Activation uses the joint one-physical-label reference of A018: data prior (Q_h tensor Q_s+delta_empty)/2, lifted by actual gate-frequency conditionals. Its posterior-label KL refund is D. Define D_core=avg child core KL-parent core KL and Lambda=avg D_child-D_parent-D_core/2. The false diagnostic is Lambda<=K Pr(h_0!=h_1) for an absolute K under this support-aware rule without the balanced-child hypothesis. The failure also holds when pricing by actual F-query influence, which is half that disagreement.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot2026-10-14 06:23 UTC, B04 STREAM_NOTES.md v2 unchanged2026-10-11 23:25 UTC, own STATUS.md and prior stage report, and EXECUTION_PROTOCOL.json in full, revision2026-10-11-execution-v2. Required campaign/context reading is carried from earlier stages; no new external theorem or literature claim is used.

New full reads: A018 run20261014T051305Z-account05-A018-shared-data-collision-law REPORT.md/CLAIMS.json, especially sections2,4-6, A018-JOINT-CONSTANT-BRANCH-REFERENCE@1 exact CE/posterior interface; A019 run20261014T055119Z-account05-A019-orthogonality-extensions REPORT.md and CLAIMS.json, A019-PRIVATE-QUERY-ZERO-ROW-TRANSFER@1 sections1,3-5. The latter explicitly leaves biased-child transfer open. Our new family consumes that exact next gap rather than repeating its balanced equal-split example. A018's sharp Gamma optimization is not used here. The earlier positive-excess and internal-pivotal guard results remain in force.

Source hashes are persisted in out/SOURCE_RECEIPTS.json. Current mutable board hashes are close-time byte receipts, not claims of an immutable stage-start snapshot. Only our own prior arithmetic helper is imported; no source-author checker is used.

## complete derivation or exact first unsupported line

### 1. Independent reconstruction of the source reference clauses

For a sign G with mean mu, activation F=1 at x0 and G at x1 has coefficients(1+mu)/2,(1-mu)/2 on the empty data row and two Ghat(T)/2 coefficients on every nonempty row. Thus H(F)=H(G)/2+Psi(mu), where

Psi(mu)=eta((1+mu)^2/4)+eta((1-mu)^2/4)+1-mu^2-eta(mu^2)/2,
eta(t)=-t log2 t.

The erased data law is R=(P_G+delta_empty)/2. With the same physical-label prior r_Q=(Q_G+delta_empty)/2 and true parent conditional gate law, parent KL is KL(R||r_Q). The tagged branch KL is KL(P_G||Q_G)/2. Chain rule gives their difference D>=0, concentrated in the empty data row:

D=(1+mu^2)/2 KL_Ber(mu^2/(1+mu^2) || t/(1+t)), t=Q_G(empty).

Therefore CE_F=c_G/2+Psi(mu)-D. With independent h and s, c_G=c_h+c_s and mu=beta sigma. Expanding the binary expression gives, in natural units,

D_nat=[mu^2 ln(mu^2/t)+(1+mu^2)ln((1+t)/(1+mu^2))]/2,

using the continuous zero conventions. This identity is reconstructed from the tagged law rather than imported from an author implementation.

For a core query with consistent incoming conditional-mixture Q_h, log-sum gives D_core=avg child KL-parent KL>=0 and c_h=avg c_b+Delta H_core-D_core. Substitution yields exactly

CE_parent-avg CE_child=Delta H_core/2+curvature+Lambda,
Lambda=avg D_child-D_parent-D_core/2.

If both children are balanced, the parent empty UNQUERIED row has zero true mass. Assigning queried frequency absent there gives Q_h(empty)=avg Q_b(empty). All activation refunds become (1/2)log2(1+t_s Q_h(empty)), t_s=Q_s(empty). Concavity of this log gives avg D_child<=D_parent, hence Lambda<=0. If instead splitting the zero row equally, the source family h0=chi_u,h1=chi_u times a private point phase, Q_b=(P_b+delta_empty)/2, gives Lambda=(1/2)log2(18/17), D_core=0. Our independent helper reproduces both conventions on k3..8 actual Boolean fixtures. Review verdict: PARTIAL HOLDS for the exact reference/insertion clauses, all-dimensional balanced-child repair and specified equal-split no-go. This review excludes the sharp curvature optimum and the source's complete sparse-family rate4 eligibility proof; no substantive repair is supplied and the original claim statement/hash are preserved.

### 2. Nearly identical children with opposite tiny means

On A=0 both children equal chi_u. On A=1 child0 is constant+1 and child1 constant-1. Thus their physical disagreement is exactly delta, and E h_0=delta, E h_1=-delta, E h=0. They are nonconstant and biased for every k>=3. They differ on the rare entire u-fiber; closeness does not make the interfering Fourier row vanish.

The Fourier coefficients of A on v are all delta. Child0 has coefficient delta on every set with u absent, coefficient-delta on every nonempty v set with u present, and main coefficient1-delta at{u}. Child1 reverses exactly the u-absent coefficients. Hence P_0=P_1=P, with P(empty)=delta^2. Each has one squared mass(1-delta)^2 and2^{k+1}-1 squared masses delta^2. The parent replaces each u-absent child frequency by that same set with q PRESENT; the u-present frequencies have q absent. This is a relabeling of the NONZERO law, so H(h)=H(h_b)=H_k, with additional zero query rows explicitly retained in reference normalization.

Every unqueried row has only one true q sector. Therefore its erased law is exactly P and the parent reference assigns the same Q=(P+delta_empty)/2 to that sector. Child and parent core KL are identically

K_core=1+delta^2 log2(delta^2/(1+delta^2))<=1.

Thus D_core=0, Delta H_core=0. In particular the empty UNQUERIED row has positive true massdelta^2, all at q present. Its reference mass(1+delta^2)/2 is FORCED to q present. Parent full-core empty-set reference mass is zero, while each child's empty-set reference is(1+delta^2)/2. No convention on zero true rows can alter this positive row while retaining the stipulated actual conditional lift.

### 3. A fixed positive net refund loss

The parent mean is zero and Q_h(empty)=0, hence D_parent=0. At either child mu^2=delta^2/4=:a and t=Q_b(empty)Q_s(empty)=(1+delta^2)/8. Both child refunds are equal, so Lambda=D_child and

Lambda_nat=[a ln(a/t)+(1+a)ln((1+t)/(1+a))]/2.

As k tends to infinity this converges to(1/2)ln(9/8), so Lambda tends to(1/2)log2(9/8)>0. A uniform explicit sign suffices. For k>=3, a<=1/256, t>=1/8 and t<=1. The first term is at least a ln a. On that interval -a ln a<=ln256/256<1/32. Further (1+a)ln(1+a)<=2a<=1/128, while (1+a)ln(1+t)>=ln(9/8)>=1/9. Therefore

Lambda_nat>(1/2)(1/9-5/128)>1/32.

Since ln2<1, Lambda_bits>1/32 as well. The upper bound Lambda<=K_core/2<=1/2 follows from the tagged KL identity, because Q_s is exact. Consequently Lambda/d>2^k/32 diverges. The actual F-query influence is d/2, so the failure is stronger in those units. This refutes the proposed balanced-child-free query-price extension, not the stated balanced-child theorem.

### 4. The actual entropy query is K1 good

Actual entropy insertion is only curvature=Psi(0)-Psi(delta/2), because Delta H_core=0. A parent F row has mixed q sectors only on the empty unqueried core/shared row. The two gate-frequency copies each have weights1/4 anddelta^2/16=a/4. Therefore exact query erasure is

B_q(F)=(1+a)/2 h2(a/(1+a)).

Using minority entropy bound and ln2>1/2,

B_q<=a[ (1/2)log2((1+a)/a)+1/(2ln2)]
<a(k+5/2)=delta^2(k+5/2)/4.

At k3, delta(k+5/2)=11/16<2, and this decreases with k. Hence B_q<delta/2=Inf_q(F): the query is K1 good, and its K4 localized derivative bill is zero. Positive Lambda is a reference-transport debt, not an unpaid actual entropy or raw derivative necessity.

For completeness, the prescribed two-shared-bit mask prefix is also K4 good for ANY h: a nonzero shared mask influence is at least1/2, so its influence in F is at least1/4 and B_i<=1<=4Inf_i; on each remaining one-bit child it is0 or1/2. Zero influence implies absent selector coefficients. This elementary finite-width guard is not a new high-influence closure result.

### 5. All references are eligible; one owned terminal bank pays once

Direct physical edges give I(h_b)=1+(k-1)delta and I(h)=1+k delta. For child0, flipping its exceptional point removes one original u-pivotal edge and adds one in each of k private-v directions, yielding the stated correction; the parent uses q on A and u elsewhere and has each v-direction influence delta.

The common spectral entropy is

H_k=-(1-delta)^2 log2((1-delta)^2)+(2^{k+1}-1)delta^2(2k).

Writing epsilon=2delta-delta^2, the inequality -(1-epsilon)ln(1-epsilon)<=epsilon and ln2>1/2 give H_k<4(k+1)delta. Thus c_b=H_k+K_core<=H_k+1, so the child's certified rate4 slack satisfies

S_b=4I(h_b)-c_b>3-8delta>=2.

Parent slack is similarly>3-4delta>=5/2. These are complete references with substantial unused budgets, not unsupported ghost distributions. Full activation references are also rate4: Psi is maximized at0 with value2 (differentiate the displayed expression or use concavity), so CE_F<=c_h/2+3<7/2+2(k+1)delta. Parent I(F)=(3+kdelta)/2, giving margin at least5/2-2delta. Child I(F_b)=[3+(k-1)delta minus/plus delta/2]/2, giving margin at least5/2-5delta>0. All three actual full-reference costs are retained in the exact insertion identity, not replaced by root-only entropy.

To name the one-use payment, each child's unused PRIVATE core half-budget is S_b/2>=1 after paying c_b/2. Mask code costs c_s/2=1 from its rate4 mask half-budget2, leaving1. The gate profile costs at most2 from gate budget2 minus/plus delta; the potential shortfall at the positive-mean child is at mostdelta and can use the mask's remaining1, leaving the private half-budget untouched. The actual insertion has no core-entropy debit and is Lambda+curvature. A019's scalar inequality (or the elementary bound below) gives curvature<delta. Together with Lambda<=1/2 and delta<=1/8, the debit is<5/8, paid once from the averaged untouched private half-reserve>=1, leaving>3/8. No positive core KL refund is claimed, no new bank is created after this query, and no future recursion is authorized by this one-step payment.

For a self-contained coarse curvature bound in this family, the actual private query entropy insertion is B_q+JS_q. The previously independently accepted JS<=2Inf_q/ln2 yields a linear bound with a finite constant, but the sharper curvature<delta can also be read directly from the elementary concavity chord argument for phi(b)=Psi(b/2): -phi''(b)=(1/4)log2((4-b^2)/b^2) is even decreasing in|b|, so its symmetric Jensen gap at child means+/-delta is bounded by delta[phi(0)-phi(1)]=delta[(9/8)log2(3)-1]<delta. Only this elementary bound is needed for the named bank; the source sharp optimum is not independently accepted as part of the review.

### 6. What fails and what remains unsupported

Unlike A019's equal-split failure, the row here is true-positive and uniquely forces query-present reference mass. The balanced-child absent-frequency repair is not robust under arbitrarily small nonzero opposite means. Discarding Lambda, pricing it solely by removed query influence, or treating the zero-row convention as a repair on positive true rows is false. All existing proved claims remain valid at their stated scopes.

The first unsupported universal line is an inherited reference policy or conserved certified child bank that pays successive positive Lambda terms on multiple biased-child exposures without renewing the same half-core slack. This family has enough unused slack for one paid insertion; it does not imply such slack always exists or telescopes through arbitrary later restrictions. NEXT tests a second essential query of a v coordinate while both core branches remain nonconstant, carrying this EXACT incoming Q_h and its booked debit. A new conditional-mixture reset or fresh exact-spectrum reference would change the question and is not permitted.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded pilot/search: helper A020 opposite-means forced-row v1, k3..8 six actual cases, maximum full dimension13, pilot k3, no symmetry quotient. Integer Walsh, physical edges and Fraction normalization check every supplied core and full activation atom. Own range-reduced40-term logarithm helper has a proved geometric tail; exact forms are canonical rational prime-log sums, so algebraic zeros are canceled before sign enclosure. Trial factoring is bounded by the fixed small integer arguments of this domain, not a large-dimension search.

Commands from this run directory: `python -X utf8 code/check.py --pilot`; `python -X utf8 code/check.py`. Corrected pilot PASS1 in0.0994944s. First full completed PASS6 in9.3365555s (saved-case time9.3342295s). A subsequent same-domain validation extension checks full activation rate4 costs, exact CE insertion and the actual query K1 erasure formula; its final receipt is in out/CHECK.json. Each completed k was saved immediately. Six paired source guards independently reproduce balanced-child Lambda0 under absent-frequency assignment and Lambda=(1/2)log2(18/17) under equal splitting.

The initial pilot failed because it compared full parent/child sorted spectral arrays of different lengths, including extra zero queried-frequency sectors. code/failed_v1.py and out/FIRST_FAILURE.json preserve the failure. The repair compares NONZERO laws and separately checks full normalization/support; prime-log canonicalization proves exact zero without a tolerance. out/VALIDATION_EXTENSION.json records the later added same-domain checks. No failed assertion, floating sign, automatic dimension growth or extra precision is accepted.

All jobs estimated80MB, each capped60s; no >300MB job was expected, so memok was not needed. Actual peak memory is not measured. No GPU, git, windows, background job, brain write, external message or other-agent mutation occurred. The infinite family and explicit1/32 bound are proved above, not extrapolated from six cases.

## proof dependencies and changed downstream conclusions

The new family, forced support, exact Lambda, lower bound, physical influences, eligible references and actual K1 erasure are self-contained. A018-JOINT-CONSTANT-BRANCH-REFERENCE@1 is reconstructed only at its exact tagged-reference scope, without Gamma. A019-PRIVATE-QUERY-ZERO-ROW-TRANSFER@1 receives partial independent acceptance of the exact insertion, balanced-child support repair and equal-split obstruction; original statement/hash and unreviewed clauses are retained. No source theorem is repaired. The optional sharper single-bank curvature bound is reconstructed directly; no universal recursive bank premise is used.

B04/A018/A019/A090/A091/A092/A095/A097/B20 should distinguish true-positive empty UNQUERIED rows from zero true FULL-frequency atoms. Near balance is insufficient. The same incoming reference can retain a fixed ghost budget on a row of vanishing true mass, making its activation-label refund drop discontinuously under a forced conditional lift. The available owner in this example is unused certified terminal slack, not the small query influence or exact bad-node bill. No shared registry or prior run was edited.

## one next mathematical action and independent reviewer

Carry the SAME incoming parent core/activation references through a second essential v-coordinate exposure, after booking less than5/8 from the named private half-reserve. Derive the actual child likelihood and remaining bank, retaining both complete nonconstant terminals and the previous q-frequency mass; test whether further positive Lambda can be paid without renewing the bank. A019/A018 review the forced positive-row counterexample and exact refund; A090/A091/A092 audit rate eligibility, K1 erasure and one-use payment. This tests inherited-history transport directly rather than enlarging the rare-query dimension.

## actual persistence receipts or precise save blocker

The four protocol files, code/, out/, frozen spec, discovery checkpoint, exact reference certificates and honest failure/archive records are saved only in A020. Rolling STATUS.md is two lines; WORKLOG.md and LEARNED.md are updated. Final schema/hash/size/JSON readback is saved in out/PERSISTENCE_RECEIPTS.json. Partial source review, new result pending independent review, local persistence, supervisor adoption and mirror verification are distinct; only the first and local save are evidenced here.

## Universal bridge

This stage moves C020/C024 and B04's C019 private-query interface by closing the balanced-child extension mechanism with a true Boolean family: tiny opposite means force a positive unqueried row's reference onto the queried frequency, leaving Lambda>1/32 while essential disagreement2^-k tends to zero, despite complete rate4 certificates and a K1-good actual query. It independently confirms the original balanced-child repair and names a single unused half-core reserve that pays this one insertion with more than3/8 remaining. Universal availability and conservation of that reserve across later biased-child exposures remain unproved. NEXT carries the SAME reference and booked bank through a second real core query, because that addresses the history/ownership gap after the zero-row shortcut has been shown inadequate, rather than producing another isolated low-influence family.
