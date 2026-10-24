# All-parameter minimal reserve on the canonical B05 tree

This is a new continuation of the completed compensator, not a new proof of the telescope. All entropy units are bits and all influences are ordinary. Fix any C>=6 (in particular C=6 or the lead's exact price 32609/5000=6.5218). For any node v of the specified physical tree let

Q*_v=max(0,D_v-C d_v+(Q*_{v0}+Q*_{v1})/2),

with zero constant leaves. This is the least nonnegative reserve for D<=Cd+Q-EQ_child. Define physical output minority mu(g)=min(P[g=-1],P[g=+1]) and psi(mu)=mu log_2(1/mu), with psi(0)=0.

The actual Boolean family is b_k(x)=(-1)^{x_1x_2+...+x_{k-1}x_k}, b'_k=b_k-2 1_{x=0}, k>=4 even. Let p=2^{-r}, r>=2k, and G=1+A_r(b_k-1), H=1+A_r(b'_k-1), F select G or H using a fresh fair physical selector. The complete tree reveals selector, then controls in increasing label order, then data in adjacent pair order. It omits irrelevant inputs and ends at constants. Binary bits here mean uniform input signs converted by x_i=(1-X_i)/2.

## Claim

On this complete tree, Q*_v<=4 psi(mu(g_v)) at every reached node. More sharply, all control nodes and all even paired data states have zero reserve, and

Q*_root=[D_selector-Cp2^{-k}]_+ <=4*2^{-k} psi(mu(F)) <=psi(mu(F))/4.

The only other possible positive reserves lie at odd point-edited data states (the unmatched partner of a quadratic pair). Their reserve is at most two bits and is canceled in expectation at the preceding paired query. This bounds the exact minimal reserve, retaining all data descendants; it is stronger than a root FEI certificate and different from the false assertion that 4 psi(mu) itself satisfies the local drift inequality.

## 1. Every fresh activation-control split is paid at rate 6

For any Boolean core h let a=1-Eh in [0,2]. At an active s-control node (s>=1), set u=2^{-s}, x=ua and d=x. Fourier coefficients at empty data are 1-x at the empty control set and -x at every nonempty control set; at nonempty data T they are u hhat(T) at every control frequency. Along any remaining control query the conditional spectral erasure is exactly

B=2x-2x^2+Phi((1-x)^2,x^2),

where Phi(R,S)=(R+S)h_2(S/(R+S)). This includes the changed empty-data coefficient in EVERY control fiber, as A089 corrected. In fact B<=3d for all x in [0,1]. For x>=1/4, the binary entropy bound h_2(t)<=2 sqrt(t(1-t)) gives Phi((1-x)^2,x^2)<=2x(1-x)<=x+2x^2. For x<=1/4, the logarithmic bound Phi(R,S)<=S log_2(e(R+S)/S), and R+S<=1, gives Phi<=x^2 log_2(e/x^2). The function f(x)=1+2x-x log_2(e/x^2) has f'(x)=2+log_2(e)-2log_2(1/x)<0 on (0,1/4]; at 1/4 it is (2-log_2(e))/4>0. Thus Phi<=x+2x^2 also in this range, which proves B<=3x. The singleton JS bound J<=2d/ln2<3d now yields D<6d when d>0, with zero-cost endpoints treated directly. This covers negative means and endpoints x=0,1 as well.

For completeness, the binary entropy bound has a one-variable calculus proof. Put z=|1-2t|. The difference sqrt(1-z^2)-h_2((1+z)/2) vanishes at z=0 and z=1. Its derivative has the sign of R(z)-ln2, where R(z)=atanh(z)sqrt(1-z^2)/z. A direct derivative gives R'(z)=(z-atanh(z))/(z^2 sqrt(1-z^2))<0 for 0<z<1. Thus R falls from 1 to 0, the difference first increases then decreases, and stays nonnegative. Only this elementary inequality and the previously accepted JS bound are used in this control estimate; no biased-uncertainty theorem is needed.

## 2. Clean quadratic data states have zero reserve

A product of independent quadratic two-bit factors and coordinate characters, with dummy variables, has reserve zero under adjacent pair order for C>=4. Querying the first variable of a quadratic pair has d=1/2 and D=2: its children lose that factor and retain either a dummy or a character on its mate. Querying a pure character has d=1 and D=0. Dummy inputs are skipped. Thus each reached clean node is locally paid and the assertion follows backward from constant leaves. This includes every branch where a data bit set to one destroys the point edit.

## 3. Point-edited pair states: nonlocal cancellation

Let E_t=b_t-2 1_0 for even t, and E_0=-1. For t>=4, its first data query has children

O_{t-1}(z,w)=b_{t-2}(w)-2 1_{z=0,w=0},

and a clean character times b_{t-2}. At O, the next query is the unmatched partner z; its children are E_{t-2} and b_{t-2}. No other point-edited state is produced in this order.

Flatness of b_t gives maximum squared Fourier coefficient of E_t at most (2^{-t/2}+2^{1-t})^2. Consequently H(E_t)>=t-2 log_2(1+2^{1-t/2})>=t-2 for even t>=2. For t=2, E_2 is minus a two-bit parity and has entropy zero; all its descendants have zero reserve.

We need the stronger lower bound H(E_t)>=t-1 for even t>=4. Let delta_t=2^{-t}, alpha_t=sqrt(delta_t), and write the bent coefficient as sigma_T alpha_t. The edited probabilities are delta_t(1-4sigma_T alpha_t+4delta_t); the average of sigma_T over all indices is alpha_t, since b_t(0)=1. Direct squaring gives chi^2(p_edited || uniform)=16delta_t(1-delta_t)<1 for t>=4. Jensen under p_edited gives its KL divergence to uniform at most log_2(1+chi^2)<1. Hence H(E_t)>t-1. This is a proved entropy bound, not a floating-point estimate.

Inductively assume Q*(E_{t-2})=0. If t=4, average child entropy at O is at least t-3=1 (E_2 is a character and has entropy zero); its own entropy is at most t-1=3. Hence D_O<=2 and Q*(O)<=2. Since H(O)>=average child entropy, the clean child's entropy t-2 and H(E_t)<=t give

D_E <=5/2.

The first query influence of E_t is exactly 1/2+2^{1-t}, from changing all t zero-vertex boundary edges. At t=4,

D_E-6d_E+Q*(O)/2 <=5/2-6(5/8)+1=-1/4<0.

For t>=6, H(E_{t-2})>=t-3 gives average odd-child entropy >=t-5/2, so D_O<=3/2 and Q*(O)<=3/2. Also H(O)>=t-5/2 gives D_E<=9/4. Therefore D_E-6d_E+Q*(O)/2<=9/4-3+3/4<=0. Thus Q*(E_t)=0 for every even t by induction, and also for any larger C by monotonicity. This is genuine adjacent-query transport: an odd child's positive reserve is absorbed by its own parent query influence once; no influence is reserved again in descendants.

For an odd state with t>=4, its physical minority is (1-alpha+alpha^2)/2 with alpha=2^{-(t-2)/2}. It lies in [3/8,1/2], and concavity of psi together with psi(1/4)=psi(1/2)=1/2 gives psi(mu)>=1/2. Thus Q*(O)<=2<=4psi(mu). All clean/even states have zero reserve. The t=2 endpoint is a character, already covered.

## 4. Activation reserve vanishes and selector reserve is exact

Both core trees end in zero reserve by parts 2 and 3. Each activation-control node is locally paid by part 1 and has one inactive constant child. Backward induction gives zero reserve at every control node. Hence at the selector root alone,

Q*(F)=[D_selector-Cd]_+, d=p delta, delta=2^{-k}.

This is an identity for the COMPLETE tree, not a stopped approximation at b,b'. The two terminal cores and every point-edited descendant were kept.

The general one-coordinate bounds B<=h_2(d) and J<=2d/ln2 give

D_selector <=d[log_2(1/d)+3/ln2] <d(r+k+9/2),

using ln2>2/3. For every C>=6, Q*(F)<=d(r+k-3/2), which is positive as an upper bound in the stated domain. Write alpha=sqrt(delta). Direct physical averaging gives

mu(F)=p(1-alpha+delta)/2 in [3p/8,p/2].

It follows that psi(mu(F))>=3p(r+1)/8. Since r>=2k,

Q*(F)/psi(mu(F)) <=(8delta/3)(r+k-3/2)/(r+1) <4delta<=1/4.

Combining the state classification with the odd-state bound proves Q*_v<=4psi(mu(g_v)) at every node. At the root the stronger factor 4delta is available.

For r=2k and any fixed finite C>=6, the exact root reserve has the sharper asymptotic Q*(F)/I(F)~(2/5)2^{-k}. To see this directly, at nonempty data packets the selector posterior theta is delta(1+O(sqrt(delta))) and their total selector mismatch mass is (1-delta)d. Empty-data packets carry only delta d mismatch mass and contribute O(kdelta d), with the exceptional empty packet contributing O(kd^2). The binary-entropy expansion therefore gives B/d=k+log_2(e)+o(1), consistently with B05's audited section 4. Uniformly all packet theta<=4delta; writing z=2sqrt(theta(1-theta)), the JS packet is q[(1+z)ln(1+z)+(1-z)ln(1-z)]/(2ln2)=2qtheta/ln2+O(qtheta^2). Summation yields J/d=2/ln2+O(delta). Hence D/d=k+3/ln2+o(1), while I(F)/d=delta^{-1}[5k/2-2k sqrt(delta)+(3k+1)delta]. The reserve is positive eventually, so dividing [D-Cd]_+ by I proves the asymptotic. This is an explicit family asymptotic, not an optional-stopping or terminal-limit exchange.

## 5. Initial resource and terminal boundaries

The cube edge-isoperimetric inequality in this normalization is I(g)>=2mu(g)log_2(1/mu(g)). A self-contained proof follows by induction on dimension. For an event of mass a split into halves of masses a_0,a_1, induction on its internal edge boundaries plus at least |a_0-a_1| cross-edge disagreement gives I>=a_0log_2(1/a_0)+a_1log_2(1/a_1)+|a_0-a_1|. Writing a=(a_0+a_1)/2 and q=a_0/(2a), the excess over 2a log_2(1/a) is 2a[h_2(q)-1+|2q-1|]>=0, since h_2(q)>=1-|2q-1| by concavity. This induction holds for all event masses, so complementing permits use of the minority event. Base dimension zero is immediate.

Therefore Q*(F)<=2delta I(F)<=I(F)/8. The minimal reserve is itself a valid drift certificate by its Bellman definition and has zero constant leaves. At C=6, summing the already accepted influence/entropy budgets gives H(F)<=6I(F)+Q*(F)<=(6+2delta)I(F)<=49I(F)/8. This numerical class bound is secondary; the useful new interface is the exact location, cancellation and root magnitude of Q*.

## 6. Why the rarity function still fails as a universal potential

A064's no-go remains valid. At B05 selector roots, the two physical child minorities are mu +/-d/2. For fixed c, the drift c[psi(mu)-average psi(mu_children)]/d is O(c delta), while D/d grows at least (1-delta)(k-2). No fixed C,c give D<=Cd+cpsi(mu)-average cpsi(mu_child) at these roots for all k. Pointwise domination Q*<=4psi(mu) proved here must not be substituted into that drift inequality: averaging the child inequality has the wrong direction for such a substitution.

The first unsupported universal step is producing an explicit cheap candidate whose Bellman update dominates its value, or proving a dimension-independent bound on the actual Q* for a physical rule beyond this aligned point-edit geometry. The canonical pair order is essential to the cancellation proof. Overlapping or incompatible edit locations can leave two positive-reserve children and require a new ownership estimate; neither that estimate nor arbitrary-core terminal admission is proved here.
