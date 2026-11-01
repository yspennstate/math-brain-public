# Strengthening — combine the two logarithmic losses before bounding

The main report proved the balanced-uniform character-cofactor local closure with the sufficient center

\[
C_{\rm sec}=3+\sqrt2+\frac{1+e^{-1}}{\ln2}=6.387646448685102\ldots .
\]

That constant can be improved immediately without changing the mechanism. For `0<d<=1/2`, the exact lower certificate in the report satisfies

\[
\frac{F_C(d)}d
=C-2(1-d)-\frac{4(1-d)}{1+(1-2d)^2}
+d\log_2d+\frac{(1-d)^2}{d}\log_2(1-d).
\]

Do **not** bound the two negative logarithmic terms separately. From

\[
-\ln(1-d)\le\frac{d}{1-d}
\]

we get

\[
-d\log_2d-\frac{(1-d)^2}{d}\log_2(1-d)
\le\frac{1-d-d\ln d}{\ln2}.
\]

The function `g(d)=1-d-d ln d` has derivative `g'(d)=-2-ln d`, hence its unique maximum on `(0,1/2]` is attained at `d=e^{-2}` and equals `1+e^{-2}`. Also

\[
2(1-d)\le2,
\qquad
\frac{4(1-d)}{1+(1-2d)^2}\le1+\sqrt2.
\]

Therefore

\[
\boxed{
F_C(d)\ge d\,[C-C_{\rm sec}^{(2)}]
}
\]

with the stronger explicit threshold

\[
\boxed{
C_{\rm sec}^{(2)}
:=3+\sqrt2+\frac{1+e^{-2}}{\ln2}
=6.0521561452448225\ldots .
}
\]

For `d>=1/2`, the main report's `F_C(d)>=C/2-2` remains unchanged. Hence Theorem B15-SECTOR-KL-01 holds for every symmetric potential with center

\[
C\ge C_{\rm sec}^{(2)}=6.0521561452448225\ldots,
\]

not merely for the earlier `6.387646...` threshold. For the live center

\[
C^\dagger=6.521851214,
\]

the certified small-disagreement linear margin is at least

\[
C^\dagger-C_{\rm sec}^{(2)}
=0.4696950687551775\ldots .
\]

This strengthening is analytic and all-dimensional; no finite search is used.
