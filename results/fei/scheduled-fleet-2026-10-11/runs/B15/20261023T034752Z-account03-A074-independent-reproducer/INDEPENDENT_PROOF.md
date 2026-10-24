# Independent reconstruction of the finite stopping-credit theorem

Let a finite query DAG have real slack S(v). Every available binary query has both equiprobable children and costs e(v,i)=mean S(child)-S(v). Stopping is always allowed. A state carries nonnegative credit a and nonnegative total booked debit D=S(v)+a. Individual debit labels may be signed. Credit may be redistributed to the outcomes with conserved conditional mean; no new donor flow or outside-account change is allowed. The required credit is

R(v)=max(0,-S(v), max_i mean R(child_i)).

The maximum over no queries is omitted. This is a finite backwards recurrence, independent of Boolean structure.

Necessity: immediate stopping requires a>=max(0,-S(v)). For any available query, each child must receive sufficient credit to support every subsequent allowed policy. By induction its credit is at least R(child). Conserving the mean requires a>=mean R(child). This applies to each query and proves a>=R(v).

Sufficiency: assume a>=R(v). For a chosen query put delta=a-mean R(child)>=0 and assign a_child=R(child)+delta. These credits are nonnegative, have mean a, and give D_child=S(child)+a_child>=0. Their mean is S(v)+a+e=D+e=:T>=0. Stopping is legal since D>=0. The same induction supports every subsequent adaptive query and stop decision. Thus the recurrence is both necessary and sufficient; the argument also gives an attaining optimal stopping policy for terminal reward (-S)_+.

Credit owners: if a>0, use kernel a_child/a for each old nonnegative credit label. Its mean is one, so each owner's conditional expected label is conserved. If a=0, both child credits vanish and every nonnegative old credit label is zero; the kernel 1 suffices.

Debit labels: append the signed new query label e to the old labels, whose sum is D. If T>0, transport each label by kernel D_child/T. This kernel is nonnegative with mean one and child label sums are D_child. If T=0, nonnegative D_child with mean zero implies both are zero. Use kernel 1: signed labels sum to D+e=0 on both outcomes and preserve every old label's mean. Individual nonzero labels can cancel; they must not be dropped. No division by zero occurs. Iterating conserves all original labels with true conditional reaches and changes no outside donor or stopped sibling.

# Independent Boolean derivation

Encode a block's negative output by x_j in {0,1}. Compute the literal table's binary multilinear coefficients by inclusion-exclusion: d_U=sum_{V subset U}(-1)^(|U|-|V|)J(1_V). Under independent biases p_j, its centered binary coefficients are b_T=sum_{U superset T}d_U product_{j in U\T}p_j. The occupied-block spectrum has mass m_T=b_T^2 product_{j in T}p_j(1-p_j). Direct integer character sums compute each inner block's Fourier coefficients; direct pivotal-edge counts compute q_j. Orthogonality verifies sum m_T=1 and sum_{T containing j}m_T=4p_j(1-p_j)q_j.

Conditioned on occupied blocks, the nonempty inner Fourier sets are independent, with normalized law w_A^2/(N^2 v_j), v_j=4p_j(1-p_j). Hence full entropy is H(m)+sum_j q_j v_j H(inner_nonempty/v_j), and full influence is sum_j q_j I(inner_j). This independently reconstructs S=4I-H by conditional entropy, instead of importing the peer's centered sign-moment transform or correction formula. The identities hold with zero-variance blocks omitted. Direct character/edge checks establish the exact finite Boolean inputs, rather than a relaxation over arbitrary spectra.

For F_plus=J(-1,+1,g,g,g,g), g in six bits negative exactly on {0,1,2}, J(x)=+1 exactly when x xor 1 belongs to {0,1,2,4,8,16,32,6,17,40}, retain all four original remaining block labels and every ternary partial-assignment tag. Each chosen block has 3^6=729 labelled states and 6*3^5=1458 labelled query rows. Dummy queries are retained: both actual restrictions are checked, not deleted from the DAG. The calculation uses exact rational log-linear expressions for equality and proved outward logarithm intervals for strict comparisons. Every candidate is compared with its Bellman winner, and every available query's credits/debits are checked nonnegative with conserved means. The exact root identity R=-S is tested as equality of rational log-linear profiles, not overlap of intervals. It is in (2857328/10^8,2857329/10^8). Therefore any actual leaf carrying D>=0 and a=D-S already has a>=R, regardless of its old signed debit labels. No donor regeneration is claimed.

# Universal boundary and first unpaid line

With all physical queries allowed and K,L>=0, a dimension-independent R_K(f)<=L I(f) is equivalent to FEI with constant K+L. One direction stops immediately: H-KI<=R_K. Conversely FEI(K+L) implies (-S_K(g))_+<=L I(g) at every restricted terminal, and expected terminal influence is at most initial influence by I(v)=Inf_i(v)+mean I(child). Apply the optimal-stopping characterization above. This equivalence supplies no bound on R_K.

The finite calculation permits queries only in one chosen remaining core. It does not prove that a later second core fits the actual credit left on each terminal, and does not allow interleaved queries between cores. The first unsupported line is that such actual inherited credit dominates the next core's stopping hull without drawing again on a spent donor. Full FEI remains open.
