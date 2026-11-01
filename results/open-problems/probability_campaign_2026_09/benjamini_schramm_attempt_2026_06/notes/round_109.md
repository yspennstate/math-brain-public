# Round 109 log

## Goal

Translate the annular obstruction into the operator and pointwise shell
languages used by the rest of the manuscript.

## Result

Added `cor:dyadic-operator-obstruction`.

If
\[
  \limsup_{p\uparrow p_c}\frac{\mathcal R_p^*}{\bar\chi_p}>0,
\]
then for some \(\epsilon>0\) and every \(\alpha>0\),
\[
  \liminf_J\limsup_{p\uparrow p_c}
  \sum_{j\ge J}2^{\alpha(j-J)}
  \left(\frac{\|T_p^{(2^j,2^{j+1}]}\|_{2\to2}}{\bar\chi_p}\right)^2
  \ge (1-2^{-\alpha})\epsilon .
\]

For connected locally finite graphs, the same lower bound holds with the
pointwise shell envelope
\[
  \frac{\sum_{2^j<n\le 2^{j+1}}\tau_p^{\max}(n)\|S_n^G\|_{2\to2}}
       {\bar\chi_p}
\]
in place of the annular operator norm.

## Interpretation

Under the mean-field susceptibility input, any equality case
\(p_c=p_{2\to2}\) must carry persistent normalized dyadic annular operator
mass arbitrarily far out.  This turns a possible counterexample into a
quantitative shell-growth obstruction.
