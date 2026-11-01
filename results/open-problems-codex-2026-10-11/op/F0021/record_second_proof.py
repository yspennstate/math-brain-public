from pathlib import Path
p=Path('~/brain_workers/TRIO_1011/op/F0021')
with p.joinpath('SECOND_ATTEMPT.md').open('a',encoding='utf-8') as f:f.write(r'''

## Lemma 9: lattice entropy-controlled chain count (proved)
Let n>=1, B>0, and ell>=1 be integers except that B is real. A chain is a sequence of sites (t_1,x_1),...,(t_ell,x_ell) with 1<=t_1<...<t_ell<=n, integer x_r, and starting point (t_0,x_0)=(0,0). Define

E(chain)=sum_{r=1}^ell (x_r-x_{r-1})^2 / (2(t_r-t_{r-1})).

Independently mark sites of the reachable cone with probability p. Let K(B) be the maximum number of marked sites in an ordered chain of entropy at most B, restricted to the cone. For 1<=ell<=n,

P(K(B)>=ell) <= [ e^2 n p/ell * (1+sqrt(2 pi B n)/ell) ]^ell.                 (9.1)

For ell>n the probability is zero. This bound retains a lattice correction, the term proportional to np/ell.

Proof. Write d_r=t_r-t_{r-1}>0 and y_r=x_r-x_{r-1}. For a chain of entropy at most B,
1 <= exp(ell) exp(-ell E/B).
For each fixed time tuple, sum the right-hand side over all integer spatial increments (enlarging from cone sites to every integer). This gives at most
exp(ell) product_{r=1}^ell [1+sqrt(2 pi B d_r/ell)].
Indeed sum_{z in Z} exp(-a z^2)<=1+sqrt(pi/a), by comparing the decreasing summands on the positive integers with the integral over [0,infinity). The Gaussian integral is the standard integral of exp(-a x^2).
By Cauchy–Schwarz, sum sqrt(d_r)<=sqrt(ell sum d_r)<=sqrt(ell n). The arithmetic–geometric mean inequality therefore bounds the product by
[1+sqrt(2 pi B n)/ell]^ell.
There are binomial(n,ell) time tuples, at most (en/ell)^ell. To justify the latter elementary bound, binomial(n,ell)<=n^ell/ell! and log(ell!)=sum_{j=1}^ell log j>=integral_1^ell log t dt=ell log ell-ell+1>=ell log ell-ell.
Thus the total number of entropy-constrained chains is at most the right-hand side of (9.1) with p removed. Every particular cone chain contains ell distinct sites, so its marking probability is p^ell by independence. A union bound proves (9.1). Finally, a longer chain has a subchain of length ell with no greater entropy (Lemma 10), so the union bound on exact length ell does cover K(B)>=ell.

## Lemma 10: entropy decreases when sites are deleted (proved)
For positive s,t and real x,y,

(x+y)^2/(s+t) <= x^2/s + y^2/t.

Proof. Subtracting the left numerator after multiplication by s+t gives the identity
(x^2/s+y^2/t)(s+t)-(x+y)^2=(t x-s y)^2/(st)>=0.
Divide by s+t>0. Deleting one interior point of a chain merges two increments and cannot increase its entropy by this inequality. Deleting the final point removes a nonnegative summand. Repetition proves the subchain assertion.
In particular each point (t,x) on a chain of entropy at most B satisfies x^2/(2t)<=B, by deleting every other point. No Lipschitz hypothesis is needed for these facts.

## Theorem 11: the polymer of all sufficiently large rewards is asymptotically the bare walk (proved special case)
Suppose only that the iid real disorder has a regularly varying right tail with exponent alpha>5. Fix beta>0 and choose

5/(3 alpha)<kappa<1/3.

Set u_n=n^kappa and eta^{(n)}_{i,x}=omega_{i,x} 1{omega_{i,x}>u_n}, and define

Z_n^{tail}=E_S exp(beta sum_{i=1}^n eta^{(n)}_{i,S_i}).

Then, with probability tending to one,

0<=Z_n^{tail}-1<=exp(-n^{1/3}/4).                                           (11.1)

Consequently log Z_n^{tail}->0 in probability, and the total variation distance between the quenched eta-polymer path law and the length-n bare-walk law tends to zero in probability. This is a triangular-array, rare-positive-reward special case. Its background is identically zero. It is not a statement about the original centered, unit-variance polymer.

### Step 1: choose an envelope exponent and count all large sites
Choose 5<q<alpha with q kappa>5/3; such a q exists since alpha kappa>5/3 and kappa<1/3. The dyadic-envelope proof in ATTEMPT.md, Lemma 1, gives P(omega>v)<=C v^{-q} for sufficiently large v.
Let A=n^{1/3}, L=ceil(log_2 n), and D=16 max(1,beta); assume n is sufficiently large that L>=1, u_n exceeds the envelope threshold, and A/(D L)>u_n. The last condition holds because kappa<1/3.
The number N of large sites in the entire cone satisfies
E N <= C n(n+3)/2 * u_n^{-q} <=2 C n^{2-q kappa}.
Therefore N/A->0 in probability, by Markov's inequality and q kappa>5/3.

### Step 2: no large point has small initial travel entropy
There are at most
S(B)=n+2 sqrt(2) n^{3/2} sqrt(B)
sites with x^2/(2t)<=B, t<=n (discarding parity and the cone boundary enlarges this count). Thus
P(exists large site with x^2/(2t)<=A)
 <= C S(A) u_n^{-q}
 =O(n^{1-q kappa}+n^{5/3-q kappa})->0.                                     (11.2)
By Lemma 10, on the complementary event, every nonempty chain consisting of large sites has entropy greater than A.

### Step 3: all chains of larger entropy have reward at most half their entropy
Use entropy levels B=2^b A, b=1,...,m, where m is the smallest nonnegative integer such that 2^m A>=n/2. For sufficiently large n, m>=1, and every such B is at most n. Every chain compatible with a nearest-neighbour walk has entropy at most n/2: each displacement obeys |y_r|<=d_r, so y_r^2/(2d_r)<=d_r/2, and sum d_r<=n.
Partition weights into dyadic layers I_j=(v_j,2v_j], v_j=2^j u_n, j>=0; every omega>u_n lies in exactly one such layer, including boundary values. Layer markings are independent across sites, with probability p_j<=C v_j^{-q}. We do not assume independence between different layers.

For a fixed B, call layers with v_j>B/(D L) high layers. The probability of any high-layer point with initial travel entropy at most B is at most
C S(B) [B/(D L)]^{-q}.
Indeed every such point has omega>B/(D L), which exceeds u_n for the n under consideration. Summing over the geometric B-levels gives an upper bound
C' (D L)^q [n A^{-q}+n^{3/2} A^{1/2-q}]
=O((log n)^q [n^{1-q/3}+n^{(5-q)/3}])->0,                               (11.3)
since q>5. Infinite high weight layers have been summed by this single threshold event; there is no unjustified finite upper cutoff on omega.

For each remaining (low) layer, v_j<=B/(D L). There are at most L+1<=2L such layers because u_n>=1 and B<=n. Put h_j=B/(D L v_j)>=1 and ell_j=floor(h_j)+1. If its entropy-controlled count K_j(B)>h_j, Lemma 9 applies at ell_j. Since ell_j>=h_j and q>2, its bracket is at most
R_n=C_1 L n^{2/3-kappa(q-1)} + C_2 L^2 n^{1-kappa(q-2)},                  (11.4)
with constants depending on C,D only. To verify (11.4), expand the bracket in (9.1), use p_j<=C v_j^{-q}, ell_j>=B/(D L v_j), and B>=A. This gives terms bounded by a constant times
L n v_j^{1-q}/B and L^2 n^{3/2} v_j^{2-q}/B^{3/2};
these decrease in v_j, so replace v_j by u_n and B by A.
Both n-exponents in (11.4) are strictly negative. Specifically,
kappa(q-1)=q kappa-kappa>5/3-1/3=4/3,
kappa(q-2)=q kappa-2kappa>5/3-2/3=1.
Thus R_n->0 polynomially up to logarithms. For all sufficiently large n it is below one, so the failure probability R_n^{ell_j} is at most R_n. There are at most O((log n)^2) entropy/layer pairs; a union bound makes the probability of any low-layer count failure tend to zero. If ell_j>n the event is impossible, which causes no exception to this reasoning.

On the event excluding both high-layer points and low-layer count failures, any compatible chain with A<E<=n/2 belongs to a dyadic level E in (B/2,B]. Each of its low-layer subchains has entropy at most B by Lemma 10, so it contains at most h_j points. Its total reward obeys
beta sum omega <= beta sum_{low j} 2 v_j K_j(B)
 <= beta * (2L) * 2B/(D L)
 =4 beta B/D <=B/4 < E/2.                                                (11.5)
High-layer points are absent from that chain because each of its points has initial travel entropy at most E<=B. Equations (11.2)–(11.5) prove, with probability tending to one, that EVERY nonempty compatible chain of large sites has E>A and beta sum omega<=E/2. All chains are controlled together, rather than one chain chosen independently of the disorder.

### Step 4: expand the exact partition function over subsets of large sites
For a realized finite environment, write R for its N large sites. For every path,
exp(beta sum eta)=product_{z in R} [1+(exp(beta omega_z)-1)1{path visits z}].
Expand this product and take bare-walk expectation. The empty subset contributes one. Any nonempty subset which cannot be visited by one path contributes zero. A compatible subset is ordered uniquely by its distinct visit times, and contributes
P_S(visits chain) product_{z in chain}(exp(beta omega_z)-1)
 <= exp(-E(chain)+beta sum_{z in chain} omega_z)
 <= exp(-E(chain)/2)
 <= exp(-A/2)
on the event from Step 3. The walk probability bound is the product of the simple-walk transition probabilities at successive time gaps, by the Markov property, each bounded by its quadratic Chernoff cost as proved in ATTEMPT.md, Lemma 3.
There are at most 2^N-1 nonempty subsets. Hence
0<=Z_n^{tail}-1<=(2^N-1) exp(-A/2)<=exp(N log 2-A/2).
Because N/A->0 in probability, with probability tending to one N log 2<=A/4; this proves (11.1). The assertion about log follows from 0<=log Z<=Z-1.

### Step 5: total variation of the quenched path measures
Let W=exp(beta sum eta)>=1 and Z=E_S W. The polymer density relative to the bare path law is W/Z. By the triangle inequality,
TV=(1/2) E_S|W/Z-1|
 <=(1/2)E_S[(W-1)/Z+(Z-1)/Z]=(Z-1)/Z<=Z-1.
Equation (11.1) completes the proof.

## Immediate limitation
Writing omega=min(omega,u_n)+(omega-u_n)_+ does NOT turn Theorem 11 into an upper bound on log Z(omega)-log Z(min(omega,u_n)). The latter partition ratio is an exponential expectation under the capped-polymer path law, not under the bare walk. The Chernoff transition estimate in Step 4 applies only to the bare walk. A product/subadditivity inequality for two backgrounds would be needed for that shortcut, and such an inequality is false in general (to be checked explicitly below).
''')
with p.joinpath('LITERATURE.md').open('a',encoding='utf-8') as f:f.write('''- Second read-only math_recall.py query: `Berger Torri entropy controlled last passage percolation quadratic entropy ordered points`; returned generic entropy/FPP cards, no relevant closure.\n- Fetched and read Berger–Torri, *Entropy-controlled Last-Passage Percolation*, arXiv:1805.11989v1 (29 May 2018), Theorem 2.1 p. 3 and entropy definition (2.1) p. 2. Its application theorems use alpha<2; not a solution of F0021. The additional attempt independently proves an iid-marking chain bound with a lattice correction, rather than invoking the continuum volume bound in a lattice setting.\n''')
print('Saved complete chain-count proof and rare-reward special-case theorem; checking next.')
