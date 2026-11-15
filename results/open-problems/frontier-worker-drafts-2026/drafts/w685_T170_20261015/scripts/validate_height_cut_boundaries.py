"""Adversarial finite checks of the all-length decomposition's boundary quotas."""
from pathlib import Path
from itertools import product
from collections import Counter
from datetime import datetime,timezone
import json,time,ctypes
ROOT=Path(__file__).resolve().parents[1]

def main():
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(),0x4000)
    start=time.monotonic();counts=Counter();naive_witness=None
    for length in range(4,19):
        for word in product((-1,1),repeat=length):
            heights=[0]
            for step in word:heights.append(heights[-1]+step)
            H=heights[-1];visits=Counter(heights)
            cuts=[i for i,h in enumerate(heights) if 4<h<H and visits[h]==1]
            assert cuts==sorted(cuts,key=lambda i:heights[i])
            counts['words']+=1
            if not cuts:
                n=length-4;m=word[4:].count(-1)
                assert 4*m>=n-17
                counts['no_cut_words']+=1
                if H<=4:counts['nonpositive_or_small_endpoints']+=1
                if 4*m<n-1 and naive_witness is None:
                    naive_witness={'word':word,'case':'no cut','n_after_seed':n,'negative_steps':m,'endpoint':H}
                continue
            n=cuts[0]-4;m=word[4:cuts[0]].count(-1)
            assert cuts[0]>=5 and 4*m>=n-17
            counts['prefixes']+=1
            for i in cuts:
                assert word[i-1]==word[i]==1
            for left,right in zip(cuts,cuts[1:]):
                width=heights[right]-heights[left];part=heights[left+1:right]
                assert all(heights[left]<h<heights[right] for h in part)
                assert all(part.count(h)>=2 for h in range(heights[left]+1,heights[right]))
                assert 4*word[left:right].count(-1)>=right-left-1
                counts['irreducible_bridges']+=1
            n=length-cuts[-1];m=word[cuts[-1]:].count(-1)
            assert n>=1 and 4*m>=n-1
            counts['suffixes']+=1
    assert naive_witness is not None,'The check must distinguish the incorrect boundary-free quota.'
    out=dict(at=datetime.now(timezone.utc).isoformat(),counts=dict(counts),
             naive_boundary_free_quota_counterexample=naive_witness,seconds=time.monotonic()-start,
             scope='finite sign-word validation of prefix/no-cut/suffix quotas and strict-bridge cuts; mathematical all-length proof is in the manuscript')
    (ROOT/'logs/height_cut_boundary_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS height-cut boundaries',dict(counts),'seconds',out['seconds'],flush=True)
if __name__=='__main__':main()
