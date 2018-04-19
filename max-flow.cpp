//written by Meghana Kumar




/*

A Big E-Commerce retail company sells a large variety of different items. Since Big Batchsnaps'18 Sale is going on, so they often run out of popular items, making customers sad. To minimize sadness, The newly hired intern from BITS is implementing a sophisticated product-ordering system. Customers text in their acceptable choices. Then they can use an algorithm to assign the preferred products to customers. Customers who do not get one of their choices should receive a Rs.100 voucher. Our intern would like to minimize the number of vouchers they give out and must beat the other tech-savvy geniuses to get the PPO!!. Since the intern is good with mathematics and algorithms but not so pro in coding could you help him/her complete the task.

In general, suppose that, on a given day, the company has m types of items b1, . . . , bm, and the quantity of each type item bj is exactly qj. Suppose that n customers a1, . . . , an text in their preferences, where each customer ai submits a set Ai of one or more acceptable product choices. The algorithm should assign each customer either one of his/her choices or a Rs. 100 voucher. It should minimize the number of vouchers.

(Note: Model this as a max flow problem.)

Input:

First line contains number of items. I

Second line contains number of customers. C

Third line contains quantity of each of the item. QI

In next C lines, ith line has a set which tells items preferred by ith customer.(Each line is terminated with -1)

Output:

Total amount in Rupees the company has to give to its customers as vouchers

*/



#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <cstdlib>
#include <limits.h>
#include <string.h>
#include <queue>
using namespace std;
int bfs(int **residual, int source, int sink, int parent[], int I,int C)
{
    int V = I+C+2;
    int visited[V];
    memset(visited, 0, sizeof(visited));
    queue <int> q;
    q.push(source);
    visited[source] = 1;
    parent[source] = -1;

    while (!q.empty())
    {
        int x = q.front();
        q.pop();
 
        for (int y=0; y<V; y++)
        {
            if (visited[y]==0 && residual[x][y] > 0)
            {
                q.push(y);
                parent[y] = x;
                visited[y] = 1;
            }
        }
    }
 	if(visited[sink]) return 1;
 	else return 0;
   
}
 
int maxBipartateMatching(int **pref, int source, int sink, int I, int C)
{ 
	int V = I+C+2;
 
    int **residual;
  	residual = new int *[V];
  	for(int x = 0; x <V; x++)
    	residual[x] = new int[V];  
    for (int x = 0; x < V; x++)
        for (int y = 0; y < V; y++)
             residual[x][y] = pref[x][y];
 
    int parent[V];  
 	
    int flow = 0;  
 	int x;
    while (bfs(residual, source, sink, parent, I, C))
    {
 
        int path = INT_MAX;
        for (int y=sink; y!=source; y=parent[y])
        {
            x = parent[y];
            path = min(path, residual[x][y]);
        }

        for (int y=sink; y != source; y=parent[y])
        {
            x = parent[y];
            residual[x][y] -= path;
            residual[y][x] += path;
        }

       flow += path;
    }
 
    return flow;
}
int main()
{

	int i, c;
  	cin >> i >> c;
  	int **pref;
  	pref = new int *[c+i+2];
	for(int x = 0; x <c+i+2; x++)
	      pref[x] = new int[c+i+2];
  	for(int x=1;x<c+1;x++)
  		pref[0][x] = 1;
  	int items[i];
  	for(int j=0;j<i;j++)
  		cin >> pref[c+1+j][c+i+1];
  	int temp;
  	for(int j=0;j<c;j++)
 	{
  		cin >> temp;
  		while(temp!=-1)
  		{
  			pref[j+1][c+temp] = 1;
  			cin >> temp;
  		}
  	}
 	/*for(int x=0;x<c+i+2;x++)
 	{
 		for(int y=0;y<c+i+2;y++)
 			cout << pref[x][y] << " ";
 		cout << endl;
 	}

	*/
	int flow = maxBipartateMatching(pref, 0, i+c+1, i, c);
	cout << (c-flow)*100;
  	return 0;
}