# Stage2: Boolean heat charges, padding reserves and coherent resets

Entropy is in bits except where explicitly marked nat. This stage consumes new A066 stage2, A067 stage2 and A039 v1 claims. A088's first-stage A066 heat identity/no-envelope and A067 maximal-support no-go reviews remain accepted unchanged; they are not recomputed. B18's v2 instruction naming them is fulfilled by retaining those receipts and auditing their new quantitative applications. All exact source statements and original hash conventions are copied into out/ORIGINAL_CLAIMS.json. No shared registry is edited.

## A066-POSITIVE-RESTRICTION-HEAT-LEDGER v1: HOLDS for singleton-tree budget; scope clarification needed

For any physical block B, let U index the queried spectral bits, T the residual bits, and q_T=sum_U p_UT. Actual signed restriction gives p_y(T)=(sum_U a_UT chi_U(y))² and E_y p_y(T)=q_T by character orthogonality. Expand the finite entropies directly:

    H_nat(parent)-E H_nat(child)=sum_T M_T+sum_T C_T,
    M_T=sum_U p_UT ln(q_T/p_UT),
    C_T=E_y p_y(T) ln(p_y(T)/q_T).

The first summand is conditional entropy multiplied by q_T; the second is convexity of x ln x on a row whose mean is q_T. Both are nonnegative. Removing the one empty residual row and canceling the parent/child empty atoms proves

    2(K(parent)-E K(child))=M_B^++C_B^++ell_B,
    ell_B=sum_{nonempty U subset B}p_U ln(1/p_U).

This positive **block identity** is valid. It is finite Parseval/entropy algebra; its cancellation does not use full Boolean convolution. Booleanity ensures each physical child's squared coefficients are a probability law, so the entropy/channel interpretations and the fair physical tree are those intended.

For a singleton i with row amplitudes a,c, channel cost q*g(2ac/q), where g(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2. Independently, g(z)<=1-sqrt(1-z²) follows by comparing derivatives of atanh z and z/sqrt(1-z²); their derivative gap is nonnegative on [0,1), and both vanish at zero. Therefore C_T<=2min(a²,c²), and summing gives C_i^+<=2I_i. This scalar inequality actually survives for general real row amplitudes.

The genuine Boolean payment is the **singleton level** bound. D_i f takes values0,+1,-1; hence x=|E D_i f|=|fhat({i})|<=E(D_i f)²=I_i. Then ell_i=2x² ln(1/x)<=2x/e<=2I_i/e. Summing the positive identity in a singleton restriction tree telescopes K with terminal K retained; influence telescopes as I(root)-E I(leaf). Thus cumulative C_i^++ell_i<= (2+2/e)I_removed for every **singleton-query** stopping tree. No ancestor influence is paid twice.

Omitting the empty row from erasure loses at most (1+2/e)I in nats: its two masses u=p_empty,v=p_i have row entropy <=v ln(1/v)+v, and v=x²<=x<=I_i. More strongly, F_m=y product_{j=1}^m g(x^(j)) places a fresh spectral character in every set, so all core contexts are nonempty. Spectral product independence yields R_nat(F_m)=m B_nat(g), I(F_m)=m I(g)+1. Consequently universal R_nat<=A I would imply B_nat<=A I with the SAME A by letting m grow. The reverse implication is immediate from R_nat<=B_nat. This is an exact C018 admission guard, not payment of the remaining erasure. The admission itself uses tensorable normalized spectra and survives beyond Boolean signs; it cannot be advertised as the Boolean phase constraint that pays R.

The source DERIVATION.md Sections2-3 correctly restrict the tree payment to singleton queries and expressly decline an all-block level bound. CLAIMS.json does not explicitly say “singleton-query” when it says “the identity telescopes in every finite physical stopping tree, with ... cumulative channel-plus-level cost <=(2+2/e)[I-E I(leaf)].” That clause must retain the singleton restriction. Its unqualified block-tree reading is false.

**Exact Boolean certificate for the block-tree reading.** Let f=1-2 indicator{x=all plus} on128 coordinates and take one node querying the entire cube. All leaves are constants. Its off-empty Fourier masses are4/2^256, total influence I=256/2^128, no nonempty residual context exists, and C_B^+=0. Therefore

    (C_B^++ell_B)/I=4(127/128)(1-2^-128)ln2.

The first three terms of ln2=2sum_{j>=0}(1/3)^(2j+1)/(2j+1) give a rational lower bound >693/1000. Meanwhile e>1+1+1/2+1/6=8/3, so2+2/e<11/4. Exact Fraction arithmetic proves the displayed rate exceeds11/4; out/A066_BLOCK_SCOPE_CERTIFICATE.json records the positive gap. This is a genuine Boolean, finite certificate to the unrestricted clause, not FEI and not the valid singleton theorem.

**Verdict:** HOLDS for the block identity, singleton payments, singleton stopping telescope and same-optimal-C018-constant reduction; GAP_SCOPE in the serialized tree clause until “singleton-query” is explicit. I do not independently accept the unqualified bundle. No alternate proof or corrected source version was supplied; an author scope clarification is required, not a repair of the valid derivation. Any downstream block-tree use must be conditional or stopped.

**Strong non-Boolean relaxation.** A normalized singleton spectrum p_i=1/n has I_i=1/n but ell_i/I_i=ln n, violating the level bound. It even has fair, normalized singleton children, since the corresponding real f=n^-1/2 sum x_i has no first-order Fourier coefficient in f². Thus child norm1 and low-order square constraints do not rescue the paid step. For a one-bit real amplitude sqrt(1-epsilon)+sqrt(epsilon)x, B_nat/I=h_nat(epsilon)/epsilon diverges as epsilon tends to zero; the character-tensor admission transports that same unpaid erasure into nonempty contexts. Norm1 plus |f|<=1 would force f²=1 pointwise, so it is not a genuine relaxation.

## A066-MAJORITY-DEFECTED-ADDRESS-HEAT-CALIBRATION v1: HOLDS

Odd majority has only odd Fourier levels. Every singleton row therefore has at most one occupied amplitude: M_i=0, and its child squared coefficients are unchanged across the two branches, so C_i=0. The pivot occurs when the other2m votes tie, giving I_i=alpha=binom(2m,m)/2^(2m), and monotonicity gives fhat(i)=alpha. Both children have mean+/-alpha. Consequently K drop is alpha² ln(1/alpha²)/2, entirely the level charge, with ratio alpha ln(1/alpha)<=1/e. For Maj3 this is strictly positive while the channel is zero. This checks the named Booleanity line (parity support and exact sign pivotal derivative), and rules out channel-only heat payment without refuting the singleton level payment.

For point-defected addressing, Fourier expansion gives original coefficients z in{+A,-A,0}, A=2^-a, with counts(4^a+2^a)/2,(4^a-2^a)/2 and the remaining zeros. A flip at the all-plus vertex subtracts2delta from every coefficient, delta=2^-D. Direct pivotal-edge counting changes one original coordinate influence by-2delta and the other D-1 by+2delta, giving I=1+a/2+2delta(D-2). For b dummy queries, w=2^b, each row has masses (z-2delta)² and w-1 copies of4delta². The exceptional physical child has coefficient z-2wdelta; all other children have coefficient z. This independently proves the three-class formulas and empty-row cancellation in source equations9-11.

For fixed a,b and r tending to infinity, zero rows have count2^(D-b)-4^a and equal M,C=w*4delta² ln w; their totals divided by2bdelta tend to2ln2. The finite original-support rows contribute smaller order. Removing one empty row is negligible, giving K-drop ratio2ln2. For b=r, the zero-row count stays2^k-4^a. Let sigma=2^-k,rho=4^a/2^k. Zero rows give2(1-rho)ln2 to both M/I and C/I. Each original-support row contributes4sigma ln2 to M/I, while its C/I tends to zero; hence M/I tends to2(1+rho)ln2. The block-contained level share tends to4sigma ln2 and the normalized boundary difference tends to zero. The resulting heat ratio stays2ln2. These limits follow from the displayed row formulas, not finite extrapolation.

Independent integer transforms verify every block in the frozen four small addressing roots and every singleton of Maj1,3,5,7. The entire calibration claim is accepted. Its generic row bookkeeping persists for a normalized real core, but the actual address flip, majority spectrum and physical pivotal formulas describe specified Boolean families; a real relaxation is not a disproof of this family statement. Its intended universal channel-only extrapolation is already false inside the Boolean domain.

The source lists A066-POSITIVE-RESTRICTION-HEAT-LEDGER v1 as a dependency. This independent calibration review uses only that lemma's separately reconstructed finite block identity and the direct signed row formulas. It does NOT use the ambiguous stopping-tree cost clause, so its acceptance does not inherit that scope gap. This component-specific substitution is recorded in the review receipt.

## A067-PADDING-STRIP-RESERVE-AND-LEAF-ACCESS v1: HOLDS

This consumes the new padding-access result, not the retired maximal-support no-go. Orient the seed spectrum by its value and characters at the edited vertex, so b_T=s chi_T(x0) ghat(T). With p=2^-(m+r), t=2p, actual edit coefficients are b_T-t when padding support is empty and-t otherwise. Summing their entropies gives source equation1. A padding query has exactly two fair physical children g,F_(r-1); subtracting those complete entropies yields equations2-3 including zero-coefficient cancellation. The seed and all terminal entropy remain present.

For fixed seed and r>=2, Boolean coefficient quantization prevents a nonzero b_T from approaching zero along the difference interval. The bound on phi'' for phi(x)=-x²log2(x²) gives the stated error4Lp[|m+r-3|+m+3/(2ln2)] and ratio4 limit. This is a fixed-seed statement; it does not become uniform for seeds growing with r. For quadratic bent seeds at fixed r, all2^m coefficients have magnitude2^-m/2. Taylor expansion of the same centered second difference, with |phi'''|=4/(ln2|x|), gives the stated linear-in-m asymptotic2^(1-r)m. This verifies the source's local-rate guard rather than treating it as a new FEI counterexample.

The point-defect rate5 estimate follows from the scalar concavity bound on[1/2,1] for n>=3, a decreasing correction for n>=4, and direct n=2,3 integer power comparisons. Dictator surgery and Maj3 tensor a point defect have the exact described padding trees: clean branches stop, the edited branch stops at residual defect dimension2, and the local entropy seed cancels on each padding step. The leaf U certificates are actual physical restrictions; no universal hereditary U assertion is used.

The new universal reserve is substantive. At residual pad count k, the edited-node probability is2^(k-r) and its padding influence2^(1-m-k); their product is the SAME root d=2^(1-m-r). A prefix of l queries spends l*d. Summing the fixed-seed curvature upper bounds over all visited k>=2 and the separately paid final k=1 step bounds the excess above rate4 by A*m*d, A=1+6/ln2. This sums a single root reserve, not a fresh reserve at each level.

To pay m*d, a nontrivial Boolean cut of an m-cube has at least m boundary edges, proved by slicing and induction. Thus I(g)>=m2^(1-m). A vertex flip changes each core influence by+/-d, so I_core>=I(g)-m*d; since2^-r<=1/2 this implies m*d<=I_core. For constant seeds I_core=m*d directly. This is the exact Booleanity line beyond coefficient granularity. Therefore Q_pad<=4I_queried+A I_core for every allowed early-stopping padding tree. Since I_core<=E I(leaf), adding H(leaf)<= (2+2b)I(leaf) gives H(root)<= (A+2+2b)I(root)=(3+2b+6/ln2)I(root). The reserve and the terminal bound share one retained-leaf price. They are not paid as separate repeated ancestor accounts.

I independently checked828 roots from every Boolean seed m=1..3 with r=1..3 and1656 padding prefixes, including constant seeds, reversals that produce constant edited core leaves, and seeds with irrelevant core bits. Exact influence telescopes and signed Fourier edits hold; rigorous rational-log intervals certify every reserve inequality. The all-seed statement follows from the induction and weighted sum above, not this finite domain.

**Strong real diagnostic.** An L2-normalized real core can have arbitrarily small positive Dirichlet influence, e.g. sqrt(1-epsilon)+sqrt(epsilon)x1, violating the discrete Boolean bound I(g)>=m2^(1-m). More generally, flipping the value of a real seed at a point uses2g(x0), not the Boolean edit amplitude2s with s=+/-1; the local influence change is no longer necessarily+/-d. For the norm1 real two-bit values[1,-1/3,5/3,1/3], the Fourier coefficients are[2/3,2/3,-1/3,0], violating Boolean granularity2^(1-m)Z even though the edited vertex value is1. The generic entropy-difference identity still exists with the actual edit amplitude. These exact diagnostics invalidate the relaxed premises used by the proof; I do not assert a counterexample to a differently normalized real-seed padding theorem that the source never states. The fixed-seed ratio4 asymptotic itself is not uniquely Boolean; for a finite real seed with nonzero coefficients separated from zero and edited value1, the same asymptotic mechanism survives.

The first unpaid universal line is certification/payment of the arbitrary core leaves g and F0. They occur with real positive probabilities. Padding access is paid, but it cannot certify arbitrary U, hereditary core access or full FEI. The full source claim is accepted at its explicit conditional-leaf scope.

## A039-COHERENT-PROJECTION-TRANSFER v1: HOLDS

Let TC= sum_j h2(d_j)-H(f), B_i=H(S_i|S_-i), J_i=H(q)-E H(p_y), and Gamma_i=sum_{j!=i}[h2(d_j)-E h2(d_j^y)]. Coherent signed children imply q=(p_++p_-)/2 and d_j=E d_j^y. Subtract these two entropy formulas without any inequality:

    TC(parent)-E TC(child)=h2(d_i)-B_i-J_i+Gamma_i.

This is the source identity because I_P(S_i;S_-i)=h2(d_i)-B_i. Finite adaptive fair-tree telescoping retains leaf TC. Gamma is nonnegative by binary-entropy concavity; it is the exact saving when the fixed residual product reference R is replaced by the optimized child products R_y. It is not additional free credit.

Apply the SAME coherent kernel k(y|T)=p_y(T)/(2q_T) to q and R, with the declared fair extension on zero q fibers. The original outcome is fair, the reference outcome is Q_Y, and the reference posteriors are Q_y. Expanding the joint KL in outcome-first order gives TC(q)=D_out+E D(p_y||Q_y), so channel injection is zero. Direct product cross entropy also gives E D(p_y||R)=TC(q)+J, while optimizing products saves Gamma. Comparing the two references proves

    E delta_y = D_out+J-Gamma,
    delta_y=E_(p_y) log2(Q_y/R_y).

The reset may be NEGATIVE. Reference-only zero fibers affect D_out and delta individually but cancel from their difference; all used P-supported atom ratios stay finite. This is a proper source-compatible application of A037, unlike independently choosing a fresh channel for each child.

For occupancy E(f)=h2(v)+vHmax(r), A=vK_occ=E-H and Delta=sum h2(d_j)-E. Subtracting their exact definitions proves the two signed transfers in source equation4 and A+Delta=TC. Constants contribute zero. Those algebraic identities require a normalized conditional law and its maximum-entropy reference, not new Boolean phase information. No monotonicity follows from positivity alone.

Exact nonmonotonic controls: K4 quadratic phase has uniform16-atom parent spectrum (TC=0) and triangle children of four atoms with fair residual marginals (TC=1), so TC increases. Its odd-parity triangle child has a feasible uniform six-set law of entropylog2 6 at the same marginals, proving positive occupancy KL. The nonempty constraint excludes the full independent optimum, proving positive Delta. Conversely the triangle phase has those positive occupancy/Delta accounts and restricts to two-bit bent children whose conditional nonempty maximum-entropy laws match exactly, so both accounts drop to zero. Independent Walsh checks certify the TC changes+1 and-1bit; strict occupancy/Delta signs are analytic entropy-maximality comparisons without a numerical root.

Point defects supply the all-dimensional local obstruction. Set a=2^(1-m), L=log2(1/a)=m-1. Binary entropy has h2(a)=a(L+log2 e)+O(a²), with remainder<=a²/ln2. Therefore Gamma=(m-1)a+O(m a²), while the full entropy drop D_H=4a+O(m a²) and J<=D_H. From the exact TC identity and K_occ=0,

    [Delta_m-(1/2)Delta_(m-1)]/a = 2m-6+log2 e+O(m a).

Independently bounding the two empty-atom remainders by4a²/ln2 and16a²/ln2 gives absolute normalized error <=[2m-6+(3m+10)/ln2]a <=(12m+16)a, matching the conservative source certificate. Thus Gamma/I_i, Gamma/(J+I_i), and the absolute expected Delta-release/I_i diverge on actual Boolean functions, in every coordinate. An existential coordinate choice does not repair these particular helpers. The true entropy decrement on this family remains O(I_i), so none refutes FEI.

**Strong non-Boolean relaxation.** The identities hold for any normalized real Fourier vector whose selected physical children also have norm1; full Booleanity is not otherwise used by the subtraction or common-kernel KL chain rule. The real f=(x1+x2+x3+x4)/2 has normalized, isospectral singleton children, Gamma=J=0, and satisfies these projection identities despite not being a Boolean sign. It retains all first-order normalization constraints. General real functions with unequal child norms instead induce energy-weighted branches, and the fair Boolean statement cannot be applied unchanged. The no-go witnesses are already Boolean, hence stronger than a relaxation diagnostic.

The new complete reset lemma is accepted; A037's previously accepted common-law conservation is used at its recorded scope. The sparse activated bent-defect formulas in A039's source instantiate this algebra but do not prove a dimension-independent net erasure/terminal payment. Their numerical occupancy root enclosures are not a proof dependency of this review.

## Synthesis and the exact unpaid line

Combining the two parts of A039 gives an equivalent tree account,

    sum_h w_h B_i = sum_h w_h[h2(d_i)+D_out-delta_bar]
                     -TC(root)+E TC(leaf).

This is another way to display the full signed reset, not a new paid bound. In particular treating either Gamma or absolute Delta change as O(I_i) is rigorously false; deleting those terms would create apparent credit. A066's singleton heat reduction pays channel and singleton level charges but leaves the same nonempty-context erasure at FEI strength. A067 pays a specific whole padding-access path with one retained-core reserve but leaves arbitrary core certification open. The next useful universal step is one combined, source-compatible reserve on two overlapping active core edits, owning each physical query once and retaining both leaf entropies; independent positive or absolute-component pricing cannot supply it.
