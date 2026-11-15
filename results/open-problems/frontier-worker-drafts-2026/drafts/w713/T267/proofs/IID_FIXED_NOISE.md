# Iid finite-support samples with fixed label noise and unit-norm ReLU teacher

T267 / Target 1 / C013 / proof draft (unaudited); novelty unestablished.
This removes stratification and vanishing label-noise amplitude from C010.
The remaining finite population support, paired initialization, tangent-
kernel limit and averaging over label noise are substantive restrictions.

## 1. Statement

Use C010's four unit inputs x_(s,t), uniform population distribution and
centered unit-norm ReLU teacher g_e=alpha_e(s+t+st). Fix nu in (0,1] and
label-noise amplitude sigma in (0,1], independently of feature scale e.
Take n(e)=ceil(sigma^2/alpha_e^2) independent population input samples,
and label each by g_e(x)+epsilon, with independent epsilon uniform +/-sigma.
Initialize an even-width two-layer ReLU net by independent Gaussian pairs
with equal hidden weights and opposite readouts +/-nu, as in C010.
Training inputs, label noises and initialization are mutually independent.
Train all parameters by simultaneous GD at step gamma=1/2 on empirical
squared loss divided by 2n(e). No post-initialization parameter tying.

Let Q_(m,e)(k) be clean population squared risk averaged over all training
label noises, conditional on input samples and network initialization.
Use C010's rates b_h and witness times k0,k1,k2,k3, and its central integer
interval I_e with B=log[b1/(b2+b12)]. Then in the iterated even-width-first,
feature-scale-second limit, with probability tending to one over iid
training inputs and initialization:

Q(k0)>Q(k1)<Q(k2)>Q(k3),
(Q(k0),Q(k1),Q(k2),Q(k3))/alpha_e^2 -> (4,7/2,4,3),

and every maximizer k_peak on I_e is interior and satisfies
b1 k_peak-B ->0. In particular

k_peak ~ (4pi/nu^2) e^(-1) log(1/e).

All convergence in probability uses the order lim_(e->0) limsup_(m->infinity)
of each failure probability. Sample size n(e) grows as 4sigma^2 e^(-4);
it is fixed during each width limit. The theorem does not assert high
probability over realized labels; risk itself averages over label noise.
No Gaussian-input or full Target1 solution is claimed.

## 2. Collapse repeated inputs exactly

Let N_i be the count of population point i, p_i=N_i/n, and
D=diag(4p_i). On the event all N_i>0 let bar y_i be the mean label in cell i.
The empirical loss equals

(1/2) sum_i p_i (f(x_i)-bar y_i)^2 + a parameter-independent constant.

Consequently every parameter update is exactly the update on these four
cell means with weights p_i. Conditional on counts, the cell-mean noise
has mean zero and diagonal covariance

V=diag(sigma^2/N_i)=(4sigma^2/n)D^(-1).

No Gaussian approximation or independence of Walsh coefficients is used.
The test law remains uniform on the population support, including when
the realized training counts are unequal.

## 3. Count concentration

Put delta=||D-I||. Each diagonal deviation has mean zero and variance 3/n,
because N_i is binomial(n,1/4). Chebyshev plus a union bound gives

P(delta>r)<=12/(n r^2).

Take r=e^(3/2). Since n is asymptotic to 4sigma^2 e^(-4), the failure
probability is O(e), for fixed sigma. For all small e, on the resulting
good event delta<=e^(3/2)<1/2, every cell is nonempty and
D lies between (1-delta)I and (1+delta)I. This is the only sample-count
event used. There is no fixed-count conditioning in the final theorem.

## 4. Weighted frozen-kernel stability without a slow-gap denominator

Let C be C009's deterministic full initial tangent matrix, with ||C||<=1,
and A=I-gamma C, gamma=1/2. Compare zero-start prediction iterations
using C and C D, both with the SAME cell-mean label vector bar y.
Write their residuals r_I(k),r_D(k) and prediction difference d(k).

The matrix I-gamma C D is similar, by D^(1/2), to the symmetric matrix
I-gamma D^(1/2) C D^(1/2). The latter has eigenvalues in [0,1] when
delta<=1/2, since gamma||D|| ||C||<=3/4. Thus

||r_D(k)|| <= kappa_delta ||bar y||,
kappa_delta=sqrt((1+delta)/(1-delta))<=sqrt(3)<2.

Subtracting the two iterations and using d(0)=0 gives

d(k)=-gamma sum_(j=0)^(k-1) A^(k-1-j) C(D-I)r_D(j).

For l>=0, spectral calculus yields
||gamma C A^l||<=1/(l+1): each eigenvalue is a(1-a)^l with a in [0,1/2],
whose maximum is bounded by 1/(l+1). Therefore

||d(k)||<=kappa_delta delta H_k ||bar y||,
H_k=sum_(j=1)^k 1/j <=1+log k, k>=1.

The crucial feature is logarithmic time growth rather than division by
the smallest eigenvalue of C. This argument does not assume that C and D
commute. For k=0 the difference is zero and H_0=0.

## 5. Uniform noise-averaged risk comparison

Let Q_D(k) denote the clean frozen risk using C D and the actual cell-
mean noise. Let Q_I,V(k) use C and the same noise covariance V. Since
||g||^2=12alpha^2 and tr V<=32alpha^2 on delta<=1/2 (n>=sigma^2/alpha^2),
E||bar y||^2<=44alpha^2<49alpha^2 and ||g||<4alpha.
The unweighted predictor has norm at most ||bar y||, and the weighted
predictor has norm at most (1+kappa_delta)||bar y||. Combining the risk
identity | ||a||^2-||b||^2 |<=||a-b||(||a||+||b||) with Section4 and
Cauchy--Schwarz, and dividing by four for the uniform population, gives

max_(k<=T)|Q_D(k)-Q_I,V(k)|/alpha^2 <=126 delta H_T.

For clarity this constant follows from kappa_delta<2,
(2+kappa_delta)E||bar y||^2+2||g||E||bar y|| <=252alpha^2;
the outside factor is kappa_delta delta H_T/4<delta H_T/2.

Now compare V with the balanced covariance V0=(4sigma^2/n)I.
The unweighted prediction noise map B_k=I-A^k has norm at most one.
Its risk covariance perturbation is at most

(1/4)||V-V0||_* <=4(sigma^2/n)delta/(1-delta)<=8alpha^2 delta.

Balanced covariance has Walsh variance sigma^2/n, while C010 uses alpha^2.
Let rho_round=sigma^2/(nalpha^2). Rounding n upward gives
0<=1-rho_round<=alpha^2/sigma^2. Each of four mode noise filters is at
most one, so the corresponding risk error is at most 4alpha^4/sigma^2.
Consequently, for C010's baseline zero-output curve Q_e^0,

max_(k<=T)|Q_D(k)-Q_e^0(k)|/alpha^2
 <=126 delta H_T+8delta+4alpha^2/sigma^2.

Choose T=ceil(e^(-5/2)). On the count-good event the right side is
O(e^(3/2)log(1/e))+O(e^4)=o(e). This is smaller than both C010's constant
normalized witness margins and its normalized central peak gap of order e.
All covariance arguments use exact second moments, not a central limit
approximation or a numerical experiment.

## 6. Actual nonlinear GD comparison under cell weights

We spell out the weighted extension of C010's finite-horizon argument.
On the count-good event ||D||<=3/2. For small e, each cell-mean label has
absolute value at most sigma+3alpha<2, hence ||bar y||<=4. The network
starts at zero. Use the deterministic neuronwise bounds of C009 with
R_0=4, S=14, L=2, n0=4, and replace its c_k by

gamma L (3/2)R_k/n0.

In its residual recurrence multiply the readout-kernel gradient term by
3/2 as well; the feature-motion term is already expressed through c_k.
This follows directly from replacing r by D r in both exact parameter
updates and bounding ||D r||<=3R/2. All resulting constants through a
fixed T are finite and uniform over D in [I/2,3I/2] and labels in [-2,2]^4.

Gaussian norm bounds, independent-pair strong laws, initial kernel
convergence and weighted initial gate-band mass are unchanged, since the
four possible input vectors are unchanged. Kernel drift and the exact
discrete-step gate remainder tend uniformly to zero. The frozen iteration
uses C D; its powers are bounded by sqrt(3) by Section4, so telescoping
still transfers predictions uniformly through T. Crucially the argument
is uniform over all bounded cell-mean label vectors; it does not take a
union over 2^n noise realizations or assume independent adaptive gates.
Uniform prediction control and the finite-horizon deterministic bounds
transfer noise-averaged risks as width tends to infinity for each fixed e.
Division by the fixed positive alpha^2 e is legitimate at this stage.

Thus max_(k<=T)|Q_actual(k)-Q_D(k)|/(alpha^2 e)->0 in probability over
initialization as width grows, on the count-good event, uniformly in its
counts. This claim does not give a uniform-in-e practical width threshold.

## 7. Witness and peak transfer, and remaining scope

The sample event fails with probability O(e). On it, Section5 gives
uniform surrogate-risk error o(alpha^2 e), and Section6 adds a vanishing
fixed-e width error. C010's positive risk witnesses and central peak
value gaps therefore transfer, first taking width to infinity and then
e to zero. Its entire integer peak interval and k3 lie below T for all
small e. The teacher identity and full tangent-kernel clocks are unchanged.
This proves the stated restricted theorem.

Fixed label noise, unit teacher norm and iid sampling are now explicit,
but n grows as e^(-4), the test population has only four atoms, readouts
are paired, risk averages over label noise and the proof is in a tangent-
kernel limit. It is not a generic Gaussian-design, macroscopic feature-
learning, realized-label high-probability, fixed-n, all-time, full-target
or novelty claim. C009/C010 and the uniform weighted nonlinear extension
await independent review. That extension is the least-trusted proof step.
No network training, dataset generation or large computation is needed.
