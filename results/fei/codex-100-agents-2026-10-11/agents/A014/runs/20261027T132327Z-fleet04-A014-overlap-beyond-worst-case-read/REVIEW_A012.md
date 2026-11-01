# Scoped independent reconstruction of the universal full-history theorem

Source: A012-UNIVERSAL-PROJECTION-PROFILE-HISTORY version1, exact statement
SHA256669f2a9dda85bc62d80c2bbf0a54c3fed46edf550966435d9738335f0cc7bb85,
run20261027T062634Z-fleet04-A012-sparse-activation-accounting.

Verdict: HOLDS for the projection/profile history inequality in sections1-4,
including the full raw query KL, both full terminal references and an old
booking b. This is a scoped acceptance of that part of the unchanged claim.
The bundled activation-hardness guard and infinite true-kernel reverse-KL
witness are NOT independently accepted by this review. No source repair is
supplied; A014 remains eligible as an independent reviewer of the stated scope.

For each query let pbar be the average actual child spectrum. Squared signed
Fourier row addition gives pbar=pi_i p, not just a chosen spectral kernel.
KL chain rule gives L=D(p||q)-D(pbar||pi_i q)>=0. Direct expansion against
the same pi_i q gives average D_child-D_parent=J-L. Every reference-only
atom and both children remain in this identity.

Reconstruct the scalar J estimate: on positive a,b write a=c(1+t),
b=c(1-t). The second derivative of j(t)=e(1+t,1-t) is
2ln[(1-t^2)/(1+t^2)]+4/(1+t^2)<=4, and j(0)=j'(0)=0. Integrating twice,
then using absolute values to handle opposite signs, gives
e(a,b)<=(a-b)^2/2. The endpoint0 terms are continuous. Summing real child
Fourier rows yields J<=(2/ln2)Inf_i. Nothing multiplies conditional bounds.

For any finite profile partition let p,q be its masses and r=(1-t)q+tp.
The actual full update keeps q's conditional law in every positive q-cell.
Coverage makes zero q-cells also zero p-cells. For 0<t<1, expanding logs
gives exactly

 D(P||Q)-D(P||R)-D(R||Q)
   =[(1-t)/t][D(r||q)+D(q||r)]>=0.

At t=0 the fee is zero. At t=1 the profile fee is D(p||q) and equality
holds by the full conditional KL chain rule; no product0*infinity is used.
Thus updates consume their FULL fee from KL decrease, with no new budget.

Across a finite adaptive tree, the exact potential identity is

 E D_terminal +sum reach*L +sum reach*fee
  =D_root+sum reach*J+sum reach*(D_after-D_before+fee).

The last sum is nonpositive. Pivotal influence telescopes exactly, and the
SIGNED entropy increments sum to H_root-E H_terminal. Hence the whole bill
is <=b+CE_root+(2/ln2)I_root. The same fixed b is present on both sides;
it is neither refunded nor silently charged from a new root.

New application: use A014's explicit full windmill root Q, proved below28I.
All finite policies within this exact projection/profile interface then have
full bill <b+31I, for every m>=4. This does not replace prescribed true-kernel
inheritance, pay mandatory floors, or imply a productive arbitrary-core rule.

Validation is independent implementation by A014, not A012's executable:
all ternary restrictions of the one- and two-triangle physical roots, all
remaining queries, t=0,1/2,1 profile endpoints, and complete depth2 trees
with actual half-profile updates, full query contractions and full terminals.
Exact query log-vector identities and rational profile likelihood identities
are checked; rigorous logarithm intervals check the scalar and full tree
bills. out/history.json records the executed counts and result. Finite checks
supplement the reconstruction above; they do not prove arbitrary partitions
or all depths by enumeration. No Lean certificate for this theorem is claimed.
