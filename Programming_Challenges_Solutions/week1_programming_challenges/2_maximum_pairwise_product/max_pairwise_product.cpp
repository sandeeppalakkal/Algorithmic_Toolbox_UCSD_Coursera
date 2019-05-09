#include <iostream>
using namespace std;

long long min(long long a, long long b)
{
    if(a < b) return a;
    else return b;
}

long long max(long long a, long long b)
{
    if(a > b) return a;
    else return b;
}

long long max_product(long long *a, int n)
{
    long long max1, max2;
    max1 = max(a[0],a[1]);
    max2 = min(a[0],a[1]);

    for(int i = 2; i < n; ++i)
    {
        if(a[i] <= max2) continue;
        else if(a[i] > max1)
        {
            max2 = max1;
            max1 = a[i];
        }
        else
        {
            max2 = a[i];
        }
    }
    return max1 * max2;
}

int main()
{
    int n;
    long long *num;
    cin >> n;
    num = new long long[n];
    //Read array
    for(int i=0; i < n; ++i)
    {
        cin >> num[i];
    }

    //Computer max product
    long long max_prod = max_product(num,n);
    cout << max_prod << endl;

    delete[] num;
    return 0;
}
