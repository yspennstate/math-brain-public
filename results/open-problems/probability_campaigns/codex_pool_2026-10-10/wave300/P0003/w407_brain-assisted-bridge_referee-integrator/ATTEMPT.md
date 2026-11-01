# P0003 referee attempt

P0003 is Grimmett's Question 2.2 about uniform fixed-n honeycomb SAWs from the origin, suitably rescaled; see SOURCE_STATUS.json. Duminil-Copin--Smirnov's chordal critical length-weighted domain conjecture is related but defines a different ensemble. My lane tests whether local identities and a conditional chordal restriction route reach the actual question.

Duminil-Copin--Smirnov prove the connective constant mu=sqrt(2+sqrt(2)), so x_c=1/mu. Their parafermionic Lemma 1 requires a simply connected honeycomb domain, a boundary source a, path-sum F with winding spin 5/8, and x=x_c. It concludes only sum_(m adjacent v)(m-v)F(m)=0 at each vertex. It does not assert compactness of F, convergence of normalized F, curve tightness, or positive endpoint partition-function asymptotics. Section 4 explicitly says the local relation is insufficient to obtain a limit.

I independently derived w406's key obstruction. With zero boundary-halfedge data, reweight each internal edge e=(u,v) by X_e=(v-u)F(m_e)/2. The vertex equations become incidence equations B X=0. A single oriented hexagonal face supports circulation X_e=delta/2, hence F(m_e)=delta/(v_e-u_e). Adjacent midpoint values differ by 1 across sqrt(3)delta/2 while |F|=1 and boundary data stay zero. Thus the local equation plus sup-norm and boundary values does not force uniqueness or mesh-uniform equicontinuity. This family need not be a true SAW path-sum, so it refutes only that abstract inference.

I independently checked w405's bridge. Its finite graph identity is exact. Its outer-buffer lemma transfers avoidance probabilities under weak compact-trace convergence when every fixed outer-buffer ratio has a limit and those limits converge as buffers shrink. Portmanteau handles zero-distance atoms because buffer radii stay strictly positive. A raw avoidance event can fail to pass to the limit, as its explicit simple broken-line example shows.

The bridge stops before even the chordal conjecture. It requires (T) tightness of critical SAW laws in a suitable curve topology with simple interior subsequential limits, and (B) the positive critical endpoint partition-function ratio for every fixed smooth buffered hull. Neither follows from the known connective constant or signed parafermionic relation. LSW Proposition 3.3 identifies a continuum law only after its sample-space and smooth-hull hypotheses hold. Theorem 6.1 supplies the formula for SLE(8/3), not for discrete SAW. Even if T and B were proved, a separate fixed-length/free-endpoint transfer with the correct spatial scale would be necessary for Grimmett's P0003.

## Exact finite conditioning step and its limit obstruction (w407; w410 audit pending)

Let G be any finite graph with origin o, let Gamma_m(G,o) be its vertex-simple m-edge paths from o with no endpoint condition, and let c_m(G,o)=|Gamma_m(G,o)|. For x>0 set Z_G(x)=sum_m c_m(G,o)x^m and P_(G,x)(gamma)=x^|gamma|/Z_G(x). If c_n(G,o)>0, then for every gamma in Gamma_n(G,o),

P_(G,x)(gamma | |gamma|=n) = [x^n/Z_G(x)]/[c_n(G,o)x^n/Z_G(x)] = 1/c_n(G,o).

Thus conditioning the *free-endpoint* finite grand-canonical law on length n gives the uniform n-step law exactly, independently of x. If G contains the radius-n graph ball around o, it contains every n-step SAW from o in the infinite lattice, so this conditional law is exactly Grimmett's finite-n lattice ensemble. This identity does not apply directly to w405's critical *chordal* law, which fixes endpoint b. Summing over endpoints and controlling domain exhaustion are additional steps.

Nor can one pass from a weak limit of unconditioned laws to conditional limits without controlling the conditioning event. As a bare probability counterexample, let P_n=(1-1/n)delta_0+(1/n)delta_1 and Q_n=(1-1/n)delta_0+(1/n)delta_2, and let E_n={value is nonzero}. Both P_n and Q_n converge weakly to delta_0, yet the conditional laws on E_n are delta_1 and delta_2. Fixed-length conditioning under a scaling grand-canonical law can be similarly rare; the exact finite identity therefore supplies no asymptotic transfer by itself. This general counterexample does not assert such behavior for SAW.

Verdicts and exact gaps are in REVIEW_PACKET.md and CLAIMS.jsonl. NEXT: seek a uniform length-and-endpoint local limit estimate that upgrades the finite conditioning identity to a fixed-n scaling statement; keep B and T separately named.
