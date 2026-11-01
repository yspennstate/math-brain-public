# Substantive checkpoint: ambient ruled-bank compiler

Let S be an ORIGINAL-coordinate three-set such that B=A_{S,S} is invertible indefinite, and set kappa_S=sigma_min(B). After conditioning on W=X_{S^c} and completing the square only in the original active coordinates, define the conditional critical value c_S(W) and the majority event M_S by the multiplicity-two sign of B. The completed fleet02/B15 rough ruled theorem gives the submeasure

nu_S^+(I)=P(Q in I, M_S)

an interval-density cap

nu_S^+(I) <= (pi sqrt(2)/kappa_S)|I|

for every interval I, despite arbitrary outside quadratic coefficients/couplings.

For K_{eps,t}(u)=eps^{-2}(eps-|u-t|)_+, integral K=1, this immediately gives the SOURCE-LEVEL inequality

E[K_{eps,t}(Q) 1_{M_S}] <= pi sqrt(2)/kappa_S.       (1)

For any finite bank of such physical blocks and weights w_S>=0, sum w_S=1,

F_{eps,t} * alpha_bar_{eps,t}
 <= pi sqrt(2) sum_S w_S/kappa_S,                    (2)

where F_{eps,t}=E K_{eps,t}(Q) and alpha_bar is the K-posterior weighted majority coverage

alpha_bar = sum_S w_S P_{eps,t}(M_S),
 dP_{eps,t}=K_{eps,t}(Q)dP/F_{eps,t}.

Hence any lower bound alpha_bar>=delta>0 pays the WHOLE tent height:

F_{eps,t} <= (pi sqrt(2)/delta) sum_S w_S/kappa_S.   (3)

Choosing w_S=kappa_S/sum_T kappa_T gives

F_{eps,t} <= pi sqrt(2) N/[delta sum_S kappa_S].      (4)

Thus if the bank has mean kappa at least c*s_3(A), then

s_3(A) F_{eps,t} <= pi sqrt(2)/(c delta).             (5)

This is a safe ambient replacement for trying to average the partner's exact-rank-three global-heat-mode inequality across conditioned blocks: the random critical values c_S(W) cause no mismatch because (1) is a submeasure domination before averaging. It retains original-coordinate product provenance and pays reciprocal local conditioning only after bank averaging.

Remaining gap: prove, from the bare three-large-eigenvalue hypothesis, a bank with both aggregate kappa and nontrivial posterior majority coverage (or combine this certificate with the existing diffuse/ridge exits). Full QFORM remains open.
