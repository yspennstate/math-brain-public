# A dimension-uniform remainder certificate and numerical scope check

Fix even d>=2, delta=2^-d, t=sqrt(delta), e=delta/2. Use actual F_d=b(y)+1_(y=0)(q(u,v)-1), where b is the product of quadratic two-bit bent signs and q=-1 only at (1,1). Work in bits and with physical flip influence. All logarithms in this proof are natural only when denoted ln.

Product character expansion gives the four signed amplitudes over a core set T:

    sigma_T t-delta/2, delta/2, delta/2, -delta/2.

Every amplitude is nonzero. The sign probabilities under a uniform core Fourier set are p_+=(1+t)/2, p_-=(1-t)/2. Each pair query has influence e, positive erasure, and complete laws mu(T,V)=delta/2, r(T,0)=delta c_sigma, r(T,1)=delta^2/2, where c_sigma=1-sigma t+delta/2. Summing the complete reference gives (1-e,e); the binary derivative law is (1/2,1/2). Conditional core laws agree at V=1. At V=0 the derivative is uniform and the reference is delta c_sigma/(1-e). Thus

    D_full=D_binary+D0/2,
    D0=sum_sigma p_sigma log2[(1-delta/2)/c_sigma],
    L_i=e D0/2,    L_u+L_v=delta D0/2.

The full normalization and this KL chain rule are exact. No derivative-free reference atom is removed. These reconstruct A073's signed amplitudes and remainder formula without importing its checker.

Let C take c_+,c_- with probabilities p_+,p_-. Its mean is b0=1-delta/2 and its variance is delta(1-delta). Since c_-<=13/8 on 0<t<=1/2, the strong concavity of ln on [c_+,c_-] implies

    ln(b0)-E ln C >= Var(C)/(2 c_-^2).

Consequently D0 >= [24/(169 ln2)] delta > (24/169)delta>0; the strict simplification uses ln2<1, and 1-delta>=3/4. This rational lower bound supplies a dimension-uniform positive sign even when a floating evaluation returns zero or negative. It is not an assertion that fixed-term logarithm intervals resolve arbitrarily tiny differences numerically.

For an upper bound, put a0=1+delta/2 and r=t/a0. Direct log algebra gives

    (ln2)D0=ln(1-delta/2)-(1/2)ln(1+delta^2/4)+t atanh(r).

For 0<r<1, atanh(r)=integral_0^r (1-z^2)^-1 dz < r/(1-r^2). Also ln(1-delta/2)<-delta/2 and ln(1+delta^2/4)>0. Hence

    (ln2)D0 < delta[(1+delta/2)/(1+delta^2/4)-1/2]
             <= (5/8)delta.

The exact positive atanh series gives ln2>2/3. Therefore

    (24/169)delta < D0 < (15/16)delta,
    0<L_i/e < (15/32)delta,
    0<L_u+L_v < (15/32)delta^2.

Each core coordinate has influence (1+delta)/2: on the gate's one negative input, the edit adds a previously nonpivotal edge at zero, and that gate input has probability 1/4. Since delta<=1/4,

    (15/32)delta^2 <= (3/64) Inf_(y1).

Indeed this last comparison is equivalent to 20delta^2<=1+delta; equality occurs at delta=1/4 and the preceding strict bound still leaves strict slack. Thus the two remainder losses together fit a dedicated 3/64 fraction of one specified core coordinate, reducing A073's stated 1/10 allowance. This is only a partial ledger for these two losses; the same fraction cannot also pay another charge. None of the retained M_i or full terminal entropy is included in this allocation.

Taylor expansion of the displayed exact expression at delta=0 gives D0=delta/(2ln2)+O(delta^2). Therefore each loss L_i=delta^2/(8ln2)+O(delta^3), and the pair loss is delta^2/(4ln2)+O(delta^3). This asymptotic is a consequence of the exact expression, not used to decide a finite sign or allocate the reserve. The rational bounds above alone close the all-dimensional certificate.

A073's original uniform remainder margin and its growing retained row price survive. The checker independently verifies every original finite law and the new rational envelope on the frozen physical cases, and supplies a certified counterexample only to a naive binary64 evaluation of D0. There is no failure of A073@1 or A098's full-scope acceptance. Signed amplitudes and complete probability normalizers, rather than a rounded zero residual, govern the result.

For the remaining original clauses, the exact polynomial 7c_+-5b0=(2-3t)(1-2t)>=0 gives D0<=log2(7/5), and 7^128<2^63*5^128 gives D0/2<63/256. The new stronger bound D0/2<15delta/32<=15/128 also implies that margin directly. Both losses fit the original 1/10 fraction because 3/64<1/10. Complete row algebra gives M_i/e=1+(1/2)log2((1-e)/e)-D0/2>d/2+3/4, since (1-e)/e=2^(d+1)-1>=2^d. Total influence is d/2+(d/2+1)delta, and H<=d+2 gives H/I<=2+4/d<=4. These clauses are reconstructed without changing A073's original statement.

Executed negative control: on the frozen even-d scan 2..1080 the specified formula first returns a nonpositive result (exact floating zero) at d=104. Fixed 48-term rational log intervals separately certify its true D0>0. No negative value occurred in that scan. The directly squared gate amplitude (delta/2)^2 first rounds to zero at even d=538; the query influence delta/2 first rounds to zero at d=1074; delta itself first rounds to zero at d=1076. These are implementation-specific smallest values for the frozen formula and ordered domain, not global minima over algorithms. For every finite dimension all these mathematical quantities remain strictly positive. The all-dimensional rational envelope guards the bridge without depending on representability or a dimension cutoff.

The first unsupported universal line is still a finite dimension-independent bound on M(f)/I(f), equivalently the complete terminal-core KL payment. This small remainder certificate does not provide that payment, and even this family has M_i/e growing with d. NEXT must audit an actual non-product conditional row whose remainder and retained terminal bill are assigned once to available child slack, with every complete reference atom retained.
