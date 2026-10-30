SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-23T13:05:13Z.
attacking: non-Lindeberg diffuse rare-fragment banks; derive the exact compound-Poisson+Gaussian limit for a dense rotated {1,1,-1} frame and rule out finite-stage density spikes using the partner/Fresnel envelope.

# Early substantive checkpoint

Full QFORM remains OPEN. This run attacks an unpaid witness class singled out by the completed fleet02/B17 diffuse-Lindeberg theorem: fully diffuse exact-rank-three frames whose input triangular arrays FAIL Lindeberg because cap-one laws carry finite-intensity remote fragments at distance sqrt(m).

Fix finite atomic measures nu_j=sum_l c_{j,l} delta_{a_{j,l}} with c_{j,l}>0 and nonzero distinct a_{j,l}; write C_j=sum_l c_{j,l}. For m>C_j define the cap-one probability density

f_{j,m}(x)=1_{[-L_{j,m}/2,L_{j,m}/2]}(x)+sum_l 1_{[a_{j,l} sqrt(m)-c_{j,l}/(2m), a_{j,l} sqrt(m)+c_{j,l}/(2m)]}(x),
L_{j,m}=1-C_j/m,

for m large enough that the intervals are disjoint. Its total support length is exactly one, hence integral f=1 and 0<=f<=1.

For S_{j,m}=m^{-1/2} sum_{k=1}^m X_{j,k}^{(m)}, the one-summand characteristic function at scale 1/sqrt(m) is

psi_{j,m}(t)=L_{j,m} sinc(L_{j,m}t/(2sqrt(m)))
 + sum_l (c_{j,l}/m) e^{i a_{j,l} t} sinc(c_{j,l}t/(2m sqrt(m))).

Therefore, for fixed t,

psi_{j,m}(t)=1+(1/m)[-t^2/24+sum_l c_{j,l}(e^{i a_{j,l}t}-1)]+O_t(m^{-2}),

so

S_{j,m} => G_j+P_j,
G_j~N(0,1/12),
P_j compound-Poisson with Levy measure nu_j,

independently across j.

This triangular array is genuinely non-Lindeberg whenever some atom a has positive weight c: for every 0<eps<|a|/2,

sum_{k=1}^m E[(X_{j,k}^{(m)}/sqrt(m))^2 1{|X_{j,k}^{(m)}|/sqrt(m)>eps}] -> sum_{|a_{j,l}|>eps} c_{j,l} a_{j,l}^2 >0.

Use the fixed orthogonal matrix

O=(1/7)[[6,-2,-3],[-2,3,-6],[-3,-6,-2]], J=diag(1,1,-1),
B=O^T J O=(1/49)[[31,-36,-12],[-36,-23,-24],[-12,-24,41]].

For each m, repeat the physical row O e_j/sqrt(m), k=1,...,m. Then R_m^T R_m=I_3 and A_m=R_m J R_m^T has exact nonzero spectrum {1,1,-1}. Every physical entry of A_m is nonzero because every entry of B is nonzero. Moreover

Q_m=X^T A_m X=S_m^T B S_m => Q_infty=(G+P)^T B(G+P).

Conditional on P=p, G+p is Gaussian N(p,I/12). The completed arbitrary-mean Gaussian theorem of fleet03/B17 gives

||p_{(G+p)^T B(G+p)}||_inf <= 3sqrt(2),

with strict inequality in the exact rank-three isotropic signature whenever p!=0. Therefore the compound-Poisson mixture has

||p_{Q_infty}||_inf <=3sqrt(2),

and if at least one nu_j is nonzero, in fact ||p_{Q_infty}||_inf<3sqrt(2).

The designated fleet02/B17 completed report supplies, via the proved Fresnel--Brascamp--Lieb Theorem F, the actual finite-frame bound for every m>=2:

|phi_{Q_m}(t)| <= min{1,(4pi)^(3/2)|t|^(-3/2)}.

Applying this inequality to the present A_m gives a common L1 envelope. Since Q_m=>Q_infty, dominated convergence yields ||phi_{Q_m}-phi_{Q_infty}||_1->0 and hence

||p_{Q_m}-p_{Q_infty}||_inf ->0.

Thus this canonical finite-intensity non-Lindeberg escape cannot beat 3sqrt(2), even at an off-zero finite-stage mode.

Near-sharpness inside the non-Lindeberg class is immediate. If C=sum_j C_j, the no-jump event has probability e^{-C}; at output zero its conditional Gaussian density is exactly 3sqrt(2). Hence

e^{-C} 3sqrt(2) <= ||p_{Q_infty}||_inf <3sqrt(2)

for every nontrivial fixed fragment cloud. Taking C>0 arbitrarily small gives genuinely non-Lindeberg source-valid rotated witnesses arbitrarily close to the sharp known obstruction.

Remaining work this run: formalize the strict-mixture argument, save an exact checker for O/B and the characteristic-function expansion, re-read corrections/control, and publish the complete source-pinned handoff.
