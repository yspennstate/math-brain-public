# Exact five-bit obstruction

All logarithms are base two.  For a Boolean (f), put

\[
p_S=\widehat f(S)^2,
\quad \pi(S)=\sum_{T\supseteq S}p_T,
\quad U(f)=\sum_Sp_S\log {\pi(S)\over p_S}.
\]

For coordinate (i), pair (S\not\ni i) with (S\cup\{i\}) and define

\[
B_i=\sum_{S\not\ni i}\left[
p_S\log{p_S+p_{S\cup i}\over p_S}+
p_{S\cup i}\log{p_S+p_{S\cup i}\over p_{S\cup i}}
\right].                                                     \tag{1}
\]

This is (H(S_i\mid S_{-i})).  The exact upper-set restriction identity

\[
\Delta_iU=B_i-\Gamma_i+K_i                                  \tag{2}
\]

shows that (K_i\le\Gamma_i+c\operatorname{Inf}_i) is exactly

\[
\Delta_iU\le B_i+c\operatorname{Inf}_i.                    \tag{3}
\]

## Witness

Let (f:\mathbb F_2^5\to\{-1,1\}) be (+1) at

\[
1,3,4,8,10,11,13,14,15,16,18,19,21,22,25,28,30
\]

and (-1) elsewhere, using little-endian integer encoding.  Take (i=1).
The truth mask is (1382935834), and direct edge counting gives

\[
\operatorname{Inf}_i={14\over32}={7\over16}.                \tag{4}
\]

## Integer reduction

For a truth table (v) of length (N), let (w_S\in\mathbb Z) be its
unnormalized Walsh transform.  Then

\[
N^2U(v)=\sum_{S:w_S\ne0}w_S^2
\log{\sum_{T\supseteq S}w_T^2\over w_S^2}.                 \tag{5}
\]

For a child table of length (N/2), its contribution to the average of the
two child potentials has multiplier (2) in the (N^2) normalization.
Formula (1) has the same (N^2) denominator.  Consequently

\[
3N^2\left(\Delta_iU-B_i-{4\over3}\operatorname{Inf}_i\right)
=\log R,                                                     \tag{6}
\]

where exact factor collection by `CERTIFY_LOCAL_NO_GO.py` gives

\[
R={7^{588}11^{96}17^{24}19^{624}23^{300}
\over2^{3148}3^{276}5^{216}13^{540}}.                       \tag{7}
\]

The numerator and denominator of (7) are computed as exact integers.
Their bit lengths are 6089 and 6086 respectively, and direct integer
comparison gives numerator (>) denominator.  Therefore (R>1), so (6)
is positive.  This proves

\[
\boxed{\Delta_iU>B_i+{4\over3}\operatorname{Inf}_i}.        \tag{8}
\]

The high-precision decimal printed only for readability is

\[
\Delta_iU-B_i-{4\over3}\operatorname{Inf}_i
=0.0011331466354368383948617\ldots .                        \tag{9}
\]

In particular, (3) is false for every (c\le4/3), including the
coefficient-one candidate (K_i\le\Gamma_i+\operatorname{Inf}_i).

## Why the aggregate route survives

Summing (2) gives

\[
G=B-\sum_i\Gamma_i+\sum_iK_i,
\qquad B=\sum_iB_i\le H.                                   \tag{10}
\]

Thus the still-open inequality (G\le H+I) asks only for

\[
\sum_i(K_i-\Gamma_i)\le I+(H-B),                            \tag{11}
\]

which permits one coordinate's excess to be paid by global dual-entropy
slack.  For the witness, exact Walsh evaluation gives

\[
H+I-G=3.9940103914495344218\ldots>0.                        \tag{12}
\]

Therefore (8) is a no-go for the local mechanism, not a falsifier of the
aggregate candidate.  No universal GU' inequality is proved here.

