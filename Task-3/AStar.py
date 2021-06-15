import numpy as np
import cv2
import collections
import heapq


'''
Why use heap?
The heap implementation ensures time complexity is logarithmic. Thus push/pop operations are
proportional to  the base-2 Logarithm of number of elements.
Implementation is through a binary tree (Just like a sieve!)
Heap property: Value of node is always smaller than both of its children unlike a binary search tree.
'''
import queue
import time
import pandas as pd
 
'''
Why Priority Queue?
Because here we have to decide the priority. So what if we had a queue that adjusts the priority for us!
Earlier attempt was to use a list/collection of nodes and find out the minimum. But the time complexity increases in that case.
'''
#Appendix:
#Diagonal Distance=1
#Dijkstra=2
#Euclidean=3
#H1=4   ...A non-admissible Heuristic.
#Manhattan=5


#Appendix:
choice=3 # Heuristic_type
choice2=2 # Travel_selection
''' 
Choice2=1 means diagonal movement allowed
Choice2=2 means diagonal movement not allowed
'''
choice3=1  # Cost_selection
'''
Choice3=1 means normal given cost
Choice3=2 valid for only Choice2=2
It is a cost method developed assuming that a bot takes some time to turn.
It is designed so that the bot will prefer to go straight (According to the path along which it has entered the current node)
'''

heuristic=['Diagonal Distance','Dijkstra','Euclidean','H1','Manhattan']
#For documentation
write_path='a a astar.txt'
#Read Image Path
img_path='C:/Research Group/Dilation_1.jpg'
#img_path='sample_for_Astar.png'

#Write Image Path
img_write_path='AStar_'+str(choice)+'_'+heuristic[choice-1]+'_'+'Case-'+str(choice2)
if(choice2==2 and choice3==2):
    img_write_path=img_write_path+'_2'
img_write_path=img_write_path+'.png'

#Written as variables so that making changes in code according to the need become easy 

wait=10000
#Define color parameters
ob_color = [255,255,255]
np_color =[0,0,0]
path_pointer=[255,255,0]
start=(139,60)
end=(141,420)


#Read Image
img = cv2.imread(img_path,cv2.IMREAD_COLOR)
#Calculate image size before search
h,w,c = img.shape


#Calculate Heuristic Func
def calcHeuristic(point1,point2=None,startpt=None,endpt=None):

    '''
 Calculates Heuristic Function according to the global choice selected.\n
 Calculates the Heuristic between points point1 and point2
 choice==1 Diagonal Distance\n
 returns max(abs(point1[0] - point2[0]),abs(point1[1] - point2[1]))\n
 choice==2 Dijkstra\n
 returns 0 (No Heuristic)\n
 Choice==3 Euclidean=3\n
 returns ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5\n
 Can delete **0.5 according to need\n
 Choice==4 H1   ...A non-admissible Heuristic.\n
 H1 is a non-Admissible Heuristic.\n Based on distance between point and a line.\nWorks well with no obstacles\n
 Choice==5 Manhattan\n
 returns abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])\n
 @param startpt and endpt required for H1\n
    '''
    if(choice==1):
        return max(abs(point1[0] - point2[0]),abs(point1[1] - point2[1]))

    if(choice==2):
        return 0

    if(choice==3):
        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5 

    if(choice==4):
        a=start[1]-end[1]
        b=end[0]-start[0]
        c=start[0]*end[1]-start[1]*end[0]
        if(a*point1[0]+b*point1[1]+c==0):
            return -10
        return abs(a*point1[0]+b*point1[1]+c) 

    if(choice==5):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])




def calcCost(point1,point2):
    ''' 
    Calculates cost
    '''
    if(abs(point1[0]-point2[0])==1 and abs(point1[1]-point2[1])==0):
        return 1.0
    if(abs(point1[0]-point2[0])==1 and abs(point1[1]-point2[1])==1):
        return 1.41421356237      #define square root of 2
    if(abs(point1[0]-point2[0])==0 and abs(point1[1]-point2[1])==1):
        return 1.0
    if(abs(point1[0]-point2[0])==0 and abs(point1[1]-point2[1])==0):
        return 0.0
    else:
      return np.inf




def calcCost2(child,current,start,parent=None): 
    '''
    Special cost function\n
    based on real runtime situation.\n
    Accounts time taken for turning by the bot\n
    '''
    point1=child.position
    point2=current.position
    start_point=start.position
    if not (point2[0]==start_point[0] and point2[1]==start_point[1]):
        parent_point=parent.position
        if(float(point2[0])==(point1[0]+parent_point[0])/2 and float(point2[1])==(point1[1]+parent_point[1])/2 ):
            return 1
        if(parent_point[0]==point1[0] and parent_point[1]==point1[1]):
            return 3
        if(point1[0]==point2[0] and point1[1]==point2[1]):
            return 0
        else:
            return 2
    else:
     if(abs(point1[0]-point2[0])==1 and abs(point1[1]-point2[1])==0):
         return 1
     if(abs(point1[0]-point2[0])==0 and abs(point1[1]-point2[1])==1):
         return 1
     if(abs(point1[0]-point2[0])==0 and abs(point1[1]-point2[1])==0):
         return 0




#check for navigation path
def isinrange(img,position):
    '''
    Returns False if given node is not accessible
    \nElse returns True
    '''
    b=False
    x=position[0]
    y=position[1]
    ob_color = [255,255,255]
    if(x>=0 and x<img.shape[0] and y >=0 and y<img.shape[1]):
        b=True
        if(img[x,y,0] ==ob_color[0] and img[x,y,1] ==ob_color[1] and img[x,y,2] ==ob_color[2]):
           b=False
    return b



# class for handling priority queues 
class PriorityQueue :
    '''
    creates a Queue Class
    '''

    def __init__(self):
        '''
        Creates a queue
        '''
        self.Queue=[]

    def isempty(self):
        '''
        Checks if given Queue is empty.
        \nReturns True if Empty
        '''
        if not self.Queue:
            return 1
        else:
             return 0
    
    def put(self,index):
        '''
        Puts given element onto the queue
        \nUses heapq.heappush for faster aproach.
        '''
        heapq.heappush(self.Queue,index)

    def get(self):
        '''
        Returns the smallest-in-priority element using heapq.heappop
        \n\nComparison based on __lt__ and __gt__ of node class
        '''
        #print(self.Queue)
        return heapq.heappop(self.Queue)




class node:
    '''
    class for handling nodes\n
    @param index=input default=None\nstands for position\n
    @param is_in_list and is_current are check-points\n
    @param parent=input default=None\n
    @param f,g,h=cost\n
    @param h stands for Heuristic cost\n
    @param f stands for total cost
    '''
    #constructor
    def __init__(self,index=None,parent=None):
        # Initialise params
        self.position=index  #position/location
        self.is_in_list=False  # chkpt
        self.is_current=False  #chkpt
        self.parent=parent     #parent node of the node
                                  # __
        self.f=np.inf             #   |
        self.g=np.inf             #   | initialise cost
        self.h=np.inf             # __|
        self.isvisted=False
    
    def __lt__(self,other):
     '''
     overload operator < (chk parameter=cost)
     '''
     return self.f<other.f
    
    def __gt__(self,other):
     '''
     overload operator > (chk parameter=cost)
     '''
     return self.f>other.f





#get neighbourhood according to choice2
def get_nbd(current):
    '''
    returns list of neighbourhood positions
    \nchoice is made based on choice2
    '''
    l=[]

    if(choice2==1):
     for i in range(-1,2):
         for j in range(-1,2):
             position=(current.position[0]+i,current.position[1]+j)
             if (isinrange(img,position)==True):
                 l.append(position) 

    if(choice2==2):
     for i in range(-1,2):
         position=(current.position[0]+i,current.position[1])
         if (isinrange(img,position)==True):
                l.append(position)
     for j in range(-1,2):
         if(j==0): #skip repetition
             continue
         position=(current.position[0],current.position[1]+j)
         if (isinrange(img,position)==True):
             l.append(position) 
          
    return l


# create a matrix/dict of objects
node_matrix=np.empty((h,w),dtype=object)
#node_matrix=collections.defaultdict(node)
for i in range(h):
    for j in range(w):
        node_matrix[i,j]=node()
        node_matrix[i,j].position=(i,j)



#main function
def main_func(img,startpt,endpt):
    '''
    The main traversing function\n
    returns time taken for traversing
    '''
    #create lists 
    visited=[]
    path=[]

    h,w,c=img.shape

    #create priority queue 
    pt_list=PriorityQueue()
    
    #Initialise start node
    start=node(startpt)
    start.g=0
    start.f=start.h=calcHeuristic(start.position,endpt)
    start.isvisted=True
    node_matrix[startpt]=start
    pt_list.put(start)

    #Start Traversing
    beg=time.time()


    while(not pt_list.isempty()):

        #while the list is not empty obtain the node with smallest f

        current=pt_list.get()

        #Now that current node is not in the list change the corresponding chkpts

        current.is_in_list=False
        current.is_current=True

        #Now to preserve the node use the matrix

        node_matrix[current.position]=current

        #break condition

        if(current.position==endpt):
            break

        #get the neighbourhood points

        nbd_list=get_nbd(current)

        # searching operation 

        for pos in nbd_list:
            # earlier attempt was to use a list of objects. But finally dealing with position.

            nbd=node_matrix[pos]

            #get the temp_cost 

            if(choice2==2 and choice3==2):
                g_temp=current.g+calcCost2(nbd,current,start,current.parent)
            else:
                g_temp=current.g+calcCost(pos,current.position)
            
            # if this newly calculated cost< the stored cost-
            if(g_temp<nbd.g):

                #make note that it is visited

                nbd.isvisted=True

                #if the point is current and the new cost is less than its stored cost-
                #make the current as it's parent and put the nbd node in the pt_list. 
    
                if nbd.is_current:
                    nbd.is_current=False
                    nbd.parent=current
                    nbd.g=g_temp
                    nbd.h=calcHeuristic(nbd.position,endpt)
                    nbd.f=nbd.g+nbd.h
                    nbd.is_in_list=True
                    pt_list.put(nbd)

                # if the nbd node is not current- then put the nbd node in the pt_list (if it is not there) along with setting the chk_points.
                else:
                    nbd.parent=current
                    nbd.g=g_temp
                    nbd.h=calcHeuristic(nbd.position,endpt)
                    nbd.f=nbd.g+nbd.h
                    if(not nbd.is_in_list):
                        pt_list.put(nbd)
                    nbd.is_in_list=True
                    nbd.is_current=False  #Just for ensuring 

        # to display progress  ************************
        #showPath(img,current,start=start,is_end=False)
        #cv2.waitKey(1)


    # finish traversing   
    finish=time.time()
    print(round(finish-beg,3))

    # display final path
    visited,path,cost=showPath(img,current,True,start,visited,path)
    path.reverse()

    #end with saving the results in a txt document
    documentation(visited,path,finish-beg,cost,start,current,1)

    #documentation(visited,path,finish-beg,cost,start,current,0)

    return finish-beg



def showPath(img,current,is_end,start,visited_list=None,parent_list=None):
    '''
    displays current progress as image if is_end is disabled\n
    if is_end is enabled-\n
    returns visited list and parent list and calculates cost
    '''
    cost=0.0
    visited_color=[100,0,100]
    path_pointer=[0,255,0]

    # to avoid errors
    if(parent_list==None):
        parent_list=[]
    if(visited_list==None):
        visited_list=[]
    

    img2=np.copy(img)

    # display/compile visited path

   

    while(current.position!=start.position):

        #display image

        temp=current.position
        img2[temp[0],temp[1],0]=path_pointer[0]
        img2[temp[0],temp[1],1]=path_pointer[1]
        img2[temp[0],temp[1],2]=path_pointer[2]

        if(not is_end):
            current=current.parent
            continue

        else:
         parent_list.append(temp)
         temp=current.parent
         
         #calculate cost

         if(choice2==2 and choice3==2):
             cost=cost+calcCost2(current,temp,start,temp.parent)
         else:
             cost=cost+calcCost(current.position,temp.position)

         current=temp
        
    if(is_end):
     parent_list.append(start.position)

    #imshow and imwrite 

    cv2.resize(img2,(1000,1000))    
    cv2.namedWindow('path',cv2.WINDOW_NORMAL)
    cv2.imshow('path',img2)
    if(is_end):
        cv2.imwrite(img_write_path,img2)

    #return the lists and the cost
    return (visited_list,parent_list,cost)


# display option changed according to option

def display(val,option,w=None):
    '''
    write data according to option specified
    '''
    if(option==0):
        print(val)
    else:
        w.write(val)
        w.write('\n')



# Documentation according to option

def documentation(visited_list,parent_list,val,cost,start,end,option):
    '''
    document the data
    '''
    if(option==1):
     #open desired file to write result-
     w=open(write_path,'w')

     #write the data
    display(str(choice)+')'+heuristic[choice-1]+' case('+str(choice2)+') -',option,w)
    if(choice2==2 and choice3==2):
        display('Using a different cost function',option,w)
    display('cost of traversing by distance='+str(round(cost,2)),option,w)
    display('cost stored at end point='+str(round(end.f,2)),option,w)
    display('No. of nodes in path='+str(len(parent_list)),option,w)
    display('No of nodes visited='+str(len(visited_list)),option,w)
    display('start point='+str(start.position),option,w)
    display('end point='+str(end.position),option,w)
    display('Nodes in path-',option,w)
    #display('Nodes visited-',option,w)
    #display(str(visited_list),option,w)
    display('time taken for traversing='+str(val),option,w)
    display(str(parent_list),option,w)

    if(option==1):
     #close file
     w.close()


t=main_func(img,start,end)
#print(t)
cv2.waitKey(0)
