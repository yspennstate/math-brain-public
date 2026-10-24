# Independent probability-branch audit of the largest-weight LTF proof

2 October 2026. Target: `largest_weight_ltf_candidate.md`. This audit was
performed independently of its author, the root's reconstruction, and the
antivoter branch's audit.

**Analytic verdict: PASS.** I read every step, recomputed the critical
constants and normalization factors, and attempted to break the argument
in the atomic, tiny-variance, highly biased, and zero-degree regimes. I did
not find a mathematical gap. The audited conclusion is FEI for all
deterministic linear threshold functions, via a largest-defining-weight
entropy split. It does not prove FEI for all Boolean functions. Historical
novelty and publication readiness require further external review.

This is an algebraic/analytic audit, not an inference from finite tests.

## 1. Primary inputs checked directly

I reopened Keller–Klein, *Biased Halfspaces, Noise Sensitivity, and Local
Chernoff Inequalities*, arXiv:1710.07429v3, Theorem 1.4:
<https://arxiv.org/html/1710.07429v3>.
Its halfspace is an indicator, its weight vector has Euclidean norm one,
and its influence is the physical probability of changing output after
flipping a coordinate. Hence that influence is identical for the indicator
and its corresponding sign-valued LTF. With largest weight w and remaining
variance sigma^2, its normalized largest weight is
w/sqrt(w^2+sigma^2)=1/sqrt(R+1). The theorem gives exactly

    alpha >= c p min{1,sqrt(L/(R+1))},

with a universal c>0. There is no extraneous factor two from translating
the output convention. The largest-weight coordinate has largest physical
influence by the explicit two-coordinate monotonicity comparison in the
draft, which I also recomputed.

I reopened Klivans–O'Donnell–Servedio, *Learning Intersections and Thresholds
of Halfspaces*, Theorem 18, on PDF page 8:
<https://www.cs.columbia.edu/~rocco/Public/focs02.pdf>.
Its noise flips each bit with probability epsilon. It states

    NS_epsilon(f) <= min{2p,20.5 p sqrt(epsilon ln(1/p))}.

This is the same sign-valued convention used in the draft. The relation
NS_epsilon=(1−Stab_(1−2epsilon)(f))/2 is also explicitly present in its
Proposition 15. Therefore the draft's square-root tail coefficient uses
the correct bit-flip/resampling conversion and the correct factor two.

## 2. Independent proof of the bounded-weight concentration estimate

For Z=sum_j b_j X_j, |b_j|<=w and v=sum_j b_j^2, define

    K(u)=[sin(u/(2w))/(u/(2w))]^2
        =w integral_{−1/w}^{1/w}(1−w|t|)exp(i t u) dt.

At u=0 the triangular integral equals one, so the Fourier normalization is
correct. For |u|<=w, sin(s)/s >=1−s^2/6>=23/24 with s=u/(2w), and thus
K(u)>0.9. On the Fourier support, |b_j t|<=1. Since log cos(s)<=−s^2/2
there (integrate tan(s)>=s), the absolute characteristic function is at
most exp(−v t^2/2). Therefore, uniformly in every interval center,

    Pr(|Z−center|<=w)
      <=(10/9) w integral_R exp(−v t^2/2)dt
      =(10/9)sqrt(2pi) w/sqrt(v)<3w/sqrt(v).

This uses no smoothness of the law of Z, so lattice atoms, zero weights,
and closed interval endpoints are allowed. The trivial bound one handles
small v. For v=0 it is used directly.

## 3. Independent mask proof of slab stability

Let X,Y have correlation rho by retaining a coordinate with probability
rho and otherwise independently resampling it. Set epsilon=1−rho and let
J be the resampling mask. Conditional on J,X, the retained signs shift
only the center of the width-2w slab. The resampled variance is
V_J=sum_{j in J} a_j^2, so the preceding estimate bounds its conditional
slab probability uniformly in X.

After scaling by w^2, write V_J/w^2=sum_j u_j Z_j with 0<=u_j<=1,
independent Bernoulli(epsilon) masks, and mean mu=epsilon R. Exponential
Markov gives

    Pr(V_J/w^2<mu/2)
      <=exp(mu/2) product_j[1−epsilon+epsilon exp(−u_j)]
      <=exp(−[(1−e^(−1))−1/2]mu)
      <=exp(−mu/8).

On its complement the interval concentration is at most 3sqrt(2/mu).
The pivotal indicator B(X) depends only on X; the mask event depends only
on J. Thus multiplication by B(X) contributes its exact mean alpha even
on the rare bad-mask event. This independence is the essential step and
it is valid. Consequently

    Stab_rho(B)<=alpha[3sqrt(2/mu)+exp(−mu/8)]
               <=6alpha/sqrt(mu).

The last constant is safe because
sup_mu sqrt(mu)exp(−mu/8)=2e^(−1/2), and
3sqrt(2)+2e^(−1/2)<6. Together with Stab<=alpha this proves the proposed
lemma, including arbitrarily small alpha and threshold atoms.

## 4. Spectral scale checks

The normalized pivotal spectrum Q_S=hat B(S)^2/alpha is a probability law
because B is an indicator. Its zero-degree mass is alpha, not alpha^2.

For integer k>=1, rho=1−1/(2k) has rho^k>=1/2. The mask estimate implies
Q(degree<=k)<=12sqrt(2k/R)<18sqrt(k/R). For real k, the floor reduces the
event and only improves this bound.

At rho=1/2, hypercontractivity gives Stab_(1/2)(B)<=alpha^(4/3), so
Q(degree<=k)<=2^k alpha^(1/3). Since alpha<=2p, for L>=2ln2 we have
ln(1/alpha)>=L/2. If k<=L/(12ln2), this is <=exp(−L/12); its conversion
to 1.5sqrt(k/L) is safe because
sup_L sqrt(L)exp(−L/12)=sqrt(6)e^(−1/2)<1.5. For the other k, the
trivial probability bound one is <=3sqrt(k/L). The regime L<2ln2 also
uses the trivial bound. Thus the maximum scale M=max{1,R,L} gives

    Q(degree<=k)<=18sqrt(k/M).

For the full split-pair spectrum P_S=hat A(S)^2+hat B(S)^2, a remaining
degree >=u implies a full-function degree >=u. At u>=1, choose bit-flip
noise epsilon=1/(2u). Each such full degree loses at least 1−e^(−1) of
its stability; the NS bound yields

    P(degree>=u)<=A0 p sqrt(L/u),
    A0=20.5sqrt(2)/(1−e^(−1))<46.

At u<1, the relevant mass is at most the full nonconstant mass
4p(1−p)<=4p, and the same displayed bound is larger. Finally the KK
comparison gives p sqrt(L/M)<=sqrt(2)alpha/c by considering L<=R+1 and
L>R+1 separately. Hence

    P(degree>=u)<=Gamma alpha sqrt(M/u).

All constants are universal; there is no hidden dependence on n or on
the smallest nonzero input weight.

## 5. Independent abstract two-spectrum entropy lemma

The LTF-specific argument reduces to the following entirely probabilistic
claim. Let P,Q be probability laws on finite spectral labels, with
P_s>=alpha Q_s, alpha in (0,1], and a nonnegative integer degree d(s).
Assume Q(d=0)=alpha, and for some M>=1 and universal a,b,

    Q(d<=k)<=a sqrt(k/M), k>=1;
    P(d>=u)<=b alpha sqrt(M/u), u>0.

Then the included-coordinate conditional entropy

    alpha sum_s Q_s log_2[P_s/(alpha Q_s)]

is at most C alpha for a constant depending only on a,b.

To verify this independently, merge degree zero into a special atom and
positive degrees into bins j=floor(log_2(d/M)). For negative j,
Q_j<=a sqrt(2)2^(j/2), hence E_Q[|j|;j<0] is universally bounded. For
all j, P_j<=b alpha 2^(−j/2). Use a reference probability with mass one
half at zero and mass proportional to 2^(−|j|/4) elsewhere. Gibbs'
entropy inequality gives

    D(Q_bins||P_bins)>=sum_j Q_j log_2[R_j/P_j].

The positive-j term is at least log_2(1/alpha) minus a constant plus j/4;
the negative-j penalty is only 3|j|/4 and has bounded expectation. The
zero atom costs at most alpha. Therefore

    D(Q_bins||P_bins)>=log_2(1/alpha)−C.

The term lost from assigning zero mass alpha is at most
alpha log_2(1/alpha)<=log_2(e)/e, another universal constant. KL data
processing has the required direction, D(Q||P)>=D(Q_bins||P_bins), so
the abstract claim follows. All Q support has positive P support because
P>=alpha Q. This independently rederives the entropy step without using
any geometric fact about halfspaces.

The complementary conditional-bit term obeys
sum_s hat A(s)^2 log_2[P_s/hat A(s)^2]<=alpha log_2(e) by ln(1+x)<=x,
including zero coefficients by continuity. Thus the total conditional
spectral-bit entropy is O(alpha).

### A second entropy derivation using two-sided degree tails

There is also a useful alternative to the draft's particular R/P reference
calculation. Since P>=alpha Q, the P-bin estimate automatically gives
Q_j<=b 2^(−j/2) for positive j. Together with the already derived negative
tail, both sides of the Q-bin degree law have geometric tails. Consequently
E_Q[|J|;positive degree] is bounded by a constant depending only on a,b.
For example, it is at most

    [a sqrt(2)+b] sum_{m>=1} m 2^(−m/2).

The reference law with mass 1/2 at the zero atom and geometrically decreasing
mass elsewhere now gives directly H(Q_bins)=O_{a,b}(1), by the usual entropy
upper bound by cross entropy. On each positive-degree bin,

    log_2(1/P_j)>=log_2(1/alpha)−log_2(b)+j/2.

Thus the Q-cross-entropy against P is at least
(1−alpha)log_2(1/alpha)−log_2(b)−(1/2)E_Q[|J|;J<0]. Subtracting the
uniformly bounded H(Q_bins), and absorbing alpha log_2(1/alpha), again
gives D(Q_bins||P_bins)>=log_2(1/alpha)−O_{a,b}(1). This route has poorer
constants but uses only two-sided geometric tails and the elementary
identity KL=cross-entropy minus entropy. It confirms the scale separation
without relying on the draft's sign cancellation of its positive-J term.

## 6. Exact split and dimension induction

For each remaining spectral label, the full Fourier pair is (Ahat,Bhat)
and the restricted pair is (Ahat+Bhat,Ahat−Bhat). With
q=Bhat^2/P and r=(Ahat+Bhat)^2/(2P), direct entropy expansion gives

    Delta_i H=sum_s P_s[1+h_2(q_s)−h_2(r_s)].

Since r(1−r)=(1−2q)^2/4 and h_2(t)>=4t(1−t),
1−h_2(r)<=4q(1−q)<=h_2(q). Therefore Delta_i H is at most twice the
conditional spectral-bit entropy, hence at most C alpha.

Every restriction of an LTF is again an LTF, so applying the same largest
weight rule at each nonconstant restriction proves by dimension induction
H(f)<=C I(f). The influence identity
I(f)=I_i(f)+[I(f^+)+I(f^-)]/2 supplies exactly the required inductive
charge. Constants have entropy zero; irrelevant zero-weight coordinates
can be discarded. No claim for general monotone functions follows.

## 7. Stress regimes and failed attempts to break the proof

- R=0 gives a dictator in the nonconstant case. Then alpha=1 and the
  pivotal spectrum is entirely the zero atom. The mask estimate is not
  invoked, the entropy bound remains valid, and actual spectral entropy
  is zero.
- R<<1, even with many microscopic weights, makes M either one or L. The
  proof uses the trivial bound or bias hypercontractivity rather than
  dividing by a small variance.
- L>>R implies p<=alpha/c, so the bias scale rather than the variance
  controls the tail comparison. The zero-degree exception has Q-mass
  alpha and incurs only a universally bounded alpha log(1/alpha) loss.
- Atomic extremal slabs and endpoint ties do not invalidate the uniform
  interval estimate. Moving the threshold strictly into its finite score
  gap preserves the represented Boolean function and the defining weights.
- Infinitely many formal dyadic bins cause no integrability issue: the
  actual spectrum is finite, the reference law is positive everywhere,
  and only negative-bin moments need a bound. Positive-bin terms can
  safely be discarded in the lower bound.
- An arbitrary prescribed or maximum-influence coordinate can fail for
  general monotone functions. This proof additionally uses the bounded
  remaining weights and the exact parallel slab representation, which
  those counterexamples lack. The prior obstructions therefore do not
  conflict with the audited LTF theorem.

## 8. Historical boundary

An important search trap is the original 2013 ECCC abstract of *Upper
Bounds on Fourier Entropy*, which claimed FEI for LTFs. The primary ECCC
record <https://eccc.weizmann.ac.il/report/2013/052/> explicitly says its
2018 revision removed inaccuracies in Lemma 5.4 and Theorem 5.5. Its revised
LTF result is only H(f)=O(sqrt n). The primary random-LTF paper
<https://arxiv.org/abs/1903.11635> (2019) explicitly says FEI for all LTFs
was still unknown and proves the random-weight case. Those are not prior
proofs of the deterministic theorem audited here.

The May 2026 primary preprint
<https://arxiv.org/html/2606.00246v1> discusses the general split-induction
framework and gives other subclasses, while FEI remains open generally.
The split framework is therefore prior methodology. The audited new
ingredient is the largest-weight slab scale separation and its entropy
application, subject to a complete expert novelty review.

**Final audit status:** no mathematical gap found; all deterministic LTF
FEI follows from the stated primary inputs and the fully checked new
lemmas. This is an internal independent proof audit, not outside peer
review or a novelty certificate.
