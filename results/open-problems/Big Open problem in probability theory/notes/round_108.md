# Round 108 log

## Goal

Turn the dyadic annular sufficient condition into a usable obstruction
statement.

## Result

Added `prop:dyadic-annular-obstruction`.

If
\[
  \limsup_{p\uparrow p_c}\frac{\mathcal R_p^*}{\bar\chi_p}>0,
\]
then there is \(\epsilon>0\) such that for every \(\alpha>0\),
\[
  \liminf_{J\to\infty}\limsup_{p\uparrow p_c}
  \sum_{j\ge J}2^{\alpha(j-J)}
  \Theta_p((2^j,2^{j+1}])
  \ge (1-2^{-\alpha})\epsilon .
\]

The proof also gives the stronger same-witness form: for every starting scale
\(J\) and every \(p_0<p_c\), one can find \(p\in[p_0,p_c)\) and a finite
non-empty \(K\) whose weighted dyadic annular profile is bounded below by the
same constant.

## Interpretation

The annular criterion now has a precise obstruction.  To prove far-leg
tightness it is enough to rule out persistent weighted annular mass carried by
one finite witness set near \(p_c\).  This is a more local target than the
global tail supremum and should be better suited to separator or shell-growth
arguments.
