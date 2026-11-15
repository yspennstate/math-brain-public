# Fixed nonzero readout variance: a restricted nonlinear GD double-descent theorem

T267 / Target 1 / C009. Proof draft, unaudited; novelty unestablished.
This is a four-point stratified-design, linear-single-index, label-noise-
averaged result. It is not the generic Gaussian-input target.

## 1. Precise statement

Fix 0<nu<=1 independently of feature scale and width. For 0<e<1/4, use
x_(s,t)=(1,e s,e^2 t)/sqrt(1+e^2+e^4), s,t in {-1,1}. The test law is
uniform on these four unit vectors; the training set contains each once.
The teacher is g(x_(s,t))=(s+t)/4, a linear single-index teacher, with vector
(0,sqrt(1+e^2+e^4)/(4e),sqrt(1+e^2+e^4)/(4e^2)). Each label has independent
noise uniformly plus or minus 1/2. Thus n=4 and ||y||<=2.

Train f_m(x)=m^(-1/2)sum_j a_j ReLU(w_j^T x) by simultaneous full-batch GD
of step eta=1/2 on ||f_m(X)-y||^2/(2n). Use derivative 1_{z>0} at each gate.
Initialize w_j iid N(0,I_3), a_j=nu epsilon_j, where epsilon_j are iid
equiprobable signs independent of hidden weights and label noise.
Q_(m,e)(k) is clean population squared risk, averaged over all sixteen
training-noise vectors, conditional on the network initialization.

Let b1,b2 be the positive rates in Section 2. Define
k0=ceil(e^(-1/2)), k1=floor(log(2)/b1),
k2=ceil(e^(-3/2)), k3=floor(log(3/2)/b2), and B=log(b1/b2).
For sufficiently small e these are strictly increasing. Let I_e be the
integer interval with endpoints floor((B-1)/b1), ceil((B+1)/b1).
For any delta>0, in the iterated limit width m->infinity first, then e->0,
the probability tends to one that

Q(k0)>Q(k1)<Q(k2)>Q(k3),

and every maximizer k_peak of Q on I_e is interior and satisfies
|b1 k_peak-B|<delta. More precisely the lim_(e->0) limsup_(m->infinity)
of the probability of failure of their conjunction is zero. Therefore

k_peak ~ (4pi/nu^2) e^(-1) log(2/e)

in this iterated probabilistic sense. This is a central local peak, not
a global maximum over all training times or a uniqueness assertion about
all extrema. No averaging over initialization defines Q.

## 2. Full initial tangent kernel and changed clocks

Write k(r)=[sqrt(1-r^2)+(pi-arccos r)r]/(2pi),
g1(r)=r(pi-arccos r)/(2pi)=r k'(r), and h_nu=k+nu^2 g1.
The deterministic full tangent kernel C_(nu,e) has entries h_nu(x_i.x_l)/4.
This follows by taking expectations of the two Jacobian blocks: the
readout block is the Gaussian ReLU covariance k, and the hidden block is
nu^2 (x_i.x_l) times the Gaussian probability of two positive projections,
(pi-arccos(x_i.x_l))/(2pi). These are the K2 and K1 displays in
Heckel--Yilmaz, arXiv:2007.10099v2, Section 3, pp.9--10. Only their kernel
formulas are used; no risk upper bound is interpreted as a risk sign change.

For a=e^2/(1+e^2+e^4), c=e^4/(1+e^2+e^4), the Walsh eigenvalues in modes
0,1,2,12 are the four signed sums of h_nu(1),h_nu(1-2a),h_nu(1-2c),
h_nu(1-2a-2c), divided by 4, with signs respectively ++++,+-+-,++--,+--+.
The readout-block eigenvalues are O(1),O(e^2),O(e^4),O(e^4), respectively:
use |k'|<=1/2 on the shrinking relevant interval and positive semidefiniteness.

To compute the hidden block put
H(z)=g1(1)-g1(1-2z)=z+(1-2z)arcsin(sqrt(z))/pi.
Then H(z)~sqrt(z)/pi, and H(a+c)-H(a)=O(c/sqrt(a)+c)=O(e^3), by the
derivative bound on a<=z<=a+c. Its mode-1 eigenvalue is
[H(a)+H(a+c)-H(c)]/4~e/(2pi). Its mode-2 and mode-12 eigenvalues are
[H(c)+H(a+c)-H(a)]/4 and [H(c)-H(a+c)+H(a)]/4, each ~e^2/(4pi).
The mode-0 eigenvalue tends to 1/2. Consequently the full eigenvalues obey

lambda0 -> (1+nu^2)/2,
lambda1 ~ nu^2 e/(2pi),
lambda2 ~ nu^2 e^2/(4pi), lambda12 ~ nu^2 e^2/(4pi).

They are positive for small e. The covariance representation makes C
positive semidefinite and its trace is (1+nu^2)/2<=1. Set
q_h=1-eta lambda_h, b_h=-log q_h. Thus q_h in [1/2,1),
b1~nu^2 e/(4pi), b2~nu^2 e^2/(8pi), b12/b2->1,
b1/b2~2/e, and b0 has a strictly positive finite limit.
The interaction mode now learns on the slow clock; it cannot be omitted.

## 3. Finite-horizon transfer for the actual nonlinear discrete GD

For each fixed e,nu and finite T, compare the network to the frozen C
prediction iteration started from its ACTUAL initial prediction f_m(X;0).
Uniformly through T and over all sixteen label-noise vectors, the
prediction error tends to zero in probability as m->infinity.

Here are the details, including nonsmooth gates. Fix M>0 and work first
on ||f_m(X;0)||<=M and mean_j||w_j(0)||^2<=6. Let u_j=1+||w_j(0)|| and
S=14. Use the deterministic recurrences of NONZERO_READOUT.md Section 1
with R_0=2+M instead of 3, L=2, and A_0=B_0=1. Their proof uses only
nu<=1 and an initial residual bound, so gives finite constants through T:

|a_j(k)-a_j(0)|<=H_k u_j/sqrt(m),
||w_j(k)-w_j(0)||<=D_k u_j/sqrt(m),
|a_j(k)|<=A_k u_j, ||w_j(k)||<=B_k u_j, ||r_k||<=R_k.

In these recurrences c_k=eta L R_k/n, H_(k+1)=H_k+c_k B_k,
D_(k+1)=D_k+c_k A_k, A=1+H, B=1+D, and
R_(k+1)=R_k+eta(L^2 S/n)B_k^2 R_k+L c_k S A_k A_(k+1).
They follow from exact simultaneous parameter updates, global ReLU
Lipschitzness and the exact prediction decomposition; no loss descent
or gate stability is assumed.

Let D_*=max_(k<=T) D_k. Every neuron that changes a gate at any training
input through T belongs to the initial band
min_i |w_j(0).x_i|<=D_* u_j/sqrt(m).
The weighted band mass
L_m=mean_j u_j^2 1{min_i|w_j(0).x_i|<=D_* u_j/sqrt(m)}
tends almost surely to zero along iid prefixes. To see this, for each
positive rational t eventually D_*/sqrt(m)<=t. The strong law bounds the
limsup by E[u^2 1{min_i|w.x_i|<=t u}]. Let rational t decrease to zero.
Dominated convergence makes this expectation zero, since E[u^2]<infinity
and each unit-input Gaussian projection is nonzero almost surely. The
countable intersection of strong-law events suffices. This is a uniform
radius-band argument, not independence of adaptively selected gate flips.

The instantaneous tangent kernel is
K(k)=K_RF(k)+(nm)^(-1)sum_j a_j(k)^2 D_j(k)XX^T D_j(k),
where D_j(k) is its diagonal gate matrix. RF drift is bounded as in C008
by (L^2 S/n)(2D_k/sqrt(m)+D_k^2/m). The hidden-block drift is at most
(L^2/n)[2nu H_k sqrt(S)/sqrt(m)+H_k^2 S/m+2nu^2 L_m].
The last term bounds changing diagonal gates by their initial band mass;
the other terms expand a_j(k)^2-a_j(0)^2. Thus max_(k<=T)||K(k)-K(0)||->0
on these fixed-M events. Entrywise strong laws give K(0)->C almost surely;
the finitely many entries have integrable summands and a_j(0)^2=nu^2.

For completeness control the discrete ReLU linearization remainder.
Write Delta h_j=D_j(k)X Delta w_j+s_j. Componentwise, |s_ji| is at most
|x_i.Delta w_j| if the gate changes, and zero otherwise. The exact full
prediction step is
f_(k+1)=f_k-eta K(k)r_k+Z_k,
Z_k=m^(-1/2)sum_j [(Delta a_j)Delta h_j+a_j(k)s_j].
The bounds above give
||Z_k||<=L c_k^2 A_k B_k S/sqrt(m)+L c_k A_k^2 L_m,
which tends to zero. This explicitly retains both feature motion and
gate-crossing errors. Subtract the frozen C iteration with the same
initial prediction and telescope, using ||I-eta C||<=1 and ||r_k||<=R_k.
The finite-horizon prediction error therefore vanishes on the fixed-M
events. Finally E||f_m(X;0)||^2=2nu^2 uniformly in m, so its tail is at
most 2nu^2/M^2. The hidden-norm event has failure tending to zero. Let
M->infinity after m->infinity to obtain convergence in probability.
The same argument is uniform over the finite sixteen-label set.

## 4. Actual risk witnesses, including random initial output

Let v=1/16, and z_h be the Walsh coefficients of f_m(X;0). The teacher
coefficients are theta1=theta2=1/4, theta0=theta12=0. Independent label
noise has mean-zero Walsh coefficients of variance v, so the frozen
noise-averaged risk, conditional on initialization, is exactly

sum_h [q_h^(2k)(z_h-theta_h)^2+v(1-q_h^k)^2].

No independence between noise Walsh coefficients is needed; Parseval
eliminates cross-mode terms. The zero-initial-output version is
Q_e^0(k)=v[(1-q0^k)^2+q1^(2k)+(1-q1^k)^2
                    +q2^(2k)+(1-q2^k)^2+(1-q12^k)^2].
At the four times in Section 1, division by v gives limiting values
3, 5/2, 3, 8/3. The last value uses q2^k3,q12^k3->2/3 and
q^2+2(1-q)^2=3(q-2/3)^2+2/3. Thus all three limiting differences have
strict positive margins, not just a non-monotone upper envelope.

The initial output cannot simply be set to zero. Its coefficients have
mean zero and variance nu^2 lambda_h^RF, exactly for every width, where
lambda^RF are the readout covariance eigenvalues of Section 2. This
follows by centering the independent readout signs. For nonconstant modes
these variances are O(e^2),O(e^4),O(e^4). At all four witness times the
constant-mode contribution has expectation O(q0^(2k0)), tending to zero.
For each other mode the expected absolute perturbation is bounded by
q_h^(2k)[Var(z_h)+2|theta_h|sqrt(Var(z_h))], tending to zero uniformly in
width. Markov's inequality shows that initialization changes these four
frozen risks by o_P(1) as e->0.
The nonlinear prediction transfer in Section 3 changes their risks by
o_P(1) for fixed e as m->infinity: frozen and actual predictions are
bounded in probability and the sixteen noise patterns are finite.
This proves the four strict witnesses in the stated iterated limit.

## 5. Central peak localization

Set z=(B+s)/b1 in the continuously interpolated zero-initial curve Q_e^0.
Uniformly on compact s intervals, differentiation of the six terms gives

(Q_e^0)'(z)/(2v b2)->exp(-s)-1,
(Q_e^0)''(z)/(2v b1 b2)->-exp(-s).

The fast term supplies exp(-s); its quadratic correction is O(b2/b1).
The slow signal/noise term supplies -1, since (b2/b1)(B+s)->0. The
interaction term is now of size O((b12/b2)b12 z)=O((b2/b1)B), still
vanishing here; its normalized second derivative is O(b2/b1). The
constant term is exponentially small. Hence the zero-initial curve has
a unique central strict peak with scaled coordinate s_e->0.

The derivative convergence also supplies a value gap: for each fixed
delta>0 small enough and all small e, the best value on I_e exceeds any
grid value with |b1 k-B|>=delta by at least c_delta v b2/b1, with a
constant c_delta>0. Indeed integrate exp(-s)-1 on each side of zero,
use compact uniform convergence, and note that grid spacing b1 tends
to zero. This also excludes the endpoints from the maximizers.

On I_e the random initial-output perturbation is o_P(e), uniformly in
width. For mode 1, q1^(2k)=O((b2/b1)^2)=O(e^2), so its expected absolute
perturbation is O(e^3). Mode 2 contributes O(e^2); mode 12 contributes
O(e^4); the constant mode decays faster than any power of e. Their sum
is o(e), and b2/b1~e/2. Markov's inequality therefore makes this
perturbation smaller than any fixed fraction of the peak gap with
probability tending to one. For fixed e, Section 3 transfers the risk
uniformly on the finite I_e as m->infinity, so its error is also smaller
than that fixed-e positive gap with probability tending to one.
All actual interval maximizers consequently have |b1 k_peak-B|<delta
and are interior. The clock asymptotics of Section 2 give Section 1's
peak-time formula. This uses probability limits, not an uncountable
almost-sure intersection or an unproved uniform-in-e width limit.

## 6. Limits of the result

Readout variance nu^2 is fixed across feature scales, including nu=1.
The changed peak scale arises from the hidden-weight Jacobian block.
Feature motion at finite width is present and controlled, but the limit
is a tangent-kernel regime, not macroscopic representation learning.
The test support is entirely represented by the stratified training
design. The teacher remains linear, and risk averages over training-label
noise. No generic iid Gaussian-input theorem, high probability over label
noise, practical width threshold, full Target 1 closure or novelty is
claimed. Independent review must check the weighted gate-band argument,
the peak value-gap transfer, and the specialist significance of the model.

Explicit normalization caveat (C009 v3): ||u_e||~1/(4e^2). At unchanged label-noise amplitude, unit-normalizing the teacher changes the four normalized risk limits to 1,5/4,2,20/9. See TEACHER_NORMALIZATION_OBSTRUCTION.md for the exact argument. This is a failure of the current witness construction, not a general impossibility result.

