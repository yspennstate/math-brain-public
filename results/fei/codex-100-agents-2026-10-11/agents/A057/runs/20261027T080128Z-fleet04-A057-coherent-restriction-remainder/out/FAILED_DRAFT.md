# Sharper original whole-core tickets (draft)
All entropies are bits. Let D_i=H(g)-E H(g|x_i), p=Inf_i(g), I=I(g).
Target: D_i <= c I for every finite uniform Boolean g, c=8/3-log2(3)+2/(3 ln2)<41/20.

Let beta(s)=min(2 min(s,1-s),max(s,1-s)). The finite piecewise-linear inequality
 beta((a+b)/2) <= [beta(a)+beta(b)+abs(a-b)]/2, 0<=a,b<=1,
is checked at every vertex of its affine partition (coordinate breakpoints 0,1/3,1/2,2/3,1; diagonal a=b; lines a+b=twice a breakpoint). Cube slicing induction gives I(u)/2>=beta(Pr[u=-1]). Base constants have both sides zero. A slice disagreement has probability >=abs(a-b).
For u=g_0 g_1, I(u)<=I(g_0)+I(g_1)=2(I-p). Consequently I>=p+beta(p); for p<=1/2 this includes I>=min(3p,1). The older isoperimetric bound I>=p+p log2(1/p) also remains available.

The exact Fourier erasure plus amplitude-pair JS estimate gives
 0<=D_i<=h2(p)+min(1,2 min(p,1-p)/ln2).
For p>=1/2, I>=1 and D<=2. For 1/3<=p<=1/2, new bound I>=1 again applies. For 1/4<=p<=1/3, I>=3p; h2(p)/p decreases, so D/I<=[h2(1/4)+(1/2)/ln2]/(3/4)=c.
For 0<=p<=1/4 set F(p)=c p(1+log2(1/p))-h2(p)-2p/ln2. It is continuous, F(0)=F(1/4)=0, and F''=[1/(1-p)-(c-1)/p]/ln2<=0 since c>2 and p<=1/4. Concavity gives F>=0. p=0 gives D=0. All cancellations use p>0; endpoint limits use p log(1/p)->0. Thus D<=c I.

Preallocate TWO tickets (41/20)tI before spending the SAME original(9/2)tI core owner, leaving(2/5)tI. Each pending ticket transports harmonically through already paid physical queries and releases(41/20)t Inf_i. At each of two adaptively selected new queries consume exactly one pending ticket to pay tD and close it. No ticket is renewed; every old cash booking, exact coherent profile and full terminal entropy is retained. Original rate remains9/2 ONLY for this partial claim, not full universal completion (A091 NAND obstruction).

Sharpness claimed ONLY for this scalar envelope, NOT the actual Boolean D/I optimum: at p=1/4 the three bounding scalar inequalities give c. Joint attainability is not asserted. Universal terminal entropy payment remains OPEN. Exact coherent alpha^2 log(1/alpha^2) terms remain inside the source profile and are never replaced by O(alpha^2).
