# B05 control-first complete-reference certificate

All logarithms are in bits. This is a scoped continuation/application of A097 v1, not another universal FEI reduction.

Fix even k>=2, delta=2^-k, e=2^(-k/2), r=2k, p=2^-r. Let b(x)=(-1)^(x1 x2+...+x_(k-1)x_k) in bit notation, b'=b-2*1_{x=0}, h(y,x) select b,b' fairly, and F=1+A_r(h-1). The chosen physical tree queries the controls in order, stops at the first mismatch, and otherwise reveals y and stops at b or b'. The k=2 member extends the actual Boolean construction; the reviewed B05 local no-go used k>=4.

Let N_+=(2^k+2^(k/2))/2, N_-=(2^k-2^(k/2))/2. Walsh coefficients of b are sigma e with these sign counts; the empty coefficient has sigma=+. The flip subtracts 2delta from every coefficient. Thus at a data index of sign sigma, the core selector coefficients and marginal are

    a_0=(sigma e-delta), a_1=delta,
    q_sigma=delta-2sigma delta e+2delta^2.

The core mean is mu=e-delta; c=1-mu belongs to [3/4,1). Let phi(a,b)=(a+b)h2(b/(a+b)), vanishing at zero atoms. Its selector erasure is

    B_sel=sum_sigma N_sigma phi((sigma e-delta)^2,delta^2).

Write H_b'=sum_sigma N_sigma[-t_sigma log2 t_sigma], t_sigma=(sigma e-2delta)^2, and J_sel=H(q)-[k+H_b']/2. This retains signs and actual child laws; no arbitrary non-Boolean spectrum is substituted.

## Prescribed leaf references

Mode E: each seed leaf gets its exact actual Fourier law. Constant leaves get delta_empty. Then the compatible reference is exact at every node; all kappa=0.

Mode U: both seed leaves get the uniform bent-spectrum reference, Q_b(T)=Q_b'(T)=delta. Its leaf cross-entropy is exactly k. At the selector the A097 lift gives

    Q_h(z,T)=delta P_h(z,T)/q_sigma,
    z_0=Q_h(empty)=delta mu^2/q_+,
    kappa_sel=J_sel.

This is a fixed normalized complete reference, including its empty atom. The terminal reference KL slack is p[k-H_b']/2. The exact reference mode has z_0=mu^2 instead.

## Control-node recurrence: B20 activation formula inserted

At the active suffix with s remaining controls, set u_s=2^-s and d_s=u_s c. Physical reach is pi_s=p/u_s. The B20 activation coefficient formula gives the residual-empty packet a=(1-d_s)^2, b=d_s^2, q_s=1-2d_s+2d_s^2. All other control packets have spectral membership probability 1/2 and total mass 1-q_s. Therefore

    B_s=phi((1-d_s)^2,d_s^2)+(1-q_s).

This is one queried-coordinate conditional entropy, not the entire aggregate C018 erasure of the suffix. In B20's activation formula its y-coordinate summand is u(1-mu^2)+(u-2u^2)c^2+phi; using 1-mu^2+c^2=2c gives exactly the displayed B_s.

Let z_(s-1) be the constructed active-child reference's empty mass. The inactive child's reference is delta_empty. The complete A097 reference lift yields

    z_s = ((1-d_s)^2/q_s)(1+z_(s-1))/2,
    w_s = (d_s^2/q_s)(1+z_(s-1))/2.

Here w_s is the reference atom for a removed control-frequency bit present and all residual frequencies absent. The actual residual-empty physical child posterior is

    k_P=(1,(1-2d_s)^2)/(2q_s),
    k_Q=(1,z_(s-1))/(1+z_(s-1)).

All nonempty residual packets have both posteriors concentrated on the active child; their kappa is zero. Hence

    kappa_s=q_s D_2(k_P||k_Q).

Zeros at the k=2 flipped leaf are harmless; true zero atoms never contribute logarithms, while the uniform reference still has full support.

The exact complete-tree numbers requested by the lead are thus

    B_T=p[B_sel+sum_(s=1)^r B_s/u_s],
    K_T=p[kappa_sel+sum_(s=1)^r kappa_s/u_s],
    R_T=(B_T-K_T)/I_removed,
    I_removed=p(rc+delta), I_terminal=p(k/2+k delta).

Influence counting is direct: each root control has influence pc; the selector has influence pdelta; the seed influences are I(b)=k/2, I(b')=k/2+2kdelta, because every neighbor of the flipped central point has value +1. The expected terminal average is p(k/2+kdelta). No terminal influence is spent in I_removed.

These finite rational/logarithmic expressions, not their decimal displays, specify the exact answer for each k.

## Independent closed root reference and KL

The root spectrum has vacuum probability (1-pc)^2, pure-control atom probability p^2 c^2, and nonempty core-index probability p^2 P_h(V), repeated over all 2^r control subsets. The compatible root reference has vacuum z_r; for a nonempty core index it has p^2 Q_h(V); for a nonempty pure-control subset whose deepest queried included index is j in {0,...,r-1}, it has 4^-j w_(r-j). Exactly 2^j such subsets have that deepest index. These are disjoint classes and sum to 1 under both prescribed normalized leaf-reference modes. They independently compute D_root and verify

    K_T=p[k-H_b']/2-D_root             (mode U).

In mode E both terms are zero. code/check_bent.py checks this identity by certified outward intervals and directly compares every root atom with a separate integer-Walsh/reference reconstruction at k=2,4. The algebraic proof of equality is the A097 v1 divergence telescope plus this exact rational root law, not an inference from overlapping intervals.

## All-even-k credit cap: exponentially negligible repair

For the uniform reference, the point-flipped bent law satisfies exactly

    chi^2(P_b'||uniform)=16delta(1-delta).

Proof: P_b'(T)-delta=delta(-4sigma e+4delta), and the average sigma under uniform indices is e. Squaring and summing gives 16delta-16delta^2. Applying ln t<=t-1 under P_b' gives D_2(P_b'||uniform)<=chi^2/ln2. The already-proved complete-reference conservation then gives

    0<=K_T<=p[k-H_b']/2
             <=8p delta(1-delta)/ln2,
    0<=K_T/I_removed<=8delta(1-delta)/[(rc+delta)ln2].

The posterior credit for these specified inexpensive uniform seed references is O(2^-k/k). One may manufacture larger reference slack by using worse references, but that increases the terminal cross-entropy bill; it is not a free repaired payment.

## All-even-k path payment and limit

For a+b<=1, phi(a,b)<=b log2(e_math/b), where e_math is Euler's number. Here d_s<=1/2 and q_s<=1, so

    B_s/u_s <= 2c + u_s c^2[log2(e_math)+2s-2log2 c].

Using sum_s u_s<=1, sum_s s u_s<=2, c in [3/4,1) and B_sel<=h2(delta)<=delta[k+log2(e_math)] gives

    B_T/p <= 2rc + C0 +delta[k+log2(e_math)],
    C0=log2(e_math)+4+2log2(4/3)<13/2.

The lower bound B_s>=2u_s c-2u_s^2 c^2 gives B_T/p>=2rc-2. Divide by rc+delta: B_T/I_removed tends to 2 as k grows through even integers. The credit cap proves (B_T-K_T)/I_removed also tends to 2.

For even k>=6, rc>=3k/2>=9 and delta(k+3/2)<=15/128, so

    B_T/I_removed <=2+(13/2+15/128)/9<3.

The certified k=2,4 intervals also lie below 3. Thus for every even k>=2 on this precise control-first tree B_T<=3 I_removed, and B_T-K_T<=3 I_removed. Each prescribed seed reference has cost <=2I(seed); constant leaves have zero cost. A097 v1 therefore supplies a complete root reference with

    CE(P_F,Q_F) <= (3+2/ln2) I_removed+2 I_terminal
                <= (3+2/ln2) I(F).

This is a scoped payment/application on an already known FEI family, not a new solution or new difficult class. It closes the lead's exact calibration and quantifies why leaf posterior credit has little leverage here.

## Exact remaining universal line

No uniform low-cost reference or equivalent small KL slack is proved for an arbitrary core seed. Replacing the bent leaves by arbitrary Boolean seeds leaves their entire terminal cost and all nonempty spectral conditional labels. The universal inequality sum pi(B-kappa)<=K I_removed plus uniformly paid terminal references remains open. Recomputing more values of this bounded-ratio family cannot settle it.
