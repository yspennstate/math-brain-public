"""Explicit Gaussian realization of the higher-rank Dicke-sector obstruction."""
from pathlib import Path
import json
import numpy as np
from check import atoms, entropy, splitter


def main():
    w=np.exp(2j*np.pi/3)
    U=np.array([[1/np.sqrt(2),0],
                [1/np.sqrt(6),1/np.sqrt(3)],
                [1/np.sqrt(6),w/np.sqrt(3)],
                [1/np.sqrt(6),w*w/np.sqrt(3)]])
    assert np.max(abs(U.conj().T@U-np.eye(2)))<1e-14
    P=U@U.conj().T
    p0=atoms(P);p1=atoms(np.eye(4)-P)
    q=atoms(splitter(P,np.eye(4)-P))
    a=np.array([p0[s]*p1[15^s] for s in range(16)])
    b=np.array([q[s+((15^s)<<4)] for s in range(16)])
    expected=np.array([1/16 if s in [0,15] else 1/144 if s.bit_count()==2 else 0
                       for s in range(16)])
    assert np.max(abs(b-expected))<1e-14
    change=entropy(b/b.sum())-entropy(a/a.sum())
    assert abs(change-np.log(4/(3*np.sqrt(3))))<1e-14
    result=dict(sector_mass=float(b.sum()),input_conditional_entropy=entropy(a/a.sum()),
                output_conditional_entropy=entropy(b/b.sum()),conditional_entropy_change=change,
                determinant_error=float(np.max(abs(b-expected))))
    print(json.dumps(result,indent=2))
    Path(__file__).with_name('dicke-sector-results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
