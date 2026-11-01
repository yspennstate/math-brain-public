# Two prepaid tickets and a stopping theorem without a depth bound

All functions are Boolean signs on finite uniform cubes. Entropy is in bits. Write D_i(g)=H(g)-E_a H(g|i=a), p_i=Inf_i(g), and I(g)=sum_i p_i. Statements concern expected-resource accounts with explicit conditional-mean-zero child innovations, as in A059@2. They do not assert subtraction-only cash in each child.

## 1. Universal one-query input, independently reconstructed

Set delta=min(p_i,1-p_i). The sign u=g_0 g_1 has influence at most I(g_0)+I(g_1)=2(I(g)-p_i). Edge isoperimetry on its smaller sign class gives I(u)>=2 delta log2(1/delta). Thus

  I(g)>=p_i+delta log2(1/delta).                         (1)

At delta=0 the logarithmic term is zero. The normalization is checked by a one-point set: a sign negative on density a has boundary influence at least 2a log2(1/a). An induction splits the two set sizes and uses h2(q)>=2q for 0<=q<=1/2. The union bound applies to each other coordinate before summing.

The spectral erasure is at most h2(p_i); the full child Jensen-Shannon packet is at most min(1,2delta/ln 2). Consequently

  D_i(g)<=h2(p_i)+min(1,2delta/ln 2).                  (2)

These are the actual children, with their empty coefficients retained. This uses the established amplitude-pair JS inequality (A057/B17), not FEI. Let ell=log2(3) and kappa=3-2/(1+ell). Then

  2<kappa<9/4,             D_i(g)<=kappa I(g).          (3)

For 0<=p<=1/2 put a(p)=p(1+log2(1/p)). Since ln2>2/3, the right side of (2) is at most h2(p)+min(1,3p). On [0,1/3] the difference kappa a-h2-3p is concave, with values zero at both endpoints. On [1/3,1/2] the difference kappa a-h2-1 is concave, with endpoint values zero and kappa-2. Both second derivatives equal [1/(1-p)-(kappa-1)/p]/ln2, which is nonpositive on these intervals. Endpoints at zero use continuity. For p>=1/2, (1) implies I>=p+delta=1 because log2(1/delta)>=1, and D<=2. The inequalities ell>1 and ell<5/3 follow from 3>2 and 27<32. This reconstructs A060's bound; it is not a new constant claim.

For an entirely rational account use k=29/13>kappa, since 3^5<2^8 implies ell<8/5. Then 9/2-2k=1/26 exactly. Every transaction below remains valid with k replacing kappa, A=2k at q=1/2, and a retained original reserve at least (1/26)tI(g) plus its previously released cash. The validation and Lean source use this rational version.

## 2. Two tickets from A091's SAME original 9/2 source

Put K=9/2 and epsilon=K-2kappa>0. Initially split the original core account K c I(G) into TWO labelled tickets kappa c I(G), and unused epsilon c I(G). This occurs BEFORE either ticket is consumed. No second root owner is added.

Through every prefix already paid by A059's original exterior cash, a pending ticket has principal kappa t I(g). At a previously paid core query i, replace its principal in actual child a by kappa t I(g_a), and add kappa t p_i to its unused cash in BOTH children. Conditional influence conservation makes this ticket harmonic. At exterior restrictions t is harmonic and g fixed; tags preserve core influence. Old unused cash is unchanged. The same transport applies to the epsilon account. This retains all already booked entropy debits and all siblings.

At the FIRST selected further core query, spend ticket 1 once on a=tD_i(g). Inequality (3) leaves its scalar cash kappa t I(g)-a>=0 in BOTH children; close ticket 1. Ticket 2 remains pending and is transported through this same split by the preceding influence identity, releasing kappa t p_i into its own cash. No fee is charged to ticket 2. At the SECOND selected further core query, spend ticket 2 by the same rule and close it. Each choice may depend on all previous physical answers; there are at most two selected extra core queries per path. Unused tickets survive in branches that stop earlier. Arbitrary already-funded exterior/tag history may intervene or follow.

At each core query the inherited-core fee is a=tD_i(g), and the FULL physical entropy debit is exactly a+E_parent-E_a E_child, with E=H(K+Cg)-tH(g). Thus combining the original exterior L+E with the labelled tickets and all their released cash gives the exact stopped identity

  H(F_root)=B_root+E_leaf[H(F_leaf)-B_leaf].            (4)

Every full terminal function remains. The source's old L>=m/8 survives. At the handoff frontier an additional epsilon t I(g) remains unspent (plus its historical releases). This is not a uniform positive absolute reserve if g is constant or t=0. Child ticket principal may exceed its parent in one branch; the stated expected-resource scope allows the explicitly balanced innovation. A subtraction-only cash statement would need extra hypotheses and is not asserted.

This pays a necessary SECOND query after A091's one-shot target using its original 9/2 rate, provided the original ticket is refined before its first expenditure. It does NOT claim that an arbitrary past protocol which has already irreversibly spent or reassigned all capacity can be repaired retrospectively. A060's smaller kappa-rate owner alone has not been enlarged for free.

## 3. Geometric stopping: arbitrary depth, one original bank

For ANY adaptive core query policy, force stopping after each selected extra core query unless a fresh independent physical fair dummy bit permits continuation. Dummy coordinates do not occur in F, so they have zero influence and entropy debit. They are distinct from the source's genuine tag, and are never used as a fictitious free tag exposure. Both outcomes and their full terminal functions remain. For a continuation probability q<=1/2, two or more fair dummy bits implement dyadic q; q=0 simply stops.

Set A=kappa/(1-q). Initially reserve ONLY A c I(G), which is at most 2kappa c I(G)<K c I(G). Carry its pending principal A t I(g) through any previously paid prefix as above. At a selected query i the actual fee is a=tD_i(g). Commit A t I(g_a) in each surviving child and zero pending principal in each stopped child. The expected surviving principal is q A t (I(g)-p_i). Therefore the scalar release available to every query/coin descendant is

  r=A t I(g)-a-q A t(I(g)-p_i)
    >=t[(A(1-q)-kappa)I(g)+q A p_i]
    =q A t p_i>=0.                                  (5)

Previously unused cash stays unused. The two physical stages (core answer followed by the independent coin) may be treated as a finite transaction: before the coin, reserve q A t I(g_a); the coin's surviving child receives A t I(g_a), its stopping child zero. Their mean equals the reserved amount; no entropy is charged at the dummy split. Conditional-mean-zero innovations and r give exact local account conservation. An adaptive choice to stop sooner only reduces the commitment. Finite stopping trees of ANY depth satisfy (4), with all terminals retained. No optional-stopping limit is needed.

Equivalently, if w_v is physical reach probability, the selected-query occupation satisfies sum_v w_v t_v I(g_v)<=c I(G)/(1-q). This follows by conditional influence conservation, harmonic exterior density, and independent survival at each stage. Applying (3) and summing gives the same bill bound. The transaction proof supplies an actual nonnegative ledger, rather than only an aggregate estimate.

At a finite cap with no further query, the pending bank is retained, or closed into unused cash. The q=0 boundary is the one-shot theorem; q=1/2 is paid by the original 9/2 owner with the same epsilon source reserve. q=1 is excluded: (5) would not admit a finite A. Reusing a queried coin, conditioning survival on the core answer without its actual conditional probability, or dropping stopped siblings invalidates the proof.

## 4. Explicit growing-depth functions and limits of the bridge

For every N>=1 let G_N be the product of N disjoint AND2 signs (each negative only at (1,1)). Let F_N=K_4+C_4 G_N z, where K_4=b_4-C_4, C_4 is the all-one exterior point, b_4 is the paired bent sign, and z is a fresh genuine tag. Adjoin N-1 independent dummy coordinates used ONLY for fair stopping. Query a fresh core factor's first variable at every surviving step, up to N, interleaving any allowed exterior/tag history. There are paths with N genuine core queries, and positive inherited-core entropy decrement on such paths (in particular the constant-child spine has fee 2t at each step). Thus the theorem covers unbounded core-query depth, not merely an arbitrarily deep syntactic description. Dimension, N and stopping depth have no uniform bound; the original source price is at most (9/2)I(F_N).

For clarity this stochastic stopping does not solve FEI. Even at q=1/2, many leaves stop with a large untouched G_N tail. A universal full-core price H(G)<=K I(G) would itself imply FEI(K); no such price has been proved here. The two-ticket and geometric statements keep terminal entropy explicitly. Removing compulsory killing, or supplying enough paid terminal entropy decay for arbitrary cores from the SAME original unused capacity, is the first unsupported line. The new result replaces the one-shot boundary with two actual queries and a depth-free paid but potentially unproductive stopping policy.
