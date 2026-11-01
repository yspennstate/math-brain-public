# Interleaved physical activation transports the paired-quarter bill

Every input is an independent fair bit; entropy is in bits. For Boolean g on its data cube and s>=1 fresh controls define V=1+A_s(g-1), A_s=1{all controls=0}, p0=2^-s. Write L_i(f)=6 sum_T |uhat(T)|^(1/2)|vhat(T)|^(3/2) at the physical i split. The prior A078 proof gives Q_i<=L_i and Delta_i H<=L_i+(9/2)Inf_i. This document retains its arbitrary core bill rather than assumes it paid.

## 1. Exact local core profile: two-sided transport

At a residual active state with p=2^-l and core g_v=u+zv, put mu=E u, nu=E v, alpha=E v^2. The actual identity from CORE_TRANSPORT_PROOF section3 is

    P_i(V)=p[P_i(g_v)-sqrt(|mu|)|nu|^(3/2)]
          +p(1-p)sqrt(|1-mu|)|nu|^(3/2)
          +p^(3/2)sqrt(|1-p+p mu|)|nu|^(3/2),
    Inf_i(V)=p alpha,

where P=L/6. It follows directly from U=1+A(u-1), D=A v and enumerating empty/nonempty data/control Fourier sectors. With |nu|<=alpha<=1, sqrt(2)<=3/2, |mu|<=1, and the latter two terms nonnegative,

    p L_i(g_v)-6 Inf_i(V) <=L_i(V)
                         <=p L_i(g_v)+15 Inf_i(V).       (1)

The lower bound is new explicit accounting: activation cannot erase a bad core-profile query except for an additive influence price. It also holds at l=0, when V=g_v.

## 2. Control queries have a paid quarter profile

At a remaining activation-control query let j=p(1-E g_v)=Inf_t(V). The actual paired empty coefficients have magnitudes1-j and j. At every nonempty residual frequency, the two paired magnitudes agree. Parseval leaves their total squared derivative mass j-j^2. Therefore

    L_t(V)=6[j-j^2+j sqrt(j(1-j))]
          <=3(1+sqrt(2))j <=(15/2)j.                   (2)

For the maximum, write j=1/2+t and bound -t+sqrt(1/4-t^2)<=1/sqrt(2) by Cauchy-Schwarz. The last inequality is strict when j>0; zero endpoints need no division. This counts real physical influence j, not the activation probability alone.

## 3. Active shadow of an arbitrary interleaved physical tree

Let T be any finite deterministic fresh-coordinate restriction tree on V. It can interleave data and control queries adaptively and stop at arbitrary leaves. Queries after a control has revealed1 act on the constant +1 function and have zero L, influence and entropy; they may be contracted. Build a data-only shadow Pi on g by taking the zero child at every control query and retaining both children of every data query. Query labels and stopping rules are inherited from T; no new order is chosen. This familiar point-control projection is credited to A027's stopping transport. The present result transports the particular signed-amplitude quarter functional through it.

At an active physical history, let w be its real reach weight, pi its shadow weight, and l its remaining controls. Then

    w*2^-l=p0*pi.                                    (3)

Both sides equal2^(-s-data_depth). This exact physical relation is the whole padding argument: no hypothetical spectral law or independent conditional schedule is introduced.

Let P_D and P_C be the consumed actual data and control influence, counted once each. Let L_Pi=sum over shadow data nodes pi L_i(g_v), L_T,D and L_T,C the corresponding actual quarter bills. Summing(1)-(2) using(3) yields

    p0 L_Pi-6 P_D <=L_T,D<=p0 L_Pi+15 P_D,
    0<=L_T,C<=(15/2)P_C,
    p0 L_Pi-6 P_D <=L_T<=p0 L_Pi+15 P_D+(15/2)P_C.     (4)

No derivative-gap, monotonicity or l1 admission is assumed on g. A poor shadow policy remains poor up to these additive prices; common activation does not magically repair it by interleaving auxiliary queries.

## 4. Exact ownership and terminal laws

Each shadow leaf lambda retains a genuine residual core g_lambda and l_lambda controls, p_lambda=2^-l_lambda, and weight pi_lambda. Its active physical leaf is V_lambda=1+A_(l_lambda)(g_lambda-1), with weight w_lambda=p0*pi_lambda/p_lambda. Other physical leaves are constant+1. Hence exactly

    E_T I(V_leaf)=p0 E_Pi[I(g_leaf)+l_leaf(1-E g_leaf)],
    P_D=p0[I(g)-E_Pi I(g_leaf)],
    P_C=p0[s(1-Eg)-E_Pi l_leaf(1-E g_leaf)],
    P_D+P_C=I(V)-E_T I(V_leaf),
    E_T H(V_leaf)=p0 E_Pi[H(V_leaf)/p_leaf].           (5)

The data equality is the ordinary physical core influence telescope. For the control equality, at an active control node w*j=p0*pi*(1-Eg_v); conditional core means form a martingale, so each queried control is charged once along the shadow path. Equivalently it follows by subtracting the exact terminal influence from I(V)=p0[I(g)+s(1-Eg)]. The terminal entropy formula retains empty-sector collisions and actual activation leaves; it is not replaced by p0 H(g_leaf) when controls remain.

Combining the prior universal node entropy bound with(4), for any such stopping tree,

    H(V)<=p0 L_Pi+(39/2)P_D+12P_C+E_T H(V_leaf).       (6)

For a complete constant-leaf tree, terminal entropy and influence vanish. If its projected core policy satisfies L_Pi<=K I(g), then

    H(V)<=max(K+39/2,12) I(V).                        (7)

This is explicitly conditional on the inherited core bill. An arbitrary terminal core theorem is not supplied. Partial trees retain the exact terminal term in(6).

## 5. Rare/rare guard and the first unsupported universal line

For the A078 shared bent/spike mux F_k and its r-control common activation W, the local data version of(1) gives

    L_x(W)/Inf_x(W)>=3*2^(k/4)-6.

Taking r=k keeps both actual branches rare and every physical influence and total influence tending to zero (A077's independently checked physical formula), yet this local overcharge persists. The identity(4) explains what survives along any specified interleaved policy: precisely its active core shadow bill, not a freely chosen easier core tree. A077's activated signed-erasure result is reviewed only at its new Sections1-3, independently of accepting our own source lemma.

The first unsupported universal line remains a paid shadow/pivot policy or one exclusive signed terminal-core reserve for arbitrary g (or genuinely overlapping controllers without a common point factor). The projection and linear taxes solve the auxiliary transport/ownership step, not universal selected-coordinate FEI.
