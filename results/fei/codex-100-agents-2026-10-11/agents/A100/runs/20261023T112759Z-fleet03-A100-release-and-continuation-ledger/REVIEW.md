# A100 independent reconstruction of singleton-ghost payment

## 1. Exact source and scope

Target A079-ZERO-SINGLETON-GHOST-CREDIT-SHARP@1, statement hash5b3fe67fddaba9db74a1c46f59f317651b5344c9fec89e56a7c6e8f510c7d059, A079 stage9 PROOF sections1-5. All costs are bits. Actual complementary controller rows a in{-1,0,1}, b=1-a^2 live on a finite physical cube independent of Boolean h. G=a+sigma b h, sigma=+/-1. A=ahat,B=bhat,beta=sum B^2=E b. Let p=hhat^2,m=Eh,r=m^2,t=1-r. CURRENT normalized R is supplied, R(empty)=r, CE(p,R)<infinity. Q(U,empty)=(A_U+sigma m B_U)^2; Q(U,T)=B_U^2 R(T) for T nonempty. Q normalizes since sum A^2=1-beta and sum AB=E ab=0. The initial influence price, earlier tags/bookings and coherent incoming form are hypotheses, not conclusions. No author code is imported. This review supplies no repair.

## 2. Reconstruct complete wrapper CE and physical query

Put v_U=(A_U+sigma m B_U)^2 and H_sub(w)=-sum w log2 w, even for subprobability w. Directly expanding all occupied labels gives

 CE(P_G,Q)=H_sub(v)+t H_sub(B^2)+beta CE(p,R)+beta r log2 r.

At a queried seed coordinate i with hhat({i})=0, both physical child means are m, so every term except beta CE_seed is IDENTICAL at parent and children. The convention0 log0=0 handles r=0. All controller-vacuum atoms remain; no signed term is discarded.

The empty seed-frequency pair at each U has true masses(v_U,0), hence zero conditional erasure. Every nonempty pair has masses B_U^2(p_0,p_1). Homogeneity of conditional entropy therefore proves B_i(G)=beta B_i(h). Independently, literal child Fourier amplitudes are u_T+/-v_T, so their mean squared law is M_i p. This uses uniform physical restrictions, not a probabilistic independence of spectral labels.

## 3. Exact ghost identity

Let rho=R({i}), theta=rho/t when t>0. If rho=t, R has no mass on any actually occupied nonempty atom: the singleton is truly zero. Finite CE excludes this, so theta<1. The calibrated inherited source has vacuum r and tail Rcal(T)=t (M_i R)(T)/(t-rho). It is normalized, finite on actual occupied atoms and retains every reference-only atom.

For remaining nonempty frequency T, set w=p_0+p_1,q=q_0+q_1. Expanding the difference of parent source CE and mean child source CE yields

 sum_b p_b log2(q/q_b) + w log2(t/(t-rho)).

The first term is that fiber's conditional entropy plus its conditional KL. Summing gives

 CE_parent_seed-mean CE_cal_child_seed
   =B_i(h)+D_*+t log2(1/(1-theta)),
 D_*=sum_{T nonempty,w>0} w KL((p_0,p_1)/w || (q_0,q_1)/q)>=0.

The seed-vacuum CE cancels because both actual means and the calibrated vacuum equal r. Multiplying by beta and adding physical erasure proves the EXACT full-reference identity

 B_i(G)+mean CE(P_child,Qcal_child)-CE(P_G,Q)
   =-beta D_*-beta t log2(1/(1-theta)).

Finite CE ensures every positive p_b has positive q_b. If q_b=0=p_b its contribution is0. If t=0 the seed and both children are constant, R is the vacuum point law, no tail division occurs and the increment is0. If beta=0, G is independent of h and the full seed transaction has charge0. These are the original endpoint rules.

## 4. Actual profile change, both outcomes and histories

In each physical child separately choose ANY normalized nonempty S_tau and lambda_tau<=theta. Set tail_new=(1-lambda_tau)tail_cal+lambda_tau S_tau. Since lambda_tau<1, all true occupied labels stay covered, new reference-only labels are permitted, and vacuum mass stays r. Pointwise tail_new>=(1-lambda_tau)tail_cal implies the extra full wrapper CE is at most beta t log2(1/(1-lambda_tau)). Thus BOTH full child costs satisfy

 transaction <=-beta D_*-beta t[log2(1/(1-theta))
                         -mean log2(1/(1-lambda_tau))]<=0.

At lambda=theta/2 the unused local release is at least beta D_*+beta t log2((1-theta/2)/(1-theta)). The threshold is sufficient in general; D_*>0 may pay more. Worst-case necessity is supplied only by the sharp witness below.

For an eligible finite adaptive tree, multiply each local inequality by its actual physical reach and sum. Internal complete CEs cancel exactly once; every old debit and both siblings/final complete terminals remain. Further coherent controller transactions must already be admitted by their stated current-source rule. At each later seed step read rho from the NEW current reference. No earlier ghost amount or original source bank is reissued. This is a finite telescoping argument, not an unjustified product of conditional probability bounds. A supplied original influence rate is preserved, not created.

## 5. Boolean sharpness and exact prepayment

Use A079's literal16-entry controller a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1), with beta3/8, and parity3 seed. Query its first bit: both children are signed parity2, nonconstant and isospectral. The singleton coefficient and every phase product u_T v_T are zero. Incoming R=(1-rho)delta_123+rho delta_1 is calibrated at vacuum0 and finite for0<=rho<1. Here D_*=0, and calibrated tail is delta_23. Mix toward delta_2 with weight lambda. Exact full erasure-plus-mean-terminal increment is

 (3/8)log2((1-rho)/(1-lambda)).

Thus lambda=rho gives equality; lambda>rho is positively charged, proving the WORST-CASE threshold sharp. The same lambda1/64 is negative at rho1/32, positive at rho1/128 and rho0. Both actual child references and all signed controller-vacuum atoms are included. This is no FEI counterfamily.

Finally start from any calibrated Rbase with zero queried-singleton mass. Inject theta t at that truly zero singleton by scaling all other nonempty reference mass by1-theta. Every occupied nonempty true mass is then multiplied by1-theta, so injection costs EXACTLY beta t log2(1/(1-theta)), the same ghost credit later released. Ghost manufacturing is advance payment. It cannot solve the initial-source-price problem or create free local capacity.

## 6. Independent exact implementation and adversarial axes

Own code/check_ghost.py uses direct character sums to cross-check integer Walsh transforms, literal physical wrappers and children, Fraction references and symbolic log forms. For any positive rational q, factor numerator/denominator into integer primes; represent log2 q as the exact finite linear form in log2 primes. Full CE/erasure/KL identities are tested by cancellation of every rational prime coefficient. Thus no floating sign, interval tolerance, author checker or borrowed Fourier/transport helper is used. Mixture payment uses exact pointwise inequalities, accompanied by the analytic log-sum proof above. Unsupported lambda values are admitted only in the sharpness test, where positive charge must be observed algebraically.

The frozen main domain has1512 labelled controller/seed/query/sign/reference transactions: every two-bit Boolean table, four explicit three-bit fixtures, all9 one-bit ternary controllers, two fixed two-bit controllers and the original A079 controller; every eligible zero-singleton query; actual source,1/8 singleton injection and1/4 uniform-tail floor. Fixed sharpness cross-grid has16 cases. Main passed90330 assertions in7.15856s, with6048 mixture instances and1056 changed seed-reference profiles (including beta0 endpoint cases, so this is not a count of changed nonzero wrapper tails);504 constant-seed and336 beta0 transactions. Pilot54 transactions/4639 assertions in0.376612s is a subset, not added twice. Pre-freeze pilot output is preserved separately and excluded: an automatic acknowledgment gate blocked the first spec write while the already queued pilot ran. The accepted rerun and main were executed only after spec/helper hash were saved. See PROTOCOL_NOTES.md. This procedural deviation is not hidden and does not alter the mathematical statement.

## 7. Verdict and exact unpaid line

HOLDS at the ENTIRE unchanged original A079 singleton-ghost theorem scope, including arbitrary finite controller/seed, both signs, arbitrary finite calibrated references, separate arbitrary child targets, endpoints, sharpness, injection prepayment and eligible finite histories. No substantive repair, no universal constant improvement, no formal compiler run, no independent acceptance of an entire FEI candidate manuscript.

The residual nullspace is a zero-singleton, isospectral, zero-current-singleton-ghost, zero-occupancy-KL transaction where a profile change is REQUIRED by a proposed global construction. It has no refund. Pay that necessary conversion from an ACTUAL unused original source/influence surplus with all old debits and BOTH full terminals, or prove an admissible policy avoids it. Arbitrary initial source/reference pricing remains influence-unpaid. These are the first universal unsupported lines, rather than another ghost-injection or canonical-return lemma.
