text(ALL_TOOLS.find(x=>x.name==="mcp__codex_apps__github_create_blob")?.description);
const H=k=>{
 const [a,b,cr,ci]=k,r=cr*cr+ci*ci;
 const p=[(1-a)*(1-b)-r,a*(1-b)+r,(1-a)*b+r,a*b-r];
 return {p,h:-p.reduce((s,x)=>s+(x>0?x*Math.log(x):0),0)};
};
const mix=(a,b,t)=>a.map((x,i)=>(1-t)*x+t*b[i]);
const cases=[
 {name:"complex indefinite",k0:[.35,.6,.10,.03],k1:[.40,.55,-.05,.07],t:.3},
 {name:"rank-one boundary",k0:[.1,.1,.1,0],k1:[.35,.35,.35,0],t:.4},
 {name:"opposite projections",k0:[.5,.5,.5,0],k1:[.5,.5,-.5,0],t:.5},
 {name:"complex pure-offdiagonal",k0:[.3,.6,.1,.05],k1:[.3,.6,-.08,.1],t:.4},
 {name:"diagonal rank-one direction",k0:[.2,.4,0,0],k1:[.7,.4,0,0],t:.25},
 {name:"definite complex direction",k0:[.2,.25,.02,.01],k1:[.5,.65,.07,.04],t:.65}
];
let checks=[];
for(const o of cases) {
 const d=o.k1.map((x,i)=>x-o.k0[i]),[u,s,vr,vi]=d,v2=vr*vr+vi*vi,delta=u*s-v2;
 const p0=H(o.k0),p1=H(o.k1),pt=H(mix(o.k0,o.k1,o.t));
 const t=o.t,gap=pt.h-(1-t)*p0.h-t*p1.h;
 const bound=t*(1-t)*(delta>0?4*delta:Math.max(2*u*u,2*s*s,16/9*(1-t+t*t)*delta*delta));
 const pure=u===0&&s===0?8/3*t*(1-t)*(1-t+t*t)*v2*v2:null;
 if(Math.min(...p0.p,...p1.p)<-1e-12 || gap+1e-12<bound || (pure!==null &&gap+1e-12<pure))throw new Error(o.name);
 checks.push({name:o.name,delta,gap,bound,pure});
}
let geoMax=0;
for(const t of [.1,.25,.5,.8])for(const x of [-.4,.15])for(const y of [0,.27]){
 const q=s=>(s*s+y*y)**2;
 const direct=(1-t)*q(x-t)+t*q(x+1-t)-q(x);
 const form=t*(1-t)*(6*(x+(1-2*t)/3)**2+2*y*y+(1-t+t*t)/3);
 geoMax=Math.max(geoMax,Math.abs(direct-form));
}
text({checks,geometryMaxError:geoMax});
store("083_checks",{checks,geometryMaxError:geoMax});