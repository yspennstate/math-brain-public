# Essential source debt survives complete cleanup

Let b>=5,k>=5 and m>=1 be integers. Write rho=2^-b,d=2^-k. A source block g_k(z,x) on k control bits z and one output bit x is -1 exactly when all k+1 inputs are0. Equivalently, when z is not the all-zero point it is1, and when z=0 it is the signed literal -chi_x. Let G be the product of m disjoint such blocks. Its mean is mu=(1-d)^m. Assume mu<1/8.

Use the BALANCED source hierarchy of A019 stage21 / A016 stage22: V is a fresh b-bit point, A=V(1-G)/2, p=rho(1-mu)/2, h=chi_u off A and chi_q on A, and F=1 at fresh gate0 and h*w at gate1, with the two-bit flat mask w of mean1/2. Fix ORIGINAL Qh=(Ph+delta_q)/2 and QF(e,T)=[Qh(Tcore)Pw(Tmask)+delta_empty(T)]/4 at BOTH gate frequencies. All descendants inherit literal original frequency marginals. Retain original U=Lq+Econv as in stage21;0<=U<5/8. This is a terminal-functional account, not a claim about a separate accumulated query-KL transaction ledger.

Query q, then reveal all k control bits of every source block. If a block's control is not0, clean its remaining x bit, retaining both identical children. If its control is0, keep x unqueried. Retain every control,cleanup and q outcome. Padding,u,mask,gate remain untouched. Let M be the number of surviving x bits. Then M is Binomial(m,d); the remaining source is a signed character of EXACTLY these M essential bits when M>0, and the constant1 when M=0. No irrelevant source bit remains.

The original g_k squared Fourier law has P0=(1-d)^2 and all other2^(k+1)-1 masses d^2. Its physical influence is I(g_k)=(k+1)d. The entropy is
H(g_k)=eta((1-d)^2)+4kd-2kd^2 <4(k+1)d=4I(g_k),
because -ln(1-d)<=d/(1-d),ln2>1/2 give eta((1-d)^2)<4d. Tensor additivity proves H(G)<4I(G). Thus this is an actual rate4 source, not an abstract probability measure or an ineligible initial supplier.

After projecting out the k controls of one block, its ORIGINAL reference on x has R(x-frequency=1)=I_x(g_k)=d and R(0)=1-d. Cleaning an inactive block removes x too and leaves reference mass1. Therefore at a complete cleaned leaf with M active blocks the actual source law is a point mass at the full M-bit set, but its ORIGINAL reference there is d^M. Consequently

CE(P_Gleaf,R_leaf)=kM, I(Gleaf)=M,
E[CE-4I]=(k-4)md,
E[r_leaf(CE-4I)]=rho*(k-4)md,

where r_leaf=Pr(V|leaf)=rho because padding has not been queried. This is an exact posterior-weighted essential debt; cleanup releases no further source cost. It disproves replacing the stage21 cleaned-source contract by root eligibility alone.

For each M>0, look at the full outer Fourier sector with NONEMPTY source frequency. There is precisely one such supported source set, the full active set. Each of its2^(b+1) padding/u replicas, four mask frequencies and two gate frequencies has true mass rho^2/64 and ORIGINAL reference mass rho^2*d^M/128. Thus this sector has total true mass rho/4 and EXACT complete CE

C_nonempty(M)=(rho/4)(2b+7+kM).

For M=0 that sector is absent. Put pi=Pr(M>0)=1-mu. Averaging ALL physical leaves gives

E C_nonempty=(rho/4)[(2b+7)pi+kmd].

The actual physical influence at a leaf, for either q sign sigma, is
4I(F_leaf)=6+(b-1-sigma/2)rho*1_{M>0}+rho*M.

This follows directly from gate,mask,u,padding,source edges; all influence is remaining influence, not a renewed budget. Averaging both q signs gives EXACTLY

E 4I=6+(b-1)rho*pi+rho*md.

Since all other CE terms and old U are nonnegative,

E[4I-CE]-U <=6+b*rho-rho*md*(k/4-1).

On the explicit all-dimensional diagonal m=2^(b+k+4),rho*md=16 and

E[4I-CE]-U <22+b*2^-b-4k.

In particular b>=5,k>=8 gives reserve<-9, even though ALL irrelevant source coordinates are cleaned and all remaining source bits are essential. Let b=k=t>=8: the reserve tends to minus infinity while the ACTUAL outer neighboring-q disagreement is p/2<2^-t/4, which tends to0. The source condition mu<1/8 holds on this diagonal because (1-d)^m<=1/(1+md),md=2^(b+4)>7 (elementary Bernoulli inequality).

The initial full root is genuinely eligible. The stage21 root proof requires only H(G)<=4I(G), not its every-restriction contract: CE_root<=H(h)/2+7/2; H(h)<=h2(2p)+2p(b+2)+(rho/2)H(G);4I_root=6+2bp+rho I(G). Hence4I_root-CE_root>19/8 by b>=5,p<1/64,h2(1/32)<1/4. Original U remains untouched. This is the same balanced hierarchy throughout, not numerical constants transplanted from the older one-balanced ghost example.

The full inherited CE has the same exact leading source debt. At source-empty rows the original core vacuum is at least rho^2(1-2mu)/8>3rho^2/32, except principal/empty rows whose reference masses are larger. Full outer reference masses on these rows are therefore at least3rho^2/512, with code length<2b+8. Thus

0<=E CE-(rho*k*md/4)<2b+8+(rho/4)(2b+7).

The exact sector formula above, not this coarse bound, supplies its leading coefficient. The true entropy is uniformly bounded: for M>0, source mean0 and entropy0 give H(core)<=h2(rho)+rho(b+2), and H(F_leaf)<=3+H(core)/2<4 for b>=5; M0 has H(F_leaf)<=3. Original root H(F)<4I(F) already follows from its positive original CE margin. This is NOT an FEI counterexample. It is a failure of arbitrary cleaned-frontier inherited-reference eligibility from an otherwise eligible root, with exact essential debt and no reference ghosts.

First unsupported universal line: an admissible useful stopping policy must avoid, bundle or fund this ESSENTIAL code-to-true mismatch, rather than only cleaning irrelevant source coordinates. A root-rate supplier is insufficient for arbitrary adaptive continuation. A continuation querying every surviving essential x does reach a paid constant-source endpoint, but the costs and allowed stopping points must be stated. Whether a necessary FEI stopping rule can choose and price such bundles from the SAME original unused owner remains open.

## Complete physical cleanup and every fixed rate

When M>0, every remaining source, padding,u,mask and gate bit is essential in F. When M=0, h=u so padding is irrelevant; reveal those remaining padding bits too, retain all their identical physical children, and marginalize the ORIGINAL reference. Its influence remains6/4. The nonempty-source sector was absent at M0 and is unaffected on all M>0 leaves, so its exact averaged lower bound survives this extra cleanup. Thus the negative reserve holds even when EVERY remaining physical coordinate at EVERY leaf is essential. No reference-only ghost is used to prove the failure. The coarse full-cost remainder bound also survives, because marginalization only increases each reference mass relative to its constituents and removes zero-influence bits.

More generally, on b=k=t>=8,m=2^(2t+4), the complete expected physical influence satisfies
E I=(22+(t-1)2^-t*pi)/4<6,
while E CE>=4t. The original root is rate4 eligible, so it is rateK eligible for every real K>=4. For EVERY FIXED K>=4 the fully cleaned frontier obeys

E[K I-CE]-U <6K-4t -> minus infinity.

All root and leaf functions here are actual Boolean functions. The conclusion is a no-go for EVERY-prefix inherited-reference eligibility from root rateK alone, for any finite K>=4; it is not a failure of the earlier theorem's explicitly hereditary source contract and not a disproof of FEI. Its proper target is a selected useful stopping policy with a full paid bundle, rather than arbitrary clean stopping.

## A necessary completion fraction

After the control/cleanup frontier, allow ANY further finite adaptive policy querying the surviving source output bits only, leaving padding,u,mask,gate untouched. Let L be the final number of surviving unqueried output bits. At each physical leaf with L>0 the true source is a signed character and its SAME original source reference gives the full active set mass d^L. Hence its nonempty-source outer CE is at least rho*k*L/4. When L0 the source is constant+1 or-1 and this sector is absent. All influences satisfy

4I_F=6+2(b-1)a+rho*L-sigma*a <=6+2b*rho+rho*L,

where a=rho/2 if L>0, and a is0 orrho at L0. Both constants and either q sign are covered. Full physical averaging and nonnegativity of every omitted CE term and old U give, for each K>=4,

E[K I-CE]-U <= K(6+2b*rho)/4 -rho*(k-K)E L/4.

If k>K, any such continuation that restores NONNEGATIVE expected original reserve must therefore satisfy

E L <= K(6+2b*rho)/(rho*(k-K)).

On the diagonal rho*md=16, the expected fraction of original surviving outputs that it may leave unqueried is at most

E L/(md) <= K(6+2b*rho)/(16*(k-K)).

Thus for every fixed K it must reveal all but O(1/k) of the surviving essential outputs in expectation. This is a necessary condition, not a sufficient stopping theorem or a claimed query-KL payment. It shows why a bounded extra-query repair cannot universalize the old cleanup policy: the necessary completion bundle itself grows with dimension. The shortest NEXT is to price a USEFUL policy's essential completion bundle from the ORIGINAL owner, rather than extending the already closed ghost-cleanup cases.

## Exact KL interpretation

Before removing inactive x ghosts the source CE is kM-(m-M)log2(1-d). Thus its exact average cleanup release is m(1-d)log2(1/(1-d))<2md, whereas the essential cost left behind is kmd. Every cleaned source character has actual Fourier entropy0, so the remaining kM is entirely KL mismatch. A true-entropy FEI bound for the regular point gate and its restrictions does not bound that original-reference KL term.

The complete full-leaf KL divergence has the same leading coefficient as CE, since its true entropy is<4. After complete physical cleanup,

-4<E KL-rho*k*md/4<2b+8+(rho/4)(2b+7).

This is a uniform-in-m remainder for every b>=5,k>=5 with (1-d)^m<1/8, not a floating asymptotic fit. On the diagonal b=k=t its leading term is4t. The debt is essential code-to-true mismatch even though the true spectra have bounded entropy. The chosen bad frontier is a permitted physical continuation; it is NOT asserted necessary for every possible FEI stopping policy, which may avoid it or complete proper blocks before admission.
