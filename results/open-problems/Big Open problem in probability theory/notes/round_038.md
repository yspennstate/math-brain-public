# Round 038 log

## Goal

Push the decorated-strip \(p_c\)-upper certificate for the remaining
\(T_3\Box\mathbb Z\) case beyond the height-ten bound
\[
  p_c(T_3\Box\mathbb Z)<5909/20000.
\]

## Faster depth-one screening

Updated `scripts/decorated_strip_float_scan.py` with a specialized
side-depth-one ladder transfer.  The previous floating scanner used the generic
frontier state even for depth one.  The new path removes the open-edge-count
coordinate and propagates probabilities directly.  I also replaced the repeated
subset summation in the Perron iteration by a weighted zeta transform:
\[
  \sum_{S\subseteq A} p^{|S|}(1-p)^{|A|-|S|} f(S)
  =
  (1-p)^{|A|}
  \sum_{S\subseteq A}\left(\frac{p}{1-p}\right)^{|S|}f(S).
\]

Validation against known exact certificates:
\[
\begin{array}{c|c|c|c}
h&p&\rho_{\rm lower}&\text{known exact comparison}\\
\hline
9&0.29716&0.500028359038&\text{matches Round 026}\\
10&0.29545&0.500014271966&\text{matches Round 028}.
\end{array}
\]

The height-eleven floating screen gives
\[
  \rho_{\rm lower}(h=11,p=0.2945)=0.500920226613,
\]
while
\[
  \rho_{\rm lower}(h=11,p=0.2940)=0.499691949256.
\]
Thus the height-eleven crossing is near \(0.29413\).

## Fixed-rational exact checker

Added `scripts/decorated_strip_fixedp_certificate.py`.  For a chosen rational
\(p=p_{\rm num}/p_{\rm den}\), it propagates exact integer numerators directly
with common denominator \(p_{\rm den}^{3h-2}\), rather than storing the full
open-edge polynomial.  It then checks \(2Mv>v\) with integer arithmetic.

The fixed-rational checker reproduces the known height-nine exact certificate:
\[
  h=9,\quad p=7429/25000:
  \qquad \min_A\frac{2(Mv)_A}{v_A}=1.00004878895.
\]

For height eleven, the following rational values certify:
\[
\begin{array}{c|c|c}
p&\rho_{\rm lower}\text{ from float Perron vector}
&\min_A 2(Mv)_A/v_A\\
\hline
589/2000&0.500920226613&1.00179484851\\
1471/5000&0.500183139816&1.00031758887\\
5883/20000&0.500060327107&1.00011629593.
\end{array}
\]

The final run used scale \(10^9\), matrix size \(2^{11}-1=2047\), and
one-column edge count \(31\).  The integer margin was positive, so the last
line is a rigorous certificate.

## New consequence

Yamamoto's criterion now gives
\[
  p_c(T_3\Box\mathbb Z)<\frac{5883}{20000}=0.29415.
\]
The corresponding SAW/operator-side target improves to
\[
  \gamma_{\rm SAW,2}(T_3\Box\mathbb Z)
  <
  \frac{20000}{5883}
  \approx3.399626041135.
\]

This is a real improvement over the previous target
\[
  20000/5909\approx3.384667456422,
\]
but it still does not close the case: the best exact finite-length SAW bound
remains
\[
  \|C_{15}\|_{2\to2}^{1/15}\le3.647511532644.
\]
