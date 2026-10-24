# A precise leaf-induction obstruction and a target for synthesis

Unfinished coordinator lead, 15 September 2026. This is not a tree-sparse concavity theorem.

For a leaf joined to a core at coordinate i, write its mean p, complex link z, and core K. Conditioning on that leaf gives the exact entropy

    h(p)+p H(K-|z|^2 e_i e_i*/p)
         +(1-p) H(K+|z|^2 e_i e_i*/(1-p)).

If p is fixed and entropy is concave in all allowed core directions, the weighted conditional expression is jointly concave in K and s=|z|^2. Removing the link increases entropy by subadditivity, so the concave function is nonincreasing in the feasible s-direction. This is the valid fixed-leaf mechanism behind C059/C062.

A naive induction for all tree-sparse kernels fails to justify the next step: after deleting one leaf, its neighbor's conditional mean changes. When that neighbor is later deleted, its Bernoulli weight is no longer fixed. The perspective variables contain pK, which is bilinear if both p and K move. Concavity of the smaller core alone therefore does not close the induction.

C057 gives the exact varying-pivot Hessian correction. C067 controls a finite version under matrix and atom-order hypotheses. C076 now has a stronger paired finite correction for a moving coherent pair, even where the individual atom-order tests fail. A concrete next target is the five-vertex path with independently moving central links or leaf means: determine whether the C076 paired correction cancels the newly varying weight and yields an entire nonperturbative family. Fixed-amplitude-orientation double stars, common scalar scaling, and weak singleton borders are already covered and should not be recounted as new scope.
