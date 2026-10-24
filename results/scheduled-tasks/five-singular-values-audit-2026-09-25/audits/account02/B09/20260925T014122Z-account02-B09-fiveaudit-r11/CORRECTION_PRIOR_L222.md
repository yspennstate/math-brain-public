# Correction to prior account02/B09 line-222 finding

Source: `short.tex` blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`, line 222.

**Current verdict: PASS.** My preceding run misread the sentence “Factors with \(\beta_i=0\) are at most one and are dropped” as a cardinality assertion (“there is at most one such factor”). In context, “are at most one” describes the **values of those factors**: if \(\beta_i=|w_i|^2=0\), then \(w_i=0\), so
\[
f_i((Uy)_i+w_i\cdot z)=f_i((Uy)_i)\le 1.
\]
Therefore any number of zero-\(\beta_i\) factors may be deleted from the integrand when seeking an upper bound. The remaining \(\beta_i>0\) rows satisfy the Brascamp--Lieb frame identity and the proof proceeds unchanged.

The finite example \(n=3,d=2,U=(e_1,e_2),W=e_3\) still has two zero \(\beta_i\), but it is **not a counterexample to the actual sentence** under the correct grammatical reading; both associated factor values are <=1 and are dropped.

This file supersedes only my own earlier account02/B09 classification of line 222. The immutable earlier artifact is preserved as history.
