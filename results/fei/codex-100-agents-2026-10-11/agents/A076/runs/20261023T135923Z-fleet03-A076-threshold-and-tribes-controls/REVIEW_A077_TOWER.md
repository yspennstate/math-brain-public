# Independent scoped review: A077 positive-face tower closure

Reviewer A076/fleet03. Source: agents/A077/runs/20261023T121221Z-fleet03-A077-sparse-defect-towers/PROOF.md, section6 equations11-13, with spectrum section2 and original physical source section4 as dependencies. Verdict: HOLDS CONDITIONAL ON THE SUPPLIED THRESHOLD THEOREM. This review does not accept the whole claim bundle or inherited prefix/local-price theorem.

Reconstruction: each face indicator has Fourier l1 norm1 and unnormalized squared-spectrum entropy2c p. The nonempty-private product rows give p[H(V)+H(W)]+Xi+2R and the mean-sector correction E-p[g(mu)+g(nu)]. Xi<=0: with s=a^2+b^2, its summand equals s[H(rotated two-point distribution)-H(original two-point distribution)-1]<=0; s0 is immediate. Thus R<=1 and |E-H(h)|<=24 imply H(F)<=p[H(V)+H(W)]+9I0+26. All terms use the actual complete spectrum, not a one-coordinate erasure surrogate.

The two face edits can affect original shared pivots only on nonseparator address coordinates; the union bound loss is at most4(c-1)p<=3/4 because c>=4. Original I0>=15/8 implies I_shared(F)>=I0-3/4>=(3/5)I0. Therefore9I0+26<=(343/15)I0<=(343/9)I_shared(F).

For each PRIVATE physical edge the shared face events are disjoint, so Inf_i(F)=p[Inf_i(V)+Inf_i(W)] exactly, even if the two profiles share all private inputs and are correlated. Summing produces the true total influence partition. Consequently H(V),H(W)<=C0 I implies H(F)<=max(C0,343/9)I(F). Induction along any finite acyclic wrapper construction preserves that same constant and does not add one constant per depth. Shared variables are fresh and independent at each wrapper as required.

The inherited-prefix source history needs its own hypotheses and is not accepted by the static tower induction. The author explicitly distinguishes these scopes; no repair is needed within the reviewed statement. The nonsubcube extension in A076's present proof is new and is not certified by this review. Neither statement proves universal FEI.
