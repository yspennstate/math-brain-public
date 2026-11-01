#include <boost/dynamic_bitset.hpp>
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <numeric>
using boost::dynamic_bitset;

static bool isprime(int n){ if(n<2)return false; if(n%2==0)return n==2; for(int d=3;1LL*d*d<=n;d+=2)if(n%d==0)return false; return true; }

struct Graph { int p; std::vector<int> verts; std::vector<dynamic_bitset<>> adj; };

Graph build_graph(int p){
 std::vector<char> qr(p,0); for(int x=1;x<p;x++) qr[(long long)x*x%p]=1;
 std::vector<int> v; for(int x=2;x<p;x++) if(qr[x] && qr[(x-1+p)%p]) v.push_back(x);
 int n=v.size(); std::vector<dynamic_bitset<>> adj(n,dynamic_bitset<>(n));
 for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) if(qr[(v[i]-v[j]+p)%p]) {adj[i].set(j);adj[j].set(i);} 
 return {p,std::move(v),std::move(adj)};
}

struct ColorResult { std::vector<int> order, color; };
ColorResult color_sort(dynamic_bitset<> P, const std::vector<dynamic_bitset<>>& adj){
 ColorResult r; int c=0; dynamic_bitset<> U=P;
 while(U.any()){
   ++c; dynamic_bitset<> Q=U;
   while(Q.any()){
     auto v=Q.find_first();
     r.order.push_back((int)v); r.color.push_back(c);
     U.reset(v); Q.reset(v); Q &= ~adj[v];
   }
 }
 return r;
}

struct MaxSolver{
 const std::vector<dynamic_bitset<>>& adj; int best=0; dynamic_bitset<> bestbits; uint64_t nodes=0;
 MaxSolver(const std::vector<dynamic_bitset<>>& a):adj(a),bestbits(a.size()){}
 void rec(int rs, dynamic_bitset<> rb, dynamic_bitset<> P){
   ++nodes;
   if(P.none()){ if(rs>best){best=rs;bestbits=rb;} return; }
   auto cr=color_sort(P,adj);
   for(int i=(int)cr.order.size()-1;i>=0;--i){
     if(rs+cr.color[i]<=best) return;
     int v=cr.order[i]; if(!P.test(v)) continue;
     auto P2=P & adj[v]; auto rb2=rb; rb2.set(v);
     rec(rs+1,std::move(rb2),std::move(P2)); P.reset(v);
   }
 }
 void run(){ dynamic_bitset<> P(adj.size()); P.set(); dynamic_bitset<> R(adj.size()); rec(0,std::move(R),std::move(P)); }
};

static uint64_t mix64(uint64_t h, uint64_t x){
 x += 0x9e3779b97f4a7c15ULL; x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL; x=(x^(x>>27))*0x94d049bb133111ebULL; x ^= x>>31; h ^= x + 0x9e3779b97f4a7c15ULL + (h<<6)+(h>>2); return h;
}
static uint64_t hash_bits(uint64_t h, const dynamic_bitset<>& P){
 std::vector<unsigned long> blocks(P.num_blocks()); boost::to_block_range(P,blocks.begin());
 h=mix64(h,P.size()); for(auto b:blocks) h=mix64(h,(uint64_t)b); return h;
}
struct DecisionSolver{
 const std::vector<dynamic_bitset<>>& adj; uint64_t nodes=0, prunes=0, leaves=0, hash=0x123456789abcdef0ULL;
 DecisionSolver(const std::vector<dynamic_bitset<>>& a):adj(a){}
 void event(uint64_t tag,int need,const dynamic_bitset<>& P,uint64_t extra=0){hash=mix64(hash,tag);hash=mix64(hash,(uint64_t)need);hash=hash_bits(hash,P);hash=mix64(hash,extra);}
 bool rec(dynamic_bitset<> P,int need){
   ++nodes;
   if(need<=0){ event(1,need,P); return true; }
   if(P.count() < (size_t)need){ ++prunes; event(2,need,P,P.count()); return false; }
   auto cr=color_sort(P,adj);
   if(cr.color.empty() || cr.color.back()<need){ ++prunes; event(3,need,P,cr.color.empty()?0:cr.color.back()); return false; }
   for(int i=(int)cr.order.size()-1;i>=0;--i){
     if(cr.color[i]<need){ ++prunes; event(4,need,P,cr.color[i]); return false; }
     int v=cr.order[i]; if(!P.test(v)) continue;
     event(5,need,P,(uint64_t)v);
     if(rec(P & adj[v], need-1)) return true;
     P.reset(v);
   }
   ++leaves; event(6,need,P); return false;
 }
 bool run(int t){ dynamic_bitset<> P(adj.size()); P.set(); return rec(std::move(P),t); }
};

bool clique_check(const Graph& g,const std::vector<int>& W){
 std::vector<char> qr(g.p,0); for(int x=1;x<g.p;x++) qr[(long long)x*x%g.p]=1;
 for(size_t i=0;i<W.size();i++) for(size_t j=0;j<i;j++) if(!qr[(W[i]-W[j]+g.p)%g.p]) return false; return true;
}

int main(int argc,char**argv){ int Pmax=1601; int Pmin=5; if(argc>1)Pmax=std::stoi(argv[1]); if(argc>2)Pmin=std::stoi(argv[2]);
 auto start=std::chrono::steady_clock::now(); int count=0;
 std::cout << "PALey exact certificate archive v1\n";
 std::cout << "Pmax="<<Pmax<<"\n";
 int first=Pmin; while(first%4!=1) ++first; for(int p=first;p<=Pmax;p+=4){ if(!isprime(p)) continue; ++count; auto g=build_graph(p); MaxSolver ms(g.adj); ms.run(); int omega=ms.best+2;
   std::vector<int> W={0,1}; for(size_t i=0;i<g.verts.size();i++) if(ms.bestbits.test(i)) W.push_back(g.verts[i]);
   if(!clique_check(g,W) || (int)W.size()!=omega){ std::cerr<<"witness_fail p="<<p<<"\n"; return 2; }
   int targetH=omega-1; DecisionSolver ds(g.adj); bool found=ds.run(targetH); if(found){std::cerr<<"decision_fail p="<<p<<"\n";return 3;}
   std::cout << "p="<<p<<" omega="<<omega<<" Hn="<<g.verts.size()<<" witness=";
   for(size_t i=0;i<W.size();i++){if(i)std::cout<<",";std::cout<<W[i];}
   std::cout<<" exclude="<<(omega+1)<<" targetH="<<targetH<<" max_nodes="<<ms.nodes<<" no_nodes="<<ds.nodes<<" prunes="<<ds.prunes<<" leaves="<<ds.leaves<<" proof64="<<std::hex<<ds.hash<<std::dec<<"\n";
 }
 auto sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
 std::cout<<"SUMMARY count="<<count<<" cutoff="<<Pmax<<" all_witnesses_pass=1 all_one_larger_exclusions_pass=1 seconds="<<sec<<"\n";
}
