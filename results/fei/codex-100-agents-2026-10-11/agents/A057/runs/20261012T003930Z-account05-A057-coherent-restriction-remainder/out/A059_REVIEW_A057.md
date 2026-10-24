# Source-bound independent reconstruction of A057 v1

Reviewer A059. Target: A057 run
20261011T220314Z-account05-A057-coherent-restriction-remainder,
REPORT.md and COHERENT_REMAINDER_PAYMENT.tex. Verdict: ACCEPT_AT_STATED_SCOPE,
analytic reconstruction only; no claim of rerunning its 34,392 checks.
A059 supplied no repair to A057's claims. This review was completed before
finalizing the new A059 source-complete candidate, respecting the B12 review cap.

I reconstructed the critical erasure allocation by partitioning a queried
Fourier fiber according to the remaining set U in the queried inner block.
When U is nonempty, the two masses are the queried inner pair multiplied by
the squared outer derivative coefficient and other-block nonempty spectral
probabilities; summing the latter gives one. Its bill is q times the inner
erasure. When U is empty, balancedness eliminates the inner empty coefficient,
so the composed pair instead has masses a_T^2 and alpha^2 b_T^2. Its bill is
L_j(alpha^2). The corresponding pair in the inner itself has masses 0 and
alpha^2 and bill zero. Thus no pair is counted twice and B_i(F)=q B_i(h_j)+L.

For the decrement, restriction changes the inner mean to +/-alpha. The empty
sector is a+/-alpha b and its averaged entropy must retain the signed cross
term. Averaging removes that cross term only in the OTHER-block entropy
weights. This gives the displayed raw R=L+J. The two raw signed vectors have
the same total squared mass because <a,b>=0, following from Booleanity ab=0.
Concavity gives the stated upper bound for L. The JS-Hellinger inequality gives
J<=one half of the squared distance between absolute-value vectors, namely
2 sum_T min(a_T^2,alpha^2 b_T^2)<=2q alpha^2. Its scalar proof is obtained
by differentiating u/sqrt(1-u^2)-atanh(u), which has nonnegative derivative
and vanishes at zero. Nonnegativity and zero-mass endpoints are valid.

For the physical log payment, alpha=E D_i h, |D_i h| is the pivotal
indicator, and |alpha|<=Inf_i(h). Maximize a ln(1/a^2) at a=e^-1 to get
q alpha^2 ln(1/alpha^2)<=(2/e)q Inf_i(h)=(2/e)Inf_i(F).
The fair physical-tree conservation identity follows by averaging the
remaining-coordinate pivotal indicators after each query. Its telescoping
retains terminal influence and cannot reuse a queried coordinate. This proves
both v1 claims at their stated balanced-representation and finite-physical-tree
scope. Biased descendants and the scaled outer-erasure/terminal bank remain
unpaid exactly as the original source says. Summing the root bank by formula
depth is not licensed; A059's counterfamily independently exposes why a
whole-subformula replacement repeats the same deficit.
