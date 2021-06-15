#include <bits/stdc++.h>
#include <iostream>

using namespace std;

const int sizen = 4;

//Initialisng variables
long long CostMatrixAA[sizen][sizen];
long long CostMatrixBB[sizen][sizen];
long long CostMatrixA[sizen][sizen];
long long CostMatrixB[sizen][sizen];
long long A[sizen][sizen];
long long B[sizen][sizen];
long long AA[sizen][sizen];
long long BB[sizen][sizen];
long long productMat[sizen][sizen];

//Function to store the minimum cost of reaching cell n,n from that cell.
long long FindMinCostA(int i, int j, int n)
{
    A[0][0]=CostMatrixA[0][0];
    int count=0;
    for(int i=1;i<sizen;i++)
    {
        for(int j=1;j<sizen;j++)
      {
          //Initialise cells to zero
          A[i][j]=0;
          if(count<4)
          {
              //initialise  cells to 0
               A[0][j]=0;
               A[j][0]=0;
               //To store the cost values of first row and first column cells.
               A[j][0]=CostMatrixA[j][0]+A[j-1][0];
               A[0][j]=CostMatrixA[0][j]+A[0][j-1];
          }
          count++;
        //To find the minimum cost
          A[i][j]=min(A[i-1][j],A[i][j-1])+CostMatrixA[i][j];
          
      }
    }
    // To invert the matrix as the cost matrix has initially been inverted to find the cost
    for(int i=0;i<sizen;i++)
    {
        for(int j=0;j<sizen;j++)
        {
            AA[i][j]=A[sizen-i-1][sizen-1-j];
        }
    }
    
    return A[3][3];
}
//Function to store the maximum cost of reaching cell n,n from that cell.
long long FindMaxCostB(int i, int j, int n)
{
    B[0][0]=CostMatrixB[0][0];
    int count=0;
    for(int i=1;i<sizen;i++)
    {
        for(int j=1;j<sizen;j++)
      {
          
          //Initialise cells to zero
          B[i][j]=0;
          if(count<4)
          {
              //initialise  cells to 0
               B[0][j]=0;
               B[j][0]=0;
               //To store the cost values of first row and first column cells.
               B[j][0]=CostMatrixB[j][0]+B[j-1][0];
               B[0][j]=CostMatrixB[0][j]+B[0][j-1];
          }
          count++;
           //To find the maximum cost
          B[i][j]=max(B[i-1][j],B[i][j-1])+CostMatrixB[i][j];
      }
    }
    // To invert the matrix as the cost matrix has initially been inverted to find the cost
    for(int i=0;i<sizen;i++)
    {
        for(int j=0;j<sizen;j++)
        {
            BB[i][j]=B[sizen-i-1][sizen-1-j];
        }
    }
    
    return B[3][3];
}
int main()
{
    int t;
    int s;
    //Initialising cost matrices
    long long filterArray[4][sizen]; 
     for (int i = 0; i < sizen; i++)
    {
        for (int j = 0; j < sizen; j++)
        {
            t=1 + rand() % 10;
            s=1 + rand() % 10;
            CostMatrixAA[i][j]=t;
            CostMatrixA[sizen-1-i][sizen-1-j]=t;
            CostMatrixBB[i][j]=s;
            CostMatrixB[sizen-1-i][sizen-1-j]=s;
            filterArray[i][j] = rand() % 2;

        }
    }
    // Calling the function
   printf(" %lld\n", FindMinCostA(0, 0, sizen));
   printf(" %lld\n", FindMaxCostB(0, 0, sizen));
   long long int temp1,temp2;
   //Declaring product matrix
   for (int  k= 0; k < sizen; k++)
    {
        for (int j = 0; j < sizen; j++)
        {
            for (int i = 0; i < sizen; i++)
                {
                    temp1=AA[i][k];
                    temp2=BB[k][j];
                    productMat[i][j] += temp1*temp2;
                }
        }

    }
}
