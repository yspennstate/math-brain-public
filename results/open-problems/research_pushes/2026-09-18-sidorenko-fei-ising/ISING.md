# Ising capacity: explicit analytic screening of Huang's moment body

Date: 18 September 2026. Status: **analytic auxiliary results and a limited exact packet replay**. This note does not claim a new complete proof of the capacity conjecture, and does not certify a full independent reproduction of the existing numerical proof.

## 1. What is already available and what is added

The public `yspennstate/ising-perceptron-capacity` repository contains a computer-assisted proof claim closing the numerical hypotheses in Ding--Sun's lower bound and Huang's upper bound at zero margin. Its theory and manuscript explicitly separate the analytic reductions from the interval certificates. Its full driver requires nine passing checks, including numerical replay of all 1404 Region-I jobs. Reading that driver, or checking a stored sign, is not such a replay.

Brice Huang, *Capacity threshold for the Ising perceptron*, arXiv:2404.18902v2, already proves the qualitative half-space exclusion in Lemma 7.17, the positivity of the moment denominator in Lemma 7.2, and exclusion of boundary maximizers in Proposition 7.16. An initially reconstructed qualitative exclusion in this session was therefore **rediscovery**, not a new capacity result.

The added useful material is an explicit rational collar on the *positive* side of that excluded half-space, certified by one fixed tilt and no numerical quadrature; an explicit one-parameter frontier of the two-dimensional moment body; and a quantitative entropy bound in terms of support-function slack. The proofs below keep the exact fixed-point hypotheses visible. These additions have not received an independent audit, and their publication novelty has not been certified.

## 2. Exact normalization and imported hypotheses

All logarithms and entropy in this note are natural. Let

    X~N(0,psi),  M=tanh X,  q=E M^2,  delta=1-q,

with 0<q<1, psi>0. Let Z~N(0,1) and write phi and Psi for the standard Gaussian density and upper tail. Set

    e(t)=phi(t)/Psi(t),
    gamma=sqrt(q/delta),
    N(Z)=e(-gamma Z)/sqrt(delta).

We assume the exact fixed-point relation

    psi=alpha E N^2.                                        (2.1)

These are Huang's zero-margin quantities. The existing certificate package purports to establish a narrow parameter rectangle around alpha=0.8330786, q=0.56394908, psi=2.5763513. No floating approximation is substituted for (2.1).

Let

    K={(E[X Lambda], E[M Lambda]): |Lambda|<=1},
    H(a)=sup E h_nat((1+Lambda)/2),  subject to those moments.

Then 0<=H(a)<=ln2. For a=(a_1,a_2) in K, put

    D(a)=sqrt(1-a_2^2/q),
    B_a(Z)=a_2 Z/[sqrt(q)D(a)] + a_1 N(Z)/[psi D(a)],
    G(a)=inf_{s>=0} {psi s^2/2 + alpha E log Psi(sN-B_a)}.   (2.2)

The source objective at a finite-parameter profile is H(a)+G(a). The infimum can equal negative infinity. No claim below replaces the original global condition by a stronger unproved equality of unrelated optimizations.

## 3. Explicit moment-body frontier

Write gamma_psi(x)=(2pi psi)^(-1/2)exp(-x^2/(2psi)),

    a=E|X|=sqrt(2psi/pi),   b=E|tanh X|.

For t>=0 take the saturated odd profile

    Lambda_t(x)=sgn(x) sgn(|x|-t).

Its moments are

    A(t)=4psi gamma_psi(t)-a=2a exp(-t^2/(2psi))-a,
    B(t)=b-4 integral_0^t tanh(x) gamma_psi(x) dx.            (3.1)

For -a<s<a define

    t(s)=sqrt(-2psi log((s+a)/(2a))),  L(s)=B(t(s)),

and extend L continuously to the endpoints. Then the entire body is

    K={(s,y): -a<=s<=a,  L(s)<=y<=-L(-s)}.                  (3.2)

### Proof

The ratio tanh(x)/x is strictly decreasing for x>0. Indeed its derivative has numerator x sech^2 x-tanh x, whose derivative is -2x sech^2 x tanh x<0 and whose limit at zero is zero.

Fix t>0 and k=tanh(t)/t. The function M-kX is positive on 0<X<t and negative on X>t, with the opposite signs for negative X. Thus Lambda_t=-sgn(M-kX) minimizes E[(M-kX)Lambda] over |Lambda|<=1. For every profile with first moment A(t), its second moment is therefore at least B(t). A(t) strictly decreases from a to -a, so this proves the complete lower boundary. Central symmetry gives the upper one. Mixtures of the two extremizing profiles with the same first moment fill the intervening vertical segment, proving (3.2).

For the derivative form,

    dB/dA=tanh(t)/t,

so the lower boundary is convex. Formula (3.1) follows by direct integration of x gamma_psi(x). Endpoint values follow by dominated convergence. QED.

This gives a scalar, explicit feasibility test for candidate moment cells; it does not eliminate the remaining optimization over the interior.

## 4. Quantitative entropy near a supporting line

For a nonzero normal w=(w_1,w_2), let

    ell=|w_1X+w_2M|,  h_K(w)=E ell,
    epsilon=h_K(w)-w dot a>=0.

For every tau>0 with epsilon/(2tau)<=1/2,

    H(a)<=P(ell<=tau)ln2+h_nat(epsilon/(2tau)).             (4.1)

### Proof

For a feasible profile define

    p=(1-sgn(w_1X+w_2M)Lambda)/2.

Then epsilon=2E[ell p], and h_nat((1+Lambda)/2)=h_nat(p) by binary-entropy symmetry. On ell>tau, E[p 1_{ell>tau}]<=epsilon/(2tau). Apply concavity of binary entropy to p 1_{ell>tau}; its entropy equals zero on the complement. Since h_nat is increasing on [0,1/2], the resulting contribution is at most the second term in (4.1). On ell<=tau it is at most P(ell<=tau)ln2. Take the supremum over feasible profiles. QED.

For nonzero w the analytic function w_1x+w_2 tanh x is not identically zero and has Gaussian-zero set of measure zero. Thus (4.1) also recovers H=0 on an exposed boundary by sending tau down to zero. The qualitative boundary fact is already present in the source/repository; the explicit modulus (4.1) is an ancillary tool for certification.

## 5. An elementary global Gaussian-tail majorant

For every real v,

    log Psi(v)<=-v_+^2/2-log(1+v_+),  v_+=max(v,0).         (5.1)

For v<=0 the bound is immediate. For 0<=v<=1, translating the Gaussian tail gives Psi(v)<=exp(-v^2/2)/2<=exp(-v^2/2)/(1+v). For v>=1 the usual integral bound Psi(v)<=phi(v)/v gives the same conclusion, because 1+v<=sqrt(2pi)v. Thus (5.1) is valid globally, including where v is negative. Using a large-positive-v expansion as a global inequality would be incorrect.

Gaussian integration by parts supplies an exact cancellation. From e'(t)=e(t)(e(t)-t),

    N'(Z)=-sqrt(q)N(Z)^2-[q/delta]ZN(Z).

The Mills bound gives at most linear growth of N, so the needed integrability and integration by parts are valid. Consequently

    E[ZN]=-delta sqrt(q)E N^2,
    alpha E[N B_a]=[a_1-psi delta a_2]/D(a).               (5.2)

Put c(a)=a_1-psi delta a_2. Combining (2.1), (5.1), and (5.2), for every s>=0,

    H(a)+G(a)
      <=ln2 + s c(a)/D(a)
            -alpha E log(1+(sN-B_a)_+).                   (5.3)

For completeness, before dropping nonpositive terms, the right side also contains

    -(alpha/2)E B_a^2+(alpha/2)E(sN-B_a)_-^2<=0,

because (sN-B_a)_-<= (B_a)_+. Thus no uncontrolled quadratic remainder is discarded.

If c(a)<=0, the last expectation tends to positive infinity monotonically as s tends to infinity, since N>0 almost surely. Hence G(a)=-infinity in this half-body. **This is the zero-margin form of Huang's Lemma 7.17**, not a new qualitative exclusion: his d_0 equals -psi delta by (5.2).

## 6. A completely explicit denominator guard

Assume only the broader rectangle

    5/2<=psi<=13/5,   1/2<=q<=3/5,   q=E tanh^2 X.          (6.1)

Then for every a in K,

    D(a)>1/15.                                             (6.2)

### Proof

Let Y=|tanh X|. Since |a_2|<=E Y,

    D(a)^2 >= Var(Y)/q >= Var(Y).

The Gaussian density prefactor exceeds 10/41, using pi<22/7 and psi<=13/5. Using psi>=5/2, exp(-1/20)>19/20, and exp(-5/4)>1/4 gives

    P(|X|<=1/2)>19/82,
    P(3/2<=|X|<=5/2)>5/41.

On the first event Y<1/2; on the second Y>9/10. The latter follows from e^3>19, which is certified by the first seven terms of its positive Taylor series. For independent Y,Y', apply Var(Y)=E(Y-Y')^2/2 to the two event orders. This yields

    Var(Y)>(19/82)(5/41)(2/5)^2=38/8405>1/225.

Thus (6.2) follows. The elementary exponential bounds can be obtained from exp(-x)>=1-x and ln2>2/3. QED.

This is an explicit, deliberately conservative version of the source's qualitative positive-denominator lemma. It needs no numerical Gaussian integration.

## 7. A fixed-tilt positive-width collar

### Theorem 7.1

Assume (2.1), (6.1), and alpha>=4/5. For every a in K such that

    c(a)=a_1-psi(1-q)a_2 <=1/230400,

the single tilt s=1024 gives

    H(a)+psi s^2/2+alpha E log Psi(sN-B_a)<-1/15.           (7.1)

In particular H(a)+G(a)<-1/15 on this closed half-space intersected with K. The statement includes a positive-width collar on the side c>0, not just Huang's known c<=0 exclusion.

### Proof

On Z in [-1,0], monotonicity of the inverse Mills ratio and q>=1/2 give

    N>=sqrt(2/[pi(1-q)])>1.

Here pi<22/7 makes its squared lower bound at least 14/11. Also |a_2|<=1 and |a_1|<=sqrt(2psi/pi), so (6.2), pi>3, and psi>=5/2 imply

    |B_a|/N <=15(1/sqrt(q)+|a_1|/psi)
              <15(3/2+8/15)=61/2<31.

For s>=62 this gives sN-B_a>=s/2 on that event. Its probability exceeds 1/6: the minimum standard Gaussian density on [-1,0] is greater than (1/3)(1/2). Equation (5.3), or the same fixed-s bound before taking the infimum, therefore gives

    H(a)+psi s^2/2+alpha E log Psi(sN-B_a)
       <=ln2+15s max(c(a),0)-(alpha/6)log(1+s/2).

At s=1024, log(1+s/2)=log513>9ln2. Since alpha>=4/5 and c_+<=1/230400,

    right side < -(1/5)ln2+15360/230400
               < -2/15+1/15 = -1/15.

We used ln2>2/3. Every numerical comparison here is a rational inequality or the stated elementary logarithm/exponential bound. QED.

The fixed-point equations and the coarse rectangle remain explicit hypotheses. The existing source-bound parameter certificate is an input if this theorem is used in the capacity proof. The theorem does not independently establish that certificate or the remaining c>1/230400 region.

## 8. What was actually replayed

`check_ising.py` performs:

* A finite exact analogue of (3.2), using four positive radii and monotone ratios: all 16 cube vertices, eight frontier vertices, and 288 integer support directions are checked.
* The rational inequalities in the denominator guard and fixed-tilt collar.
* An exact Fraction/isqrt reconstruction of the inball geometry from the four matrix packets in the committed `verification/results/huang_star_interior.json`, Git blob `889549cf88ef270333efa77ad0d5083f6f1d9d39`. Its payload identifier is `e03fa07e2ea959ceb035313d28f222e193fd4d78427b389796746f3c69ae790a`.

From those packets it verifies determinant positivity, inradius greater than 0.0150391982, and inradius greater than the required padded star radius. These are independently reconstructed arithmetic consequences of the **stored** integral enclosures. The defining Gaussian integrals were not recomputed here. The checker explicitly records `Gaussian_integral_enclosures_recomputed=false` and `full_capacity_certificate_chain_replayed=false`.

The public repository's earlier `star_interior_portable_check.py` already performs a more extensive stored-packet geometric check. The replay in this session provides an additional consistency check; it is not a newly discovered verification architecture or an end-to-end capacity audit. The working environment did not have python-flint, and a fresh repository download into that environment failed. No full replay is claimed in place of it.

## 9. How to use the additions

The rational collar can be used as an analytic pre-screen before invoking any expensive cell integration: an entire cell is safe if interval arithmetic bounds c above by 1/230400 and the imported parameter hypotheses hold. Cells outside K can instead be rejected using the scalar frontier or support witnesses. The entropy bound (4.1) provides a possible boundary-collar estimate where direct entropy duals are inconvenient.

The remaining decisive capacity obligation is still formula-to-code scrutiny and a clean end-to-end replay of the full published package, or an analytic proof replacing the remaining numerical conditions. This note supplies neither by implication. For the unresolved positive interior of H+G, especially near its zero maximizer, the current package's ray-curvature argument remains necessary.
