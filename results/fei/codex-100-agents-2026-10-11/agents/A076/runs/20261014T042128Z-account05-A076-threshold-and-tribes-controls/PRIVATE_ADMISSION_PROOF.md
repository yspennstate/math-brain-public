# Private-query admission from one marked selector account

Inputs are independent uniform bits, signs use the Walsh basis, and entropy
is in bits. Let F select G(y) when z=0 and H(y) when z=1, where z is a fresh
selector and G,H may share arbitrary remaining data. At the queried data
coordinate i assume H is independent of i. Let d=Inf_i(G),
delta=Pr[G!=H]=Inf_z(F), and B_i denote conditional spectral erasure.

## 1. A scalar comparison with a retained quarter

Put Phi(p,q)=(p+q)h2(q/(p+q)) with continuous zero boundaries. For fixed
q>=0, f(p)=Phi(p,q) is increasing, concave, f(0)=0, and hence subadditive.
For c>=1, f(cp)<=f(p)+q log2(c): integrate f'(p)=log2(1+q/p)
and use ln(1+t)<=t. At p=0 the same inequality follows directly.

For arbitrary real u,v,a put e=u-v, q=a^2. Since
(u+v)^2=(2u-e)^2<=8u^2+2e^2, these facts give

Phi((u+v)^2,q)<=Phi(u^2,q)+Phi(e^2,q)+4q.

Adding Phi((u-v)^2,q)=Phi(e^2,q) proves the upper half of

0 <= Phi((u+v)^2,q)+Phi((u-v)^2,q)-Phi(u^2,q)
  <= 4q+2Phi(e^2,q).                                      (1)

For the lower half, max(|u+v|,|u-v|)>=|u| and Phi is increasing in its
first argument. No restriction on signs, relative sizes or spectral support
is used. These scalar bounds are not the former quarter-power L surrogate.

## 2. Actual private-query spectrum and influence price

For residual Fourier sets T not containing i let u_T=Ghat(T),
a_T=Ghat(T+i), v_T=Hhat(T). Hhat(T+i)=0 by the physical hypothesis.
The two actual selector-frequency pairs are (u_T+v_T,a_T)/2 and
(u_T-v_T,a_T)/2, so

B_i(F)=sum_T[Phi((u_T+v_T)^2,a_T^2)
                   +Phi((u_T-v_T)^2,a_T^2)]/4,
Inf_i(F)=d/2.                                            (2)

Define the nonnegative admission remainder A_i=B_i(F)-B_i(G)/4. From (1),
homogeneous concavity/log-sum, and Parseval,

0<=A_i<=d+Phi(E,d)/2, E=sum_T(u_T-v_T)^2=4delta-d.         (3)

The identity for E is simply ||G-H||_2^2=4delta after decomposing into
the mean and i-derivative sectors. Booleanity and H's independence give
d<=2delta: on every pivotal i-edge exactly one endpoint disagrees with H.
Nonpivotal disagreeing edges can only increase delta. Therefore
d/(4delta)<=1/2 when delta>0. Using Phi(E,d)<=E+d=4delta gives

             B_i(G)/4 <= B_i(F) <= B_i(G)/4+4delta.       (4)

At delta=0, G=H is independent of i, and all terms are zero. Formula (3)
is the sharper profile bound; (4) spends at most four of a named actual
selector influence. In the earlier signed notation D_i=B_i(F)-B_i(G)/2,
this proves D_i<=4delta-B_i(G)/4. It does not bound |D_i| by delta.

Both arbitrary biased cores and every coherent residual row, including
the empty row, are present. No common activation or derivative gap is
assumed. Conditional descendants obey the same theorem whenever the
queried coordinate is absent from one current branch.

## 3. Antichain ownership under arbitrary earlier data exposure

Keep z unqueried. Under any adaptive data restrictions,
delta_v=Pr[G_v!=H_v] is the physical conditional expectation of the fixed
disagreement indicator. Thus delta_v is a nonnegative martingale.
Let V be any antichain of data-query nodes, meaning each root-to-leaf
path meets at most one selected node, and suppose the selected query i_v
is private to one current branch. Exchange G,H where necessary, and call
the branch containing i_v K_v. The actual reach weights w_v satisfy

sum_(v in V) w_v delta_v <= delta_root,
sum_(v in V) w_v [B_i(F_v)-B_i(K_v)/4]
                    <=4 delta_root.                      (5)

This is one marked selector account, not a fresh allowance at each depth.
The unsampled paths retain the unused conditional account. In particular
all nodes querying one fixed private coordinate form such an antichain,
even with arbitrary adaptive shared-data or activation-control queries
before it. For A077's common-activated bent/spike family, delta_root=q*c,
so all weighted private-x exposure remainders cost <=4q*c for every k,r,
despite the unbounded local remainder/Inf_x and absence of a derivative gap.

This accounts for the first private collision. Spending the same 4delta
again on a second incomparable time layer is not licensed. Nor is the
selector's own future erasure or entropy decrement paid by (5).

## 4. The retained quarter is optimal

For even k>=2 let N=2^k, a=1/N, b=1/sqrt(N), h(s) be the tensor quadratic
bent sign with h(0)=1, and let G(s,x)=h(s)[1-2*1{s=0,x=0}], H(s,x)=h(s).
These are actual Boolean branches. The private x query has u_T=hhat(T)-a,
a_T=-a, v_T=hhat(T)=+b or -b; d=a and delta=a/2. Hence exactly

B_x(G)=sum_T Phi((hhat(T)-a)^2,a^2),
B_x(F)=sum_T[Phi((2hhat(T)-a)^2,a^2)+2a^2]/4.             (6)

Because b>=a, |2hhat(T)-a|>=|hhat(T)-a|. Consequently
B_x(F)>=B_x(G)/4+a/2. Also Phi(p,q)>=q log2(p/q) yields

B_x(G)>=a log2((sqrt(N)-1)^2)>=a(k-2).                   (7)

For any c<1/4, (B_x(F)-c B_x(G))/delta >=
2(1/4-c)(k-2)+1, which diverges. Thus no inequality
B_i(F)<=c B_i(G)+K Inf_z(F) can hold for all these actual Boolean functions
with c<1/4 and fixed finite K. The coefficient 1/4 in (4) is sharp; the
constant four on the selector reserve is not claimed sharp. This is a
transport lower bound, not an FEI counterexample; all physical influences
and both terminal core spectra must still be counted.

The full physical influence ledger is explicit: each shared influence of
G is 1/2+a, that of H is 1/2, and that of F is 1/2+a/2. At the edited
vertex all quadratic neighbors had the same sign, so the edit adds one
formerly nonpivotal edge in every original G coordinate. Thus
I(G)=k/2+(k+1)a, I(H)=k/2,
I(F)=k/2+(k+2)a/2, with Inf_x(F)=Inf_z(F)=a/2.
This sharpness test does not hide the shared quadratic influence.

## 5. Why the selector account cannot be reset

For any integer m>=1 let G=y*product_(j=1..m)(-1)^(a_j b_j), H=1,
with y a fresh literal, all a_j,b_j private data, and z the fresh selector.
Keep y unqueried and expose a_1,...,a_m first. At every reached node the
unqueried literal forces E G=Ghat({a_j})=0. Tensor factorization of the
remaining two-bit quadratic gives B_(a_j)(G)=1 and Inf_(a_j)(G)=1/2.
The shifted empty-row correction is zero, so

B_(a_j)(F)=1/2, A_(a_j)=1/4, Inf_(a_j)(F)=1/4,
delta_v=1/2 at every such node.

Therefore the expected m-query prefix has

sum w A_i=m/4, delta_root=1/2, consumed influence=m/4.    (8)

No finite K can bound sum w A_i<=K delta_root for arbitrary repeated
private-query layers. This proves the antichain/one-mark qualification is
necessary for a selector-only reserve. The example does not refute payment
using consumed physical core influence: here it pays A exactly at rate one.

Full costs are explicit: I(G)=m+1, I(F)=m/2+1, H(G)=2m,
H(F)=m+2=2I(F). After the prefix the actual G leaf is a character containing
y and those b_j whose revealed a_j=1. Hence E H(F_leaf)=2 and
E I(F_leaf)=1+m/4, exactly matching the removed influence m/4.
The prefix has actual B=m/2 and JS=m/2, giving entropy decrement m.
This is an exact ownership obstruction, not a search for Q/I growth or FEI
failure. It is consistent with the board's separate common-factor reserve
warnings; no general new claim about those different ledgers is made.

## 6. Full terminal law and the exact universal gap

For arbitrary leaves put R(G,H)=H(F)-[H(G)+H(H)]/2, evaluated from the
actual paired coefficient vectors. Precisely,
R=sum_S[phi((ghat_S+hhat_S)^2/4)+phi((ghat_S-hhat_S)^2/4)
                         -phi(ghat_S^2)/2-phi(hhat_S^2)/2].
Thus E H(F_leaf)=E[H(G_leaf)+H(H_leaf)]/2+E R_leaf.
Querying z at a leaf leaves exactly the half-sum core entropy; its actual
decrement R is not assumed paid by the marked private-query account.

For precision about the next target, consider balanced arbitrary G, H=1,
and complete core-only trees T, leaving the selector to the end. Put
Pi=I(G)/2 and A_T=sum w[B_i(F)-B_i(G)/4]. The proposition
"there is a uniform K such that every balanced G admits one such tree with
A_T<=K Pi" is FEI-strength, not a completed cheap core estimate.
Indeed JS_i<=c Inf_i, c=2/ln2, follows from
[(1+t)ln(1+t)+(1-t)ln(1-t)]/2<=1-sqrt(1-t^2); differentiate the difference
to obtain t/sqrt(1-t^2)-atanh(t)>=0. Entropy telescoping then gives

A_T>=H(F)-cPi-H(G)/4=H(G)/4+2-cPi.

Thus such a K gives H(G)<=2(K+c)I(G)-8 for balanced G. For arbitrary f,
apply this to G=y*product_(j=1..m)f_j on disjoint inputs. Its H=mH(f),
I=1+mI(f), so m->infinity gives full FEI with C=2K+4/ln2.
Conversely FEI(C) gives A_T<=B_T(F)<=H(F)=H(G)/2+2
<=(C+4)Pi for every such tree, since balanced G has I(G)>=Var(G)=1.
This equivalence only guards the scope of the remaining combined account;
it is not counted as progress toward bounding K.

The selector-only repeated extension is now refuted by (8). The first
unsupported universal line is paying repeated private collisions with a
combined, nonreused selector/core-child account, or paying a genuinely shared
data query, while retaining all arbitrary terminal core entropy. NEXT should
combine the quarter inherited-erasure reduction with an actual certified child
surplus at the second collision. It must use the same original selector account
and only unspent physical core influence. Full FEI and C018/C019 remain OPEN.
