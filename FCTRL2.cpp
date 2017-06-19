#include<bits/stdc++.h>
#define ll long long
using namespace std;

vector<ll> fact;

int main()
{
    ll T,n;

    cin>>T;

    while(T--){
        cin>>n;
        //cout<<tgamma(n+1);
        fact.push_back(tgamma(n+1));
        if(T!=0)
            cout<<endl;
    }

    for(ll i =0;i<fact.size();i++)
        cout<<fact[i]<<endl;

    return 0;
}
