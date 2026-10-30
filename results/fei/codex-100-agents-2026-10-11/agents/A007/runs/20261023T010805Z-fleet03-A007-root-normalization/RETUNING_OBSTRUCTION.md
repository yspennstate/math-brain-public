# All roots rare does not pay the gate-name mismatch

The following refutes the additional assertion v(f) KL_bits(Q_lambda'||Q_lambda)<=K I(f) for EVERY pair of packing-feasible fixed prime references related by thinning. It does not refute the existence of a suitable single reference, optimized queue cost or FEI. The Boolean function is fixed; it is a family of references, not an unbounded H/I Boolean family.

Use the actual three-bit function f=2[x2 AND (x1 OR x3)]-1. Its exact positive primes are R1={x1,x2} and R2={x2,x3}; they overlap at x2. Both have rarity1/4. Physical pivotal counting gives

    Pr(f=+1)=3/8, v=15/16, I=1/4+3/4+1/4=5/4,
    v/I=3/4.

For any integer j>=1 set delta=2^-j and fix BEFORE sampling a Fourier set

    lambda=(delta/2,delta^2/2),
    lambda'=(delta^3/2,delta^2/2).

Both vectors are positive and coordinatewise ordered. The largest packing row, at x2, is at most (delta+delta^2)/2<=3/8; all others are smaller. Every gate remains in the SAME exact prime table. The root activities are

    x=(delta/8,delta^2/8),
    y=(delta^3/8,delta^2/8),
    L=sum(x-y)=(delta-delta^3)/8.

Every activity tends to zero. The singleton laws nevertheless swap their weights:

    r_x=(1,delta)/(1+delta),
    r_y=(delta,1)/(1+delta).

Their exact bit KL is

    KL_bits(r_y||r_x)=j(1-delta)/(1+delta).             (1)

ROOT_THINNING.md retains the SAME nonempty-root normalizers and proves that the full root-prior KL differs from (1) by at most L/ln2. Since ln2>2/3 (the first positive atanh term, with remaining terms positive),

    v KL_bits(Q_y||Q_x)/I
      >=(3/4)j(1-delta)/(1+delta)
                                    -9(delta-delta^3)/64
      >(3/4)j-1.                                     (2)

For the last step, j2^-j<=1/2 follows from the initial j=1 value and adjacent ratio (j+1)/(2j)<=1. The deficit from (3/4)j is at most 3/4+9/128=105/128<1. Hence the ratio in (2) diverges; more sharply it equals (3/4)j+o(1), because j2^-j tends to zero and L tends to zero.

The exact signed normalization is not omitted: A_y/A_x=delta, and

    ln(D_y/D_x)=ln(delta)+Delta(y)-Delta(x),
    -L<=Delta(y)-Delta(x)<=0.

The leading rarity/total-mass logarithm combines with the likelihood of the same rare gate names; it does not cancel the name mismatch after the singleton laws swap. Multi-root conditioning contributes only O(delta), while the unpaid relative gate-name cost is order j. This locates the failed helper precisely and keeps rare-root normalization in its mathematical role.

The old OR2 forced-two-root posterior warning is also retained as a scope guard: a forest posterior concentrated on two singleton roots is not Q_y and need not satisfy a singleton approximation. That warning is inherited, not advertised as a new obstruction. The new three-bit reference-thinning family already defeats a universal all-reference KL payment within genuine overlapping prime tables.
