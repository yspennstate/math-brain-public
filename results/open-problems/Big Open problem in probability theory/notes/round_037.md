# Round 037 log

## Goal

Audit Yamamoto's two \(T_d \Box \mathbb Z\) papers as external inputs for the
remaining \(T_3\Box\mathbb Z\) bottleneck.

## Sources checked

Downloaded and extracted the arXiv sources for:

- Kohei Yamamoto, "An upper bound for the critical probability on the Cartesian
  product graph of a regular tree and a line", arXiv:1705.06873,
  https://arxiv.org/abs/1705.06873.
- Kohei Yamamoto, "The critical probability for the percolation on the
  Cartesian product graph of a regular tree and a line", arXiv:1810.07162,
  https://arxiv.org/abs/1810.07162.

The extracted source files are in `research/external/`.

## Findings

The 2017 paper proves
\[
  p_c(T_d\Box\mathbb Z)\le \frac1d,\qquad d\ge3,
\]
and gives the additional numerical improvement
\[
  p_c(T_4\Box\mathbb Z)<0.225.
\]
It obtains these from a lower bound on Schonmann's fixed-direction exponent
\(\alpha(p)\).  In the notation of the paper, the finite criterion is:
if there are \(p\) and \(x\in(1,1/p)\) with
\[
  h_p(x)\ge \frac{1-p}{p},\qquad x<d-1,
\]
then \(p_c(T_d\Box\mathbb Z)\le p\).  The proof of the general theorem takes
\(x=(1-p)/p\), which yields the \(1/d\) bound.

The 2018 paper proves the exact characterization already used in the
decorated-strip route:
\[
  p_c(T_d\Box\mathbb Z)
  =
  \alpha^{-1}\!\left(\frac1{d-1}\right).
\]
For \(d=3\), this is the criterion \(\alpha(p)>1/2\Rightarrow
p>p_c(T_3\Box\mathbb Z)\).

## Numerical comparison

For \(d=3\),
\[
  \frac{3-\sqrt5}{2}=0.381966011250,\qquad
  \frac13=0.333333333333,
\]
whereas the current decorated-strip certificate is
\[
  p_c(T_3\Box\mathbb Z)<\frac{5909}{20000}=0.29545.
\]
Thus the 2017 \(d=3\) upper bound is weaker than the current certificate.

The Lyons-Peres lower bound on \(p_u\) at \(d=3\) is
\[
  \left(\sqrt2+1+\sqrt{2\sqrt2-1}\right)^{-1}
  =0.265505028230,
\]
which is also below the current \(p_c\)-upper certificate.  Therefore these
external bounds do not close \(T_3\Box\mathbb Z\) and do not improve the
current SAW-side target
\[
  \gamma_{\rm SAW,2}(T_3\Box\mathbb Z)
  <
  \frac{20000}{5909}
  \approx3.384667456422.
\]

## Consequence

The Yamamoto sources validate the fixed-direction framework behind the
decorated-strip lower process, but they do not provide a stronger
non-oriented \(p_c\) comparison for \(T_3\Box\mathbb Z\).  The remaining
routes are still:

1. sharpen the decorated-strip or another \(\alpha(p)\) lower bound below
   \(5909/20000\);
2. improve the operator-side SAW bound below \(20000/5909\);
3. find a genuinely different comparison for \(p_c\) or \(p_{2\to2}\).
