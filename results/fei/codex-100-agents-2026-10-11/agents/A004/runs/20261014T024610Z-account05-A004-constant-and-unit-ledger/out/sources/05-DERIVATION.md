# A single correlated spectator can carry the terminal refund

All functions are actual finite uniform-cube Boolean signs and all logarithms are in bits. For p_S=hat f(S)^2 let e_i=Inf_i(f), r_i(T)=p_T+p_(T+i), mu_i(T)=p_(T+i)/e_i. Both complete row laws normalize to one. The retained row price is

    M_i(f)=e_i[log2(1/e_i)-D(mu_i||r_i)].

Zero rows are omitted. These definitions and M<=B<=M+I/ln2 are existing baselines, not new results.

## 1. Precise new target from the A001/A090 objections

Deleting an independent common spectator factor loses zero KL. Does deleting only ONE physical spectator from a genuinely correlated row have a bounded refund loss per influence of that deleted bit? No. The exact loss below can lie between (d-1) and d times that influence, although the whole Boolean family has H/I<=3. This closes a local payment shortcut; it does not refute a complete conditional-edge refund or FEI. It also identifies the exact original terminal row that must own the loss.

For any row quotient C, KL chain rule gives

    L_i(C)=e_i[D(mu_i||r_i)-D(Cmu_i||Cr_i)]
          =e_i sum_c mu_i(c)D(mu_i(.|c)||r_i(.|c))>=0.   (1)

The reference is marginalized as a probability law, never conditioned on derivative support. After coarsening, M_i^C=M_i+L_i.

## 2. Exact partial parity-duplication transport

Let f have physical coordinates x_1,...,x_n. For an arbitrary subset J, replace each x_i, i in J, by u_i v_i on two fresh uniform coordinates, keeping the other coordinates unchanged. Denote the resulting actual Boolean function by F_J. This is a physical construction, not a claim that arbitrary changes of Fourier basis preserve influence. Explicit character expansion embeds each spectral set S by replacing i in S cap J with both u_i,v_i. All other Fourier coefficients vanish. Consequently

    H(F_J)=H(f),
    I(F_J)=I(f)+sum_(i in J)e_i,
    M(F_J)=M(f)-sum_(i in J)M_i(f).                      (2)

The last identity follows row by row. An unduplicated coordinate has exactly the same row pair masses as f, with deterministic support relabeling. For a duplicated row u_i, write A_T=p_T and B_T=p_(T+i) from f. Its only nonzero complete-reference atoms are

    r_u(T,v=0)=A_T,  r_u(T,v=1)=B_T;
    mu_u(T,v=0)=0,   mu_u(T,v=1)=B_T/e_i.

Thus D_u=log2(1/e_i), M_u=0 and B_u=0. The same holds for v_i. In particular these new relevant coordinates can have zero erasure.

Now let C_u erase only the partner occupancy v_i and retain ALL other spectral information. The coarsened laws are literally

    C_u r_u(T)=A_T+B_T,  C_u mu_u(T)=B_T/e_i.

They are the full original f row, with its exact unit normalizer. Therefore

    D(C_u mu_u||C_u r_u)=D_i(f),
    L_u(C_u)=M_i(f),  M_u^C=M_i(f).                     (3)

Both partner rows together lose 2M_i(f). Over the disjoint coordinate pairs the loss and the one physical influence ledger are exactly

    L_total=2sum_(i in J)M_i(f),
    I(F_J)=I(f)+sum_(i in J)e_i.                         (4)

This is the source-owned terminal bill, not an independent payment. Charging each loss to a new generic spectator allowance would discard (3). If J is all coordinates, M(F_J)=B(F_J)=0, I(F_J)=2I(f), yet L_total/I(F_J)=M(f)/I(f). Thus a uniform aggregate bound for this particular one-partner deletion family has optimal constant exactly K_M in the extended reals. This consequence is a diagnostic of a proposed shortcut, not a fresh equivalent formulation offered as a solution of FEI. Entropy resides in the physical descendants even though this root erasure is zero.

## 3. Positive repair: retain the partner bit and discard the core

The same genuinely correlated row admits an exact binary sufficient statistic in the OPPOSITE direction. Let K_u retain only partner occupancy v_i and discard every other residual coordinate. Its complete row laws are

    K_u mu_u=(0,1),  K_u r_u=(1-e_i,e_i).

The reference still has total mass one, including its derivative-free atom. Thus D(K_u mu_u||K_u r_u)=log2(1/e_i)=D_u and the KL loss is exactly zero. On v_i=1 the two conditional laws of the discarded T coincide, both B_T/e_i; on v_i=0 the derivative has zero mass. No independence of v_i and T under r is required. This supplies an exact spectator-compatible quotient for the present non-product row: keep the informative bit, cancel only the conditionally common factor. Tensoring both original row laws with an arbitrary common independent spectator law leaves this quotient and its zero-loss proof intact.

This is not the invalid operation of conditioning r on derivative support. The atom of reference mass 1-e_i is retained, so all log2(1/e_i) rarity refund survives. If every coordinate is duplicated, the complete rowwise binary references and the original coordinate weights e_i/I(F) yield a normalized joint reference with exact original joint KL and zero root M. They do not encode the terminal seed entropy or pay its physical descendants. For a general row, retaining only its derivative-support event recovers log2(1/r(support)) but leaves D(mu||r(.|support)); that conditional term is not discarded or bounded here.

## 4. Actual non-product row with an unbounded local loss

Let d>=2 be even, N=2^d, delta=1/N and t=sqrt(delta)=2^(-d/2). On d physical bits choose the quadratic bent sign

    b(y)=(-1)^(y_1 y_2+...+y_(d-1)y_d),

where y_j are 0/1 labels of the uniform cube. Each two-bit factor has four Fourier coefficients of magnitude 1/2, so every Fourier coefficient of b is sigma_T t, sigma_T in {-1,1}. This proves the bent property directly, without a literature premise. At the all-zero vertex b(0)=1. Let c=b-2 1_{y=0}, and use a fresh selector s:

    g(s,y)=b(y)-1_{y=0}+s 1_{y=0}.

Its two actual children are b and c. For the selector row,

    a_T=sigma_T t-delta,  b_T=delta,
    A_T=(sigma_T t-delta)^2, B_T=delta^2,
    e_s=delta,
    r_s(T)=delta[1-2sigma_T t+2delta].                 (5)

Since 0<t<=1/2, 1-2t+2t^2>=1/2. Hence r_s(T)/B_T>=1/(2delta), giving

    M_s(g)>=delta(d-1).

The upper bound M_s(g)<=delta d follows from D(mu_s||r_s)>=0 and the complete normalized row identity. Thus

    d-1<=M_s(g)/e_s<=d.                               (6)

There are both positive and negative sigma_T (also immediate from the two-bit factor). Thus B_T/(A_T+B_T) takes two different values. The partner bit in (3) is correlated with T under the reference law; this is genuinely a non-product row, not an independent tensor spectator.

Duplicate only this selector: G(u,v,y)=g(uv,y). Then Inf_u=Inf_v=delta, M_u=M_v=B_u=B_v=0, while erasing the ONE partner occupancy has

    delta(d-1)<=L_u<=delta d,
    delta(d-1)<=L_v<=delta d.                          (7)

In particular L_u/Inf_v>=d-1, and even pooling both duplicate influences gives (L_u+L_v)/(Inf_u+Inf_v)>=d-1. No finite local K pays these losses using only the queried/erased pair influence, despite complete normalization and deletion of just one spectator bit. Its binary conditional KL can be arbitrarily large: a one-bit alphabet is not a one-bit divergence bound.

This witness has a paid total physical scale. Every bent coordinate has influence 1/2. At zero, its neighbor under b also has sign +1; the single vertex flip adds one undirected pivotal edge, hence Inf_j(c)=1/2+2delta. Thus

    Inf_j(g)=Inf_j(G)=1/2+delta,
    I(G)=d/2+(d+2)delta.

Fourier embedding gives H(G)=H(g)<=d+1, because g has d+1 coordinates. Therefore H(G)/I(G)<=2+2/d<=3. This is a counterexample only to the local exclusive-spectator reserve, not an unbounded-ratio Boolean family. A terminal/core influence reserve remains available but is not assigned for arbitrary overlapping rows by this argument.

## 5. Honest surviving gap and changed mechanism

The independent-factor cancellation rule is exact, and section 3 gives an exact conditional binary repair for this correlated row. Marginalizing the informative bit is false at the explicitly tested local rate. The next surviving question is whether a signed, physically justified conditional partition can retain the likelihood-ratio information in a nonzero-erasure row, or assign its exact remaining conditional loss once to a disjoint terminal-core reserve. The first unsupported universal line is still

    sum_i e_i D(mu_i||r_i)>=sum_i e_i log2(1/e_i)-K I

for one absolute K and all actual Boolean f. Equations (3)-(7) forbid using only spectator bit count or the erased pair's influence as its payment. They do not forbid a structured function-specific reference, a complete global tree, or a policy paying from certified child slack. NEXT must name that terminal reserve and its ownership rather than propose another lossy degree or one-bit compression.
