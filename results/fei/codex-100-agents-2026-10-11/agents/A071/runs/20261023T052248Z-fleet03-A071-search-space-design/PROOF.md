# Complete bounded four-core continuation

Entropy is in bits. This proves a finite restriction-family theorem, conditional on the credit already supplied at the retained terminal. Full FEI remains open.

## Boolean domain and completeness

Let g on six bits be negative exactly on {0,1,2}; let h be negative on {0,1,2,4,8,16,32,6,17,40}; put J(x)=-h(x xor1). The retained function is Fplus=J(-1,+1,g,g,g,g). Its four-input outer truth table K is +1 precisely on {0,1,2,4,8,10}. All four inner cores use disjoint uniform physical bits. Put S(f)=4I(f)-H(f), and A=-S(Fplus)>0. A is already supplied by the original stopped donor; this theorem does not raise it afresh or reprice any donor.

Every restriction of g, after removal of pointwise dummy coordinates, is one of the twelve literal profiles: P=+1, A_m negative only at0 for0<=m<=5, and L_m negative exactly on{0,1,2} for2<=m<=6. A_0=-1. For A_m each physical query has children A_(m-1),P. Each of the two special coordinates in L_m has children A_(m-2),A_(m-1); each other coordinate has children L_(m-1),P. For L_2 there are no padding coordinates. Dummy deletion changes neither the function nor its spectrum, query cost or credit. A queried dummy has identical children and leaves credit fixed.

The implementation exhausts all3^6=729 labelled restrictions and all1458 available physical restriction/query rows. Each raw transition either is a dummy or agrees with a listed profile transition after literal dummy deletion. Thus the product domain of12^4=20736 profiles is complete for every physical restriction and adaptive policy on these24 fixed bits; no other Boolean gate or dimension is silently included.

K is literally invariant under swapping physical cores2 and4 and under swapping3 and5 (indices in the original J). All16 truth values are checked for each permutation. Sorting the two profile pairs gives(12*13/2)^2=6084 full spectrum orbits. An admitted mask is permuted together with its profiles. Old credit paths remain labelled; there is no averaging over histories. Across all15 nonempty masks there are8280 distinct admitted-mask/profile orbits. The labelled admission cuts count is4*12*3+6*144*2+4*1728=8784, of which6912 admit the fourth core.

## Independent spectral reconstruction

For each inner profile, direct character summation computes its Walsh coefficients and H_j, I_j, mu_j. Direct physical edge counts independently agree with the Fourier influence sum. Let v_j=1-mu_j^2 and let Khat be the ordinary four-bit Walsh transform of the literal table. For each occupied subset U define

    c_U=sum_(M containing U) Khat(M) prod_(j in M\U)mu_j,
    p_U=c_U^2 prod_(j in U)v_j.

Expanding K in the orthogonal centered product basis proves these are the occupied spectral masses. They sum to1. Let q_j be K's true pivotal probability in coordinate j, averaged over the other independent signs with means mu. The weighted physical-edge formula computes q_j directly, and each state checks sum_(U containing j)p_U=v_j q_j.

Conditional on an occupied U, disjoint physical Fourier subsets factor across the occupied cores, with each core's nonempty Fourier law normalized by v_j. Shannon's chain rule and the ordinary first-moment identity therefore give

    H(F)=H(p)+sum_j q_j[H_j-h2(v_j)],
    I(F)=sum_j q_j I_j.

If v_j=0, its nonempty masks have zero mass and its H_j and I_j vanish. The displayed expression is still valid, with no division by0. This derives the product formula without assuming a product law for the outer occupied set. The primary spectrum engine uses direct Walsh-subset coefficients; the pilot compares all144 two-core states to the independently centered-transform source engine. The source review reconstructs all3456 A075 triple state instances by the new subset formula.

All resulting H and S values are exact rational linear combinations of log2(prime). Rational factorization and cancellation prove equality. Nonzero comparisons use directed192-bit rational log intervals, derived from an80-term atanh series with its explicit geometric tail bound. An unresolved sign raises an error; no floating tolerance decides any result. Times and memory figures are observational metadata only.

## Sharp stopping hull and owner preservation

For a fixed admitted subset M, allow stopping and all physical queries in its cores. On the finite acyclic restriction DAG, define

    rho_M(s)=max(0,-S(s),max_(query in M) mean rho_M(children)).

Backward induction shows rho_M is the largest expected terminal (-S)_+ over all such stopping policies. It is the least nonnegative superharmonic majorant. Indeed a policy either stops or chooses one query and then separate child policies; this is a Bellman argument, not multiplication of conditional bounds. Conversely a maximizing policy attains the maximum on this finite DAG.

For incoming a>=rho_M(s), set

    a_b=rho_M(child_b)+a-mean rho_M(children),
    d_b=S(child_b)+a_b.

Both quantities are nonnegative; mean a_b=a. With D=S(s)+a and e=mean S(children)-S(s)=H(parent)-mean H(children)-4 Inf(query), one has mean d_b=D+e. Every old signed debit label L and the newly booked signed query label e is transported using the common kernel d_b/(D+e) when that total is positive. Each label's conditional mean is preserved and the sums equal d_b. At total0 both outgoing debits vanish; kernel1 retains the old and new signed labels whose sum is0. Credit-owner labels use kernel a_b/a when a>0; if a=0 all outgoing credits are0. Nonnegative credit owners stay nonnegative. Hence all original owners are retained separately, without an outside flow, a future full-child-positivity assumption, or a new donor draw. Other stopped terminal functions and all earlier spent donor accounts stay untouched.

Necessity: any nonnegative, mean-conserved credit covering nonnegative stopped debit must dominate (-S)_+ at every stopping state. Its initial credit consequently covers the maximal stopping expectation. Thus the hull is sharp for this supplied-credit model. The existence of a universally influence-paid initial bank is not a consequence.

## Actual histories and sequential admissions

Admit one core at the root. At any later state one may stop, query any already admitted core, or admit a previously untouched core. An admission changes neither the full Boolean state nor the actual incoming credit. Between admissions use the exact hull allocator for the current mask. A later core may be chosen in response to all preceding answers. Admitting a core before querying it is allowed. Every adaptive physical policy is representable by admitting each distinct core when first needed.

For a fixed labelled mask/state, let amin_M(s) be the minimum actual credit over every history leading there from initial A. There is a finite minimum: queries decrease the number of free coordinates, while admissions strictly enlarge the mask. Each child allocator has slope1 in the actual incoming credit, so minimum propagation is exact. The primary checker propagates minimum arrivals forward over all possible admissions and query choices. The second checker reconstructs these minima from all reverse predecessors: either an admission predecessor with an untouched core, or a physical query predecessor with its actual delta rho(child)-mean rho(children). This enumerates histories without replacing any source allocation.

The exact saved result is

    rho_all4(root)=A,
    max_(every admission M->M+j at every state s)
        (rho_(M+j)(s)-amin_M(s))_+ = 0.

All8784 labelled cuts are checked, including all6912 fourth-core cuts. Thus every actual credit covers the enlarged hull. Repeated Bellman induction pays every continuation using the SAME original A, all prior owners and the already spent donor. A check only at the root would not imply this stronger history statement.

If an arbitrary real old net debit D>=0 was already supplied together with initial credit A+D, every child allocation and every unchanged admission sends the extra D forward with coefficient1. Consequently every actual arrival shifts by exactly D; the zero thresholds remain sufficient for all real D, without a parameter grid. This does not promise admission for arbitrary alternative past credit allocators. The prescribed allocator is part of the hypotheses.

## Review and first unsupported universal line

The A075 three-core claim is independently reconstructed unchanged: all3456 source S/rho entries agree exactly and all864 stronger source paths are replayed using original physical coordinate labels and their true dyadic reaches. This is independent source acceptance because the critical spectrum representation, Bellman code and path reconstruction differ. The bounded logarithm primitive is shared and attributed. The second checker of this new four-core theorem is an author audit, not external independent acceptance.

The first unsupported universal line is to construct a dimension-independent signed-component superharmonic envelope whose initial credit is paid from influence, uniformly over arbitrary Boolean outer spectra and physical restrictions. This finite domain starts with an already subsidized negative terminal, so its successful closure does not supply that bank. No unbounded H/I Boolean family, all-dimensional proof, Lean certificate or universal rate4 bound is claimed.
