# A068: activation-sensitive quadratic contrast

Full FEI remains OPEN. The current owner packet sets the campaign deadline at 2026-10-23 14:49 UTC; older dates in the read-only protocol snapshots are superseded. This stage repairs the weak-pair interface, with an independent quadratic relative phase. It does not claim payment when the common phase and relative phase share control variables, or after an arbitrary inherited control query.

## exact target, quantifiers, hypotheses and units

All entropies and reference costs use bits. Let g_+,g_- be arbitrary Boolean functions on the SAME uniform data cube X. Let beta be a Boolean quadratic F2 phase on a DISJOINT uniform cube Z. Put F=g_+ when beta=+1 and F=g_- otherwise. Set b=E beta, p=(1+b)/2, d=Pr_X(g_+ != g_-), r=rank over F2 of the alternating polar matrix, L=1-b^2, w=Ld, and K=number of nonempty Fourier-support atoms of beta. For nonconstant beta, K>=1, K=2^r if b=0 and K=2^r-1 otherwise. Given ANY complete normalized references Q_+,Q_- supporting the two full data spectra, let Q=pQ_+ +(1-p)Q_-. The candidate complete reference is

R(A,empty)=(1-w)Q(A), and R(A,T)=w Q(A)/K for each nonempty T in supp(beta-hat).

At w=0 only the first branch is used; at w=1 only the second is used. The target is

Gamma_R(F) <= p Gamma_{Q_+}(g_+) +(1-p) Gamma_{Q_-}(g_-) + h2(p)+h2(w)+w log2 K.

Both terminal reference bills keep their physical branch weights. No fresh private tag is introduced. Quadratic rank is charged only at spectral activation w, rather than uniformly.

## sources actually read, revisions and theorem locators

Exact byte hashes, source sizes and encodings are recorded in out/SOURCES.json. The primary predecessor is A068 stage5 (20261014T052938Z); later stage directories are not presumed to contain new mathematics merely because their timestamps advanced. Source baseline: execution protocol 2026-10-11-execution-v2; A068 stage5 REPORT and LEARNED; B14 STREAM_NOTES v2; current BOARD. The session wake returned attachment-lock integrity failures, so no affected brain attachment is an accepted premise.

## complete derivation or exact first unsupported line

Write u=(g_++g_-)/2 and v=(g_+-g_-)/2, so uv=0 pointwise, ||v||_2^2=d, and F=u+beta v. Independence of X and Z gives F-hat(A,empty)=u-hat(A)+b v-hat(A) and F-hat(A,T)=v-hat(A) beta-hat(T) for nonempty T. Consequently the exact data spectral marginal is

M(A)=u-hat(A)^2+2b u-hat(A)v-hat(A)+v-hat(A)^2 = p g_+-hat(A)^2 +(1-p)g_--hat(A)^2.

The total nonempty control mass is w. Quadratic flatness makes the conditional nonempty control law uniform on K atoms, independently of A. R is normalized and supports every nonzero coefficient, including all zero/one activation boundaries. Therefore

Gamma_R=h2(w)+sum_A M(A) log2(1/Q(A))+w log2 K.

The inequalities Q>=pQ_+ and Q>=(1-p)Q_- give the displayed complete cost bound (zero branch weights are omitted). This uses full spectra, including the empty data atom.

For every physical data coordinate, Inf_i(F)=p Inf_i(g_+)+(1-p)Inf_i(g_-); for every physical control coordinate, Inf_j(F)=d Inf_j(beta). A quadratic phase has Inf_j(beta) in {0,1/2,1}; each nonzero polar row contributes 1/2, and the number of such rows is at least r. Hence r<=2I(beta), and w log2 K<=dr<=2dI(beta)=2I_Z(F). Thus

Gamma_R <= weighted full terminal bills + h2(p)+h2(w)+2I_Z(F).

### Strengthening: pay rare mixing from the actual disagreement boundary

Let e=g_+g_- be the Boolean disagreement sign and J=I(e). Write Gamma_bar=p Gamma_{Q_+}(g_+)+(1-p) Gamma_{Q_-}(g_-). The stronger theorem is

    H(F) <= Gamma_R(F) <= Gamma_bar + 4J + 2I_Z(F).

This uses the SAME references Q_+,Q_-; they need not be actual spectra or newly chosen references. To prove it, put P_+=g_+-hat squared, P_-=g_--hat squared. Joint convexity of relative entropy (the log-sum inequality, applied at each data atom) gives

    CE(M,Q)-Gamma_bar <= JS_p(P_+,P_-).

In detail, p D(P_+||Q_+)+(1-p)D(P_-||Q_-) >= D(M||Q). Expanding D as cross-entropy minus entropy yields precisely this inequality. All full terminal bills survive; a zero physical branch weight contributes zero. Finiteness requires support of each Q on its branch spectrum.

For 0<p<1, ln(t)<=t-1 bounds Jensen-Shannon by its weighted chi-square:

    JS_p <= [p(1-p)/ln 2] sum_A (P_+(A)-P_-(A))^2/M(A).

Set a=g_+-hat(A), c=g_--hat(A). Both exact identities

    M-p(1-p)(a+c)^2=(p a-(1-p)c)^2,
    M-p(1-p)(a-c)^2=(p a+(1-p)c)^2

are nonnegative. At M=0 both a,c vanish, and the summand is defined as zero. Otherwise cancellation gives separate bounds by (a-c)^2 and by (a+c)^2. Parseval then gives

    JS_p <= (4/ln 2) min(d,1-d).

No product of conditional probabilities is used. Since Var(e)=4d(1-d)<=J and 4d(1-d)>=2min(d,1-d), it follows that JS_p <=(2/ln 2)J<3J. The strict numerical inequality follows from ln 2>2/3 (the positive atanh series at 1/3).

The EXACT control spectral marginal is C=(1-d)delta_empty+d P_beta, whether or not beta is quadratic. Hence H(C)<=h2(d)+d H(beta). Our R is exactly Q times C, because quadratic nonempty coefficients are uniform. Entropy tensorization for the Boolean sign e gives h2(d)<=J. For completeness, H(e(X))=sum_i I(e;X_i|X_<i)<=sum_i I(e;X_i|X_-i)=sum_i H(e|X_-i)=I(e): the inequality uses independence of the uniform input bits to condition X_i on the omitted future; the last equality holds because each fiber is either constant or balanced. This also handles d=0,1 exactly. Combining these facts with H(beta)=r<=2I(beta) proves Gamma_R<=Gamma_bar+4J+2I_Z.

### The quadratic facts and every boundary case

Write beta(z)=(-1)^q(z), B its polar alternating form, and K0=ker B. Fourier autocorrelation gives

    beta-hat(t)^2 = E_h [(-1)^(q(h)+q(0)+t dot h) 1_{h in K0}].

On K0 the exponent q(h)+q(0) is a linear form. Character orthogonality makes the displayed square either 0 or |K0|/2^m=2^-r. The supported t form an affine coset of dimension r. Thus H(beta)=r; the mean b is either 0 or +/-2^(-r/2). A nonzero polar row produces an unbiased affine coordinate derivative and influence 1/2; a zero row produces influence 0 or 1. The number of nonzero rows is at least their rank, proving r<=2I(beta). Any nonzero alternating matrix has a nonsingular 2-by-2 principal minor, so its rank is at least two. For a nonconstant beta with nonzero b, r>=2, so |b|<=1/2. Consequently min(p,1-p)>=1/4 for EVERY nonconstant quadratic beta, including nonconstant linear characters (b=0,r=0).

If beta is constant, use the single selected inherited reference and zero control cost. If d=0 or 1, J=0 and JS=0: there is no data mixing tax. If w=0 or 1 the unused reference branch has zero mass and no logarithm is evaluated there. Atoms with M=0 or C=0 have zero output mass. These observations account for every cancelled denominator and normalization boundary.

### A paid weak/unequal pair with one original reserve

The edge union bound gives J<=I(g_+)+I(g_-). For nonconstant quadratic beta, the physical branch weight lower bound gives J<=4 I_X(F). Therefore

    Gamma_R <= Gamma_bar + 16 I_X(F) + 2 I_Z(F).

If the SAME original terminal references satisfy Gamma_{Q_s}(g_s)<=C_reg I(g_s), the extra reserve 16 I_X funds the new conversion exactly once. Since C_reg<8.937, the complete output reference has Gamma_R<25 I(F) for every nonconstant output (and zero for constant output). This does not assume I(g)>=1 for a nonconstant gate; that tempting absorption is false for sparse thresholds.

In particular, for arbitrary real weights a,c, affine ell, and fixed tie convention, use g_s(x,y)=sgn((a+s c)x+ell(y)-theta). This proves the weak/unequal identified pair with independent quadratic relative phase, including rare disagreement, negative merged coefficients, and constant terminal gates. More generally each g_s may already be an admitted quadratic-controlled threshold core, provided ALL its controls belong to X and are independent of beta's Z. No new parity tag is introduced. The example g_+=x,g_-=y,beta=(-1)^(z1 z2) is nonunate: the z1 derivative has both signs as (x,y) varies, so no fixed orientation makes it monotone.

This is a rate-25 closure fixed BEFORE the conversion: the 16I_X reserve is included in that original chosen budget. It does not establish the prior C_reg rate for weak pairs, and it does not create a new allowance after earlier debits.

The all-dimensional conclusion uses the accepted COMPLETE A068 reference theorem for terminal gates, not merely their entropy bound. If only H(g_s)<=C I(g_s) is available, choosing their exact spectra proves an entropy-only corollary, but it is not an inherited-reference payment.

### Why the old uniform control decoder cannot cover weak pairs

Let q be odd, m=2q^2, beta a full-rank matching quadratic on m controls, and

    F=sgn(x+x beta+sum_{i=1}^q y_i).

Its terminal gates are g_+=sgn(2x+sum y_i) and g_-=sgn(sum y_i), and d=Pr(|sum y_i|=1)/2. The central coefficient c_q=binom(q-1,(q-1)/2)/2^(q-1) satisfies c_q<=1/sqrt(q): c_1=1 and c_{q+2}=q c_q/(q+1), with q(q+2)<=(q+1)^2. Since Pr(|sum y_i|=1)=2q c_q/(q+1), d<=1/sqrt(q). Physical influences obey I_X<=q+1 and I_Z=d m/2. Thus

    m/I(F) >= 1/[(q+1)/m+1/(2sqrt(q))] >= (2/3)sqrt(q) -> infinity.

Any reference with uniform independent spectral control label on all 2^m subsets has complete cost at least m, regardless of its data reference. It therefore admits no absolute influence payment on this actual Boolean family. The new reference uses activation weight d instead. This refutes the uniform decoder, not FEI; the family has the paid <25 bound just proved. This diagnostic is part of the same weak-pair repair, not a separate broad candidate.

The remaining OPEN line is conditional/overlapping phase payment after a physical query from a prescribed SAME inherited source with old debits. The present reserve is an original 16I_X allowance, not a grant that may be renewed at each descendant.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification SPEC.json precedes computation. The 256-case pilot PASSed 24164 assertions in 0.726s. The full verifier PASSed all 4096 ordered two-bit data-function pairs/quadratic two-bit selectors and all 27 prescribed weak/unequal threshold fixtures: 452345 exact assertions in 7.766s; 145 distinct certified prime-log signs. No symmetry reduction, stochastic sample, or dimension escalation was used.

Commands (from A068):

    python -X utf8 -u runs/20261022T211502Z-fleet03-A068-antichain-beyond-one-order/code/verify.py --pilot
    python -X utf8 -u runs/20261022T211502Z-fleet03-A068-antichain-beyond-one-order/code/verify.py

The main domain includes constants, identical/opposite branches, all linear and quadratic phases, b=0,+/-1/2,+/-1, and d=0,1. Targeted q=1,3,5; weights (1,1),(2,1),(1,2); controls=2,3,4 include balanced/nonbalanced selectors, negative/zero merged coefficients and fixed ties. The separate physical truth-table FWHT, physical edge counts, derived coefficient formula, both spectral marginals, reference support/normalization, and complete reference payment are checked exactly. Uniform and softened inherited references independently test the log-sum transfer, rather than substituting exact spectra for the original references.

Entropy differences are rational linear combinations of prime logarithms. Forty-eight-term atanh series with a rational remainder certify every nonzero sign; identically zero prime coefficients certify equality. The source/helper hash is af436c9eaac4e0f2617d170517f163636ef03d669d83b7e93ca41ee3f0fde5d0. Finite checks support the derivation; the all-dimensional statement follows from the full proof above.

Lean source code/Contrast.lean states the two denominator/marginal identities over Q. Formal compiler admission and its exact outcome are in out/LEAN_ADMISSION.json. The proof rung is author proof plus exact finite certificates, NOT a Lean-checked entropy theorem. No compiler result certifies the prose translation or its entire dependency chain.



Three fixed hypothesis controls pass in out/HYPOTHESIS_GUARDS.json, under a frozen spec: sharing beta=x with g_+=x,g_-=-x gives constant F and invalidates the independent data-influence formula; a three-bit point-defect phase has H(beta)>2I(beta)+1/8 and invalidates the unrestricted two-price substitution; a reference of mass2 has negative cross-entropy and invalidates the entropy bound. These are out-of-hypothesis guards, not counterexamples to the theorem.

The source comparison is threshold_paper_38pp Section8.2, Proposition8.6 equations75--79 and Corollary8.7: the recovered bound charges two bits per physical selector and requires positive selector energy to absorb that amount. Our weak family has selector influence per active coordinate tending to zero. The current result replaces that uniform charge by the activated quadratic law and a disagreement-boundary debit. The component mixture/channel ingredients are standard; no literature novelty is asserted. Section8.3 independently explains why arbitrary selectors would contain full FEI.

Fresh memok returned exit1: physical free1.7GB below4GB, commit free11.5GB above8GB. Lean's own admission also held (snapshot physical3977MB below5500MB). No compiler was started and no admission override was used. The two rational Lean identities remain source-formalized but UNVERIFIED by a compiler; failed admission is not evidence against the mathematical identities.

## proof dependencies and changed downstream conclusions

The algebra uses quadratic spectral flatness and the complete-reference mixture interface, with their proofs reconstructed in this report. It does not assume FEI for arbitrary leaves. For weak/unequal identified threshold pairs with common phase 1, take g_+=sgn((a+c)x+ell(y)-theta), g_-=sgn((a-c)x+ell(y)-theta), with the same tie convention. Both are actual threshold terminal gates; their full inherited references enter unchanged. Independent common-phase controls can be included inside X; controls shared with beta cannot.

## one next mathematical action and independent reviewer

Next: replace the independent flat beta law by the actual signed conditional law after one physical control exposure, and pay its nonuniform conditional rank/flag cost from the SAME unused original terminal reserve. Requested reviewers: A070 (complete references and boundary cases), A088 (Booleanity/independence), A094 (same-source budget). No review acceptance or message delivery is asserted.

## actual persistence receipts or precise save blocker

The four protocol files, code, frozen spec and exact outputs are saved locally. out/RECEIPTS.json records SHA256 and byte size; out/SCHEMA_CHECK.json validates exact protocol fields and the compatibility copy. STATUS is two lines; WORKLOG is appended and LEARNED updated. Independent review, supervisor collection, shared-registry adoption and mirror verification are not asserted. No git, mail, shared index write, brain write or external publication performed.

## Universal bridge

This stage moves C019 stopping-tree payment through a weak collision: a uniform control-rank bill, rigorously impossible on the displayed odd-majority family, is replaced by the activated control law at cost at most 2I_Z plus 4I(g_+g_-), retaining both original full terminal references. One original 16I_X reserve pays that contrast for every independent quadratic relative phase, giving complete references below 25I for the admitted threshold terminals. Full FEI remains OPEN: phases overlapping the terminal variables, conditional nonflat conversion, and payment after earlier debits are not covered. Carrying this SAME reference and its unused original reserve through one actual control exposure is the shortest next step because a renewed flat reference or reserve would restart the universal gap rather than close it.
