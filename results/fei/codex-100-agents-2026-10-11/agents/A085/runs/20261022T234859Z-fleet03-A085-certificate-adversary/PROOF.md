# One actual query inside an exit can be paid before its reset

The prescribed exit-source theorem survives the scope check. A further query inside an exit is also affordable when its new reference is defined by direct marginalization of the original supplied source, followed by ONE calibration at the final child. Intermediate calibration is a different operation and is not silently substituted.

All entropy and cross entropy are in bits. References are complete normalized laws, including their empty and reference-only atoms. Physical reach is a probability of input-bit outcomes. No source, child or exit receives a fresh influence quota.

## 1. Exact setup and imported scopes

At a live edited node let a>=1,b>=0,r>=1,d=b+r>=2, n=a+b, s=2^-a,t=2^-n,e=2^(1-n-r), mu=1-2s. Let

    g=1-2A_a, F=g+2A_(a+b+r).

The a active, b dummy-data and r control coordinates are disjoint. Supply the current source R on all n data Fourier coordinates, obtained from the original supplied source by the previously paid canonical operations. It has R(empty)=mu^2, finite c=CE(P_g,R), and no restrictions on reference-only mass. Set h=e/s=2^(1-d)<=1/2. The complete canonical reference of F is

    Q(U,T)=R_e(T) P_F(U,T)/q_F(T),
    R_e(T)=(1-h)R(T)+h mu 1_(T=empty)+2et,
    q_F(T)=sum_U P_F(U,T).

The supplied-source floor theorem bounds its cost by W=c+10e(a+b+r). The previously scoped active/dummy/control substitutions pay all eligible live histories from the same original K I(F_root), K=2C0+10, and leave at least12e_root. These are the exact A096/A097/A073 upstream premises; they are not a cheap-reference theorem for arbitrary Boolean functions. An eligible non-active query is a dummy query b>=1 or a control query r>=2. Its off-child is g with an irrelevant coordinate removed. Call that child's full inherited reference Qoff. No reset has yet occurred inside this exit.

The new policy executes ONE arbitrary still-unqueried physical coordinate j inside that exit, under Qoff. It keeps the outcome-one child's entire marginal reference M_j Qoff. On outcome zero only, it resets to the following reference: start with the source R at the creating live parent; marginalize precisely the data coordinates physically removed at creation of this exit and at the inside query; then calibrate the empty mass ONCE to the actual source child's squared mean. Put point Fourier mass on all remaining irrelevant controls. If the child is constant, use its explicit empty point law. This defines the reference before inspecting any numerical sign.

This direct reference can differ from the reference obtained by first calibrating at the unqueried exit root and then querying it. The theorem below concerns only the stated direct policy. Both actual children, every earlier live-branch debit and every other terminal remain in the ledger.

## 2. A likelihood floor with no missing support

Define

    gamma=(1-h)/(1+h/2)>0, L=-log2 gamma>0, m=mu^2.

For every nonempty active source label T (with all dummy frequencies zero),

    Qoff(control-vacuum,T) >= gamma R(T),
    Qoff(empty) >= m.                                     (1)

These statements refer to the full inherited reference, without renormalizing away other control frequencies.

Here is the direct coefficient check. Write z_T=ghat(T). The joint coefficient is z_T 1_(U=empty)+e, and

    q_F(T)=z_T^2+2e z_T+2et.

Empty calibration makes R_e(empty)=q_F(empty), so Q(empty)=(mu+e)^2>=mu^2. For a nonempty active label z_T=-2s. At a control exit the old vacuum-control multiplier is

    ((2s-e)^2+e^2)/(4s^2-4se+2et).

Its reciprocal is <=1+h/2: if N=(2s-e)^2+e^2 and D=4s^2-4se+2et, then (1+h/2)N-D=2e(s-t)+e^3/s>=0. Also N>=4s(s-e)>0. At a dummy exit the first contributing packet has multiplier

    (2s-e)^2/(4s^2-4se+2et),

whose reciprocal is also <=1+h/2: b>=1 gives t<=s/2, the difference is 2et-e^2<=2et<=es, and (2s-e)^2>=2s^2. The other dummy packet is nonnegative and is retained. Multiplying by R_e(T)>=(1-h)R(T) proves (1). Adding packets also preserves its vacuum bound. All denominators are positive, including a=1. Reference-only labels need not satisfy (1); they remain in the true complete laws and all their normalizers.

For 0<h<=1/2,

    -log2(1-h)<=2h,
    log2(1+h/2)<=h/(2 ln2)<3h/4,
    L<11h/4.                                             (2)

The first bound is the convex graph below its chord on [0,1/2]. The second uses ln(1+x)<=x and ln2>2/3 (the first positive atanh term gives 2/3, with a strictly positive tail). Thus

    (1-m)L <=4sL<11e.                                    (3)

In particular the old whole exit cost is at most c+(1-m)L<c+11e: the occupied vacuum likelihood is no worse than R(empty), and all occupied nonempty source atoms obey (1). If m=0, the zero true vacuum is not logged. This recovers the source-bound likelihood estimate needed by A099 without a total-variation surrogate.

## 3. A query already executed inside the exit

### Active j

The outcome-one child is constant +1. Let v=R({j}) and V0=m+v. Its source-comparison cost is k0=-log2 V0, while the actual unchanged old terminal costs k=-log2 W0, W0=(M_j Qoff)(empty). By (1), W0>=m+gamma v, even if the creating exit removed a dummy. Only the original active singleton is used in this lower bound; additional packets remain nonnegative.

Finite source cost gives V0>0: if a>=2 then m>0; if a=1 then P_g({j})=1 forces v>0. Also v<=1-m. The likelihood ratio increases with v, so

    k-k0 <= -log2[m+gamma(1-m)] <= (1-m)L.               (4)

The last inequality is concavity of log at the mixture m*1+(1-m)*gamma. It includes m=0 and m=1 by direct endpoint evaluation. No endpoint normalization is canceled.

The source chain rule for querying j under R gives

    B_j(g)+(CE(P_on,M_j R)+k0)/2 <= c.

The prescribed fresh on-reference further marginalizes the creating dummy, if present, and calibrates once to the actual child vacuum. Marginalization of a physically irrelevant data bit can only increase each occupied reference atom, so it decreases CE. Calibration decreases CE by the binary KL of the old and actual vacuum masses. Hence, writing cnew for the full new on-cost,

    B_j(g)+(cnew+k0)/2 <= c.

When a=1, the on-child is constant -1 and cnew=0; its point reference replaces the calibration formula, so there is no 0/0 endpoint. When a>=2, the on-child is nonconstant and finite source cost ensures a positive nonempty normalizer. Combining with (4), the ACTUAL post-query exit ledger obeys

    B_j(g)+(cnew+k)/2 <= c+(1-m)L/2 < c+11e/2.          (5)

The old query B_j(g) is explicitly booked. Its sibling's full inherited CE k has not been reset to zero.

### Dummy-data or control j

The actual function is independent of j, so B_j(g)=0 and both children remain g (nonconstant for every a>=1). The inherited child's CE after spectral marginalization is no larger than the old whole exit cost. The fresh direct source marginal/calibration has cost at most c. Therefore

    B_j(g)+(cnew+cold)/2 < c+11e/2.                     (6)

Both complete nonconstant terminals are retained in (6). This includes a dummy creating exit followed by a control query, and a control creating exit followed by a dummy query. No new source is supplied inside the exit.

## 4. One original quota pays the entire transaction

At the creating non-active parent, the actual erasure is <12e. Its live on-floor has envelope <=c+20e(a+b+r-1); at a dummy creation its calibrated source cost is <=c. Replace the old off-terminal by the ENTIRE ledger in (5) or (6), including its already executed inside query. The resulting local bill is strictly less than

    12e + [c+20e(a+b+r-1)+c+11e/2]/2
      = W+19e/4 < W+8e.                                (7)

Thus any collection of the previously retained non-active exits may each perform the one stated query and reset; other exits keep their old full references. All old live debits and all complementary terminals remain paid by the SAME original K I(F_root), with the prior >=12e_root reserve unchanged. Subsequent finite no-reset continuations at the new frontier are also paid, by complete-reference disintegration.

If every non-active exit uses this post-query policy, its coefficient is 19/4 instead of8. At most d_root-1 such exits are created and physical reach times e is always e_root. The source reserve before these charges is >=5a_root*2^d_root e_root. For every integer d>=2,

    5*2^d-(19/4)(d-1)>=61/4.

At d=2 this is equality; each increment is 5*2^d-19/4>0. The complete all-post-query-exit policy therefore leaves at least(61/4)e_root. This is a DIFFERENT policy from A099's immediate exit-root conversions, which leave18e_root; the smaller reserve reflects the additional executed query and retained sibling. It is not a correction of A099's number. Structural source has unchanged rate18, and no all-dimensional FEI constant improves.

The original quota algebra uses I_g=2as, E=ae, X=de and I(F)=I_g+X-E. With c<=c_raw<=C0 I_g,

    (2C0+10)I(F)-W
      >=(C0+10)(I_g-2E)+2C0 X>=5 I_g=5a2^d e,

because E/I_g=2^-d<=1/4. All influences here are physical influences of the original supplied root, not newly minted child banks. An untouched independent terminal retains its entire additive CE with coefficient one and supplies none of these allowances.

## 5. Scope check, exact validation and first unsupported line

A099-PRESCRIBED-EXIT-SOURCE-RESET@1 holds at its stated added exit-conversion scope, relative to the named upstream active/dummy/control and source-floor premises. Its unqueried-exit restriction is observed; the new theorem above is a separate extension. The proof of its original source continuation is finite CE disintegration, followed by calibration or explicit constant points; all costs decrease or remain booked. Its global8 and2 coefficients are the creating-parent substitutions, and its12 and18 reserve constants follow from the exact source quota algebra. This is not a review of the full assembled candidate, and it accepts no universal arbitrary-core reference theorem.

The finite certificate independently constructs actual Boolean truth tables, character sums and physical edges; normalized source floors, inherited old references, old active-prefix debits, creating-parent erasure, inside-exit erasure and both full terminal costs. A direct-source final reference is compared with the actual incoming reference; it is never substituted retrospectively. Exact log expressions cancel algebraically before outward interval evaluation, so exact equalities are not inferred from interval overlap. Positive resets are sought after an earlier active debit. The frozen finite dimensions are validation only; Sections1--4 supply the all-parameter proof.

The first unpaid step is a SECOND prescribed reset after this transaction's actual signed debit, with an additional nonconstant sibling still carrying its old full reference, or a useful generic signed source profile with an absolute original influence price. No arbitrary replacement reference is authorized merely by closeness in total variation. NEXT should pay that repeated direct-source or correlation-preserving reset from the measured SAME remaining account; a further census or precision refinement does not replace the missing ownership proof.
