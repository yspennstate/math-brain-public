# A014: a normalized whole-set reference for one-bit blocker overlap

All logs are base two. Let x be one uniform bit and let Y,Z be disjoint finite private cubes. For i=0,1, let h_i(Y),k_i(Z) be Boolean indicators with h_1<=h_0 and k_1<=k_0 pointwise. Private monotonicity is not required. Set C(x,Y,Z)=h_x(Y)k_x(Z), f=1-2C. Positive clause blockers with one shared variable satisfy this nesting after orienting x. Let a_i=E h_i, b_i=E k_i, A_i=a_i b_i, s=(A_0+A_1)/2. Omit any zero-mass branch and handle s=0 separately as a constant output.

## Physical influence: one owned account

Nestedness implies C_1<=C_0, hence I_x(f)=A_0-A_1. For a private coordinate j in Y, conditioning on x and Z gives

    I_j(f)=(b_0 I_j(1-2h_0)+b_1 I_j(1-2h_1))/2.

The analogous formula holds on Z with a_i and k_i. Thus

    I(f)=A_0-A_1 + sum_i [b_i I(1-2h_i)+a_i I(1-2k_i)]/2.       (1)

These weights are not independent payment accounts: they exactly partition the actual influence. The overlap variable is owned once.

## Exact signed row ledger

Write lambda_i=A_i/(2s). For nonzero h_i define P_hi(U)=h_ihat(U)^2/a_i, and analogously P_ki. Each is a normalized spectrum of a non-Boolean blocker; it includes its empty Fourier set. For T=(U,V), write z_i(T)=h_ihat(U)k_ihat(V). Define

    r_T=(z_0^2+z_1^2)/(2s)=sum_i lambda_i P_hi(U)P_ki(V).
    beta_T=z_1^2/(z_0^2+z_1^2),
    eta_T=(z_0-z_1)^2/[2(z_0^2+z_1^2)].

Zero rows are omitted. The actual normalized spectrum P_C(T,xi) has probabilities (z_0+z_1)^2/(4s) at xi=0 and (z_0-z_1)^2/(4s) at xi=1. In particular its row marginal is r, but its separator probability depends on the signs, not just beta. Define L=sum_T r_T h2(beta_T) and J=sum_T r_T h2(eta_T). The entropy chain rule for the branch-labelled product mixture and then for the actual separator gives

    H(P_C)=sum_i lambda_i[H(P_hi)+H(P_ki)]+h2(lambda_1)-L+J.     (2)
    sum_T r_T eta_T=(A_0-A_1)/(4s)=I_x(f)/(4s).                (3)

(3) follows from Parseval and E C_0 C_1=A_1, which is precisely where nestedness is used. This is a blocker-specific specialization of the already-known block restriction entropy law, not a claim to a new universal collision identity. Its role here is to retain the exact signed terms and once-paid activation in the whole-function reference.

## Whole-function activation and complete terminal ledger

Since C is an indicator, ||C||^2=E C=s and P_C(empty)=s. Put v=4s(1-s). Every nonempty coefficient of f has squared mass 4s P_C(A), while the empty output mass is 1-v. Therefore

    H(f)=h2(v)+4s[H(P_C)-h2(s)].                              (4)

This subtracts the empty blocker mass before charging the whole output. Each blocker separately satisfies H(1-2h_i)=h2(4a_i(1-a_i))+4a_i[H(P_hi)-h2(a_i)]. Substitute this identity and the corresponding k identity into (2)-(4). With

    B=sum_i [b_i H(1-2h_i)+a_i H(1-2k_i)]/2,
    v_hi=4a_i(1-a_i), v_ki=4b_i(1-b_i),

the exact terminal-inclusive formula is H(f)=B+D, where

    D=h2(v)-sum_i [b_i h2(v_hi)+a_i h2(v_ki)]/2
      +2sum_i A_i[h2(a_i)+h2(b_i)]
      +4s[h2(lambda_1)-L+J-h2(s)].                           (5)

All terminal entropies are retained. A terminal FEI hypothesis at K pays B<=K I_private using (1), but (5) alone does NOT pay D by the shared influence. Even when x is absent, the outer AND/OR operation has a cost. A selector-only estimate cannot silently absorb that cost; a complete recursion needs the same physical private reserves and its true gate cost.

## Explicit normalized reference built from terminal references

Fix normalized terminal references Q_hi,Q_ki that are positive on the corresponding blocker spectra. These may be constructed from previously certified complete component references; any conversion between Boolean-output references and blocker references must retain its empty-mass normalization. For nonzero branches define

    R(U,V)=sum_i lambda_i Q_hi(U)Q_ki(V),
    Q_C(U,V,xi)=R(U,V)/2.                                   (6)

This is a normalized whole-set reference, fixed from component references and physical branch masses, without selecting a posterior gate separately for each derivative. It contains all signed-row support because at least one branch amplitude is nonzero whenever an actual row is nonzero. Its complete blocker cross-entropy is

    CE_C=CE(r,R)+1
       <=h2(lambda_1)+sum_i lambda_i[CE(P_hi,Q_hi)+CE(P_ki,Q_ki)]+1.

The inequality follows pointwise from R>=lambda_i Q_hi Q_ki and averaging branch i; the +1 is the actual uniform separator-bit cost. The exact reference debt, rather than a silently discarded signed collision, is

    CE_C-H(P_C)=KL(r||R)+1-J.                               (7)

Let q_e=Q_C(empty)=R(empty private set)/2, so 0<q_e<=1/2 (nonzero Boolean indicators have nonzero means; support positivity forces this row positive). For 0<s<1 define the full Boolean-output reference

    Q_f(empty)=1-v,
    Q_f(A)=v Q_C(A)/(1-q_e) for nonempty A.                  (8)

It sums to one and is positive on every actual nonempty coefficient. If s=1 the output is constant and use point mass on empty; the same applies to s=0. Direct summation gives the COMPLETE cost

    CE(f,Q_f)=h2(v)+4s[CE_C-s log2(1/q_e)+(1-s)log2(1-q_e)]. (9)

There are two essential normalization terms in (9), including the empty-row refund. For example C identically one has CE_C=1 with the exact-product references, but its whole-output cost is zero, not an unpayable constant. More generally

    CE(f,Q_f)-H(f)
      =v KL(P_C(.|nonempty)||Q_C(.|nonempty))>=0.             (10)

Thus the reference is concrete, normalized and complete, yet no universal influence payment is assumed. This moves the prior derivative-local conditioning repair to a single whole-set reference. Exact entropy closure still requires a cost bound, not just support coverage.

## First unsupported line and downstream use

The unsupported line is a dimension-independent bound for the excess in (9) together with all terminal conversion costs using ONE influence account (1), permitting iteration through overlapping blocker families. Disjoint-product entropy plus a local residual estimate does not establish it. The signed ledger (5), the same-row refund (9), and the KL debt (10) identify the quantities a whole-set occupation/forest reference must pay. A008's corrected occupation mass may supply a better R than the product mixture; using it requires matching the same actual row law and retaining the full normalizer. No such match or independent adoption has been proved here.

Next: test a complete occupation-based R against (9) in the first genuinely overlapping graph blocker component, with the same terminal reference, and certify either a paid excess or an explicit unpaid signed sector. This directly joins the B02 whole-set mass improvement to B03's C020 gap.
