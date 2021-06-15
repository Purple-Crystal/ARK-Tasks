#This is to create matrices and perform the filters operations..
def create_A(m):
  calc_m=m
  calc_m[0,0]=calc_m[0,0]+m[1,0]*t
  calc_m[1,0]=calc_m[1,0]+m[1,1]*t
  return calc_m

def calc_perror(p_measured,p_prev):
  return abs(p_measured-p_prev)

def calc_perror2(p_measured,p_prev):
  p_max_error=abs(p_measured-p_prev)
  return 1/(2*(np.pi)*(p_max_error**2))

#R is the co-varaince matrix of measurement
#Variance is calculated about the predicted path point

def create_R(prev,curr):
  var_px=calc_perror2(curr[0][0],prev[0][0])
  var_py=calc_perror2(curr[0][1],prev[0][1])
  var_vx=calc_verror2(curr[1][0],prev[1][0])
  var_vy=calc_verror2(curr[1][1],prev[1][1])
  R=np.diag([var_px,var_py,var_vx,var_vy])
  #R=np.diag([0.8,0.8,0.1,0.1])
  return R

#Calculate Kalman Gain

def calc_K(P,R):
 return (np.dot(P,np.linalg.inv(np.add(P,R))))

#This is for the update step

def update_X(prev,curr,P,R): # update X
  t=np.subtract(curr,prev)
  K=calc_K(P,R)
  t[0][0]=K[0][0]*t[0][0]
  t[0][1]=K[1][1]*t[0][1]
  t[1][0]=K[2][2]*t[1][0]
  t[1][1]=K[3][3]*t[1][1]
  t=np.add(t,curr)
  return t

def update_P(P,R): # update P
   K=calc_K(P,R)
   I=np.identity(4,dtype=float)
  return np.dot(np.subtract(I,K),P)
