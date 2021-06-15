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


#pragma omp simd
  long long finalMat[sizen / 4];
   // applying the filter
  for (int i = 0; i < sizen - 4; i += 4)
  {
    long long sum = 0;
     // dot product of 4xn portion of productMat
     for (int j = 0; j < sizen; j++)
     {
        for (int filterRow = 0; filterRow < 4; filterRow++)
        {
            sum += productMat[i + filterRow][j];
        }
      }
     finalMat[i / 4] = sum;
  }
