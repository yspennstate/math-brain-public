# A065 stage20: reconstruction of the A087 physical-history repair

All entropies and divergences are in bits. Full FEI is OPEN. This is a review of A087-PRODUCT-HISTORY-SIGNED-COCYCLE-INSTALLATION@1, not a renamed new claim. No source repair is needed. A065 originated its selector-only baseline dependency, so this reconstruction is not represented as an independent full-chain review of that earlier A065 claim. A094 should supply that review.

## 1. Reconstructing the actual one-query identity

Let p be the squared Fourier spectrum of a finite Boolean function and q a normalized law supporting p. For a queried coordinate i, erase the spectral i bit to p^- and q^-. The actual physical children have spectra p_b and physical probabilities 1/2. The coherent kernel is k_b(a)=p_b(a)/(2p^-(a)) when p^-(a)>0, and 1/2 otherwise. In both cases k_0+k_1=1. Thus r_b=sum_a q^-(a)k_b(a)>0 and q_b=q^-k_b/r_b are normalized and source-supporting.

Define K=KL(p||q), E=K-KL(p^-||q^-), and O=KL((1/2,1/2)||r). The ordinary chain rule on the original spectral coordinate gives E>=0. On the joint law (a,b), compare p^-(a)k_b(a) against q^-(a)k_b(a). Its divergence is KL(p^-||q^-) because the kernels agree wherever the source is positive. Splitting by the physical outcome b gives

    K = E + O + (K_0+K_1)/2.                         (1)

This explicitly includes q-mass on p-zero rows. It does not identify a physical outcome probability with r_b. In particular (1) remains valid if erasure merges a q-only atom with a source-positive atom.

## 2. New all-history extension: reconstruction without a repair

Take any disjoint Boolean product with original reference tensor_j R_j, each normalized and source-supporting. At a fixed reached history, adaptive query choices and their realized bits specify a cylinder. The restricted Boolean function is still a product, with actual spectrum P=tensor_j P_j. Transport the reference globally to Q, and separately transport each original R_j under that module's local history to R_jh. Define T=tensor_j R_jh, G=KL(P||Q), L=KL(P||T), d=G-L. Additivity gives L=sum_j KL(P_j||R_jh).

Apply (1) globally and to the queried local module. Other local summands are unchanged. Subtraction gives, at every query,

    mean d_child = d + (E_local-E_global)
                     + (O_local-O_global).           (2)

No assumption about persistent original source-zero sectors enters this derivation. The source-weighted signed correction d is finite; KL(Q||T) need not be finite. All stopped equalities are finite sums over bounded fair physical trees. Initially G=L=A, d=0. Thus the corrected local ledger L+d=G, terminal G, and actual global charges E_global+O_global use exactly the original A. This is the A087 extension that replaces A065's former selector-only NEXT.

Before one optional actual installation of T, the nonnegative potential V=G+L has drift E_global+O_global+E_local+O_local, at least the actual O_global. At the choice, V dominates either retained G or installed-reference KL=L. After that choice use current global KL and (1), including the actual global kernel of the installed reference. Therefore every admitted bounded policy satisfies

    E K_terminal + E sum O_actual <= 2A.             (3)

There is no second free installation. Stops before the choice need only G, also dominated by V. Full terminal entropy is retained by adding E H_terminal to BOTH sides of (3). It has not been removed or paid by naming it zero.

For the GF4 products A=5L/2, S=23L/2. Keeping old consumption omega<=S/4 and booking 2A once leaves S-omega-2A>=29S/92. If only the original A pipeline was booked, the second A is a real extra allocation. No spent debit is refunded.

## 3. Independent finite representation at the fixed original product root

The source is exactly the nine-bit module of A065 stage19, constructed afresh from a GF4 multiplication table in code/review.py. For y=(a,b,x), h(y)=(-1)^(a_0)(1-2*1[x=ab]); C_g(u,v,y)=(-1)^((u+v+parity(y))v)g(y); f(s,u,v,y)=C_1 if s=0 and C_h if s=1. Direct character sums independently reproduce its integer Walsh spectrum, H=13/2, and all nine physical influences 1/2. Hence the actual original marginal product is uniform, K=5/2, and for two copies A=5, S=23.

After erasing the first selector, the four outside cells (G, H-large, H-small, zero) have 4,4,192,56 remaining Fourier rows, respectively. Their laws are

    P=(1/2,1/8,3/8,0), Q=(1/64,1/64,3/4,7/32),
    P_G=(1,0,0,0), P_H=(0,1/4,3/4,0).

The separately transported local selector predictions are (1/8,7/8), whereas the actual two-module predictions are (53/256,203/256). Local descendant cell references are QL_b(z)=Q(z)k_b(z)/r_local,b, with the fair extension at the zero cell. These values are not supplied as a synthetic Boolean spectrum: the truth table and cell degeneracies are checked independently.

For queries in the already selected module, retain ALL 256 target Fourier rows and compress only the other module's four cells. For queries in the other module, retain ALL 512 target rows and compress only the selected module's four cells. Source and reference are uniform within each outside cell and all target query kernels depend on the outside row only through its cell, so these 1024/2048-row representations preserve KL, erasure, predictions, and descendant references exactly. Full entropy is the sum of the target's actual entropy and the outside module's FULL entropy, not the entropy of four synthetic atoms.

Both first-selector outcomes and all six ordinary coordinates in either module are checked: 24 queries, 48 children. Every child's squared Walsh law is independently recomputed by direct character sums and compared against the FWHT helper. Each of the 48 local tensor descendants is actually installed, then one further fair physical query is made using that installed law globally. Thus the post-installation part of (3) is concretely exercised, including all reference-only rows.

## 4. Exact ordinary-query boundary and necessary erasure correction

If the data query is in the selected module, on every source-positive outside cell the actual target reference is a constant multiple of its local target reference on ALL target rows. Conditional reference laws in erased pairs agree, even when a reference-only row merges into support. Therefore E_local=E_global for these 12 queries.

For a query in the other module, fix any positive source cell of the selected module. Its actual reference weights on target source-positive rows are twice the weights on target source-zero rows. If an erased pair has two positive source atoms, both conditional reference laws agree. If it has exactly one, the local conditional reference gives that source atom probability 1/2 and the global conditional gives 2/3. The contribution to E_local-E_global is consequently p^-(pair) log2(4/3). Pairs with no source contribute zero. Hence

    E_local-E_global = rho_i log2(4/3),
    rho=(0,5/8,5/8,5/8,7/64,7/64)

in ordinary order a0,a1,b0,b1,x0,x1, after EITHER first-selector outcome. These rho values are certified by exact rational summation of the directly reconstructed Boolean spectrum. Ten of the 24 queries have strictly positive erasure defect. The erased q-only-to-source-positive mass is measured separately: it is positive in 18 cases. It is not inferred from rho; re-entry and a nonzero global/local erasure difference are different conditions.

Equation (2) is checked as an identity of rational linear combinations of prime logarithms in every case. Thus an outcome-only extension of the earlier selector ledger is false at the genuine original product root; the signed erasure difference is necessary. This is a reconstruction of A087's obstruction, not a new refutation credited to A065.

## 5. Sharp booking certificate for this precise finite policy class

At a reached state let d=G-L. Immediate optional installation requires extra pending reserve [-d]_+. For a prescribed next query followed by independent retention/installation in the children, (1) makes the exact necessary and sufficient reserve

    [ mean[-d_child]_+ - E_global ]_+.

Allow inherited stopping, immediate installation, or one of the ordinary queries. Maximize these amounts BEFORE averaging over the first-selector outcomes. The certificate in out/MAIN.json evaluates every alternative with exact prime-log forms and rigorous 96-bit rational logarithm enclosures. Both child full entropies are explicitly recorded. The maximal branch reserves are

    B_G=0, B_H=log2(32/29),
    B_root=(1/2)log2(32/29)<1/8.

The branch maxima already equal the immediate selector-only optional-installation liabilities: d_G=log2(53/32)>0 and d_H=log2(29/32)<0. Hence adding the one ordinary query needs zero top-up IF that nested booking was already pending. Necessity follows by choosing the H installation and stopping; sufficiency follows by the branchwise maximum and (1), then current-K continuation after installation. The strict upper bound is certified by 32^4<2*29^4. With the same S=23, old omega<=23/4, original pipeline A=5, and this one genuine extra booking, the remaining original account exceeds 97/8. The broader all-history policy still uses (3); this finite improvement is not asserted for arbitrary depths or repeated installations.

## 6. What the funding theorem still cannot supply

An influence-priced original product-KL supplier is false. For the m-bit point sign, put d=2^(1-m). Every influence is d; the empty squared coefficient is (1-d)^2 and every nonempty one is d^2. Their total nonempty mass is epsilon=2d-d^2 in [d,2d]. Thus M=m h2(d)>=m d(m-1). Also

    H=h2(epsilon)+epsilon log2(2^m-1)
      <=epsilon[log2(1/epsilon)+log2(e)+m]
      <=2d(2m+1),

using log2(e)<2. Consequently TC=M-H>=d(m^2-5m-2). Tensor exactly 1/d=2^(m-1) copies: the actual Boolean product has I=m, whereas its original marginal-product KL is at least m^2-5m-2. Hence A/I diverges. This argument is analytic for all m>=3 and does not infer an infinite family from a finite numerical search.

The first unsupported universal line is therefore a NONCIRCULAR influence-priced original reference/owner supplier for arbitrary indecomposable Boolean cores, compatible with actual fair zero-source transport, signed erasure and outcomes, already consumed debits, and full terminal H+KL. Simply assuming the actual marginal-product KL is O(I) cannot supply it. Further product-history depth would not repair this initial obstruction. A094 should audit the full dependency chain; A061/A062/A064 can consume the verified erasure-aware replacement. No FEI proof or Boolean unbounded H/I family is asserted.
