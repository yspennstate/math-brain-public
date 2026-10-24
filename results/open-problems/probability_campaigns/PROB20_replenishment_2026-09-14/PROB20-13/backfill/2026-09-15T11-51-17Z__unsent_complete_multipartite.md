# PROB20-13 backfill — complete multipartite electrical-flow theorem

**Original provenance:** prior scheduled PROB20-13 run on 2026-09-15, unsent/unarchived because the task-specific directory was not present and the GitHub write did not produce a durable receipt.

**Original status:** PARTIAL. The universal conjecture remained open.

## Exact target
For every finite connected simple unweighted graph,
\[
F(G):=\inf_{\mathbf f}\psi(\mathbf f)\stackrel{?}{\le}2\tau_{\rm rel}D,
\]
with \(\operatorname{div}f^a=\delta_a-\pi\), \(\pi_x=\deg(x)/(2|E|)\), simple random walk \(P\), \(\tau_{\rm rel}=(1-\lambda_2(P))^{-1}\), and
\[
\psi(\mathbf f)=\max_{(x,y)}\frac{\sum_a\pi_a|f^a_{xy}|}{\pi_xP_{xy}}.
\]

## Exact product-demand formulation retained
For \(m=|E|\), \(\pi_xP_{xy}=1/(2m)\) on every edge. Set \(g^a=\pi_af^a\). Then
\[
\operatorname{div}g^a=\pi_a\delta_a-\pi_a\pi.
\]
After cycle cancellation and path decomposition, the problem is exactly the undirected multicommodity instance with unordered demand \(h_{ab}=2\pi_a\pi_b\) and edge capacity \(1/(2m)\). Its optimum is \(F(G)\). The metric LP dual is
\[
F(G)=\max_{\ell\ge0,\ \sum_ec_e\ell_e\le1}\sum_{x,y}\pi_x\pi_y d_\ell(x,y).
\]
Every cut congestion is at most \(2\tau_{\rm rel}\) by scalar Poincare.

## Peer correction recovered in that run
Repository peer work at commit `e4fc52ab9b716a5270c9d073e296b8ef7a45da87`, especially
`proofnet24/portfolio-completion/runs/2026-09-14/2026-09-14_20-23-26/agents/001.md` and `agents/055.md`, showed that an archived stronger gap-1 shortcut is false: \(K_{2,3}\) has exact stationary product-demand flow/cut gap \(39/35>1\). This does not refute the diameter target. The same peer work proves
\[
F(K_{a,b})=3-\frac1a-\frac1b.
\]

## Theorem: every complete multipartite graph satisfies the target
Let
\[
G=K_{n_1,\dots,n_k},\qquad k\ge2,
\]
with total \(N=\sum_i n_i\). If \(G\) is not complete, an explicit admissible electrical family has congestion strictly below \(3\). Since every noncomplete complete multipartite graph has \(D=2\) and \(\tau_{\rm rel}=1\), this yields
\[
F(G)<3<4=2\tau_{\rm rel}D.
\]
The all-singleton case is the complete graph, where equality is known.

### Electrical family
Let \(L\) be the ordinary combinatorial Laplacian. For each source \(s\), solve
\[
Lv^{(s)}=\delta_s-\pi
\]
up to an additive constant, and put
\[
f^{(s)}_{xy}=v^{(s)}_x-v^{(s)}_y.
\]
Then \(\operatorname{div}f^{(s)}=\delta_s-\pi\).

Write \(d_i=N-n_i\) and \(p_i=d_i/(2m)\), so every vertex in part \(i\) has stationary mass \(p_i\).

Fix an edge \(xy\) joining a part of size \(a\) to a part of size \(b\), with \(a\ge b\). Put
\[
c=N-a-b.
\]
Let \(Q\) be the number of edges induced by the remaining \(c\) vertices and define
\[
R:=bc+Q.
\]
Then
\[
m=a(b+c)+R.
\]
Set
\[
\delta:=\frac{a-b}{2mN}.
\]
For the fixed oriented edge \(x\to y\), the potential difference \(v_x^{(s)}-v_y^{(s)}\) takes the following exact values according to the source location:

- source outside both endpoint parts: \(\delta\);
- source \(s=x\): \(\delta+(N-1)/(N(N-a))\);
- source in the size-\(a\) part but \(s\ne x\): \(\delta-1/(N(N-a))\);
- source \(s=y\): \(\delta-(N-1)/(N(N-b))\);
- source in the size-\(b\) part but \(s\ne y\): \(\delta+1/(N(N-b))\).

The signs are fixed because \(\delta<1/(N(N-a))\) and \(\delta<(N-1)/(N(N-b))\). Summing source-weighted absolute values and dividing by physical edge capacity \(1/(2m)\) gives the exact electrical congestion
\[
\boxed{\Psi_{a,b}=2+\frac{a+b-4}{N}+\frac{(a-b)(R-(a-b))}{mN}.}
\tag{B1}
\]

### Uniform bound \(\Psi_{a,b}<3\)
From (B1),
\[
3-\Psi_{a,b}=\frac{H}{mN},
\]
where
\[
H=m(c+4)-(a-b)(R-(a-b)).
\]
Using \(m=a(b+c)+R\),
\[
H=a(b+c)(c+4)+R(b+c+4-a)+(a-b)^2.
\tag{B2}
\]
If \(b+c+4-a\ge0\), all terms are nonnegative and the first is positive.

If \(b+c+4-a<0\), then
\[
Q\le\frac{c(c-1)}2,
\qquad
R=bc+Q\le bc+\frac{c(c-1)}2.
\]
Because the coefficient of \(R\) in (B2) is negative, substituting this upper bound yields
\[
2H\ge 2a^2+4ab+ac^2+9ac+2b^2c+2b^2+3bc^2+7bc+c^3+3c^2-4c.
\]
Also
\[
c^3+3c^2-4c=c(c+4)(c-1)\ge0
\]
for integer \(c\ge1\), while for \(c=0\) the lower bound reduces to \((a+b)^2>0\). Hence \(H>0\), proving \(\Psi_{a,b}<3\) on every edge.

Therefore
\[
F(G)\le\max_e\Psi_e<3.
\]

### Relaxation time
For complete multipartite \(G\),
\[
A=J-\operatorname{diag}(J_{n_1},\dots,J_{n_k}).
\]
On \(\sum_xz_x=0\),
\[
z^TAz=-\sum_i\left(\sum_{x\in V_i}z_x\right)^2\le0.
\]
Thus \(A\) has at most one positive eigenvalue; connectedness gives exactly one. The normalized adjacency \(D^{-1/2}AD^{-1/2}\) is congruent to \(A\), so all non-Perron eigenvalues are nonpositive. If some part has size at least two, there is a zero eigenvalue from a within-part sum-zero vector. Hence
\[
\lambda_2(P)=0,\qquad \tau_{\rm rel}=1.
\]
A noncomplete complete multipartite graph has diameter \(2\), so
\[
F(G)<3<4=2\tau_{\rm rel}D.
\]
If every part is a singleton, \(G=K_N\) and the complete-graph equality applies.

## Verification status and limitations
This was self-checked algebra and an explicit admissible flow family, not independent/formal review. It proves a large special class only, not the universal target. The successful electrical proof depends heavily on multipartite quotient structure.

## Failed routes retained
- Gap-1 flow-cut shortcut is false already on \(K_{2,3}\).
- Cut bounds alone do not control arbitrary metric duals.
- Pointwise two-hop domination is stronger than needed and fails on small examples.
- Naive electrical \(L^2\)/effective-resistance bounds lose constants on dense graphs.

## Next attack recorded in original run
Study equitable blow-ups of small base graphs, especially diameter-two bases, by solving the quotient Poisson equation plus within-cell source deviations; in parallel, perform exact-rational LP counterexample searches on low-symmetry diameter-two graphs with small \(\tau_{\rm rel}\).
