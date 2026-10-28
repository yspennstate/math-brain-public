# Scoped independent reconstruction of A078's original collision account

Source: A078/runs/20261022T211614Z-account03-A078-coding-and-padding/PROOF.md, signed account equations(2)-(4), physical/reserve identities(5)-(6), stopped bookkeeping(8)-(9) CONDITIONAL on its declared input(7), and original donor equation(10). Verdict: HOLDS AT THESE SCOPED LOCATORS; no repair supplied. This is not whole-bundle acceptance or a review of arbitrary shared queries.

Reconstruction uses the complete physical truth table with private bits low-order, shared bits high-order, and vertex edits at0 and1. For each nonempty private label put m=a^2+b^2. If m>0, its collision is exactly

    k(a,b)=m[h2((a+b)^2/(2m))-h2(a^2/m)-1].

Hence -2m<=k<=0, and Parseval gives -4e<=Xi<=0. With a single original account K=B-Xi_start+Xi_current, K_start=B and Delta Xi=K_parent-average K_child exactly. Finite original-reach summation gives Xi_start-E Xi_leaf+E K_leaf=B, with no independence assumption on V,W, no clipping, and no repeated 4e charge. If B>=4e, every conditional K>=B-4e because Xi_start<=0. This proof also holds at every stopped frontier.

For the physical wrapper, disjoint edited shared vertices give Inf_i(F)=e(Inf_i(V)+Inf_i(W)). Child means mu+/-Vhat(i),nu+/-What(i) give the stated single reserve release by squaring. Substituting the declared local mean inequality into the account identity and summing proves the stopped formula with BOTH core entropy decrements and complete F terminal entropy retained. The substitution is conditional on that local inequality, so it is not an independent acceptance of the whole upstream analytic chain. Our MIXED_TWO_POINT_PROOF.md section1 supplies a separate curvature reconstruction of that input.

Finally, V=y*b_k has 2^k Fourier rows of square2^-k, so H(V)=k. Each bent input has influence1/2 and y has influence1, yielding I(V)=k/2+1 and S=e(3k/2+5). After the OLD D0 and first4e debit, B=S-D0-4e. Admission D0<=S-8e gives B>=4e and expected retained K>=S-D0-8e. This is one original surplus; inherited eH(V) and S are disjoint parts of5eI(V). No descendant certificate is required or reissued.

Executed independent reproduction: code/check.py constructs actual Boolean spectra, direct edge counts and direct character sums; out/validation.json records12,792 exact assertions, all828 ordered two-point roots and66 one-point roots, and three complete-sibling mixed histories. out/MIXED_LEDGER.json records every retained state and terminal, old first-query debit, inherited erasures, original-bank carry and physical influences. This is an A076 implementation and a prose reconstruction, not a Lean formalization. A076 is a contributor only to the NEW shared-query extension in this run, and this acceptance concerns A078's prior account identities, not that new extension.
