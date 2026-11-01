# Actual-disagreement controller reserve graft with shared data

Entropy is in bits, influence ordinary. Let a be any Boolean seed on a fresh block z. Let u,v be ANY two Boolean signs on one common data cube x; their data may overlap arbitrarily. Introduce fresh sign w, and define

M(w,x)=(u(x)+v(x))/2+w*(u(x)-v(x))/2,
F(z,w,x)=(u(x)+v(x))/2+w*a(z)*(u(x)-v(x))/2.

Write b=(u+v)/2, c=(u-v)/2, and t=E c^2=Pr[u!=v]. Fix finite complete own-history trees T_a for a and T_M for M. Global policies may adaptively interleave T_a seed queries with T_M data queries. A T_M query of w is allowed only after T_a reaches its zero-reserve constant leaf; the sign of w is then consistently translated. Each shared data coordinate is queried once. Independent initial randomization may be conditioned on first. No inherited reserve bound is assumed.

## 1. Exact spectra, without independent-core substitution

The b sector has no w label. The c*a sector always has the fresh w label. These sectors are disjoint even at empty seed or data frequencies; inside the second sector, seed and data factors use disjoint coordinates. Therefore

H(F)=H(M)+t H(a).

This follows from the unnormalized product identity: sum_{S,T} h(chat(T)^2 ahat(S)^2)=H(chat^2)+t H(a), where h(p)=p log2(1/p) and sum ahat^2=1. It holds for arbitrary means, non-flat core spectra and shared core data. No mean-only profile is needed.

At a seed query i, actual directional edge disagreement occurs only on the data event u!=v. Thus d_i(F)=t d_i(a), and D_i(F)=t D_i(a). At a data query j, t is a conditional probability of one fixed physical event. Its two actual restrictions satisfy t=average t_child. The seed's remaining function is fixed at that query. Thus the t H(a) term has zero expected decrement, giving D_j(F)=D_j(M). The tag keeps w*a fair even after seed exposure, so d_j(F)=d_j(M)=(d_j(u)+d_j(v))/2. All statements hold at actual partial histories, with the same restricted u,v; no independent copies are created.

## 2. Nonnegative graft and finite stopping budget

Suppose r_a>=0 is any C_a-priced potential on T_a and r_M>=0 any C_M-priced potential on T_M, both zero at complete constant leaves. They may be the complete least reserves. Define on the actual mixed history

R=t*r_a+r_M.

At a seed query the profile r_M and t are unchanged, so its drift pays t D_a at price C_a against actual influence t d_a. At a shared-data query r_a is unchanged and t is harmonic, so the inherited controller term t*r_a has ZERO drift. The SAME r_M drift pays the actual D_M at price C_M. No profile is renewed at the child. At w, T_a is at its zero-reserve constant leaf, so a is constant and r_a=0; F is the sign-translated actual M and the r_M potential applies. Consequently R is a nonnegative potential at price alpha=max(C_a,C_M) for every finite declared mixed policy.

For any complete such policy, Q_alpha(F)<=t_root*r_a(root)+r_M(root). In particular Q_alpha(F)<=t Q_C(a,T_a)+Q_C(M,T_M) when the two prices are C. This graft extends the preceding parity half-transfer to unequal non-flat SHARED cores, retaining the complete paired-profile reserve as its own owner rather than asserting it is zero.

At a finite partial stop tau the accepted finite budgets yield
H(F_root)<=C_a Pi_seed+C_M Pi_profile+R_root+E[H(F_tau)-R_tau].
Both actual terminal entropy and actual terminal reserve remain. Since all entropy decrements are nonnegative, E R_tau<=R_root+C_a Pi_seed+C_M Pi_profile. Each original influence account is used only for its reached query type. These are applications of the established finite interface, not new optional-stopping identities. No unbounded-depth or varying-core limit is taken.

If the profile data queries finish before the seed, u,v are constants at every data frontier; t is then 0 or 1, while the actual remaining function is a constant or +/-w*a. The t*r_a controller owner remains on disagreeing outcomes. Finishing the data does not erase it.

## 3. An unequal non-flat shared-data query, and the false proxy

Use three binary data bits, u=-1 only at vertex0 and +1 elsewhere; v=-1 at vertices0 and2 and +1 elsewhere. Both are nonconstant and non-flat. At the query of data bit0:

root means (Eu,Ev)=(3/4,1/2), actual t=1/8;
child bit0=0 means (1/2,0), actual t_child=1/4;
child bit0=1 means (1,1), actual t_child=0.

Hence the inherited controller coefficient has exactly zero fair drift. The independent-core proxy t_ind=(1-Eu*Ev)/2 instead equals5/16 at the root and has child mean1/4, producing a false release1/16. In general its artificial drift at a shared-data query is beta_u*beta_v/2, with beta_j=(mean_child0-mean_child1)/2. Independence is a substantive hypothesis in A030's mean-product transport and is NOT refuted at its stated scope.

In this example the actual profile entropy decrement D_data(F)=D_data(M) is independent of how difficult the fresh seed a is. The false proxy would claim a controller-reserve release Q_C(a)/16 even though the actual term releases zero. A supplied controller reserve cannot be spent using that fictitious coefficient.

This discrepancy can grow without bound at a fixed physical query. At C_a=4 take the three-bit point-defect seed a0=-1 only at0. Its first-query local debt ell=D_i(a0)-4d_i(a0) is strictly positive (certified separately). For a product of L independent copies, prescribe the first coordinate of each copy before finishing any copy. Each such query has the same ell, by product Fourier entropy and influence, unaffected by revealed coordinates in other copies. Iterating the Bellman inequality with nonnegative frontier reserves gives Q_4(a0^tensor L)>=L ell. Thus the fake shared-data release is at least L ell/16, while the actual release stays zero and the physical data influence is fixed. This is a refutation of a bookkeeping substitution, not an unbounded H/I family or a disproof of FEI.

## 4. Costs which are still unpaid

The fresh tag is essential to the proved disjoint-sector entropy identity and to keeping the data-query seed term harmonic. If w is exposed while a remains nonconstant, the sectors collide; no theorem here pays that untagged signed profile correction. No uniform initial bound on r_a or r_M in terms of unused influence is supplied. The profile M may itself retain arbitrary shared-core difficulty. Existing A038/A039 certified source surplus must be carried as the same account if used to certify r_M; it cannot be renewed after this data query.

The first unsupported universal line is pricing the tag-exposed collision with the supplied remaining controller/profile reserves and both actual child terminal references. NEXT is that one tag/controller exposure at the unequal-core frontier above, starting with the explicit r_a and r_M already transported, rather than another root-only spectrum census.
