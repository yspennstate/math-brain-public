# Root audit: arbitrary-backbone matching CNA and all-port adjacent NC

3 October 2026 UTC. PASS within the two stated configurations. I read the
complete new matching proof, the complete hypothetical-triangle lemma,
both independent lemma audits, the complete ant matching audit, the full
all-port adjacent proof, and the complete K adjacent audit. I inspected
the actual author and independent implementations and reran their exact
checks. These are restricted derived results; historical novelty and
external specialist review remain unverified.

## Arbitrary backbone, three ports, whole marked matching

The split baseline is an actual graph, retaining all endpoint stars. Its
ordinary unrooted-forest parameters F,M,J therefore satisfy the credited
matroid log-concavity theorem. Adding the hypothetical triangle gives
exactly Z=F+A·z+r(z12z13+z12z23+z13z23), with no cubic term. The three
direction logarithmic Hessian gives AAᵀ-rF(11ᵀ-I) positive semidefinite.
Testing on (b1b2,b1b3,b2b3) yields M²>=2BJF, with J=r b1b2b3. Every
normalization is from the actual split graph, so there is no extra D
factor outside F,M,J. The scalar one-apex derivative alone would give
only the insufficient factor 3/2; the full Hessian is essential here.

The homogeneous refinement is also correct. For the degree-N coefficient-
one independent-set polynomial g, S=-Hess(log g) is positive semidefinite.
Differentiated Euler gives Sa=grad(log g), aᵀSa=N. Semidefinite Cauchy-
Schwarz gives xᵀ[AAᵀ-rF(11ᵀ-I)]x>=(Aᵀx)²/N at the boundary point.
Thus M²-2BJF>=M²/N, strict when M>0. Boundary continuity is legitimate
because g=F>0; no assumed strict log-concavity is used.

I rederived the terminal exponential: T(x)=dI+x²P+x³Q,
P²=2BQ and all higher products vanish, with d=1+Bx,
alpha=x²/d, gamma=x³/d². The exact marked contraction ratio is
c_i exp(delta_i P+epsilon_i Q). Expanding the entire matching, including
the within-coordinate P² contribution, gives the stated independent
Bernoulli OR size-at-most-two forced subset law. Its singleton weights
are h_i t_i, with h_i=M+J epsilon_i/delta_i+BJ delta_i, and its pair
coefficient is K=2BJ. The explicit configuration calculation confirms
the law, not merely equality of total partition sums.

For positive endpoint rows, delta in (0,1/B²) and epsilon/delta in (0,2/B)
follow from exact superadditivity. Elementary BM>=9J then gives
M<=h_i<=4M/3. Along with M²>=KF this proves both gates of the complete
forced-subset NA lemma. I checked its hit-event expansion and the reduction
of arbitrary increasing events to singleton triggers on support size two.
Upper-level events cover real increasing functions. Independent Bernoulli
averaging preserves that NA through the OR map.

Zero rows give independent bridge indicators; B=0 and M=J=0 give product
laws. Required backbone edges are contracted and absent edges deleted;
identified ports give r=J=0 without invalid divisions. Conditioned matching
endpoints may be absorbed into the arbitrary backbone, preserving the
family for the remaining matching. The theorem's backbone/marked fields
and simultaneous conditioning scope is valid. Arbitrary individual spoke
fields and spoke conditioning are not covered. The matching vector alone
is CNA; no all-indicator or strong-Rayleigh assertion is inferred.

Root reruns exited zero: the Hessian implementation checked 33,864 simple
backbones and 106 weighted/conditioned multigraphs; the author matching
implementation checked 980 backbone conditions, 33,588 matching laws and
401,588 ordered increasing-event inequalities; the independent ant route
checked 954 backbone conditions, 14,310 laws and 7,314 unordered event
inequalities. The two literal uncontracted K4 examples agree with their
whole marked configuration laws. These finite checks supplement the proof.

## Arbitrarily many ports, adjacent proportional attachment

For each actual backbone forest, contraction of its components aggregates
each profile sum x_C and rejects multiple spokes to the same new vertex.
This exact weighted bijection reverses the roles: the three new vertices
become the core, regardless of how many common neighbors there were.
The averaged transfer is D exp(UP+Gamma Q), where Gamma contains the full
s Var(U_A) term, s=a+b+c. Omitting that variance would be invalid.

The apex sum D(s)=sum_A w_A product_C(1+s x_C) is the actual ordinary
forest partition. The correct coefficient-one matroid theorem makes it
log-concave. Differentiation gives exactly U/s-Gamma=-(log D)''/s>=0.
I checked that total profile A0 is constant across forests, which is what
allows Var(U_A)=Var(W_A)/s². The s=0 case is separated before division.

Direct core deletion/contraction gives the four marked coefficients:
A/D=1+rho+[ab+ac+bc+rho b(a+c)]U+abc Gamma+sabc U²,
E/D=1+rho+c(a+b)U, F/D=1+rho+a(b+c)U, C/D=1.
The outer edge is forbidden when both marks are present. Expansion yields
R/D²=rho(1+rho)+ac[(1+2rho)U+acU²-b Gamma]. Both the rho² and 2rho terms
are required. Substitution of Gamma<=U/s gives the positive lower bound
in the proof, with covariance -w_e w_f R/Z². Strictness and all zero
boundaries are exactly as claimed.

Backbone contractions sum profile weights and preserve proportionality;
deletions and activities preserve the same arbitrary-backbone class.
Conditioning the outer edge present makes the two marks parallel, so
simultaneous presence is impossible. There is no conclusion for unrelated
marked positions, nonproportional spokes, or all forest edge indicators.

Root reran the complete author checker: all 2,440 backbone conditions
passed, including literal four-port cyclic graphs and exact apex derivatives.
Root reran the independent K whole-vertex DP: all 11 additional cases
passed, including six positive profiles, rho below one, rational fields,
zero backbone activities, contraction and all degenerate columns. The
independent DP retains all original vertices and does not call the author
terminal transfer or contract components to compute marked coefficients.

## Failed rows and primary-source boundary

I inspected and reran the exact four/five-port abstract-row obstruction.
The four-port negative cross coefficient obstructs coefficientwise
positivity. The five-port negative Rayleigh row has positive log-apex
second derivative and is therefore unrealizable by an actual forest graph.
It is not a forest counterexample. Likewise the formal three-port row
(1,0,0,0,1) violates the Hessian scalar bound by -3; dropping actual-graph
realizability is an invalid proof step.

I reopened the full primary ALOV1811.01600 PDF and checked Theorem4.1's
coefficient-one polynomial and Lemma2.2's affine specialization. This
classical matroid theorem is a credited input, not a new achievement.
I also checked Huang2311.00965's adjacent sufficiently-large-fugacity
statement and the current2610.00549 Proposition5.7. The latter concerns
random-cluster weights at fixed 0<q<1; its outer-edge lower bound cannot
be transported directly to ordinary forests, whose arboreal limit scales
z_e=q beta_e. These source scopes do not certify priority of the present
attachment results. General forest pair-correlation and NA remain open
in this work; the new all-port disjoint-pair route is still a candidate.
