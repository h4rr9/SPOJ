#include<bits/stdc++.h>
#define ll long long

using namespace std;

int main()
{
    ll b=0,x,c=1,i=0;
    char a[10];

    scanf("%s",a);

    while(a[i]!='\0')
    {
        b+= (a[i]-48)*(a[i]-48);
        i++;
    }
    while(b > 9)
    {
        x=0;

        while(b>0)
        {
             x+=(b%10) * (b%10);
             b/=10;
        }

        b=x;
        c++;
    }

    if(b==1)
        printf("%d",c);
    else
        printf("-1");

    return 0;
}
