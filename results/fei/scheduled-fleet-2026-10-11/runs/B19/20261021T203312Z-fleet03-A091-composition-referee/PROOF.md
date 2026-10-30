# First private point query before shared Y: dimension-free payment

Rung: analytic proof, conditional on the explicitly cited scalar packet and physical-channel lemmas already reconstructed in stage6. New grouped Fourier algebra is checked independently below. External review pending. Full FEI remains OPEN.

All entropy is in bits. Let Y be a fresh fair bit, A a point event on r>=1 fresh private bits with q=2^-r, and B any indicator on another finite uniform block with p=EB. Boolean cores u,v,G occupy mutually disjoint blocks, independent of A,B,Y. There is ONE physical G. It may have its own private fine selector, still independent of B and the other blocks. Put

F=(1-Y)G+Y[A u+(1-A)H], H=Bv+(1-B)G.

At any remaining A coordinate i, write d=Inf_i(F), m=Eu, n=Ev, z=EG, c=1-p, h=EH=pn+cz, M=1-mh, Vu=1-m^2, Vv=1-n^2, VG=1-z^2, VH=1-h^2. Then

    d=q M/2,
    B_i(F)<=12 d,
    D_i H(F)<= (12+2/ln 2)d <15d.                 (T)

Here B_i=sum Phi(fhat(S)^2,fhat(S+i)^2), D_i is H(F) minus the fair average of the two physical child entropies, eta(t)=-t log2 t and Phi(a,b)=eta(a)+eta(b)-eta(a+b). No child entropy is omitted.

## Exact grouped identity

Define P=Phi((1-q)^2,q^2), L=(1-q)h+qm, w=q(m-h), and

    S=p Vv+p(1-p)[VG+(n-z)^2]=VH-c^2 VG >=0,
    R0=[Phi((z+L)^2,w^2)+Phi((L-z)^2,w^2)]/4,
    RG=[Phi((1+(1-q)c)^2,q^2 c^2)
          +Phi(((1-q)c-1)^2,q^2 c^2)]/4.

The saved NEXT_IDENTITY equation (1), followed by disjoint data-frequency decomposition, gives

    B_i=(q-2q^2)M+q^2 Vu+(S/2)P+VG RG+R0.       (1)

To reconstruct the grouping: nonempty u frequencies have H=G=0 and sum to q^2 Vu. Nonempty v frequencies give (p Vv/2)P since sum Bhat(T)^2=p. Nonempty G frequencies with nonempty B frequency give p(1-p)VG P/2. Empty-data/nonempty-B frequencies give p(1-p)(n-z)^2 P/2. Nonempty G frequencies with empty B frequency give VG RG. The fully empty data/B frequency gives R0. The remaining nonempty A frequencies are the first term in (1). These sectors partition the physical Fourier basis; arbitrary B geometry and G dimension enter only through Parseval. In particular two independent copies of G would not give (1).

## Bounds and every side condition

For a,b real, the previously reconstructed scalar lemma is Phi(a^2,b^2)<=2|ab|, including zero arguments. All factors below are nonnegative. For |m|,|h|<=1,

    Vu<=2M, VH<=2M, |m-h|<=M.

The first two follow from 2M-Vu=(m-h)^2+VH and 2M-VH=(m-h)^2+Vu. For the third, M^2-(m-h)^2=Vu VH>=0 and M>=0. Also

    VH=p Vv+c VG+pc(n-z)^2 >= c VG,
    0<=S=VH-c^2 VG<=VH.

Since 0<q<=1/2,

    (q-2q^2)M+q^2 Vu <=qM=2d.                   (2)

Because |L|<=1 and |z|<=1, and |z+L|+|L-z|=2 max(|z|,|L|), the scalar lemma implies

    R0<=|w| max(|z|,|L|)<=q|m-h|<=qM=2d.        (3)

Since 0<=c<=1 and 0<= (1-q)c <=1, the same absolute-value identity yields RG<=qc. Therefore

    VG RG<=qc VG<=q VH<=2qM=4d.                 (4)

Finally P<=2q(1-q), so

    (S/2)P<=q(1-q)S<=q VH<=2qM=4d.             (5)

Adding (2)-(5) proves B_i<=12d. The physical-channel inequality D_i=B_i+J_i, J_i<=2d/ln2, gives (T). No tiny influence is divided out. If d=0, (2)-(5) force every nonnegative sector in (1) to vanish; D_i=0 as well. Empty or certain B (p=0 or1), constant cores, r=1, and arbitrarily large r all remain in these same formulas. If physical data have previously been exposed, apply the statement to the actual restricted sign cores; their dimensions and biases are unrestricted. Prior data exposure must preserve the stated independent-block geometry.

## Original reserve and terminals

For the original physically merged fine reserve R=sum eta(label probability) Var(fine core), the saved NEXT_IDENTITY equation (2) gives

    kappa= q Vu/2 + p k(q)Vv/2 + kG(q,p) ZG >=0,
    k(q)=eta(1-q)-eta(1-2q)/2,
    kG=eta((1+(1-q)(1-p))/2)
        -[eta((2-p)/2)+eta((1+(1-2q)(1-p))/2)]/2.

Here ZG=sum a_l Var(g_l) over G's actual fine cores; use ZG=VG if G itself is one core. Concavity proves both coefficients nonnegative, including all endpoints. No independent-copy reserve is introduced. The inherited U is harmonic at this controller query. Hence

    (H-U-R)_parent - E(H-U-R)_child
       =D_i-kappa <=(12+2/ln2)d.                (6)

This spends no additional old surplus. It preserves both exact child H-U-R terminals and the old labels/debits. It closes the first-live-A NEXT_IDENTITY interface with an arbitrary B event and one repeated fallback. It does NOT assert an analogous bound for a later B query while A is unresolved, multiple earlier live priorities, mixed orientations, overlapping selected-data blocks, or a universally funded inherited U/R. Those require their own geometry and funding. The accepted A059 rate<17 can accommodate this node, but no arbitrary-order tree theorem is asserted from this one-node extension.

First unsupported line toward the next target: for a B coordinate queried while A and Y both remain unexposed, bound the correlated earlier-u/fallback packets at the SAME original reserve and preserve both terminals. The current grouping uses that u is selected directly by the queried point event; swapping A and B does not preserve that hypothesis.
