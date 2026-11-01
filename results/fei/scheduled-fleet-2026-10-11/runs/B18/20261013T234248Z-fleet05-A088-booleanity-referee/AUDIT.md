# A067 bounded-fiber theorem: HOLDS at the exact Boolean scope

Reviewed claim: A067-BOUNDED-FIBER-TWO-EVENT-ACCESS-RESERVE v1, A067 run 20261013T222025Z. The canonical statement-and-hypotheses SHA256 is bff928c14877300aff73932ed9c66ba2a6c57b4ad6fc101b08283a88bccd8f25. No proof repair or statement change supplied. The new review is independent of A067's code. All entropy units below are bits.

## Independent reconstruction

Let core x have m bits, control z have r bits, and F=g(x)(1-2e(x,z)), with actual Boolean g and actual final indicator e. Write a_x=E_z e, rho=E_x a_x, A={x:a_x>0}, epsilon=P(A). Assume a_x<=k/2^r<=1/4. The mask means XOR for sequential flips and union for union-once editing; no separate-event reserve is reused.

Group the squared Walsh law by core label T, q_T=sum_U p_(T,U). Actual children have coefficients c_T(z). Walsh orthogonality gives q_T=E_z c_T(z)^2. Direct subtraction of the three entropies gives

    Q=H(p)-E_z H(p_z)=H(U|T)+sum_T Ent_z(c_T^2)=B+J.

This is an exact grouping identity, with all actual child entropies present. It also holds for any norm-one real seed multiplied by the same sign mask: every child remains norm one. On a single control edge, the row entropy of (a+bz)^2 is <=2b^2/ln2. For completeness, its normalized natural-log expression is q*g(2ab/q), where g(t)=((1+t)ln(1+t)+(1-t)ln(1-t))/2. Comparing derivatives proves atanh(t)<=t/sqrt(1-t^2), hence g(t)<=1-sqrt(1-t^2). Multiplication by q gives <=2min(a^2,b^2)<=2b^2. Entropy tensorization follows by the two-block entropy chain rule and convexity of Ent in its density (log-sum inequality). Sum over T and apply Parseval to the physical derivative to obtain J<=2I_Z/ln2. This fragment is real-valued; interpreting energy as pivotal influence requires Boolean output.

Because g^2=1, partial Parseval gives alpha=P(U nonempty)=E_x[4a_x(1-a_x)]<=4rho<=1. Conditional entropy of a control label is bounded by its flag entropy plus alpha*r. Since h2(alpha)<=alpha log2(e/alpha), and u log2(e/u) increases on [0,1],

    B<=4rho[r+log2(e/(4rho))].

Nonempty fibers contain at least one assignment, so rho>=epsilon/2^r. Therefore B<=8r*rho+4rho log2(1/epsilon), using log2(e)<2. Empty E is handled separately and has B=J=Q=0.

Applying entropy tensorization to a set indicator gives the elementary cube isoperimetric bound I(1-2*1_D)>=2P(D)log2(1/P(D)): each crossing one-bit pair contributes exactly half its pivotal probability to Ent(1_D). Apply this within each control fiber to obtain

    I_Z>=2E_x[a_x log2(1/a_x)]>=2rho(r-log2 k).

For the critical ownership step, inspect a core edge x,x'. The mask mismatch probability p is at most a_x+a_x'<=1/2. If g agrees at its endpoints, the final edge is pivotal with probability p. If g disagrees, it is pivotal with probability 1-p>=p. Averaging actual edges gives I_X(F)>=I_X(mask), once for the combined mask. No assumption about disjoint edit projections or independent events is used.

Every core slice E^z is contained in A. Its measure epsilon_z satisfies epsilon_z<=epsilon and E_z epsilon_z=rho. The same set isoperimetry gives

    I_X(F)>=E_z I(mask_z)>=2E_z[epsilon_z log2(1/epsilon_z)]
           >=2rho log2(1/epsilon).

Thus the rarity charge in B is <=2I_X, and its 8r*rho term is <=4r I_Z/(r-log2 k). Add J to obtain exactly Q<=K I_Z+2I_X. This proves all finite dimensions and every admissible integer k, including k=1 and k=2. The finite checker only uses these two values; general k is established by the argument, not inferred from enumeration.

Revealing every control gives E I(core leaf)=I_X and spent influence I_Z, in any adaptive order. The entropy telescope retains E H(F_z). The already reviewed Boolean granularity theorem gives H(leaf)<=2I+2U-(2-log2 e)Var<=(2+2b)I if U<=bI. Thus H(F)<=K I_Z+(4+2b)I_X<=max(K,4+2b)I(F). This is conditional leaf admission, not FEI for arbitrary cores.

For an early control-only tree, every singleton entropy drop equals nonnegative conditional spectral entropy plus nonnegative row channel entropy. Extending to all controls therefore gives Q_partial<=Q_full. The influence identities are I_Z(root)=I_spent+E I_Z(early leaf), I_X(root)=E I_X(early leaf). Combining the full access price with the U-certified early terminal price yields coefficients K on spent influence, K+2+2b on remaining control influence and 4+2b on core influence. Since K>=4, the latter is <=K+2+2b. The claimed early bound follows. Descendants need not satisfy the root fiber cap, and no nodewise use of the cap was made.

Verdict: HOLDS, no unsupported line within the exact claim. The universal extrapolation first fails at dimension-independent conditional reference payment for large fibers and/or admission of arbitrary retained core leaves.

## Strong normalized-real scope diagnostics

Use all norm-one real seeds g, with sign-mask multiplication, spectral Dirichlet influences, and actual norm-one restricted children. This preserves more structure than arbitrary spectra while removing Boolean output. The row grouping and channel estimates above still hold. The alpha identity instead reads E_x[g(x)^2*4a_x(1-a_x)]; its physical-density specialization and the final-edge pivot comparison require Booleanity.

The exact 625-case diagnostic fixes core values (1,-1/3,5/3,1/3), mean-square one, two controls, and all <=1-assignment fibers. Seventy-two cases violate reserve ownership. The first has fiber labels (0,1,empty,0), final core energy 13/18, mask core influence 3/4. No access-bound violation was certified in this grid. This separates a failed proof/payment statement from an unproved claim that the bare Q inequality fails for real seeds.

A compressed, dimension-explicit real ownership obstruction is psi(x)=(x_1+...+x_16)/4. Its norm and core energy are one. Edit only its zero middle Hamming layer and z=00 on two controls. F=psi is unchanged, all children remain norm one, and the cap k=1,r=2 holds. Mask core influence is (1/4)*2*16*binom(16,8)/2^16=6435/4096>1. Thus the ownership substatement of the quantified theorem is actually false on this normalized-real relaxation. The checker uses only a binomial count; no 16-bit table was allocated.

The terminal corollary also has an actual rational normalized-real counterexample, even with empty E. Take g=(1023+64x)/1025, so its Fourier squared masses are 1-p,p with p=4096/1050625<1/256. U=0, I=p, and H/I=h2(p)/p>log2(1/p)>8. With r=2,k=1,b=0, the claimed constant is max(K,4)=K<7, since ln2>842/1215>2/3. Thus the real extension of the terminal corollary fails despite norm-one children, U admission, and the sparse cap. This is not a Boolean FEI counterexample. The Boolean granularity payment has genuine content separate from reserve ownership.

Deleting the fiber cap already fails on Boolean inputs: the one-core/one-control diagonal mask has core mask influence one, while multiplying it by the core dictator leaves a pure control dictator with zero core influence. This refutes that extension of ownership, not the source theorem.

## Correction propagated since stage 2

The read-only A066 stage-3 CLAIMS.json explicitly states the paid budget only for singleton trees in A066-POSITIVE-RESTRICTION-HEAT-LEDGER v2. The read-only A067 REVIEW_AND_CORRECTIONS.md withdraws its old unqualified v1 all-block acceptance, substitutes v2, and retains the signed refinement transfer. This is actual local source-bound downstream use of A088's n128 objection. I do not independently accept or repair A066 v2 in this run; its improved constant and transfer require their own source reconstruction. A067's new access theorem is independent of A066, so no v1 dependency is hidden in this acceptance. Registry adoption, mirrors and supervisor copies remain unverified.
