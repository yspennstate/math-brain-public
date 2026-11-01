# Paired-query ownership with two surviving edits

All entropies are in bits. C>=6. Q denotes the complete fixed-tree minimal reserve
Q(g)=[H(g)-average H(children)-C Inf_i(g)+average Q(children)]_+,
with constant-leaf reserve zero. Queries use increasing physical coordinate order, skipping irrelevant inputs. No terminal entropy or influence is discarded.

Let b_k(x)=(-1)^(x_1 x_2+...+x_{k-1}x_k), k even. The new core is T_k obtained by flipping b_k at 0 and e_1+e_3, for k>=4. Both vertices have b_k=+1. We prove Q(T_k)=0 for every even k>=4, and prove the single-edit phase correction needed for its descendants. These extend the previous reserve proof rather than repeat its telescope.

## 1. Single-edit phase correction, all positions

An input translation sends an arbitrary edited vertex to zero and turns b_t into a sign times b_t times a coordinate character. Complementing inputs merely exchanges children and preserves the complete increasing-order tree. Output characters preserve Fourier entropy (they permute spectral labels). Accordingly the even edited entry has entropy H(E_t), E_t=b_t-2*1_0, independently of its character phase. The first-query odd edited child likewise has entropy H(O_{t-1}), where O(z,w)=b_{t-2}(w)-2*1_{z=0,w=0}. Its other child is clean, with entropy t-2. These statements concern entropy only: influences and reserves are NOT invariant under output characters.

Write a in {0,1} for the character on the unmatched mate z in the edited child. Its query influence is delta_m for a=0 and 1-delta_m for a=1, where m=t-2 and delta_m=2^-m. Its two children are a single-edited m-core and a clean m-core, with arbitrary inherited phases. At the even entry, the first influence is 1/2+2^(1-t) if a=0 and 1/2-2^(1-t) if a=1: flipping the one zero endpoint toggles one edge, originally agreeing or disagreeing respectively. The phase on the queried bit affects branch signs, not these quantities.

For every phase the edited spectrum has chi-square divergence 16 delta_t(1-delta_t) from uniform. Indeed multiplication by a character permutes its canonical spectrum. Hence H(E_t)>=t-log2(1+16 delta_t(1-delta_t))>t-1 for t>=4. The argument is Jensen under the edited law, KL(p||uniform)<=log2(sum p^2/uniform). Also H(E_t)<=t. For t=2 every single edit is a character or constant after a phase, so all reserves are zero.

Inductively let the edited even m-core have zero reserve for every phase. At t=4, average odd-child entropy is at least 1, so D_O<=2. At t>=6 it is at least t-5/2, so D_O<=3/2. Since the odd entropy is at least average child entropy (the nonnegative JS increment at this query), the even entropy decrement is at most 5/2 at t=4 and 9/4 at t>=6. Sharpen the t=4 bound: its canonical edited probabilities are ten copies of 1/64 and six copies of 9/64, so H(E_4)=6-(27/16)log2(3)<7/2, using log2(3)>3/2. Thus D_E<9/4 at t=4 too.

If a=0, the odd reserve is at most 2 for t=4 and 3/2 for t>=6. The even Bellman input is at most 9/4-6(5/8)+1<0 at t=4, and at most 9/4-6(1/2+2^(1-t))+3/4<0 at t>=6. If a=1, the odd influence is at least 3/4, so its reserve is zero (D_O<=2 and the edited/clean children have zero reserve). The even Bellman input is strictly below 9/4-6(3/8)=0 at t=4 and at most 9/4-6(1/2-2^(1-t))<0 for t>=6. Backward induction proves every arbitrary-position, arbitrary-character-phase single edit has Q=0 at its even paired entry. It also identifies the precise paid account at each odd character child.

## 2. Two edited children at the first query

At T_k the first query has influence d=1/2+4 delta_k: the two edited endpoints lie in different x_1 halves, have x_2=0, and each toggles an originally agreeing edge. Its x_1=0 child is a cheap odd single edit with unmatched mate character a=0; its x_1=1 child is an expensive odd single edit with a=1, at residual vertex e_3. Translating that vertex introduces a residual phase, already covered above. Both odd children have the same entropy H(O_{k-1}); one is not a clean child. The expensive child's reserve is zero. After querying the mate both children have the phase-corrected single-edit/clean even states, hence no further entry reserve.

At k=4, H(O_3)>=1, Q_cheap<=2, and H(T_4)<=4, giving the parent Bellman input <=3+1-6(3/4)=-1/2.
At k=6, H(O_5)>=7/2 and Q_cheap<=3/2, giving input <=5/2+3/4-6(9/16)=-1/8.
For k>=8 put m=k-2>=6. The chi-square bound improves to H(E_m)>m-1/2, because 16 delta_m<=1/4 and log2(5/4)<1/2. Therefore H(O_{k-1})>=m-1/4, D_cheap<=5/4 and Q_cheap<=5/4. The parent input is <=9/4+5/8-6(1/2+4 delta_k)<-1/8. Thus Q(T_k)=0 for every even k>=4. Both child reserves have been retained; only the expensive child's own physical query sets its reserve to zero. No influence account is counted twice.

## 3. Activated selector: initial influence pays the remaining reserve

Let r>=2k, p=2^-r, delta=2^-k, alpha=2^(-k/2). Form G=1+A_r(b_k-1), L=1+A_r(T_k-1), and select G or L by a fresh fair bit. Query selector, controls, then paired data, with constant leaves. The earlier all-core activation bound D_control<6 Inf_control applies unchanged. Since both core entries now have zero reserve, every activation node has zero reserve. At the root exactly
Q_root=[D_selector-2Cp delta]_+.

Using B<=h2(d), J<=2d/ln2, h2(d)<=d log2(e/d), and ln2>2/3 gives, for d=2p delta,
Q_root<=d(r+k-5/2).
The physical minority is mu=p(1-alpha+2delta)/2, in [3p/8,p/2]. Hence psi(mu)>=3p(r+1)/8. As r>=2k,
Q_root/psi(mu) <=(16delta/3)(r+k-5/2)/(r+1)<8delta.
By the already proved cube edge-isoperimetric bound I>=2psi(mu), Q_root<=4delta I_root. This is an initial influence credit, not a second descendant budget. At C=6, the complete telescope yields H<= (6+4delta) I <=25I/4.

The exact initial influence is
I_root=p[k/2+r(1-alpha+2delta)+(2k-2)delta].
Indeed selector influence is 2pdelta; each control has p(1-alpha+2delta); edited core data influences are 1/2 for labels 2 and 4 and 1/2+4delta for all other labels. Averaging clean and edited data gives p[k/2+2(k-2)delta].

## First unsupported universal line

The proof uses that, among the two surviving children, exactly one unmatched-mate query has a character and influence near one. Arbitrary multiple edits can leave two cheap edited children, or residual cores outside the single-edit phase class. No bound on their combined Bellman reserve in terms of their parent's owned influence has been proved. Substituting a rarity upper bound into the local drift still has the wrong inequality direction. No randomized or infinite-depth limit is needed here: each finite cube is exhausted and the all-k theorem is a separate induction, not an interchange of limits.
