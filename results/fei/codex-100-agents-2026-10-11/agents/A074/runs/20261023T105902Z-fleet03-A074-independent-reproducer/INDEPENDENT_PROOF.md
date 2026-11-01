# Scope and independent reconstruction

Review target: A072-LOCAL-HULL-ADMISSION-DAMAGE-UNBOUNDED@1. The mathematical conclusions below use K=1 only for the constructed family; the small-dimension theorem uses all real K>=0. Neither conclusion contradicts a rate4 finite certificate or a suitably influence-paid universal envelope. Entropy is the full squared-Fourier Shannon entropy in bits. All physical branches and existing labels remain present.

# 1. Arrival capital as a forward path constraint

At a Boolean restriction v and current admitted mask M, put b(v)=max(0,H(v)-K I(v)). Write rho_M for the least stopping envelope when queries are limited to M. The prescribed local allocator gives the two actual credit increments

delta_b=rho_M(v_b)-mean rho_M(v_c).

Admissions enlarge M with no credit increment. For a path p ending at w, define Deltap as the sum of all its query increments. If initial credit is a0, the actual credit at w is a0+Deltap. Solvency at that arrival is equivalent to a0>=b(w)-Deltap, since this simultaneously enforces nonnegative credit and nonnegative full booked debit S(w)+credit. Stopping is allowed at every arrival. Consequently the least robust capital is the maximum of b(w)-Deltap over all actual paths, including the empty path.

Grouping paths by their first edge gives the source's exact max-child/admission recurrence. Grouping them instead by their LAST arrival gives a different algorithm: at each augmented state store the minimum accumulated increment among all incoming paths, and maximize b minus that stored offset. A strict topological order exists: rank=2*(number of fixed coordinates)+|M| increases by one for every single-coordinate admission and physical query (query removes its coordinate from M). The verifier uses this forward min-plus algorithm, not the peer's backward capital recurrence or its path-pruning code. It keeps all 4^n augmented states: each original coordinate is free-unadmitted, free-admitted, fixed0 or fixed1.

Every global-hull policy can be made available by admitting all coordinates before querying. Thus robust capital T>=rho_all. If all coordinates are already admitted initially, T=rho_all: by finite induction child requirements are rho_all(child), and subtracting the prescribed child increment leaves their common conditional mean, exactly the usual hull recurrence. This argument also proves the general claim independently of the constructed family.

# 2. Solvent label transport, including zero totals

When a>=T, each arrival has a_child>=0 and d_child=S_child+a_child>=0. The increments have mean zero, hence mean a_child=a. Each nonnegative old credit-owner label is multiplied by a_child/a if a>0. If a=0, every old nonnegative credit label is zero and both child credits are zero; kernel1 handles this case.

Let old signed debit labels sum to D=S+a, and append the signed physical query label e=mean S_child-S. Their new total Tbook=D+e equals mean d_child>=0. If Tbook>0, multiply every old/new signed label by d_child/Tbook; each label conserves its mean and their child sums equal d_child. If Tbook=0, both nonnegative child totals vanish; kernel1 preserves the possibly nonzero cancelling signed labels and sums to zero. Nothing is dropped. Admissions change no credit, label, spent outside donor or stopped sibling. This is the already reviewed finite conservation mechanism, here reapplied under the exact arrival-capital criterion.

# 3. All Boolean functions on at most three bits, every K>=0

A one-bit Boolean function has Fourier entropy zero, so S=K I>=0. At a state with at most two free bits, every nontrivial proper restriction therefore has nonnegative slack; for every mask its local stopping hull is exactly the current b. For a three-bit state, the children of its first query have at most two free bits, and both their local AND full hulls equal their b. A query thus assigns a_child=b_child+a-mean b_child. Starting with a>=rho_all(parent) ensures a>=mean b_child, so each child's actual credit covers its full hull. The same reasoning continues at smaller states. Admissions do not change credit. This proves T=rho_all from any initial mask, in particular the empty mask, for every Boolean function on at most three physical bits and every nonnegative real K. No finite grid in K proves this continuum statement; the grid is a check only.

# 4. An actual Boolean rank-one perturbation

For n=d+3, let P be the three parity coordinates and define

F_d(z)=chi_P(z)-2*1_{z=0}.

At zero the parity value is +1, so this formula is sign valued: it flips exactly that value. More generally F_{r,t} has r parity coordinates and t selectors, m=r+t. Its Fourier coefficients are 1_{A=P}-2/2^m. This follows by directly summing the single-vertex perturbation, without any computational search. The integer Walsh coefficients W_A=2^m*1_{A=P}-2 have inverse exactly the stated truth table. Parseval is the integer identity (N-2)^2+4(N-1)=N^2 for N=2^m.

Independently count physical edges. Pure parity has rN/2 crossing edges. Flipping zero removes r crossings and creates m-r crossings. Counting both endpoints in total influence gives I_{r,t}=r+2(m-2r)/N. For m=0 use I=H=0. The squared spectrum consists of one mass (1-2/N)^2 and N-1 masses 4/N^2; these are the full Fourier masses, not a relaxed distribution.

If any queried bit is 1, the point perturbation disappears and the remaining function is pure parity, with H=0 and nonnegative K=1 slack. All positive stopping reward is therefore confined to the single all-zero path. A stopping policy can choose an order along that path and stop at any remaining (r,t), reaching it with true probability 2^{-(d+3-r-t)}. Conversely every rewarding leaf is of this form, and a deterministic stopping policy has at most one such leaf. Thus

R_d=max_{0<=r<=3,0<=t<=d} 2^{-(d+3-r-t)}*(H_{r+t}-I_{r,t})_+.

This proves both directions, including attainment, for every integer d>=0. Randomizing policies cannot improve a maximum of deterministic payoffs.

# 5. All-dimensional separation of global and arrival capital

Set u=2/2^m. In natural logarithms the entropy is

H_m ln2=-2(1-u)^2 ln(1-u)-2u(2-u)ln u.

Its derivative in u is 4(1-u)ln((1-u)/u)-2. For 0<u<=1/4 this is positive: 1-u>=3/4 and ln((1-u)/u)>=ln3>1. The last strict inequality follows from the first positive atanh term plus the positive remainder. Therefore H_m decreases for m>=3. At m=3, H_3=4-(9/8)log2(3)<9/4, since 3^9>2^14. Directly I_{3,0}=9/4, I_{3,1}=11/4, I_{3,2}=47/16, and I_{3,t}>=3 for t>=3. Every F_{3,t} thus has STRICTLY positive rate1 slack.

Admit only selectors and query them with zero answers. At every such state, stopping or continuing selectors sees only positive-slack F_{3,t} or pure parity. Its current local hull is zero, so every actual credit increment is zero. On the all-zero selector branch the original credit arrives unchanged at F_{3,0}. Upon admitting the parity bits, each parity query has a two-bit point-defect child (H=2,I=1,need1) and a pure-parity child (need0). Since F_{3,0} itself has positive slack, its full hull is exactly1/2. Consequently T_d>=1/2 for every d, regardless of how small the initial global hull was.

For the opposite global bound, m>=2 and v=1-(1-2/N)^2 give 1/N<=v<=4/N. The tail is uniform, hence H_m=h2(v)+v log2(N-1). The elementary inequality -(1-v)ln(1-v)<=v yields H_m<=v[log2(1/v)+1/ln2+m]. Since ln2>1/2 and log2(1/v)<=m, this is at most8(m+1)/2^m. Entropies m=0,1 vanish. Discounting each candidate in the exact formula yields R_d<=8(d+4)/2^{d+3}->0. Retaining r=2,t=0 gives deficit1 at reach2^{-(d+1)}, proving R_d>0. Combining with T_d>=1/2 gives T_d/R_d>=2^{d-1}/(d+4)->infinity. This is an analytic all-d argument, not extrapolation from the finite checks.

For d=1, direct exact computation gives R_1=1/4,T_1=1/2. An independent analytic upper bound follows because any first physical query has full child hulls1/2 and0. The bad child's current local hull is between0 and1/2; its pure-parity sibling's is0. Starting with1/2 sends at least1/2 credit to the bad child and nonnegative credit to the good child. The at-most-three-bit theorem then pays all later admissions. The selector-first path gives the matching lower bound. Thus dimension four is the first possible failure of this equality at K>=0.

# 6. Exact finite validation and first unpaid universal line

The implementation computes Fourier coefficients by direct character sums and checks every inverse sign, Parseval and separate coordinate edge count. Shannon entropy is stored independently as 2n-(2/N^2)*sum W_A^2 log2|W_A|, canonically factored into rational coefficients of prime logarithms. Equalities are exact profile equalities. Strict orders use A074's earlier positive-series logarithm helper with a proved remainder and112-bit outward rounding. The forward capital algorithm retains all physical partial assignments and admission masks, without symmetry quotient. Finite d values were frozen before execution; there is no automatic dimension escalation.

The no-damage theorem and all-d separation are proved above. Finite checks serve as attempts to falsify them, not their substitutes. Source output comparisons are performed only after independent calculation. No peer executable is imported or rerun. Any earlier source donor ancestry is outside this review.

The first unpaid universal line is an initially influence-paid, owner-coherent full-universe envelope at an appropriate absolute rate for arbitrary Boolean functions. Here I(F_d)=3+2(d-3)/2^{d+3}->3, so a positive bounded capital requirement remains compatible with a constant times influence. The result rules out converting global hull price to admission-safe price by a universal factor for the prescribed changing-local-hull rule at K=1; it supplies no negative conclusion at K=4 and no FEI counterfamily.

# 7. New conditional corollary: the sharp one-query coherence charge

This corollary is A074's author proof, separately pending independent review; it repairs no line of the reviewed A072 theorem. Let R be the full stopping hull and rho the current admitted-set hull, and fix one available binary physical query. Write R_b and rho_b for its child hulls, g_b=R_b-rho_b>=0, and q=R_parent-mean R_b>=0. Suppose the incoming account is funded at the full parent hull R_parent and the query nevertheless uses the current local allocator. The exact additional nonnegative parent credit needed to ensure BOTH actual child credits cover their full child hulls is

charge = ( |g_0-g_1|/2 - q )_+.

Proof: before any top-up, child b's full-hull shortfall is R_b-[R_parent+rho_b-mean rho] = g_b-mean g-q. Maximizing over two equiprobable outcomes gives |g_0-g_1|/2-q. A common extra parent amount shifts both child credits by that amount; its smallest nonnegative feasible value is the positive part. This proves both necessity and sufficiency for the one query, not merely an upper bound. All hulls are real; no rationality or Boolean special form is used in the algebra. The hull hypotheses ensure nonnegative full child credit covers every later full-universe continuation. General signed-label transport from section2 then preserves the existing account when this new charge has actually been supplied.

Hence a local allocator is coherent relative to the full funded parent envelope on this query iff the difference between the children’s unadmitted gaps is at most twice q. Global root equality alone supplies no such bound. For the actual d=1 witness's selector query, R_parent=1/4, R_children=(1/2,0), rho_children=(0,0), so q=0 and charge=1/4. After that unfunded query, admitting parity and taking a zero outcome leaves credit3/4 at a two-bit point defect with slack-1: total booked debit is-1/4 at true root reach1/4. This is an actual Boolean accounting failure, not only a gap in a proof. It remains a rate1 accounting witness, not an FEI disproof.

The next useful mathematical inequality is to pay this sharp charge from the SAME actual unused owner resource at an appropriate absolute rate, or to retain an admission-independent full-universe allocator and pay its initial envelope directly. Neither payment follows from the corollary.
