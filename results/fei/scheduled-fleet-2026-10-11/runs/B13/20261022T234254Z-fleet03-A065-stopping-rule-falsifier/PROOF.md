# Core histories preserve the carrier; their reset booking need not stay small

This is an exact history-transfer interface and a scoped falsifier. Entropies and KL are in bits. Independent review is pending. Full FEI remains OPEN.

## General invariant, including every reference-only row

Let g be any Boolean core, R any normalized spectral reference supporting its squared Fourier spectrum p, and let u,v be fresh bits. Write F=(-1)^((u+v+L(y)+c)v)g(y,z), for any linear parity L and affine bit c. The lifted reference is Q(su,sv,T,Z)=R(T xor su*L,Z)/4; the actual law has the same form with R replaced by p. sv is a separate free frequency bit. No assumption that R is a product or equals p is made.

Query ANY non-carrier physical coordinate j. On erasing j, the reference is R^{-j}(Trest xor su*Lrest,Z)/4: if L_j=1, the two j terms merely swap when su changes. The actual erased source has the identical lift of p^{-j}. The physical child functions have the SAME carrier with c replaced by c+b L_j, and core g_b. Their squared laws are lifts of p_{g_b}/4. Hence on positive erased source rows the child kernel is p_{g_b}/(2 p^{-j}), exactly the core-only kernel. On zero-source rows BOTH use the prescribed fair kernel1/2. The predicted physical reaches equal the core-only reaches, and after normalization Q_b is exactly the lift of the actual core-transported R_b. All reference-only rows survive. Outcomes have positive predicted reach because Q supports p and each actual physical restriction is a normalized Boolean law.

Thus arbitrary finite adaptive histories on non-carrier coordinates preserve the lifted-reference form, by induction on the actual history. Masked and unmasked core coordinates both qualify. No independence of query choices is required. In particular ordinary core restrictions cannot create the erased carrier imbalance eta from A064: eta remains0, and subsequent v query always has O_v=0. An actual breaking history must leave this factorization/reference class (for example consuming a carrier coordinate), not simply fix an ordinary core bit.

K=KL(p_g||R) equals KL(p_F||Q) because the four equal lift factors cancel. Likewise each ordinary query has the SAME O and erasure credit E as the core-only query. The exact chain is K=E+O+mean K_child. This uses source-supported references and nonnegative E; it does not assert that a reset is free.

## Complete signed booking after an interposed query

At a node where v will be exposed next, its two actual terminals are g and a character translate of g. Both have full H(g) and full TC(g). The needed nonnegative booking is b=[TC(g)-K]_+. Keeping K+b as potential pays the zero carrier outcome cost and retains the full terminal product KL. The general erasure-pair bound prices O only, not b.

If first a declared ordinary data query j is made, followed in each branch by carrier conversion with complete child bookings b_0,b_1, the least nonnegative PENDING booking at the pre-data node is

    B_j = max(0, (b_0+b_1)/2 - E_j).                 (1)

Indeed incoming potential K+B_j has drift E_j+O_j+B_j-mean b_child >= O_j. Conversely any nonnegative booking paying that drift must satisfy (1). For stopping either before the extra data query or after it, include the immediate carrier option: B=max(b_current,B_j). A fixed old b_current cannot be assumed to dominate B_j.

For arbitrary finite declared core histories with a carrier-conversion option at each stopping node, the exact conservative recursion is

    B_rho=max([TC(g_rho)-K_rho]_+,
              max_declared_queries(mean B_child-E_query)).

A max over no continuation queries is omitted. This is a finite backward recursion; it requires no optional-stopping limit. P=K+B pays every declared core query outcome, and the carrier terminal retains full H+TC. One ORIGINAL source account S with old booking omega must actually supply B_root in addition to omega. Neither KL conservation nor this recursion proves that such unused capacity exists for arbitrary g/history. The universal eligibility gap remains visible.

## Actual finite stress history

Use A061's bilinear-field core h(a,b,x)=psi(a)(1-2*1[x=ab]) at field width l=2 or3, A064's common two-bit bent carrier and physical shear, and its actual uniform root product reference. Query selector s and retain its normalized Bayes references, including reference-only rows. In the H branch, expose the FIRST physical core bit (the psi-sensitive a direction), retain both actual Bayes child references, then expose v and convert explicitly to actual products. The G branch may follow the same ordinary-data/carrier order. Original reaches remain fair; the H branch is reached with physical probability1/2. This is a legitimate history of the SAME root function and reference, not a manually tilted artificial reference.

PILOT.json already certifies that at l2,j0 the branch booking increase B_j-b_old is strictly greater than 11/25 (0.44) bits, while eta=0 in both children. Full sweep and source-account comparisons are recorded separately when complete. The old tiny deferred booking bound from A064 is scoped to selector then carrier, so it is not itself refuted. The falsified extension is that its original booking remains sufficient after an interposed ordinary data query. Both complete child terminal laws are retained in INTERPOSITION/child records. Global reference-kernel tensor amplification is NOT assumed; a two-module first-selector prediction check detects its failure. The earlier entropy/influence product witness remains valid.

## Independent A062 review

A062 v6's all-price early-tag obstruction has been independently reconstructed at its stated scope: clean character-times-bent branches cost at most4 per influence; E_k/O_j is the actual paired recurrence; the O_j bound15/16, E_(j+2) margin -21/128, width2/4 bases and majority3 zero reserve all hold. Its packet lambda lower bound gives epsilon>2^-k(k-5C/2) at every C>=6. Raising a fixed price cannot repair early tag priority. This independently reconstructs the NEW all-width zero-profile induction, without adopting unrelated bundled outputs or claiming independent implementation of the reused log kernel. A065 supplied the earlier finite prefix/product input consumed by v6, so this is NOT counted as independent acceptance of the ENTIRE v6 dependency chain. No repair to the all-width induction is supplied here; full-chain external review remains A087/A094.

## First unsupported universal line

A non-carrier general history has an eligible original unused source S-omega dominating the finite full-booking recursion, or admits a selected pairing/reveal rule outside fresh carriers that controls the same signed costs. Core-only histories keep exact pairing; their terminal booking still changes. The next useful target is payment of that complete signed reset from the SAME original capacity, not a renewed eta estimate or another early-tag price sweep.

## Completed exact frontier and asymmetric stopping cut

INTERPOSITION.json contains all30 labelled one-data-query cases at l2,l3; all preserve eta=0, including reference-only rows. The l3 new bookings are exactly zero. At l2 the G branch booking is zero and all six H directions increase the required booking; the largest increase is in each a/b direction (coordinates0--3). For the explicit direction0:

    b_old = 11 -(3/2)log2(3) -(5/2)log2(5) -log2(7),
    B_new = 13/2 -(9/8)log2(3) -(5/8)log2(5) -log2(7),
    Delta = B_new-b_old = -9/2 +(3/8)log2(3)+(15/8)log2(5) >11/25.

The data erasure credit E is EXACTLY0 here; both data-child inherited KLs are log2(7/4). The two core terminal entropies are both7/2, their actual TCs differ, and their positive reset bills are retained separately in the output. Reference-only mass1/8 survives each carrier step. The inequality Delta>11/25 follows by logarithm monotonicity from the exact integer comparison3^75*5^375>2^988. No floating sign or log-interval overlap proves it.

Consider the actual asymmetric cut: query selector; STOP its G branch with its full inherited Bayes reference; in its H branch query the first core bit, then carrier v, then explicitly convert all four actual terminals to their products. Root and stopped G reference KL are retained. The complete cut has

    E KL_terminal + E sum O - K_root - W_old = Delta/2 >11/50.

The mean FULL terminal entropy is11/4, so equivalently the same shortfall appears in E CE_terminal+E sum O-(K_root+W_old+E H_terminal). This is a real expected cut shortfall, not a high price on one rare node. DIRECT_REPLAY.json reconstructs the entire nine-bit parent by explicit GF4 multiplication and direct character sums, separately transports normalized references, and checks this exact prime-log identity. Original S=23/2 is independently rechecked as actual mean(4I-H), including direct edge counts.

Global tensor amplification FAILS at its first unsupported line: the prescribed fair extension on source-zero rows is global, so normalized reference transport need not factor over independent Boolean modules. On a two-module product, the first selector predicts53/256 instead of1/8. Its other-module reference mass on actual source support is25/32; hence the exact prediction is(25/32)(1/8)+(7/32)(1/2). NON_TENSOR.json certifies this countercheck. No all-L growing-debt claim is made for this new reference-based cut. The earlier A065 entropy/influence product argument did not use reference kernels and is unaffected.

For every declared direction at l2,l3 the updated TOTAL expected root booking W_new (including the original W_old, topped up ONCE) obeys W_new<S/50. The sharpest l2 value is B_new/2. Its bound follows from3^225*5^125*7^200>2^1208; the remaining l2 directions are checked exactly and l3 has W_new=0. If earlier other bookings omega<=S/4 stay booked, then S-omega-W_new>73S/100. Equivalently, from an already booked omega+W_old, consume only W_new-W_old; do not book W_new a second time. Both full H+TC and reference-only rows remain at every actual stopping boundary. These payment quantifiers are the fixed finite l2,l3 frontier not arbitrary field widths, product modules or arbitrary histories.

The structural lift invariant applies to ALL finite adaptive non-carrier histories in arbitrary dimension. The small certified payment applies only to the declared one-data frontier. The next unpaid step is an original-source bound on the full booking recursion after another ordinary data query, or at a genuine exit from the carrier/reference factorization; ordinary core exposure alone never creates eta. External independent acceptance is pending.
