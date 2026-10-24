"use strict";
/*
Agent 106 independent audit of Agent 090's cubic theorem.
Dependency-free exact JavaScript. Executed in the functions V8 runtime.
This is an arithmetic/symbolic audit, not a proof-assistant formalization.
Rows are generated as multiplicity vectors, and derivatives are obtained
from grouped cubic monomials, independently of Agent 090's ordered-pair
expansion. The analytic argument is in 106_cubic_uniqueness_audit.md.
*/
(function () {
  let assertions = 0;
  function check(ok, label) {
    assertions++;
    if (!ok) throw new Error(label);
  }
  const fact = [1n, 1n, 2n, 6n];
  function gcd(a, b) {
    a = a < 0n ? -a : a; b = b < 0n ? -b : b;
    while (b) { const r = a % b; a = b; b = r; }
    return a;
  }
  function rat(n, d = 1n) {
    n = BigInt(n); d = BigInt(d);
    check(d !== 0n, "nonzero rational denominator");
    if (d < 0n) { n = -n; d = -d; }
    const g = gcd(n, d);
    return [n / g, d / g];
  }
  function add(a,b) { return rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]); }
  function sub(a,b) { return rat(a[0]*b[1]-b[0]*a[1],a[1]*b[1]); }
  function mul(a,b) { return rat(a[0]*b[0],a[1]*b[1]); }
  function cmp(a,b) { const s=a[0]*b[1]-b[0]*a[1]; return s<0n?-1:s>0n?1:0; }
  function fmt(a) { return a[1]===1n?String(a[0]):a[0]+"/"+a[1]; }
  function equal(a,b,label) { check(cmp(a,b)===0,label); }
  const one=rat(1), zero=rat(0), lambda=rat(3,10);
  function put(p,e,v) { const k=e.join(""); p[k]=(p[k]||0n)+v; if(p[k]===0n)delete p[k]; }
  function sumPoly(a,b) { const p={...a}; for(const k of Object.keys(b)) { p[k]=(p[k]||0n)+b[k]; if(p[k]===0n)delete p[k]; } return p; }
  function samePoly(a,b,label) {
    check([...new Set([...Object.keys(a),...Object.keys(b)])].every(k=>(a[k]||0n)===(b[k]||0n)),label);
  }
  function evalPoly(p,m) {
    let v=0n;
    for(const [e,c] of Object.entries(p)) {
      let t=c;
      for(let r=0;r<4;r++)for(let k=0;k<Number(e[r]);k++)t*=m[r];
      v+=t;
    }
    return v;
  }
  const rows=[];
  for(let n0=0;n0<=3;n0++)for(let n1=0;n1<=3-n0;n1++)
    for(let n2=0;n2<=3-n0-n1;n2++) {
      const n=[n0,n1,n2,3-n0-n1-n2];
      const names=[]; for(let r=0;r<4;r++)for(let k=0;k<n[r];k++)names.push(r+1);
      const multinomial=6n/n.reduce((v,k)=>v*fact[k],1n);
      const derivative=[];
      for(let j=0;j<4;j++) {
        const p={};
        if(n[j]) {
          const e=n.slice(); e[j]--;
          const numerator=multinomial*BigInt(n[j]);
          check(numerator%3n===0n,"integral A derivative coefficient");
          put(p,e,numerator/3n);
        }
        derivative.push(p);
      }
      let cut={...derivative[0]};
      for(const [e,c] of Object.entries(derivative[2]))cut=sumPoly(cut,{[e]:-c});
      const allowed=n.flatMap((count,r)=>count===0?[r]:[]);
      check(allowed.length>0,"strict cubic row has an allowed offspring");
      const groups=[...new Set(allowed.map(r=>r<2?1:0))];
      rows.push({n,key:names.join(""),multinomial,derivative,cut,allowed,groups});
    }
  rows.sort((a,b)=>a.key.localeCompare(b.key));
  check(rows.length===20,"twenty multiplicity rows");
  const free=rows.filter(r=>r.groups.length===2);
  check(free.length===12,"twelve independent group choices");
  let forced={};
  for(const row of rows)if(row.groups.length===1&&row.groups[0]===1)forced=sumPoly(forced,row.cut);
  samePoly(forced,{"1001":-2n,"0101":-2n,"0002":-1n},"forced contribution");
  const expectedFree={
    "111":{"2000":1n},
    "113":{"2000":-1n,"1010":2n},
    "114":{"1001":2n},
    "133":{"1010":-2n,"0020":1n},
    "144":{"0002":1n},
    "222":{},
    "223":{"0200":-1n},
    "224":{},
    "233":{"0110":-2n},
    "244":{},
    "333":{"0020":-1n},
    "444":{}
  };
  for(const row of free)samePoly(row.cut,expectedFree[row.key],"independent derivative row "+row.key);
  // A single deterministic tensor realizes the sharp bound for every q.
  // Keys and values are one-based parent multisets and offspring labels.
  const witness={
    "111":2,"112":3,"113":2,"114":2,"122":3,
    "123":4,"124":3,"133":4,"134":2,"144":2,
    "222":1,"223":4,"224":1,"233":4,"234":1,
    "244":1,"333":4,"334":1,"344":1,"444":1
  };
  let witnessCut={};
  for(const row of rows) {
    const offspring=witness[row.key]-1;
    check(row.allowed.includes(offspring),"admissible sharp witness row "+row.key);
    if(offspring<2)witnessCut=sumPoly(witnessCut,row.cut);
  }
  samePoly(witnessCut,{"1010":2n,"0101":-2n},"all-coordinate witness identity D=2ac-2bd");
  // Every free p is affine, so its extrema occur at the 4096 binary
  // assignments. Check the maximum independently at rational test points
  // covering all ratio regimes, boundaries, and zero-coordinate cases.
  const inputs=[
    [1,1,1,1], [8,8,8,1], [1,1,1,0],
    [4,1,1,2], [2,1,1,4], [2,1,3,2],
    [1,1,2,4], [1,2,6,7], [0,1,2,1],
    [2,1,0,1], [0,1,0,1]
  ];
  const maxima=[];
  let enumeratedAssignments=0;
  for(const input of inputs) {
    const m=input.map(BigInt), den=m.reduce((a,b)=>a+b,0n);
    const base=evalPoly(forced,m), weights=free.map(r=>evalPoly(r.cut,m));
    let best=null;
    for(let mask=0;mask<(1<<free.length);mask++) {
      let value=base;
      for(let k=0;k<free.length;k++)if(mask&(1<<k))value+=weights[k];
      if(best===null||value>best)best=value;
      enumeratedAssignments++;
    }
    const options=[m[0]*m[0],2n*m[0]*m[2],m[2]*m[2]];
    const formula=options.reduce((a,b)=>a>b?a:b)-2n*m[1]*m[3];
    check(best===formula,"full binary maximum at "+input.join(","));
    maxima.push({numerators:input,denominator:String(den),maximum:fmt(rat(best,den*den))});
  }
  // Recompute A directly from all 64 ordered parent triples, checking the
  // grouped differentiation against a different construction.
  const sharp=[];
  for(const [qn,qd] of [[1,4],[8,25],[1,3]]) {
    const m=[BigInt(qn),BigInt(qn),BigInt(qn),BigInt(qd-3*qn)], den=BigInt(qd);
    const A=Array.from({length:4},()=>Array(4).fill(0n));
    for(let a=0;a<4;a++)for(let b=0;b<4;b++)for(let j=0;j<4;j++) {
      const key=[a+1,b+1,j+1].sort((u,v)=>u-v).join("");
      A[witness[key]-1][j]+=m[a]*m[b];
    }
    for(let j=0;j<4;j++) {
      check(A[j][j]===0n,"zero diagonal");
      check(A.reduce((s,row)=>s+row[j],0n)===den*den,"column stochasticity");
      for(let r=0;r<4;r++) {
        let grouped=0n;
        for(const row of rows)if(witness[row.key]===r+1)grouped+=evalPoly(row.derivative[j],m);
        check(grouped===A[r][j],"ordered A agrees with grouped derivative");
      }
    }
    const D=A[0][0]+A[1][0]-A[0][2]-A[1][2];
    const target=2n*BigInt(qn)*(4n*BigInt(qn)-den);
    check(D===target,"sharp cap transfer");
    // DT=(7I+9A)/10 with common denominator 10*den^2.
    let cutNorm=0n, evaluatedCuts=0;
    for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(i!==j)
      for(let mask=0;mask<16;mask++) {
        let value=0n;
        for(let r=0;r<4;r++)if(mask&(1<<r))
          value+=7n*den*den*((r===i?1n:0n)-(r===j?1n:0n))+9n*(A[r][i]-A[r][j]);
        if(value>cutNorm)cutNorm=value;
        evaluatedCuts++;
      }
    check(evaluatedCuts===192,"every cut and ordered transfer checked");
    check(cutNorm<=9n*den*den,"witness derivative contraction bound");
    sharp.push({cap:fmt(rat(qn,qd)),transfer:fmt(rat(D,den*den)),derivativeNorm:fmt(rat(cutNorm,10n*den*den)),evaluatedCuts});
  }
  function f(s) {
    const t=sub(one,s);
    return add(mul(rat(7,10),s),mul(lambda,mul(t,mul(t,t))));
  }
  equal(f(rat(1,3)),rat(29,90),"invariant cap endpoint");
  const chain=[[1,1],[7,10],[1,2],[2,5],[7,20],[1,3]].map(v=>rat(...v));
  const endpoint=[[7,10],[4981,10000],[31,80],[431,1250],[26191,80000]].map(v=>rat(...v));
  const capChain=[];
  for(let k=0;k<5;k++) {
    const value=f(chain[k]);
    equal(value,endpoint[k],"exact cap endpoint "+k);
    check(cmp(value,chain[k+1])<=0&&cmp(lambda,chain[k+1])<=0,"both convex-envelope endpoints bounded");
    capChain.push({from:fmt(chain[k]),endpoint:fmt(value),to:fmt(chain[k+1]),endpointEquality:cmp(value,chain[k+1])===0});
  }
  const cutBounds={
    sameSide:rat(9,10),
    reverseCrossing:add(rat(-7,10),rat(9,10)),
    singletonForward:rat(7,10),
    tripleForward:rat(7,10),
    pairForward:add(rat(7,10),mul(rat(9,10),rat(2,9)))
  };
  for(const [label,value]of Object.entries(cutBounds))check(cmp(value,rat(9,10))<=0,"cut class "+label);
  equal(mul(rat(3),rat(2,9)),rat(2,3),"uniqueness gain");
  equal(mul(rat(10),lambda),rat(3),"residual multiplier");
  const result={
    status:"PASS",
    method:"multiplicity-vector generation and differentiation of grouped cubic monomials",
    symmetricRows:rows.length,
    independentFreeRows:free.length,
    exactBinaryAssignmentsEnumerated:enumeratedAssignments,
    binaryMaximumChecks:maxima,
    symbolicAllQWitness:"D=2*a*c-2*b*d; at (q,q,q,1-3q), D=2*q*(4*q-1)",
    deterministicWitness:witness,
    sharpExamples:sharp,
    capChain,
    cutBounds:Object.fromEntries(Object.entries(cutBounds).map(([k,v])=>[k,fmt(v)])),
    residualMultiplier:"3",
    assertionCount:assertions
  };
  if(typeof globalThis.audit106Report==="function")globalThis.audit106Report(result);
  else console.log(JSON.stringify(result,null,2));
  return result;
})();
