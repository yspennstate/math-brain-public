# Exact boundary of a coordinate entropy estimate

Draft independent derivation by w508, 2026-10-10, for review by w509. The canonical store already contains the upper-bound constant in a related owner result. This is not a novelty claim.

For any Boolean f under uniform measure, define Delta_i=H(f)-(H(f_+)+H(f_-))/2 and alpha=I_i(f). With base-2 entropy, the following holds:

0 <= Delta_i <= h_2(alpha)+(2/ln 2) min(alpha,1-alpha).

Consequently Delta_i <= alpha log_2(1/alpha)+(3/ln 2) alpha, with the zero-alpha convention. The additive coefficient 3/ln 2 cannot be decreased in an estimate of this latter form valid for every Boolean f and every coordinate.

Proof of the upper bound. Let u and v be the normalized Walsh coefficient vectors of the two restrictions, and let r=(u^2+v^2)/2 and q=(u-v)^2/(4r), with zero-r pairs omitted. Direct pairwise entropy decomposition gives

Delta_i=JS(u^2,v^2)+sum_s r_s h_2(q_s), and alpha=sum_s r_s q_s.

Both terms are nonnegative. By concavity, sum r_s h_2(q_s)<=h_2(alpha).

For nonnegative p,q, their contribution to JS in natural logarithms is

J(p,q)=1/2 [p ln(2p/(p+q))+q ln(2q/(p+q))].

Set t=|p-q|/(p+q) in [0,1]. Then J=(p+q)/2 * L(t), where L(t)=ln 2-h_n((1+t)/2). We have L'(t)=atanh(t), while R(t)=1-sqrt(1-t^2) has derivative t/sqrt(1-t^2). The latter dominates atanh(t): both vanish at zero, and its derivative (1-t^2)^(-3/2) dominates (atanh)'(t)=(1-t^2)^(-1). Since L(0)=R(0)=0, L<=R, including endpoints by continuity. It follows that

J(p,q)<=1/2 (sqrt(p)-sqrt(q))^2.

Apply p=u_s^2,q=v_s^2 and sum. Since (|u_s|-|v_s|)^2<=(u_s-v_s)^2, JS in bits is at most 2alpha/ln 2. Replacing f by x_i f preserves H(f) and the two restriction entropies, while replacing alpha by 1-alpha. This proves the symmetric upper bound. Finally -(1-alpha)ln(1-alpha)<=alpha proves the stated log-cost bound. At alpha=0 or 1, the restrictions are respectively equal or opposite and Delta_i=0.

Sharpness. For the saved one-point bent selector with alpha=1/N and even m=log_2 N, the bounds in INDEPENDENT_DERIVATION.md give

Delta_i/alpha - log_2(1/alpha) -> 3/ln 2.

Therefore any universal additive coefficient in Delta_i <= alpha log_2(1/alpha)+c alpha must satisfy c>=3/ln 2. No numerical limit is used.

Limit: the logarithmic dependence on 1/alpha remains. Removing it by coordinate selection or a justified global aggregate bound is precisely the missing FEI step. This is a coordinate estimate, not a proof of P0162.
