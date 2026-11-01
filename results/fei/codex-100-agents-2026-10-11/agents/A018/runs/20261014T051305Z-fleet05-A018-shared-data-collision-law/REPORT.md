# A018 stage5: one physical branch label and arbitrary certified terminal cores

Run 20261014T051305Z-fleet05-A018-shared-data-collision-law, B04/A018. Full FEI remains OPEN. A joint physical-branch reference closes the constant-terminal shared fanout with arbitrary supplied non-flat core references, preserving any core rate at least the existing fine profile constant Gamma in(4.872,4.873). The scalar optimum belongs to A060; it is independently reconstructed here and not claimed as a new class or constant. The substantive reference result is a single-use physical budget and exact empty-row KL refund. Replacing a product prior by the joint prior is not a universally nonnegative credit; an eligible six-bit counterexample is certified. A019's internal-pivotal edit theorem independently HOLDS at full stated scope.

## exact target, quantifiers, hypotheses and units

All physical bits are independent fair bits, signs are Boolean, and H, CE and KL use bits. For any r>=1 and arbitrary Boolean private cores g_j(y_j) on mutually disjoint private cubes, define G=product_j g_j and F(z,y)=G(y) at z0, constant1 at z1, with one common fresh physical bit z. Constants and zero true Fourier rows are allowed. Each core comes with a supplied normalized complete finite-cost spectral reference Q_j, cost c_j=CE_Qj(g_j). No universal availability of c_j<=C I(g_j) is assumed.

Put mu_j=E g_j, mu=product mu_j, P_j=ghat_j^2, P=product P_j, Q=product Q_j, R=(P+delta_empty)/2, q=(Q+delta_empty)/2, and let nu_F(A|T) be the actual parent conditional shared Fourier law, fixed from the two known branch spectra. On zero true rows choose any fixed normalized conditional. The normalized parent reference is Q_F(A,T)=nu_F(A|T)q(T).

Let eta(x)=-x log2 x with eta(0)=0 and

Psi(mu)=eta((1+mu)^2/4)+eta((1-mu)^2/4)+(1-mu^2)-eta(mu^2)/2.

Then

H(F)=H(G)/2+Psi(mu),
I(F)=sum_j I(g_j)/2+(1-mu)/2,
CE_QF(F)=sum_j c_j/2+Psi(mu)-D_ref,
D_ref=sum_j KL(P_j||Q_j)/2-KL(R||q)>=0.

The refund is exactly the physical-label posterior KL, concentrated in the empty private row:

D_ref=(1+mu^2)/2 * KL_Ber(mu^2/(1+mu^2) || Q(empty)/(1+Q(empty))).

For Gamma=max_{0<d<=1}[4-4d+Ppair(d)/d], Ppair(d)=eta((1-d)^2)+eta(d^2)-eta((1-2d)^2)/2, A060's existing fine profile result gives 4.872<Gamma<4.873 and Psi(mu)<=Gamma(1-|mu|)/2. A self-contained simpler fallback is Psi(mu)<=gamma_0(1-|mu|)/2 with gamma_0=4+5/(8ln2)<5.

If every supplied c_j<=C_j I(g_j), the same normalized parent reference obeys CE_QF(F)<=max(Gamma,C_1,...,C_r) I(F). Private inputs are paid at their physical half-branch weight, and the single actual shared influence is paid once. This conditional reference transfer supplies no arbitrary Boolean core certificate and no universal nonconstant-fallback theorem.

## sources actually read, revisions and theorem locators

Read BOARD.md, supervisor snapshot2026-10-14 05:11UTC, relevant entries plus the previously truncated middle; B04 STREAM_NOTES v2 still2026-10-11 23:25UTC; own STATUS and stage4 report; full EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2. Required earlier campaign/paper context is retained and not reasserted as new theorem evidence.

New dependency: A019 runs/20261014T025011Z-fleet05-A019-orthogonality-extensions REPORT sections1-4 and CLAIMS.json, A019-INTERNAL-PIVOTAL-EDIT-ACCOUNT@1. A020 LEARNED stage4 explains why positive W/raw sufficient-ledger failure need not reflect actual unpaid entropy, and why biased core plus biased nonlinear mask creates the next coincident empty row. A019 independently confirms our previous eleven-bit falsifier at its finite scope; its review is not treated as acceptance of all our asymptotic/reference assertions.

During the derivation, read A060 LEARNED, then runs/20261014T033739Z-fleet05-A060-composition-sharpness REPORT, PROOF sections1-4 and CLAIMS. Our Psi is exactly its fine profile dG(d), so the scalar optimization is consumed, with an independent positive-series reconstruction below, instead of reported as another new scalar result. A060-SHARP-POINT-CONTROLLER-LEDGER-CONSTANTS@1 receives a partial independent HOLDS review only for the fine profile supremum, unique maximizer/enclosure and dyadic realizability; its full coarse/fine controller ledger and tensor clauses are not reviewed here.

Read threshold_paper_38pp.txt Proposition8.9 lines around2550-2588 to identify the already known activation/composition baseline. The new result is a reference/ownership application to the shared-label collision gap, not a priority claim for activation entropy or read-once closure. Only A018 stage2 Fraction log definitions are imported; their main search is excluded. No A019/A060 checker or source utility is imported. Source receipts bind available bytes at stage close; mutable board/rolling hashes do not imply immutable start snapshots.

## complete derivation or exact first unsupported line

### 1. Independent full-scope A019 reconstruction

For a=g, b=g(-1)^1_E and D=g1_E, partition each directed private edge using the real Dirichlet normalization (h(x)-h(x^i))^2/(4*2^n). An internal pivotal edge contributes equally to J=(Ia+Ib)/2 and kappa=I(D); an external pivotal edge contributes to J only. On a crossing edge one sign child is pivotal and the other is not, so J has twice the derivative contribution. Crossing contributions cancel in2kappa-J. Thus exactly2kappa-J=P_in-P_out, and half-private iff P_in<=P_out. Point edits have kappa=n2^-n/2; if r original incident directions were pivotal, J=I(g)+2^-n(n-2r)>=n2^-n because I(g)>=2r2^-n. No flat spectrum is required.

For an arbitrary shared edge and independent private modules, write C_j=sum |T| ahat_j(T)bhat_j(T), q_j=E a_j b_j and Q_-j=product_{h!=j}q_h. Product cross-energy is sum C_j Q_-j, so

I(D_product)=sum_j[(1-Q_-j)J_j,edge/2+Q_-j kappa_j]
           =sum_j[J_j,edge+Q_-j(2kappa_j-J_j,edge)]/2.

For an unchanged mask, the effective edit is EMPTY: kappa=0 and correction=-J, not0. For changed edits of density<=1/2, q_j>=0. Under P_in<=P_out every edge account is <=J_j,edge/2. Averaging both directions of the two-shared-bit prefix uses one account u_j<=J_j. Parseval gives T_private=2J+W, with the stated signed edge-average W, and adds the root mixed charge2E_zw. Since2E_zw<=d, W<=0 impliesT<=2J+d<=2I. The two-bit source witness g=[1,1,-1,1], E={0,2} has J1,kappa3/4,q0 and refutes the unconditional half-private extension.

For arbitrary supplied four-leaf references, their physical mixture with the actual parent conditional is normalized, and log-sum bounds its data KL by the physical average child KL. Hence CE_root<=cbar+Delta_block H. The previously independently accepted B04-NODE-BOUNDARY@1 on the prescribed two-query tree gives CE<=cbar+T+(3/ln2)d; the stated conditional max(C+2,1+3/ln2) bound follows. This reconstructs every clause at its stated scope without repair. It does not infer a free terminal reserve or a necessary entropy obstruction from W>0.

### 2. One joint physical-label reference

For T nonempty, the constant branch has coefficient0 and the parent's two shared coefficients are Ghat(T)/2. Their squared masses are P(T)/4 each. On T empty the coefficients are(mu+1)/2 and(mu-1)/2. Summing these entropy packets gives H(F)=H(G)/2+Psi(mu). The private spectral influence is I(G)/2; physical shared disagreement is d=(1-mu)/2. Independence of private blocks makes H(G)=sum H(g_j) and I(G)=sum I(g_j).

The data law is R=(P+delta_empty)/2. Form q=(Q+delta_empty)/2 using the SAME one physical label. Q_F=nu_F q is normalized because every conditional sums to1, including zero true rows. Finite supplied CE ensures that q is positive on every positive true row, so the parent CE is finite. Its exact debt is KL(R||q), since its selector conditional matches the true conditional.

Apply the KL chain rule to the tagged law of (b,T), with b fair and branches P,delta_empty, and reference branches Q,delta_empty. Its joint KL is KL(P||Q)/2; its marginal data KL is KL(R||q). Their difference is posterior-label KL D_ref>=0. At every nonempty row the actual and reference label are both branch0, giving no posterior cost. At the empty row the actual label probability is mu^2/(1+mu^2) and the reference probability is Q(empty)/(1+Q(empty)). This proves the displayed exact binary refund formula, not just its log-sum upper bound. If mu=0 and Q(empty)=0, both Bernoulli parameters are0 and the cost is0; finite CE excludes the unsupported positive-true/zero-reference case.

Now CE_QF=H(F)+KL(R||q)=sum c_j/2+Psi-D_ref. This retains every terminal CE and uses a single shared physical prior. It does not assume cheap arbitrary terminals or erase a remaining nonconstant fallback.

### 3. Identify and consume A060's fine profile

Write d=(1-mu)/2. Then Psi(mu)=4d(1-d)+Ppair(d), so Psi(mu)/d is exactly A060's G(d). The symmetry Psi(mu)=Psi(-mu) means that values d>1/2 cannot exceed their folded ratio at1-d. No context-dependent character folding is performed or used to reduce the actual physical influence.

Here is a different strict-concavity proof and a self-contained fallback bound. For 0<d<1/2, expand

(1-d)^2 ln(1-d)=-d+3d^2/2-sum_{k>=3}2d^k/[k(k-1)(k-2)].

It follows that

ln2*G(d)=4ln2+d(3-4ln2-2ln d)
        -sum_{k>=3}(2^(k+1)-4)d^(k-1)/[k(k-1)(k-2)].

All coefficients of the subtracted series are positive. Its second derivative together with -2/d is strictly negative, proving G''<0. Series differentiation is valid on compact subintervals of(0,1/2); endpoint values follow by continuity. The coefficient k3 is2. Discarding all higher negative terms and using the tangent of -dln d at d=1/4 gives

ln2*G(d)<=4ln2+1/2+d-2d^2<=4ln2+5/8.

Indeed -dln d<=1/4+(2ln2-1)d, and5/8-(1/2+d-2d^2)=2(d-1/4)^2. Thus gamma_0=4+5/(8ln2)<5 is a safe elementary bound, not a new sharp constant.

For the existing sharp Gamma, directly differentiate Ppair or the equivalent series. G'(1/8)>0 is certified by7^126>3^60*2^256, and G'(1/4)<0 by3^5<2^8. Strict concavity gives one root and the global maximum there; symmetry handles d>1/2 and the limit at0 is4. Our own24 rational derivative bisections and a concave tangent at the lower bracket certify4872/1000<Gamma<4873/1000. This uses A018's independent80-bit rational-log arithmetic and the series proof rather than A060's source checker/integral proof. Any dyadic d is realized by an actual Boolean core with that negative fraction. Continuity and dyadic density prove necessity of the fine profile supremum. The scalar optimization was already done by A060; this is a scoped review and its reference application.

### 4. Preserve the supplied rate with one physical reserve

Let C=max(Gamma,C_1,...,C_r). Since D_ref>=0,

CE_QF<=sum_j c_j/2+Gamma(1-|mu|)/2
      <=C[sum_j I(g_j)/2+(1-mu)/2]=C I(F).

Each supplied core cost is paid at its actual half-branch probability. The selector term uses only its own physical influence, once. No additional rate2 is charged per merge, no module slack is assumed absent its certificate, and no loss-only bound for the previously refuted shared-product excess is invoked. Repeating this construction within the restricted constant-terminal/disjoint-private grammar preserves the same C, PROVIDED references are supplied at its terminal cores and the construction is used with the actual functions. This is a closure/application of known composition calculus, not a universal reduction that manufactures terminal references.

The previous eleven-bit positive-excess control survives: using exact point-core references, the new q equals actual R, so its complete CE is H(F). The separately lifted module-marginal product reference costs H(F)+TC. The difference is exactlyTC; G=H(F)-sum H(f_j)>0 remains positive. Thus the signed collision is not eliminated by asserting entropy subadditivity. The reference uses one physical branch label rather than r auxiliary ones.

### 5. Changing arbitrary supplied priors is signed

For comparison define q_sep(T)=product_j[(Q_j(T_j)+1{T_j=empty})/2] and q_joint=(product_j Q_j+delta_empty)/2. Both lifted parent references have the same true conditional selector law. Therefore

CE_sep-CE_joint=E_R log2(q_joint/q_sep).

For exact core references this equalsTC>=0. For arbitrary supplied references its sign is not guaranteed, even when the references satisfy a valid core rate. Take private point-defect cores of dimensions3 and2, whose means are3/4 and1/2 and influences3/4 and1. Give them uniform core references, with costs3 and2 respectively; both satisfy c_j<=5I_j. The six-bit parent has I=19/16, and exactly

CE_sep-CE_joint=[128ln2+73ln11-127ln3-80ln5]/(128ln2)<0,

proved without approximation by2^128*11^73<3^127*5^80. The parent rate guarantee from the DIRECT joint-reference proof remains valid; it does not rely on labeling this change a refund. This is not a negative D_ref: that posterior KL is always nonnegative, while the comparison of two different data priors is a separate signed quantity. Neither may be spent twice.

### 6. Exact first unsupported universal line

This transfer requires one actual branch to be constant. Replacing it by an arbitrary nonconstant fallback makes the physical-label posterior likelihood depend on every spectral row, not just(mu^2,Q(empty)). The first unsupported line is a noncircular bound for that full signed row transfer, using the SAME supplied core references and one genuinely unused child/physical reserve after a real core restriction. Terminal CE remains part of the bill. Mean-only profiles and the false shared entropy-subadditivity or loss-only prices cannot replace it.

NEXT makes one nonconstant fallback/actual core-data exposure, carries the joint reference and rowwise likelihood statistic, and tests whether an owned certified child surplus pays its signed change. The A019 internal-pivotal correction and A020 raw-overcharge control must both remain in the ledger. A free reset to an exact unknown core spectrum is not authorized by this conditional transfer.

## executed validation with domain, arithmetic, commands and outputs

Every job specification preceded its job. Memory estimate80MB per job, maximum60seconds; no planned >300MB job, so memok gate did not apply. Peak memory is not measured. Jobs ran sequentially without GPU, randomization, automatic dimension escalation, windows or background helpers.

From this run directory:

- `python -X utf8 code/check_reference.py --pilot`:8 cases,192 exact checks,0.106s.
- `python -X utf8 code/check_reference.py`:534 fixed cases,14474 checks,9.374s. All278 single-core tables through n3 and256 ordered two-private-bit pairs;128 non-flat cases. Each tests actual-spectrum and uniform supplied references.1002 reference cases satisfy the tested rate6 core hypotheses; remaining references still satisfy the general normalized CE/profile transfer but are not admitted as rate6 certificates. Own recursive Walsh, separate iterative Walsh, physical edges, exact profiles, every complete reference atom and zero true row are checked. Completed cases saved immediately.
- `python -X utf8 code/check_prior_change.py`:two fixed reference choices on the3+2-private-bit witness,27 checks,0.021s; exact positive TC for actual references and negative change for eligible uniform references.
- `python -X utf8 code/check_control.py`:eleven-bit prior-stage positive-excess control,31 checks,0.657s; normalized new/old reference identity, exactTC refund, positive excess and supplied/core/root rate5 checks. The already saved pure-integer falsifier is source-bound, not re-run as a discovery.
- `python -X utf8 code/review_internal.py --pilot`:16 one-bit core/edit pairs,40 checks,0.001s.
- `python -X utf8 code/review_internal.py`:272 all one/two-bit core/edit pairs plus256 actual two-shared-mask products,3892 checks,2.771s.80 core/edit pairs violate unconditional half-private,52 products have positiveW; all exact signed identities pass. The unchanged-edge correction=-J is explicitly checked.
- `python -X utf8 code/check_analytic.py`:6 fixed algebra/integer/ln2 checks,0.001s, including the negative uniform-prior integer sign and the fact selector rate4 alone is insufficient for the profile at mu1/2.
- `python -X utf8 code/review_profile.py`:24 certified derivative bisections,28 checks,0.089s; distinct all-parameter concavity proof and exact rational tangent give the existing Gamma enclosure. No scalar grid or floating extrapolation is used.

Total final receipt checks18690. Entropy is handled by exact Fraction prime-log identities; interval signs use range-reduced36-term positive atanh series with proved geometric tail and outward2^-80 grid. Profile review keeps rational log arguments intact rather than factoring large numerators. No assertion failure, precision escalation or mathematical repair occurred. Finite validation supplements the all-parameter proofs above.

## proof dependencies and changed downstream conclusions

A019-INTERNAL-PIVOTAL-EDIT-ACCOUNT@1 receives full-scope independent A018 HOLDS without repair. Its CE clause retains the already independently accepted B04-NODE-BOUNDARY@1. A060-SHARP-POINT-CONTROLLER-LEDGER-CONSTANTS@1 receives scoped independent HOLDS for the fine profile optimization/enclosure/Boolean realizability only; its full claim stays outside that review's acceptance scope. The new A018-JOINT-CONSTANT-BRANCH-REFERENCE@1 is a conditional reference interface, with fully supplied arbitrary-core CE, finite-cost and one-constant-branch hypotheses. The sharper Gamma part uses the independently reconstructed fine profile; the simpler gamma_0<5 proof is self-contained. This is not an assertion of a new optimal activation class result.

B04/A016/A019/A020/A056/A060/A086/A090/A091/A095/A096/A097/B20 may use the exact one-label mixture and binary posterior refund as a non-flat constant-fallback control. Keep the negative eligible prior-change witness: an exact-spectrum TC refund must not be generalized to arbitrary priors without the signed likelihood bill. Previous entropy-excess and folded/internal ownership results are unchanged. No shared registry, earlier run, other-agent file, brain, git or messaging operation occurred.

## one next mathematical action and independent reviewer

Expose one actual private core coordinate while a nonconstant fallback remains, preserving both supplied child/terminal references and the same joint-label prior; derive the rowwise signed posterior cost and test payment from one certified unused child surplus. Use the eleven-bit positive-excess family, eligible negative prior-change pair and A019's positive-W two-bit core as mandatory controls. A090/A091 review the new normalized reference/rate application; A060 challenges profile identification and its scoped independent review; A019/A095/A097 audit posterior versus prior-change credit ownership.

## actual persistence receipts or precise save blocker

The four protocol files, code/, out/ frozen specs, complete-reference/control/negative-prior certificates, independent reviews and source receipts are saved in the assigned run. STATUS.md remains exactly two lines; WORKLOG.md and LEARNED.md are updated. out/PERSISTENCE_RECEIPTS.json verifies claim/progress schemas, declared statement hashes, identical packet delta, all report fields, final Universal bridge paragraph, JSON parsing and20MB file limits. The new interface independent review, shared adoption, supervisor copying and mirror verification remain distinct and pending.

## Universal bridge

This stage advances C020's complete-reference collision interface from pointed terminals to arbitrary supplied non-flat private cores with a constant physical fallback: a single joint selector prior retains every terminal CE, localizes its exact nonnegative KL refund to the empty row, and preserves the existing core rate whenever it is at least A060's Gamma<4.873, with no repeated additive merge tax or duplicated private reserve. It advances C019 by fully reviewing A019's signed internal-pivotal account and certifying that a valid reference change can have negative credit even in an eligible six-bit pair. No universal nonconstant-fallback or history payment follows; arbitrary terminal certification and rowwise likelihood/slack availability remain open. NEXT replaces the constant fallback once under an actual core exposure, carrying the same references and one unused child surplus, because it tests the exact hypothesis that concentrates the posterior cost rather than producing another isolated composition constant.
