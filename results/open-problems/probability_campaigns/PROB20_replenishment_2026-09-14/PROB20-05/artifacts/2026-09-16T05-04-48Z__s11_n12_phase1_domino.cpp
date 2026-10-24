#include <algorithm>
#include <array>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <numeric>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_set>
#include <vector>
using namespace std;

static inline int psi12(int k){ k=abs(k); if(k==0) return 8; if(k==1) return 13; return 12*k; }

struct Tup { int a,b,c,d,e,f; bool operator==(Tup const&o) const {return tie(a,b,c,d,e,f)==tie(o.a,o.b,o.c,o.d,o.e,o.f);} };
struct TupHash { size_t operator()(Tup const&k) const { size_t h=0; int v[6]={k.a,k.b,k.c,k.d,k.e,k.f}; for(int x:v) h=h*1009+(x+500); return h; } };

static void hungarian11(const double cost[11][11], int assign[11]){
    const int n=11; double u[12]={},v[12]={}; int p[12]={},way[12]={};
    for(int i=1;i<=n;i++){
        p[0]=i; int j0=0; double minv[12]; bool used[12]={}; for(int j=1;j<=n;j++) minv[j]=1e100;
        do{
            used[j0]=true; int i0=p[j0],j1=0; double delta=1e100;
            for(int j=1;j<=n;j++) if(!used[j]){
                double cur=cost[i0-1][j-1]-u[i0]-v[j];
                if(cur<minv[j]){minv[j]=cur;way[j]=j0;}
                if(minv[j]<delta){delta=minv[j];j1=j;}
            }
            for(int j=0;j<=n;j++) if(used[j]){u[p[j]]+=delta;v[j]-=delta;} else if(j) minv[j]-=delta;
            j0=j1;
        }while(p[j0]!=0);
        do{int j1=way[j0]; p[j0]=p[j1]; j0=j1;}while(j0);
    }
    for(int j=1;j<=n;j++) assign[p[j]-1]=j-1;
}

vector<vector<pair<int,int>>> factorization10(vector<int> vv){
    vector<vector<pair<int,int>>> out;
    for(int r=0;r<9;r++){
        vector<pair<int,int>> ps; ps.push_back({vv[9],vv[r]});
        for(int i=1;i<5;i++) ps.push_back({vv[(r+i)%9],vv[(r-i+9)%9]});
        out.push_back(ps);
    }
    return out;
}
struct Slot{char typ;int z;};

using P12=array<unsigned char,12>;
P12 invp(const P12&p){P12 q;for(int i=0;i<12;i++)q[p[i]]=i;return q;}
P12 revc(const P12&p){P12 q;for(int i=0;i<12;i++)q[i]=11-p[11-i];return q;}
string enc(const P12&p){string s(12,'\0');for(int i=0;i<12;i++)s[i]=char(p[i]);return s;}

int main(int argc,char**argv){
    const double ELQ=-0.3617152614957746, ELA=0.6382847385042254;
    const double EHQ=0.2293817209459398, EHA=0.7667760747728821;
    const double EQ=-0.0661667702749174, EA=0.7025304066385537, ETQ=0.06944369427706908;
    vector<int> rem; for(int q=1;q<11;q++) rem.push_back(q); auto fac=factorization10(rem); int rhsround[5]={0,1,2,3,5};
    vector<array<Slot,11>> tils;
    for(int rr:rhsround){array<Slot,11> sl; int c=0; for(auto [a,b]:fac[0])sl[c++]={'L',a+b-10}; for(auto [a,b]:fac[rr])sl[c++]={'H',a+b-10}; sl[c++]={'V',-10}; tils.push_back(sl);}

    array<int,11> sig; iota(sig.begin(),sig.end(),0);
    long long total=0,unipass=0,unifail=0,fixedpass=0,adaptpass=0,remain=0; int min_unipass=1e9,max_unifail=-1e9; long long uses[5]={};
    unordered_set<Tup,TupHash> fixedtuples, adapttuples; unordered_set<string> reps;
    const int N=12, rhs=8*N*N*N*N;
    do{
        ++total; int half=0; int gp[12]; for(int i=0;i<11;i++)gp[i]=sig[i]; gp[11]=11;
        for(int i=0;i<N;i++) for(int j=i+1;j<N;j++){int d=i-j,e=gp[i]-gp[j];half += abs(d-e)*psi12(d+e);} int margin=5*(2*half)-rhs;
        if(margin>=0){++unipass;min_unipass=min(min_unipass,margin);continue;} ++unifail;max_unifail=max(max_unifail,margin);
        struct Br{int j,s,d;}; vector<Br> br; for(int j=0;j<11;j++)br.push_back({j,j+sig[j],j-sig[j]}); sort(br.begin(),br.end(),[](auto&x,auto&y){if(x.s!=y.s)return x.s<y.s;if(x.d!=y.d)return x.d<y.d;return x.j<y.j;});
        vector<Br> low(br.begin(),br.begin()+5),high(br.begin()+6,br.end());Br vert=br[5];sort(low.begin(),low.end(),[](auto&x,auto&y){return x.d<y.d;});sort(high.begin(),high.end(),[](auto&x,auto&y){return x.d<y.d;});int nums[5]={-9,-5,0,5,9};int CSL=0,CSH=0,ZL=0,ZH=0;for(int i=0;i<5;i++){CSL+=low[i].s;ZL+=low[i].d*nums[i];CSH+=high[i].s-2;ZH+=high[i].d*nums[i];}int sV=vert.s,ZV=0;
        double T=CSL*ELQ+CSH*EHQ+sV*EQ+(ZL/11.0)*ELA+(ZH/11.0)*EHA-200*ETQ;
        if(T>1e-12){++fixedpass;fixedtuples.insert({CSL,CSH,sV,ZL,ZH,ZV});continue;}
        int s[11],d[11];for(int j=0;j<11;j++){s[j]=j+sig[j];d[j]=j-sig[j];}bool ok=false;
        for(int ti=0;ti<5&&!ok;ti++){
            double C[11][11];auto&sl=tils[ti];for(int j=0;j<11;j++)for(int c=0;c<11;c++){double z=sl[c].z/11.0,score;if(sl[c].typ=='L')score=s[j]*ELQ+d[j]*z*ELA;else if(sl[c].typ=='H')score=(s[j]-2)*EHQ+d[j]*z*EHA;else score=s[j]*EQ+d[j]*z*EA;C[j][c]=-score;}
            int asg[11];hungarian11(C,asg);CSL=CSH=sV=ZL=ZH=ZV=0;for(int j=0;j<11;j++){auto slot=sl[asg[j]];if(slot.typ=='L'){CSL+=s[j];ZL+=d[j]*slot.z;}else if(slot.typ=='H'){CSH+=s[j]-2;ZH+=d[j]*slot.z;}else{sV=s[j];ZV=d[j]*slot.z;}}
            T=CSL*ELQ+CSH*EHQ+sV*EQ+(ZL/11.0)*ELA+(ZH/11.0)*EHA+(ZV/11.0)*EA-200*ETQ;
            if(T>1e-10){ok=true;++adaptpass;++uses[ti];adapttuples.insert({CSL,CSH,sV,ZL,ZH,ZV});}
        }
        if(ok)continue;
        ++remain;P12 p;for(int i=0;i<11;i++)p[i]=sig[i];p[11]=11;P12 a=invp(p),b=revc(p),c=invp(b);P12 best=min(min(p,a),min(b,c));reps.insert(enc(best));
    }while(next_permutation(sig.begin(),sig.end()));

    if(argc>=4){
        ofstream f1(argv[1]), f2(argv[2]), f3(argv[3]);
        for(const auto &k: fixedtuples) f1<<k.a<<","<<k.b<<","<<k.c<<","<<k.d<<","<<k.e<<","<<k.f<<"\n";
        for(const auto &k: adapttuples) f2<<k.a<<","<<k.b<<","<<k.c<<","<<k.d<<","<<k.e<<","<<k.f<<"\n";
        for(const auto &s0: reps){ for(int i=0;i<12;i++){ if(i) f3<<","; f3<<(int)(unsigned char)s0[i]; } f3<<"\n"; }
    }
    cout<<"total="<<total<<"\n";
    cout<<"universal_pass="<<unipass<<" universal_fail="<<unifail<<" min_pass="<<min_unipass<<" max_fail="<<max_unifail<<"\n";
    cout<<"fixed_pass="<<fixedpass<<" fixed_unique_tuples="<<fixedtuples.size()<<"\n";
    cout<<"adaptive_pass="<<adaptpass<<" uses=";for(int i=0;i<5;i++)cout<<(i?",":"")<<uses[i];cout<<" adaptive_unique_tuples="<<adapttuples.size()<<"\n";
    cout<<"remain="<<remain<<" canonical_reps="<<reps.size()<<"\n";
    if(total!=39916800LL||unipass!=39049390LL||unifail!=867410LL||min_unipass!=2||max_unifail!=-8||fixedpass!=610996LL||fixedtuples.size()!=49641||adaptpass!=8820LL||adapttuples.size()!=453||remain!=247594LL||reps.size()!=144834){cerr<<"ASSERTION FAILURE\n";return 3;}
    cout<<"EXACT/LOCATOR S11 N12 PHASE1+DOMINO CENSUS PASSED\n";
    return 0;
}
