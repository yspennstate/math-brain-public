# Boolean-cut reserves at a three-state controller

All cubes are finite and uniform, all functions are Boolean signs, and all entropy is in bits. Let an arbitrary physical controller label map kappa(z) take values in {1,...,k}; put C_j=1_{kappa=j}. The data cores u_j occupy mutually disjoint cubes independent of z. Duplicate physical core labels must be merged. At every actual reached history, unqueried physical bits remain independent and fair. Let m_j=E u_j on their actual remaining cubes. Fix ONE prescribed finite controller-coordinate policy T depending only on its own controller history and an initially fixed independent seed; it is the same policy for every output labeling below.

## 1. The actual complete-data boundary and its unique harmonic extension

For epsilon in {-1,+1}^k define the actual Boolean controller seed g_epsilon(z)=epsilon_{kappa(z)}. Let r_epsilon(v)>=0 be a supplied C-priced potential for g_epsilon on T, depending only on controller history v. It may be the least reserve Q_C(g_epsilon,T), with sign-invariant prescribed continuations. Set

pi_m(epsilon)=product_j (1+epsilon_j*m_j)/2,
P(v,m)=sum_epsilon pi_m(epsilon) r_epsilon(v).       (1)

P is nonnegative. At every DATA query only one mean m_j changes, its fair average is unchanged, and all other block means and r_epsilon remain fixed. Since (1) is affine separately in every m_j, P has exactly zero conditional mean drift. At a complete-data frontier, every m_j is its actual constant output epsilon_j and P is exactly that actual controller seed reserve r_epsilon. No arbitrary remaining controller entropy is discarded.

Among functions of just the current vector m that are harmonic at every DATA revelation and have those prescribed vertex values, (1) is unique. To prove uniqueness without a smoothness assumption, realize each m_j as the mean of a finite Boolean core whenever it is dyadic, reveal all its fair bits, and apply finite harmonic averaging. The independent vertex law is precisely pi_m. If a continuous extension to non-dyadic means is requested, density makes it unique as well. Alternatively separate affinity and the k-fold endpoint interpolation prove the same multilinear formula. Uniqueness is asserted on physically realizable mean vectors (or with this explicitly stated continuous extension), not on arbitrary discontinuous functions off that domain.

For every controller query i,

E_epsilon Inf_i(g_epsilon)=Inf_i(F),
F(z,x)=u_{kappa(z)}(x).                             (2)

Proof: on an actual coupled controller edge with the same state both sides, both quantities are zero. On an edge changing states j,l, the probability the independent actual outputs differ is (1-m_j*m_l)/2, exactly the product-labeling probability epsilon_j!=epsilon_l. Average each original edge once. Combining the supplied seed inequalities therefore proves

E_epsilon D_i(g_epsilon)<=C Inf_i(F)+P-E P_child.   (3)

This pays ONLY the expected seed decrement, not the full F decrement. The difference is the explicit unproved controller correction below. Root certificates r_epsilon<=K I(g_epsilon) imply P<=K I_ctrl(F) by the SAME edge identity; they are additional hypotheses, not inferred from the label map. Binary labels recover the previously reviewed delta*r_h exactly: equal output labelings are constant, opposite labelings are sign copies of h.

This is an explicit cut form of the earlier actual-boundary harmonic graft. Its new three-label coefficients and edge ownership are given next; the harmonic-boundary idea itself is credited to A064.

## 2. Three states: three exact coefficients, not one selected binary seed

For k=3 let h_j=1-2C_j and use r_j=Q_C(h_j,T). Each nonconstant sign labeling is, up to output sign, exactly one h_j. The two constant labelings have reserve0. Output sign invariance then collapses (1) to

P=w_1 r_1+w_2 r_2+w_3 r_3,
w_j=[1+m_l*m_s-m_j*(m_l+m_s)]/4, {j,l,s}={1,2,3}. (4)

w_j is the probability that epsilon_j is the odd sign and the other two signs agree. Hence w_j>=0, their sum is at most1, and every w_j is separately affine and harmonic through either core's physical data query. For a physical edge changing states j,l,

w_j+w_l=(1-m_j*m_l)/2.                            (5)

Thus summing singleton-cut influences weighted by w_j charges that edge exactly once at its actual Boolean pivotal probability. Balanced cores give w_j=1/4 for all j, not a renewed quarter budget per physical edge. Formula(5) is the correct three-state replacement for the binary mismatch delta. Disjoint data is essential; shared core outputs require their actual joint labeling law instead of pi_m.

At any controller node define the signed residual

E_i=D_i(F)-sum_j w_j D_i(h_j)-kappa_i,
kappa_i=R-E R_child,
R=sum_j phi(q_j)(1-m_j^2), q_j=E C_j.              (6)

The rarity release kappa_i is nonnegative. Equations(3),(6) give the exact compatible controller-payment interface: if E_i<=K Inf_i(F), then P+R is a nonnegative controller potential at price C+K. During DATA queries P is harmonic, so the scoped reviewed A064 local data lift attaches without a reset. No universal K is proved here. R is the existing variance-rarity account; the source A028/A029 boundary-product bank is another object and is not added for free.

## 3. A raw Boolean witness showing the extra cut debt

On two control bits take the state table (1,1,2,3), in least-significant-coordinate order. Use three independent dictator data cores. Use controller order coordinate1 then coordinate0; C=1. The singleton cut h_1 is a dictator and has Q_1=0. Each h_2,h_3 is a two-bit point defect: H=2, first query influence1/2, dictator children H=0 and Q_1=0. Therefore Q_1(h_2)=Q_1(h_3)=3/2, giving P=3/4. Keeping only the selected first cut's reserve would give zero and lose an actual complete-data frontier debit.

The root Fourier entropy of F is3. Its first actual control influence is1/2, its children have entropies0 and2, and the live binary-selector child has Q_1=3/2. Hence its actual controls-first reserve is

Q_1(F)=[3-(0+2)/2-1/2+(0+3/2)/2]_+=9/4.

The root rarity bank is R=H(1/2,1/4,1/4)=3/2; the first-query release is1. The expected seed decrement is1, so (6)'s residual is0 at that query. P+R=9/4 numerically matches the actual root reserve, whereas replacing P by the zero dictator-cut reserve leaves only3/2, short by3/4. This root equality is NOT a local potential proof: at the live binary-selector child the cut seeds are dictators with reserve and entropy0, P=0,R=1, while the actual child Q_1=3/2. Its final controller query has D_F=2, expected seed decrement0, rarity release1, and influence1/2. Thus E_i=1 and any universal correction price in(6) must have K>=2. The terminal data dictators have H0, influence1, and zero reserve; their influence remains in the full physical ledger. Root I_ctrl=3/4, data influence1, H/I=12/7<2. This is not an FEI counterexample or a claim that every possible single-cut upper bound fails. It refutes dropping the two other actual cut reserves in this stated interface and refutes a zero-price signed-correction extension.

## 4. Exact finite correction census and honest boundary

The frozen census exhausts all81 label maps on two controls and, up to independent input sign translation, all27 mean patterns of three one-bit cores (each +constant,-constant,dictator). It reconstructs (1) both by all8 sign labelings and by(4), tests actual coupled-edge ownership, every DATA harmonic identity, and every reached controller face. The exact maximum positive correction ratio E_i/Inf_i(F) is3, attained at labels(1,1,2,2), means(1,0,1), query coordinate1. That endpoint is an effective binary selector between a constant and a dictator: D_F=2, expected seed decrement0, rarity release1/2 and actual influence1/2. Its ratio3 is exact. The all-domain upper bound is an exhaustive exact certificate, not a floating search. Constant/dummy controller restrictions remain within this fixed hereditary family.

This certificate also covers arbitrarily large disjoint parity cores under every partial DATA exposure, with no new enumeration. A remaining nonconstant parity has mean0, variance1, entropy0 and one occupied nonempty data support; replacing that support by a fresh singleton preserves every controller entropy decrement, seed coefficient and queried control influence. A fully revealed parity is one of the two constant endpoint cases. Distinct nonconstant core supports remain disjoint. Arbitrary controller restrictions of an at-most-two-control map are included as dummy/constant maps in the same census. Thus E_i<=3 Inf_i(F) holds for this declared all-dimension parity-core family on every controller history. Coupling P+R to A064's reviewed local data lemma with zero parity-core reserves gives a full interleaved potential at alpha=max(11/2,C+3), keeping actual terminals. The new K=3 control correction is sharp in the full declared family; it is not asserted sharp after excluding degenerate output endpoints or requiring all three cores nonconstant. Neither finite result nor parity support transport pays arbitrary non-flat cores or arbitrary-dimensional controllers.

First unsupported universal line: E_i in(6) is bounded by a fixed K times actual query influence, or by one genuinely unused signed child surplus, on arbitrary-dimensional non-point three-state controllers after nonconstant core data exposure. The three prescribed Boolean-cut reserves and the actual entropy of all remaining core/controller leaves must remain in that proof. Many-label boundary harmonicity alone does not pay this coherent signed correction. A064's finite paid-reference conversion and A028/A029's conserved product banks cannot be substituted for it without an additional compatibility theorem.
