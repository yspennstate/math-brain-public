# One conserved rare-event account pays deep mixed pair restrictions

All entropies and cross-entropies are bits. This is a supplied-source stopping theorem, pending independent-person review. Full FEI remains OPEN.

## Theorem and explicit stopping rule

Let m>=4 be even and b(x)=(-1)^[c+sum_pairs(x_a x_b+alpha_a x_a+alpha_b x_b)], where the pairs partition the m original core coordinates. Thus b is a matching quadratic bent sign, with arbitrary affine terms. Let v!=w be any two core vertices, let b_v,b_w be their actual single-vertex flips, and use the SAME shared balancing sign and fair nested controls as stages18-19:

    g=(zb,zb_v,zb_w), f=g0+A[g1+B(g2-g1)-g0].

Allowed core queries are: choose either coordinate of any intact pair; once one coordinate has been fixed, query its partner ONLY IF its coefficient in the restricted phase is zero. A partner whose coefficient is1 is a LIVE LINEAR SURVIVOR and is not queried. The orientation/pair choice may depend on the entire observed history. Physical controls and z may be queried at any time. Stop at ANY finite frontier of such a policy. A complete pair-processing policy stops after every pair has been opened and all resulting dummy partners cleared. This is an explicit query rule, not a rule that inspects the unknown target bank for positivity.

At history h, let k be the number of remaining original core variables, r=twice the number of intact pairs, and l the number of live linear survivors. Let b_h be the ORIGINAL unedited seed restriction. Use precisely the old prescribed reference

    q_h=(P_bh+Uniform_{2^k})/2,
    nu_root=(1-3delta/2,delta/2,delta/2,delta/2), delta=2^-m,
    nu_h=the MARGINAL PROJECTION of ORIGINAL nu_root onto remaining control frequencies,
    Q_h=q_h*nu_h*mandatory_z_frequency_if_z_remains.

Deleting z projects its mandatory frequency, without admitting a new reference. Let C_h=CE(P_fh,Q_h), K_h=C_h-H(f_h), I_D(h) count the remaining original core influence plus z if live, and retain the SAME physical reserve

    R_h=2sum_{i<j}pi_h(i)pi_h(j)I(g_ih*g_jh),

with actual conditional label probabilities pi_h. Keep ONE old debit0<=U<=m/8. Then EVERY allowed mixed stopping frontier satisfies

    E B_h > 7m/8-1-(9m+15/4)2^-m >=1/64,
    B_h=4I_D(h)-C_h-U-R_h.

For every even m>=6, E B_h>m/2. There is NO expected-depth hypothesis. A complete pair-processing frontier has expected original core depth3m/4, tripling the preceding m/4 sufficient budget while retaining old U, both full KLs and R. This theorem specializes the seed class from arbitrary bent seeds to matching quadratic bent seeds; it does not strengthen that quantifier.

## 1. Rarity is one physical event, not a renewed descendant budget

Let E1={actual control label1 and core=v}, E2={actual label2 and core=w}. These events are disjoint and fixed at the ORIGINAL root. Let M_i(h)=Pr(Ei|h), M=M1+M2. If vertex i is consistent with the observed core bits, its conditional core probability is2^-k; otherwise it is0. Hence

    M=2^-k[pi_h(1)1_{v consistent}+pi_h(2)1_{w consistent}],
    M(root)=delta/2.

At every physical query, M_i(parent)=average M_i(children), including adaptive mixed choices. This is just conditional probability under the actual physical cube; history choices impose no extra condition on untouched coordinates. For a reached node of mass a, the two child lots have total a*M_i(parent). They partition the same original lot; they do not each receive a fresh copy. Let tau_i be the first revelation with M_i in{0,1}, or the chosen frontier if unresolved. After resolution, zero lots stay zero and the resolved event lot is carried through descendants without being credited again. Finite tower summation gives E_frontier M=delta/2 at EVERY stopping frontier. Our perturbation bill below is charged ONCE at that frontier against these conserved original lots, not once at every preceding node.

## 2. A conserved source potential replaces the crude query count

Matching quadratic restrictions have a flat Fourier law on an affine support of size2^r; live linear survivors translate that support. Thus

    H(b_h)=r, I(b_h)=r/2+l, Z_h=4I(b_h)-r=r+4l.

Opening an intact pair removes its contribution2 to r. With conditional probability1/2 its partner becomes dummy (new pair contribution0 to Z); with probability1/2 it becomes a live character (contribution4). The average is exactly2, the old contribution. Querying a dummy partner changes neither r nor l. Controls and z do not affect b_h. Therefore Z is a physical martingale and E Z_h=m at EVERY allowed mixed frontier, including unequal/adaptive depths. No influence supply is renewed in a child.

For a complete pair-processing policy, each pair uses1 first query plus a dummy query with probability1/2. Hence expected core depth=(m/2)*(3/2)=3m/4, regardless of adaptive pair/orientation scheduling. The original source potential, rather than raw depth, pays these histories. The zero pivots are zero only for the unedited seed; actual edited functions and their query costs are kept in the next step.

## 3. Actual edits and the full prescribed data reference

Flipping one surviving vertex in a k-cube changes each coordinate influence by at most2*2^-k. Averaging the actual control labels therefore gives

    I_D(h)>=I(b_h)-2k M(h).

An unqueried z only improves this bound by1; revealing it is already paid, not parked as a required donor.

Let A_h be the seed's affine Fourier support, |A_h|=2^r. Outside A_h the Fourier amplitude of each surviving single-vertex edit has magnitude2*2^-k, so its total outside spectral mass is4*2^-k(1-2^{r-k}). The actual core spectral marginal is the mixture of the three source spectra with ACTUAL pi_h, by Parseval on the remaining controls. Therefore its outside mass is exactly

    epsilon_h=4M(h)(1-2^{r-k})<=4M(h).

On A_h, q_h=(2^-r+2^-k)/2>=2^(-r-1); outside, q_h=2^(-k-1). Consequently the COMPLETE data cross-entropy obeys

    C_X(h)<=(1-epsilon)(r+1)+epsilon(k+1)
           <=r+1+4(k-r)M.

This bound pays every prescribed nonflat reference conversion. The actual joint law need not factor: the PRODUCT reference implies C_h=C_X(h)+C_Y(h) regardless of actual core/control correlations. All full KL terms are inside C_h and are never discarded.

## 4. The original controller and SAME R survive

As in stage18, the ORIGINAL projected controller reference CE is a martingale at core queries, a supermartingale at control queries, and unchanged at z. Hence E C_Y<=H(nu_root). The SAME physical pair-product reserve R is a supermartingale under all allowed queries, including z with zero release. Direct physical edges give R_root=(3m/2-eta/2)delta<=3m delta/2. These are identities/inequalities for actual conditional pi, not a reset to the original or a uniform child label law.

## 5. Full frontier payment and exact constants

Combine the actual influence and reference estimates:

    B_h >= Z_h-1-U-C_Y(h)-R_h-[8k+4(k-r)]M(h).

Since0<=r<=k<=m, the bracket is at most12m. Use the TWO conserved original accounts E Z=m and E M=delta/2, retaining the old U and same remaining R, to obtain

    E B>=m-1-U-H(nu_root)-6m delta-R_root
        >=m-1-U-H(nu_root)-(15m/2)delta.

The rigorous stage19 entropy envelope H(nu_root)<(3m/2+15/4)delta follows from -(1-t)ln(1-t)<t, t=3delta/2, and ln2>2/3. Therefore

    E B>7m/8-1-(9m+15/4)2^-m=:F(m).

For integers m>=4, (9m+15/4)2^-m strictly decreases, because twice its numerator minus the next numerator is9m-21/4>0. F is increasing and F(4)=1/64. Similarly F(m)-m/2 increases; at6 it is89/256>0. This proves both asserted constants in all even dimensions. Exact finite checks below are validation, not the finite-to-infinite bridge.

## 6. Both full terminals, old booking and negative branches

Keep the signed booking Delta B=4a-Delta C-Delta R, where a is the actual data-owner queried influence (including1 for z,0 for controls). It is exact because I_D has the physical influence telescope. Put W=B+4I_controls. The full identity remains

    E_leaf(W+K+R)+sum_queries reach*(4Inf_i-Delta_i H)
       =W_root+K_root+R_root.

Both full child KLs, every signed reference change, all old sibling reaches and old U survive. No source sector becomes an additional donor. In the canonical seed with even-coordinate-first queries, fully processed all-dummy first-bit outcomes have probability2^(-m/2). They leave no original core influence. With z already revealed and controls live, R=0 and B=-C_Y-U<0, since the ORIGINAL controller reference has every atom strictly below1. These ACTUAL negative leaves remain in the paid expected frontier. The theorem cannot be promoted to pointwise child-bank positivity.

## 7. Paid live-survivor continuation from the SAME diminished account

The preceding rule can be relaxed quantitatively. Allow live linear survivor queries too, and let N_h be the number actually consumed along the physical history. Such a seed query has influence1, entropy-rank decrement0, and Z_parent-average Z_child=4 exactly. All other query types still conserve Z in expectation. Thus the SAME original source has

    E Z_h=m-4 E N_h.

The flat-support and exact rare-event perturbation arguments hold after these queries, with the CURRENT restricted seed and ORIGINAL projected references. They do not require an intact-pair-only history. Hence, for every adaptive mixed stopping frontier on this matching-quadratic family,

    E B_h>F(m)-4 E N_h.

For every even m>=6, the fixed sufficient budget E N_h<=m/16 gives

    E B_h>5m/8-1-(9m+15/4)2^-m>=473/256>1.

The scalar expression is increasing for integer m>=6 and equals473/256 at6. The old U, both full terminal KLs, CURRENT q, SAME nu and remaining R are still subtracted. This pays the missing actual linear query rather than adding a donor: its full4 is withdrawn from original Z. No additional influence of z is parked; z may already have been spent.

An explicit full continuation first finishes pair processing and reveals z and both controls. On the ORIGINAL physical outcome A=B=0 only, query every retained linear survivor. On the other three controller outcomes stop. Since the pair frontier is constructed before these controls are revealed, its remaining count L has mean m/4 independently of the fresh fair controller outcomes. Therefore E N=(1/4)(m/4)=m/16 and expected original core depth=3m/4+m/16=13m/16. On that entire quarter-cube branch every core and z is fixed, both control axes are deleted from the ORIGINAL reference, and B=-U. Its negative balance is retained with physical mass1/4. No terminal or full-KL deletion is needed to pay the expected frontier.

## First unsupported universal line

An arbitrary bent restriction need not have flat affine Fourier support or the matching-pair potential Z. An arbitrary Boolean source need not supply the large original Z=m. Live survivors are now priced, but consuming them beyond the explicit E N budget can exhaust the original source; revealing all core bits and z is the exact negative-bank obstruction from stage19. NEXT is a genuine change of the nonempty seed/reference profile after this paid continuation, retaining CURRENT q/nu, full KLs, old U, consumed-survivor debit and SAME diminished R. The open step is transport from flat affine support to a nonflat supplied source without renewing the rare lot or source potential, directly testing the universal restriction mechanism.
