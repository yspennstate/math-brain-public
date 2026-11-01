SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B07, 2026-09-24T05:34:10Z.
attacking: fleet03/B07 r44's literal physical near-rank-two crossing; replace ordinary Frobenius-tail reasoning by an exact second/third exterior-volume split, then stress the surviving fan by an original-coordinate diffuse construction.

Early calculation.  Let x1>=x2>=... be the squared singular values of the r44 physical crossing C, put
M=x1*x2, T=sum_{j>=3} xj, U=sum_{3<=i<j} xi*xj, R=e2(x)-M, V=e3(x).
Then exactly
R=(x1+x2)T+U,
V=M*T+(x1+x2)U+e3(x_{>=3}).
Consequently
T<=V/M,
U<=V/(x1+x2),
R-x1*T=x2*T+U<=2V/x1,
and x2*R<=2V, hence R<=2V/x2.

For the partner constants V<1/64 and s1*s2>gamma=1.19876993884320, M>gamma^2=1.437049366274..., so T<1/(64 gamma^2)=0.010872973725....  If s2>=1/2 then R<1/8, so the leading (1,2) exterior singular mode carries > gamma^2/(gamma^2+1/8)=0.9199769208 of the full E2 volume.  If s2<1/2 then s1>2 gamma and the whole nonleading E2 packet differs from the common-factor fan x1*T by <2V/x1<0.005436.  This is the branch to analyze; ordinary ||C-C2||_F smallness is not the invariant.
