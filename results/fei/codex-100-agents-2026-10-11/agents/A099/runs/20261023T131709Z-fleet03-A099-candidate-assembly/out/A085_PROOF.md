# Exact ghost scope check and arbitrary-core zero-credit depth obstruction

Entropy, CE and KL are bits. Physical cubes are uniform. No universal FEI constant or FEI counterfamily is claimed.

## 1. Independent reconstruction of A079's current-reference ghost credit

Let a be ternary {-1,0,1}, b=1-a^2 on independent controller coordinates, beta=E b^2, and let h be an actual Boolean seed. For G=a+sigma*b*h, m=Eh, r=m^2,t=1-r, supply a normalized finite-CE reference R with R(empty)=r. Its coherent complete reference has signed vacuum (ahat(U)+sigma*m*bhat(U))^2 and nonempty entries bhat(U)^2 R(T). Parseval and E ab=0 give normalization, including reference-only atoms.

At a physical seed query i with hhat({i})=0, both child means are m. Set rho=R({i}). If t>0, finite CE forces rho<t. After marginalization and calibration back to empty r, the nonempty reference is t*(M_i R)(T)/(t-rho). For nonempty remaining pairs let D_* be the true-mass-weighted conditional occupancy KL between (p(T),p(T+i)) and (R(T),R(T+i)). The empty pair has true masses (r,0), hence zero erasure. On every nonempty pair the coherent wrapper carries the same factor bhat(U)^2. Summing the exact conditional CE identity gives

    B_i(G)+mean CE(P_child,Q_cal_child)-CE(P_parent,Q)
       =-beta*D_*-beta*t*log2(t/(t-rho)).

This calculation keeps both physical children, actual phases, reference-only atoms and all incoming costs. A later lambda mixture toward an arbitrary nonempty law costs at most beta*t*log2(1/(1-lambda)); therefore lambda<=rho/t is paid. Constant seeds have t=rho=0 and require no tail division; beta=0 removes the tail charge. Finite CE supplies every occupied denominator. At lambda<1 the old component preserves actual support.

Injecting singleton ghost fraction theta into a calibrated source with no such atom multiplies every occupied nonempty probability by1-theta. Its exact wrapper cost is beta*t*log2(1/(1-theta)), the same credit later removed. Thus the ghost is prepayment, not fresh phase energy. For parity3 with R=(1-rho)delta_full+rho delta_i, D_*=0 and both full signed child costs change by beta*log2((1-rho)/(1-lambda)); the sharp threshold is lambda=rho. This independently accepts A079-ZERO-SINGLETON-GHOST-CREDIT-SHARP@1 at its stated supplied-source scope, without repair. It does not accept a universal initial source price.

## 2. Embed ANY Boolean core into the phase nullspace

Fix ANY Boolean g on m bits, ANY integer L>=2, and m disjoint blocks B_j of L physical bits. Put y_j=product_(i in B_j) x_i and h_L(x)=g(y_1,...,y_m). The y_j are independent uniform signs. If U(J)=union_(j in J) B_j, exact Fourier expansion gives

    hhat_L(U(J))=ghat(J), with all other coefficients ZERO.

Hence H(h_L)=H(g), I(h_L)=L*I(g), and its mean equals Eg. Each physical influence in block j equals I_j(g), by conditioning on the other parity inputs. Any finite calibrated core reference S pushes forward to R(U(J))=S(J), zero elsewhere; normalization and finite CE are preserved and CE(P_hL,R)=CE(P_g,S). Reference-only core atoms are retained. This is a genuine Boolean construction, not arbitrary normalized Fourier amplitudes.

Every relevant coordinate has zero queried-singleton coefficient and no occupied adjacent frequency pair: U(J) and U(J') differ on whole blocks of size>=2. Thus d=0 and u_T*v_T=0 for EVERY remaining frequency pair. Every nonempty-bin phase sum, Gamma*d^2 and the refined JS separation of the two child squared laws are zero. This holds for EVERY choice of complementary controller and every partition, not just a floating-point-selected binning. A097's phase theorem correctly prescribes zero-strength extra mixtures here.

## 3. Arbitrary hidden query depth with all terminals intact

For any fixed D>=1 choose L=D+1. Consider ANY adaptive physical SEED query tree with at most D queries on each path, never querying a fixed coordinate again. Before EACH of those queries, every block still has at least TWO unqueried coordinates: fewer than L-1 coordinates can have been queried in any block. At each resulting leaf no block is fully queried. Each restricted seed is therefore

    g(s_1*parity(B_1 remaining),...,s_m*parity(B_m remaining)),

where s_j is the product of already revealed signs in block j. Squaring removes the Fourier sign product, so at EVERY node its spectrum is the SAME core squared law pushed to the remaining block unions. Both children have identical squared spectra, equal to the parent frequency marginal, even though their actual Boolean phases can differ.

Carry the same complete lifted S by physical marginalization. Its occupied and reference-only frequencies are exactly remaining block unions. BEFORE each query, the two labels of every frequency fiber cannot both lie in this support, because the queried block still has size>=2. True and reference occupancies coincide wherever actual mass is positive, so conditional occupancy KL is EXACTLY0. The queried singleton reference mass is also0. Coherent signed vacua are unchanged because m is unchanged; both full wrapper child spectra equal the full parent marginal and both references are its corresponding full marginal. Therefore actual erasure, occupancy KL, ghost credit, coherent vacuum/whole-tail calibration refund, child JS and phase-bin energy ALL vanish. CE is unchanged at EACH inherited/coherent terminal. No prior source debit or complementary sibling is omitted.

For the MATCHED core reference S=P_g, Q=P_G, so both inherited child laws already equal their actual spectra. EVERY finer-bin calibration refund is then also exactly0, for every partition. For general S, a finer-bin calibration can release existing source mismatch; that prepaid credit is not zero in general and is not new phase energy. In fact the full retained KL equals beta*D(P_g||S) at each wrapper node. The isometry retains this entire liability, rather than discarding it. This distinction corrects the overly broad initial draft wording recorded in out/SCOPE_CORRECTION.json.

For any finite stopping frontier, the reach-weighted full terminal CE equals the original CE and the intervening total erasure is0. This proves no fixed depth D can guarantee a positive local refund on all non-character/nonflat sources merely by searching more coordinates, bins or query histories. A finite-depth numerical observation without a separate width-independent structural argument cannot supply that missing universal bridge.

The depth statement is sharp as a uniform phase-delay assertion: for g(y)=y, L parity bits hide phase energy for L-1 queries; the last query has singleton coefficient+/-1. This sharpness concerns phase delay, not entropy or FEI. For nonflat examples choose the three-bit point defect g=-1 only at0: ghat(empty)=3/4 and all seven other coefficients=-1/4. Width2 gives an explicit six-bit nonflat Boolean source with H=4-(9/16)log2(9)>0 and I=3/2, but all six relevant seed queries have the complete zero-credit behavior. Tensoring k such cores gives unbounded entropy k*[4-(9/16)log2(9)] while retaining zero credit at every initial query. The H/I ratio is constant; this is NOT an FEI counterfamily.

A smallest-dimension entropy-bearing ALL-coordinate zero-phase example is even smaller: on THREE seed bits set h=-1 precisely at truth indices0,7, otherwise+1. Its expansion is h=(1-x1*x2-x1*x3-x2*x3)/2, so its spectrum is1/4 at empty and the three pairs, zero elsewhere; H(h)=2,I(h)=3/2 and every physical influence is1/2. All queried singletons and adjacent coefficient products are zero. An exact census of ALL22 labelled tables of dimension<=2 confirms that any table satisfying this all-coordinate phase-null condition has a one-atom spectrum and H=0; thus seed dimension3 is minimal for this stated condition. No minimality of the full controller wrapper or of nonflat examples is asserted.

For this three-bit seed and original beta=3/8 controller, use matched R=P_h. Query ANY seed bit; both actual children are nonconstant two-bit point defects with spectrum1/4 at every frequency. In each current conditional nonempty tail mix63/64 of the uniform three-atom law with1/64 of a singleton target, keeping the true empty mass1/4 and the full signed vacuum. The exact positive increment on EACH full child is

    (3/32)*log2(131072/130977) > 0,

since the favored conditional-tail ratio is32/33 and the two others64/63, and32*64^2=131072>33*63^2=130977. The query erasure, occupancy, all calibration refunds, ghost credit and phase energy are0. This refutes free positive-strength transport funded solely by current query refunds even on a non-character, entropy-bearing source where EVERY coordinate is relevant. It does not show that this target conversion is necessary or globally unaffordable.

## 4. The nullspace contains the full source-pricing problem

Suppose a dimension-independent entropy theorem H(h)<=K I(h) were proved for ALL width2 parity embeddings of arbitrary Boolean cores. Then for EVERY g,

    H(g)=H(h_2)<=K I(h_2)=2K I(g).

Conversely a full FEI bound applies to that subclass. Likewise, a universally supplied normalized source with CE(P_h2,R)<=K I(h_2) would imply full FEI with constant2K, since H<=CE. Thus dismissing the isospectral zero-credit sector as only parity characters hides the whole arbitrary-core initial-pricing problem, within factor2. This does not contradict the older B17 zero-erasure transport lemma: that lemma already allows a zero-erasure deletion, but does not price a fresh source or promise positive phase at bounded depth. The new result here is the full arbitrary-core/reference embedding and uniform hidden-depth scope obstruction, not a reproof claimed as new of the old single-coordinate identity.

## 5. Exact remaining gap

For matched R=P, each zero-credit full wrapper terminal is already actual. Any genuinely different normalized reference on its occupied support has strictly positive KL cost, unless it leaves that actual law unchanged. No conversion is intrinsically required by this construction: ordinary marginal continuation remains admissible. A claimed universal supplier must therefore either exhibit an ACTUALLY NECESSARY incoming-to-target conversion and its SAME unused source surplus, or design a construction avoiding it while still influence-pricing arbitrary core entropy. Neither necessity nor initial universal source price is proved here.

The all-parameter assertions above are algebraic proofs, separately checked on the frozen finite domain. A079's original ghost theorem is independently reviewed; the new arbitrary-depth/source-pricing scope theorem awaits external review. No formal verification is claimed. Full C018/C019/C020/C024 and FEI remain OPEN.
