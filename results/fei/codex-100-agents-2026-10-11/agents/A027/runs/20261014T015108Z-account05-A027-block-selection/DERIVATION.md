# Projected-core transport for interleaved point controls

Let u be any Boolean sign on a uniform m-bit core, r>=1 fresh point controls, p=2^-r, and F=1+A_r(u-1). All entropy is in bits. A finite adaptive physical tree may interleave core and control coordinates in any order, without repeating a coordinate along a path. Stop immediately after a failing control; this prunes only queries of the constant function +1, whose entropy and influence decrements are zero. Leaves after failing controls remain actual constant terminals. The control passing value is 0 without loss of generality.

At an active node v all queried controls passed. Let w_v be its actual reach probability, r_v the remaining number of controls, p_v=2^-r_v, and u_v the restricted core. Then its actual function is F_v=1+A_(r_v)(u_v-1), interpreted as u_v at r_v=0. Define d_v=Pr(u_v=-1). A core query costs p_v Inf_i(u_v). A control query costs 2p_v d_v; this is the negative probability of the passing child. These are actual physical edge influences, not nominal per-occurrence costs.

## The projected core tree

Condition the ORIGINAL INPUT on all r controls passing. Delete the now deterministic control queries from the tree. What remains is one actual adaptive core-only restriction tree U; it is not a coupling of unrelated descendant spectra. For each active leaf l its conditional weight is

    v_l = w_l p_l/p = 2^(-number of core queries on its path).

The same formula applies to every active core-query node. All active projected leaf weights sum to 1; inactive leaves have conditional weight zero. Therefore

    Q_core = sum_core_nodes w_v p_v Inf_i(u_v) = p Pi_I(u;U),
    p Pi_H(u;U) = sum_core_nodes w_v p_v Delta_i H(u_v).

This is conditioning on a single physical control event of positive input probability p. It is not a claim that descendant spectral witnesses satisfy a Markov or root-compatibility condition.

## Signed scalar reserve, retained once

Use the exact point-activation correction G_(r_v)(d_v) from A027 version 1, with G_0 identically zero. The actual full entropy decrement has the single endpoint formula

    E_T := Pi_H(F;T)-p Pi_H(u;U)
         = G_r(d_root)-sum_active_leaves w_l G_(r_l)(d_l).

No intermediate reserve is inserted again. Decomposing this one potential along the tree gives E_T=C_core+C_control, where a core node contributes w_v[G_(r_v)(d_v)-(G_(r_v)(d_0)+G_(r_v)(d_1))/2] and a control node contributes w_v[G_(r_v)(d_v)-G_(r_v-1)(d_v)/2]. Inactive child correction is zero. At a control query the p_v H(u_v) part cancels exactly with the passing child's doubled p_v and half weight.

A027 version 2 bounds EACH core-node correction in absolute value by kappa times its physical queried influence, kappa=4+12/ln2<22. This follows from linear controller entropy cancellation and the scalar derivative bound, with the conditional point controller treated as one actual Boolean function. At r_v=0 there is no correction. Write Q_core_live for the physical core influence queried while at least one control remains. Then |C_core|<=kappa Q_core_live.

For a control node the actual passing child is g=1+A_(r_v-1)(u_v-1), whose negative probability is 2p_v d_v. The parent is a one-bit dictator activation of g. The independently reconstructed A028 scalar bound supplies

    0 <= Delta_control H(F_v) <= C0 (2p_v d_v),
    C0=2+2/ln2+1/(sqrt(e)ln2)<6.

Its lower bound is the recovered actual restriction identity Delta H=B+mixing with both terms nonnegative. Thus 0<=C_control<=C0 Q_control. This does not multiply a whole controller-first price by every remaining control: EACH control contributes only its OWN actual physical influence, and the sum is Q_control.

The resulting all-dimensional, all-order transport is

    -kappa Q_core_live <= E_T <= kappa Q_core_live+C0 Q_control.

In particular Pi_H(F;T)<=p Pi_H(u;U)+kappa Q_core_live+6Q_control. Entire core entropy at active terminals remains explicit. Inactive terminal entropy is zero.

## Terminal-inclusive conditional selection theorem

The exact influence partition is

    I(F)=Q_core+Q_control+sum_active_leaves w_l I(F_l).

If the PROJECTED actual core tree U obeys Pi_H(u;U)<=K Pi_I(u;U), K>=0, and EVERY actual active terminal obeys H(F_l)<=L I(F_l), L>=0, then

    H(F)<=max(K+kappa,C0,L) I(F).

The same bound holds with rational relaxation 6 replacing C0. If the projected tree is proper (leaves at least one physical core coordinate on every core path), this is an adaptive proper-core block/stopping-tree transport theorem; exhausted controls are allowed, exhausted cores are not declared a reduction. It transports a SPECIFIED projected partition and does not prove that a universally paid proper partition exists. Point-activated C001-regular core terminals may use their previously certified allowance; arbitrary core leaves must retain their actual entropy.

## Remaining gap and relation to neighboring work

A038 already conserved an interleaved positive-cap selector reserve; this proof concerns the FULL signed entropy decrement and its projected inner core payment, not that cap. A028 owns controller-first and shared-priority gates; those are not rediscovered. A048's descendant-witness injection objection is respected because input-conditioning here supplies an actual physical core tree, not a proposed common spectral reference.

First unsupported universal line: select U (or an interleaved T whose projection is U) with dimension-independent K and certified active terminal allowance L for EVERY Boolean core, without assuming core FEI or silently spending terminal influence. Interleaving by itself does not establish that line. Shared core/control coordinates remain outside the activation model.
