# P0162: independent specified-coordinate obstruction

Saved before reading w510's proof. This is an independent derivation, pending w512's mathematical review. It refutes a stronger auxiliary statement, not Fourier entropy versus total influence. Novelty is unverified.

## Exact target

For every n >= 1 and every Boolean f:{-1,1}^n -> {-1,1}, with uniform input, write f=sum_S fhat(S) chi_S. Does there exist an absolute C such that H(f)=sum_S fhat(S)^2 log_2(1/fhat(S)^2) <= C I(f), where I(f)=sum_S |S| fhat(S)^2? Include the empty coefficient in H, take 0 log(1/0)=0, and include constant functions. C may not depend on n or f.

Primary statement: O'Donnell, Wright, Zhou, author PDF https://www.cs.cmu.edu/~jswright/papers/fei.pdf, introduction. Recent relevant primary source: Gonzalez, MacManus, Pereyra, arXiv:2606.00246v1, introduction equation (1), Ansatz 1.1, and Section 4.2. Their induction asks for an EXISTING suitable splitting coordinate. The all-coordinate strengthening below is distinct.

## Independently derived family

Let n=2r >= 2. Identify the original n coordinates with t in F_2^n, with characters chi_S(t)=(-1)^(sum_{j in S} t_j). Set

g(t)=(-1)^(t_1 t_2 + t_3 t_4 + ... + t_{n-1} t_n),
delta_0(t)=1 if t=0 and 0 otherwise,
h(t)=g(t)-2 delta_0(t).

Both g and h are Boolean, since g(0)=1. Add a selector z in {-1,1} and set F(t,+1)=g(t), F(t,-1)=h(t). Set p=2^-n and s=sqrt(p)=2^-r.

The two-variable factor (-1)^(t_1 t_2) has coefficients (1,1,1,-1)/2. Tensoring gives ghat(S)=s sigma_S, sigma_S in {-1,1}. Fourier inversion at t=0 gives sum_S sigma_S=1/s. Thus the counts of positive and negative signs are N_+=(1/p+1/s)/2 and N_-=(1/p-1/s)/2. These are integers for every even n.

Since delta_0hat(S)=p, hhat(S)=s sigma_S-2p, and the two blocks of F's spectrum are

A_S=Fhat(S)=s sigma_S-p,
B_S=Fhat(S union {z})=p.

The selector influence is I_z(F)=sum_S B_S^2=p. The A block has total mass 1-p, and the B block has mass p.

## Rigorous unbounded ratio

Let U be the uniform distribution on the 2^n Fourier indices, U_S=p. Let P_A(S)=A_S^2/(1-p) and P_h(S)=hhat(S)^2. Write D_2 for relative entropy in bits and h_2 for binary entropy. The entropy chain rule gives

H(F)=n+h_2(p)-(1-p)D_2(P_A||U),
H(g)=n,
H(h)=n-D_2(P_h||U).

Consequently the actual split increment is

Delta_z H(F)=H(F)-(H(g)+H(h))/2
             =h_2(p)-(1-p)D_2(P_A||U)+D_2(P_h||U)/2.

For P_A/U=(1-s sigma_S)^2/(1-p), using E_U sigma=s yields the exact chi-square divergence

chi^2(P_A||U)=4p/(1-p).

The elementary inequality ln u <= u-1 gives D_2(P||U) <= chi^2(P||U)/ln 2. Also D_2(P_h||U)>=0 and h_2(p)>=p log_2(1/p)=np. Therefore

Delta_z H(F)/I_z(F) >= n - 4/ln 2.

For any fixed K, choose an even n > K+4/ln 2. This disproves the existence of a universal K with Delta_i H(f)<=K I_i(f) for EVERY Boolean f and EVERY splitting coordinate i.

The associated stronger squared-spectrum bridge also fails, with exact ratio

sum_S |ghat(S)^2-hhat(S)^2| / I_z(F)
= 4(1-p)/sqrt(p).

Proof: |ghat^2-hhat^2|=4p |s sigma-p|; insert N_+ and N_- and simplify.

## Boundary and scope checks

This is Boolean throughout. Multiplying F by an independent dictator w makes F, g and h balanced and preserves their Fourier entropies, selector influence, and split increment. Thus balancedness alone does not repair the all-coordinate bridge. This modification adds 1 to total influence.

For each original coordinate j, flipping g at 0 changes a formerly agreeing edge {0,e_j} into a disagreeing edge. Hence I_j(g)=1/2, I_j(h)=1/2+2p, and I_j(F)=1/2+p. Thus

I(F)=n/2+(n+1)p.

In particular this family does not refute the original FEI conjecture. Its total influence grows with n; its H(F)/I(F) tends to 2. It also does not refute the existential-coordinate induction. A good splitting coordinate can be one of the original coordinates.

## Independently derived sharp absolute increment bound

For any Boolean split g=f^+, h=f^- put a_S=ghat(S), b_S=hhat(S), w_S=(a_S^2+b_S^2)/2. For w_S>0 put q_S=a_S^2/(a_S^2+b_S^2), r_S=(a_S-b_S)^2/[2(a_S^2+b_S^2)]. Then sum_S w_S=1 and

Delta_i H(f)=sum_S w_S [1+h_2(r_S)-h_2(q_S)].

Since binary entropy lies in [0,1], this proves 0<=Delta_i H(f)<=2 bits. The upper bound is sharp: f(z,x,y)=((1+z)x+(1-z)y)/2 has four Fourier coefficients of magnitude 1/2, so H(f)=2, both restricted entropies are 0, and I_z(f)=1/2.

Consequently every original-coordinate split of the obstruction family has Delta_j H(F)/I_j(F)<=2/(1/2+p)<4. Quantifier choice is the hardest remaining piece of this proposed induction route.

## Sharp general profile and sharpness within Boolean functions

For u in [0,1], set L(u)=ln(2)[1-h_2((1+u)/2)] and J(u)=1-sqrt(1-u^2). Both vanish at 0. Their derivatives are L'(u)=atanh(u), J'(u)=u/sqrt(1-u^2). The derivative of J'-L' is (1-u^2)^(-3/2)-(1-u^2)^(-1)>=0. Integrate twice and use continuity at 1 to conclude L(u)<=J(u).

For a coefficient pair a,b take u=|a^2-b^2|/(a^2+b^2). Since sqrt(1-u^2)=2|ab|/(a^2+b^2) and 1-2|ab|/(a^2+b^2)<=1-2ab/(a^2+b^2)=2r, this proves 1-h_2(q)<=2r/ln(2). Sum with weights w and use concavity of h_2 and sum_S w_S r_S=delta=I_i(f). The result is

Delta_i H(f)<=h_2(delta)+(2/ln 2)delta.

This bound is prior work in the recalled Opus F4 memo; the argument here is an independent rederivation. It does not imply FEI because h_2(delta)/delta diverges at zero.

The constructed Boolean family shows that the additive coefficient 2/ln 2 is sharp when the binary entropy term is fixed. Define

L_k(s)=(1/2) sum_{sigma=+1,-1} (1+sigma s)(1-k sigma s)^2 log_2((1-k sigma s)^2).

For fixed k=1,2 this is an even analytic function near s=0. Expansion of its logarithm gives L_k(s)=[(3k^2-2k)/ln 2]s^2+O(s^4). The exact grouped entropies are H(h)=n-L_2(s) and H(F)=n(1+p)-L_1(s). Consequently

Delta_z H(F)/p=n+3/ln 2+O(p),
h_2(p)/p=n+1/ln 2+O(p),
[Delta_z H(F)-h_2(p)]/p -> 2/ln 2 as even n -> infinity.

Thus no smaller additive coefficient c works in Delta_i H(f)<=h_2(I_i(f))+c I_i(f) for all Boolean f and all i. This is sharpness of the restriction profile. The balanced wrapper preserves it.

## Remaining work

Recover exact local P0162 attempt rows and the relevant proof scar; record bounded recall results. Numerically check the explicit formulas with exact integer Fourier transforms in small dimensions. Then read w510's candidate argument and identify the precise step this obstruction affects. Request w512's independent review and prepare only concept/draft brain entries until it arrives.
