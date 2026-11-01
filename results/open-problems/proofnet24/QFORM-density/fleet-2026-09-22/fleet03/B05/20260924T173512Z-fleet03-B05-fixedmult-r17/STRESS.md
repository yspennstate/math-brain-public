# Exact strict-no-pivot stress family

Fix c=tau=99/1000 and 0<delta<=1/25. Set r=(1,0,-delta)^T and w=(delta,0,1)^T. Define

B_delta=tau*(w r^T+r w^T)/(1+delta^2),
C_delta=c*[[0,delta],[1,0],[0,1]].

Then r is perpendicular to w, C_delta^T r=0, and B_delta r=tau w. Thus v=r/sqrt(1+delta^2) spans ker(C_delta^T) and v^T B_delta v=0.

The cross product of the two columns of C_delta is c^2 r. Hence the bordered vector d=B_delta(c^2 r) is exactly
d=c^2 tau (delta,0,1)^T.
Therefore sum_h d_h^2=c^4 tau^2(1+delta^2)>0 while the null-square curvature is exactly zero.

Let T be the two crossing-bank columns. The literal cross seed and successor are
det C_delta[{1,2},T]=-c^2 delta,
det C_delta[{2,3},T]=c^2.
The shared bordered determinant using self column 3 is d_3=c^2 tau. Hence d_3/seed=-tau/delta, whose magnitude diverges as delta decreases. A large bordered-residual-to-seed ratio therefore does not force null-direction square curvature.

Embed these blocks in the symmetric 5 by 5 matrix A_delta=[[B_delta,C_delta],[C_delta^T,0]]. For delta<=1/25,
max |A_ii|<0.00792<0.01,
max off-diagonal modulus<=0.099<sqrt(0.0101),
and every nonzero principal 2 by 2 determinant is nonpositive with absolute value at most max(c^2,tau^2)=0.009801<0.01. Thus the family lies strictly inside the eta=1/100 scalar/pair no-pivot collar.

At delta=1/25:
Delta=30066655113/312500000000000,
d1=970299/25000000000,
d2=0,
d3=970299/1000000000,
seed=-9801/25000000,
successor=9801/1000000,
and d3/seed=-99/40.

The local spectrum is {0,+/-c,+/-sqrt(tau^2+c^2(1+delta^2))}. Scaling the whole matrix by 1/c and using c=tau gives {0,+/-1,+/-sqrt(2+delta^2)}. Hence the same alignment failure occurs inside an actual unrestricted QFORM target matrix with four eigenvalues of modulus at least one. This is not a counterexample to bounded density and is not an s7 example; it only refutes the structural inference that bordered-star mass automatically supplies null-square curvature.