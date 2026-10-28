# Signed data payment for arbitrary biased controllers

All logarithms are base two. Let a be a Boolean sign on physical controls Y,
independent of the shared data cube X carrying Boolean G,H. Set c=(1-a)/2,
p=E c, V=4p(1-p), gamma=Pr(G!=H), and F=(1-c)G+cH.
All restrictions below query actual coordinates of these two fixed disjoint cubes.
Both source functions remain present at every node, even when a is constant.

For data Fourier row t write g_t=Ghat(t), h_t=Hhat(t),
z_t=(1-p)g_t+p h_t, d_t=(g_t-h_t)/2,
q_t=(1-p)g_t^2+p h_t^2, and w_t=V d_t^2.
Then q_t=z_t^2+w_t, sum q_t=1, and sum w_t=V gamma.
For V>0 let A(s)=ahat(s)^2/V on nonempty controller sets s.
This is a normalized probability law. Define

    J=H(q)-(1-p)H(G)-pH(H),
    B=sum_t q_t h2(w_t/q_t),
    L=B+V gamma H(A).

A zero row contributes zero. If V=0 define B=L=J=0; the selected source is F.
The actual squared Fourier law has empty-control atom z_t^2 and nonempty-control
atoms d_t^2 ahat(s)^2. Entropy chain rule therefore gives the exact identity

    H(F)=(1-p)H(G)+pH(H)+J+L.                 (1)

J is a weighted Jensen--Shannon divergence, so 0<=J<=h2(p); L>=0 as well.
This derivation covers biased, non-point, restricted, and constant controllers.

At a DATA query i, p remains fixed. Write delta_i H(U)=H(U)-avg_b H(U_b).
The signed residual after retaining both source decrements and the structural cost is

    D_i=delta_i H(F)-(1-p)delta_i H(G)-p delta_i H(H)
        -[L-avg_b L_b]
       =J-avg_b J_b.                         (2)

The structural difference in (2) is signed, and need not be nonnegative.
Dropping it or replacing it by a fresh positive budget is invalid.

At a CONTROL query j, G,H do not change and p=(p_0+p_1)/2. For these fixed
source spectra, J(p)=H((1-p)P_G+pP_H)-(1-p)H(P_G)-pH(P_H) is concave in p,
including its endpoints. Thus C_j=J-avg_b J_b>=0. This is the key step that
permits controller queries during an otherwise arbitrary data history.

For any finite adaptive stopping tree T, let r_v be the physical reach of node v.
Telescoping the single potential J gives

    sum_DATA r_v D_v + sum_CONTROL r_v C_v + E_leaf J_leaf = J_root. (3)

Consequently the SIGNED total data residual is <=J_root<=h2(p_root)<=1.
Every partial frontier has remaining budget

    J_root - sum_past_DATA r_v D_v
      = sum_past_CONTROL r_v C_v + E_frontier J >=0.                (4)

Negative data debits are refunds. Positive parts need not obey (3). Neither the
stopping policy nor the depth appears in the bound; no ancestor bank is renewed.
Equations (1)--(4) are independent of all FEI hypotheses and of any chosen K.

Quantitative source interface, conditional on A028 v5's tensorized JS lemma:
J_root<=2 log2(e) gamma_root I(a_root). The v5 proof also gives
L_root<=gamma Hplus(a)+log2(e) gamma V+R,
R=V I(GH)/2. Thus this extends the SAME original source price, not a new
controller allowance at each data query. Exact algebra for the second bound:
B<=h2(V gamma), H(A)=Hplus(a)/V+log2 V,
h2(w)<=w log2(1/w)+log2(e)w, and edge isoperimetry
gamma log2(1/gamma)<=I(GH)/2. Endpoints follow by continuity.

Audit of scope: L is an exact inherited structural cost, not an already paid
per-node nonnegative release. The theorem prices the remaining data residual
after its signed variation is retained. It does NOT price discarded source
decrements, arbitrary terminal KL under prescribed reference resets, or arbitrary
Boolean admission. To control an entire mixed tree with no structural booking,
one must also account for the complete L variation and both source terminals.
Their algebraic telescope is available, but a universal influence payment is not.
The v5 quantitative lemma remains pending independent review. The new identities
and concavity argument do not depend on its acceptance.

For clarity, the concavity argument has no division at a zero row. On 0<p<1,
every row with P_G(t)+P_H(t)>0 has q_t>0 and
J''(p)=-log2(e) sum_t (P_H(t)-P_G(t))^2/q_t<=0.
Rows zero in both sources are omitted. Entropy is continuous at zero masses,
so concavity extends to p=0,1. No derivative or limit is taken over an infinite
sum: every cube and every tree is finite.

If both source classes are restriction-closed FEI-certified and the remaining
controls are eventually resolved, all terminal functions lie in those certified
classes. Adding every ACTUAL signed entropy decrement and full terminal entropy
gives H(F_root), bounded by the v5 root constant
max(K+3log2(e), L_G+2p, L_H+2(1-p)) times I(F_root), when Hplus(a)<=K I(a).
This corollary retains the existing root constant; its new bookkeeping content is
the signed J allocation through mixed histories, not a new class or FEI constant.

First unsupported universal line: bound inherited source entropy/reference costs
and any required structural conversion on unrestricted root functions using one
genuinely unused ancestor influence account. The present theorem supplies no such
universal source certification. Full FEI remains OPEN.
