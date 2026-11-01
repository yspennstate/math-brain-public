# Repair: a common conditional spectral kernel, with its full terminal cost

Uniform physical cubes; Boolean signs; entropy and KL in bits. A finite deterministic fresh-singleton tree queries controller coordinates C only. Other coordinates are divided into a retained frequency block U and a spectator frequency block Z. Labels remain ambient. The tree may stop with nonconstant data functions. References are normalized complete spectral laws, not labelled variance sums.

## 1. Exact hypothesis and normalization

At every reached node v, assume its ACTUAL Fourier-square law has the form

    p_v(c,u,z)=pbar_v(c,u) k(z|u),

where one fixed normalized conditional kernel k is used throughout the controller prefix. Controller coordinates already fixed disappear from c. The same kernel is used in every chosen reference:

    q_v(c,u,z)=qbar_v(c,u) k(z|u).

Require pbar_v absolutely continuous with respect to qbar_v. Arbitrary normalized definitions of k at never-used u are permitted, but reference-positive rows must also be normalized. Bias-free tensor independence is a sufficient special case; k need not be independent of u, and the quotient pbar need not itself be the Fourier law of a Boolean quotient function.

For one law p and one reference q, the KL chain rule says

    D(p||q)=D(pbar||qbar)+E_pbar D(p(Z|c,u)||q(Z|c,u)).

The last term vanishes if and only if their conditional laws agree on every p-positive row. Thus matching the conditional spectator law is the necessary and sufficient condition for OMITTING NO conditional KL. This is the weakest exact reference-level zero-correction condition, not a claim of a weakest physical hypothesis for every possible influence bound. The hereditary fixed-k assumption is the useful checkable additional hypothesis for a controller tree.

The lifted reference is normalized because sum_z k(z|u)=1. Its actual cross-entropy and KL are exactly

    CE(p,q)=CE(pbar,qbar)+L_v,
    D(p||q)=D(pbar||qbar),
    L_v=E_{pbar_v} H(k(.|U)).

The same identities hold at every leaf. Spectator entropy is not erased by quotienting.

## 2. Physical kernel, inherited reference and signed reset

At a fair controller query i, erase its spectral bit to T=(c without i,u). The actual fiber mass is p_e(T,z)=pbar_e(T)k(z|u). The actual coherent branch probability is

    K_b(T,z)=p_child_b(T,z)/(2p_e(T,z))
            =pbar_child_b(T)/(2pbar_e(T)).

Thus the channel depends only on the quotient T. On source-zero fibers choose a normalized fallback independent of z; then even reference-only rows transport correctly. Applying the SAME K to the erased reference gives branch predictions q_b and normalized Bayes children. The full and quotient predictions agree, and each full Bayes child equals its quotient Bayes child times k. No fresh marginal projection is called inherited credit.

For any one source/reference node let E_v be the conditional erasure KL, O_v the physical- versus reference-branch KL, and let q'_b be a freshly chosen child reference. Define the SIGNED reset

    rho_v=average_b [D(p_b||q'_b)-D(p_b||q_Bayes_b)].

Since keeping T makes the channel embedding lossless for KL,

    D(p_v||q_v)=E_v+O_v+average_b D(p_b||q'_b)-rho_v.

Every one of E,O,rho, source KL and child KL is exactly its quotient counterpart under the common-k hypothesis. Finite telescoping preserves their signs:

    D(root)+sum reach rho = sum reach(E+O)+E D(terminal).

Neither a positive reset nor a positive labelled reserve is automatically paid. The theorem preserves the once-only normalized account, including its negative terms; it does not create a universal reserve.

## 3. Controller entropy/influence and terminal transport

The fair restriction identity implies the retained U marginal martingale pbar_v(U)=average_b pbar_b(U). Hence L_v=average_b L_b and L_root=E L_terminal. It follows that each controller erasure entropy M_v, channel information J_v and total entropy decrement D_v agree with their quotient values. For M this is H(query bit|T,Z)=H(query bit|T); for J use the common-k channel and entropy cancellation. Physical controller influence equals its spectral marginal and also agrees with the quotient marginal. Consequently

    H(f)-E H(f_leaf)=H(pbar_root)-E H(pbar_leaf),
    CE(p_root,q_root)-E CE(p_leaf,q_leaf)
       =CE(pbar_root,qbar_root)-E CE(pbar_leaf,qbar_leaf).

Any previously proved controller-prefix inequality on the quotient laws transfers at EXACTLY THE SAME controller price. This clause requires an actual quotient certificate; there is no automatic Boolean quotient and no automatic universal FEI claim. Full terminal cross-entropy is E CE(pbar_leaf,qbar_leaf)+L_root, once, rather than an extra copy per branch. All physical terminal influence remains in the physical account.

Useful physical sufficient condition: f(z,x)=v(z)G(x), where z and x are disjoint physical coordinates, v is any Boolean sign, and only G's controller coordinates are queried. Every selected core, including the fallback, must contain the SAME unqueried factor v. Then k=P_v is constant in u, the quotient functions are actual restrictions of G, H(f)=H(v)+H(G), and I(f)=I(v)+I(G). For any normalized quotient reference Q_G, Q_f=P_v tensor Q_G has CE=H(v)+CE(G,Q_G); all controller Bayes/erasure/reset costs are unchanged. If an actual G theorem gives controller bill <=K R and leaf certificates CE(G_leaf)<=C I(G_leaf), use the same K on controllers and retain H(v) once. A certificate H(v)<=C_v I(v) then gives the full bound with max(K,C,C_v) on its exclusive budgets. This is a scoped inheritance theorem, not an appeal to universal FEI to generate v's certificate.

## 4. Application scope and the common-parity obstruction

A048's new family is admitted exactly: G=1-2(1-AND_m)AND_n and f=yG. Its actual cores are y and y*h_n, including fallback y, so k is the deterministic parity-spectrum law. Its entropy cost is H(y)=0, its terminal influence I(y)=1 is retained once, and every normalized quotient controller account remains unchanged. The failed labelled reserve does not share this property: with psi(q)=q log(1/q), a common factor of mean b changes sum psi(q_j)Var(u_j) by (1-b^2)sum psi(q_j)(E u_j)^2. The matching signed residual changes oppositely. The normalized repair retains that cancellation rather than separately buying the inflated release. It also admits arbitrary common independent Boolean factors of nonzero Fourier entropy, retaining their actual entropy and any certified terminal bill once. Different quotient cores may use disjoint data as required by their supplier theorem; their full physical cores may all overlap on the common factor.

The reference-level hypothesis is strictly broader than an independent Z spectrum. Example f=c*h_3(U,Z_1,Z_2), with c a character and h_3 a three-bit point defect, has conditional Z law depending on the U frequency: k(.|U=0)=(3/4,1/12,1/12,1/12), k(.|U=1)=(1/4,1/4,1/4,1/4). A controller-only query still preserves that k exactly. Quotient spectra need not be Boolean, so only their proved marginal account transfers.

Another genuine shared-data example chooses among h(U,Z), Z-character*h(U,Z), -h(U,Z), and h(U,Z), where h is the two-bit AND sign. Its Fourier Z rows at U=0 are proportional with the same sign and at U=1 with opposite sign. Thus all controller restrictions share k(Z-frequency|U-frequency)=(1/2,1/2), although the two data cores are not the same independent spectator times Boolean functions of U alone. The quotient may be non-Boolean; the normalized signed transport still holds.

EXCLUDED: A092's prescribed priority gate with fallback +1, parity core on (U,Z), and AND-sign core on the SAME (U,Z). Conditional Z distributions disagree even at the terminal core rows: on U-frequency=0, the fallback is Z-frequency=0 certainly while the AND-sign core is fair. On U-frequency=1, parity is Z-frequency=1 certainly whereas the AND-sign core is fair. There is no common conditional k for those terminals under this split. Their bank cannot be paid separately; nothing here repairs that failed standalone-bank inequality. Also excluded without an explicit new correction are queries in U or Z and changing conditional spectator laws after data exposure.

## 5. Exact first data-query boundary

For f=c*h_3(U,Z_1,Z_2), now query the PHYSICAL U bit rather than a controller. The two terminal data functions are constant and h_2. The root U-frequency marginal is (3/4,1/4). Its average conditional Z entropy is

    L_root=H(h_3)-h2(1/4)=2-(3/8)log2(3).

The average terminal spectator entropy is (1/2)H(h_2)=1. Thus the omitted correction would be

    L_root-E L_leaf=1-(3/8)log2(3)>0,

proved since 3^3<2^8. The data-side channel J is 2-(5/8)log2(5)>0. This is an actual Boolean, nonconstant-terminal counterexample to extending the controller-only cancellation unchanged through an arbitrary data query. Terminal influence and entropy remain retained. Section 6 pays the POSITIVE ENTROPY correction, but not an arbitrary conditional-reference reset or the quotient/core bill.

## 6. A first data query: paid entropy drift and sufficient likelihood ratio

Let a fresh query i belong to the retained quotient block and let Z remain unqueried. Put T for all remaining quotient frequencies. No fixed-k assumption is needed for the following entropy identity. Define L=H(S_Z|S_i,T) at the parent and L_b=H(S_Z|T) in the ACTUAL child spectral laws. The exact drift is

    DeltaL=L-average_b L_b
          = I(B;S_Z|T) - I(S_i;S_Z|T).

Here B is the coherent physical branch and the first mutual information uses its actual joint with the retained spectrum; the second uses the actual root spectrum. Indeed M_full-M_quot=-I(S_i;S_Z|T), while J_full-J_quot=I(B;S_Z|T). Both conditionals are nonnegative. Therefore

    [DeltaL]_+ <= J_full <= (2/ln(2)) Inf_i(f).

The last inequality is uniform and Boolean: in each child-amplitude fiber G,H, its natural-unit fair channel information is at most (|G|-|H|)^2/2 <= (G-H)^2/2. To prove the scalar inequality, g(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2 has coefficients 1/[2k(2k-1)]; 1-sqrt(1-z^2) has coefficients binom(2k,k)/[4^k(2k-1)], which dominate since binom(2k,k)/4^k>=1/(2k) by induction. Multiplying by (G^2+H^2)/2 and applying Parseval gives the displayed physical price. Thus the first data query's extra conditional ENTROPY drift has an unconditional influence price, with its negative credit retained. This does not bound arbitrary KL reset costs.

There is a useful additional local reference hypothesis that avoids a new conditional KL altogether:

    p(s_i,T,z)=r(T)q(s_i,T,z) on all source/reference rows,

for a positive function r; rows with both masses zero are ignored. In words, the source/reference likelihood ratio is measurable from the RETAINED quotient frequency T. This allows p!=q and does not require the spectator kernel to stay fixed after this data query. Summing over s_i gives p_e(T,z)=r(T)q_e(T,z). Applying the same actual K_b then gives

    p_b(T,z)/q_Bayes_b(T,z)=r(T) q_b/(1/2).

The ratio is independent of z. Thus each inherited child reference and each actual child have the same conditional spectator law given T. Full and quotient erasure KL are zero, branch predictions/outcome KL agree, and the full Bayes child KL equals the quotient child KL. Any chosen child reference with that actual child conditional law incurs exactly its quotient reset, with no extra conditional KL. This is proved by normalized transport, not by identifying root, released and child banks. The inherited matching condition itself is exactly zero conditional KL at the child; the measurable-ratio condition is a sufficient constructive source criterion, not claimed necessary in all channels.

If the quotient has a certified data-query price K*Inf_i, its full entropy price is at most (K+2/ln(2))*Inf_i under this decomposition. The SAME data influence is charged this summed coefficient once; it is not available again at full price for a separate reserve. Full terminal costs and signed quotient resets remain retained. Future controller queries require the common-k hypothesis to be checked anew at their actual histories.

Nontrivial actual example: f=h_2(C_1,C_2)*h_3(U,Z_1,Z_2), query physical U, and use q=P_ref(C-frequency) tensor P_h3(data-frequency), where P_ref is any positive normalized controller reference. Then p/q=P_h2(C)/P_ref(C) depends only on retained C, so the two Bayes child references are P_ref(C) tensor P_constant(Z) and P_ref(C) tensor P_h2(Z). They preserve the exact source KL with zero outcome/extra conditional-reset debt. Each child now again has a common independent spectator for its subsequent controller queries. This is an actual data/controller continuation, not a claim that an arbitrary unfinished shared core satisfies the likelihood condition.

FIRST UNSUPPORTED universal line: when this retained-frequency likelihood condition fails, pay the changed conditional-reference reset and the certified quotient/core decrement together with both actual terminal profiles from one unused signed child/control account. The paid entropy-drift lemma alone does not supply those missing credits or make a non-Boolean quotient eligible for Boolean FEI induction.
