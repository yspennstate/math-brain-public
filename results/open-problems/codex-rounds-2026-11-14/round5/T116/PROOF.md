# Common-reference testing audit

This is a direct verification of an existing final testing step. The construction of the hard words and its numerical estimates are hypotheses here.

Let W be an injective map from {0,1}^g to binary words of length n. Let P_theta be the law of m independent complete traces of W(theta). Suppose a single probability law R on the observation space satisfies

\[
\operatorname{TV}(P_\theta,R)\le\varepsilon
\quad\text{for all }\theta\in\{0,1\}^g.
\]

Every randomized reconstruction rule has uniform average success on this family at most

\[
2^{-g}+\varepsilon. \tag{1}
\]

To prove this, write a_theta(z) for the conditional probability that the rule outputs W(theta) on observing z. Each a_theta lies in [0,1]. Injectivity gives sum_theta a_theta(z) <= 1, since these are probabilities of different outputs. No restriction is imposed on computation or on outputs outside the family.

For any probability laws P,R on a finite set, put h(z)=P(z)-R(z). The sum of h is zero. Therefore the sum of its positive entries equals TV(P,R). For 0<=f<=1,

\[
\mathbb E_P f-\mathbb E_R f
=\sum_z h(z)f(z)
\le\sum_{h(z)>0}h(z)
=\operatorname{TV}(P,R).
\]

Apply this to f=a_theta and sum over all 2^g choices. This yields

\[
2^{-g}\sum_\theta \mathbb E_{P_\theta}a_\theta
\le 2^{-g}\mathbb E_R\sum_\theta a_\theta+\varepsilon
\le 2^{-g}+\varepsilon,
\]

which proves (1). Complete traces of length-n inputs have finite support, so the observation space for each finite m is finite. Every bit of every trace, including its length, is included in z.

Consequently, if the rule succeeds on every length-n word with probability at least s, then

\[
s\le 2^{-g}+\varepsilon. \tag{2}
\]

For any fixed s>0 choose a fixed integer g with 2^(-g)<s. If epsilon tends to zero, (2) fails eventually. This works also for s<=1/2. Pairwise testing alone would not give that conclusion.

In the opened implementation, the supplied family estimate has the form

\[
\varepsilon=\sqrt{mgN^{-d}}+2mgE. \tag{3}
\]

For example, fix eta with 0<eta<s-2^(-g). If m<=eta^2 N^d/(4g) and 2mgE<=eta/2, then the two terms in (3) are at most eta/2 each. Thus epsilon<=eta and the strict contradiction follows. These conditions only verify the transfer from a family estimate; they do not assert the existence of the family or the required bound on E.

There is a second way to check (1). Let mu(theta,z)=2^(-g)P_theta(z), the joint law under a uniform prior, and let nu(theta,z)=2^(-g)R(z). Expanding the definition of total variation gives

\[
\operatorname{TV}(\mu,\nu)
=2^{-g}\sum_\theta\operatorname{TV}(P_\theta,R)
\le\varepsilon.
\]

Under nu the hidden choice is independent of the data, so the success probability of any rule is at most 2^(-g). The bounded success function differs in expectation under mu and nu by at most epsilon, proving (1) again.

The assumptions cannot be discarded. For g=1 and P_0=P_1=R, the bound gives success at most 1/2, attained by guessing a fair bit. If the two laws have disjoint supports and R=P_0, epsilon=1 and the bound is valid but uninformative; exact recovery is possible. If W is not injective, the inequality sum_theta a_theta<=1 need not hold, so recovery of the word does not imply recovery of the hidden choice. All three checks agree with the stated hypotheses.
