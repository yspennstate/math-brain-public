import census, sys, time
t=time.time()
total, c, mnf = census.run(7)
print(f"n=7  normalised matrices={total}   ({time.time()-t:.0f}s)")
for k in ('PAIR0','PAIRNZ','REP','REPNZ','CORANK2','INTSPEC'):
    print(f"   {k:8s} {c[k]:10d}   P = {c[k]/total:.8g}   x 4^n = {c[k]/total*4**7:.4f}")
print(f"   smallest float margin among UNflagged: {mnf:.3e}")
