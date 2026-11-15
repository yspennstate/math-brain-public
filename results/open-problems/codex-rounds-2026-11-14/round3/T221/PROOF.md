# A quantitative finite-model obstruction from an entropy witness

All logarithms are natural. Entropy refers to finite random variables.
Let G be a group, A a finite alphabet of size k >= 2, and p a probability
vector on A. Let S,D be nonempty finite subsets of G, B a nonempty finite
alphabet, and f:A^S -> B. For independent p-labels (X_g) on G put

\[
 Y_g=f((X_{gs})_{s\in S}),\qquad
 a=H(Y_e),\quad c=H(X_e\mid(Y_t)_{t\in D}),\quad
 \delta=H(p)-a-c.                                      \tag{1}
\]

The result below is useful when delta > 0. It applies in particular to
every strict witness from the earlier report. No example with delta > 0
over an infinite group is constructed here.

## 1. The finite information inequality

Let V be a nonempty finite set. For each g in
K={e} union S union D union DS, let T_g be a permutation of V, with
T_e the identity. No multiplication law is assumed. Give V independent
p-labels (U_v), and define

\[
 Z_v=f((U_{T_s(v)})_{s\in S}),\qquad
 N_v=(Z_{T_t(v)})_{t\in D}.                            \tag{2}
\]

The entire Z-vector is a deterministic function of the U-vector. Consequently

\[
\begin{split}
 |V|H(p)
 &=H(U_V)=H(Z_V)+H(U_V\mid Z_V)\\
 &\leq\sum_{v\in V}H(Z_v)
       +\sum_{v\in V}H(U_v\mid Z_V)\\
 &\leq\sum_{v\in V}\{H(Z_v)+H(U_v\mid N_v)\}.        \tag{3}
\end{split}
\]

The first inequality is entropy subadditivity and conditional
subadditivity, obtained by the chain rule and removal of conditioning.
The second holds because N_v is a subtuple of Z_V (possibly with repeated
entries). Independence gives H(U_V)=|V|H(p).

Call v encoder-good if the points T_s(v), s in S, are distinct.
Call v decoder-good if both of the following conditions hold:

1. The points T_g(v), g in {e} union DS, are distinct for distinct g.
2. T_s(T_t(v))=T_{ts}(v) for every t in D and s in S.

At an encoder-good v, the law of Z_v is the law of Y_e, so H(Z_v)=a.
At a decoder-good v, the law of (U_v,N_v) is the law of
(X_e,(Y_t)_{t in D}), so H(U_v|N_v)=c. To verify the latter claim,
replace each occurrence of Z_{T_t(v)} using (2). Condition 2 replaces
its inputs by U_{T_{ts}(v)}. Condition 1 then gives precisely the
independence and coincidence pattern of the coordinates {e} union DS
in G, including repeated occurrences of a product ts.

At every vertex H(Z_v)<=log|B| and H(U_v|N_v)<=H(U_v)=H(p).
If alpha and beta are the respective fractions of encoder-bad and
decoder-bad vertices, (3) therefore proves

\[
 \boxed{\quad
 \delta\leq\alpha(\log|B|-a)+\beta(H(p)-c).
 \quad}                                                \tag{4}
\]

Both coefficients on the right are nonnegative. If eta is the fraction
of vertices bad in at least one sense, alpha,beta<=eta. Since
log|B|-a+H(p)-c=log|B|+delta, (4) gives, for delta>0,

\[
 \boxed{\qquad
 \eta\geq\frac{\delta}{\log|B|+\delta}.
 \qquad}                                               \tag{5}
\]

This bound is independent of |V|, the support sizes, and the probabilities
of individual labels. It does not assume approximate freeness or any
asymptotic model. The permutations can even be replaced by arbitrary
maps in (2)–(5); the permutation assumption is needed only below.

## 2. Relation to the earlier error certificate

For any d:B^D -> A put epsilon=Pr[X_e != d((Y_t)_{t in D})] and

\[
 \Phi_k(u)=-u\log u-(1-u)\log(1-u)+u\log(k-1).
\]

Let E record whether this decoder is wrong. E is determined by X_e and
Y_D. Conditional chain rules give

\[
\begin{split}
 H(X_e\mid Y_D)
 &=H(E\mid Y_D)+H(X_e\mid E,Y_D)\\
 &\leq H(E)+\varepsilon\log(k-1)=\Phi_k(\varepsilon).
\end{split}                                            \tag{6}
\]

Indeed, on E=0 the decoder fixes X_e, and on E=1 at most k-1 alternatives
remain. This proof includes epsilon=0 or 1, with 0 log 0=0.
If the earlier certificate has gap
Delta=H(p)-H(Y_e)-Phi_k(epsilon)>0, then delta>=Delta.
The function u/(log|B|+u) is nondecreasing for u>0. Thus (5) also holds
with Delta in place of delta. If |B|=1, then Y_D is constant and
c=H(p), so delta=0; no strict witness is lost by restricting to |B|>=2.

For uniform bases, the conditional-entropy form of the cost in (1) is
established prior work: it is the group specialization of the local
criterion of Lewis Bowen and Michael Chapman,
*Surjunctivity does not characterize cosoficity of invariant random
subgroups*, arXiv:2511.06586v1, Theorem 4.1 and Section 5. Here its role is
to sharpen the explicit finite-model defect bound. No new general local
entropy characterization is asserted.

## 3. Explicit word constraints

Suppose G is finitely generated, and choose words w_s and v_t in a free
group F_r representing s and t. Form the finite list of words

\[
 W=\{1\}\cup\{w_s:s\in S\}
             \cup\{v_tw_s:t\in D,s\in S\}.             \tag{7}
\]

Identical free words may be merged. The occurrences of w_s and v_tw_s
retain their indices for the tables. The equality classes of W in G
are part of the input data.

Choose a representative r_j from each equality class W_j. Let E consist
of the pairs (u,r_j) for u in W_j other than r_j. Let I consist of one
pair (r_i,r_j) for each i<j. The pairs E assert equality in G; the pairs
I assert inequality. Put m=|E|+|I|.

Assign arbitrary permutations to the free generators on any nonempty
finite V. Evaluate words as right actions: T_{uv}=T_v composed with T_u,
and evaluate inverse letters by inverse permutations. In this section
T_w is indexed by a free word, even when two words represent the same
element of G. For a permutation q write

\[
 \operatorname{fix}(q)=|\{v:q(v)=v\}|/|V|,\qquad
 d_H(q,1)=1-\operatorname{fix}(q).
\]

For each assignment define

\[
 Q(T)=\sum_{(u,v)\in E}d_H(T_{uv^{-1}},1)
      +\sum_{(u,v)\in I}\operatorname{fix}(T_{uv^{-1}}).
                                                               \tag{8}
\]

**Proposition.** If delta>0 for the code (1), then every such assignment
on every finite nonempty V satisfies

\[
 \boxed{\qquad Q(T)\geq
                  \frac{\delta}{\log|B|+\delta}.\qquad}       \tag{9}
\]

**Proof.** Call a vertex good when all the equalities in E hold there and
all the inequalities in I hold there, using word evaluations. At a good
vertex, all words in an equality class have the same image, and images
of distinct classes differ. Thus the entire equality pattern on W is
correct. The union bound shows that the fraction of vertices which are
not good is at most Q(T): for any pair (u,v),

\[
 T_u(z)=T_v(z)
 \quad\Longleftrightarrow\quad T_{uv^{-1}}(z)=z,         \tag{10}
\]

because T_{uv^{-1}}=T_v^{-1} composed with T_u.

Set Z_z=f((U_{T_{w_s}(z)})_s) and
N_z=(Z_{T_{v_t}(z)})_t. The information inequality (3) still applies.
Word evaluation gives T_{w_s}(T_{v_t}(z))=T_{v_tw_s}(z)
at every z. At every good z, the pattern on W therefore gives
H(Z_z)=a and H(U_z|N_z)=c. If eta is the fraction of vertices not good,
the same estimate as (5) gives eta>=delta/(log|B|+delta).
Combining with eta<=Q(T) proves (9). This argument does not require
choosing one permutation T_g for each group element. □

If m>0 and each summand in (8) is at most epsilon, (9) implies

\[
 \varepsilon\geq\frac{\delta}
                   {m(\log|B|+\delta)}.                 \tag{11}
\]

If m=0, Q(T)=0, so (9) rules out delta>0 immediately.
All words uv^{-1} from E are trivial in G, and all those from I are
nontrivial in G. This is a finite, explicit obstruction to their being
simultaneously close to identity and close to fixed-point-free,
respectively. It is a necessary consequence of an entropy witness,
not a converse to non-soficity.

For the finitely presented cover constructed in the earlier report,
the equalities E can be used as defining relators. The quotient onto the
original subgroup preserves the inequalities I. Thus every hypothetical
counterexample supplied by that reduction carries the quantitative
constraint (9). Exact rational statistics determine delta; a rational
strict lower bound for delta gives a numerical lower bound in (9).
The equality pattern itself is still required and is not claimed to be
decidable from an arbitrary finite presentation.

## 4. Checks and limitations

There is a second proof of the unsharpened version of (5). For each finite
model form the rank correction R_z relative to d(N_z). The vector (Z,R)
determines every U_z, even at bad vertices. Hence
|V|H(p)<=sum_z H(Z_z,R_z). At good vertices this is at most
H(Y_e)+Phi_k(epsilon), and at bad vertices it is at most log(|B|k).
If Delta>0 this gives

\[
 \eta\geq\frac{\Delta}
 {\log|B|+\log k-H(p)+\Delta}.                         \tag{12}
\]

For uniform p this agrees with (5) with Delta substituted for delta.
For nonuniform p the direct conditional proof is stronger because
H(U_z|N_z)<=H(p), whereas the rank alphabet bound uses log k.

The order v_tw_s in (7) is essential. Right evaluation was chosen exactly
so that it matches the nested encoder/decoder positions. Coordinates
which coincide in G must coincide in the model at a good vertex;
injectivity alone is insufficient. Conversely, imposing equalities alone
does not certify the needed independence between distinct coordinates.
Both kinds of defects are counted in (8).

The finite conditional information inequality itself already underlies
the known sofic lower bound. This note gives explicit constants for one
finite witness; it proves no new instance of RBS, finds no violating
code, and does not infer RBS failure from non-soficity. A finite search
without a witness has no implication for unrestricted window sizes.

References opened in this session:

- Brandon Seward, *Krieger's finite generator theorem for actions of
  countable groups II*, [arXiv:1501.03367v4](https://arxiv.org/abs/1501.03367v4),
  Theorems 1.10 and 1.12, for the earlier full-base reduction.
- Lewis Bowen and Michael Chapman, *Surjunctivity does not characterize
  cosoficity of invariant random subgroups*,
  [arXiv:2511.06586v1](https://arxiv.org/abs/2511.06586v1),
  Theorem 4.1 and Section 5.
