from t353_core import diffT2, I, w2
for z in [1.95, 1.99, 1.999, 2.0, 2.001, 2.003, 2.005, 2.007, 2.01, 2.02, 2.05]:
    al, be, ga = w2(z)
    print("z=%.4f diff=% .4e  I_S=%.6e I_A=%.6e" % (z, diffT2(z), I(0, -1, al, be, ga), I(2, 1, al, be, ga)), flush=True)
