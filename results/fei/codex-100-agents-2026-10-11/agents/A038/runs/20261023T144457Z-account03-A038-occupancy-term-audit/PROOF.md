# Positive query-cost potential: exact Bellman recursion and tensor additivity

All inputs uniform, functions Boolean, entropy in bits, influence in the spectral convention. Set

 delta_i(f)=H(f)-(H(f|i=0)+H(f|i=1))/2-4 Inf_i(f).

Define V4(f) as the maximum over finite fresh-coordinate adaptive query trees of sum_h p_h[delta_(i_h)(f_h)]_+. Constants have V4=0. There are finitely many depth-at-most-n trees, so this is a maximum; stopping is allowed. Completing a partial tree only adds nonnegative charges, so a complete maximizing tree exists.

THEOREM (all Boolean functions, all dimensions).

 (1) V4(f)=max(0,max_i{[delta_i(f)]_+ +(V4(f_i0)+V4(f_i1))/2}).
 (2) For independent-coordinate Boolean factors, V4(f*g)=V4(f)+V4(g).
 (3) [H(f)-4I(f)]_+<=V4(f). Hence a uniform bound V4(f)<=K I(f) would prove FEI with C=4+K.

Proof of(1): condition on the first query. Its charge is fixed, and either child admits its own independently maximizing continuation. Conversely every tree has this first-query decomposition. A stop costs0. This also shows V4 is the least nonnegative function satisfying all these Bellman inequalities, by induction on remaining dimension.

Proof of(2): spectra of f*g tensor, so H and I add, and querying a coordinate of f has exactly delta_i(f), independently of the unchanged g factor. Induct on the total number of remaining coordinates. The child potentials are additive by induction. Each f-query alternative equals V4(g) plus its f Bellman alternative, and similarly for g. These alternatives are at most V4(f)+V4(g), including stopping. For the opposite inequality concatenate complete maximizing trees for f and g. On every first-factor terminal the second factor is unchanged up to a Boolean sign, which changes neither entropy, influence nor the subsequent query costs. This concatenated tree attains the sum. Constants and dummy coordinates cause no exception. Thus tensorization cannot amplify V4/I beyond the maximum factor ratio (when nonconstant factors have positive influence).

Proof of(3): exact physical influence conservation is I(f)-E_i I(f_i)=Inf_i(f). Entropy telescopes on any complete tree, and constant leaves have H=I=0. Therefore sum_h p_h delta_h=H(f)-4I(f); taking positive local parts dominates its positive part. No occupancy reference or reset credit is used in these identities.

The exact current occupancy definition remains the pinned account02/B15 Theorem2.1/section4 definition used in version5: v=Var(f), r_i=Inf_i/v, Q is Ber(c r_i) conditioned nonempty with1-c=product(1-c r_i), K_occ=KL(P+||Q), and completed M gives KL(P||M)=v K_occ. None of these equalities identifies full-product TC with occupancy KL. This stage neither modifies that definition nor retires any version5 source/reset booking.

UNEXECUTED VALIDATION PLAN. code/check.py is a prepared two-lane checker for all278 truth tables on n=0,1,2,3 and eight ordered tensor checks (four distinct selected four-bit product tables). It was NOT RUN: the clock returned14:51:31 UTC, after the campaign end14:49 UTC, before a census was launched. No finite inequality V4<=I, numerical maximum, checked witness or CHECK.json result is claimed. FROZEN_SPEC.json records only the planned bounded domain; its interval-helper copy would occur on execution and has not been performed. The all-dimensional structural proof above is analytical and awaits external independent reconstruction.

FIRST UNSUPPORTED LINE. V4(f)<=K I(f) with a dimension-independent K for arbitrary Boolean f remains unproved. Tensor products cannot produce a worse ratio than their factors, so NEXT must seek a nonfactor Boolean restriction mechanism or an all-dimensional Bellman supersolution. Failure of this stronger V4 target alone would not disprove FEI. The old three-reset family result remains at version5 scope; no fourth optional reset is asserted. Full FEI remains OPEN, and external independent review of the new structural proof is pending.
