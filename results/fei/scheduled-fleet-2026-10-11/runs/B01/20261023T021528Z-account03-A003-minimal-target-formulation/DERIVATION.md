# Vacuum calibration absorbs every earlier vacuum calibration

All logarithms are base two. This is an author proof awaiting independent review. It corrects the repeated-return scope distinction in A096's 20261023T010221Z DERIVATION.md, sections 1, 2 and 5, for the precisely stated operations below. It does not extend to arbitrary new references, editing the function, resetting to a different source, or imposing additional atomwise floors between calibrations.

## 1. Definitions and absorption identity

On a finite frequency space with distinguished empty atom 0, write a normalized reference S=q delta_0+N, where N(0)=0. For a desired true empty occupancy p in [0,1], vacuum calibration is

    C_p(S)=p delta_0 + [(1-p)/(1-q)] N,                 (1)

when q<1. At p=1 define C_1(S)=delta_0. The case q=1,p<1 is inadmissible when the actual law has finite cross entropy against S.

Let M be any positive linear mass-preserving map between finite frequency spaces such that M delta_0=delta_0. Physical coordinate deletion and every finite composition of such deletions satisfy these hypotheses. For q<1 and p<1, put b=(1-p)/(1-q)>0. Then

    C_p(S)=b S+(1-b)delta_0,
    M C_p(S)=b M S+(1-b)delta_0.                       (2)

Although 1-b can be negative, both displayed measures are nonnegative because they are the actual calibrated law and its positive image; no signed law is used as a reference. Every nonempty atom of M C_p(S) is b times the corresponding atom of M S. If the desired final occupancy r<1 is admissible, their nonempty totals are both positive, and (1) therefore gives the EXACT normalized-law identity

    C_r(M C_p(S)) = C_r(M S).                         (3)

At r=1 both sides are delta_0. At p=1, finite CE against the actual Boolean spectrum forces the actual function at that node to be constant. Every physical descendant is then constant, so r=1 and (3) again holds. The abstract linear-map identity is not asserted for p=1,r<1; those parameters are physically inadmissible. Empty raw mass q=1 has the same constant-only endpoint. If q=0, (1)-(3) remain literal whenever admissible. No log or 0/0 is taken at an unoccupied atom.

For physical restrictions, finite CE propagates under coordinate deletion: a nonzero restricted Fourier coefficient is a sum or difference of ancestor coefficients in its frequency fiber, so at least one ancestor in that fiber is occupied. Thus all calibrations used in (3) are admissible at every nonconstant descendant.

## 2. Pathwise policy equivalence

Fix ONE root source law S. For each physical history v let S_v be its direct coordinate marginal from that same S; the outcomes change the actual restricted function g_v but do not change which frequency coordinates are deleted. Allow arbitrary finite adaptive queries. After the first reset on a branch, permit either of the following operations at any later node v:

* calibrate the CURRENT full inherited reference to p_v=(E g_v)^2;
* reset to C_(p_v)(S_v), the DIRECT marginal of the ORIGINAL S followed by one final vacuum calibration.

They give identical full laws. Indeed, after the last earlier calibration at u, the current inherited law is M_(u to v) C_(p_u)(S_u). Equation (3) makes its next calibration exactly C_(p_v)(S_v). Induction proves this statement after any finite number of intervening queries and calibrations. Adaptivity and selective branch choices do not change this pathwise equality. Before a first reset the old Q law is retained; it need not equal or dominate S. A reset to a different source, or a calibrated EDITED-function floor, is outside this identity.

Every complementary terminal keeps its COMPLETE inherited law, including all vacuum, reference-only and control-frequency mass. A nonconstant sibling can therefore remain old while another sibling returns repeatedly to S. The equality concerns complete laws, not just their costs.

## 3. Same original comparison cost and bank

Use A096's supplied-likelihood hypotheses, stated here explicitly. Let g be any Boolean function on a finite uniform cube, P_g its squared Fourier law and m=P_g(0). Supply a subprobability D=m delta_0+N with total mass at most one and finite c=CE(P_g,D), and normalized references S,Q satisfying

    S>=D, Q(0)>=m, Q(T)>=gamma D(T) for T!=0,
    0<gamma<=1, L=log2(1/gamma).                       (4)

Run any finite adaptive physical-query tree, allowing ANY number of direct-original-S marginal/final-calibration resets along each branch; a reset is optional and can depend on the full physical history. Other nodes inherit the current reference by coordinate marginalization. At the first-reset frontier, A096's supplied-likelihood theorem bounds all already executed erasures plus the complete first-reset/old frontier costs by

    c+(1-m^2)L.                                       (5)

For completeness, that theorem follows by telescoping CE(P,D), then using calibration's CE decrease on reset terminals and, on retained terminals, the bound

    CE(P_leaf,Q_leaf)-CE(P_leaf,D_leaf)
      <= L[(1-m)+m Var(g_leaf)].

Here D_leaf=m delta_0+M N, and concavity of log gives the vacuum penalty <=(1-m)L, while each nonempty penalty is <=L. Total variance yields the constant (1-m^2). The comparison D is never supplied as a normalized actual reference.

Below the first-reset frontier, every subsequent return-to-original-S operation is a CURRENT-reference calibration by section 2. A physical query costs its erasure and leaves the full two-child references paid by the exact complete-reference CE chain; the conditional KL refund is nonnegative. A current-reference calibration decreases CE by

    D_Bern(p_v || current_reference(0)) >= 0.          (6)

Thus every continuation below that frontier is paid by its initial full frontier CE. The same (5) holds for the ENTIRE repeated-return tree. There is NO factor for the number of returns or queried dimensions. First-reset nodes form an antichain; only that antichain is used for the initial likelihood comparison. The proof does not pretend all last-reset nodes form an antichain.

If the original global quota is M0, old erasures cost d, and an eligible exit has physical reach w, replacing its complete old terminal by this repeated-return tree changes only that exit's existing allocation. All old debits and all other full terminal costs remain unchanged in the identity U=M0-d-sum(reach*CE). No source or child receives a new influence quota.

## 4. Consequence for the current negative-cell bridge

In A096 section 3's negative-cell exit, m=(1-2s)^2, h=e/s<=1/2 and gamma=(1-h)/(1+h/2), so (1-m^2)L<22e. Therefore the ENTIRE exit policy, now allowing arbitrarily many returns to the same original source marginal after intermediate calibration and queries, costs <c+22e. A096's already stated one-original-bank assembly is unchanged:

    creating-node complete bill <W+13e,
    final reserve >=[5a*2^d-13(d-1)]e_root>=7e_root,
    K=2C0+10, and K=18 for its structural C0=4 source.

The numerical application remains conditional on A096/A097's exact creating/live-step and original-bank hypotheses. The absorption identity and abstract extension (5) are self-contained and require none of the negative-cell algebra. No all-dimensional FEI constant is claimed to improve.

## 5. First unsupported line and smallest next lemma

Repeated returns to a fixed original source after pure vacuum calibrations and physical deletions are no longer a distinct unpaid mechanism. The unsupported universal line remains constructing, for arbitrary Boolean f, an influence-priced admitted source and an occupied-support likelihood floor (4) whose excess and all creating costs fit ONE original influence bank. References involving a new edit floor or a changed nonempty shape are not covered by (3). For the minimal-target packet, the next genuinely stronger lemma is a source-transport bound across ONE operation that changes relative nonempty reference weights, priced by the same remaining ancestor bank; testing more pure-calibration interleavings cannot advance that gap.
