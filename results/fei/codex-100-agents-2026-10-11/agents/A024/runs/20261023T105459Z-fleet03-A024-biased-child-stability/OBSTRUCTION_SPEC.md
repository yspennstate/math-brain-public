# Frozen fixed stress certificates, no search

Exactly two actual Boolean functions, with data dimensions m=4 and m=10 fixed
now. Physical selector is bit0; q=sum_{j=0}^{m/2-1} x_(2j+1)x_(2j+2),
edit E={vertex1}. Query selector bit0 (not a quadratic incident pivot).
Use exact full spectra on32 and2048 inputs. Check B>4d at m4 and B>10d at m10,
q_odd=m*d and I=m/2+(m+1)*d. Record q_odd/I. Check every distinguished
fiber fails the sufficient good-query certificate at the indicated K; this
is NOT a counterexample to existence of a good query or to FEI. Run<=60s,
memory<50MB, no random sampling or further dimension increase. Helper unchanged
from code/check_flat.py; hashes recorded. Execute after other jobs finish.
