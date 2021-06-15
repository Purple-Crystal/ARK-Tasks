import numpy as np
from numpy.linalg import inv

x_observations = np.array([320, 330, 340])
v_observations = np.array([50, 100, 150])

z = np.c_[x_observations, v_observations]

# Initial Conditions
a = 1  # Acceleration
v = 80
t = 1  # Difference in time

# Process / Estimation Errors
error_est_x = 10
error_est_v = 4

# Observation Errors
error_obs_x = 25  # Uncertainty in the measurement
error_obs_v = 8

def prediction2d(x, v, t, a):
    A = np.array([[1, t],
                  [0, 1]])
    X = np.array([[x],
                  [v]])
    B = np.array([[0.5 * t ** 2],
                  [t]])
    X_prime = A.dot(X) + B.dot(a)
    return X_prime


def covariance(s1, s2):
    cov1 = s1 * s2
    cov2 = s2 * s1
    cov_matrix = np.array([[s1 ** 2, cov1],
                           [cov2, s2 ** 2]])
    return np.diag(np.diag(cov_matrix))


# Initial Estimation Covariance Matrix
P = covariance(error_est_x, error_est_v)
A = np.array([[1, t],
              [0, 1]])

# Initial State Matrix
X = np.array([[z[0][0]],
              [v]])
n = len(z[0])

for data in z[1:]:
    X = prediction2d(X[0][0], X[1][0], t, a)
    # To simplify the problem, professor
    # set off-diagonal terms to 0.
    P = np.diag(np.diag(A.dot(P).dot(A.T)))

    # Calculating the Kalman Gain
    H = np.identity(n)
    R = covariance(error_obs_x, error_obs_v)
    S = H.dot(P).dot(H.T) + R
    K = P.dot(H).dot(inv(S))

    # Reshape the new data into the measurement space.
    Y = H.dot(data).reshape(n, -1)

    # Update the State Matrix
    # Combination of the predicted state, measured values, covariance matrix and Kalman Gain
    X = X + K.dot(Y - H.dot(X))

    # Update Process Covariance Matrix
    P = (np.identity(len(K)) - K.dot(H)).dot(P)

print("Kalman Filter Matrix is:\n", X)