# An inherited nonflat fallback through one density-lowering exposure

All entropies are bits. Validation is initially pending; the final report records its outcome. Full FEI remains OPEN.

## 1. Actual functions and original account

Let m>=4 be even, c=2^-m, and b on m independent bits be the paired quadratic bent sign, with b(0)=1 and E b=sqrt(c). Put C=1_{x=0}. Let g on a disjoint cube be ANY Boolean function of mean mu, including an inherited nonflat fallback after compatible actual restrictions. Let X be a fresh fair physical bit. Define the actual function

W(0,x,y)=g(y),   W(1,x,y)=b(x)-C(x)+C(x)g(y).

The SAME physical g occurs in both children. Its parent exterior density is a=(1+c)/2; after X=1 it is c, and after X=0 it is1. Both complete child functions and every subsequent terminal are retained.

The actual source influence is

d_X=[1-c-mu(sqrt(c)-c)]/2.                              (1)

Indeed the two children differ only off C, and the mismatch indicator for g and b is (1-gb)/2 there. Independence gives E[(1-C)gb]=mu(Eb-c). Because sqrt(c)-c>=0, mu<=1 and sqrt(c)<=1/4,

d_X >=(1-sqrt(c))/2 >=3/8.                            (2)

Also d_X<=(1+sqrt(c)-2c)/2<=9/16: t ->(1+t-2t^2)/2 is increasing for0<=t<=1/4. Thus d_X is never divided by zero. This source disagreement is actual; it is not replaced by the fair-g formula (1-c)/2.

At ANY Boolean physical split the full decrement D_X=H(W)-[H(W_0)+H(W_1)]/2 lies in[0,2]. To check this, write its exact decomposition into spectral erasure of the queried bit (at most one bit) plus the Jensen-Shannon divergence of the two actual child spectra (between0 and1). Both children have normalized squared spectra by Boolean Parseval. No child entropy is omitted.

Freeze the original source account B0=6d_X. Book the ACTUAL D_X first, leaving B1=6d_X-D_X. The account is not restarted when density changes.

## 2. One descendant query, or a stopped continuation of influence at most one

At a specified physical coordinate i of g let delta_i=Inf_i(g), so0<=delta_i<=1. In the X=1 child its actual influence is c delta_i. The retained all-density wrapper theorem's EXTRA logarithmic charge, with original root reach1/2, is

T_i=(c/2)delta_i log2(1/c)=(mc/2)delta_i<=1/8.         (3)

The bound m2^-m<=1/4 for integer m>=4 follows from its value at4 and ratio (m+1)/(2m)<=1 thereafter. No Fourier-flatness or balance of g is used. From (2), D_X<=2 and (3),

D_X+T_i <=17/8 <=(17/3)d_X,
B1-T_i >=d_X/3 >0.                                  (4)

Thus the SAME source rate6 pays the actual source decrement and this new rare-density charge for arbitrary inherited nonflat g. This is stronger than merely importing a fresh descendant allowance. Relative to A060's fair-g remainder>7d_X/30, the new bound uses the sharper absolute tax<=1/8; the geometry is broader and the arithmetic bound is different.

More generally let an arbitrary finite stopped physical query tree on the rare g branch consume conditional controller influence L=sum_v w_v Inf_{i_v}(g_v). Compatible restrictions preserve the fixed exterior density c. Its extra logarithmic bill is EXACTLY

T_tree=(mc/2)L.                                      (5)

Whenever L<=1, the same source account and residual (4) apply. This allows adaptive choices and nonflat core-data interruptions if only the indicated controller tax is charged here; ordinary data/source costs and the20-times-influence base price remain separate. An upper bound on L is a stated hypothesis, never inferred from the number of syntactic gates or from a single-coordinate bound.

If g is represented as a private priority list of disjoint fine Boolean cores h_j with probabilities p_j, let Vbar=sum p_j Var(h_j). Its original merged masses at the source are a p_j, and its actual child masses are p_j and c p_j. Any exterior labels are constants and have variance zero. For phi(t)=t log2(1/t), the SAME original fine reserve releases

kappa_X=[phi(a)-phi(c)/2]Vbar>=0.                     (6)

To prove it, expand phi(a p)=a phi(p)+p phi(a) in parent and both children; all phi(p) terms cancel because a=(1+c)/2. Concavity of phi at1,c gives the sign. U=sum p_label[H(h)-phi((Eh)^2)] is harmonic at X. This holds even if Vbar>0 or g has biased and nonflat cores. We book D_X itself, so none of (6) is used as a second subsidy. The actual residual child U/R and both H-U-R terminals are carried unchanged.

For one controller query whose imported all-density base price is20 and whose original fine release is kappa_i(g), a literal two-query telescope consequently gives

H(W)-E H(actual X/i terminals)
 <=6d_X +20[(delta_0+c delta_1)/2]
          +kappa_X+[kappa_0+c kappa_1]/2,

provided the imported local query bound applies in each chosen child and0<=delta_1<=1. The reserve terms are drops of one account, not new allocations. This displayed consequence is conditional on that previously stated local wrapper bound; the source-budget inequality (4) is self-contained. Arbitrary terminal entropy, the20 base price and inherited core entropy have NOT been paid by (4).

## 3. Why the source account cannot pay an unrestricted whole continuation

There is an actual Boolean family refuting the assertion that the account6d_X alone pays ALL descendant density-log charges for every inherited private priority fallback. This is an obstruction to that helper, not to FEI or to the local wrapper inequality.

Fix the exterior m=4, hence c=1/16. For integer r>=48 put k=2^r and let g_r be+1 if any of k independent r-bit blocks equals zero, and-1 otherwise. This is a private point-priority list with selected/default constant fine cores. Thus its ORIGINAL fine U=R=0 at source and throughout every restriction. It is not spectrally flat: its mean is1-2(1-1/k)^k, which is nonzero, and the spectrum contains different coefficient magnitudes. All its r k coordinates have influence (2/k)(1-1/k)^{k-1}, so

I(g_r)=2r(1-1/k)^{k-1}>2r/3.                         (7)

For completeness, ln(1-t)>=-t/(1-t) for0<=t<1 follows by integrating1/(1-s)<=1/(1-t) over0<=s<=t. With t=1/k it yields (k-1)ln(1-1/k)>=-1. Hence the power is>=exp(-1)>1/3. The last strict inequality follows from exp(1)<3: sum_{j=0}^2 1/j!=5/2, and the tail is at most (1/6)/(1-1/4)=2/9. There is no limiting argument or floating sign.

On ANY complete actual physical query tree for g_r, influence conservation gives L=I(g_r). Its root-weighted descendant density tax is therefore

T_all=I(g_r)/8>r/12>=4,
while B0=6d_X<=27/8<4.                              (8)

Thus the density tax already exceeds the entire original source account, even BEFORE the actual old D_X is booked. The gap grows at least linearly in r. The full terminals of the rare/frequent exterior branches remain actual; U/R never supplied hidden funds because every fine core is constant. These finite, if extremely large, Boolean functions are defined exactly; no giant truth table is constructed or claimed exhausted. The analytic proof handles all r>=48.

The needed repair is to transfer genuinely unused INTERNAL g influence capacity, with its prior debits, into the rare branch's logarithmic bill, or to prove a policy keeping L within the paid budget. Assigning another6d_X at each descendant, or calling L<=1 without proof, would repeat the obstruction. Section4 supplies a scoped version of the first repair.

## 4. The SAME unused internal ticket pays arbitrary subsequent continuations

Now let g be any private point-priority list with disjoint fine-core cubes and constant default, as required by the imported A059/A060 local controller bounds. Assume exterior bent bits stay unqueried. Arbitrary internal core-data/controller histories before the source X exposure are permitted. At a reached hidden-X state retain the SAME original fine U/R and define its remaining internal ticket

Q_hidden=a[21 I_ctrl(g)+5 I_data(g)],  a=(1+c)/2.

Here I_ctrl and I_data are influences on the actual residual internal controller/data blocks. This ticket must be the remaining allocation from the original ancestor account after its previous booked costs. It is not assigned as an extra budget at the exposure. The old frequent-wrapper bound (<21 per controller influence), and the signed data price3/ln2<5, maintain it under every earlier internal query. Physical block influence has exact fair drift: it decreases by the queried influence when a bit in that block is queried, and has zero expected drift otherwise. Thus unused Q_hidden follows from the original ticket by induction, including adaptive histories.

At X replace its ticket by the two ACTUAL child allocations

Q_0=20 I_ctrl(g)+5 I_data(g),
Q_1=c[(20+m) I_ctrl(g)+5 I_data(g)].

The all-density local price is<20+log2(1/c)=20+m in the rare child; at density1 it is<20. The allocation identity is EXACT:

Q_hidden-(Q_0+Q_1)/2
 =[a-mc/2] I_ctrl(g)
 =[1-(m-1)c] I_ctrl(g)/2
 >=(13/32) I_ctrl(g)>=0.                             (9)

The last bound uses (m-1)2^-m<=3/16 for integers m>=4, proved by its value at4 and successive ratio m/[2(m-1)]<=1. Thus the entire rare-child logarithmic tax for an UNRESTRICTED subsequent internal stopping tree is funded from the SAME unused incoming internal capacity. It is not also charged to the source bank in Section2. Choose one funding route for each bill. The independent source bank books only the ACTUAL D_X and leaves6d_X-D_X>=(2/3)d_X; (6) is not counted as extra cash.

After X, keep the allocated rate20 or20+m on its actual child; all subsequent controller/data query debits are paid by its influence drift, with unchanged fine U/R. The original terminal H-U-R remains, and the remaining Q at each terminal is also retained as unused capacity. No favorable terminal is discarded to subsidize its sibling. This works for arbitrary adaptive policies of the internal controls and fine data, with arbitrary stopping, while the exterior bits remain unqueried.

More explicitly, let Q_v be the above actual phase-dependent ticket on every leaf/state. On any finite policy that queries only internal variables, optionally exposes X once at a stopping frontier, and then continues internally, the same-root ledger gives

H(W_root) <= U_root+R_root+Q_root+6 Inf_X(W_root)
          +E[H_leaf-U_leaf-R_leaf-Q_leaf-6 Inf_X(W_leaf)]. (10)

At a hidden-X internal node, the imported local payment is at most drop(U+R+Q). At an X query it is at most that drop plus6d_X, since U is harmonic, R release and (9) are nonnegative, and D_X<=6d_X. At an exposed-X internal node, the chosen actual child rate prices the same signed local remainder. Weight and telescope on the SAME physical tree. Physical block-influence conservation gives the sum of reached X-query influences equal to Inf_X(W_root)-E Inf_X(W_leaf), with source influence0 after X is exposed. Thus source ticket6 is assigned once and its unused terminal amount is returned explicitly. Formula(10) retains both complete actual terminal profiles and all old debits.

The source-dependent continuation statement relies on A059's local frequent-wrapper/signed-data/last-frequency inputs and A060's all-c local bound. It does not prove a universal reference bank. It specifically removes the fair-g assumption from A060 Section5 and pays arbitrary further internal continuations using unused original internal capacity. The source-only counterexample in Section3 explains why that second capacity is necessary.

The next unpaid step is ONE exterior bent-data query after Q_0/Q_1 have been allocated and some internal costs booked: it changes the actual C/K0 profiles and can lower or kill density. Its charge and new child rates must fit the SAME diminished ticket, with both terminal profiles, rather than invoking a new density-root allowance. Inherited U and exterior bent terminal entropy remain unpaid universally.
