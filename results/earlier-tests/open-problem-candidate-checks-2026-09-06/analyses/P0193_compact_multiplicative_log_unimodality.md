# P0193: independent algebra and source check

Status: scoped mathematical check, 6 September 2026. No change was made to the
candidate.

The candidate uses the two-atom probability law with equal masses at 1/10 and 10.
Its source is Hasebe, Ueda and Wang, arXiv:2009.13848v1. The complete title page and
pages 2 through 11 were read from the exact archived PDF. The relevant items are
the density parametrization on pages 2–3, Lemma 3.2, Lemma 4.1 and its proof on
pages 8–9, and Problem 4.7 on page 11. The question is eventual log-unimodality for
an arbitrary compact initial support inside the positive line. The candidate uses
precisely this meaning of log-unimodality and the same time normalization.

## Algebraic route independent of the logarithmic kernel calculation

Write c = -cos(R), so c belongs to [0,1] when R belongs to [pi/2,pi]. Define

    A = r^2 + 20 c r + 100,
    B = 100 r^2 + 20 c r + 1.

Direct substitution of the two atoms into the original integral gives

    I(r,c) = 5 r (A+B)/(AB).

Both denominators are positive for r>0 and c in [0,1]. The level equation
I(r,c)=1/10 is therefore equivalent, without extraneous positive roots, to

    P(r,c) = 100 r^4 + (2020 c - 5050) r^3
             + (10001 + 400 c^2 - 2000 c) r^2
             + (2020 c - 5050) r + 100 = 0.

With y=r+1/r this becomes P(r,c)=100 r^2 Q(y,c), where

    Q(y,c) = y^2 + (101 c/5 - 101/2) y
                    + 9801/100 + 4 c^2 - 20 c.

For every c in [0,1],

    Q(2,c) = 101/100 + 102 c/5 + 4 c^2 > 0,
    Q(101/10,c) = -31003/100 + 9201 c/50 + 4 c^2
                 <= -12201/100 < 0.

As Q tends to positive infinity at positive infinity, it has one root strictly
between 2 and 101/10 and another strictly greater than 101/10. These are distinct
and exhaust its roots because Q is quadratic. Each y>2 has exactly two distinct
positive preimages r=(y +/- sqrt(y^2-4))/2. Different y values have disjoint
preimages. Thus the original integral has exactly four positive solutions at the
chosen level, uniformly for all c in [0,1]. This uses neither a root finder nor
an asymptotic passage through the boundary R=pi.

For every finite t>=5 pi, choose R in [pi/2,pi) by R/sin(R)=t/10. The function
R/sin(R) is continuous and strictly increasing there, begins at pi/2 and tends to
infinity. Therefore the chosen R exists, is unique, and makes the source criterion's
right-hand level R/(t sin R) exactly 1/10. Lemma 4.1 now rules out log-unimodality
for every one of these times.

## Separate sign and density checks

Substitution in the original integral gives I(1,c)=10/(101+20c)<1/10. At r=1/10
or 10, one half-weighted atom alone contributes 1/[4(1+c)]>=1/8>1/10. At the two
tails I tends to zero. These produce four distinct crossings independently of
the quartic calculation. Exact rational controls additionally use finite exterior
points 1/1000 and 1000; five choices of c give the required alternating signs.

The source necessity direction follows from its density parametrization and a
homeomorphism of the positive line. Four solutions at a positive level correspond
to four distinct points of the log-density at that level. Analyticity on the
positive-density region excludes a flat positive interval that might otherwise
permit a unimodal function to have many equal-height points. The source proof
supplies this exact exclusion. Compact support stays strictly away from zero;
the question permits atomic initial laws. The initial law is multiplicatively
symmetric but not log-unimodal, so the symmetric-and-log-unimodal preservation
theorem supplies no contrary conclusion. Ordinary unimodality is not established
or refuted by this argument.

## Strongest counter-case and controls

The likely ways to break the claim are a missing half mass, an incorrect kernel
sign or time normalization, or applying a sufficient criterion as if it were
necessary. The source read and direct substitution address those concerns. The
checker rejects every omitted-half-mass identity and rejects the asserted four-sign
pattern after the atoms collapse to a single atom. Its finite cases are controls,
not a proof of the uniform statement; the inequalities above establish that part.

A less widely separated pair may lose the valley, so this is not a claim about all
two-atom laws. The construction makes no optimal-time claim and needs no assertion
about times smaller than 5 pi. An already published solution would defeat novelty
without changing the mathematical validity of this construction.

## Literature and evidence limitations

Focused queries of the exact title, Problem 4.7, compact initial laws and
counterexamples located the original publication and the authors' publication
pages. The publisher identifies the 2022 journal article. Auer's later paper at
arXiv:2505.05984 concerns the Brownian law and its expression through a semicircle
and uniform law; its abstract alone is not an exhaustive check of general initial
laws. No later resolution was verified in this bounded search. This is not a
certificate that the problem remains open in September 2026.

It was discarded before substantive claims. The exact validated source ID and URL
selected the correct fourteen-page paper; its SHA256 was recorded. Reading
the title page confirmed the authors in title case. Neither failed retrieval was treated
as a successful source check.

Primary references:

- https://arxiv.org/abs/2009.13848
- https://www.impan.pl/en/publishing-house/journals-and-series/colloquium-mathematicum/all/169/2/114564/log-unimodality-for-free-positive-multiplicative-brownian-motion
- https://www.math.sci.hokudai.ac.jp/~thasebe/index.html
- https://sites.google.com/view/yukiueda1114/publication
- https://arxiv.org/abs/2505.05984
