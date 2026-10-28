# Alternating priority lists force a controller coefficient at least pi?/(2 ln 2)

The result concerns a local stopping-tree ledger. It is not a lower bound for the full FEI constant. The exact finite certificate gives D/Inf_query > 7.119. The analytic limit is pi?/(2 ln 2), approximately 7.11941466. All statements below have finite Boolean witnesses; entropy is in bits, and ln is natural logarithm.

## 1. The actual Boolean family and its original reserve

Choose integers r,l>=1. Put p=2^-r and b=1-p. On l disjoint r-bit cubes let A_i be the indicator of the all-zero point. Let Z be one fresh fair sign. Set m_i=(-1)^(l-i), E=product_i(1-A_i), and

    K=sum_i m_i A_i product_(h<i)(1-A_h),     F=K+E Z.

Exactly one priority branch is selected, or all tests fail and Z is returned, so F is a Boolean sign on rl+1 coordinates. Query Z FIRST, before any priority control. Both physical children are K+E and K-E; they are not independent copies. Write e=b^l. The actual query influence is e.

One may describe the last core Z as a fair one-bit test selecting constants +1 and -1. Every selected core in this fine representation is a constant, including every earlier m_i. Thus original fine U=R=0 at root AND both query children. No reserve renewal, core variance subsidy or omitted terminal is available. D=H(F)-[H(K+E)+H(K-E)]/2 is the complete decrement. Constants may coincide as values on different priority cells; merging equal constant outputs leaves R=0.

## 2. Exact Fourier packets

For an indicator A of mean p, its failure indicator has empty Fourier coefficient b, nonempty coefficients -Ahat, and nonempty squared mass pb. Therefore under nu(T)=Ehat(T)^2/e the independent nonempty-block flags each have probability p. If the last nonempty block is j and k=l-j, this group has probability p b^k; the all-empty frequency has probability e. Division is legitimate: for point events every Fourier coefficient of every failure block is nonzero, since 0<p<=1/2 and b>0.

For such a last nonempty block, earlier priority terms have a later nonempty frequency and vanish. Direct division gives

    R_k=Khat/Ehat=-m_j/b^k + sum_(h>j) m_h p/b^(l-h+1)
       =[p-2(-1)^k b^-k]/(2-p).

At the empty frequency,

    R_empty=(-1)^(l-1) p[1-(-b)^l]/[(2-p)b^l].

The denominator 2-p is >=3/2. These are exact rational identities. Put eta(x)=-x log2 x, Phi(a,b)=eta(a)+eta(b)-eta(a+b), with eta(0)=0, and

    d(x)=eta(x?)-eta((x+1)?)/2-eta((x-1)?)/2.

Both Phi(x?,1) and d(x) are even and continuous, including x=0,1. Homogeneity cancels the row normalization in each decrement. Consequently

    B_Z/e = e Phi(R_empty?,1)+sum_(k=0)^(l-1) p b^k Phi(R_k?,1),
    D_Z/e = e d(R_empty)+sum_(k=0)^(l-1) p b^k d(R_k).

The second identity explicitly includes BOTH full physical child entropies. No child-channel bound is substituted into D. For every k, b^-k <= |R_k| <= c_p b^-k, where c_p=(2+p)/(2-p)<=5/3.

## 3. The logarithmic moment and its critical exponent

The A059 last-frequency tail t_J has values b^k on the nonempty groups and e on the empty group. Its exact moment is

    E_nu ln(1/t_J)= b(1-b^l)(-ln b)/p.

For s>0,

    E_nu t_J^-s = b^((1-s)l) + p sum_(k=0)^(l-1) b^((1-s)k).

For 0<s<1, summing the upper endpoint of each interval in the decreasing function t^-s gives E t_J^-s <=1/(1-s). Let l tend to infinity and then p=2^-r tend to zero: this bound is sharp. For s=1 the exact value is 1+lp, and for s>1 the expression is unbounded as l increases, even at fixed p. Thus the log-moment constant 1 nat is sharp on actual private point indicators, and substituting a uniformly bounded first inverse-tail moment is false.

This obstruction is present in actual coherent amplitudes too: |R_k|>=t_J^-1 on every nonempty group, so their first absolute moment is >=lp. It is not merely an artificial guard majorant. The coherent logarithmic moment reaches 1 nat in the same small-p/deep-list limit (the multiplicative c_p error tends to 1, and the empty atom vanishes). This does not show that every constant in A059's packet upper bound is sharp.

## 4. Finite-to-infinite passage with domination

Take the explicit diagonal l=4^r=p^-2, r tending to infinity. Then e=b^l<=exp(-1/p) tends to zero. Couple all nonempty groups to a uniform variable t in (e,1]: group k is (b^(k+1),b^k]. This interval has length p b^k. If t lies there, 1/t_k <=1/t<=1/(b t_k), t_k=b^k. Thus |R_k| tends to 1/t for each fixed t>0, since b and c_p tend to 1.

Here is a uniform integrable envelope. For x>=1,

    Phi(x?,1) <= [1+ln(1+x?)]/ln2,
    0<=d(x)<=Phi(x?,1)+4/ln2.

The first inequality follows from x? ln(1+1/x?)<=1. For the second let a=(x+1)?, b=(x-1)? and v=x?+1. The nonnegative child-channel gap in natural units is J=[a ln(a/v)+b ln(b/v)]/2. Using ln u<=u-1 gives J <=[(a?+b?)/v-(a+b)]/2=4x?/(x?+1)<=4. Thus this envelope uses only an elementary scalar inequality, not a quoted FEI or log-Sobolev theorem. At 0<=x<=1 continuity gives a finite constant. Hence both functions at |R_k|<=5/(3t) are bounded by C+2 ln(1/t)/ln2, integrable on (0,1]. This is the dominating function, independent of r and l.

The empty frequency satisfies |R_empty|=|EK|/e<=1/e, so its contribution to either moment is at most e[C+2 ln(1/e)/ln2], which tends to zero. Dominated convergence for the coupled nonempty terms therefore proves

    B_Z/e -> integral_0^1 Phi(t^-2,1) dt,
    D_Z/e -> integral_0^1 d(1/t) dt.

The family parameters and the witness depend on r explicitly; no fixed-dimensional continuum object is mistaken for a Boolean witness.

## 5. Evaluation of both limits

In natural units,

    ln2 Phi(t^-2,1)=ln(1+t?)/t? + ln(1+t^-2).

Integration by parts gives the two integrals -ln2+pi/2 and ln2+pi/2. Thus the erasure ratio tends to pi/ln2.

Let A(t)=(1+t)? ln(1+t)+(1-t)? ln(1-t). Then

    ln2 d(1/t)=A(t)/t?-2 ln t,
    A'(t)=2[(1+t)ln(1+t)-(1-t)ln(1-t)]+2t.

The endpoint A(t)/t tends to zero at t=0, because A(t)=3t?+O(t^4); A(1)=4ln2, interpreted continuously. Integration by parts yields

    integral_0^1 [A(t)/t?-2ln t]dt
      =2 integral_0^1 ln((1+t)/(1-t))/t dt
      =4 sum_(j>=0) 1/(2j+1)? = pi?/2.

For the series step, ln((1+t)/(1-t))/t=2 sum_(j>=0)t^(2j)/(2j+1) has nonnegative summands, so monotone convergence justifies integration. The classical Basel identity evaluates the odd-square sum as pi?/8; the exact positive series itself also specifies the constant without that evaluation. All boundary terms and both exchanges are justified above. Thus the claimed limit is pi?/(2 ln2).

## 6. Necessary coefficient, tensorization, and full FEI scope

Any uniform local inequality D_Z H-drop(R)<=C Inf_Z, valid at every unfinished private-priority point query in the ORIGINAL fine ledger, must have C>=pi?/(2ln2). This family uses R=0, even without data interruption, shared data or nonconstant cores. The prior leading-point coefficient Gamma<4.873 cannot be substituted here: earlier unresolved priority outputs create a coherent prefix. A059's current upper coefficient 6+(5+ln10)/ln2<17 remains valid; the new result gives a necessary floor, not an optimal upper coefficient.

For tensor-closed rules with additive per-factor ledgers, use N independent copies of one finite witness and query all N corresponding Z coordinates. Product Fourier entropy is additive at root and every terminal, total spent query influence is N e, and the original fine reserve remains zero in each factor. A fixed additive allowance A becomes A/N; it cannot repair C below the limiting floor. This does not assert the same representation under a new canonical single-controller description, or eliminate an overhead charged PER factor.

The whole function has total influence

    I(F)=e + 2r(1-e)/(2-p) - [r p? b^(l-1)/(2-p) if l is odd, else 0].

The formula follows by summing the actual mismatch edges of each earlier point bit (or the disjoint substitution recurrence). In particular I(F) is asymptotic to r on our even diagonal, whereas Inf_Z=e tends to zero. The large local ratio does not provide a large H(F)/I(F), much less a divergent FEI ratio. The actual unresolved terminal entropies are retained rather than paid. Full FEI remains OPEN.
