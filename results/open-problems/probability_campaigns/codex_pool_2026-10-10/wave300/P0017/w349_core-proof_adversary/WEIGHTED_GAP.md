# A counterexample inside the log-concave localization class

This derivation was completed independently of w348's proof. It isolates a
false expectation factorization, rather than refuting KLS.

Let X=E-1, with E exponential of rate 1. Its law is isotropic and log-concave
in dimension one. At a fixed time s>0 observe Y_s=sX+sqrt(s) Z, where Z is
an independent standard Gaussian. Write mu_{s,y}=Law(X | Y_s=y).
Bayes' formula gives the density

    mu_{s,y}(dx) proportional to
    exp((y-1)x - s x^2/2) 1_{x>=-1} dx.

This is N((y-1)/s,1/s) truncated below at -1. Let
A(y)=Var(X | Y_s=y), and choose the fixed test function f(x)=x. Then

    Var_{mu_{s,y}} f = A(y),
    Cov_{mu_{s,y}}(f,X) = A(y),
    ||Cov(mu_{s,y})||_op = A(y).

The proposed shortcut

    E |Cov_{mu_s}(f,X)|^2
      <= (E ||Cov(mu_s)||_op) (E Var_{mu_s} f)

would therefore say E A(Y_s)^2 <= (E A(Y_s))^2.
It is strictly false. To check strictness, put
a=(-1-(y-1)/s)sqrt(s) and lambda(a)=phi(a)/(1-Phi(a)).
The truncated-normal formula is

    A(y) = [1+a lambda(a)-lambda(a)^2]/s.

In particular A(y) tends to 0 as y tends to -infinity, and to 1/s as y
tends to +infinity. The first limit also follows by rescaling the density
near its lower endpoint; the second follows by moving the truncation
arbitrarily far into the Gaussian's left tail. A is continuous and
nonconstant. Y_s has an everywhere-positive density. Moreover 0<A(y)<=1/s:
lambda(a)>a for every real a, so the displayed variance is at most 1/s.
Thus A(Y_s) is square integrable and nonconstant, and

    E A(Y_s)^2 - (E A(Y_s))^2 = Var(A(Y_s)) > 0.

This is a concrete dependent counterexample satisfying isotropy,
log-concavity, a genuine Gaussian observation posterior, and a fixed
locally Lipschitz L^2 test function. No random choice of f is involved.
It does not show that the weighted estimate below is false.

# The precise sufficient lemma

Fix a full-dimensional compactly supported isotropic log-concave law mu,
X~mu, and independent Brownian motion B_t in R^n. Let
Y_t=tX+B_t, F_t=sigma(Y_r:0<=r<=t), and mu_t=Law(X | F_t).
Equivalently, mu_t(dx) is proportional to
exp(<Y_t,x>-t|x|^2/2) mu(dx); Y_t is a sufficient statistic.
Let a_t=mu_t x, A_t=Cov(mu_t), and
v_t(f)=mu_t[(f-mu_t f)(x-a_t)].

The outstanding input for this route is: there exist universal T>0 and
K<infinity such that, for every such mu and every smooth f, for almost
every 0<t<T,

    E |v_t(f)|^2 <= K E Var_{mu_t}(f).                 (W)

The constants must be independent of n, mu, and f. This is a
variance-weighted estimate. An unweighted estimate on E||A_t|| does not
imply it. A stronger sufficient input is
E[||A_t|| Var_{mu_t}(f)] <= K E Var_{mu_t}(f), by Cauchy-Schwarz.
Neither input is proved in this packet.

# Conditional reduction, with the input visible

Under (W), C_P(mu) <= exp(KT)/T. Here is the derivation.

The innovation W_t=Y_t-integral_0^t a_r dr is Brownian in F_t:
its conditional drift vanishes and its quadratic variation is t I.
Bayes' likelihood formula and Ito's rule give

    d(mu_t f)=<v_t(f),dW_t>.

For compact support, smooth f and all finite times, the quantities used
here are bounded; the martingale identities and their expectations are
justified without exchanging divergent integrals. The total variance
formula and Ito isometry yield

    V_f(t) := E Var_{mu_t}(f)
            = Var_mu(f) - integral_0^t E |v_r(f)|^2 dr.

Thus V_f is absolutely continuous and (W) implies
V_f'(t)>=-K V_f(t) almost everywhere. Consequently

    V_f(T)>=exp(-KT) Var_mu(f).

At time T the posterior has a T-strongly convex potential on a convex
support. The standard strong log-concavity Poincare bound is 1/T,
including a convex support by approximation. Hence

    V_f(T) <= (1/T) E mu_T |grad f|^2
           = (1/T) mu |grad f|^2.

Combining these gives the claimed conditional bound. If (W) holds with
the same constants for all compactly supported isotropic log-concave
laws, conditioning an arbitrary law on expanding balls and then
recentering and whitening extends the bound. The laws and second moments
converge; compactly supported smooth test functions pass to the limit.
A standard cutoff/density argument extends the inequality to its
locally Lipschitz L^2 domain. This last extension must retain covariance
normalization: the affine maps converge to the identity.

The reduction is not a proof of (W) or of the full target. The referee
must separately check the innovation identity, the strong-convexity
inequality with convex support, and the limit argument.

NEXT: Independently audit (W) or replace it by a proved retention estimate;
never factor its two dependent quantities.
