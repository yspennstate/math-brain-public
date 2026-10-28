# One original donor pays every later private collision

Entropy is in bits. This is a restricted history-payment theorem, not full FEI. The new collision-account theorem below is elementary and unconditional. Its entropy corollary uses the explicitly stated mean-sector inequality from A077 stage6, which remains pending independent review.

Let d>=1, e=2^-d, and let h be a Boolean sign on the shared d-cube with h(0)=h(e_1)=1. On an independent private cube take arbitrary, possibly correlated, Boolean signs V,W. Set F(s,x)=V(x) at s=0, W(x) at s=e_1, and h(s) elsewhere. A private tree queries only private physical coordinates, adaptively, once per path, and may stop anywhere. All actual leaves, including constant controllers and zero Fourier rows, are retained.

Write g(t)=-t^2 log2(t^2), with g(0)=0, and

    k(a,b)=[g(a+b)+g(a-b)]/2-g(a)-g(b),
    Xi(V,W)=e sum_(T nonempty) k(Vhat(T),What(T)).

For r=a^2+b^2>0 put p=(a^2,b^2)/r and q=((a+b)^2,(a-b)^2)/(2r). Homogeneity gives k(a,b)=r[H(q)-H(p)-1]. Both p,q are binary probability vectors. Therefore -2r<=k<=0. For r=0 the contribution is zero without division. Parseval gives the dimension-independent bound

    -2e[Var(V)+Var(W)] <= Xi(V,W) <= 0,
    in particular -4e <= Xi(V,W) <= 0.                 (1)

Every private restriction leaves exactly the same two shared vertices, h and e, so (1) holds at EVERY descendant. This is where the private-query hypothesis is used. Shared queries are outside the theorem.

Fix one original continuation state o, a budget B, and an inherited old debit that has already been subtracted in forming B. Define at each actual descendant

    K_v=B-Xi_o+Xi_v.                                  (2)

If B>=4e+Xi_o, then K_v>=0; the convenient sufficient condition B>=4e gives K_v>=B-4e. At every binary private query, exactly

    Xi_v-(Xi_++Xi_-)/2+(K_++K_-)/2=K_v.              (3)

Multiplying (3) by the ORIGINAL physical reach weight and summing proves, for EVERY finite adaptive stopping tree and EVERY prefix frontier,

    Xi_o-E Xi_leaf + E K_leaf = B.                   (4)

No positivity of individual collision decrements is assumed. There is no absolute-value sum and no fresh 4e allocation at each node. One signed account pays the entire continuation. The proof is a finite telescoping identity; no exchange of limits or dimension-dependent witness is used.

For clarity, the exact wrapper spectrum is

    Fhat(S,empty)=hhat(S)+e(mu-1)+e(-1)^(1 in S)(nu-1),
    Fhat(S,T)=e[Vhat(T)+(-1)^(1 in S)What(T)], T nonempty.

Thus Xi is the signed row collision of the COMPLETE spectrum. It is not an entropy attached to an abstract spectral law. Direct physical edge counting gives

    j_v=Inf_i(F_v)=e[Inf_i(V_v)+Inf_i(W_v)].          (5)

Let R_v=de[2-(EV_v)^2-(EW_v)^2]. The exact release is

    R_v-E R_child=de[Vhat_v(i)^2+What_v(i)^2].        (6)

The input from A077 stage6 PROOF sections6-8 is the mean-sector inequality

    Delta H(F_v) <= e[Delta H(V_v)+Delta H(W_v)]
                    +R_v-E R_child+12j_v+Delta Xi_v. (7)

This source proof uses the finite row curvature estimate and |g'|<=6 on [-1,1]; all child means are in that interval. The present theorem does not strengthen the physical price12 or assert a new independent review of that continuum estimate. Our finite checker independently verifies (7) on its frozen domain.

Substituting (3) into (7) gives the stopped-node payment

    Delta H(F_v)+E[R_child+K_child]
       <= e[Delta H(V_v)+Delta H(W_v)]+12j_v+R_v+K_v. (8)

With P=sum_v reach(v) j_v, finite telescoping gives

    H(F_o)-E H(F_leaf)+E[R_leaf+K_leaf]
      <= e[H(V_o)+H(W_o)-E(H(V_leaf)+H(W_leaf))]
                      +12P+R_o+B.                 (9)

Both complete actual F terminal spectra and BOTH inherited controller entropy bills appear in (9). Their being retained does not mean they have universally paid FEI certificates. The erasure variant retains both core erasures with price12+2/ln2, by Delta H=B_i+JS_i and the existing JS bound. We do not use that variant to erase terminal entropy.

## A concrete original donor after the first debit

Take even k>=4, untouched private sign y, the quadratic bent sign b on k private bits, V=y b, and an arbitrary W on the SAME private cube (extra private padding bits are allowed). At the original source, H(V)=k and I(V)=k/2+1, including the added y influence. Hence its actual C=5 surplus is

    S=e[5I(V)-H(V)]=e(3k/2+5)>=11e.                (10)

The eH(V) entropy allocation and S are disjoint pieces of the single original 5eI(V) bill. Do not charge the full 5eI(V) again at a descendant. All later inherited V entropy decrements plus expected terminal V entropy telescope to that ORIGINAL eH(V) allocation, even if the private continuation queries bent bits or y. No descendant V certificate is introduced.

Suppose an old debit D0>=0 and the FIRST collision debit4e have already been booked. Preserve them. Set B=S-D0-4e at the chosen continuation state. If D0<=S-8e, then B>=4e, and (2)-(9) fund EVERY subsequent private adaptive tree from this SAME remaining original donor, with

    K_leaf>=S-D0-8e.

For D0=0 this leaves at least3e for all k>=4. This explicitly includes a second unequal private split; it also includes arbitrarily many later private queries and arbitrary stopping. The stronger state-sensitive admission B>=4e+Xi_o is available, but not required by the certificate. If D0>S-8e the convenient admission is unavailable; we assert neither failure of all possible payments nor a new source. No old debit is canceled.

An actual padding family is W=y[1-2*1{z=0,x_1=...=x_m=0}], with m>=2 padding bits and V=y b(z). Query x_1 first, then x_2 on either child, or any later adaptive private order. The inactive first branch has W=y; the active branch remains a point defect times y. All these controller children are balanced and nonconstant as long as y is untouched, so R releases zero there. Equation(5) counts the physical padding influence exactly: at a node with l remaining padding bits the next live padding query costs e*2^(-(k+l-1)); its inactive sibling has zero further padding influence. The full original influences include every z,y,x bit and every shared bit. The checker computes them from truth tables independently of Fourier mean degree.

The universal continuation allowance4e is sharp at an initial state with Xi_start=0: take private characters V=xy and W=y, then query x. The root Fourier labels differ, so Xi_start=0; both children have coincident nonempty labels, giving Xi_child=-4e. A budget below4e makes their carried bank negative. This is the existing actual A077 character witness applied to the new bank admission, not an FEI counterexample.

For the point-padding family above put t=2^(1-k-m) and b0=2^(-k/2). Its COMPLETE original influence is

    I_shared=e(2d-1-b0+t),
    I_bent_bits=e(k/2+kt), I_padding=e mt, I_guard=2e,
    I_total=e[k/2+2d+1-b0+(k+m+1)t].

Direct counting uses disagreement probability Pr(bent!=point)=(1-b0+t)/2 on the edge between edited shared vertices. Every other shared coordinate has influence2e. The data components follow from disjoint physical vertex events. code/influence_audit.py verifies all components independently for the eight frozen fixtures; out/PADDING_INFLUENCE.json records every physical-coordinate influence. No spectator or auxiliary influence is omitted.

## First unpaid universal step

The donor admission is a real restriction: arbitrary roots need not contain an unused certified surplus S>=4e after inherited debits. Arbitrary W core entropy remains in (9), and a shared query changes e/h/event geometry and hence the inherited Xi normalization. Full FEI requires noncircular original-source eligibility and payment for those shared/mixed queries, with complete terminal bills. This theorem closes the further-private-continuation part of the A077/A078 handoff when its explicit original donor is available; it does not make arbitrary cores or terminals free.
