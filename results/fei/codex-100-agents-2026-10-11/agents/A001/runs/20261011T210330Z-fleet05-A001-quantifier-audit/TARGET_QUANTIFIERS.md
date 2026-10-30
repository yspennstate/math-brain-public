# exact target, quantifiers, hypotheses and units

Run: 20261011T210330Z-fleet05-A001-quantifier-audit. Agent A001, stream B01. Artifact: source-bound quantifier audit. Full FEI remains OPEN. Independent acceptance of this audit is pending.

The target is

\[
\exists C\in[0,\infty)\ \forall n\in\mathbb N_0\ \forall f:\{-1,1\}^n\to\{-1,1\},\qquad H_2(f)\le C I(f).
\]

Here \(\widehat f(S)=2^{-n}\sum_x f(x)\prod_{i\in S}x_i\), \(P_f(S)=\widehat f(S)^2\), \(H_2(f)=\sum_SP_f(S)\log_2(1/P_f(S))\), and \(I(f)=\sum_S|S|P_f(S)=\sum_i\Pr[f(X)\ne f(X^{\oplus i})]\). Set \(0\log(1/0)=0\). Constants, including the zero-dimensional cube, have H=I=0. Ratios are taken only for nonconstant functions, equivalently I>0. The assertion \(\forall n\exists C_n\) is weaker and elementary; it is not FEI.

Equivalently, \(C_{\rm FEI}=\sup_{n,f:I(f)>0}H_2(f)/I(f)<\infty\). A disproof requires actual Boolean signs \(f_j\) with \(H_2(f_j)/I(f_j)\to\infty\). Refuting a proposed constant, a local payment, or a non-Boolean relaxation does not satisfy this target. Natural-log entropy is \(H_{\rm nat}=(\ln2)H_2\).

Use \(D_{\rm char}=\sum_i\min(I_i,1-I_i)\), \(v=\operatorname{Var}(f)\), and \(\delta=I-v\). These are distinct from dual total correlation, physical pivotal influence under biased measures, and the influence drop of a restriction. Uniform H+ is the nonempty-atom contribution; under biases it includes the product-basis correction and can be negative.

