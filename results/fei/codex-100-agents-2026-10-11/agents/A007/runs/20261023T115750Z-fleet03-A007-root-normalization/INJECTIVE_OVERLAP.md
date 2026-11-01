# Exact transfer through overlap with private parity coordinates

This is a universal supplied-reference transport lemma with an explicit structural hypothesis. It supplies an overlapping application of the signed root normalization; it does not solve arbitrary physical overlap.

Let f:{-1,1}^N -> {-1,1} be any Boolean function, and let b_1,...,b_N be fixed subsets of k auxiliary coordinates. With independent private bits x_1,...,x_N and auxiliary bits z_1,...,z_k define y_j=x_j prod_{t in b_j} z_t and G(x,z)=f(y). For S subset [N], write b(S)=symmetric_difference_{j in S} b_j and L(S)=S union (N+b(S)), with the two coordinate types disjoint. Character substitution gives

    Ghat(L(S))=fhat(S), and Ghat(A)=0 off the image of L.

The map L is INJECTIVE because its private-coordinate part is S. Thus no two amplitudes alias, and their squares really do transport as probabilities. The invertible triangular change (x,z)<->(y,z) preserves the uniform cube. Consequently means, variance and entropy are unchanged, and

    I(G)=I(f)+sum_S fhat(S)^2 |b(S)| >= I(f).           (1)

For ANY fixed normalized nonempty reference q on virtual subsets, define Q(L(S))=q(S) for nonempty S and zero elsewhere. This is an explicit normalized output law and covers every nonempty Fourier-supported set of G. It obeys

    C_G(Q)=C_f(q).                                    (2)

The full empty/nonempty wrapper transfers identically. Positivity off the spectral image is not needed for this root cost. If a later interface specifically requires strict positivity on EVERY nonempty physical subset, use Q_epsilon=(1-epsilon)Q+epsilon U for a fixed full-support reference U: C_G(Q_epsilon)<=C_f(q)+v log(1/(1-epsilon)), with v<=I(G), charged ONCE. No free reset along histories is asserted.

Apply this to the whole-set conjunction sampler in NORMALIZATION_TELESCOPE.md, or to A015's independently reviewed explicit dictionary. Its masks, local subsets, root denominator and arbitrary-activity KL remainder transport WITHOUT CHANGE. In particular the negative v log(1-B) term and the cancellation in formula (5) remain exact even though all physical components may share auxiliary bits. The influence payment uses I(f)<=I(G); it does NOT replace virtual component influences in the disjoint identity by a sum of overlapping physical component influences.

Concrete all-parameter overlapping family: take A015's arbitrary independent mixed-width obstruction family F=2U_X[1-U_Y(-Y)]-1. Replace EVERY private variable by x_j z using ONE common auxiliary bit z. Every actual clause now depends on that shared physical bit. This is an actual Boolean family on N+1 bits, with arbitrarily many physically overlapping clauses. Its transported whole-set reference has nonempty cost <8I(G), full wrapped cost <9I(G). Means and root normalizers are identical to the disjoint base. If the image-only code is sufficient there is no extra selector cost. A full-support mixture with epsilon=1/2 instead gives <9I(G) and <10I(G), respectively. This is a reference-transfer application, not a new original-prime queue bound and not a novelty claim about FEI on this class.

Why the unrestricted bridge remains open: arbitrary shared variables need not admit private coordinates that make L injective. With amplitude collisions, the exact OR2 certificate in NORMALIZATION_TELESCOPE.md shows that squared spectral mass is not the positive pushforward. A universal proof must pay this signed interference and its changed conditioning from ONE physical influence account. Private parity lifts isolate the collision-free part precisely, rather than assuming all overlap is disjoint or all overlap is fatal.
