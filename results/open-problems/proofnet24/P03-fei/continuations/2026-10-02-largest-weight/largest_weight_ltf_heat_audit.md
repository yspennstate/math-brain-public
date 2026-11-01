# Independent audit of the largest-weight deterministic LTF argument

2 October 2026. heat_entropy read `largest_weight_ltf_candidate.md` in full.
The proof's new slab-stability estimate, dyadic KL separation, and spectral
split calculation pass this independent analytic audit. The audit relies on
the parent/FEI branch's primary-source verification of the stated
Keller--Klein largest-influence estimate and Klivans--O'Donnell--Servedio biased
noise estimate. Historical novelty is not certified.

## Slab estimate

The Fourier triangular-kernel identity has the right scale: its value at zero
is one and its integral prefactor is w. On the interval of half-width w the
squared sinc kernel exceeds 9/10. Every cosine is nonnegative on the integration
range and is bounded in absolute value by exp(-b_j^2 t^2/2). The resulting
constant is (10/9)sqrt(2*pi)<3, as required.

The resampling-mask application is valid even for atoms and an arbitrary
threshold center. Conditional on the mask and original input, the resampled
signs are independent and unbiased; the retained coordinates only change the
center. The concentration estimate is uniform in that center. The original
slab indicator depends on X, while the good/bad variance event depends only on
the independent mask. Therefore the bad-mask probability is multiplied by
alpha, rather than being an additive error without alpha. This is the key
point of the argument.

The weighted Chernoff estimate is valid for summands in [0,1]. Its exponent
constant (1-exp(-1))-1/2 exceeds 1/8. Also
sup sqrt(mu)exp(-mu/8)=2exp(-1/2), whose addition to 3sqrt(2) is below six.
The R=0 case and the regime where the displayed stability upper bound exceeds
one are covered by the trivial stability bound alpha.

## Degree and KL estimates

The positive-degree low-tail bound follows by setting rho=1-1/(2k), for which
rho^k>=1/2, and by the indicator hypercontractive estimate at rho=1/2. The
rare-event inequality alpha<=2p supplies log(1/alpha)>=L-log2. The constants
in the two L regimes are adequate. Combining whichever of R,L,1 attains M
therefore proves the stated normalized slab degree lower-tail bound.

The split-pair spectral law P is a probability law because A^2+B^2=1.
Its positive-degree tail is bounded by the full LTF spectral tail; adding the
distinguished coordinate cannot lower full degree. The KOS noise estimate gives
the stated tail factor with the factor of two in the noise/stability identity
included. For u<1 the separately used nonconstant spectral mass 4p(1-p) is
valid, so no zero-degree mass is accidentally included in that tail bound.

The dyadic bins use the lower endpoint for the P upper-tail bound and the
upper endpoint for the Q lower-tail bound. Empty subunit positive-degree bins
are harmless. The negative-bin first moment is finite with an absolute bound;
no positive-bin Q-tail estimate is required because its coefficient in the
reference-law logarithm is nonnegative.

For the auxiliary reference law R,
D(Q||P)=D(Q||R)+E_Q log(R/P)>=E_Q log(R/P).
This is the correct inequality direction. The special atom contributes at
least -alpha because its reference mass is 1/2 and its P mass is at most one.
Its Q mass is exactly alpha, not alpha^2. Thus the claimed lower bound
D(Q||P)>=log2(1/alpha)-C_D follows, with the alpha log(1/alpha) term bounded by
an absolute constant. Data processing makes the KL divergence on individual
spectral subsets at least the coarse-bin divergence, also in the required
direction. Since P>=alpha Q pointwise, no P-zero denominator occurs on Q's
support.

## Entropy split and induction

The included-bit conditional entropy contribution is exactly
alpha[log2(1/alpha)-D(Q||P)]. The excluded-bit contribution is at most
alpha log2(e), including vanishing Fourier coefficients by continuity.
For a spectral subset with a=Ahat, b=Bhat and P=a^2+b^2, the exact split
increment is P[1+h2(b^2/P)-h2((a+b)^2/(2P))]. The inequality
h2(t)>=4t(1-t) bounds this by twice its included-bit binary entropy term.
Summing gives the desired absolute-constant multiple of alpha.

For a nonconstant monotone Boolean function some coordinate is pivotal, so the
largest-weight coordinate has alpha>0. A constant restriction is a legitimate
base case. Restrictions of an LTF remain LTFs, and the total-influence split
identity has the correct coefficient one on the distinguished influence.
The resulting induction therefore proves the claimed deterministic-LTF FEI
bound if the primary KK/KOS hypotheses and conventions are exactly as stated.

No finite computation is being used as a substitute for these asymptotic
arguments. This audit does not extend the conclusion to all Boolean functions.
