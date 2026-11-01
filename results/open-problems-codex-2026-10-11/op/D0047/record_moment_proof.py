from pathlib import Path
p=Path('ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write('''
## 12. Additional serious attempt: two routes and the chosen one

Reopened at the user's request on 2026-10-12. The two unexecuted routes were written in NEW_APPROACHES.md before pursuing either: (A) quantitative discounted first-hitting estimates; (B) adjoint propagation of the one-pole Lax residual. Route A is pursued below. Route B remains a proposal, not a proved selection argument.

The brain was asked for the gap using "Painleve V isomonodromy connection Fokker Planck Rumanov boundary selection" and "Brownian carousel discounted hitting time Girsanov small gap level repulsion". No source-specific selection theorem was returned. A follow-up recall on geometric-Brownian characteristic roots supplies only a hint for the power test function below; the calculation and stopping proof are checked independently.

## 13. New proved generator-side small-gap bound

The notation is that of Section 2, with theta=0, c=beta/4>0, L=2pi, X_t=A_(t wedge tau), and V(s,0)=E exp(-c tau). Define

    p=min(2, (1+sqrt(1+8c))/2).

Then 1<p<=2 and p(p-1)/2<=c. For every s>=0,

    0<=G_beta(s)-1+s/L <= (s/L)^(p+1)/(p+1).                       (12)

In particular, at beta=2 take p=(1+sqrt(5))/2. The remainder is O(s^((3+sqrt(5))/2)), hence o(s^2). This is proved directly from the carousel SDE; no determinantal identification or Painleve equation is used.

Proof of the moment estimate. The stopped first-moment equation gives

    0<=E X_t=cs integral_0^t exp(-cu)P(u<tau)du
               <=s(1-exp(-ct)).                                    (13)

For 1<p<=2, the function x^p is C1 on [0,infinity) but may not be C2 at zero. To avoid assuming Ito's formula there, use f_epsilon(x)=(x+epsilon)^p, epsilon>0, in the stopped discounted Ito formula up to T wedge tau. The terminal term is exp(-c(T wedge tau))f_epsilon(X_T). All stochastic integrands are bounded on [0,T] for fixed epsilon since 0<=X<=L; thus their expectations vanish. As epsilon decreases to zero, every term converges by dominated convergence: the first-derivative term is bounded by p(L+1)^(p-1), the potential term by c(L+1)^p, and the second-derivative term satisfies

    2p(p-1)sin^2(x/2)(x+epsilon)^(p-2)
        <=(p(p-1)/2)x^p,  0<=x<=L,

using 4sin^2(x/2)<=x^2 and p-2<=0. At x=0 the left side is zero. The starting value epsilon^p tends to zero. Therefore the exact limiting discounted Ito identity is valid for x^p and yields

    E[exp(-c(T wedge tau))X_T^p]
     =E integral_0^(T wedge tau) exp(-ct)
          [pc s exp(-ct)X_t^(p-1)
            +2p(p-1)sin^2(X_t/2)X_t^(p-2)-cX_t^p]dt.

The last two terms together are <=0 because p(p-1)/2<=c. The expression at X_t=0 is defined by its continuous zero limit. Consequently

    E[exp(-c(T wedge tau))X_T^p]
      <=pc s integral_0^T exp(-2ct)
                    E[X_t^(p-1)1_{t<tau}]dt
      <=pc s integral_0^T exp(-2ct)(E X_t)^(p-1)dt.                  (14)

The last inequality first drops the indicator (the random variable is nonnegative), then uses concavity of x^(p-1), since 0<p-1<=1. Substitute (13). As T tends to infinity, the left side tends by bounded convergence to L^p E exp(-c tau): on tau<infinity it is eventually L^p exp(-c tau), while on tau=infinity it tends to zero because X_T<=L and exp(-cT) tends to zero. The nonnegative upper integral converges monotonically, giving

    L^p V(s,0)
      <=pc s^p integral_0^infinity exp(-2ct)(1-exp(-ct))^(p-1)dt
      =p s^p integral_0^1 u(1-u)^(p-1)du
      =s^p/(p+1).                                                  (15)

For the last equality, put v=1-u and integrate v^(p-1)-v^p: the integral is 1/p-1/(p+1)=1/[p(p+1)]. Section 2 gives G_beta(s)-1+s/L=(s/L)V(s,0)>=0, so (15) proves (12). QED.

Referee points. The terminal discount is stopped at T wedge tau, not merely at T; using exp(-cT) after a finite hit would erase the hitting transform and invalidate the proof. The random variables used for concavity are X_t including its constant post-hit value L; dropping the pre-hit indicator only increases the upper bound. All constants remain independent of s and T. The nonsmooth-power step is explicitly justified by epsilon regularization, and the singular second derivative is compensated by the squared diffusion coefficient.

## 14. The exponential branch is now excluded without a determinant

For the fake branch exp(-s/L), Taylor's theorem gives

    exp(-s/L)-1+s/L = s^2/(2L^2)+O(s^3).

In contrast (12), with p>1, gives

    lim_(s downarrow 0) [G_beta(s)-1+s/L]/s^2=0.                    (16)

The functions therefore differ for all sufficiently small positive s, for every beta>0. At beta=2 this rejects precisely the linear-sigma branch recorded in Section 6, using only generator-side probabilistic information. No existence of a classical second derivative of G_beta at zero is asserted solely from the remainder bound: (16) is a Peano quadratic datum. If an analytic candidate gap is to equal the physical gap, its quadratic Taylor coefficient must be zero.

This removes the previously missing branch datum at quadratic order. The central physical/Lax selection and nonlinear closure are still unproved.
''')
print('Saved complete new moment proof and branch exclusion.')
