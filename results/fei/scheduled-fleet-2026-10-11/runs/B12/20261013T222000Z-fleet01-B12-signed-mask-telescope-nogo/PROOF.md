# Signed-mask obstruction to the complete shared-coordinate telescope

Write

\[
 \mathcal E(r)=\sum_S\widehat r(S)^2
 \log_2\frac1{\widehat r(S)^2}
\]

for the unnormalised raw Fourier entropy.  For Boolean endpoints `u,v` and
Boolean activation `h`, put

\[
 a=(u+v)/2,\qquad b=(v-u)/2,\qquad F=a+hb
\]

and consider the natural gauge-corrected shared potential

\[
 \widetilde J(u,v;h)=\mathcal E(F)-\mathcal E(hb)+\mathcal E(b).
\]

The preceding A057 proof shows why this is the exact object in the disjoint
source/activation case.  The previous A058 run showed that one shared query
can increase it.  The issue left open there was whether a larger query block
or a complete restriction telescope repairs that local defect.

## Four-bit exact witness

Index truth tables by `0,...,15` in binary order and define

\[
 q=(1,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0),
\]

\[
 g=(1,0,0,0,0,1,0,0,1,0,1,-1,1,0,0,0).
\]

Thus `q` is the indicator of

\[
 D=\{0,5,8,10,11,12\},
\]

and `g` is a signing of the same support.  Let

\[
 a=1-q,qquad b=g,qquad u=a-g,qquad v=a+g,qquad h=v.
\]

Because `a` and `g` have disjoint supports and `|g|=q`, all of `u,v,h` are
genuine Boolean functions.  Moreover

\[
 hb=(a+g)g=g^2=q,qquad F=a+hb=1.
\]

The unnormalised Walsh numerators of `q` consist of one coefficient of
absolute value `6` and fifteen of absolute value `2`.  Those of `g` consist
of six coefficients of absolute value `4` and ten zeros.  Consequently

\[
 \mathcal E(q)=\frac9{64}\log_2\frac{64}{9}+\frac{90}{64},
 \qquad \mathcal E(g)=\frac32,
\]

and hence

\[
 \boxed{\widetilde J(u,v;h)
 =\frac{6-9\log_2(64/9)}{64}
 =-0.3042292966721747\ldots<0.}
\]

This disproves endpoint nonnegativity, not only nodewise monotonicity.

## Every query-block repair fails on the same witness

For every nonempty coordinate set `A subseteq {1,2,3,4}` and every assignment
`z` to `A`, the restricted functions `q_z` and `g_z` have identical
multisets of absolute Fourier coefficients.  This is a finite exact
certificate: `CHECK.py` compares rational Walsh coefficients on all 80
nonempty faces.  Since `F_z=1`, it follows that

\[
 \widetilde J(u_z,v_z;h_z)=0.
\]

Therefore every nonempty query block has the same strictly negative
decrement

\[
 \widetilde J(u,v;h)-\mathbb E_z\widetilde J(u_z,v_z;h_z)
 =\frac{6-9\log_2(64/9)}{64}<0.
\]

In particular, pairing two shared queries does not repair the defect, and the
complete four-coordinate telescope has a negative total.  No regrouping of
the same increments can turn them into nonnegative charges.

## All-dimensional tensor family

Let `q_m=q^{tensor m}` and `g_m=g^{tensor m}` on `4m` variables, and repeat
the construction

\[
 a_m=1-q_m,\quad b_m=g_m,\quad
 u_m=a_m-g_m,\quad v_m=h_m=a_m+g_m.
\]

Again all three functions are Boolean, `h_m b_m=q_m`, and `F_m=1`.  If
`p=||q||_2^2=||g||_2^2=3/8`, the exact product law

\[
 \mathcal E(r\otimes s)=||s||_2^2\mathcal E(r)
   +||r||_2^2\mathcal E(s)
\]

gives

\[
 \boxed{\widetilde J_m
 =m\left(\frac38\right)^{m-1}
   \frac{6-9\log_2(64/9)}{64}<0}
\]

for every `m>=1`.  Thus the obstruction is an explicit unbounded-dimension
Boolean family, although its magnitude decays.  It is not an FEI
counterfamily: the realised output is constant and has both entropy and
influence zero.

## Consequence for the active hierarchy gap

The alpha-log envelope remains valid.  What fails is the proposed mechanism
for absorbing the entire changing coherent remainder into the endpoint
potential `E(F)-E(hb)+E(b)`.  A valid universal ledger must retain an
additional joint signed-support/collision credit.  It cannot be a correction
depending only on the final value of this potential, and no fixed finite
grouping of shared physical queries repairs the issue.

The next viable mechanism is to condition the credit on how the sign pattern
of `b` concentrates the spectrum relative to the unsigned support `|b|`, or
to charge an explicit posterior divergence between these two spectral laws.
Any such credit must be tested on the tensor family above and must still be
owned by one physical source-influence or terminal-reserve budget.

Full FEI remains **OPEN**.
