#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
using U=uint64_t;
int pc(U x){return __builtin_popcountll(x);}
struct Stats {double H=0,I=0,sumE=0,m=1e100; array<double,6> inf{},er{},w2{};};
Stats metrics(U f,int n,bool monotone=true){int N=1<<n; array<int,64>a{}; for(int x=0;x<N;x++) a[x]=((f>>x)&1)?1:-1;
for(int h=1;h<N;h*=2)for(int x=0;x<N;x+=2*h)for(int t=0;t<h;t++){int p=a[x+t],q=a[x+t+h];a[x+t]=p+q;a[x+t+h]=p-q;}
array<double,64> mu{};Stats s;int norm=0;
for(int x=0;x<N;x++){norm+=a[x]*a[x];mu[x]=double(a[x]*a[x])/(N*N);if(mu[x])s.H-=mu[x]*log2(mu[x]);for(int i=0;i<n;i++)if(x>>i&1){s.inf[i]+=mu[x];if(pc(x)==2)s.w2[i]+=mu[x];}}
assert(norm==N*N);
for(int i=0;i<n;i++){int edges=0;for(int x=0;x<N;x++)if(!(x>>i&1)){double p=mu[x],q=mu[x|(1<<i)],z=p+q;if(p>0)s.er[i]-=p*log2(p/z);if(q>0)s.er[i]-=q*log2(q/z);edges+=((f>>x)&1)!=((f>>(x|(1<<i)))&1);}
assert(abs(s.inf[i]-double(edges)/(N/2))<1e-12);if(monotone)assert(abs(abs(double(a[1<<i])/N)-s.inf[i])<1e-12);s.I+=s.inf[i];s.sumE+=s.er[i];if(s.inf[i])s.m=min(s.m,s.er[i]/s.inf[i]);}
assert(s.sumE<=s.H+1e-10);return s;}
string dnf(U f,int n){string z="";int N=1<<n;for(int x=0;x<N;x++)if(f>>x&1){bool m=true;for(int i=0;i<n;i++)if((x>>i&1)&&(f>>(x^(1<<i))&1))m=false;if(m){if(z.size())z+="|";z+=to_string(x);}}return z;}
vector<U> gen(int n){if(!n)return {0,1};auto v=gen(n-1);vector<U>out;for(U a:v)for(U b:v)if((a&~b)==0)out.push_back(a|(b<<(1<<(n-1))));sort(out.begin(),out.end());return out;}
struct Perm {array<array<U,256>,8> t{};};
void census(int n){int N=1<<n;auto v=gen(n-1);int L=v.size(),half=N/2;unordered_map<U,int>idx;for(int i=0;i<L;i++)idx[v[i]]=i;
vector<uint8_t> seen((size_t(L)*L+7)/8);vector<Perm>ps;vector<int>p(n);iota(p.begin(),p.end(),0);do{Perm pp;for(int chunk=0;chunk<(N+7)/8;chunk++)for(int b=0;b<256;b++){U y=0;for(int j=0;j<8;j++)if(b>>j&1){int x=chunk*8+j;if(x>=N)continue;int xx=0;for(int i=0;i<n;i++)if(x>>i&1)xx|=1<<p[i];y|=U(1)<<xx;}pp.t[chunk][b]=y;}ps.push_back(pp);}while(next_permutation(p.begin(),p.end()));
ofstream out("census_n"+to_string(n)+".csv");out<<setprecision(17)<<"truth_hex,orbit,H,I,sumE,minratio,inf,erasure,w2,minterms,maxterms,rule_maxInf,rule_minInf,rule_shortest,rule_minW2,rule_maxW2,rule_term_clause\n";
long long total=0,classes=0,orbit_total=0;U mask=half==64?~U(0):(U(1)<<half)-1;
for(int ai=0;ai<L;ai++)for(int bi=0;bi<L;bi++){if(v[ai]&~v[bi])continue;total++;size_t key=size_t(ai)*L+bi;if(seen[key/8]>>(key%8)&1)continue;U f=v[ai]|(v[bi]<<half);int orbit=0;
for(auto &pp:ps){U g=0;for(int j=0;j<(N+7)/8;j++)g|=pp.t[j][(f>>(j*8))&255];auto ia=idx.find(g&mask),ib=idx.find(g>>half);assert(ia!=idx.end()&&ib!=idx.end());size_t k=size_t(ia->second)*L+ib->second;if(!(seen[k/8]>>(k%8)&1)){orbit++;seen[k/8]|=1<<(k%8);}}
classes++;orbit_total+=orbit;if(f==0||f==(n==6?~U(0):(U(1)<<N)-1)){out<<hex<<f<<dec<<","<<orbit<<",0,0,0,0,,,,,,,,,,,\n";continue;}
auto s=metrics(f,n);vector<int>terms,clauses;int dt=100,dc=100;for(int x=0;x<N;x++){if(f>>x&1){bool m=true;for(int i=0;i<n;i++)if((x>>i&1)&&(f>>(x^(1<<i))&1))m=false;if(m){terms.push_back(x);dt=min(dt,pc(x));}}else{bool m=true;for(int i=0;i<n;i++)if(!(x>>i&1)&&!(f>>(x|(1<<i))&1))m=false;if(m){clauses.push_back((N-1)^x);dc=min(dc,pc((N-1)^x));}}}
array<int,6> ct{};int tu=0,cu=0;for(int t:terms)if(pc(t)==dt){tu|=t;for(int i=0;i<n;i++)if(t>>i&1)ct[i]++;}for(int c:clauses)if(pc(c)==dc)cu|=c;
array<double,6>rules{};double maxinf=*max_element(s.inf.begin(),s.inf.begin()+n),mininf=1e100,minw=1e100,maxw=-1;int maxct=*max_element(ct.begin(),ct.begin()+n);for(int i=0;i<n;i++)if(s.inf[i]){mininf=min(mininf,s.inf[i]);minw=min(minw,s.w2[i]/s.inf[i]);maxw=max(maxw,s.w2[i]/s.inf[i]);}rules[5]=1e100;
for(int i=0;i<n;i++)if(s.inf[i]){double r=s.er[i]/s.inf[i],w=s.w2[i]/s.inf[i];if(abs(s.inf[i]-maxinf)<1e-12)rules[0]=max(rules[0],r);if(abs(s.inf[i]-mininf)<1e-12)rules[1]=max(rules[1],r);if(ct[i]==maxct)rules[2]=max(rules[2],r);if(abs(w-minw)<1e-12)rules[3]=max(rules[3],r);if(abs(w-maxw)<1e-12)rules[4]=max(rules[4],r);if((tu&cu)>>i&1)rules[5]=min(rules[5],r);}
assert(rules[5]<1e99);out<<hex<<f<<dec<<","<<orbit<<","<<s.H<<","<<s.I<<","<<s.sumE<<","<<s.m<<",";for(auto a:{s.inf,s.er,s.w2}){for(int i=0;i<n;i++){if(i)out<<"|";out<<a[i];}out<<",";}out<<dnf(f,n)<<",";for(int j=0;j<(int)clauses.size();j++){if(j)out<<"|";out<<clauses[j];}for(double r:rules)out<<","<<r;out<<"\n";
}
assert(total==orbit_total);cout<<"n="<<n<<" labelled="<<total<<" classes="<<classes<<" orbit_sum="<<orbit_total<<endl;}
void unrestricted(int n){int N=1<<n;U end=U(1)<<(N-1);double vals[3]={-1,-1,-1};U fs[3]{};for(U f=1;f<end;f++){auto s=metrics(f,n,false);double q[]={s.m,s.H/s.I,s.sumE/s.I};for(int j=0;j<3;j++)if(q[j]>vals[j]){vals[j]=q[j];fs[j]=f;}}cout<<setprecision(17)<<"unrestricted n="<<n;for(int j=0;j<3;j++)cout<<" "<<vals[j]<<"@"<<hex<<fs[j]<<dec;cout<<endl;}
int main(int argc,char**argv){if(argc>1&&string(argv[1])=="npn"){for(int n=1;n<=5;n++){ifstream in("../FEIB12/npn"+to_string(n)+".bin",ios::binary);assert(in);uint32_t f;long long count=0;double val[3]={-1,-1,-1};U fs[3]{};while(in.read((char*)&f,4)){count++;auto st=metrics(f,n,false);if(st.I==0)continue;double q[]={st.m,st.H/st.I,st.sumE/st.I};for(int j=0;j<3;j++)if(q[j]>val[j]+1e-13){val[j]=q[j];fs[j]=f;}}cout<<setprecision(17)<<"npn n="<<n<<" classes="<<count;for(int j=0;j<3;j++)cout<<" "<<val[j]<<"@"<<hex<<fs[j]<<dec;cout<<endl;}return 0;}if(argc>1&&string(argv[1])=="unrestricted"){for(int n=1;n<=4;n++)unrestricted(n);return 0;}for(int n=1;n<=6;n++)census(n);}
