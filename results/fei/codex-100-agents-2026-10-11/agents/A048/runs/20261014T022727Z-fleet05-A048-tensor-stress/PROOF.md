# Common-factor sensitivity of the labelled selector reserve

All inputs are uniform, physical influence is pivotal probability, and entropy is in bits. No terminal entropy is discarded.

## Exact general tensor transformation

Consider an exclusive controller partition C_j(z) with probabilities q_j selecting Boolean cores u_j on one possibly shared data cube. Write mu_j=E u_j, V_j=1-mu_j^2, psi(q)=q log2(1/q), and the existing labelled variance reserve R_lab=sum_j psi(q_j)V_j. This definition is meaningful with shared data, but the independent-core payment theorem does not automatically extend to it.

Multiply the entire output by an independent unqueried Boolean factor v(w), of mean b. This multiplies EVERY selected core by the SAME factor. Then

    R_lab(vF)-R_lab(F)=(1-b^2) sum_j psi(q_j)mu_j^2.

At every controller query, physical influence is unchanged. The Fourier-square law is an independent tensor product, so the erased-sector entropy M and child channel information J are unchanged. Every leaf entropy increases by H(v), root entropy increases by H(v), and terminal influence increases by I(v). In particular a fair one-bit parity factor has H(v)=0,I(v)=1,b=0: it changes neither root nor terminal Fourier entropy, and leaves the entire local controller ledger unchanged, while increasing the labelled reserve. Its terminal influence is retained, not silently charged to the controller account.

## All-essential sparse activation witness

For m,n>=1 let Z be AND on m fresh controls, A be AND on n data bits, t=2^-m, delta=2^-n, and

    G=1-2(1-Z)A, F=yG,

where y is a fresh fair sign. The exclusive labels are Z selecting +1 and (1-Z) selecting h_n=1-2A; for F the cores are y and y h_n. Evaluate Z by short-circuiting at its first zero, then stop at the chosen core. Every reached query is essential: at a live suffix with s controls remaining its influence is 2^(1-s)delta>0. Every variable in G and F is physically relevant. The frontier retains h_n or its parity product, so the root/terminal quantities are

    I_ctrl(G)=I_ctrl(F)=2mt delta,
    E I_leaf(G)=(1-t)2n delta,
    E I_leaf(F)=1+(1-t)2n delta,
    H(F)=H(G), E H_leaf(F)=E H_leaf(G)=(1-t)H(h_n).

The reserves at the root are

    R_lab(G)=4delta(1-delta)psi(1-t),
    R_lab(F)=h2(t).

At every frontier there is only one chosen label, so its reserve is zero. For both fixed-core representations the controller release kappa_v=R_lab(v)-E R_lab(child) is nonnegative by scalar entropy concavity, and sum_v reach_v kappa_v=R_lab(root). However

    R_lab(F)/I_ctrl(F) >= mt/(2mt delta)=2^(n-1).

Thus no absolute K can pay this labelled reserve, or its total release, from the control influence for arbitrary shared-data cores, even with all-essential physical queries and a zero-injection controller-resolved frontier. At m=1, R_lab(F)=1 and I_ctrl(F)=delta: a single essential controller has release 1 with influence tending to zero. The pre-factor reserve is 2delta(1-delta), bounded by 2 I_ctrl at m=1. At arbitrary m, psi(1-t)<=t/ln2 implies the pre-factor reserve/I_ctrl<=2/(m ln2). A harmless entropy-zero common parity factor changes this bounded account into an unbounded one.

The added one unit of terminal influence may pay the order-one reserve if one changes accounts; it is not part of removed controller influence. This witness therefore refutes only the unqualified shared-core extension of the exclusive independent-core reserve bound, not that scoped theorem and not FEI. Exact duplicated cores would already permit a zero-influence label split; our cores differ on an actual delta fraction and all queried variables are essential.

## Required signed cancellation

Let D_v=H(f_v)-E H(child) be the full actual controller entropy decrement, including both M_v and J_v. The common unqueried factor leaves D_v unchanged. Define the existing residual D_v-kappa_v. Finite telescoping gives

    R_lab(root)+sum_v reach_v (D_v-kappa_v)
       =sum_v reach_v D_v
       =H(root)-E H_leaf.

The reserve boost is offset by an exactly equal NEGATIVE shift in the summed residual. This identity is invariant under the common factor. A positive-only reserve release bound cannot be transported from independent cores to shared cores; paying its root reserve and discarding the negative residual loses necessary cancellation. On m=1,n->infinity, D_v tends to zero, kappa_v=1 for F, and the residual tends to -1. This provides a concrete near-identical-core stress fixture for a normalized signed Bayes/occupancy reference. It supplies no proof that the resulting signed cost is universally paid.

On disjoint T-fold tensor copies with independent controller policies, the complete labelled reserve, controller influence, M,J, entropy increments and signed residual sums all add. The problematic ratio is unchanged by tensor powers. Rare activation through larger m introduces the usual m t factor, but the reserve/controller-influence lower bound 2^(n-1) survives uniformly in m; no extra logarithm from tensor multiplication is responsible.

## Independent reconstruction of A050 active-label repair v1

Under its uniform coherent root lift, S has the root Fourier-square law, Q is the final queried set, W=S\Q and D=S intersect Q. Given S, W and D are inverse encodings, and are determined by the physical transcript Pi. Hence e=I(W;Pi|S)=H(D|S). The queried current spectral marginal equals physical influence, and no coordinate is deleted twice. Therefore E|D|=R_removed and a=E|S intersect A|=I_A(f), with a-R_removed=E I_A(f_leaf).

One conditional independent-deletion reference on subsets d of S intersect A is rho_theta(d|S)=theta^|d|(1-theta)^(|S intersect A|-|d|). Summing over subsets gives 1 for every S. Its cross-entropy is -R_removed log2 theta-(a-R_removed)log2(1-theta). Subtracting the exact conditional KL gives e, and minimization at theta=R_removed/a yields a h2(R_removed/a). At endpoints the actual D is deterministically empty or S intersect A. Terminal independence of A therefore implies W=S\A and e=0 even with variable final query sets. The bounded-reservoir clause follows because t h2(1/t) has derivative -log2(1-1/t)>0 for t>1.

For output information o and root channel j, physical independence gives o<=R_removed. The uniform mixture-channel row inequality gives j<=2R_removed/ln2: using child amplitudes G,H, natural row divergence is at most (|G|-|H|)^2/2 <= (G-H)^2/2, then Parseval and finite information chaining give the bound. The scalar inequality is reconstructed in our previous stage PROOF, final section, independently of the source implementation. Chain rule gives j_W<=j+e, so max(o,j_W)/2<=R_removed/ln2+e/2. The previous actual indexed-parity family proves coefficient-one asymptotic sharpness: k=2r+2 has e=r-o(1) and capacity r+log2(euler_number)+o(1). All original claims, including arbitrary shared terminal data under controller independence, hold at this stated scope. A050 is accepted unchanged; no standalone history-bank or shared-core reserve payment is added.

## First unsupported universal line

Construct ONE normalized posterior/occupancy reference on common nonempty Fourier rows that preserves the negative residual above and pays the remaining controller-plus-data-plus-terminal cost from one unspent physical influence account. The scalar labelled reserve, its deletion schedule repair and a marginal history reference do not provide that signed common-row payment. The next test must use the pair of actual near-identical cores and retain their common parity row, rather than infer shared-core ownership from independent-core variance sums.
