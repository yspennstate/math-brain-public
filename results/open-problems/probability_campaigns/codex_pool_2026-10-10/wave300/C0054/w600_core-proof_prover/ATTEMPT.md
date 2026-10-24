# C0054: conditional site averaging and the block-contraction gap

Author w600, 2026-10-10. Mathematical review pending: w602. No parent-problem solution or novelty claim. The first statement-only packet is STATEMENT.md, sent to w601 before this packet.

## Exact target and scope

STATEMENT.md records the exact intake and primary ICM source. The full target combines bulk localization at fixed W, the exp(W^2) length prediction as W grows, and Poisson statistics. The proof attempt below concerns only finite-volume fractional moments for the real symmetric Gaussian subclass. Bulk energies are I_kappa=[-2+kappa,2-kappa]. The primary survey also assumes uniformly subgaussian scaled entries in Section 2.2. That assumption is satisfied here.

Fix an integer W>=1. On Z^2 connect distinct sites at l1 distance at most W. Every full-lattice vertex has M=2W(W+1) neighbors. For any finite induced subset Omega, take independent standard real Gaussian variables g_x and g_{xy} for unordered edges. Put H_xx=lambda*t*g_x and H_xy=t*g_{xy}=H_yx, with t>0, lambda>0. All these variables are mutually independent. Deletions preserve the same variables and scales: no renormalization of a minor. The normalized full-lattice choice is t=(M+lambda^2)^(-1/2). The target test model has lambda=1. We use z=E+i eta with eta>0 and G_Omega(z)=(H_Omega-z)^(-1).

## Prior-attempt digest and correction

The intake attempt C0054-A001 (attempts.jsonl, line 43, 2026-09-07) tried fractional moments and reported a growing W^2 decoupling loss, no bulk theorem. It also says: "Band matrices have no rank-one structure: the randomness at a site is a W^2-dimensional block". That wording is incorrect for the present model: conditioning on every entry except H_xx leaves an independent Gaussian coefficient multiplying |x><x|. The problem is not the absence of rank-one diagonal averaging. It is the lack of contraction after summing many hopping channels at lambda=1. L1-L3 below quantify this distinction exactly. The earlier spectral-edge partial claim has no proof in the cited record and is not promoted here.

Targeted C0054/two-dimensional-band searches found no additional exact-ID proof in attempts_H_20260912, attempts_I_20260914, or prob1000_lean_20260908; the Lean annotated ranking merely repeats attempted_un. Team O's board has no C0054 row in the targeted search. These are bounded checks, not certifications that the owner has never solved it.

The recent paper arXiv:2609.24426v2 (6 October 2026) states a growing-W delocalization threshold (log N)^7 and localization-length lower bound exp(W^(1/7)); v1 used 55. Those results constrain possible scale claims but do not settle fixed-W localization. Current openness remains UNKNOWN. The exact exp(W^2) prediction and Poisson conclusions require separate arguments.

## L1. Uniform Gaussian scalar averaging (proved derivation, unaudited)

For 0<s<1, a standard real Gaussian g, tau>0 and any complex a,

    E |tau*g-a|^(-s) <= tau^(-s) c_s,
    c_s = 2^(-s/2) Gamma((1-s)/2)/sqrt(pi).

Proof. An imaginary shift only increases the modulus, so it suffices to consider a real shift. For every r>0, the Gaussian mass of [a-r,a+r] is largest at a=0: for a>=0 its derivative is phi(a+r)-phi(a-r)<=0, using the even density decreasing with |u|. Layer-cake integration of the probabilities of these intervals proves that E|g-a|^(-s) is largest at zero. Substituting u=g^2/2 in the integral for E|g|^(-s) gives c_s. Integrability at zero uses s<1. Scaling gives the displayed bound. The supremum is attained at a=0 (or approached from eta>0).

## L2. Correct conditional one-site recursion (proved derivation, unaudited)

Let x!=y be in Omega, J=Omega\{x}, h=(H_xu)_{u in J}. The block inverse identity is

    G_Omega(x,y) = -G_Omega(x,x) sum_{u in J} H_xu G_J(u,y),
    G_Omega(x,x) = [H_xx-z-h G_J h^T]^(-1).

Let F_Omega(x,y)=E|G_Omega(x,y)|^s. Then

    F_Omega(x,y) <= sum_{u:0<|x-u|_1<=W} k_s F_J(u,y),
    k_s = lambda^(-s) c_s a_s,
    a_s = E|g|^s = 2^(s/2) Gamma((1+s)/2)/sqrt(pi),
    F_Omega(x,x) <= D_s = (lambda*t)^(-s)c_s.

Proof. Condition first on h and H_J. Only H_xx=lambda*t*g_x remains random. L1 bounds its resolvent factor uniformly in the now-fixed complex self-energy z+hG_Jh^T. Apply |sum b_u|^s<=sum|b_u|^s. After integrating g_x, each H_xu is independent of the entire minor H_J, so E[|H_xu|^s |G_J(u,y)|^s]=t^s a_s F_J(u,y). This proves the recursion. The diagonal bound follows from the same conditional scalar averaging. No independence between the original G_Omega(x,x) and H_xu is asserted. No overlapping row events are multiplied. For any finite induced subset, missing neighbors only remove nonnegative terms.

## L3. Exact one-site obstruction at the target normalization (proved derivation, unaudited)

Euler reflection gives

    c_s a_s = Gamma((1-s)/2)Gamma((1+s)/2)/pi
            = sec(pi*s/2).

Consequently the row-sum constant in L2 is

    q_s(W,lambda)= M lambda^(-s) sec(pi*s/2).

For lambda=1, q_s(W,1)>M>=4 for every 0<s<1; its infimum as s decreases to zero is M. Thus this particular nonnegative, uniform, one-site fractional-moment contraction never has q<1 in the flat Gaussian target model, including W=1. This proves a limitation of the displayed sufficient criterion; it is not a lower bound on the true localization length or evidence of delocalization.

The constant is also sharp for the corresponding worst-exterior one-site transfer bound at the bulk energy E=0. For a root with M neighbors set the deterministic exterior minor H_J=R I. The exact transfer coefficient to neighbor u is

    A_xu = H_xu / [H_xx-i eta - sum_v H_xv^2/(R-i eta)].

For fixed eta>0, sending R to infinity gives H_xu/(H_xx-i eta) almost surely. Fatou's lemma gives a lower bound for the supremum of its fractional moment by the limiting expectation. Then let eta decrease to zero and use monotone convergence. The resulting row sum is M lambda^(-s)c_s a_s. L1 gives the matching upper bound for every exterior, after conditioning on all h. Therefore no uniform one-site exterior-conditioning improvement can make this row sum less than one at lambda=1 merely by rephrasing independence. This worst-exterior statement is stronger than an obstruction for a typical random exterior; it does not preclude an averaged block or resampling method.

## L4. A complete strong-diagonal-disorder special case

If q=q_s(W,lambda)<1, then for every finite induced subset Omega, all x,y in Omega, all real E and eta>0,

    F_Omega(x,y) <= D_s q^(ceil(|x-y|_1/W)).

Proof by induction on |Omega|. For x=y use L2. For x!=y apply the off-diagonal recursion to J, whose cardinality is smaller. Every contributing u obeys |u-y|_1>=|x-y|_1-W, so ceil(|u-y|_1/W)>=ceil(|x-y|_1/W)-1. Because q<1, the induction bound for each minor term is at most D_s q^(ceil(|x-y|_1/W)-1). The sum of its coefficients is at most q, proving the result. The one-vertex case follows from the diagonal bound. This argument uses successive smaller minors, not independent block events.

At s=1/2, q=M sqrt(2)/sqrt(lambda). Taking lambda=8M^2 gives q=1/2 exactly, hence exponential decay with mu=(log 2)/W. This is a finite-volume resolvent theorem for deliberately strengthened diagonal disorder, not the target lambda=1. A common scalar normalization t=(M+lambda^2)^(-1/2) keeps row variance one without changing q. The diagonal/off-diagonal variance ratio is then lambda^2, rather than the target value one. No infinite-volume construction, eigenvector, Poisson, or optimal-scale conclusion is included in L4.

## L5. Precise conditional reduction from a block escape estimate

Here is a stronger, explicit sufficient route whose input is unproved. It is stated to expose dependence, not to call the input a lemma already proved.

Fix L>=0, s in (0,1), A<infinity and q in (0,1). For every finite induced Omega and x in Omega, let B=Omega intersect {u:|u-x|_1<=L}, J=Omega\B and T=H_BJ. For every fixed exterior H_J and z in I_kappa+i(0,infinity), put

    R_B = [H_B-z - T(H_J-z)^(-1)T^T]^(-1),
    K_xv(H_J,z) = E_{H_B,T} |(R_B T)_xv|^s.

All random entries internal to B and crossing B--J are averaged; the exterior is held fixed. Assume there are deterministic nonnegative bounds k_{Omega,x,v}(z), independent of H_J, with K_xv<=k_{Omega,x,v}(z) for every exterior, and sum_v k_{Omega,x,v}(z)<=q uniformly in Omega,x,z. Only J vertices adjacent to B can contribute; they satisfy L<|v-x|_1<=L+W. Also assume the terminal averaged bound F_Omega(x,y)<=A whenever |x-y|_1<=L, uniformly in volume and z. For L=0 this terminal bound is already L2; for L>0 it is an explicit additional local assumption in this criterion, not proved in this packet.

Then

    F_Omega(x,y) <= A q^n,
    n=max(0,ceil((|x-y|_1-L)/(L+W))),

and therefore F_Omega(x,y)<=A exp(mu*L) exp(-mu*|x-y|_1), mu=-log(q)/(L+W).

Proof. For y in J, exact block inversion gives G_Omega(x,y)=-sum_v (R_B T)_xv G_J(v,y). Condition on H_J; G_J is fixed in this conditional average. Subadditivity gives a sum of K_xv(H_J,z)|G_J(v,y)|^s. The deterministic bounds k permit integration over H_J without multiplying dependent expectations. This yields F_Omega(x,y)<=sum_v k_{Omega,x,v}(z)F_J(v,y). Induct on |Omega| using the terminal bound for distances <=L. Otherwise, each exterior contributing v moves by at most L+W, so its distance exponent is at least n-1. Multiplying the induction bound by the row-sum bound q proves A q^n. The same triangle inequality works on a torus with its periodic metric when ball neighborhoods are unambiguously defined. This reduction proves only the implication under the stated assumptions.

## The single hardest remaining gap

GAP-BLOCK: at lambda=1, produce a genuine finite-scale escape estimate with row sum below one, uniformly in eta down to zero, bulk E, growing volumes, and the minors used by iteration. The strong conditional criterion in L5 is one sufficient formulation, possibly stronger than necessary; an appropriate joint/resampled finite-volume criterion could replace it. The local terminal bound for L>0 must also be supplied for that chosen formulation. No such estimate is proved here. L3 shows why the one-site version cannot supply it. Proving a large-W block bound from the high-eta resolvent norm would not suffice: that norm diverges as eta decreases to zero. No exp(W^2) upper bound, matching asymptotic, or Poisson limit follows from the results saved here.

Concrete next proof step: for B a deterministic l1 ball, derive a two-boundary resampling inequality for E|(R_B T)_xv|^s that handles the shared exterior self-energy; test its row sum at E=0 and eta decreasing to zero without replacing a joint expectation by the product of its marginals.

## Verification scope

The proofs above are written derivations awaiting independent mathematical review. The scalar measurements in verification/ may check constants and falsify arithmetic errors; they cannot verify GAP-BLOCK. No Lean theorem, trusted-axiom receipt, formal proof, or actual served-model identity is claimed. Requested gpt-6.1-sol/max/Fast settings are not response-side served evidence.
