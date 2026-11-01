# Same original bank pays every padded-bit prefix with fresh floors

All logarithms are base two. This refines A011's existing arbitrary-core envelope; it is not a universal FEI theorem. The fresh floors below are prescribed, not freely replaced by true spectra.

Let g be any nonconstant Boolean function on a>=1 source bits, b>=1 independent padded data bits, r>=1 fresh control bits. Put n=a+b, t=2^(-n), p=2^(-r). Translate the edit point to zero and set F=g-2g(0)1_(controls=0,data=0). Supply any source subprobability R of mass s<=1, positive on P_g support, with c=CE(P_g,R)<infinity. Pad R by zero on every nonempty dummy frequency. Assume only c<=C0 I_g, C0>=0. The original root floor is A011 stage6's Rdagger=(Rpad+6pt U_n)/(1+6pt), lifted through the true conditional control kernel. Its complete mass is (s+6pt)/(1+6pt). Write K=4C0+15. The accepted scope here is author proof, independent review pending.

Query ell padded bits, 1<=ell<=b, continuing only when all queried values match the edit point. Off that path, the Boolean function is exactly g with its remaining unused coordinates; prescribe the ORIGINAL source reference R with zero dummy/control frequencies. On the surviving branch, prescribe the SAME floor formula using the ORIGINAL source R, n-ell remaining data bits, and beta_ell=6p2^ell t. No child's influence-paid source certificate is asserted. Every source copy is charged with its actual root reach, whose sum off the surviving branch is 1-2^-ell. The surviving floor has mass (s+beta_ell)/(1+beta_ell), not root mass, and its missing mass remains in its CE and divergence.

Let P_v,Q_v be the true spectral law and prescribed reference at each node. Let d_v be actual physical query influence and Delta_v=H(P_v)-[H(P_v0)+H(P_v1)]/2. Define each signed reset charge

    lambda_v = [D(P_v0||Q_v0)+D(P_v1||Q_v1)]/2-D(P_v||Q_v).

Here D(P||Q)=CE(P,Q)-H(P) for a subprobability Q; it includes -log(sum Q). If using physical inherited references first, the earlier mass-preserving disintegration and then the fresh reset give exactly the same lambda_v; neither normalization is erased. The FULL reset ledger is

    L_ell = CE(P_root,Q_root)+sum_(j<ell) 2^-j lambda_j
          = sum_(j<ell) 2^-j Delta_j + sum_leaves reach(v) CE(P_v,Q_v)
          = H(F)+sum_leaves reach(v) D(P_v||Q_v).             (1)

All off-path leaves and the surviving nonconstant terminal are present. The telescoping equality follows by cancellation of each INTERNAL prescribed reference, not by assigning a fresh source bank. Arbitrary independent terminal h and its subprobability R_h add c_h to (1) and add D_h to every weighted terminal divergence; their masses multiply, so they cannot fund the reset.

The existing envelope bound CE<=2c+15(C+E+J) applies to the surviving point edit using its original source R. Thus, with s0=n+r,

    sum_leaves reach CE <= (1+2^-ell)c +30pt(s0-ell).       (2)

At depth j the physical pivotal probability of the queried padded bit is d_j=2p2^j t. It is strictly between0 and1, since a>=1 and j<=b-1. The elementary one-bit spectral identity gives

    Delta_j <= h2(d_j)+(4/ln2)d_j
            <= d_j[log2(1/d_j)+5/ln2].

For completeness, the child amplitudes u,v have m=(u²+v²)/2. The entropy decrement is membership conditional entropy plus JS of the child squared spectra. Membership entropy is at most h2(d_j) by concavity. The pair JS contribution in natural units is

    [u² ln(u²/m)+v² ln(v²/m)]/2
    <= (u²-v²)²/[2(u²+v²)] <= (u-v)².

The first inequality is log x<=x-1 (zero terms by continuity), and the second is (u+v)²<=2(u²+v²). Summing and dividing by ln2 gives JS<=4d_j/ln2, because sum(u-v)²=4d_j. Zero pairs contribute zero and require no division. Thus no sharp JS/Hellinger comparison or external analytic premise is required.

Since ln2>3/5, 5/ln2<9. Combining (1),(2) and summing log2(1/d_j)=s0-j-1 gives

    L_ell <= (1+2^-ell)c + 2pt T,
    T=15(s0-ell)+ell(s0+8)-ell(ell-1)/2.                (3)

This bounds the full leaf-plus-query bill, not selector entropy alone. The elementary inequality ln2>3/5 follows, for example, by integrating 1/x on [1,2] and using the lower midpoint-paired bound 2/3 (or the first atanh term at 1/3).

The hypercube's minimum nonzero edge boundary is a, hence I_g>=2a2^-a. One elementary induction proves the edge boundary fact. If both (a-1)-dimensional sections are proper nonempty sets, their internal boundaries total at least2(a-1)>=a for a>=2. If exactly one section is proper, its internal boundary is at least a-1 and at least one crossing edge leaves the set. If neither is proper and the full set is nontrivial, one section is full and the other empty, giving2^(a-1)>=a; a=1 is immediate. Thus no dependence-on-every-coordinate hypothesis is needed.

Set q=b+r>=2. Because ell>=1, ell<=b<=q-1, a>=1,

write T=(15+ell)a+H with H=(15+ell)q-7ell-ell(ell-1)/2. Here H>=ell²/2+19ell/2+15>0, using q>=ell+1. Thus dividing H by a>=1 can only decrease it. This justifies the sign-sensitive first inequality below; the negative terms cannot separately be divided and discarded.

    T/a <= (15+ell)(1+q)-7ell-ell(ell-1)/2
         <= (q+14)(q+1)-7 = q²+15q+7.

The sequence (q²+15q+7)/2^q decreases for integer q>=2: twice its numerator at q minus the next numerator is q²+13q-9>0. Its maximum is41/4 at q=2. Consequently

    2pt T <= (41/4) I_g,
    L_ell <= (3/2)c+(41/4)I_g.                          (4)

Let d be g's original pivotal degree at the source point. Erased edges E=2ptd obey E<=p2^-b I_g<=I_g/4, because I_g>=2*2^-a*d; all those d edges are distinct. Created edges C=2pt(n-d) and controls J=2rpt remain retained in I(F)=I_g+C-E+J. In particular I(F)>=3I_g/4. At the SAME original K=4C0+15,

    K I(F)-L_ell >= [(3/2)C0+1] I_g >0.              (5)

Indeed (3/4)(4C0+15)-(3C0/2+41/4)=3C0/2+1. The exact residual bank after paying the incoming root CE is B_root=K I(F)-CE_root. Equations(1),(5) imply sum reach lambda<=B_root-[(3/2)C0+1]I_g. This pays prescribed fresh floors from the SAME unused original remainder, with no renewed rate or descendant reserve. A previously booked debit A remains permitted only when A is no larger than the displayed remaining margin; it is never silently refunded.

Padding bits may be chosen in any adaptive order on the sole active path; permutation fixes the source, translated edit point and prescribed padded references, so the same reaches and costs apply. Unedited branches may be stopped at their supplied full source reference. For nonconstant g every stopped and surviving leaf is nonconstant (a control assignment outside the edit retains g), including ell=b.

The nonconstant-source assumption is used in the minimum-boundary conversion. A constant source with a positive-cost reference fails c<=C0 I_g; even with c=0 it has I_g=0 and the claimed Ig-scaled bounds in(4) need not hold. Fresh queries of a genuinely source-dependent bit also fail the source-copy premise in(2). Those are excluded, not proved by the padding argument.

First unsupported universal line: pay a prescribed fresh reference after a query that changes the SOURCE core itself, retaining the original reference and every already booked debit. The source-independent symmetry and I_g lower bound do not price arbitrary amplitude changes. Full FEI remains OPEN.

All denominators used above are valid: a>=1, every active q_T>0 by q_T=(ghat(T)-2pt phase)^2+4p(1-p)t² with 0<p<=1/2, and finite source CE forces s>0. Root and fresh masses are therefore positive; each nonzero child true law has positive inherited Z_b. The query probabilities d_j are in(0,1), and zero amplitude pairs are excluded before dividing by u²+v². Translations of the physical edited point preserve squared source spectra and source model cost. The only new integer sequence parameter is q=b+r>=2; no continuum or dimension extrapolation is used.
