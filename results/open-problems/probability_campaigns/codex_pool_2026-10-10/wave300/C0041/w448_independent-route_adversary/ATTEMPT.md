# C0041 independent approach (saved before reading w447's proof)

Recorded 2026-10-10. The exact target is nearest-neighbor RWRE on Z^d, d>=2, with a site-iid environment and a deterministic lower bound kappa>0 on all 2d transition probabilities. Under the annealed law P_0, assume X_n.l tends to +infinity almost surely; seek liminf X_n.l/n>0 almost surely. Current openness is UNKNOWN: a primary public manuscript now claims this result, but its proof and trusted axioms have not been audited here.

Prior C0041-A001 used directional zero-one laws and regeneration-time integrability. I instead use killed Green functions, annealed occupation flow, and the single-site return tilt. No claim of novelty for these standard identities. No paired-prover proof has been read at this checkpoint.

Let U be a finite connected subset of Z^d containing 0, T_U the first exit time, and G_U(0,x;omega)=E_{0,omega}[sum_{n<T_U}1_{X_n=x}]. Uniform ellipticity gives a finite quenched and annealed exit-time bound for each fixed U: from every point choose a path out of U of length at most |U|; each has probability at least kappa^{|U|}, so blocks of |U| steps bound the tail geometrically. This uses the Markov property in a fixed environment, not independence of attempts.

Write g_U(x)=E[G_U(0,x)] and
  hat_omega_U(x,e)=E[G_U(0,x) omega(x,e)]/g_U(x).
Then g_U(y)=1_{y=0}+sum_{x in U}g_U(x)hat_omega_U(x,y-x), using the occupation balance equation and Tonelli. The auxiliary killed chain has the same Green row and expected exit time. It is uniformly elliptic since each ratio is at least kappa. The sum of the occupation-weighted directional drifts equals E_0[X_{T_U}.l]; telescoping is justified by the finite mean exit time and bounded jumps.

For a specified site x, condition on all other sites. Let h=P_{0,omega}(H_x<T_U), taking h=1 if x=0, and let
  r_e=P_{x+e,omega}(T_U<H_x), with r_e=1 for x+e outside U.
Both h and r are independent of the outgoing vector omega(x,.) because their stopped paths never use a transition from x. First-step return decomposition gives
  G_U(0,x)=h/[sum_e omega(x,e)r_e].
Thus iid allows integration over omega(x,.), but DOES NOT make G_U(0,x) independent of it. The relevant drift is tilted by inverse escape probability. A fresh environment at first arrival is not a fresh environment at every visit.

An independent two-site obstruction is ready for exact checking. In d=2, sample each site independently with outgoing probabilities, ordered (+e1,-e1,+e2,-e2):
  A=(7/10,1/10,1/10,1/10), with probability 11/20;
  B=(1/10,7/10,1/10,1/10), with probability 9/20.
All probabilities are >=1/10 and E[d(0).e1]=3/50>0. Take U={0,-e1}. Given types at 0 and -e1, G_U(0,0)=1/(1-omega(0,-e1)omega(-e1,+e1)). Direct summation over the four iid type pairs predicts
  E[G_U(0,0)]=2021/1581;
  E[G_U(0,0)d(0).e1]=-202/2635;
  hat_d_U(0).e1=-606/10105<0.
This refutes factorizing occupation and outgoing probabilities, and refutes deducing uniform positive auxiliary drift from positive mean site drift plus UE+iid. It is NOT a counterexample to C0041: directional transience of this particular law is not asserted.

A sufficient condition isolating the route's hardest piece: if some delta>0 satisfies hat_d_U(x).l>=delta for every such finite U and x in U, then for finite U contained in {y:y.l<L}, E_0[T_U]<= (L+1)/delta. Exhausting the half-space by finite connected sets gives E_0[H_{X.l>=L}]<=(L+1)/delta by monotone convergence. This is a stronger condition; no deduction of it from directional transience is available here. A completed C0041 proof must derive quantitative occupation/escape control or another valid mechanism from the original hypotheses, not silently assume this bound.

Independent-review obligations for w449: check the return decomposition, all four rational terms and the exhaustion limit. Check any peer argument that replaces an occupation-weighted mean by the unweighted site mean. The optional fresh-site law must be conditioned on actual first hitting, not on future success or the total number of visits.

Evidence: C0041-A001 in the named intake attempts.jsonl; Drewitz-Ramirez arXiv:1005.0376v2 Conjecture 1.1; memory scars proof_steps_need_derived_joint_structure_2026_09_09 and perceptron_proof_open_gaps_fleet_2026_07_12. The top-three recall hits were read, with the hypothesis-localization hint used only as a hint.

NEXT: Check the two-site rational certificate, then read w447's saved route and audit its hardest quantitative step.
