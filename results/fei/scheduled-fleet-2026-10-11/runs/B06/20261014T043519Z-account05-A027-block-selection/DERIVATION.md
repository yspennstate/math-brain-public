# First-core-split admission and a nonrenewable control bank

All cubes are uniform, Boolean signs use normalized Fourier coefficients, entropy is bits. Let u on m>=2 physical core coordinates have children g,h after a chosen core split, epsilon=Pr(g!=h), delta=(Pr(g=-1)+Pr(h=-1))/2. Put p=2^-r, r>=1 fresh point controls, F=1+A_r(u-1), and F_g,F_h its ACTUAL children with the SAME unqueried controls. All remaining core and control entropy stays in these children. A one-coordinate core block is proper because m>=2.

## Reserve geometry, using the recovered B05 price

Use the established B05-ODDFACE-ISO-PAYMENT@1 and C005 mixing bound, not a new local lemma: any Boolean split with children v,w and queried influence q obeys Delta H<=(1/2)I(vw)+(3/ln2)q. Write c=3/ln2<9/2. Here q=p epsilon and the ACTUAL product of the activated children is

    F_g F_h = 1+A_r(gh-1).

Direct physical edge counting therefore gives

    I(F_g F_h)=p I(gh)+2rp epsilon,
    Delta_core H(F)<=c q+B_data+B_future,
    B_data=(p/2)I(gh), B_future=rp epsilon.

The expected complete terminal influence after this ONE split has two distinct components

    T_data=(p/2)[I(g)+I(h)], T_control=2rp delta.

Since an edge of gh is an edge of g or h, B_data<=T_data. Since mismatch requires at least one child to be negative, epsilon<=2delta. For delta>0 put rho=epsilon/(2delta); then B_future=rho T_control and 0<=rho<=1. If delta=0 everything vanishes and define rho=0. Both owner bounds are SHARP, even for arbitrarily small positive delta: take h=+1 and g a point defect on an arbitrarily large remaining core cube. This is the precise fraction of the unqueried control bank borrowed at the first core split, not a renewed controller-first account.

## Signed certified-child admission

For target price C>=0, let s_g=C I(F_g)-H(F_g), s_h=C I(F_h)-H(F_h). The recovered child-deficit identity gives the SUFFICIENT condition

    (s_g+s_h)/2 >= B_data+B_future+(c-C)q  ==>  H(F)<=C I(F).

Signed s_g,s_h are retained; a negative child deficit cannot be clipped. Any genuinely certified LOWER bounds on these complete child slacks may replace them. This is not a new derivation of the baseline child identity: the delta is the explicit product-mask data/control owner decomposition and its sharp rho coefficient. The condition is sufficient, not necessary, because the B05 local price can overestimate actual entropy.

An owner-separated certificate may use available average child slack S_data>=B_data and S_control>=rho T_control, with their SUM charged only once, and C>=c. More generally the positive query-price allowance (C-c)q can reduce the required bank. If both actual activated children have an entropy allowance L I, then at target C>=max(L+1,c) their average surplus funds B_data+B_future<=T_data+T_control. Thus a SPECIFIED first proper core split with certified children closes at max(L+1,c), rather than the earlier coarse wrapper-transport surcharge. This is a conditional finite lifting rule, not universally certified children or a depth-independent induction theorem. In particular point-activated C001-regular core children may use their already recorded regular allowance; arbitrary children are not declared regular.

## Exact failure of renewing this reserve

For ANY actual core-only stopping tree U with these controls untouched, summing this particular future-control debit gives sum_v w_v B_future(v)=rp Pi_I(u;U)=r Q_core(F). Expected terminal control influence remains2rp delta_root by the core bias martingale. For positive delta the ratio is therefore Pi_I(u;U)/(2delta_root), not automatically at most1. This calculation concerns the unsigned sufficient debit, not an identity for actual entropy.

Take u=D_m, the sign negative only at the all-zero point of m core bits, m>=2. F is the ACTUAL point defect D_(m+r). Query m-1 core coordinates, stopping immediately at the first core value1, with controls untouched. Every path leaves a physical core coordinate unqueried. At reached core depth k=0,...,m-2, reach weight2^-k and mismatch epsilon_k=2^{-(m-k-1)}. Hence each weighted future-control debit is

    w_k r p epsilon_k=2rp delta_root,

and their sum is (m-1) times the ORIGINAL unqueried-control bank T_control=2rp delta_root. This SAME bank remains in expectation at the actual terminals. Therefore the proposed unsigned rule sum_core w B_future<=T_control is FALSE already at m=3, and its ratio is unbounded with m. There are no extra controls or changed physical functions at deeper nodes. This is an exact certificate against renewing the sufficient reserve, not an FEI counterexample and not a proof that actual entropy needs this growing debit.

Indeed every reached F node is a point defect, hence a dictator activation of its passing child. The independently reconstructed A028 one-bit scalar price gives actual Delta H<=6q at each such core query; their summed ACTUAL full entropy path cost is paid at rate6 with terminal entropy retained. The unsigned B_future overbill and the paid actual entropy coexist. This separates the failed funding mechanism from the desired stopping-tree theorem.

## Universal gap and next mechanism

First unsupported universal line: for every Boolean core choose a proper split with actual certified complete child surplus that pays the displayed owner-specific requirement, then transport the UNUSED surplus to the next split without renewing either owner. Root certificates or regular terminal examples do not supply this selection. The point-defect calculation proves that charging the unfiltered sufficient B05 future-control debit at every core query is the wrong induction mechanism. NEXT must preserve a signed refund or localize the debit to genuinely unpaid queries on the same physical leaf partition, rather than spend rho T_control anew at every depth.
