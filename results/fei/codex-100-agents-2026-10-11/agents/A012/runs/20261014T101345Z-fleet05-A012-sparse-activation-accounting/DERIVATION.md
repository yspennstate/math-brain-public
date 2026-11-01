# All three-bit phase pairs with a common arbitrary private event

Bits throughout. Uniform physical Boolean cubes; ideal probability costs. This refines the existing admission packet, not a universal FEI claim.

## 1. Exact family and collision ownership

Let c,h be any Boolean signs on three shared bits s (dummy bits allowed), W={s:c(s)!=h(s)}, m=|W|, and E an arbitrary Boolean event on an independent private cube V. Put theta=Pr(E), kappa=1-2 1_E, and define G=c(s), H=c(s)(1-2 1_W(s)1_E(V)), F=mux_z(G,H), with fresh selector z. One common event is used at every changed shared row; unequal or separately varying row probabilities are not assumed to be covered.

Let a_T=chat(T), b_T=Fourier(c 1_W)(T). Then Hhat(T)=a_T-2theta b_T on shared-only frequencies; Hhat(T,U)=b_T kappahat(U) for U nonempty private. Parseval gives sum b_T^2=m/8. The actual selector influence is d=m theta/8, and shared minority mass before folding is delta=m theta^2/8. Parent shared amplitudes are a_T-theta b_T and theta b_T. Private frequencies belong to H alone, and their parent selector probabilities are equal. Their full erasure mass is v_H/2=2(d-delta), v_H=(m/8)(1-mu^2), mu=1-2theta. Therefore exactly

    B_z=2(d-delta)+sum_T Phi((a_T-theta b_T)^2,(theta b_T)^2),
    Phi(A,B)=L(A)+L(B)-L(A+B), L(x)=x log2(1/x).

Set d*=min(d,1-d). The target is B_z<4d* when d*>0, with zero erasure at d*=0. Folding H to -H exchanges selector-frequency atoms and preserves child spectra, B, JS, CE and reference debts. The physical influence accounting remains I(F)=(I(G)+I(H))/2+d, using original physical coordinates. Collision influence is reserved once, never added on top of an already paid outside contribution.

## 2. Exact finite reduction and real continuum

Every c,W is represented by two eight-bit masks. Integer/rational Walsh transforms exhaust all256x256=65,536 pairs. For each frequency simultaneous sign reversal of (a,b) preserves both squared arguments; normalize b>=0 (or a>=0 if b=0), then sort the eight pairs. Together with m this gives exactly46 profiles. ALL_PROFILES.json contains every profile, its multiplicity and an actual representative. Their multiplicities sum65,536. Independent verify.py recomputes each Walsh coefficient by direct character sums, without the Walsh helper, and reproduces precisely the profile multiset. This is a finite classification of eight-point phases, not an unproved extremal reduction of arbitrary private means.

Analytic pruning applies to arbitrary three-bit shared overlap when private branches are disjoint (G has no private coordinates here). After folding, the shared minority cap is delta_f<=min(d*,8d*^2): conditional means u,v satisfy |u-v|<=1-uv, so every shared difference coefficient has magnitude at most2d*. Jensen bounds shared erasure by h2(delta_f); hence B<=2d*+h2(delta_f)-2delta_f. For 0<d*<=1/32, monotonicity of q log2(e/q)-2q up to1/4 and x=8d*<=1/4 imply B/d*<=2+x[1+1/ln2-2log2 x]<=2+(5+1/ln2)/4<4 (ln2>2/3). For d*>=1/6, maximize h2(q)-2q at q=1/5: B<=2d*+log2(5/4)<2d*+1/3<=4d*. verify.py checks the strict logarithmic bound rationally. At d*=0 the branches are identical/opposite pointwise, giving B=0.

The remaining continuum uses128 equal rational theta intervals for each profile. For theta in[l,h], set A_Tmax=max((a_T-l b_T)^2,(a_T-h b_T)^2), B_Tmax=max((l b_T)^2,(h b_T)^2). Phi is increasing in either argument (partial derivatives log2(1+B/A), log2(1+A/B), and continuous axes). Define

    R(theta)=4 min(m theta/8,1-m theta/8)-m theta/4+m theta^2/4.

Then 4d*-B>=min(R(l),R(h))-sum Phi(A_Tmax,B_Tmax). The minimum is at an endpoint: below m theta/8=1/2, R=m(theta+theta^2)/4 is increasing; above it, R=4-3m theta/4+m theta^2/4 is decreasing on[0,1]. The kink is a maximum. This proves the interval bound including crossing intervals.

All5,888 seed intervals were covered without subdivision. Of them1,880 have strictly positive outward rational certificates, and4,008 lie entirely in zero/rare/moderate regimes. Smallest saved positive lower bound is1342651833647/281474976710656. Author logs use32-term exact rational atanh bounds, range reduction and a proved tail, rounded down to2^-48. Independent verify.py imports no author logarithm code and uses64 rational terms, direct L(A)+L(B)-L(A+B) instead of the author's positive direct-log Phi expression. It checks every saved bound, every pruning domain, and contiguous exact coverage from0 to1 for each profile. No floating grid sign is used in the proof. Therefore all real theta in[0,1] satisfy the target, including every finite Boolean event in every dimension.

The standard scalar JS bound is JS_z<=2d*/ln2. Coefficientwise it follows from ((1+x)ln(1+x)+(1-x)ln(1-x))/2<=1-sqrt(1-x^2), followed by the shared/minority square sum. Consequently Delta=H(F)-average child H=B_z+JS_z<=K d*, K=4+2/ln2<7.

## 3. Whole reference and explicit controller retention

For arbitrary supplied normalized child references positive on true support and of finite cost, calibrate each shared-only atom to its true mass and rescale the private complement while preserving its conditional reference law, including off-target private reference mass. Calibration decreases CE by categorical KL. G's calibrated reference is its true spectrum. Set Q=P_F on all shared-only output rows; on private H frequencies set Q(u,T,U)=R_Hcal(T,U)/4 for each selector sector u. This is a single fixed normalized reference: shared mass1-v_H/2, private reference massv_H/2. Direct expansion gives

    D_F=D_Hcal/2,
    CE_F=(CE_Gcal+CE_Hcal)/2+Delta,
    I(F)=(I(G)+I(H))/2+d.

Both child bills remain. If they are certified <=K times their actual influences, this reference has CE_F<=K I(F). No controller or opaque terminal receives an automatic certificate.

Explicitly empty-calibrate any prescribed reference R_kappa to mu^2, keeping its nonempty conditional law. Write D_kappa=CE_kappa-H(kappa). On nonempty private U use R_H(T,U)=b_T^2 R_kappa(U), and on shared-only T use actual Hhat(T)^2. Normalization follows from sum b^2=m/8 and the actual private mass. Its exact retained debt is

    D_H=(m/8)D_kappa, D_F=(m/16)D_kappa,
    CE_F=H(F)+(m/16)[CE_kappa-H(kappa)].

The true controller entropy is inside H(F), and its prescribed excess is retained with the displayed coefficient. For m>0 and0<theta<1, private labels have total massv_H/2. Their full CE is (v_H/2)[log2(2/v_H)+1+H(beta)+CE(private controller conditional)], beta_T=b_T^2/(m/8). Shared labels retain their exact coherent masses; together these form at most17 complete sectors. An independent common terminal factor tensors the whole reference and adds exactly its CE and KL; it is a separate product node, not an unused reserve.

## 4. Admission, physical heredity and changed nonmember

Extend the earlier literal/constant grammar by the above fresh-selector node: G must be a pure phase on at most3 shared coordinates, H switches G to another such phase under ONE physically independent private event, and BOTH ACTUAL CHILDREN must already have structural certificates. The pointwise representation identity is checked as certificate metadata. Keep earlier overlap<=2 muxes, disjoint products, sign flips, and fresh point activations. Each node constructs its complete reference as above; child calibration lowers CE. Induction gives CE<=K I, with no opaque leaves. Earlier point activation surcharge<6 is below K.

Fixing a private coordinate replaces the common event by its actual cofactor and preserves the rule; fixing a shared coordinate leaves at most2 shared coordinates (both actual restricted children remain certified by induction); fixing z chooses a certified child. Products and activations preserve physical heredity as before. Thus disjoint tensoring, balancing and rare activation are closed, and any hidden seed has equivalent membership to its fresh balanced tensor or activation: restrictions recover that seed, up to an allowed sign.

This rule admits every function on at most4 bits. Every three-bit function is already certified by recursively using overlap<=2 muxes; any four-bit function has two three-bit cofactors and the new rule with E identically1. In particular the old FOUR-BIT at-least2 nonmember is now admitted. That conclusion from v3 must not be carried forward as a nonmember for v4; prior v3 syntax itself is unchanged.

The new grammar remains proper. Take the FIVE-BIT sign+1 iff at least two binary ones. All10 one-bit cofactors depend on all4 remaining coordinates, excluding an overlap<=2 mux, and excluding the new rule because one actual child of it must have support<=3. All15 unordered disjoint coordinate bipartitions have a nonzero2x2 rank-one minor, excluding disjoint-product roots. Every activation root has a constant cofactor and is excluded as well. Sign flips preserve these exclusions. NONMEMBER_CERTIFICATE.json records exact cofactor supports and every integer minor. Its balanced tensors and rare activations remain nonmembers by physical restriction reflection. This is an admission obstruction, not a FEI counterexample.

## 5. Source consumption and exact remaining line

Read A013-TWO-ROW-ARBITRARY-EVENT-TRANSPORT@1's full report/derivation/claim and reproduce all4,093 rational rectangle sign bounds and exact subdivision coverage using our separate32-term positive-log arithmetic. This record is restricted to continuum sign/coverage reconstruction: phase classification, root-cover metadata and the full dependency chain are not independently accepted. A012 contributed earlier ownership/one-row inputs to that source, so this cannot count as full-chain independent review. It supplies a complementary unequal TWO-event family; the present theorem supplies every shared phase-pair for ONE common event. Neither contains all of the other.

First unsupported line: arbitrary three-bit private conditional means in1/32<d*<1/6 either reduce to a pure branch with a common event, or satisfy B_C<=2d*+2delta_f by another realizable signed-row argument. A common event enforces rank-one private/shared interaction; arbitrary unequal three-row events or two private branches need not have it. No such reduction is proved. Growing overlap requires an additional nonreused shared-core/terminal reserve. Full FEI remains open. NEXT tests the first unequal three-row conditional profile against the conserved collision budget and its full joint private reference, rather than extending dimensions or dropping inherited entropy.
