# Two-coordinate collision error with a retained phase margin

All functions are finite uniform-cube Boolean signs; entropy is in bits. Fix a two-coordinate queried block A. Zero-mass retained child Fourier rows are omitted. For each row write w_t(x)=hat(f_x)(t), q_t=E_x w_t^2, u_t=w_t/sqrt(q_t), and nu_t=hat(u_t)^2. Define

    c_t=E_x (w_t^2/q_t-1)^2,
    C_A=sum_t q_t c_t,
    Gamma_A=sum_t q_t log2(1+c_t),
    h_t=sign(w_t), with sign(0)=1.

Let W_0 be the sum of q_t for constant h_t. Among nonconstant phases let W_g be the mass with c_t<=1/16 and W_b the mass with c_t>1/16. Then W_0+W_g+W_b=1 and W_b<=16 C_A. These are actual Boolean row phases, but are not treated as physical descendants.

## 1. Elementary two-bit phase facts

Every nonconstant two-bit Boolean phase has influence at least 1. A one- or three-point negative set has four boundary edges, hence influence 1; a two-point negative set is adjacent (influence 1) or diagonal (influence 2). These exhaust the 14 nonconstant signs. Its entropy is at most 2, so FEI(2) on two bits follows directly. The constant phase has Fourier law delta_empty.

For unit physical row u and h=sign(u), put tau=||u-h||_2. The pointwise inequality (|u|-1)^2<=(u^2-1)^2 gives tau^2<=c. For unit Fourier vectors, summing |v_s^2-z_s^2| and Cauchy--Schwarz give spectral TV<=||v-z||_2=tau. Therefore TV(nu,hat(h)^2)<=sqrt(c). Expectations of degree, a function in [0,2], differ by at most 2 TV.

If h is nonconstant and c<=1/16, I(nu)>=I(h)-2 sqrt(c)>=1/2. As H(nu)<=2, for every K>=4,

    H(nu)-K I(nu) <= 2-K/2.                         (1)

On the nonconstant bad rows simply H(nu)-K I(nu)<=2. No square-root error is charged to good nonconstant phases: their known influence margin absorbs it.

If h is constant, e=1-nu(empty)=1-(E u)^2. Since |E u|=E |u|, e=(1-E|u|)(1+E|u|)<=2(1-E|u|)=tau^2<=c. For any law with mass 1-e at the empty set and remaining three atoms,

    H(nu)<=h2(e)+e log2 3,   I(nu)>=e.

Thus for EVERY K>=0,

    H(nu)-K I(nu)
       <=h2(e)-(K-log2 3)e
       <=log2(1+3*2^-K)=:r_K.                      (2)

The last bound follows by maximizing the binary entropy expression on [0,1]; its maximizer is e=3/(2^K+3). No criticality premise enters these row estimates.

## 2. Exact row-class bank and retained physical children

The Fourier restriction identities are

    B_A=sum_t q_t H(nu_t),   I_A=sum_t q_t I(nu_t),
    D_K(f)+S_A=B_A+J_A-K I_A,
    S_A=-E_x[H(f_x)-K I(f_x)].

The second identity is valid for arbitrary f; S_A has no stipulated sign there. Summing (1),(2) and the bad-row cap gives, for K>=4,

    D_K(f)+S_A+(K/2-2)W_g
        <= J_A+r_K W_0+2 W_b
        <= Gamma_A+r_K W_0+2 W_b.                 (3)

Every term uses the same queried influence I_A. There is no repeated row-level influence budget. W_g is a retained phase margin, W_b an explicitly charged exception mass, and S_A contains ALL four physical child deficits. Markov's inequality gives the relaxed form

    D_K(f)+S_A+(K/2-2)W_g
        <=log2(1+C_A)+r_K+32 C_A.                 (4)

For a least-essential-dimension FEI(K) violation, K>=4, the queried block is proper because every two-bit Boolean sign already obeys FEI(2). Each child has smaller dimension, so S_A>=0, and D_K(f)>0. Equations (3),(4) are then necessary on EVERY pair. In particular

    (K/2-2)W_g < log2(1+C_A)+r_K+32 C_A          (K>4).

This is a genuine phase-weight restriction on critical sources, not admission of arbitrary hard-core wrappers. Exponentially small r_K by itself does not contradict a positive deficit.

## 3. Pure collision modulus without an exponential floor

Define psi_2(s)=h2(s)+s log2 3 for 0<=s<=3/4, and psi_2(s)=2 for 3/4<=s<=1. This is concave, nondecreasing and psi_2(0)=0. Constant-phase rows have e<=min(1,c), hence H(nu)-K I(nu)<=psi_2(min(1,c)). Nonconstant good rows obey (1); bad rows are capped by 2. Let s_t=min(1,c_t) on constant-phase rows and s_t=0 otherwise. Jensen and sum q s_t<=min(1,C_A) give

    D_K(f)+S_A+(K/2-2)W_g
       <=Gamma_A+psi_2(min(1,C_A))+2 W_b
       <=log2(1+C_A)+psi_2(min(1,C_A))+32 C_A.     (5)

For C_A<=3/4 this is

    D_K(f)+S_A+(K/2-2)W_g
       <=log2(1+C_A)+h2(C_A)+(log2 3+32)C_A.

The error is O(C_A log(1/C_A)) as C_A tends to zero. It improves A052's O(sqrt(C_A)log(1/C_A))+2K sqrt(C_A) bound for two-coordinate blocks at K>=4. Both are valid statements with distinct scopes; the larger-block theorem is unchanged. This improvement uses the finite two-bit phase margin, not a claim that Fourier TV always has order C.

## 4. Collision is controlled by the same queried influence

Write the four real Fourier coefficients of a physical row as alpha,beta,gamma,delta, with delta the degree-two coefficient and q=alpha^2+beta^2+gamma^2+delta^2. Expanding the square gives

    c=4[(alpha beta+gamma delta)^2
         +(alpha gamma+beta delta)^2
         +(alpha delta+beta gamma)^2]/q^2,
    I(nu)=(beta^2+gamma^2+2 delta^2)/q.

By Cauchy--Schwarz the first two squares are at most q(beta^2+delta^2) and q(gamma^2+delta^2), respectively. The third square is at most each of q(delta^2+beta^2) and q(delta^2+gamma^2), so it is at most their average. Adding gives

    c<=6 I(nu),    C_A<=6 I_A.                    (6)

This bound is not claimed sharp. It prices collision and the exceptional phase mass against the same physical queried influence, with Gamma_A<=C_A/ln2<=6 I_A/ln2 and W_b<=96 I_A. The entropy/deficit selection still remains: paying those explicit collision terms does not pay the constant-phase entropy or force a positive reserve. No second influence account is introduced.

## 5. Exact guard against a singleton-collision shortcut

For f(x1,x2,y)=(-1)^((x1 xor x2)y) on three fair 0/1 bits, its four nonzero squared Fourier coefficients are each 1/4, on empty, {y}, {x1,x2}, {x1,x2,y}. Each singleton Fourier row for x1 or x2 has at most one nonzero coefficient, giving C_x1=C_x2=0. Yet the pair has C_{x1,x2}=1 and I_{x1,x2}=1: the degree-two signed product alpha delta+beta gamma remains. out/PARITY_GUARD.json is an exact direct-character certificate.

Thus no finite constant bounds joint pair collision by the sum of its two singleton collisions unconditionally. This example is not dimension-minimal: H=2,I=3/2,R=4/3, while a physical singleton child is a quadratic two-bit sign of ratio 2. The minimal-witness restriction cannot be omitted, and this low-ratio guard does not refute a guarded critical-source comparison or FEI.

## 6. Honest remaining line

These inequalities pay phase approximation by row-class margins and collision on any two-bit queried block; they do not pay B_A at a universal rate. The first unsupported line is: at some dimension-independent K>=4, every least-dimensional violating witness has a pair (or a larger paid block) for which the right side of (3) or (5) is smaller than its retained D_K+S_A+(K/2-2)W_g. Neither C_A nor W_b has been proved sufficiently small relative to this reserve. The shortest next step is to price the signed degree-two parity term with actual singleton orientation/child reserves under minimality, without replacing it by the false unconditional comparison above or reusing influence. This targets the universal gap rather than extending a finite class census.
