# Additional equality case (not an inequality failure)

The first full census stopped at n=4, table mask 1343, because the helper
incorrectly assumed every equality table would be a Maj3 junta. It certified
Lambda_bits=3(I-1) exactly first; the failure was only the extra classification
assertion. out/UNEXPECTED_EQUALITY.json retains the actual Walsh spectrum.
The singleton coefficients are (1/4,1/4,1/2,1/2); I=3/2. Hence Lambda_bits
=2*(1/16)*4+2*(1/4)*2=3/2, the same ratio as Maj3. The rest of the spectrum
has six additional coefficients of magnitude 1/4. Removed the unsupported
uniqueness assumption; census now retains every equality table and marks
Maj3 juntas separately. Domain/arithmetic/constant are unchanged.

The table has the direct Boolean description: if x3=x4 return x3;
otherwise return x1 when x3=+1 and x2 when x3=-1. This four-bit equality
family will be proved and independently checked after the census completes.
