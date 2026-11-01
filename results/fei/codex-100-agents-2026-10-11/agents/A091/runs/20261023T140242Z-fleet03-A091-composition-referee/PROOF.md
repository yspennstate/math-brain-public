# Independent composition review, stage21

## Exact generic escrow identity
Let F=K(Z)+C(Z)g(Y), with disjoint finite uniform cubes, C indicator of density t, K=0 on C and a sign off C. With mu=Eg, p_T=ghat(T)^2, and eta(a)=-a log2(a), the empty-core amplitudes are Khat+mu Chat. Every nonempty-core amplitude is Chat(s)ghat(T). Thus
E=H(F)-tH(g)=sum_s eta((Khat+mu Chat)^2)-t eta(mu^2)+(1-mu^2)sum_s eta(Chat^2).
The core spectral marginal is (1-t)delta_empty+t p because sum Khat Chat=E(KC)=0. Mixture entropy bounds and conditional exterior entropy give 0<=E<=m+h2(t), including t=0,1 and mu=0,+/-1. Spectral interference and arbitrary exterior/core biases are retained exactly; independence refers to physical input cubes, not spectra.

## Same original owner and old debits
For paired bent b on m divisible by4, C the all-one point and fresh nonempty tag character, b(all-one)=+1. Balance of the tag makes each original exterior influence 1/2-c, c=2^-m. Hence B0=4I_ext=2m-4mc. A specified old physical core query costs d_old=c D_iH(G)<=2c, retaining both full restrictions. The tag leaves the new core mean zero and entropy H(G_a); E_start is therefore independent of the answer. Allocate L0=B0-d_old-E_start and B=L0+E_current, never a descendant influence owner.
For frozen G, A=tH(G) is harmonic under exterior queries and unchanged under tag queries, including the final tag. Therefore D_iH(F)=E_parent-average(E_child) and B satisfies the exact local debit identity. Child innovations E_child-average(E_child) have conditional mean zero and can increase a child's allocation. This is an expected-resource ledger; it does NOT assert A057's stronger cash-only bookkeeping.

## Additional physical core queries
At current density t, inherited core G and L, a core query changes A by a=tD_iH(G), 0<=a<=2t. Set L_child=L-a equally in both actual children; recompute their actual means and E. Then B_parent-average(B_child)=D_iH(F) exactly. Exterior/tag queries leave L unchanged. This includes core queries after the last tag, when current means genuinely change.
The bound h2(c)<=cm+c/ln2<=11/32 gives L0>=3m/4-15/32. At most m/4 additional core queries per path spend at most m/2; hence L>=m/4-15/32>=m/8 for m>=4. Alternatively admit each next core query only if current L-2t>=m/8. All old costs remain booked, the reserve is never renewed, and every full terminal has B=L+E>=m/8. Local identities telescope to Hroot=B0+E_leaf(Hleaf-Bleaf), for all finite adaptive admitted physical trees. Analytic induction supplies the arbitrary-policy scope.

## Exterior-only obstruction
For G_N a product of N disjoint AND2 signs, H(G_N)=2N and I(G_N)=N exactly. Keeping tag and exterior unqueried, all core revelations cost 2cN, with full terminal entropy E_start unchanged. The first AND2 query has positive cost2c. For N=m*2^m-2m+1, 2cN-B0=2c>0. Thus an original exterior-only owner with nonnegative terminal allocations cannot fund arbitrary core continuation. This is not an FEI counterexample: original physical core influence equals cN.

## Independent A057 full-exterior cash proof
A coordinate with influence d has erasure at most h2(d) and JS at most2min(d,1-d)/ln2. A first original-pair query costs at most2, giving at most m per path. A second partner after mask death is a literal or dummy factor and costs0. On a surviving mask branch with n exterior variables, its base derivative is1 and 1-d=t(1-Eh)<=2t, t=2^-n. For n>=2 its cost is at most2^(1-n)(n+4); n=1 costs at most2. Summing over distinct n yields2+3+4=9. Proper tags cost0, and their sole final query costs at most2. Thus spent-or-pending tag plus old debit plus exterior costs is at most2c+m+11. Original cash is at least B0-2c-m-11>=m/4 for m>=16 divisible by4. This argument is pathwise and does not require an influence floor for the low-influence tag block.
The retained-log coherent bound T(t,q)=t[q log2(1/t)+q log2(1/q)+(9/2)q] follows from erasure Jensen and JS<=2tq/ln2. U=min(T,2) remains concave in t for fixed q. It is a current earmark within the same cash, not a renewed grant. Exact full terminals and arbitrary residual G entropy are retained in both reviews.

## First unsupported line
A necessary next core query after actual admitted L is exhausted still requires a noncircular original core resource or an actual Booleanity refund. Neither reviewed source supplies it; the exterior-only unlimited substitute is explicitly false. No full FEI proof follows.

## Scalar coherent bound reconstructed independently
For a real amplitude pair u,v, put w=u^2+v^2 and r=2uv/w (zero pair contributes0). Its JS in natural units is w*F(r), F(r)=[(1+r)ln(1+r)+(1-r)ln(1-r)]/2. Both sides are even, and for r>=0 the derivative difference of r/sqrt(1-r^2) and atanh(r) is (1-r^2)^(-3/2)-(1-r^2)^(-1)>=0. Integrating twice from0 yields F(r)<=1-sqrt(1-r^2). Thus JS_bits<=2min(u^2,v^2)/ln2. At the last tag only empty-core pairs contribute; their second squared mass is t*q, so JS<=2tq/ln2. Erasure satisfies Phi(a,b)<=b[1+ln(1+a/b)]/ln2 since a ln(1+b/a)<=b. Weighted Jensen with b=q*Chat^2 and total mass tq yields L<=tq[log2(1/t)+log2(1/q)+1/ln2]. Together this proves T with coefficient9/2 because ln2>2/3. All zero endpoints follow by continuity or literal zero packets.
