# Tetrahedral critical payment and a physical tangent query

All cubes are uniform; phases take values in {+1,-1}; spectral entropy and erasure use log2. Let K=4+2/ln(2). The finite normal-form proof below closes the previous affine-span-three gap at twelve coherent edits. It is an author-checked proof with exact certificates and a separate spectral implementation; external independent review remains pending. Full FEI remains open.

## 1. Critical-node rigidity and exhaustive normal form

Let g=(-1)^q(1-2*1_E) on six physical controls, q quadratic over F2, |E|<=12. Fix physical i with nonzero polar row Q_i, and suppose Inf_i(g)=1/8, i.e. four pivotal undirected pairs. The quadratic starts with16 pivotal pairs. Let R count original pivotal pairs removed, A original nonpivotal pairs added, D pairs with both endpoints edited. Then R-A=12 and |E|=R+A+2D<=12. Subtraction forces R=12,A=D=0 and |E|=12. The four surviving child locations W lie in the derivative hyperplane P={partial_i q=1}. Both endpoints outside P are unedited. The planar W case and complete terminal payment are inherited from stage17; only affine span3 remains here.

If W has affine span3, its four points are affinely independent. Translate a W point to zero and make an invertible affine change ONLY in the five unqueried variables. Write them (r,u), r=(t1,t2,t3,v) in F2^4, with P={u=0}, W={0,e1,e2,e3} at u=0 and v=0. The derivative becomes1+u. Multiplying by an unqueried affine sign makes the child at selector i=0 equal+1 at all four W vertices. Such a character exists because W is affinely independent. The original quadratic remains quadratic. This transform and common characters permute selected Fourier row pairs, and so preserve only the selected B_i and Inf_i; no other physical influence is transported.

The resulting actual Boolean parent has the following complete description. On u=0 let its children be a(r) and a(r)-2*1_W(r), where a=1 on W and is arbitrary on the other12 vertices. On u=1 both children equal b(r), a quadratic sign on four variables. Multiplication by (-1)^u normalizes b(0)=+1 without changing a or W. Thus b runs over all2^(4+6)=1024 normalized quadratic signs; a runs over exactly4096 masks. This is an exact normal form, not a relaxation. Conversely every such parent is realized by12 edits to a quadratic with selected derivative1+u: write b=(-1)^(q0(r)+l(r)), q0 homogeneous quadratic, l linear, and take q=s*(1+u)+q0(r)+u*l(r). On W, q0=0. On each of the other12 u=0 pairs edit exactly one endpoint to obtain the requested a. The u=1 pairs stay untouched.

## 2. Explicit symmetry and orbit certificate

There are11 explicit generators in out/orbits.json. Four translations r->r+e_j acting ONLY at u=1 are the affine unqueried maps (r,u)->(r+u*e_j,u); a possible outside constant is removed by (-1)^u. Three affine tetrahedron permutations generate S4 on W: swap t1/t2, swap t2/t3, and swap0/e1 via t1->1+t1+t2+t3. Three shears t_j->t_j+v fix W pointwise. One common v-character multiplies both a and b and equals+1 on W. All generators are bijective, preserve the family, and preserve selected B and influence. Outside constants are always removed by a common unqueried u-character; selector characters are never used.

The exact BFS checks every one of1024 outside words under all11 generators and obtains14 orbits, with (representative truth mask, size):
(0,2),(60,12),(150,16),(780,192),(854,384),(3900,48),(3990,24),(4080,8),(5912,64),(6030,32),(6168,32),(6990,192),(15420,6),(15450,12).
Their sizes sum to1024. Parent pointers and generator data permit reconstruction of every normalization. For each orbit representative all4096 actual inside masks are retained. Because every generator maps the entire4096-element inside domain bijectively to itself,14*4096=57344 cases exhaust the selected-coordinate problem. No geometric symmetry is used to claim an unrelated physical query is paid.

## 3. Exact spectral payment

Let d_k=Walsh(1_W)(k)/2 on16 r frequencies, w_k=Walsh(a)(k)/2, z_k=Walsh(b)(k)/2. These are integers: Walsh(a),Walsh(b) are even and Walsh(1_W) is even. For each r frequency and u frequency epsilon in {+1,-1}, the absent and present selected-coordinate amplitudes, up to common signs, are

 (w_k-d_k+epsilon*z_k)/16, d_k/16.

The present squared integer mass is32, absent mass224, total256, so Inf_i=1/8. With Phi(t,u)=(t+u)log2(t+u)-t log2(t)-u log2(u),

 256 B_i = sum_(k,epsilon) Phi((w_k-d_k+epsilon*z_k)^2,d_k^2).

The exact test is product(t+u)^(t+u)<=2^128 product(t^t*u^u), omitting zero factors. Denominators are positive products of positive integers; zero entropy terms are handled as zero and need no division. tetra.py exhausts all57344 parents, caches540 exact squared-amplitude histograms, and has zero failures. Therefore B_i<=1/2=4 Inf_i for every critical span3 node.

independent.py separately reconstructs64-bit Boolean truth tables and computes every Walsh sum by XOR/popcount with a character mask, without a fast Walsh transform or projected amplitudes. It checks all57344 parents, Parseval, actual selected pivotality, and the inequality using integer prime-exponent products. Its global maximum ratio agrees by cross multiplication. It also checks all11264 actual-parent generator actions with nonconstant inside masks, rather than merely trusting the polynomial orbit action. These are two independent computational representations by the same author; no external acceptance is asserted.

## 4. Complete twelve-edit stopping consequence

Take arbitrary n, quadratic q, linear address M, independent physical sign data y_z, and any set E of at most12 vertices contained in one fiber of M. Then F(x,y)=(-1)^q(x)(1-2*1_E(x))*y_(Mx) has

 H(F)<=K*(I(F)-1).

Query address-active physical controls first; their influence1/2 is K4-good, exactly as in the inherited ledger. At phase nodes with D>=7 any nonzero polar coordinate has Inf>=1/2-24/2^D>=5/16 and is paid by B<=h2(Inf)<=4Inf. At D=6 the lower bound is1/8. Four pivotal pairs are now fully paid: four distinct child vertices have affine span2 or3, and the planar and tetrahedral certificates cover both cases. Five pivotal pairs use the inherited odd-lattice certificate; six or more use the >=3/16 binary-entropy bound. At D<=5 use the inherited maximum-influence physical policy. If the polar matrix vanishes, retain the entire character-times-mask terminal. Unedited quadratic terminals retain their full entropy as well.

Stage17 proves all affine mask terminals with s<=12,D>=6 are paid at the unchanged K. Its endpoint is2 ln(2)+log2(3)<3, from ln(2)<7/10 and3^5<2^8; s=0 is treated separately and all denominators are positive. Small-dimensional terminals use the generic five-control theorem. Restrictions keep q quadratic and do not increase the number of edits. Every query is an original physical query; the bad-node bill sum_(B_i>4Inf_i) weight_i*2I(D_i) is zero.

Writing A for weighted queried influence and T for weighted remaining phase influence, the exact physical ledger retains the ONE full shared-data influence: I(F)-1=A+T. The exact entropy split satisfies Delta_i<=B_i+(2/ln2)Inf_i<=K Inf_i. Therefore H(F)<=K A+K T=K(I(F)-1). No terminal entropy, data influence, label cost or oblique-coordinate influence has been discarded. This removes stage17's planar-critical-node condition; the extension is now unconditional through twelve coherent same-fiber edits. It does not treat arbitrary edit sets or full FEI.

## 5. Count-independent physical tangent payment

Here is a further local step with no bound at all on the number of edits in one half-cube. Let q be quadratic on n physical variables, Q its alternating polar matrix, g=(-1)^q(1-2*1_E), Q_i nonzero, and P={partial_i q=1}. Suppose physical j!=i satisfies Q_ij=0 and Q_j not in span_F2{Q_i}. Write e_out=|E intersect P^c|. Then

 Inf_j(g)>=1/4-2*e_out/2^n.

Indeed j is tangent to P, so its edges do not leave P^c. Since Q_j is independent of Q_i, the affine derivative partial_j q is balanced on P^c. Hence the unedited quadratic has exactly probability1/4 of j-pivotal vertices in that half. Every edited vertex in P^c can alter at most one undirected j-edge there, with probability cost2/2^n; editing inside P cannot affect these edges. The other-half influence is nonnegative. This proves the lower bound in ORIGINAL physical coordinates, with no affine normalization.

In particular e_out<=2^n/32 implies Inf_j(g)>=3/16. The exact inequality3^3*13^13>2^52 gives h2(3/16)<3/4 and monotonicity of h2(t)/t gives B_j<=4Inf_j. Thus

 H(g)<=K Inf_j(g)+(H(g|j=0)+H(g|j=1))/2,
 I(g)=Inf_j(g)+(I(g|j=0)+I(g|j=1))/2.

This is one paid physical query with BOTH full child entropies retained, regardless of how many edits lie inside P. Its charge is its actual queried influence; it does not spend the quadratic half-cube a second time. No invariant preserving this hypothesis in either child is yet proved, and no terminal class is assigned to the arbitrary children. If used with g*y, the one physical data influence is retained as before.

The structural hypotheses are necessary for this particular lower bound. For q=x1*(x0+x2), E=negative(q) lies inside P={x1=1} and the edited phase is constant. Choosing i0,j1 breaks tangency; choosing i0,j2 breaks independence (Q_j=Q_i); both have Inf_j=0. For q=x0*x1+x2*x3 on six bits, make the edited phase constant on P, then edit outside vertices8,9. The lower bound is attained at3/16. Adding outside vertex24 gives Inf_j=5/32, so the threshold e_out<=2^n/32 cannot be raised while asserting the same3/16 bound. Exact fixtures and4624 finite checks are saved in out/tangent_certificate.json.

## 6. Honest universal frontier

The twelve-edit theorem is a restricted all-dimensional result; external review is pending. The new tangent step is independent of the number of inside edits but only pays one original physical query. The first unpaid universal line is preservation or transfer of an eligible tangent-row certificate and its unspent influence after that query, with both actual child entropies retained. If no such physical tangent exists, an oblique parity direction is not a substitute; that case still needs an adaptive payment. The theorem does not make the unrestricted branches easy and does not establish full FEI.


## 7. A whole physical tangent block survives every history

The clean case e_out=0 has a useful history invariant. Let J be any set of ORIGINAL physical coordinates, disjoint from i, such that Q_ij=0 for j in J, Q_j not in span{Q_i} for each j in J, and Q_jk=0 for all j,k in J. Assume E is contained in P={partial_i q=1}. Query every coordinate of J in any fixed order, on every branch.

After restricting any prefix L subset J to any values, P is unchanged because Q_i has zero entries on L. Each remaining Q_j also has zero entries on L, so deleting those columns preserves its independence from Q_i exactly. The restricted quadratic is still quadratic; its linear terms may change but do not affect that independence. No edits enter P^c under restriction. Hence EVERY reached relevant j has Inf_j>=1/4, so B_j<=1<=4Inf_j. The hypothesis survives every history; there is no root-bank reset or probabilistic independence assumption.

With A_J=sum_(j in J) Inf_j(g), the complete fixed physical tree gives

 H(g)<=K A_J + average_a H(g|J=a),
 I(g)=A_J+average_a I(g|J=a).

The second identity and A_J expression follow by averaging each physical coordinate influence over restrictions of distinct earlier coordinates. Equivalently they follow from the standard node influence telescope. Both full child entropies are retained at every step. The block may have arbitrarily many coordinates and the number of edits inside P is unrestricted. This pays access to the retained leaves, not the leaves themselves. If J is empty the identities reduce to the original unpaid problem, so no universal selection has been smuggled in.

block.py checks every one of65536 inside-half edit masks for q=(x0+x2+x4)*x1+(x2+x4)*x3 on five physical bits with J={2,4}, including all three query histories per parent, sharp positive influences and the complete original influence telescope to all four actual leaves. The complete leaf truth tables are retained. A general all-dimensional leaf-entropy payment, or a way to extend a paid block when no eligible independent physical tangent remains, is still unproved. This is the next C019 obligation; proceeding to another fixed edit-count census would not resolve it.


The pairwise Q_jk=0 condition in the block theorem cannot simply be dropped. On five bits take q=x0*x1+x2*x3, P={x1=1}, and edit its negative vertices inside P so the phase is constant on P. Rows j2 and k3 are both originally eligible, but Q23=1. Query j2: its actual influence is1/4, yet the j2=0 child is constant and has Inf_k3=0. The saved actual Boolean fixture verifies both edge counts. It invalidates the hereditary eligibility claim without pairwise noninteraction; it does not refute a policy stopping on the constant branch.
