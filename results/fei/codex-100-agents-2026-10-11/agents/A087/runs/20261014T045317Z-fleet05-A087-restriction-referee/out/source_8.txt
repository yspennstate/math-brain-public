# Conditional non-point two-core controller transfer

All entropies are bits. At any reached physical restriction history, let h be a Boolean controller on z, and u,v Boolean cores on disjoint remaining data blocks, independent of z and each other. Put F=((1+h)/2)u+((1-h)/2)v. Means may have arbitrary bias or be constant. Write b=Eh,m=Eu,n=Ev,q=(1+b)/2,p=1-q,a=(m+n)/2,c=(m-n)/2,V_u=1-m^2,V_v=1-n^2,delta=(1-mn)/2. The mismatch probability of these actual independent cores is delta, so a queried controller bit has influence d_F=delta*d_h. If delta=0, both cores are the same constant and F is constant; all displayed correction terms vanish.

Let phi(s)=s log2(1/s), lambda(t)=phi(t^2), with continuous zero endpoints, and define

B(b;m,n)=lambda(a+cb)-delta*lambda(b)+(1-b^2)phi(c^2)
          +(V_u+V_v)(1-b^2)/2
          +V_u lambda(q)+V_v lambda(p)-q lambda(m)-p lambda(n).

The exact entropy decomposition is

H(F)=delta H(h)+q H(u)+p H(v)+B(b;m,n).                 (1)

Proof: the empty-data control row is a+c h, with constant mass (a+cb)^2 and nonempty masses c^2 hat h(S)^2. A nonempty u-data row is hat u(T)*(1+h)/2, and a nonempty v-data row is hat v(T)*(1-h)/2. Their data supports are disjoint. Homogeneous entropy gives the coefficient of H(h) as c^2+(V_u+V_v)/4=delta; the remaining terms are exactly B. This is actual Fourier amplitude algebra, not mixture-law entropy. At b=+1 or -1, B=0 and the selected terminal is respectively u or v.

For a control query the core functions and their means remain fixed, the child means are b+-beta with beta=hat h(i), and q is a fair martingale. Consequently

D_F=delta D_h+B(b;m,n)-E B(b_child;m,n).              (2)

This explicitly retains both actual core terminal entropies. It covers any non-point controller and any previous independent-block data exposure.

## A dimension-independent correction price including rare biases

On [-1,1], lambda is 3-Lipschitz: for t>0, lambda'(t)=-2t(2ln t+1)/ln2. The function t(2ln t+1) ranges between -2e^(-3/2) and1; its absolute value is at most1. Thus |lambda'|<=2/ln2<3, using ln2>2/3. Continuity and evenness cover zero and negative t. Also phi(c^2)<=2|c|/(e ln2)<(9/8)|c|, since s ln(1/s)<=1/e, e>8/3 and ln2>2/3.

Boolean mean constraints imply |c|<=delta and V_u+V_v<=4delta. Differentiate B in b with m,n fixed. Its seven terms have total absolute derivative at most

3|c|+3delta+2phi(c^2)+(V_u+V_v)
 + (3/2)(V_u+V_v)+(3/2)|m-n|
 <= (85/4)delta <22delta.                          (3)

The separate terms here are the constant-row derivative, -delta lambda(b), scalar rescaling, variance term, two indicator rows together, and two core mean terms together. No singular logarithm survives without its actual Boolean mismatch factor. Endpoints follow by continuity. In particular B is 22delta-Lipschitz, and |B(b)|<=22delta*(1-|b|), using B(+-1)=0.

Since |beta|<=d_h (Boolean derivatives belong to {-1,0,1}), equations (2)--(3) prove

D_F <= delta D_h+22d_F.                            (4)

The price22 is conservative, not asserted optimal. It owns one actual queried control influence. Rarity release is not spent to derive (4).

## Self-contained controller-prefix and grafting theorem

Fix any finite fresh-coordinate controller tree T with constant h leaves and any declared core continuations T_u,T_v. For C>=0 let Q_C=[D-Cd+E Q_child]_+, zero at the specified leaves. The least reserve for a controller-only prefix at price C+22 is at most delta Q_C(h,T), even though the actual prefix leaves retain u or v. This follows by backward induction from (4). For a declared controls-first full graft, at price alpha>=C+22 its least reserve is at most

delta Q_C(h,T)+q Q_alpha(u,T_u)+p Q_alpha(v,T_v).    (5)

The weighted terminal reserves have zero drift during control queries and match the actual core reserve at each constant-controller leaf. The whole controller seed difficulty is inherited, not certified. At any stopped control prefix the entropy in (1) remains the actual terminal bill.

## Conditional full interleaving lift with an existing reviewed data lemma

For prescribed own-history core trees let nonnegative r_u,r_v satisfy D_core<=C_d*d_core+r_core-E r_child. Fix a controller tree with nonnegative r_h satisfying D_h<=C_h*d_h+r_h-E r_h,child. All trees must be respected by an arbitrary finite adaptive interleaving, and reserves may depend only on their respective block histories and any independent seed fixed initially. Define

R=q r_u+p r_v+phi(q)V_u+phi(p)V_v+delta r_h.         (6)

At a control query, the first two terms are martingales, the variance-rarity bank releases a nonnegative amount, and (4) gives the potential inequality at price C_h+22. At a u- or v-data query, delta=(1-mn)/2 is a martingale because the queried core mean is a martingale and the other mean remains fixed. The own-history r_h is unchanged, so delta r_h is also a martingale. A064's additional-v2 local data lift, independently accepted at that scope by A087, supplies price C_d+11/2 for the other terms. It applies conditionally at the current controller; it does not require q to remain fixed at other query times. Thus, conditional on that reviewed local lemma, R is a nonnegative potential at price alpha=max(C_d+11/2,C_h+22) for the entire declared interleaved policy.

The initial account is

R_root <= q r_u+p r_v+delta r_h+2 I_ctrl(F),        (7)

by A064's reviewed original-edge rarity ownership. At every partial stop actual terminal H(F)-R is retained. If controls are resolved, R is the selected core reserve. If both data cores are exhausted to constants with zero reserve, R is either0 (equal outputs) or r_h (opposite outputs), exactly the inherited remaining-controller interface. Complete controller-and-data leaves have H=R=0. Finite Bellman induction dominates the least alpha reserve by R. Neither (7) nor any other statement bounds arbitrary inherited r_h or core reserves by influence.

For expected terminal control, E R_stop<=R_root+C_d Pi_data+C_h Pi_ctrl: weighted core reserves grow by at most C_d*d_F at data queries, delta r_h grows by at most C_h*d_F at control queries (D_h>=0), and the rarity bank decreases in conditional mean at both types. This identifies resource ownership without a controller or core-tree reset.

The interleaving corollary is conditional on the exact local A064 data lemma and root ownership; only the self-contained controller correction and graft theorem are new independently reconstructed assertions. A064's broader bundled assertions are not adopted. Shared physical data among distinct cores are excluded. More than two selector states are not reduced to an independent replacement fallback.

## First unsupported line

Universal FEI would still require dimension-independent initial payment of delta r_h and the inherited weighted core reserves, or a noncircular selected policy that avoids that debit. A generic many-state repeated-fallback/controller collision does not obey this two-core scalar row law. Extending (2) to its actual complete row profile while preserving a single inherited controller reserve is the next unsolved interface. No rarity release or completed data entropy is available twice.
