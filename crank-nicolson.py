import numpy as np


# Using crank-nicolson method to simulate Uxx = Ut;

'''
Let there be 100x100 (NxN) grid, with dx,and dt as 0.1
'''

N = 11
alpha = 0.005/0.1**2
def update(grid,t):
    A = np.zeros((N,N))
    A[0,0] = 1     # Boundary Condition
    A[N-1,N-1] = 1     # Boundary Condition
    for i in range(1,N-1):
        A[i,i+1] = -alpha/2

    for i in range(1,N-1):
        A[i,i] = (1+alpha)

    for i in range(1,N-1):
        A[i,i-1] = -alpha/2

    Y = np.zeros((N,1))
    for i in range(1,N-1):
        Y[i,0] = alpha/2*(grid[t-1,i-1] - 2*grid[t-1,i] + grid[t-1,i+1]) + grid[t-1,i]
    Y[0,0] = 0
    Y[N-1,0] = 0
    
    for i,val in enumerate((np.linalg.inv(A)@Y).flatten()):
        grid[t,i] = val
    print(A)


def method():
    grid = np.zeros((N,N))
    for i in range(N):
        grid[0,i] = 100*np.sin(np.pi*(i/(N-1)))
    # update(grid,1);
    for i in range(N-1):
        update(grid,i+1)
    print(grid)



def main():
    method()


if __name__ == "__main__":
    main()

