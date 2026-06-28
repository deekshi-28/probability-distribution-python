from scipy.stats import binom, poisson
import matplotlib.pyplot as plt

# =====================================
# Binomial Distribution
# =====================================

print("===== Binomial Distribution =====")

num_trials = 10
heads_probability = 0.5

probs = [
    binom.pmf(i, num_trials, heads_probability)
    for i in range(num_trials + 1)
]

plt.figure(figsize=(8, 5))
plt.stem(range(num_trials + 1), probs)
plt.title("Binomial Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.grid(True)

plt.show()

# =====================================
# Poisson Distribution
# =====================================

print("===== Poisson Distribution =====")

rate = 3.3

probs = [
    poisson.pmf(i, rate)
    for i in range(15)
]

plt.figure(figsize=(8, 5))
plt.stem(range(15), probs)
plt.title("Poisson Distribution")
plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.grid(True)

plt.show()