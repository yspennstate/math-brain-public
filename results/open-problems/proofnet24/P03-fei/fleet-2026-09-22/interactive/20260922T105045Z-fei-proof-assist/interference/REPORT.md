# Physical restriction entropy and the phase-potential refund

## Status and scope

This note proves a source-level quantitative link between the physical Fourier-entropy restriction argument and the phase correction used in the current FEI critical-core programme. It applies to every finite uniform-cube Boolean function and every finite adaptive tree of genuine coordinate restrictions. The full Fourier entropy–influence conjecture remains open.

The restriction/tree framework is prior work: González, MacManus and Pereyra, *Further evidence for the Fourier entropy–influence conjecture*, arXiv:2606.00246, especially Ansatz 1.1–1.2 and Section 4/Appendix B, https://arxiv.org/pdf/2606.00246 . The present task received the relevant primary-source statements through the coordinating researcher; direct web retrieval in this runtime was unavailable. No priority claim is made for the restriction identity, the stopping-tree principle, or the phase function. All inequalities needed below are proved here without relying on an unverified reference-family representation.

An internal source motivating the accounting question is fleet01/B15's restriction I-projection report, repository `yspennstate/math-open-problems`, commit `b293d016f9bd94819fb11385986608b8acc0b83d`, path `proofnet24/P03-fei/fleet-2026-09-22/fleet01/B15/b15-20260922T103236Z-restriction-iprojection-chain/REPORT.md`, Sections 2 and 7–8. Its proposed KL reference formulas and any later errata are not premises of this note. We use only actual Fourier coefficients of genuine Boolean restrictions and rederive their entropy relation directly.

The target remains one finite universal constant C such that H(f) <= C I(f) for every f:{-1,+1}^n->{-1,+1}. Entropies and logarithms are in bits unless written ln.

## 1. Definitions

For a Boolean function g on a set of remaining coordinates, write

    H(g) = sum_S ghat(S)^2 log2(1/ghat(S)^2),
    I_i(g) = sum_{S containing i} ghat(S)^2,
    I(g) = sum_i I_i(g).

Set h(t)=-t log2 t-(1-t)log2(1-t), with zero terms interpreted continuously, and define

    j(t) = 1-h(1/2+sqrt(t(1-t))),              0 <= t <= 1,
    P(g) = sum_i j(I_i(g)),
    J(g) = sum_i min(I_i(g),1-I_i(g)),
    F(g) = H(g)-P(g).

P is the phase correction already used in the current critical-core programme. Both P and J are unchanged by multiplication of g by any character. Moreover

    0 <= P(g) <= (2/ln 2) J(g) <= (2/ln 2) I(g).       (1)

The first upper bound will follow from the scalar lemma below; it is not assumed.

At an internal tree node, choose an actual remaining coordinate r, possibly as a function of all previously revealed bits. Let g0,g1 be its two restrictions. On the other coordinates, put

    u_S = g0hat(S),              v_S = g1hat(S),
    E_S = (u_S^2+v_S^2)/2,
    q_S = (u_S-v_S)^2/[2(u_S^2+v_S^2)]     when E_S>0,
    d = I_r(g) = Pr(g0 != g1) = sum_S E_S q_S.

Zero-mass packets are omitted. E is a probability law. Define the actual child spectral Jensen–Shannon information and the parent packet conditional entropy by

    Q(g,r) = H(E) - [H(g0)+H(g1)]/2,
    L(g,r) = sum_S E_S h(q_S).

Here Q is an information quantity of actual child spectra, not an I-projection KL. The sign of u_S v_S is retained in q_S.

## 2. Exact scalar entropy decomposition

### Lemma 1

For every genuine uniform physical restriction,

    H(g) - [H(g0)+H(g1)]/2 = Q(g,r)+L(g,r),            (2)
    Q(g,r) = sum_S E_S j(q_S).                        (3)

In particular Q and L are nonnegative.

**Proof.** The two parent Fourier coefficients in packet S are (u_S+v_S)/2 and (u_S-v_S)/2. Their squared masses sum to E_S, and their second mass divided by E_S is q_S. The entropy chain rule therefore gives H(g)=H(E)+sum E_S h(q_S). Subtracting the average child entropy proves (2).

For a nonzero packet let a=u_S^2/(u_S^2+v_S^2). The contribution to Q is E_S[1-h(a)]. Directly,

    q_S(1-q_S) = (u_S^2-v_S^2)^2/[4(u_S^2+v_S^2)^2].

Consequently 1/2+sqrt(q_S(1-q_S)) equals either a or 1-a. Their binary entropies agree, giving 1-h(a)=j(q_S) and proving (3). The identity retains even the packet S=empty; no special reference-law convention is needed. QED.

## 3. Uniform strong concavity of the phase function

### Lemma 2

The function j is continuous and concave on [0,1], symmetric about 1/2, and is uniformly strongly concave with modulus

    m = 4/(3 ln 2).

Thus for every finitely supported random variable Z in [0,1],

    j(E Z) - E j(Z) >= [2/(3 ln 2)] Var(Z).           (4)

Also j(t)<= (2/ln 2) min(t,1-t).

**Proof.** Put z=2sqrt(t(1-t)). For t in (0,1) away from 1/2, direct differentiation yields

    j''(t) = -4[atanh(z)-z]/[(ln 2)z^3]
           = -(4/ln 2) sum_{k>=1} z^(2k-2)/(2k+1)
           <= -4/(3 ln 2).                          (5)

At t=0 or 1, the second derivative has the finite one-sided limit -4/(3 ln 2). At t=1/2 it tends to minus infinity; j itself and its first derivative extend continuously there, with j'(1/2)=0. Therefore j(t)+(m/2)t^2 is concave on the whole closed interval, by its second derivative on either side and the matching first derivatives at 1/2. Jensen's inequality for this function gives (4).

Finally j(0)=0, j'(0+)=2/ln 2, and concavity bounds j by its tangent at zero. Symmetry gives the corresponding bound from one. Summing establishes (1). QED.

### Corollary 3: a quantitative packet refund

Let

    V_packet(g,r) = sum_S E_S (q_S-d)^2.

Then

    j(d)-Q(g,r) >= [2/(3 ln 2)] V_packet(g,r).        (6)

This is an exact improvement over simply pricing Q by (2/ln 2)d: it charges variation of the signed parent packet posterior to a nonnegative refund.

There is also a sign-insensitive intermediate refinement. Put

    delta_spec = [1-sum_S |u_S v_S|]/2
               = sum_S E_S min(q_S,1-q_S).

Since j is symmetric and increasing on [0,1/2],

    Q(g,r) <= j(delta_spec) <= j(min(d,1-d)) = j(d).   (7)

The first inequality can itself be strengthened by the variance of min(q_S,1-q_S). No replacement of actual signs by freely chosen signs has occurred: delta_spec and the refund are calculated from the actual source.

## 4. The local phase-potential refund

For each unqueried coordinate i!=r write

    a_i=I_i(g0),             b_i=I_i(g1).

Physical restriction gives the exact marginal identity I_i(g)=(a_i+b_i)/2. Define

    B(g,r) = P(g)-[P(g0)+P(g1)]/2-Q(g,r).             (8)

### Theorem 4

B(g,r) is nonnegative, and the following explicit bound holds uniformly in the dimension:

    B(g,r) >= [2/(3 ln 2)] V_packet(g,r)
              +[1/(6 ln 2)] sum_{i!=r} (a_i-b_i)^2. (9)

Moreover the exact residual recursion is

    F(g)-[F(g0)+F(g1)]/2 = L(g,r)-B(g,r).             (10)

**Proof.** Isolate the queried coordinate's phase contribution and use the physical marginal identity:

    B(g,r) = j(d)-Q(g,r)
             +sum_{i!=r} {j((a_i+b_i)/2)
                           -[j(a_i)+j(b_i)]/2}.

The first term is bounded by (6). For each remaining coordinate, apply (4) to the equally weighted two-point law {a_i,b_i}. Its variance is (a_i-b_i)^2/4, yielding the coefficient 1/(6 ln 2). This proves (9). Subtract the phase increment in (8) from the exact entropy increment (2) to obtain (10). QED.

The second refund is information about actual variation of physical influences across restrictions. It is not a free choice of an occurrence law and does not require an I-projection parameterization.

## 5. Any finite adaptive physical tree

Let T be any finite tree which queries only previously unqueried physical coordinates on each path. The next coordinate may depend on the previously revealed values. Leaves may be arbitrary stopping functions, not necessarily constants. Let pi_v be the genuine uniform probability of reaching node v. Let G_leaf be the remaining Boolean function at a random leaf. Define sums over internal nodes:

    Q_T=sum_v pi_v Q(g_v,r_v),
    L_T=sum_v pi_v L(g_v,r_v),
    B_T=sum_v pi_v B(g_v,r_v),
    T_fold=sum_v pi_v min(d_v,1-d_v),
    V_T=sum_v pi_v V_packet(g_v,r_v),
    M_T=sum_v pi_v sum_{i!=r_v}(I_i(g_v0)-I_i(g_v1))^2.

### Theorem 5: cumulative accounting without repeated expenditure

Every such tree satisfies

    H(f) = E H(G_leaf) + Q_T + L_T,                  (11)
    P(f) = E P(G_leaf) + Q_T + B_T,                  (12)
    F(f) = E F(G_leaf) + L_T - B_T,                  (13)
    I(f) = E I(G_leaf) + sum_v pi_v d_v,             (14)
    T_fold <= J(f)-E J(G_leaf),                     (15)
    B_T >= [2/(3 ln 2)] V_T + [1/(6 ln 2)] M_T.      (16)

In particular,

    Q_T <= P(f)-E P(G_leaf)
        <= P(f)
        <= (2/ln 2) J(f),                            (17)

and separately

    Q_T <= (2/ln 2) T_fold.                         (18)

**Proof.** Multiply the local identities (2), (8), (10), and I(g)=d+[I(g0)+I(g1)]/2 by the probability of reaching the node, then sum. Every nonroot internal-node term cancels exactly against its contribution as a child of its parent. The leaf terms remain. This proves (11)–(14); the cancellation does not depend on a fixed coordinate order.

For (15), the function t -> min(t,1-t) is concave. Hence its sum over remaining influences obeys

    J(g)-[J(g0)+J(g1)]/2 >= min(d,1-d).

The same tree telescoping proves (15). This also supplies a direct elementary proof of the optional-stopping interpretation: the pivotal indicator of coordinate i is independent of its own queried value, and its conditional mean before that query is the corresponding restricted influence. No hidden averaging over an already queried i is used.

Sum (9) for (16). Equations (12), (1), and nonnegativity yield (17); the local Q<=j(d)<=(2/ln 2)min(d,1-d) yields (18). QED.

When all leaves are constants, their H,P,I,J,F are zero. In that case the complete tree carries all spectral entropy, all influence, and all phase refund exactly, with

    H(f)=L_T+Q_T,        P(f)=Q_T+B_T,
    F(f)=L_T-B_T,        sum pi_v d_v=I(f).           (19)

Thus the entire cumulative child-mixture term is already paid by the existing phase correction. It need not be bounded again at each depth using a fresh copy of the root influence.

## 6. An exact three-part variance conservation law

There is an independent, sharper accounting identity for the two new variance statistics. Define

    W(g)=sum_i I_i(g)(1-I_i(g)),
    A_T=sum_v pi_v sum_S E_{v,S}q_{v,S}(1-q_{v,S}).

### Theorem 6

For every finite adaptive physical stopping tree,

    W(f)-E W(G_leaf) = A_T+V_T+M_T/4.                (20)

Every term on the right is nonnegative. Consequently

    A_T+V_T+M_T/4 <= W(f) <= J(f),
    V_T <= J(f),                  M_T <= 4J(f).      (21)

**Proof.** At a query of r, I_i(g)=(a_i+b_i)/2 for i!=r. For w(t)=t(1-t), the exact quadratic Jensen gap is

    w((a_i+b_i)/2)-[w(a_i)+w(b_i)]/2=(a_i-b_i)^2/4.

It follows that W(g)-average W(children)=d(1-d)+sum(a_i-b_i)^2/4. The ordinary law of total variance for the Bernoulli packet label gives

    d(1-d)=sum_S E_S q_S(1-q_S)+Var_E(q_S).

Combining these identities and telescoping proves (20). Finally t(1-t)<=min(t,1-t) pointwise, proving (21). QED.

This gives a dimension-independent, nonreused replacement budget for these *specific adaptive-tree* variance quantities. It is not a bound on arbitrary raw mixed curvature or on a sum over every physical pair at the root. The stronger constant M_T<=4J(f), for example, uses the tree probabilities and genuine restriction filtration essentially.

The refund in (16) can be written particularly simply as

    B_T >= [2/(3 ln 2)](V_T+M_T/4).

Together with (20), this identifies which part of the root's physical variance is refunded and which part remains as packet-label uncertainty. The remaining packet entropy uses h(q), rather than q(1-q); controlling that logarithmic gap is still a substantive requirement.

## 7. A concrete, sufficient branch-closing criterion

The new quantitative refund gives a checkable sufficient condition, not an assertion that every Boolean function satisfies it. Suppose a proposed actual stopping rule has leaf bound E F(G_leaf)<=K E I(G_leaf) and establishes

    L_T <= K sum_v pi_v d_v
           +[2/(3 ln 2)]V_T+[1/(6 ln 2)]M_T.         (22)

Then (13), (14), and (16) give F(f)<=K I(f), and (1) gives

    H(f) <= (K+2/ln 2) I(f).                        (23)

This does not follow from the existence of a tree. What has been paid unconditionally is Q_T; what remains is the real packet conditional entropy L_T after the demonstrated posterior and influence-variation refunds. The target in (22) contains specific source observables and a fully proved refund. It is a concrete sufficient condition, not a claim that the remaining universal problem is easier than FEI.

## 8. Limitation and exact next step

The scalar function h(q) has h(q)/q tending to infinity as q tends to zero. Therefore no universal pointwise O(d) bound for L follows from its definition. The challenge is to choose a source-realizable tree whose packet entropy is paid by its accumulated refunds and physical influence. The present theorem neither discards the rare-event logarithm nor infers that the two quadratic refunds are automatically sufficient. Indeed any proposed universal sufficiency of those refunds needs a separate test against sparse suspensions and other current obstructions.

The first new quantitative target is therefore: use actual Booleanity and adaptive physical selection to prove (22) on a nontrivial critical-core branch, or construct an actual Boolean family showing that these particular variance refunds miss a necessary logarithmic scale. Either result concerns a precise source-dependent statistic, not an arbitrary guessed positive covariance.

## 9. Verification

The accompanying checker computes exact integer Walsh transforms of actual truth tables, then evaluates entropies numerically. It checks the exact entropy identity, exact packet formula, the explicit strong-concavity lower refund, and all complete-tree balances. Floating evaluation is a sanity check only; the arbitrary-dimension statements are proved analytically above. The checker also exercises constants, characters, one-point defects, recursive majority and general Boolean samples. Its output records the actual number of cases and maximum numerical discrepancy.

Executed result: all 276 Boolean truth tables in dimensions 1–3, 672 seeded Boolean samples in dimensions 4–6, and additional character, one-point-defect and nine-input recursive-majority examples passed. There were 16,383 local source-coordinate checks and 1,231 complete-tree checks. The largest floating identity discrepancy was 1.3322676295501878e-15. `CHECKER_OUTPUT.json` preserves the output. Run with `python checker.py`; the seed is fixed in the source.

No native memory, a full FEI proof, an independent literature novelty check, or a formal proof-assistant verification is claimed.
