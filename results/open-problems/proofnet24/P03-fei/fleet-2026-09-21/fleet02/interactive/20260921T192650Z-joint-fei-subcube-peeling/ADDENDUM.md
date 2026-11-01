# Further derivation: arbitrary derivative signs and an approximate-support block step

Continuation after the first proof package was pushed. Full FEI remains OPEN / NOT PROVED. The results below strengthen the preceding report and complete a quantitative near-support implication. They do not establish that every Boolean function has the required local structure.

The first report's 4+8epsilon constant-sign theorem remains valid. This addendum proves a stronger 4+4epsilon step with ARBITRARY signs on an exact subcube support, provided the genuine active-branch entropy is retained, and a coefficient-12 block step for a maximum-influence row sufficiently close to a subcube in support. The stronger proofs can be given with classical entropy tensorization, without using the Holevo theorem from the first proof.

## A. Arbitrary signs are allowed when their actual child is retained

Replace the first report's constant-sign derivative condition by the weaker exact-support hypothesis

    |D_x f(z,w)|=1{z=a},                               (A.1)

where z consists of r>=1 physical coordinate bits, q=2^-r and q0=1-q. There is now an arbitrary Boolean payload g(w) such that

    f(x,a,w)=(-1)^x g(w),
    f(x,z,w)=h_z(w) for z!=a.                           (A.2)

The active payload g and every h_z are genuine proper physical restrictions up to an irrelevant global sign. They can share all residual variables.

Exactly as before,

    B=sum_k[I_zk(f)-q]>=0,
    I(f)=q(r+1)+B+q I(g)+q0 E_z I(h_z).                (A.3)

The x-containing Fourier sector has mass q and conditional entropy r+H(g), rather than just r. The x-absent sector is unchanged. Hence every entropy inequality in Sections 3-4 of REPORT.md extends by adding q H(g) to its right side. At B=0 this gives the exact identity

    H(f)=q H(g)+q0 H(h)+K_r,
    K_r=phi(q0^2)+2qr(2-q)<4q(r+1).                   (A.4)

Consequently a centered H/J-critical core of ratio >4 cannot have a maximum-influence pivot whose SENSITIVITY SUPPORT is an exact coordinate subcube, even if its oriented derivative changes sign arbitrarily inside that support.

The payload term cannot be dropped. With r=1, h=1 and a six-bit bent g of entropy six, direct Fourier calculation gives H(f)=2+(1/2)*6=5, while the unamended no-payload constant-four right side would be four. This is a small Boolean counterexample to that incorrect extension, not to FEI. The correct payload has entropy contribution three.

## B. A punctured-cube log-Sobolev estimate improves the positive-surplus coefficient

For a nonnegative random variable Y, write Ent(Y)=E[Y ln Y]-(EY)ln(EY). First, for two real numbers u,v,

    Ent_{uniform two points}(u^2,v^2)<=(u-v)^2/2.        (B.1)

A direct proof is available from the scalar inequality

    d(t):=[(1+t)ln(1+t)+(1-t)ln(1-t)]/2
         <=1-sqrt(1-t^2), 0<=t<=1.

Both sides vanish at zero. Their derivatives are atanh(t) and t/sqrt(1-t^2); the latter dominates because the derivative of their difference is (1-t^2)^(-3/2)-(1-t^2)^(-1)>=0. Normalize by (u^2+v^2)/2, and use (|u|-|v|)^2<=(u-v)^2. This proves (B.1), including zeros by continuity.

Classical entropy tensorization on the product cube then gives, for any real u on Q_r,

    Ent_{Q_r}(u^2) <= (1/N)sum_unordered_edges (u(z)-u(z'))^2,
    N=2^r.                                            (B.2)

Indeed tensorization bounds the left side by the sum of conditional two-point entropies; applying (B.1) counts each unordered edge with factor 1/N. Tensorization itself follows from the entropy chain rule and convexity of the conditional entropy functional. This is the usual elementary cube log-Sobolev inequality, not a new claim of that methodology.

### Lemma B.1 — remove one vertex with a bounded extension cost

For r>=2 and real u on Q_r minus {a},

    Ent_punctured(u^2)
       <= [(1+2/r)/(N-1)] sum_internal_edges (u(z)-u(z'))^2. (B.3)

Proof. By translating take a=0. Extend u to zero by the mean of its r neighboring values u(e_i). The added edge energy is

    sum_i [u(e_i)-mean_j u(e_j)]^2
      =(1/r)sum_(i<j)[u(e_i)-u(e_j)]^2
      <=(2/r)sum_(i<j){[u(e_i)-u(e_i+e_j)]^2
                       +[u(e_j)-u(e_i+e_j)]^2}.

Each edge in this last sum is a distinct internal edge, so the full-cube energy is at most (1+2/r) times the internal energy. Entropy decomposition between the puncture and its complement gives Ent_full(u^2)>=q0 Ent_punctured(u^2), because the remaining two-group entropy is nonnegative. Apply (B.2) and use N q0=N-1. QED.

### Lemma B.2 — measured residual mixture is paid by internal boundary

For the residual Boolean family h_z in (A.2), let P_z be its squared Fourier spectrum and Pbar its mean. Then, in bits,

    H(Pbar)-E_z H(P_z) <= kappa_r B/q0,
    kappa_r=(2/ln2)(1+2/r),                            (B.4)

for r>=2. For r=1 the mixture is a single distribution and B=0.

Proof. Apply (B.3) to each REAL signed Fourier coefficient u(z)=hhat_z(s), sum over s and divide by ln2. The left side becomes the Jensen-Shannon mixture information. Parseval makes each edge's summed squared coefficient difference equal E_w(h_z-h_z')^2, four times the physical disagreement probability. The internal boundary identity B=(2/N)E_w[number of internal sign-changing edges] gives (B.4). QED.

This keeps the actual measurement information rather than replacing it by the generally larger pure-state ensemble entropy. It avoids a logarithm of a tiny perturbation parameter in that term.

### Theorem B.3 — stronger one-row Shannon peeling

Under (A.1), for any epsilon>=0 with B<=epsilon q,

    H(f)<=q H(g)+q0 E_z H(h_z)+4(1+epsilon)q(r+1).     (B.5)

In particular B<=q/16 gives coefficient 17/4, improving 9/2 from the first proof, and arbitrary signs are allowed through the true payload g. No residual-dimension factor appears.

Proof. Let v=E_w[1-(E_z h_z)^2]. The punctured variance lemma of REPORT.md gives v<=2B/q0. The x-absent control-frequency nonzero mass is s=q+q0v. Its entropy is at most Phi_N(s)=h_2(s)+s log_2(N-1). As Phi_N is concave on [0,1],

    Phi_N(s)-Phi_N(q)<=2r q0v

regardless of how large v is; no v<=1/2 condition is needed here. Replace the Holevo part of the original proof by (B.4). The entropy excess over the exact B=0 expression is at most

    kappa_r B+2r q0^2 v
       <=[kappa_r+4r q0]B.                             (B.6)

For every integer r>=2,

    kappa_r+4r q0 <=4(r+1).                            (B.7)

For completeness, ln2>2/3 implies kappa_r<3+6/r. For r>=6 this is at most four; for r=2,3,4,5 it is respectively at most 6,5,9/2,21/5, each at most 4+4r2^-r. Rearranging gives (B.7). Combine (B.6), K_r<4q(r+1), and B<=epsilon q. For r=1, B=0 and (A.4) applies. QED.

The corresponding critical-core exclusion and restriction-closed-class induction hold exactly as in the original report, now with arbitrary support signs and coefficient 4(1+epsilon). This still does not prove that arbitrary critical cores have such exact support or small transverse surplus.

## C. An actual near-support elimination step, with coefficient twelve

The next theorem permits support errors. It does not require any agreement of derivative signs.

Let eta_x=1{f(0,z,w)!=f(1,z,w)} be the sensitivity indicator of a pivot x. Let Q={z=a} be a coordinate subcube of codimension r>=1 in the other variables. Put q=2^-r and

    E=Pr[eta_x != 1_Q].                                (C.1)

Write Z for the r defining control coordinates and I_Z=sum_(k in Z)I_k(f). Let p=I_x(f). It suffices to assume the average control condition I_Z<=r p; in particular this holds if x is a maximum-influence coordinate.

### Theorem C.1 — near-subcube maximum-row block step

For every Boolean f, if

    I_Z<=r I_x(f),    E<=q/(16r),                       (C.2)

then restricting the PHYSICAL control block Z gives

    Delta_Z H:=H(f)-E_z H(f_(Z=z)) <=12 I_Z(f).          (C.3)

There is no dependence on the number of residual variables. In particular the exact support requirement from the first report is no longer needed for this coefficient-12 block result. The error tolerance is explicitly relative to q/r, NOT a fixed relative-1/16 tolerance independent of r.

Proof, step 1: control boundary versus support error. Let F_z be the actual Boolean restriction f_(Z=z), which retains x and w. On an edge from a to a+e_k, if eta_x differs between the endpoints, the two Boolean functions of x disagree at exactly one of the two x values. Therefore that edge's x-averaged disagreement is at least half the difference of the sensitivity indicators. Write e_a=Pr_w(eta_x(a,w)=0) and e_b=Pr_w(eta_x(b,w)=1) for b!=a. The total contribution of edges incident to a to I_Z is at least

    rq-q[r e_a+sum_(b neighbor a)e_b] >=rq-rE.          (C.4)

Also |p-q|<=E and I_Z<=rp. If B_int is the internal punctured control boundary of the family F_z, then

    I_Z>=rq-rE,
    B_int<=r(q+E)-(rq-rE)=2rE<=q/8.                   (C.5)

Proof, step 2: a general near-constant punctured ensemble. Let v=1-||E_(z!=a)F_z||_2^2. The same punctured-cube variance bound applies to F_z as unit Boolean vectors on the common residual cube, so v<=2B_int/q0. Let theta be the probability that the actual Fourier sample of f contains some coordinate of Z. Parseval gives

    theta=1-||q F_a+q0 E_(z!=a)F_z||_2^2
         =q0 v+q q0||F_a-E_(z!=a)F_z||_2^2
         <=2B_int+4q <=17q/4.                          (C.6)

Proof, step 3: true restriction mixture information. Apply the FULL cube log-Sobolev inequality (B.2), now to each residual Fourier coefficient of F_z. Summing as in Lemma B.2 gives the standard block restriction mixture bound

    H(E_z |Fhat_z|^2)-E_z H(F_z) <= (2/ln2) I_Z.       (C.7)

The entropy chain rule and H(S_Z|S_remaining)<=H(S_Z) imply

    Delta_Z H <= H(S_Z)+(2/ln2)I_Z.                    (C.8)

For r>=3, 17q/4<=1-q, and Phi_N(s)=h_2(s)+s log_2(N-1) increases up to 1-q. Equations (C.6) and h_2(s)<=s log_2(e/s) therefore give

    H(S_Z)<=Phi_N(17q/4)
           <=(17/2)qr+(17/4)q log_2(4e/17)
           <(17/2)qr-(17/8)q.                         (C.9)

The last strict bound uses e<3 and 12/17<1/sqrt(2), the latter following from 288<289. Since 2/ln2<3 and I_Z>=q(r-1/16), (C.8)-(C.9) are below 12 I_Z: explicitly,

    9I_Z >=9qr-(9/16)q
            >(17/2)qr-(17/8)q.

For r=1,2, use H(S_Z)<=r in (C.8). The lower bound I_Z>=q(r-1/16) makes r/I_Z+2/ln2<12 directly (indeed the coarse use 2/ln2<3 suffices). This proves (C.3). QED.

### Corollary C.2 — quantified exclusion in a putative high-ratio primitive core

Let f be centered and H/J-critical under proper physical restrictions, with H(f)/J(f)>12. For every maximum-influence pivot and every coordinate subcube Q of codimension r>=1 in its sensitivity domain,

    Pr[eta_x != 1_Q] > 2^-r/(16r).                    (C.10)

Proof. Otherwise (C.3) applies. The exact folded drift satisfies D_Z=J(f)-E J(f_(Z=z))>=I_Z>0 in the centered gauge. Criticality gives Delta_Z H>=R D_Z, whereas (C.3) gives Delta_Z H<=12 I_Z<=12 D_Z, contradicting R>12. QED.

A restriction-closed class in which each centered noncharacter member has a row/block satisfying (C.2) obeys H<=12J by induction. This is a CLASS theorem under a checkable structural hypothesis, not a claim of a universal FEI constant twelve. The missing universal assertion is that every dangerous core admits such a block, or an alternative paid elimination. The previous dilution counterexample still rules out maximum-influence selection WITHOUT the near-support hypothesis.

## D. Executed extension checks and exact limits

New `check_support_extension.py` imports the delivered basic Walsh/entropy routines and tests the new claims. It examines all 256 three-bit Boolean functions and 4,096 seeded four-bit samples (with possible repeats, not exhaustive four-bit coverage). It finds 1,967 exact-subcube-support rows, 398 maximum-influence rows, and certifies the arbitrary-sign peeling bound for all 1,967 rows with rational logarithm enclosures. Zero-surplus structural and influence identities are integer/Fraction exact.

Five genuinely approximate-support families are materialized in dimensions 6,10,13,15,18, with 64 through 262,144 actual truth-table values. They have f=(-1)^x when z=0 OR w=0, and f=1 otherwise. Their support error E=q0*2^-m is positive and at most q/(16r); each has a unique maximum ORDINARY-influence pivot. The r=1 example has pivot influence 17/32 and is not presented as already centered. The coefficient-12 control-block inequality is verified by exact rational entropy enclosures. The sign-payload omission example has exactly H=5 and the incorrect no-payload right side four.

The exact support theorem allows arbitrary derivative signs through a retained genuine payload. The near-support theorem allows support error at the explicit q/(16r) scale. Neither proves the current all-row relative-constant error case or pays an arbitrary positive-defect bank. These are concrete new transfers to the adaptive restriction programme, not the full proof. All results remain self-checked/pending independent review; no priority claim is made for the use of log-Sobolev tensorization or composition.
