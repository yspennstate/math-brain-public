# Shared phase queries preserve a specified source book after refined calibration

All entropies and cross entropies are in bits. This is an extension of the existing A056 transport candidate, not an all-dimensional FEI theorem. Its general reference-closure assertion has an analytic proof below. The rate7 surviving-terminal assertion is separately certified only on the frozen finite domain.

## 1. Model and the previously missing transition

Let u,v be arbitrary Boolean signs on the same finite uniform cube S. Let Ru,Rv be normalized references supporting their true squared Fourier laws Pu,Pv. Empty-calibrate them: Ru(0)=(Eu)^2 and similarly for v. Retain arbitrary nonempty conditional laws, including reference mass at zero true coefficients. Put cu=CE(Pu,Ru), Du=cu-H(u), and similarly for v.

Let disjoint private point events A,B have probabilities a=2^-r,b=2^-s. Put G=1+A(u-1), H=1+B(v-1), and let F be their fresh fair mux. Selection weights are pi=1/2,1/2 before selection, or 1,0 afterwards. Failed and zero-width events are allowed. Define wu=pi*a,wv=(1-pi)*b.

Use the stage6 reference Q: all shared-only root atoms are their true masses; private-only empty-phase atoms also have true mass; each exclusive nonempty-private/nonempty-phase atom has the appropriate mux coefficient factor times a^2 Ru(T) or b^2 Rv(T). The formula includes reference-only phase atoms. Consequently

    D(PF||Q)=wu(1-a) Du + wv(1-b) Dv.                 (1)

The independently derived stage6 price remains

    CE(F,Q) <= wu cu + wv cv + Icore + 7 Icontrol,
    Icore=wu I(u)+wv I(v).                            (2)

No new source certificate is asserted in (2).

Query a physical coordinate i in S. The source references are not replaced by uniform or actual descendant spectra. For each phase, merge the spectral pair T,T+i, use its true physical outcome kernel, normalize at each outcome, then calibrate its empty/nonempty partition. These operations uniquely prescribe Ru,t and Rv,t once the zero true-fiber extension is fixed. At zero true pairs use the fair extension in both the phase and root reference. This rule is part of the construction; arbitrary unsynchronized completions are not covered.

## 2. Exact closure requires a finer partition

For a source phase, write A_T=uhat(T), B_T=uhat(T+i), where i is absent from T. The pair has true mass M_T=A_T^2+B_T^2 and reference mass N_T=Ru(T)+Ru(T+i). Its physical kernel is

    K(t|T)=(A_T+(-1)^t B_T)^2/(2 M_T)                (3)

when M_T>0. The kernel is fair when M_T=0. Thus the unnormalized child reference is N_T K(t|T); let zu,t be its total mass. Positive true child probability implies zu,t>0: support domination and the true pair kernel give positive reference mass on every positive child atom. Normalize by zu,t, then set the empty mass to the actual squared child mean and rescale its entire nonempty complement. This preserves all nonempty likelihood ratios within that complement.

Transport the root Q with its own physical kernel. For a nonempty remaining phase set T and a nonempty private A mask, the two parent root amplitudes are the same fixed signed mux/private factor times A_T,B_T. Therefore their kernel is exactly (3). Their root reference pair mass is the same squared factor times N_T. The statement remains true on reference-only pairs because the phase and root zero extensions agree. Hence the nonempty child phase reference inside each exclusive owner is proportional to the nonempty part of Ru,t, uniformly across remaining private masks and the selector spectral coordinate. The same holds for v.

The phase-empty packet is different: on a private owner its amplitudes contain uhat(0)-1, rather than uhat(0). It need not have the phase kernel. It must therefore be a separate calibration category. Partition root child atoms into:

* every shared-only atom individually;
* exclusive A-owner empty-phase atoms, and exclusive A-owner nonempty-phase atoms;
* the analogous two B-owner categories;
* zero true two-owner atoms (discard their reference mass).

Calibrate the mass of each category to its true child mass, retaining the conditional reference within it. Empty-phase private amplitudes and reference masses are uniform over the nonempty private masks and selector copies, so their category becomes exactly the prescribed true private-only law. The preceding proportionality gives the required nonempty owner law. Shared rows are singletons. These categories exhaust the support. The result is precisely the stage6 reference rebuilt from the prescribed transported phase references Ru,t,Rv,t. This is an atomwise proof for arbitrary dimension and bias, not an inference from the finite census.

The older owner-total partition did not justify this transition: it mixed empty and nonempty phase packets. The refinement is necessary to the present proof. No assertion that every choice of categories works is used.

## 3. Normalizers and paid reference release

For any such physical pair transport, relative entropy has the exact chain rule

    D(P||R) = Eerase + Doutcome + E_t D(Pt||Rpost,t).

Eerase is the conditional KL lost by merging each pair. Doutcome is KL between the fair physical outcome and the reference outcome zt, namely -(log2(2z0)+log2(2z1))/2. Both are nonnegative. Categorical calibration saves KL of the true category distribution against its inherited category distribution, also nonnegative. Thus source release

    ru = Du - (Du,0+Du,1)/2 >= 0

includes every source normalizer and the source empty/nonempty calibration. The root release, after its refined categorical calibration, is exactly

    Rroot = wu(1-a) ru + wv(1-b) rv >= 0.             (4)

Equation (4) follows by applying (1) before and after the query; the owner weights and event probabilities do not change at a shared query. Independently, it equals root Eerase + Doutcome + mean categorical saving. It is not an allowance to choose a fresh unrelated descendant phase reference.

For the physical entropy, merge the true spectral pairs to a law M on remaining subsets. The joint law of the fair outcome and child spectrum has mass Pt(T)/2 and marginal M. Therefore

    H(F)-E H(Ft)=B_i(F)+I(outcome;remaining spectrum).

All terms on the right are nonnegative. Combining this identity and (4) gives the exact full account

    CEroot = B_i + JS_i + Eerase + Doutcome
                       + E categorical_saving + E CEterminal.       (5)

Both terminal H+KL bills and all normalizers appear. The channel terms and the complete expected terminal cost in (5) are paid from the original CEroot, hence from (2). This part is general closure of a specified reset; it does not independently prove an influence-priced source reference exists.

## 4. Original source potential through arbitrary physical histories

The construction can be iterated after any shared query, and combined with stage6's private/selector point kernels. Use the refined categories at shared queries; the prior compatible private rule still applies at other queries. Let current phase costs be their actual transported/calibrated CE, not freshly certified bounds. Physical entropy and reference KL are both supermartingales under their respective prescribed query/transport, so current phase CE is a supermartingale under a shared query.

Define

    V=wu cu,current + wv cv,current + Icore + 7 Icontrol.

At a shared query, the expected phase-cost part cannot increase, Icore decreases by the actual queried influence, and Icontrol is harmonic. At a private or selector query, the phase-cost and core parts are harmonic and Icontrol decreases by the queried influence. Thus Vroot pays

    E CEterminal + sum_shared reach*Inf_query
                         + 7 sum_controls reach*Inf_query <= Vroot. (6)

No terminal coefficient in (6) is multiplied by a newly issued source certificate. The one-unit core mark and seven-unit control mark are original quantities. Finite-tree telescoping proves (6), since CEterminal<=Vterminal by (2). If original source costs obey cu<=Cu I(u), cv<=Cv I(v), then Vroot<=K Iroot for K=max(Cu+1,Cv+1,7). This expected gross-bank statement is distinct from CEterminal<=K Iterminal at every reached leaf or in expectation; that stronger terminal admission does not follow from an original source certificate alone.

## 5. Exact finite terminal admission and boundary controls

The frozen domain consists of all labelled two-bit phase pairs, private widths (1,1),(2,1), two source laws and each shared coordinate; and a specified three-bit family covering all256 u with one prescribed transformed partner v, widths(1,1), both laws and each shared coordinate. This is not all three-bit pairs. The source uniform law uses equal nonempty weights; the index-weighted law uses weights j+1, normalized and empty-calibrated.

The copied two-bit source4I assertion fails on three-bit weighted dictators: a singleton assigned2/35 gives CE=log2(35/2)>4 since35>32. This is a reference-cost counterexample, not an FEI counterexample. The frozen amendment uses source6I, retaining the same rate7 in (2). The checker verifies source6I, closure, every root/source normalizer, decomposition (5), nonnegative KL terms, and the stronger mean-terminal inequality E CEterminal<=7 E Iterminal directly. It preserves nonzero terminal KL in selected three-bit examples and explicitly counts both-nonconstant-root-child cases. See out/checks.json for actual counts, not the prospective case count.

Boundary checks include constant phases, failed/certain child spectral sectors, zero true Fourier pairs carrying reference-only mass, changing child means, deterministic one-bit phases and spectral cancellation. Disjointness is used only for private control blocks and their influence identities; u and v may overlap completely. Booleanity makes physical outcomes fair and their spectra normalized. Positivity of outcome/category denominators follows from support domination where true mass is positive; zero true categories are set to zero without division.

## 6. First unpaid universal line

The all-dimensional closure and gross-bank theorem require supplied original influence-priced source references. The finite stronger terminal admission does not provide such references for arbitrary phases or certify arbitrary descendants at the same rate. The next step is one nonflat shared query followed by a private query with both full terminal references and the old debit retained, using a proved hereditary source surplus or a quantitative signed refund. General fresh occupancy/floor resets remain outside this construction. Full FEI remains OPEN. No independent acceptance or full Lean certification is claimed.
