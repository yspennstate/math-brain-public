# Independent reconstruction of A012 v9

All information costs are in bits; the certificate uses nats. Full FEI is open.

## Actual target and account

Let s=(s0,s1,s2) be three uniform bits and let U,V,z be three more uniform bits. Put c(s)=1-2 1{s=0}, G(s,U)=c(s)(1-2 1{s=0,U=0}) and J(s,V)=c(s)(1-2 1{s=1,V=0}). Let F=G when z=0 and F=J when z=1. The integer direct-character transform defines P(T)=Fhat(T)^2, and the original complete reference is Q=P. The checker reconstructs every cofactor from this truth table, without importing the author's helpers. It verifies I(F)=7/8 and I_shared(F)=5/8.

Keep K=4+2/ln(2), the original capacity K I(F), and the entire old liability b=5/(4ln(2))=(2/ln(2)) I_shared(F). This is the original capacity, not K times current remaining influence. No already-paid variance reserve is reissued.

For a physical restriction s, let P_s be its actual Fourier law and Q_s the marginal of the original Q on its free coordinates. On the first state with s0,s1 fixed and s2 still free, perform the mandatory conversion before stopping or querying again. If p=P_s(empty), q=Q_s(empty), put r=(p+q)/2 and beta=(1-r)/(1-q). The converted reference has empty mass r and nonempty masses beta Q_s(T). Charge the complete fee D(R||Q_s). Future references are physical marginals of this anchored reference. No second conversion occurs.

Every conversion denominator 1-q is checked positive. At a descendant t of the anchor the reference is beta Q_t+(1-beta)delta_empty. This is an algebraic identity, not a convex-mixture assertion: beta can exceed one. The checker verifies actual nonnegativity, mass one, and cover on every positive target atom. A zero target atom with positive reference is retained in normalization and in conversion fees. Constant targets retain their full reference cost -log2 Q_t(empty), which need not vanish.

## Finite completeness and the Bellman certificate

An augmented state records a physical restriction and either no conversion or its actual anchor. Reconstruct all reachable states from the root, taking both outcomes of every permitted query. At a mandatory conversion entry take the conversion before allowing any stop/query. At an ordinary entry allow stopping and every unqueried coordinate. This reproduces 729 raw restrictions, 108 conversion entries, and 2121 stored potential rows. The total augmented-state count is 2229, including conversion entries. Both injections and surjections of this enumeration are checked; repeated paths do not create duplicate state rows or duplicate conversion fees.

Let W be the saved rational potential in nats. At an ordinary state it satisfies

    W(s,a) >= D_nat(P_s || Q_s,a),
    W(s,a) >= [B(s[i=0],a)+B(s[i=1],a)]/2,

where B is W at an ordinary entry and fee+W(s,s) at a mandatory conversion entry. Every one of these inequalities is checked, including both children and all reference-only atoms. Induction on the number of free coordinates, with the compulsory conversion as an intermediate transition, gives

    E_terminal D_nat(P||Q) + E_sum full conversion fees <= W(root).

Finite success needs no asymptotic termination assumption: each physical query reduces the free-coordinate count and conversion occurs at most once. The physical-tree policy count obeys T0=1 and Tk=1+k T(k-1)^2, giving T6=482455353348902740055257. This count is not an enumeration of all policies; induction proves the universal policy quantifier.

The rational logarithm enclosure reduces x=2^k r with 1<=r<2 and uses ln(r)=2 sum_{j=0}^{23} z^(2j+1)/(2j+1)+tail, z=(r-1)/(r+1). Here 0<=z<1/3 and the tail lies between zero and 2 z^49/[49(1-z^2)]. Multiplication by k uses the appropriate endpoint of the independently enclosed ln(2). Outward rounding to the common 2^-64 grid preserves containment. Atomwise rational-weighted summation bounds KL and entropy; no floating-point sign establishes an inequality. Decimal output is diagnostic only.

The complete signed entropy telescope is

    b + sum_v reach(v)[H_v-avg H_children]
      + E_terminal CE(P,Q) + E_sum conversion fees
    = b + H(F) + E_terminal D(P||Q) + E_sum conversion fees.

The Bellman bound therefore gives solvency from the SAME original owner. It does not use A011 v5's erroneous identification of a conversion ledger with a terminal functional; this cost convention explicitly includes signed physical entropy increments. It does not pay their positive parts or unspecified extra execution charges.

The exact check compares [(4 ln2+2)(7/8)-5/4-H_nat(F)]-W(root) with (19/1024) ln2, and obtains a strict positive margin. Therefore the weaker stated margin 1/64 bit holds. The separate prescribed policy (s0,s1, conversion, s2, U, stop) is reconstructed from all sixteen complete terminals with four full conversion fees weighted by 1/4; its original-owner margin exceeds 3/5 bit.

Every physical edge also verifies I(parent)=Inf_i(parent)+avg I(children), shared influence conservation with the queried shared coordinate charged only when i is shared, and influence conservation for EACH unqueried coordinate. Thus private queries cannot erase the fixed old shared liability. No new owner or disappearance of a terminal bill is used.

## Tensor bridge by an additive potential

This reconstruction uses a direct additive potential rather than the author's conditioning on full external inputs. Take any finite number m of disjoint physical copies with the product reference and factorwise mandatory conversion rule. At each global history, both its physical cylinder and its complete reference factor across blocks. Fourier laws and references consequently tensor; their terminal KL values add. A factorwise conversion has exactly its local full KL fee because the other factors have mass one.

Assign a global potential equal to the sum of local entry potentials B(s_j,a_j). A query or mandatory conversion in one block satisfies the already-checked local inequality. All other summands stay fixed. Thus every adaptively chosen global operation preserves the required conditional upper bound, regardless of the query order across blocks. Finite backward induction gives total expected terminal KL plus all fees at most m W(root). Entropy and original influence both add, and the signed global entropy telescope then leaves more than 19m/1024 bits from the original m K I(F) capacity, hence more than m/64. This proof retains all original liabilities and full terminals and needs no new history enumeration or independence assumption about the scheduler's decisions.

## Scope and first unsupported line

Verdict is HOLDS at the exact A012 v9 signed-cost supplied-source scope once AUDIT.json and U_POLICY.json report PASS. There is no source repair and no independent-review conflict for A086 on this version. Exact finite certificate plus the analytic finite induction and additive tensor argument is the attained rung. A compiler was not admitted by the fresh memory gate; no Lean certificate is claimed.

The first unsupported universal line is a dimension-independent influence-priced INITIAL complete reference, with suitable current full-reference eligibility, for arbitrary Boolean collision cores; alternatively, a noncircular admission/contraction theorem paid from that same unused original influence. This six-bit source and its disjoint tensors do not supply it. Repeating this seed's query histories cannot settle that line.
