import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file (compiled C program)
coin_toss = ctypes.CDLL('./ct.so')

# Set argument and return types for the C function
coin_toss.calculate_probabilities.argtypes = [
    ctypes.c_int,                   # int n (number of trials)
    ctypes.POINTER(ctypes.c_double), # double* probabilities
    ctypes.POINTER(ctypes.c_double)  # double* cdf
]

# Parameters
num_trials = 100000  # Number of simulations (adjustable)
probabilities = (ctypes.c_double * 4)()  # Array for PMF (Probability Mass Function)
cdf = (ctypes.c_double * 4)()            # Array for CDF (Cumulative Distribution Function)

# Call the C function
coin_toss.calculate_probabilities(num_trials, probabilities, cdf)

# Convert results from C arrays to Python NumPy arrays for easy handling
probabilities = np.array(list(probabilities))
cdf = np.array(list(cdf))

# Define the outcomes
outcomes = ['0 Heads', '1 Head', '2 Heads', '3 Heads']

# Visualization of PMF and CDF in the same plot
plt.figure(figsize=(10, 6))

# Plot PMF with blue color
plt.stem(outcomes, probabilities, basefmt=" ", linefmt="b-", markerfmt="bo", label="PMF")

# Plot CDF with red color
plt.step(outcomes, cdf, where="post", color="r", label="CDF")

# Customize the plot
plt.title('PMF and CDF for Heads in 3 Coin Tosses')
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
