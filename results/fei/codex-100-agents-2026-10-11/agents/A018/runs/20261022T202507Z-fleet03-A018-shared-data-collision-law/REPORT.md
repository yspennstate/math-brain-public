# A018 stage17: equal-mean private queries preserve the activation reference refund

The two private children may be biased. Equality of their means suffices for a nonpositive net activation-reference surcharge, with arbitrary supplied complete child references and any independent Boolean mask. This extends the balanced-child part of A019's existing interface. It does not supply inexpensive references for arbitrary cores or settle FEI.

## exact target, quantifiers, hypotheses and units

All cubes are uniform, all signs Boolean, and all entropy, cross entropy CE and KL are in bits. Let h(q,u) have children h_0,h_1 with the SAME mean beta in [-1,1]. Let s(w) be any Boolean mask on disjoint bits, sigma=E s, and let F(x,q,u,w)=1 on x0 and h(q,u)s(w) on x1. Query the actual core bit q. Its two F children can both be nonconstant. Supply normalized finite-cost complete references Q_0,Q_1,Q_s. The incoming core reference MUST already equal the actual q-frequency conditional lift of qbar(U)=(Q_0(U)+Q_1(U))/2. On zero true rows fix q-frequency absent, before any sampling. The same Q_s and supplied Q_b occur throughout. An arbitrary unrelated incoming reference cannot be replaced by this one.

Write P_v for actual core squared spectra, c_v=CE(P_v,Q_v), K_v=KL(P_v||Q_v), a_v=Q_v(empty), a=(a_0+a_1)/2, t=Q_s(empty), and m=sigma^2. Define

D_c=(K_0+K_1)/2-K_h,
E=beta^2 log2[a/sqrt(a_0 a_1)],
J=log2(1+t a)-[log2(1+t a_0)+log2(1+t a_1)]/2,
p=m beta^2.

When beta=0, define E=0 without taking log of a possible zero. Finite CE makes both a_b positive when beta!=0. Then 0<=E<=D_c and J>=0. For the SAME physical-label activation references from A018/A019, the exact insertion is

CE(F)-[CE(F_0)+CE(F_1)]/2 = [H(h)-(H(h_0)+H(h_1))/2]/2 + Lambda,
Lambda= -[D_c-m E+(1+p)J]/2 <= -[(1-m)E+(D_c-E)]/2 <=0.

This is an all-dimensional conditional reference theorem. No universal terminal CE bound is assumed or produced.

## sources actually read, revisions and theorem locators

Execution protocol revision2026-10-11-execution-v2 was read in full. Current owner deadline2026-10-23T14:49Z supersedes its old endpoint. Read the current BOARD snapshot2026-10-22T20:25Z, B04 lead v2 (2026-10-11T23:25Z), A018 STATUS and LEARNED, stage5 REPORT, and run-directory history; later A018 fleet05 folders lack substantive reports, so the saved stage5 NEXT remains the productive handoff. Required campaign README/CURRENT_STATUS, B04 registry/packet/obstruction locators, STREAM_NEXT_ACTIONS, campaign plan B04 acceptance and universal-gap passages, supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING were consulted. The paper text was checked at the shared-data identity/activation sections; the earlier threshold and both percolation versions were consulted for scope. Percolation conclusions are not dependencies of this proof.

Main new source: A019 runs/20261014T055119Z-fleet05-A019-orthogonality-extensions/REPORT.md sections1,3,4, CLAIMS.json claim A019-PRIVATE-QUERY-ZERO-ROW-TRANSFER@1, original digest44b12f41883a5d5aa4b7e99df6db51a5f83e9b3a1105a8e8d8e742ef59b258a1. A020 LEARNED stages5-6 supplies the opposed-small-bias guard and warns against assuming local child eligibility. A019 and A020 rolling files were read directly. Own stage5 A018-JOINT-CONSTANT-BRANCH-REFERENCE@1 supplies the normalized activation construction, independently rederived below. No source-author checker is imported. One two-wording read-only math recall returned no card settling this reference question; unrelated search matches are not premises.

## complete derivation or exact first unsupported line

For coefficients a_b(U)=hat(h_b)(U), R(U)=(a_0(U)^2+a_1(U)^2)/2 is the unqueried row mass. The parent core coefficients are (a_0+a_1)/2 and (a_0-a_1)/2. Its reference is their actual normalized squared conditional times qbar(U). Log-sum applied to the auxiliary physical-child label gives

D_c=sum_U R(U) KL((a_b(U)^2/(2R(U)))_b || (Q_b(U)/(2qbar(U)))_b)>=0.

Only R(U)>0 rows enter this expression. Other reference mass is retained in the normalized lift. At the empty unqueried row, equal means imply a_0(empty)=a_1(empty)=beta. When beta!=0 the q-present coefficient is zero, hence a_h=a. The same equality follows from the specified absent convention when beta=0. The empty-row summand in D_c is exactly E. Every other summand is nonnegative, proving 0<=E<=D_c. This is the KL source that was absent from the purely balanced proof.

For any core node v, set G_v=h_v s, with mean mu_v=beta_v sigma and product reference Q_v tensor Q_s. Its activation has data marginal (P_Gv+delta_empty)/2 and reference marginal (Q_v tensor Q_s+delta_empty)/2; lift by its actual x-frequency conditional. This is normalized and supports every positive true atom. With eta(r)=-r log2 r and eta(0)=0, put Psi(mu)=eta((1+mu)^2/4)+eta((1-mu)^2/4)+1-mu^2-eta(mu^2)/2. Directly squaring the two x sectors gives

CE(F_v)=(c_v+c_s)/2+Psi(mu_v)-A(mu_v^2,t a_v),
A(r,z)=[r log2(r/z)+(1+r)log2((1+z)/(1+r))]/2.

The first term is zero when r=0, including z=0; positive r forces z>0. This is the posterior physical-label KL refund, rather than an arbitrary change of reference prior. Separately c_h=(c_0+c_1)/2+Delta H_h-D_c. Substitution gives A019's exact insertion identity. Here mu_v is identical at parent and both children, so profile curvature is ZERO.

Expanding the three A values at their common r=p gives

(A(p,t a_0)+A(p,t a_1))/2-A(p,t a)=m E/2-(1+p)J/2.

If t=0, finite mask CE forces sigma=0; the identity reduces continuously to zero on both sides. If beta=0, the r log term vanishes without dividing by beta. Concavity of log(1+t z) on z>=0 gives J>=0. Combining the last equation with -D_c/2 proves the exact Lambda formula and sign. The only coefficient bound used is 0<=m<=1, true for the mean of a Boolean sign. There are no limits, infinite sums or dimension-dependent constants.

Consequently, a core query already certified by Delta H_h<=K Pr(h_0!=h_1) induces activation query insertion<=K Inf_q(F), since Inf_q(F)=Pr(h_0!=h_1)/2. It consumes no additional child slack. For a finite consistently referenced core stopping tree whose EVERY reached query preserves its child mean, telescope this inequality with reach probabilities; all complete terminal activation references remain. This is conditional on the actual core query certificates. Such a tree need not exist for a general Boolean function, and a nontrivial biased mean cannot be preserved through a complete reveal to constant leaves.

Independent review: A019's exact insertion and balanced-child absent-frequency repair HOLDS at the original stated scope, by the rowwise KL reconstruction above and the independent exact implementation. This is a PARTIAL review of A019-PRIVATE-QUERY-ZERO-ROW-TRANSFER@1: its separate sharp-curvature optimization and all-k equal-split eligibility/no-go are not newly accepted by this review. The new equal-mean extension is author proof, independent review pending; A018 cannot independently accept its own extension.

The first unsupported universal line is payment of Lambda plus the nonzero profile curvature when beta_0!=beta_1 under the SAME incoming reference and remaining ancestor bank. Opposite tiny means can force q-present at the empty unqueried row and leave a fixed positive Lambda. Therefore equal means cannot be weakened merely to small means or small disagreement. No arbitrary-core bank, good-query existence or FEI implication is claimed.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: out/FROZEN_SPEC.json; checker code/check_equal_mean.py has no candidate-author imports. Pilot: python -X utf8 code/check_equal_mean.py --pilot, all6 equal-mean ordered pairs on one unqueried bit, three independently selected references per child, three masks with exact/uniform references:324 cases,7475 assertions,PASS in0.716s. The spec's pilot case note initially said648; the actual loop and case count are324, with no omitted cases. Full-domain receipt out/CHECKS.json:4104 cases (2160 balanced,1944 nonbalanced),94687 assertions,PASS,87.769294s. This exceeds the frozen60s estimate; the overrun is recorded rather than hidden, with no further domain escalation or full search. Exact spectra are cross-checked by direct character sums; physical disagreement is checked against spectral query influence. Complete CE, actual activation spectra, KL decomposition, insertion identities and the stronger Lambda formula use exact rational prime-log forms. Signs use outward rational36-term atanh enclosures; exact zero forms cancel algebraically, without tolerance.

Boundary specification is frozen in code/check_boundaries.py before execution:144 prescribed cases, biased and balanced essential equal-mean cores, unequal child references, constant signed masks and signed three-bit point masks, plus one A020 opposed-mean k3 guard. It reconstructs the activation Boolean truth table and its independent direct Walsh spectrum. Receipt out/BOUNDARIES.json:144 boundary cases and one opposed-mean guard,2745 assertions,PASS in0.595569s. These are separate from the full census; combined assertions97432, excluding the pilot. The opposed-mean guard must have positive Lambda; it checks that the new hypothesis is substantive.

Before a possible Lean compiler job, required memok.py returned exit1: physical free2.2GB versus required4.0GB, commit free2.5GB versus required8.0GB. No compiler was launched. code/RefundSign.lean formalizes only the final ordered-field sign implication; its source is UNCOMPILED, not a certificate. The mathematical rung is an analytic proof with exact finite checks, awaiting independent review, not Lean-checked. No GPU, remote compute, dimension escalation or job above300MB was used.

## proof dependencies and changed downstream conclusions

The normalized reference construction is A018's existing physical-label mixture. The exact query insertion is independently reconstructed from it and the two-sector Walsh identity; A019's balanced repair is a special case. This theorem removes balance while keeping equal means and extends the mask from the nonlinear two-bit case to any independently supported Boolean mask with a supplied complete reference. No FEI rate improves. The known positive-excess shared-product and negative prior-change controls remain untouched; neither entropy subadditivity nor a universally positive prior-change credit is used. In particular, the new proof subtracts every actual child refund with its correct sign.

## one next mathematical action and independent reviewer

A019/A020 or A090 should reconstruct the exact E,J decomposition independently. Next derive the unequal-mean empty-row likelihood identity and split its signed term into the equal-mean paid part and an explicit contrast remainder; test its payment from ONE already unused supplied terminal bank, retaining both complete terminals and all previous debit. A020's opposed-mean guard must remain positive, so an absolute Lambda<=K disagreement proposal is excluded. This targets the actual unpaid contrast rather than another phase census.

## actual persistence receipts or precise save blocker

The run's four protocol files, source receipts, checker code, frozen spec, validation receipts and local SHA256 manifest are stored under this A018 run. STATUS.md stays two lines, WORKLOG.md and LEARNED.md receive dated entries. Final schema/hash/size validation is recorded in out/VALIDATION.json. Shared adoption, supervisor copying, independent acceptance and remote mirror verification are not observed here. No shared index or other agent file is modified.

## Universal bridge

This stage advances C024 history transfer and B04's C019 interface: every mean-preserving private query has nonpositive net activation-reference surcharge at the SAME supplied references, even with biased nonflat children, and a finite such history telescopes with no added source debit and all terminals retained. It identifies the paid source exactly as the empty-row part of the core-label KL, plus a concavity refund. The unresolved universal step is the unequal-mean contrast remainder, its profile curvature and payment from a single unused ancestor bank; general query existence and terminal supply remain open. NEXT isolates that contrast in the very same identity, which is a direct route toward conserved arbitrary-core histories rather than another isolated class closure.
