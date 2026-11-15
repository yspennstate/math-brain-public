# Small fixed nonzero random readout preserves the four-point witnesses

T267, Target 1, C008. Status: sketch; analytic proof and novelty unaudited.
This removes the exactly-zero readout restriction from C007, with the other
restrictions retained. Its peak transfer allows readout variance to depend on feature scale;
it does not prove generic Gaussian-input double descent or novelty.

## Statement and scope

Use the four-point inputs, stratified training design (n=4), uniform test
law, linear single-index teacher, independent plus/minus 1/2 label noise,
network normalization, loss and step eta=1/2 of C007, as specified in
FOUR_POINT_DISCRETE_GD.md. In particular clean risk Q is averaged over all
sixteen training-noise vectors, conditional on network initialization.
For a fixed sufficiently small feature scale e, let the four C007 witness
times be k0<k1<k2<k3=T. Write gamma>0 for the smallest of its three limiting
risk differences. The positivity of gamma is the analytic input from C007;
it remains unaudited, not an independently checked premise.

Initialize w_j independently N(0,I_3), and initialize a_j=nu epsilon_j,
where epsilon_j are independent equiprobable signs, independent of hidden
weights and label noise. For each requested failure tolerance alpha in
(0,1), there is a nu>0, fixed independently of width, such that the actual
network has the same three strict expected-noise risk differences with
probability at least 1-alpha for every sufficiently large width m.
Both layers are updated simultaneously by GD. The choice of nu may depend
on e and alpha, and may be extremely small. This is not a theorem for an
arbitrary prescribed O(1) readout variance, nor probability tending to one
at one fixed nu. No averaging over initialization defines Q.

## 1. Uniform finite-horizon deterministic bounds

Put L=2, S=14, Y=2. For initial hidden weights set u_j=1+||w_j(0)||.
Work on the events m^(-1)sum_j||w_j(0)||^2<=6 and ||f_m(X;0)||<=d<=1.
Then m^(-1)sum_j u_j^2<=14=S, by (1+r)^2<=2+2r^2,
and the initial residual norm is at most 3. Assume 0<nu<=1.

Set H_0=D_0=0, A_0=B_0=1, R_0=3. Define successively, for k<T,

c_k=eta L R_k/n,
H_(k+1)=H_k+c_k B_k,
D_(k+1)=D_k+c_k A_k,
A_(k+1)=1+H_(k+1), B_(k+1)=1+D_(k+1),
R_(k+1)=R_k+eta (L^2 S/n) B_k^2 R_k
                 +L c_k S A_k A_(k+1).

All these nonnegative constants are finite for fixed T and do not depend
on m, nu, the initialization, or the label-noise realization. Inductively,

|a_j(k)-a_j(0)|<=H_k u_j/sqrt(m),
||w_j(k)-w_j(0)||<=D_k u_j/sqrt(m),
|a_j(k)|<=A_k u_j, ||w_j(k)||<=B_k u_j,
||f_m(X;k)-y||<=R_k.

Indeed the simultaneous parameter updates and ||X||op<=L give
|Delta a_j|<=c_k||w_j(k)||/sqrt(m) and
||Delta w_j||<=c_k |a_j(k)|/sqrt(m). The first four bounds follow.
For the residual bound use the exact prediction identity in Section 2,
||K_RF(k)||op<=(L^2 S/n)B_k^2, and its coarse remainder bound
||E_k||<=L c_k S A_k A_(k+1). This proves the R recurrence without assuming
loss descent or gate stability. At zero preactivation use derivative zero.

## 2. Exact identity and the refined error

Let h_j(k)=ReLU(Xw_j(k)),
K_RF(k)=(nm)^(-1)sum_j h_j(k)h_j(k)^T, K_m=K_RF(0).
The exact simultaneous-update identity is

f_m(k+1)=f_m(k)-eta K_RF(k)(f_m(k)-y)+E_k,
E_k=m^(-1/2)sum_j a_j(k+1)[h_j(k+1)-h_j(k)].

This includes feature motion. Only global Lipschitzness of ReLU and the
bound on its chosen derivative are used, so gate crossings are allowed.
The first-layer displacement bound implies

||K_RF(k)-K_m||op <= (L^2 S/n)(2D_k/sqrt(m)+D_k^2/m).

Use the sharper estimate |a_j(k)|<=nu+H_k u_j/sqrt(m), rather than A_k u_j.
Since mean u_j<=sqrt(S)<4, the remainder satisfies

||E_k|| <= L c_k [nu^2
       +4nu(H_k+H_(k+1))/sqrt(m)+S H_k H_(k+1)/m].

Define four finite nonnegative horizon constants (sums over 0<=k<T):

F_T=sum L c_k,
G_T=sum 4 L c_k(H_k+H_(k+1)),
J_T=sum eta (L^2 S/n) 2D_k R_k,
M_T=sum [eta (L^2 S/n) D_k^2 R_k+L c_k S H_k H_(k+1)].

On ||K_m-K_e||op<=m^(-1/4), the covariance kernel K_e of C007 has norm
at most 1/2, whence K_m is positive semidefinite with norm<=3/2 and
||I-eta K_m||op<=1. Compare actual predictions to the frozen K_m iteration
started from zero, then compare that to the frozen K_e iteration from zero.
The latter residual norm is at most Y. A telescoping induction gives,
uniformly in k<=T and all sixteen label-noise vectors,

||f_m(X;k)-fbar_e(X;k)|| <=
E(m,nu,d):=d+F_T nu^2+(G_T nu+J_T)/sqrt(m)+M_T/m
                       +eta T Y m^(-1/4).

The initial d term propagates by a contraction. No independence of gates
or trajectory and initialization is assumed. Because all test inputs lie
in the four-point training support and ||fbar_e-g||<=4, the clean risk
error at each time is at most 2E+E^2/4. Averaging over the sixteen label
noise vectors preserves the same bound.

## 3. Probability and choice of nonzero variance

The Gaussian norm and initial covariance estimates from C007 give failure
probability at most 2/(3m)+48/sqrt(m) for the two hidden-weight events used
above. They use Chebyshev and a union bound, not independence of events.

At each unit input x, E[f_m(x;0)^2]=nu^2/2: distinct neuron cross terms
vanish because of independent centered signs. Hence
E||f_m(X;0)||^2=2nu^2 and P(||f_m(X;0)||>d)<=2nu^2/d^2.
Again a union bound suffices, including the event depending on both blocks:

P(all comparison hypotheses) >=
1-2/(3m)-48/sqrt(m)-2nu^2/d^2.

Choose epsilon>0 with 2epsilon+epsilon^2/4<gamma/2. Set
d=min(1,epsilon/4). Choose fixed

0<nu<=min(1, d sqrt(alpha)/2,
                   sqrt(epsilon/(4 max(F_T,1)))).

Then the initial-prediction failure bound is at most alpha/2,
d<=epsilon/4, and F_T nu^2<=epsilon/4. For sufficiently large m the other
three terms in E sum to at most epsilon/2, while
2/(3m)+48/sqrt(m)<=alpha/2. Thus E<=epsilon with probability at least
1-alpha. Each limiting witness difference is at least gamma, while the
sum of its two endpoint errors is strictly less than gamma. All three
strict risk differences therefore survive in the nonlinear GD network.

## 4. Optional finite-grid peak transfer

The same uniform error can also preserve C007's central peak on its finite
integer interval I_e, which lies before T=k3 for sufficiently small e.
Let A_e be the nonempty set of maximizing integers of the limiting Q_e
on I_e. C007 gives A_e in the interior and every element within one step
of its interpolated central peak. The finite gap
Delta_e=max_(k in I_e) Q_e(k)-max_(k in I_e\A_e) Q_e(k)
is positive, since the complement contains the endpoints and is finite.
Choose epsilon above to satisfy additionally
2epsilon+epsilon^2/4<Delta_e/2. The same initialization selection then forces
every maximizer of Q_(m,e) on I_e into A_e, with probability at least
1-alpha for all sufficiently large m. In particular it is an interior
local maximum and obeys |b1 k_peak-log(b1/b2)|<=|s_e|+b1.
Along any sequence e tending to zero and alpha(e) tending to zero, choose
nu(e)>0 and m sufficiently large for each e by these finite inequalities.
Then the scaled localization error tends to zero in probability and the
leading peak scale is 8 e^(-2) log(1/e). This permits variance to shrink
with e. It is NOT a peak asymptotic at one variance fixed across scales.

## 5. Unresolved pieces

The claim uses a fixed nonzero variance at each fixed (e,alpha), but does
not make that variance uniform as e tends to zero. The constants may be
astronomical. It preserves C007's four-point stratified design, linear
teacher and noise-averaged risk. Its peak transfer requires choosing variance with the scale and
finite peak gap; it does not replace a specialist novelty
search or independent analytic review. The hardest remaining Target 1
piece is double descent with peak localization in the intended generic
nonlinear single-index model, not initialization alone.
