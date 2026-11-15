# Unit-norm nonlinear ReLU teacher with paired initialization

T267 / Target 1 / C010 / proof draft (unaudited); novelty unestablished.

This removes the diverging teacher norm in C009, at the price of paired
initialization and noise that shrinks with the signal. It is a restricted
four-point, stratified-design, noise-averaged theorem. It does not establish
the generic iid Gaussian-input target or a fixed-positive-noise result.
The hardest remaining target step is sign-level population-risk control
for a genuinely sampled nonlinear model beyond this finite-support
infinite-width construction.

## Statement

Fix nu in (0,1]. For 0<e<1/4 let D=1+e^2+e^4 and use the same four inputs
x_(s,t)=(1,e s,e^2 t)/sqrt(D), s,t in {-1,1}. Training contains each once;
the test law is uniform on these four points. Let

u_e=(0,e,1)/sqrt(1+e^2),
c_e=e^2/[sqrt(D)*sqrt(1+e^2)], alpha_e=c_e/2,
g_e(x)=ReLU(u_e.x)-E_X ReLU(u_e.X).

The vector u_e has norm one. On this support u_e.x=c_e(s+t), so

g_e(x_(s,t))=alpha_e(s+t+st).

Thus the teacher is genuinely nonlinear even when restricted to the
support: no affine function of x has a nonzero st Walsh coefficient.
The centering constant is the population mean c_e/2. Labels are g_e(x_i)
plus independent equiprobable noise +/-c_e, so the noise standard deviation
is c_e, not a fixed positive constant as e decreases.

Take even width m=2N and initialize each independent pair by
w_(2j-1)=w_(2j)=W_j iid N(0,I_3),
a_(2j-1)=nu, a_(2j)=-nu.
Pairs are independent; the individual neurons are NOT iid. Initially f=0
exactly. Train both layers of every neuron by simultaneous GD at step 1/2,
loss ||f(X)-y||^2/(2n), n=4, with f=m^(-1/2) sum a ReLU(w.x) and gate
convention 1_{z>0}. No symmetry is imposed after initialization.

Let Q_(m,e)(k) be clean population squared risk, averaged over the sixteen
training-label-noise patterns, conditional on initialization. Let b_h be
C009's rates for the full initial tangent kernel h_nu=k+nu^2 g1, with mode
indices 0,1,2,12. Set

k0=ceil(e^(-1/2)), k1=floor(log(2)/b1),
k2=ceil(e^(-3/2)), k3=floor(log(2)/b2),
B=log[b1/(b2+b12)].

In the iterated limit m=2N->infinity first, then e->0, the probability of
failure of the strict witnesses

Q(k0)>Q(k1)<Q(k2)>Q(k3)

tends to zero. More precisely the four risks divided by alpha_e^2 converge
in probability, in that iterated sense, to 4,7/2,4,3.
For every fixed delta>0, every maximizer k_peak on the integer interval
I_e=[floor((B-1)/b1),ceil((B+1)/b1)] is interior and satisfies
|b1 k_peak-B|<delta with probability tending to one in the same iterated
sense. Consequently

k_peak ~ (4*pi/nu^2) e^(-1) log(1/e).

This localizes a central local peak, not a global maximum or all extrema.

## 1. Teacher identity and exact initialization

ReLU(s+t) takes values 2,0,0,0, whose mean is 1/2. Its centered version is
(s+t+st)/2. The unit norm and displayed teacher identity follow directly.
The nonzero interaction coefficient rules out an affine teacher on the
four inputs, even though two projections lie exactly at the teacher's
ReLU kink. No differentiability of the teacher is used in training.

Each pair has exactly cancelling outputs. Its two readout-Jacobian Gram
summands are identical. Its two hidden-Jacobian Gram summands are also
identical because their readout factors are squared. Dividing by m=2N
therefore gives the same expected full kernel as in C009:

C_(nu,e)(i,l)=[k(x_i.x_l)+nu^2 g1(x_i.x_l)]/4.

Strong laws apply to the N independent pairs. No independent-neuron
concentration or centered independent readout-sign argument is needed.

## 2. Transfer from the actual nonlinear GD

Here we specify why C009 Section 3 applies despite correlated pairs.
For e<1/4, c_e<e^2<1/16. The largest absolute teacher value is 3c_e/2;
the largest label magnitude is at most 5c_e/2<5/32. Thus ||y||<5/16<2.
The actual initial output is identically zero; use M=0 and R_0=2 in the
deterministic finite-horizon recurrences of C009 Section 3. Those bounds
are neuronwise and use no independence. They hold separately for both
members of every pair, even after their hidden weights separate.

The empirical mean of initial squared hidden norms converges almost surely
to 3 by the pairwise strong law. The weighted initial gate-band mass is
now exactly the mean over N independent W_j of
(1+||W_j||)^2 1{min_i|W_j.x_i| <= D_* (1+||W_j||)/sqrt(2N)}.
It tends to zero by the same rational-band strong-law and dominated-
convergence argument as C009. The initial kernel converges entrywise to
C by the pairwise strong law. These are the only probabilistic inputs to
the instantaneous-kernel and exact discrete-step remainder bounds in C009.
Their finite-horizon telescoping proof therefore gives

max_(k<=T) ||f_actual(k)-f_frozen(k)|| -> 0 in probability

for every fixed e,nu,T, uniformly over all sixteen noise patterns. The
frozen iteration starts at zero exactly. Here and below T may depend on e;
width tends to infinity separately for each fixed e. This does not claim a
uniform feature-scale rate or a feasible numerical width.

## 3. Risk margins

All three nonconstant teacher Walsh coefficients are alpha=alpha_e.
Independent +/-c_e label noise has Walsh variances c_e^2/4=alpha^2.
Parseval and the zero initial prediction give the exact frozen risk

Q_e^0(k)/alpha^2 = (1-q0^k)^2
                 + sum_(h=1,2,12) [q_h^(2k)+(1-q_h^k)^2],
q_h=exp(-b_h).

C009 Section 2 supplies b1~nu^2 e/(4pi), b2~nu^2 e^2/(8pi),
b12/b2->1, and b0 bounded away from zero. At k0 all nonconstant modes
remain unlearned, giving 1+1+1+1=4. At k1 the fast component has q1->1/2
and the two slow components remain at one, giving 1+1/2+1+1=7/2.
At k2 the fast component has q1->0 while slow components remain at one,
giving 4. At k3 both slow components have q->1/2, giving 1+1+1/2+1/2=3.
The three strict limiting margins are 1/2,1/2,1. For fixed e, alpha>0 and
the finite-horizon transfer changes risk by o_P(1), hence by o_P(alpha^2)
as width grows; division by a fixed positive alpha^2 is legitimate.
Then let e decrease. This proves the four strict actual-risk witnesses.

## 4. Central peak

Interpolate the frozen curve continuously and put z=(B+s)/b1 with
B=log[b1/(b2+b12)]. Uniformly for s in compact intervals,

(Q_e^0)'(z)/[2 alpha^2 (b2+b12)] -> exp(-s)-1,
(Q_e^0)''(z)/[2 alpha^2 b1 (b2+b12)] -> -exp(-s).

Indeed each nonconstant mode contributes 2 alpha^2 b_h q_h(1-2q_h).
The fast term contributes exp(-s); its quadratic correction is
O((b2+b12)/b1). The two slow terms contribute -b2/(b2+b12) and
-b12/(b2+b12), up to errors O(((b2+b12)/b1) B). The constant-mode
term and its derivatives vanish faster than any polynomial of e.
The same estimates after one further differentiation give the stated
second derivative. Thus the frozen central peak has scaled coordinate
s_e->0 and a strict value gap away from any fixed delta neighborhood,
of order alpha^2 (b2+b12)/b1, by integrating the derivative on [-1,1].
The grid spacing b1 tends to zero, so discrete maximizers obey the same
localization. When delta>=1, the conclusion follows from any smaller
positive delta, and interval endpoints are excluded as well.

For each fixed e the interval is finite and its positive peak gap is a
fixed positive number. Section 2 therefore transfers the maximizer
localization to the actual risk with probability tending to one as width
grows. No random initial-output perturbation occurs. Finally
b1/(b2+b12)~1/e and b1~nu^2 e/(4pi) give the peak asymptotic.

## Scope and dependencies

This proof depends on the unaudited deterministic bounds and Gaussian
kernel asymptotics in C009, not on an independent audit or a floating-point
fit. Pair cancellation is only an initial condition, not frozen weights.
The centering offset is part of the single-index link ReLU(z)-c_e/2.
The teacher has uniformly unit norm and is nonlinear on the support;
its variation and the label-noise standard deviation both vanish as e^2.
The design remains stratified, finite support, with every test input in
training, and risk averages over labels. No fixed-noise, iid-design,
macroscopic feature-learning, full-target or novelty claim is made.
Primary kernel source: Heckel--Yilmaz arXiv:2007.10099v2 Section 3 K1/K2.
The existence of two noise thresholds in Stephenson--Lee 2108.12006 is not
used to infer that this model has the same noise window.
