# account02/B20 P5 issue ledger

Exact source: math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c; short.tex c4f2a997cf336ee974e15409b5bccdd8cca039d8; short.pdf 8be3aae36ecad7a9dc9b7c95978aad09499f32d0; PDF SHA-256 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423.

- C04 L41/p1 FALSE exposition: abstract random-sign sentence omits no-pivot; A=I_5 is a counterexample to the unqualified sentence.
- C07 L62/p1 UNCHECKED metadata: current-literature status only, not a proof premise.
- C05 L65/p1 FALSE exposition: a definite pair may have bounded density; only upper-envelope language is universal.
- B20-R5-L148-PADDED-SVD L148/p3 GAP: the approximation-number proof invokes the first j right singular vectors even when padded index j exceeds the number of columns. Repair j>n_cols separately: s_j(T)=0 and B=T has rank<j; use the printed kernel-intersection proof only for j<=n_cols. Downstream manuscript uses are in range; no constants change.
- C06 L148/p3 editorial only: “Both” -> “All three”.
- L222/p5 PASS: “factors ... are at most one” refers to factor values; beta_i=0 => w_i=0 => f_i((Uy)_i)<=1, and arbitrarily many may be dropped.
- C02 L319-321/p7 GAP: insert |E F|^2 <= E|F|^2 before averaging.
- C08 L398/p9 GAP presentation only: define the density formula a.e./for z!=v or assign the density value at v arbitrarily.
- C01 L412/p9 FALSE literal chart claim: delete the angular seam/null ray; Jacobian and constant unchanged.
- C03 L441/p10 GAP: state the critical indefinite level is two affine lines and hence null.
- C09 L613/p13 GAP notation/order only: define J(0)=+infinity or invoke no-atoms before E J(R-a).
- L74/p2 related-work metadata UNCHECKED.

After C01-C03 and the L148 padded-index case split, this pass found no additional theorem-level obstruction. C08/C09 are constant-neutral source hygiene.
