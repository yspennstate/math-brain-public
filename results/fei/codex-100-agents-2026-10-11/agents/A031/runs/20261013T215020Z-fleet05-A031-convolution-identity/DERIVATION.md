# Signed derivative-carrier credits and the tree quantifier

All functions are finite uniform-cube Boolean signs. Entropy is in bits.
Fix an actual coordinate and its children g,h. Put A=(g+h)/2,
V=(g-h)/2, u=hat A, v=hat V, d=E V^2=Inf_i(f), and q_T=u_T^2+v_T^2.
The full signed Boolean convolution constraints imply A V=0 pointwise.
In particular sum_T u_T v_T=E AV=0. No absolute value is taken here.

## 1. A child-measurable carrier and a conserved mass

Let E={T:v_T!=0}; equivalently E={T:hat g(T)!=hat h(T)}.
Let rho=sum_(T in E) q_T. Since v vanishes off E, signed cancellation gives

    sum_E u_T v_T=sum_all u_T v_T=0,
    sum_E hat g(T)^2=sum_E (u_T+v_T)^2=rho,
    sum_E hat h(T)^2=sum_E (u_T-v_T)^2=rho.              (1)

Thus BOTH genuine children assign exactly rho to their disagreement carrier.
Moreover d<=rho<=1. This is the Boolean-specific admission; the subsequent
entropy chain rule alone is a generic probability identity. If d=0 then
E is empty, rho=0 and B_i=0. Otherwise rho>0 and define the normalized
carrier law P_E(T,Z=0)=u_T^2/rho, P_E(T,Z=1)=v_T^2/rho on E,
with mu=I_(P_E)(T;Z)>=0. Outside E the sector Z is deterministic zero.
Consequently

    B_i=rho h2(d/rho)-rho mu <=rho h2(d/rho)
        <=d log2(e rho/d).                             (2)

The last inequality uses -(1-t)ln(1-t)<=t, including t=1 by continuity.
Writing M_i=h2(d)-B_i, the exact credit decomposition is

    M_i=[h2(d)-rho h2(d/rho)]+rho mu.                  (3)

The bracket is I(Z;1_{T in E}) and is nonnegative. It is the credit from
knowing whether a Fourier row belongs to the carrier. The within-carrier
mutual information rho mu is separate and cannot be discarded for payment.
Equations (1)-(3) preserve signed cancellation before the entropy bound.
They use only the zero-shift consequence E AV=0 of full Booleanity, so
they are NOT a stronger replacement for full fourth-root admission.

Combining with the already proved fourth-root ledger, without dropping a
credit, gives B_i=W_i+log2(e)d-R_i-sigma(d)
-[h2(d)-rho h2(d/rho)]-rho mu. Nothing here proves its aggregate payment.

## 2. A normalized non-Boolean vector excluded by (1)-(2)

On the one-coordinate parent let u=12/13, v=-5/13 (only the empty retained
row). This real spectral vector has squared norm one but is not Boolean.
Its inverse values are 7/13 and 17/13. The formal child-carrier mass from
g is rho_g=49/169, with d=25/169<=rho_g<=1. Hence the claimed child-based
bound would read h2(25/169)<= (49/169) h2(25/49), which is false.
The right side is even below 49/169, whereas the left side exceeds 49/169;
the saved rational-log intervals certify the strict sign. The actual
q-carrier mass is one, NOT 49/169; the two child masses disagree.
The generic q-based conditional entropy inequality still holds. This is
precisely why the child-measurable formulation needs signed admission.

Tensoring by any genuine Boolean sign on disjoint coordinates preserves
d,rho,mu and B for the old coordinate: u,v multiply by the new Fourier
amplitudes, E becomes E times their nonzero support, and total squared
mass of that factor is one. Dummy coordinates are the special case of
a constant factor. A three-bit point defect is included in the checks.
No conditional-law or address hypothesis is imposed.

## 3. Exact carrier-only tree obstruction, not an FEI counterexample

Let f_n=1-2*1_{x=0}, n>=1. Every nonconstant restriction is another point
defect, and every complete physical restriction tree has exactly one
nonconstant history at each remaining dimension j, of reach 2^{j-n}.
Coordinate choices, even adaptive choices, do not change these values.
At dimension j, V is plus or minus the indicator of one retained point,
so every retained Fourier row has nonzero v, rho=1 and d_j=2^{1-j}.
Let C_K(T)=sum_internal w_v[rho_v h2(d_v/rho_v)-K d_v]_+ for fixed K>=0.
Since h2(d_j)>=d_j log2(1/d_j)=d_j(j-1),

    C_K(T)/I(f_n) >= (1/n) sum_(j=1)^n (j-1-K)_+,    (4)
    I(f_n)=n 2^{1-n}.

For integer K this lower bound is (n-K-1)(n-K)/(2n) when n>=K+1.
For arbitrary fixed real K use its ceiling. Thus C_K/I diverges for
EVERY complete tree: no adaptive order can pay the carrier-only envelope.
This is the known scalar-envelope obstruction specialized to the new
carrier currency, not a claim of a new Boolean family or FEI disproof.

For comparison the TRUE excess D_4(T)=sum w[B_v-4d_v]_+ is identically zero.
Each point-defect split has a constant child. Independently: for any
constant +1 child and other Boolean child h, d=(1-Eh)/2 and

    B=2d(1-d)+phi((1-d)^2,d^2),
    phi(a,b)=a log2(1+b/a)+b log2(1+a/b).

Since a+b<=1, phi(a,b)<=b log2(e/b), giving
B/d<=2+d(log2(e)-2)+2d log2(1/d). Its variable part is maximized at
d=1/(2sqrt(e)), with value log2(e)/sqrt(e)<1. The last strict inequality
follows from ln2>2/3 and e>5/2. Thus B<3d for 0<d<1; endpoints follow
directly. This recovers the constant-child lemma also used by A025,
not a new class theorem. The missing within-carrier credit obeys
rho mu=h2(d)-B >=d(j-4) for every point-defect node with j>=4.
Across the tree its required credit is quadratic before normalization by I.

## 4. The true positive-excess bill has no weaker tree quantifier

For ANY finite physical stopping tree T, let H_L=E H(f_leaf),
I_L=E I(f_leaf), J_T=sum_internal w JS_v, and
D_K(T)=sum_internal w[B_v-Kd_v]_+, K>=0. The exact singleton entropy
and influence telescopes (C005) give

    sum w B_v=H(f)-H_L-J_T,
    sum w d_v=I(f)-I_L,
    0<=J_T<=c_JS[I(f)-I_L], c_JS=2/ln2.

Taking positive parts only after retaining all local credits yields

 [H(f)-H_L-(K+c_JS)(I(f)-I_L)]_+
                <=D_K(T)<=H(f)-H_L.                  (5)

The lower bound uses B<=Kd+[B-Kd]_+ node by node. The upper bound uses
[B-Kd]_+<=B and nonnegative JS. For COMPLETE trees H_L=I_L=0.
Define A_exist(K)=sup_f inf_(complete T) D_K(T)/I(f), and
A_all(K)=sup_f sup_(complete T) D_K(T)/I(f), excluding constant f.
Then in the extended real sense

 A_exist(K)<=A_all(K)<=C_FEI<=A_exist(K)+K+2/ln2.       (6)

Therefore finiteness of the true joint-credit excess for SOME tree and
for EVERY tree is equivalent to FEI. Tree selection may improve constants
or larger sufficient currencies such as raw odd-face cost; it cannot
relax finiteness for the exact D_K currency. This does not refute the
existential localized raw odd-face target: raw cost is a different bill.

The universal first unsupported line remains a dimension-free influence
payment for the within-carrier signed entropy residual (or an alternative
full erasure residual). The carrier envelope alone is rigorously dead.
The positive proof route must exploit distribution within the carrier,
not merely expose whether the derivative's Fourier coefficient vanishes.
