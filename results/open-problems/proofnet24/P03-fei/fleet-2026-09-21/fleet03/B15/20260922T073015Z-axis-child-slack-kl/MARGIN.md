# Comparable gate-margin form

The owner-requested comparable quantity is

\[
c_P(p)=-{D_{\Gamma_0}(P;p)\over W_P(p)},\qquad
W_P(p)={1\over4}\sum_i\operatorname{It}_i(P;p)-p_{\rm out}(1-p_{\rm out}).
\]

For `W_P(p)>0`, the fixed lift identity gives

\[
c_P(p)=a^\dagger-{D_{\Gamma^\dagger}(P;p)\over W_P(p)},
\qquad a^\dagger=0.268204856.
\]

On a five-input gate, `sum_i It_i<=5`, hence `W_P<=5/4`.  The axial theorem in `REPORT.md` gives, before using its additional nonnegative KL credit,

\[
D_{\Gamma^\dagger}(P;p)\ge0.000222928605760.
\]

Therefore throughout the certified axial collar,

\[
\boxed{c_P(p)\le0.268204856-{4\over5}(0.000222928605760)
=0.268026513115392.}
\]

This is only a comparable off-center margin bound for the proved axial region.  It is not a claim that this value is sharp.  If `W_P=0`, the quotient `c_P` is undefined and the defect statement in `REPORT.md` is the relevant one.
