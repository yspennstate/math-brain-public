# Independent reconstruction of the signed pair/refund interface

Source A052-SIGNED-PAIR-ORIENTATION-REFUND@1, statement SHA256 0d5d1b3a63e30b4dd8764721c26540119443affc0750d61c11e42b7931ef71c7, SIGNED_PAIR_PROOF.md sections1--4 in run20261014T015635Z-fleet05-A052-critical-source-structure. A053 verdict: ACCEPT complete analytic scope, including the two stated dependencies reconstructed below. No substantive repair supplied. Source finite assertion totals are not adopted.

For a real Fourier quartet, write A=alpha^2+beta^2 and B=gamma^2+delta^2. The weighted variance identity

    4[(alpha beta)^2/A+(gamma delta)^2/B-(alpha beta+gamma delta)^2/(A+B)]
      =4[alpha beta B-gamma delta A]^2/[(A+B)AB]

independently reconstructs M_i; the zero-weight extension is zero. Interchange beta and gamma for M_j. Expanding the square of the physical row gives three nonconstant Fourier coefficients of w^2, namely twice alpha beta+gamma delta, alpha gamma+beta delta and alpha delta+beta gamma. Parseval then gives exactly C_pair=C_i+C_j+P-M_i-M_j. This is signed variance before squaring and retains both refunds.

Cauchy--Schwarz bounds the parity square by q(delta^2+beta^2) and also q(delta^2+gamma^2). Averaging prices P by2v. For every nonnegative x,y,4xy/(x+y)>=2min(x,y), so the two singleton collisions pay2e. The identity v=e+o is pointwise and hence yields P<=C_i+C_j+2o, and the claimed unconditional orientation-corrected bound follows.

Reconstruction of A055-SINGLETON-CRITICAL-RESERVE@1 (SHA256 bfc2c09293d9446e7301b5c562668288de096d6758459530ec93bf1db80c09bf): singleton B is the q-weighted binary entropy of minority mass e. The row JS even series has coefficients1/[ln2*2k(2k-1)]. Comparing with the binomial series of1-sqrt(1-z^2) proves J<=2beta/ln2. Concavity gives D+S+K O<=h2(beta)-(K-2/ln2)beta, bounded by its binary Legendre maximum log2(1+2^(2/ln2-K)). Keeping actual physical S_i,S_j and their nonnegative sign only for least-essential-dimension violations proves A052's guarded substitution. An exponentially small residual is an upper bound, not a contradiction to D>0.

Reconstruction of A051-TWO-BIT-CRITICAL-PHASE-RESERVE@1 (SHA256 25d00942803b7fd8918a198dc313101701674dc04a88f5919f6624bf28288e09): classify actual sign rows. A nonconstant two-bit Boolean phase has influence>=1; at c<=1/16 its normalized row law has influence>=1-2sqrt(c)>=1/2 and entropy<=2. A constant-phase row has nonempty Fourier mass e<=||u-sign(u)||2^2<=c, and the entropy-minus-Kinfluence is bounded by log2(1+3*2^-K). Bad phase mass is at most16C. Summing uses the exact D+S_pair=B+J-KI_pair. Jensen bounds J<=Gamma and Gamma<=log2(1+C); the concave capped entropy function yields the collision-only bank. The three quartic squares are each priced by their Cauchy--Schwarz degree masses, yielding C<=6I. This reproduces every dependency needed for A052's monotone bank insertion with no missing reserve.

The parity guard remains a valid Boolean control; the sharp orientation coefficient refers only to real rows. Actual Boolean witnesses are not inferred from arbitrary real quartets. The new zero-refund classification and sparse-code surgery estimates in this run are separate applications and do not repair or alter the reviewed A052 version. Registry adoption remains pending.
