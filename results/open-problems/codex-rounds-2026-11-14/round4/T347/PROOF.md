# A strictly decreasing shell profile with strict local minima

All patterns in this construction are deterministic and correlated.
It gives no bound on the capacity for iid patterns. It shows that even
strict decrease of the limiting shell ground-state profile does not,
by itself, exclude single-spin local minima near a stored pattern.

## Construction and statement

Fix an integer B >= 3. For q >= 1 let K=2^q and N=BK. Index neurons
by (z,l), where z belongs to F_2^q and 1 <= l <= B. For a,z in F_2^q
write

\[
\chi_a(z)=(-1)^{a\cdot z}.
\]

Store the all-positive pattern \(\xi^0\) once. For each nonzero a,
store the two patterns

\[
\xi^{a,+}_{z,l}=\chi_a(z),\qquad
\xi^{a,-}_{z,l}=-\chi_a(z).
\]

There are M=2K-1 patterns. For any spin configuration sigma define

\[
Q(\sigma)=\sum_\mu(\xi^\mu\cdot\sigma)^2,
\qquad H(\sigma)=-\frac{Q(\sigma)}{2N}.
\]

The shell energy-gain profile around the stored reference \(\xi^0\) is

\[
E_N(d)=\max_{d(\sigma,\xi^0)=d}\frac{Q(\sigma)}{2N^2},
\qquad m_d=1-\frac{2d}{N},\qquad 0\le d\le N.
\]

**Theorem.** These arrays have the following properties.

1. The patterns are pairwise distinct and M/N tends to 2/B.
2. If r is the remainder of d on division by B, then
   \[
   E_N(d)=1-\frac{m_d^2}{2}
                 -\frac{4K r(B-r)}{N^2}. \tag{1}
   \]
   In particular
   \[
   \sup_{0\le d\le N}
   \left|E_N(d)-\left(1-\frac{m_d^2}{2}\right)\right|
   \le\frac1K. \tag{2}
   \]
   The limiting profile \(E(m)=1-m^2/2\) is strictly decreasing on
   \([0,1]\): for every \(0\le m_1<m_2\le1\),
   \(E(m_1)>E(m_2)\).
3. There are exactly \(2^K\) single-spin local minima. They are precisely
   the configurations constant within each block. All are strict, and
   every single-spin flip from any of them increases H by at least
   \[
   2\left(1-\frac MN\right)>0. \tag{3}
   \]
   Equality is attained at the all-positive reference. Thus every stored
   pattern is itself a strict minimum, and the smallest flip cost at
   the reference tends to \(2(1-2/B)>0\).

For B=14 the limiting load is 1/7=0.142857142857..., and the limiting
smallest flip cost at the reference is 12/7. The profile at that reference
still strictly decreases throughout positive overlap. This comparison
with 0.138 is only an illustration for correlated patterns.

## Proof of the Gram identity

For any nonzero b, choose a coordinate j with b_j=1. Pairing a with
a+e_j shows

\[
\sum_{a\in\mathbb F_2^q}\chi_a(b)=0.
\]

For b=0 the same sum is K. Since
\(\chi_a(z)\chi_a(w)=\chi_a(z+w)\), it follows that

\[
\sum_a\chi_a(z)\chi_a(w)=K\mathbf1_{\{z=w\}}.
\]

Let A be the neuron Gram matrix, so
\(A_{(z,l),(w,t)}=\sum_\mu\xi^\mu_{z,l}\xi^\mu_{w,t}\).
The one constant pattern and the two signs of each nonconstant pattern
give

\[
A_{(z,l),(w,t)}
=1+2\sum_{a\ne0}\chi_a(z)\chi_a(w)
=2K\mathbf1_{\{z=w\}}-1. \tag{4}
\]

In particular A has diagonal entries 2K-1=M. Put

\[
S_z=\sum_{l=1}^B\sigma_{z,l},\qquad S=\sum_z S_z.
\]

Expanding the quadratic form using (4) gives the exact identity

\[
Q(\sigma)=2K\sum_z S_z^2-S^2. \tag{5}
\]

The listed patterns are distinct. At z=0 every positive character is
+1 and every negative character is -1, so a positive and a negative
character cannot agree. Different positive characters differ at some z,
because their quotient is a nonconstant character; the same holds for
two negative characters. The positive constant character is included
only once and the negative constant character is excluded. Repetition
of coordinates within blocks preserves these distinctions. Finally,
M/N=(2K-1)/(BK) tends to 2/B.

## Exact maximization on each shell

At Hamming distance d from the all-positive reference, let r_z be the
number of negative spins in block z. Thus

\[
0\le r_z\le B,\qquad \sum_zr_z=d,\qquad
S_z=B-2r_z,\qquad S=N-2d.
\]

On the shell, the term S^2 in (5) is fixed. Maximizing Q is therefore
equivalent to maximizing \(\sum_z(B-2r_z)^2\).

Suppose two blocks have counts x,y strictly between 0 and B. Relabel
them so x <= y. Move one negative spin from the block with count x
to the block with count y. The new counts x-1,y+1 remain between 0 and B,
and the change in the sum of squared block magnetizations is

\[
\begin{aligned}
&(B-2(x-1))^2+(B-2(y+1))^2\\
&\hspace{15mm}-(B-2x)^2-(B-2y)^2
=8(y-x+1)>0.
\end{aligned}
\]

Thus a maximizing tuple has at most one count strictly between 0 and B.
Conversely, writing d=tB+r, 0 <= r < B, one can fill t entire blocks
with negative spins and put the remaining r negative spins in one block
if r>0. When d=N take all K blocks full. Such a tuple exists on every
shell, and every maximizing tuple has this form up to the choice of
blocks. Its squared block magnetizations sum to

\[
\max\sum_z S_z^2=KB^2-4r(B-r).
\]

Substitution in (5), followed by division by 2N^2, proves (1), since
\(K^2B^2=N^2\). The bound \(0\le r(B-r)\le B^2/4\)
proves (2), including the endpoint shells d=0,N. For m_1<m_2 in [0,1],
\(E(m_1)-E(m_2)=(m_2^2-m_1^2)/2>0\).

## All local minima and their stability margin

For an individual neuron i=(z,l), expansion of H under a spin flip gives

\[
H(\sigma^{(i)})-H(\sigma)
=\frac{2}{N}\sigma_i\sum_{j\ne i}A_{ij}\sigma_j.
\]

The diagonal must be removed even though it contributes only a constant
to H. From (4), the signed off-diagonal field numerator is

\[
\sigma_i\sum_{j\ne i}A_{ij}\sigma_j
=\sigma_i(2KS_z-S)-M. \tag{6}
\]

Suppose a block contains both a positive and a negative spin. For the
positive spin to be stable, (6) requires \(2KS_z-S\ge M\).
For the negative spin to be stable, it requires \(2KS_z-S\le-M\).
These are incompatible because M>0. Every non-strict local minimum
must therefore be constant in each block.

Conversely, let every block have a uniform sign t_z. Then S_z=Bt_z,
\(|S|\le N\), and (6) becomes

\[
2KB-t_zS-M\ge2KB-N-M=N-M.
\]

For B>=3 and K>=2, N-M=(B-2)K+1>0. All such configurations are strict
local minima, and their flip costs obey (3). There are exactly two
choices for each of K blocks, giving exactly 2^K minima. At the
all-positive reference S=N, so equality holds in (3) at every neuron.
Every stored pattern is constant within blocks, completing the proof.

There is also a direct check of the margin at the reference that does
not use the off-diagonal field identity. Every nonconstant stored pattern
has zero dot product with the reference, so Q_0=N^2. After one spin flip,
the constant-pattern projection is N-2 and each of the other M-1
projections has absolute value 2. Hence

\[
Q_1=(N-2)^2+4(M-1)=N^2-4(N-M),
\]

again giving the flip cost \(2(1-M/N)\).

## Barriers hidden by the limiting profile

The reference is a strict local minimum but a lower-energy state is
obtained by reversing an entire block. If r spins in one block have
been reversed from the reference, direct use of (5) gives

\[
Q_r-Q_0=4r(Mr-N),\qquad
H_r-H_0=2r\left(1-\frac MN r\right). \tag{7}
\]

At r=1 this is the positive cost in (3). At r=B it equals
\(-2B(1-1/K)<0\). Reversing the block one spin at a time gives a path
to a lower-energy state with maximum energy excess at most

\[
\max_{x\in\mathbb R}2x(1-(M/N)x)=\frac{N}{2M}.
\]

This remains bounded as K grows with B fixed. Every path leaving the
reference first pays the cost (3), so the barrier to the set of
lower-energy states is positive and of order one in total energy.
Dividing by N removes it. In particular, uniform convergence to a
strictly decreasing macroscopic profile need not preserve the sign of
adjacent-shell differences.

The construction excludes an inference from strict decrease alone.
Its antipodal pattern pairs and identical neuron rows inside each block
violate iid sampling. An exclusion theorem using iid information, and
the AGS threshold and replica-symmetric free energy requested in T347,
remain outside this result.
