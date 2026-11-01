# A rational-mean obstruction for complete spectral conditioning

The empty coefficient in the normalized product Fourier basis is the physical mean. Every Boolean sign under finitely many rational Bernoulli biases has a rational mean: each physical atom has rational probability and the mean is a finite signed sum of those probabilities. This necessary condition holds after deterministic coordinates or repeated wires are contracted as well. It is independent of every nonempty Fourier phase.

## 1. Every proper empty-retaining conditioning of fair AND fails

Let d>=2, let f=2 product_i X_i-1 on d independent fair bits, and put a=2^(d-1). Its empty squared Fourier coefficient is (a-1)^2/a^2; each of its 2^d-1=2a-1 nonempty squared coefficients is 1/a^2. These follow by expanding the product, or by the alternating mixed difference on every nonempty set.

Let E be ANY event in the Fourier-set space that contains the empty set and exactly r nonempty sets, where

    1 <= r <= 2a-2.

Condition the entire spectral law on E, including its actual normalizer. The conditional empty mass is

    Q(empty)=(a-1)^2 / [(a-1)^2+r].                 (1)

The integer N=(a-1)^2+r lies strictly between the consecutive squares (a-1)^2 and a^2. It is not a square. A rational square root of an integer is an integer (write it in lowest terms and use prime factorization). Therefore sqrt(N) is irrational, and so is

    sqrt(Q(empty))=(a-1)/sqrt(N),                  (2)

because a-1 is a nonzero integer. No choice of the empty Fourier sign can turn this into a rational mean. Q is consequently not the normalized product Fourier law of any Boolean gate on ANY finite cube with rational product biases. The conclusion is not restricted to the source dimension, fair biases, inherited phases, or distinct candidate wires. A candidate with repeated wires must first identify the underlying physical variables, which still have rational atom probabilities.

The choice of the retained nonempty sets is arbitrary. Equal nonempty source masses make (1) depend only on their number, but this does not assert that the whole conditioned laws are equivalent. This necessary one-coordinate test rejects every such event, including those selecting on Fourier degree, one direction, or a proposed packet owner.

## 2. Scope tests that prevent a false strengthening

Both excluded endpoints are admitted. At r=0 the law is the empty point mass and is the spectrum of a constant Boolean function. At r=2a-1 there is no conditioning and the original AND gate supplies the spectrum. For d=1 there are no events in the stated proper range and the theorem makes no assertion.

The rational-input hypothesis matters. On fair AND2, retain the empty set and one singleton. The resulting two-atom law is (1/2,1/2). It is the spectrum of a Boolean sign equal to its single physical sign input at the irrational bias p=(1+1/sqrt(2))/2: its mean-square is (2p-1)^2=1/2, and its nonempty mass is 4p(1-p)=1/2. If the ambient label space has an unused second coordinate, add it as a dummy. Thus no rejection under all real product biases follows from this argument. It rejects admission at inherited rational biases and every other rational product law, exactly as stated.

Keeping the empty atom is also essential. Conditioning away the empty atom evades this particular test; the other Boolean identities remain to be checked. A finite real vector can have norm one and still fail Boolean admission. Conversely Q is a valid normalized spectral REFERENCE despite being non-Boolean, so Gibbs/KL identities can use Q. What fails is importing an inequality whose premise says Q itself comes from a Boolean gate.

Physical restrictions differ from (1). Fixing an AND input to zero gives a constant; fixing it to one gives AND on fewer inputs with all coefficients recomputed. Both have rational means at rational biases. Neither is this spectral conditioning. No product independence of spectral labels is presumed.

## 3. Relation to complete-reference payment

The all-d theorem strengthens the prior AND3 triple-deletion control: arbitrary proper empty-retaining spectral events now fail admission, for all phases and all finite rational input dimensions. It is an audit criterion, not an entropy lower bound, and it does not refute FEI or the complete quadratic-reference mechanism. A merged reference must be paid by its complete cross-entropy and ordinary KL remainder, not by resetting it to a fresh Boolean gate at rational induced biases.

The first unsupported universal line is unchanged: pay the complete selected signed cross-entropy from the same original mixed deficit with all terminal spectra and normalization retained. The A041 review in REVIEW_A041.md independently reconstructs its new coherence and mass-tax clauses, and supplies the concrete admitted alternative to an illegal Boolean reset. Its generic jump logarithm remains arity dependent.
