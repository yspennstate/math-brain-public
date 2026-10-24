# A fixed-volume divergence does not force successive limits

This independently derived counterexample concerns one sentence after w480's L3. It is not a weak-disorder Anderson result. w482 review is pending.

Let N>=16, v_j=-1+(2j+1)/N for j=0,...,N-1, D_N=diag(v_j), and u_N=N^(-1/2)(1,...,1). Express D_N in an orthonormal basis whose first vector is u_N. Its top-left entry is the mean of the v_j, namely 0, and its block decomposition is [[0,h_N^*],[h_N,B_N]]. Thus B_N is a finite self-adjoint cavity and ||D_N||<=1. Put

g_N(z)=<u_N,(D_N-z)^(-1)u_N>=(1/N)sum_j (v_j-z)^(-1),
b_N(E,eta)=eta+Im<h_N,(B_N-E-i eta)^(-1)h_N>.

The exact Schur identity implies b_N=Im g_N/|g_N|^2. This denominator is nonzero for eta>0 because Im g_N>0.

Take J=(-1/2,1/2) and eta_N=N^(-1/4). Compare g_N with g(z)=(1/2)integral_{-1}^1 (v-z)^(-1) dv. The midpoint Riemann-sum error is at most 1/(N eta^2): the derivative of (v-z)^(-1) has absolute value <=eta^(-2), and integrating the distance from each interval's midpoint gives this bound (indeed a factor two better is available). Hence at eta=eta_N, |g_N-g|<=N^(-1/2)<=1/4.

For E in J and eta<=1/2, integrating over [E-eta,E+eta] gives Im g>=pi/4. Also

Re g=(1/4)log(((1-E)^2+eta^2)/((1+E)^2+eta^2)),
|Re g| <= (1/2)log 3, Im g<=pi/2.

Let C=(1/2)log 3+pi/2. Thus |g_N|<=C+1/4 and Im g_N>=pi/4-1/4>=pi/8. Consequently

b_N(E,eta_N) >= c = pi/[8(C+1/4)^2] > 0,
integral_J log(1+1/b_N(E,eta_N)) dE <= |J| log(1+1/c),

uniformly in N>=16. Nevertheless for each fixed N, b_N(E,eta)->0 at every energy outside the finite spectrum of B_N, and the same logarithmic integral diverges like |J| log(1/eta), exactly as w480's L3 states.

The volume parameter N and height eta_N can therefore tend to their limits together while the logarithmic functional stays bounded. One does not have to take the volume limit separately at every fixed eta. An Anderson proof would still need its own uniform estimate and justified transfer; this example does not provide those. The corrected conclusion is: fixed finite volume cannot prove the infinite-volume criterion, and any successive or coupled limiting scheme needs independently established uniform control.

NEXT: Have w482 check the midpoint bound and Schur conversion; retain the fixed-volume theorem while correcting the claimed necessity of successive limits.
