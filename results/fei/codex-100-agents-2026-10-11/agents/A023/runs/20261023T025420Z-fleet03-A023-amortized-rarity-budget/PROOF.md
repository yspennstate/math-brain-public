# Revealing the balancing sign from the same original account

This is stage19, extending the prescribed-reference theorem in stage18, not a universal FEI proof. Entropies, CE and KL are bits. All probabilities below are actual uniform physical reaches. Source trees and peer outputs are read-only.

## Statement and precise prescription

For every even m>=10, let b be ANY bent Boolean sign on m core bits, v!=w, and g=(zb,zb_v,zb_w), with one independent sign z and the same fair nested two-control f as stage18. At ANY physical restriction h (including queries of z), let d_h count only queried original core coordinates. The original seed restriction b_h uses only that core history. Define

    q_h=(P_bh+Uniform_{2^(m-d_h)})/2,
    nu_root=(1-3delta/2,delta/2,delta/2,delta/2), delta=2^-m,
    nu_h=the marginal projection of this SAME nu_root onto remaining control axes,
    Q_h=q_h * nu_h * pointmass_on_the_z_axis_if_it_remains.

When z has been queried, its frequency axis is deleted; it is not replaced by a new reference. Q is normalized and positive on the entire actual spectral support. Let C=CE(P_fh,Q_h), K=C-H(f_h). Let I_D count remaining original core influences AND the z influence only if z remains. Controls keep their original separate owner. Let pi_h be the ACTUAL conditional label law, and retain

    R_h=2 sum_{i<j} pi_h(i)pi_h(j) I(g_ih*g_jh).

The shared z cancels in every pair product whether it is fixed or live. Keep one old debit0<=U<=m/8. Let B_h=4I_D(h)-C_h-U-R_h. For EVERY finite adaptive stopping tree on ALL original coordinates, including arbitrary interleaving of z, controls and core data, with E_leaf d_h<=m/4,

    E_leaf B_h > 729/4096 > 1/8.

No per-path data-depth cap is needed. The reference prescription, original source, SAME boundary reserve, full KLs and old debit are carried throughout. No individual-history nonnegativity is claimed. The stage18 negative rare-branch guard still applies, and revealing z makes that branch's bank smaller by4.

## 1. The actual missing physical query costs exactly4

At every history where z is live, the function is z times some remaining Boolean F. The Fourier law is the law of F with the z frequency obligatorily appended. Its two actual z restrictions are F and -F. Thus each child law equals the parent law with that mandatory frequency deleted. The reference has exactly the same projection. Consequently BOTH actual children have

    H_child=H_parent, C_child=C_parent, K_child=K_parent,
    I_D(child)=I_D(parent)-1, I_controls(child)=I_controls(parent),
    pi_child=pi_parent, R_child=R_parent,
    B_child=B_parent-4.

The exact signed booking is therefore4, with queried influence1 and entropy decrement0. There is no released KL or controller subsidy to spend. The full4 is charged to the unused ORIGINAL data owner, after its old U and remaining R have already been subtracted. This is not a new source admission.

## 2. Keep the exponentially small original terms

Stage18's source and reference identities hold unchanged under the z projection, which is just a spectral shift deletion. Write D=E d_h and p=Pr(z is queried before the frontier). Exact physical influence telescoping, and Inf_i<=1 on each core query, give

    E I_D(h)>=I_D(root)-D-p,
    I_D(root)>=1+m/2-m delta.

The full prescribed data-reference floor gives C_h<=m-d_h+1+C_Y(h). The original controller CE C_Y is still a martingale at core data queries, a supermartingale at control queries, and unchanged at z queries. Thus E C_Y<=H(nu_root). The SAME R is a supermartingale at all queries, with no change at z, and R_root=(3m/2-eta/2)delta<=3m delta/2.

Combining these facts before replacing delta by a constant yields

    E B_h >= m+3-3D-4p-U-H(nu_root)-(11m/2)delta.

This is a general sufficient-condition bound for this family; its hypotheses, the actual reference, and the old debit must not be dropped. Compared with stage18, it prices the physical z query explicitly rather than assuming z remains forever.

## 3. A rigorous uniform source surplus for all even m>=10

Put t=3delta/2. The controller entropy is

    H(nu_root)=-(1-t)log2(1-t)+t(m+1).

For0<t<1, -(1-t)ln(1-t)<t, by integrating1/(1-x)<1/(1-t) over0<=x<t and multiplying by1-t. Also ln2>2/3: the positive atanh series ln2=2[1/3+(1/3)^3/3+...] has first term2/3. Hence

    H(nu_root)<(3m/2+15/4)delta.

With D<=m/4,U<=m/8,p<=1, the complete remaining balance is therefore

    E B_h > m/8-1-(7m+15/4)2^-m.

For integers m>=10, (7m+15/4)2^-m is strictly decreasing, since

    2(7m+15/4)-[7(m+1)+15/4]=7m-13/4>0.

The linear term m/8-1 is increasing. At m=10 the expression is exactly

    1/4-(295/4)/1024=729/4096>1/8.

This proves the all-dimensional theorem for every even m>=10 and ANY bent seed, independent of the exact finite validation family. No floating-point logarithm or unproved FEI estimate is used.

## 4. Every old booking and both full terminals survive

At a core or control query the stage18 exact booking B_parent-avgB_child=4a-DeltaCE-DeltaR still holds, where a is the actual core pivot or0 for a control. At a z query a=1 and both CE/R releases are0, giving precisely4. All quantities are signed and the old U is carried without renewal. For W=B+4I_controls, the complete physical telescope remains

    E_leaf[W+K+R]+sum_queries reach*(4Inf_i-Delta_i H)
      =W_root+K_root+R_root.

The full CE contains the complete source/controller structural sectors plus KL. Both full child KLs, every negative branch, unused controls and all old physical sibling reaches remain in this equation. It neither bounds every local entropy increment by4Inf nor pays an arbitrary newly chosen reference. The prescribed q changes at every core query and all those actual signed changes are included.

## Exact universal gap and shortest next action

The only general-source supply used here is absent: I(b)=m/2 comes from bent flatness. Arbitrary Boolean sources need not provide this surplus. An unlimited-depth extension of THIS bank is actually FALSE: query all m core bits and z, leaving both controls live. At every leaf I_D=0, R=0 and q has one atom. At each of the two edited core vertices the actual control spectrum is uniform on four frequencies; at every other vertex it is concentrated at the empty frequency. Thus the average control law is exactly nu_root, and

    E B=-H(nu_root)-U<0,
    E H_leaf=4delta, E K=H(nu_root)-4delta.

The full KL is retained; it cannot be erased to claim a positive CE bank. This exact Boolean frontier has D=m and lies outside the theorem. It disproves only unlimited-depth positivity for the prescribed bank, not FEI or an alternative signed terminal payment. The next action is to locate the actual original-bank exhaustion boundary using cumulative core pivots rather than the relaxation Inf_i<=1, preserving the same q, projected nu, all full KLs and U. That tests the costly induction step after the balancing-sign subsidy is actually spent, rather than adding another untouched donor.
