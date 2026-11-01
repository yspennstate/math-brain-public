# heeded:none sanity check of fei_core against published values
from fei_core import *
limit_process()
for name, F, ref in [("numaro g", numaro_g(), "H=6.7766053090, I=261/128=2.0390625"),
                     ("maj17", majority(17), "H/I=2.3988"),
                     ("tribes w2 s8", tribes(2, 8), "H/I=4.3296"),
                     ("bent+flip m4", bent_plus_flip(4), "H/I=2.2977"),
                     ("recmaj depth2", recmaj3(2), "H/I=2.2222")]:
    H, I = HI(F)
    print(f"{name:15s} n={len(F).bit_length()-1:2d} H={H:.10f} I={I:.10f} H/I={H/I:.4f}   ref {ref}")
