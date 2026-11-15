# Erasure entropy and witnesses

Each numbered claim below is labelled PROVED, CHECKED with its finite scope, or OPEN. A result marked PROVED (inherited) invokes the named earlier theorem; it is not a new proof of that theorem. Entropies use base-two logarithms. Put Phi(a,b)=(a+b)h(b/(a+b)), with Phi(0,0)=0. Its arguments are masses, not Fourier coefficients.

## 1. Sufficient statistics — PROVED

Write a_T=mu(T), b_T=mu(T+i). A statistic s_i is sufficient for this erasure problem exactly when b_T/(a_T+b_T) is constant on each positive-mass cell. Then

    H(1[i in U] | s_i(U-i)) = sum_T Phi(a_T,b_T) = E_i.

This follows by collecting cells and the equality case of entropy concavity. Without sufficiency the same concavity gives the witness upper bound. All witnesses in this report are functions of U-i alone; none is allowed to inspect whether i is present.

PROVED: H^-<=H by the chain rule: in any coordinate order, conditioning on all other coordinates gives no more entropy than conditioning on the preceding coordinates. Sum these inequalities. The upper bounds on H inherited below therefore also bound H^-.

## 2. Symmetric functions — PROVED, with an inherited constant

Let c_k be the Fourier coefficient on every set of size k, and W_k=C(n,k)c_k^2. For a fixed i and |T|=k the two edge masses are c_k^2 and c_(k+1)^2. Thus s_i(T)=|T| is sufficient, and

    H^- = n sum_(k=0)^(n-1) C(n-1,k) Phi(c_k^2,c_(k+1)^2).

At a nonzero pair the down-ratio at level k is

    c_(k-1)^2/c_k^2 = (W_(k-1)/W_k)(n-k+1)/k.

Zero coefficients must be treated by the continuous mass formula, not by division.

If f(-x)=f(x), its Fourier support has even cardinality; if f(-x)=-f(x), its support has odd cardinality. In either case parity of |T| determines whether i is present, so every E_i=0. Here “even/odd” means reversal of all signs, not monotonicity or parity of the truth-table integer.

PROVED (inherited): the later symmetric theorem H<=4.650431 I gives

    H^- <= 4.650431 I,

with the sufficient count witness. The supplied ../../inputs/fei_sym_v4/paper/main.tex is older and states 4.657435. The actual source for 4.650431 is ../FSYM47/repository/paper/main.tex with ../../inputs/fsym44_cert/ledger_certificate.json. inherited_audit.json independently reconstructs its exact seed and rational ledger; the analytic envelopes and large block census are inherited. FEIB02's report uses the later coefficient too. FEIB02's new B<=3.459354 I and Gamma<=8I/5 do not give a smaller erasure constant by a direct transfer. No improvement to 4.650431 is proved here. The symmetric erasure census in symmetric.json is a separate CHECKED result through n=20; it cannot certify an all-dimensional constant.

OPEN: the optimal symmetric erasure constant and a proof below the inherited coefficient. The data suggest considerably more room than the H theorem, but do not prove a uniform improvement. The tempting bound sum_T |fhat(T)fhat(T+i)|<=2 Inf_i is false even in the symmetric class: symmetric.json records larger ratios. Thus Phi<=2 sqrt(ab) does not by itself prove a coefficient 4 by that route.

## 3. Exact biased composition — PROVED

Let F=g(g_1,...,g_m), on disjoint input blocks B_j. Set b_j=E g_j, v_j=1-b_j^2, and remove constant blocks by fixing the corresponding input of g. Let alpha_A be the Fourier coefficients of g in the product law with independent means b_j, using the normalized basis (y_j-b_j)/sqrt(v_j). Put

    lambda(A)=alpha_A^2,
    nu_j(R)=g_jhat(R)^2/v_j for nonempty R,
    beta_j=sum_(A contains j) lambda(A).

For S_j=S intersect B_j, A={j:S_j nonempty}, substitution of the centered child expansions gives exactly

    Fhat(S) = alpha_A prod_(j in A) g_jhat(S_j)/sqrt(v_j),
    mu_F(S) = lambda(A) prod_(j in A) nu_j(S_j).             (3.1)

In particular lambda(empty)=(E F)^2. It is generally wrong to insert the uniform spectrum of the outer gate when its inputs have nonzero means. Equation (3.1) may also be expressed using the uniform coefficients of g: alpha_A=(prod_(j in A)sqrt(v_j)) sum_(D contains A) ghat(D)prod_(l in D-A)b_l.

Fix i in B_j, let q_i=g_jhat({i})^2/v_j, and let mu_j denote the full spectrum of g_j, including its empty atom. Then

    E_i(F) = (beta_j/v_j) [ E_i(g_j)-Phi(b_j^2,mu_j({i})) ]
             + sum_(A subset [m]-j) Phi(lambda(A), q_i lambda(A+j)).   (3.2)

Also

    Inf_i(F)=(beta_j/v_j) Inf_i(g_j).                         (3.3)

Proof of (3.2): split edges according to R=(T intersect B_j). If R is nonempty, the block stays active at both ends; its outside spectral factors agree and sum to beta_j, giving the first term after removing R=empty from E_i(g_j). If R is empty, the lower end has j inactive while the upper end activates {i}. For each outside occupied-block set A the common product of other nu's sums to one, giving the displayed second term. Equation (3.3) follows by summing the upper masses. Homogeneity of Phi handles all positive common factors; zeros use continuity.

CHECKED: composition.json compares (3.1)–(3.3) with direct tables of independently generated, biased children and outer gates, including constant outer gates. The checks do not assume balanced children. The empty-block correction is essential; dropping it produces an incorrect recursion. For XOR of disjoint children the full spectrum is a product and E_i(F)=E_i(g_j), even when children are biased. No similarly simple unconditional additive law holds for an arbitrary gate.

## 4. Read-once path witness — PROVED

At every gate on the path from a literal i to the root, retain, for EACH sibling child, the bit saying whether T meets that child's variable block. Let s_i(T) be the tuple of these bits along the path. It is a statistic of T=U-i. The sibling blocks along a path partition all leaves other than i.

This statistic is sufficient for E_i, for arbitrary gates and arbitrary intermediate biases. To prove this, apply (3.1) at a gate. If the path child has a nonempty spectral set at both endpoints, the outer occupied-child pattern is the same, so the outer factor cancels in the ratio. If its lower spectral set is empty, the two patterns differ by activation of that child, and their ratio depends only on the occupied siblings and the child's singleton coefficient. Whether the lower path-child set is empty is itself determined by the lower sibling bits. Continue toward the root. Detailed nonempty sibling coefficients multiply both endpoints by the same factor and cancel. Cells of zero total mass can be ignored. Constant child outputs are removed before the recursion. This proves constancy of the posterior on every cell.

At an AND/OR gate the bit for a sibling is exactly the FLOW 10(d) block witness with N equal to that sibling's variable set. With more than one sibling, retain the separate bits; their OR is the coarser single “meets the union of siblings” witness. Repeated tuples, rather than just one bit at one gate, avoid losing the nested activation information. The same witness works for XOR and MAJ gates without any new definition. CHECKED: composition.json tests the tuple's sufficiency on random read-once formulas with arbitrary gates.

PROVED (inherited constants): for read-once AND/OR/XOR/NOT formulas, CKLS Theorem 5.11 gives H<=10I, hence the exact path witness has total cost H^-<=10I, independently of depth and fan-in. The author is Kulkarni in this paper; Kundu is an author of the different random-LTF paper named in the brief.

For a read-once decision tree in the GLOBAL sense (each variable labels at most one internal node in the entire tree), write each internal node as a mux gate on its selector and its two disjoint subtrees. The same path witness is sufficient. OWZ's read-once decision-tree theorem gives H^-<=4.88I. “No variable repeated on one root-to-leaf path” is the usual unrestricted decision-tree convention and is not the read-once hypothesis of this theorem.

For MAJ_3 together with binary AND/OR/XOR, the bounded-arity O'Donnell–Tan theorem already supplies a depth-independent constant. An explicit conservative coefficient from their Lemma 4.1 is 2^(3k+1)/ln 2 for all gates of arity at most k: sum the lemma over at most 2^k nonempty sets and coordinates, then use sum_j Var(D_j)=sum_(|A|>=2)|A|lambda(A)<=2(I-Var). Thus k=3 allows 1024/ln 2. This does not handle arbitrary fan-in MAJ by replacing k with 3; that is a different class.

PROVED (inherited, recent preprint): the author's October 2026 threshold paper, Theorem D/Corollary 7.3, gives H<=744I for arbitrary-fan-in symmetric-threshold/parity read-once formulas under uniform original inputs. AND, OR and MAJ are symmetric thresholds. Therefore our path witness yields H^-<=744I for the full gate set and arbitrary depth and fan-in in the brief. Its stated bit constant is 80+460/ln 2<744. This conclusion relies on that cited product-measure gate theorem; the gate theorem is not independently re-proved here. See LITERATURE.md for the exact source and scope. Merely knowing uniform-input FEI for each gate is insufficient for biased composition.

OPEN: a shorter direct witness proof, and an improved explicit erasure constant for mixed arbitrary-fan-in formulas. The sufficient statistic and exact composition law are proved here, while the depth-independent cost bound above is transferred from established/cited H results.

## 5. Degree and decision-tree depth — PROVED, constant witness

A nonzero multilinear polynomial of degree at most r is nonzero on at least a 2^-r fraction of the cube. Induct on the number of variables: if it is independent of the last variable, remove it; otherwise its derivative is a nonzero polynomial of degree at most r-1. On each outside assignment where that derivative is nonzero, at least one of the two values of the polynomial is nonzero. This proves the claim.

For Boolean f of degree d>=1, D_i f has degree at most d-1 and values in {-1,0,1}. Hence every nonzero delta_i=Inf_i satisfies delta_i>=rho_d=2^(1-d). Take the CONSTANT statistic s_i(T)=0. Its cost is h(delta_i). The function h(p)/p is decreasing on (0,1], since its derivative is ln(1-p)/(p^2 ln 2). Consequently

    sum_i H(1[i in U] | s_i) = sum_i h(delta_i)
       <= C_d I,       C_d=2^(d-1) h(2^(1-d))
       <= (d-1+log_2 e) I.                                (5.1)

The final estimate uses -(1-p)ln(1-p)<=p. Degree one has rho=1 and C_1=0; degree zero is constant. Subadditivity also gives H<=sum_i h(delta_i), so (5.1) bounds H itself. This is a shorter proof and a better coefficient than the granularity-only bound [2(d-1)+log_2 e]I in FEIB12, not a claimed new best result in the literature. CHECKED: audit.json verifies both the influence lower bound and (5.1) on the entire NPN census through n=5.

A depth-d decision tree represents a polynomial of degree at most d (induct on its root expansion). Thus the same constant witness and C_d work for every such tree. If size s means NUMBER OF LEAVES, then degree<=s-1 and C_(s-1) is an explicit coefficient for s>=2. If size counts internal nodes instead, use C_s. These statements are uniform in ambient dimension, but their constants depend on d or s.

PROVED (inherited, alternative size/read bounds): WWW gives H<=9k I for a tree in which each variable occurs at most k times. Shalev's covariance bound and WWW Lemma 1.5 give H<=[2+(4+4sqrt(k))log_2 3]I. The alphabet factor and the additive empty-set charge are essential: the protocol length 4I+2Cov is in ternary characters, not bits. A binary s-leaf tree has k<=s-1, so H^-<=min(C_(s-1),2+(4+4sqrt(s-1))log_2 3)I. The identity statistic T is a witness for the transferred bound; no cheap structural witness for arbitrary repeated-variable trees is claimed. CKLS's absolute entropy bound H<=2 E[depth]<=2 log_2 s is separate and cannot simply be divided by I to obtain 2 log_2 s as an FEI coefficient when I<1.

## 6. Width-w DNF — partial PROVED; general target OPEN

PROVED: for disjoint-term DNF (tribes, with arbitrary term widths and negations) the read-once path witness and coefficient 10 apply. A monotone width-w DNF is a different, broader class. Brain recall points to a provisional local down-set paper claiming H<=(w+8.1)I there; this report does not treat that remembered claim as a verified theorem. The proof was not audited in this task.

OPEN here: an explicit C(w) for ALL overlapping width-w DNFs by the requested witness method. Width does not bound the read number, the degree, or the decision-tree depth, so none of the preceding bounds proves that statement. The singleton influence lower bound also fails badly: x_0 AND (x_1 OR ... OR x_m) is a monotone width-two DNF and a leaf variable has influence 2^-m.

The named older papers prove FEI for read-once formulas/read-bounded trees, or FMEI for restricted DNFs; they must not be cited as a full Shannon FEI theorem for arbitrary bounded-width DNF. The 2026 threshold preprint supplies read-k union/DNF bounds depending on k, not a coefficient depending on width alone when overlap is unrestricted. No new C(w) is inferred from those results. See LITERATURE.md.

## 7. LTF and monotone scope — inherited PROVED / CHECKED / OPEN

PROVED (inherited from the October 2026 preprint): for every LTF,

    H^-<=H<=[log_2(4+e)+2 log_2(e pi)] I < 8.937 I.

This is a recent cited theorem, not an implication of the older O(sqrt(n)) entropy estimate of CKLS. It does not prove that any one of the five cheap families has that coefficient. The sufficient log-likelihood statistic in section 10 does yield a witness at the inherited coefficient, but depends on the entire spectrum; it is not a structural LTF solution. The best parity/block/count statistics for LTFs are CHECKED only on the saved finite samples. For homogeneous LTFs without ties, oddness gives the much stronger exact zero erasure and a parity witness.

OPEN: a proved, uniformly bounded-cost cheap witness for arbitrary biased LTFs, and a uniform monotone bound in general. Every Boolean function is a Boolean function of its coordinate literals, but that does not make it a read-once formula over the restricted gates. Monotonicity does not force parity support or constant-sign higher derivatives. Neither the monotone samples nor the older FMEI result settles Shannon FEI or erasure FEI for all monotone functions.

## 8. Parity-only witnesses fail uniformly — PROVED

Consider AND_n, with f=+1 except at one corner (global sign does not matter). Set

    delta=2^(1-n), q=delta^2, M=2^(n-1), c=(1-delta)^2.

The empty spectral atom is c, every nonempty atom is q, and Inf_i=delta. For any NONEMPTY P subset [n]-i, exactly M/2 of the T's have each parity. The parity-zero cell contains the exceptional empty atom. Thus EVERY such P has the same cost

    delta + Phi(c+(M/2-1)q, delta/2).                       (8.1)

The empty P is the constant statistic and cannot do better, by conditioning. Divide (8.1) by delta. Since its first mass tends to one,

    best parity cost/Inf_i = n/2 + 1 + 1/(2 ln 2) + o(1).

All coordinates are equivalent. Family (i), even optimized separately for each i, has an unbounded total-cost/I ratio on these Boolean functions. A block-meets witness with N=[n]-i, or |T|, separates the exceptional empty mass and avoids this loss. This explains the large AND entries in the census. The failure occurs already on symmetric, monotone, threshold and read-once functions; no general FEI obstruction follows.

## 9. Cardinality-only witnesses also fail uniformly — PROVED

Fix w>=2, let g=AND_w and F_s be the XOR of s disjoint copies of g. The spectrum of F_s is the product of the child spectra. Write K for the size of a sample from one child's full spectrum. K has positive probabilities at 0 and 1, and support {0,...,w}. For a fixed i in the first block, X=1[i in U] has probability delta=2^(1-w), while

    |U-i| = Z_(s-1) + L,

where Z_(s-1) is a sum of independent copies of K and is independent of the first block. Conditional on X=0 or 1, L has one of two distributions on {0,...,w}.

For any fixed integer r, the total variation distance between Z_s and Z_s+r tends to zero. An elementary proof avoids a local-limit assumption: because P(K=0),P(K=1)>0, split off an epsilon-weight fair Bernoulli component from K. Conditional on the number M of such components and all residual variables, the sum contains Bin(M,1/2). Its variation distance from an r-shift is at most |r| times its maximum atom, which tends to zero as M tends to infinity in probability. Convolution contracts total variation. Thus the two conditional laws of |U-i| become indistinguishable. Their joint law with the binary X approaches the product law, and continuity of binary conditional entropy gives

    H(X | |U-i|) -> h(delta),
    total cardinality-witness cost/I -> h(delta)/delta       (s -> infinity).

The latter ratio tends to infinity as w tends to infinity. This proves that family (iv) cannot have an absolute coefficient. The order of limits is first s then w; no claim is made that a fixed small XOR power already attains the limiting value. A witness confined to i's own block handles this example. CHECKED finite convolutions and error diagnostics are saved in cardinality_dilution.json.

## 10. General likelihood witnesses — PROVED; cheap general target OPEN

For any Boolean function, s_i(T)=mu(T)/mu(T+i), with separate zero/infinite conventions, is sufficient. It encodes the posterior itself and therefore gives E_i exactly. This observation alone bounds no cost.

There is also a universal quantized version. Give all edges with zero lower mass one cell and all edges with zero upper mass another. On edges with both masses positive set

    s_i(T)=floor(log_2(mu(T)/mu(T+i))).

Then

    E_i <= H(1[i in U] | s_i(U-i)) <= E_i+Inf_i.           (10.1)

To prove it, set r=a/b and F(r)=Phi(r,1). In a cell r lies in [r_0,2r_0). Its contribution is B F(E_b r), versus sum_T b_T F(r_T). Since F is increasing and

    dF(r)/d(ln r)=r log_2(1+1/r)<=1/ln 2,

their difference is at most B[F(2r_0)-F(r_0)]<=B. Sum cells. The zero-mass cells have zero cost. For a Boolean n-variable truth table all nonzero coefficient magnitudes are integers times 2^(1-n), so this statistic uses only O(n) possible logarithmic bins. It still requires knowledge of the Fourier coefficients.

Thus a single spectrum-dependent statistic type has bounded total cost IF AND ONLY IF FEI holds, with an additive one in the erasure coefficient. It is not a proof of FEI or a finite cheap-witness theorem. This distinguishes three different meanings of “finite”: finitely many tested functions (always bounded), finitely many statistic templates with many mask choices, and a uniform mathematical bound.

CHECKED: for all NPN classes through n=5 and the saved n=6..10 draws, every family and their coordinatewise union has the finite maxima tabulated in RESULTS.md. The union chooses, separately for each coordinate, the least cost among all five families; it is not merely the minimum of five total costs.

OPEN: a uniform bound for family (iii), family (v), or their union on every Boolean function. A proof would imply general FEI by the witness principle and the supplied erasure equivalence. Family (ii) is poor on majority in the saved finite data; this report does not prove its optimized asymptotic divergence. Families (i) and (iv) are ruled out uniformly by sections 8 and 9. Path tuples show concretely why nested block information is a useful extension of one parity and one block bit.
