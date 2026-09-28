# %% [markdown]
# ## Assignment II: Slicing, Arrays, Functions, and Rotations
# 
# **Total: 100 points.** Questions 1 to 3 (75 points: Q1 is 20 points, Q2 and Q3 are 25 points each, including the 5-point Submission), plus Question 4 (25 bonus points).
# 
# This assignment pulls together everything from Sep 9 to Sep 18: list and NumPy array slicing, array arithmetic, writing your own functions, generating lists, and building rotation matrices. **All arrays and lists in this assignment are 1D or 2D only.** You will not need (and should not use) any 3D or higher-dimensional arrays anywhere below.
# 
# - Each of Questions 1 to 3 is split into **Part (a)** and **Part (b)**.
# - **Question 4 is an entirely bonus question worth 25 points.** It asks you to explore the relationship between SU(2) and SO(3), the famous "double cover," using only the tools you already have (complex numbers, 2D arrays, and functions).
# - Write your code in the cell provided for each part, and make sure it **prints** your final answer(s) clearly, ideally with an f-string that says what the printed value represents.
# - **Submission (5 points):** see the instructions at the very end of this notebook.
# 

# %% [markdown]
# ### AI Usage Policy
# 
# **No AI tools (ChatGPT, Claude, GitHub Copilot's suggestion/chat features, etc.) may be used to generate, complete, or rewrite your solutions for this assignment.** All code and explanations must be your own work.
# 
# **Exception and disclosure requirement:** If you have **GitHub Copilot active** in your editor (e.g. inline autocomplete suggestions appearing as you type), you do not need to disable it, but you **must disclose this** by adding a short **markdown cell right below this one** stating:
# - That Copilot (or any other AI tool) was active while you worked, and
# - Briefly, how you used or did not use its suggestions (e.g. "Copilot was active but I did not accept any of its suggestions for graded cells" or "I accepted a Copilot suggestion for the boilerplate `for` loop in Q3(a) but wrote the logic myself").
# 
# Notebooks with AI-generated solutions that are not disclosed as above will not receive credit, regardless of correctness.
# 

# %% [markdown]
# **AI Usage Disclosure (student to fill in):**
# 
# *(If GitHub Copilot or any other AI tool was active while you worked on this assignment, describe that here. If no AI tool was active at all, write "No AI tools were used.")*
# 

# %% [markdown]
# ### Question 1: Slicing, Lists and NumPy Arrays (20 points)
# 
# **(a) [12 pts] Lists.** Create a list of at least 8 numbers called `my_list`. Using slicing (no loops), print:
# 1. The first 4 elements.
# 2. The last 4 elements.
# 3. Every 3rd element, starting from the first.
# 4. The list reversed.
# 
# **(b) [8 pts] 2D arrays.** Create a 5x5 NumPy array `M` containing the integers 1 through 25 (using `np.arange` and `.reshape`). Using slicing, print:
# 1. The 3rd row of `M`.
# 2. The 2nd column of `M`.
# 3. The 2x2 sub-matrix in the *bottom-right* corner of `M`.
# 4. `M` with its rows reversed, using slicing, **not** `np.flip`.
# 

# %%
my_list = [1,2,3,5,7,11,13,17]
first4 = my_list[:4]
last4 = my_list[-4:]
every3 = my_list[::3]
reverse = my_list[::-1]
print(first4)
print(last4)
print(every3)
print(reverse)

# %%
M = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print(M)
print(M[2, :])
print(M[:, 1])
print(M[3:5, 3:5])
print(M[::-1, :])


# %% [markdown]
# ### Question 2: Arithmetic with NumPy Arrays (25 points)
# 
# **(a) [15 pts] Elementwise arithmetic with floats.** Create `x = np.linspace(1, 10, 10)` (this always gives you floats). Print `x + 3`, `x - 2`, `x * 4`, `x / 5`, `x ** 3`, and `np.sqrt(x)`. Then compute `y = np.sqrt(x) ** 2` and use `np.isclose(x, y)` to confirm that `y` matches `x` element by element, even though squaring a square root does not give back the *exact* original floating-point value.
# 
# *Example of how `np.isclose` works:* `np.isclose(0.0000001, 0)` returns `True`, because the two values are equal up to a small numerical tolerance, even though `0.0000001 == 0` would return `False`. This is exactly why we use `np.isclose` instead of `==` when comparing floating-point results, such as your `x` and `y` above: after the square root and the squaring, the values will differ from the originals by something like `1e-15`, not exactly `0.0`.
# 
# **(b) [10 pts] Matrix multiplication and standardization.** Create two `3x3` matrices `A` and `B` of your choice (any numbers). Compute their matrix product `A @ B` (**not** elementwise multiplication) and print it. Then confirm, using `np.allclose(A @ B, B @ A)`, that matrix multiplication is generally **not commutative** (this should print `False`, unless you happened to pick special matrices). Finally, compute a "standardized" version of `A`: subtract `A.mean()` and divide by `A.std()`. Print the standardized array, and confirm its new mean is (approximately) `0` using `np.isclose`.
# 

# %%
x = np.linspace(1,10,10)
print(x + 3)
print(x - 2)
print(x * 4)
print( x / 5)
print(x ** 3)
print(np.sqrt(x))
y = np.sqrt(x) ** 2
np.isclose(x,y)
print(np.isclose(x,y))


# %%
A = np.array([[1,2,3],[2,4,6],[3,6,9]])
B = np.array([[6,9,7],[2,5,4],[3,9,1]])
print(A @ B)
np.allclose(A @ B, B @ A)
A.mean()
A.std()
print(np.isclose(A.mean(),A.std()))


# %% [markdown]
# ### Question 3: Defining Functions and Generating Lists (25 points)
# 
# **Background: the double factorial.** For a positive integer $n$, the **double factorial** $n!!$ is the product of every second integer counting down from $n$ to either $1$ or $2$ (whichever has the same parity as $n$). For example:
# - $6!! = 6 \times 4 \times 2 = 48$
# - $7!! = 7 \times 5 \times 3 \times 1 = 105$
# 
# By convention, $0!! = 1$ and $1!! = 1$.
# 
# **(a) [15 pts] A simple generator function.** Write a function `double_factorial(n)` that computes and returns $n!!$ for a single non-negative integer `n`, using a `for` (or `while`) loop. Then write a function `double_factorials_up_to(n)` that uses a loop over `k = 1, ..., n` (calling your `double_factorial` function each time) to build and return a list of $[1!!, 2!!, 3!!, ..., n!!]$. Call it with `n = 10` and print the result.
# 
# **(b) [10 pts] A function with a custom recurrence.** Write a function `custom_sequence(a0, a1, n)` that returns a list of the first `n` terms of the sequence defined by $s_0 = a_0$, $s_1 = a_1$, and $s_k = 2 s_{k-1} + s_{k-2}$ for $k \geq 2$ (a "Pell-like" sequence). Give `a1` a default value of `1`. Call your function with `a0 = 0`, using the default for `a1`, for `n = 10` terms, and print the result.
# 

# %%
def double_factorial(n):
    result = 1
    for k in range(n, 0, -2):
        result *= k
    return result
def double_factorial_up_to(n):
    result = []
    for k in range(1, n+1):
        result.append(double_factorial(k))
    return result
print(double_factorial_up_to(10))

# %%
def custom_sequence(a0,a1=1,n=10):
    sequence = [a0, a1]
    for k in range(2, n):
        next_term = 2*sequence[k-1] + sequence[k-2]
        sequence.append(next_term)
    return sequence[:n]
print(custom_sequence(0, n=10))

# %% [markdown]
# ### Question 4 (Bonus, 25 points): SU(2) and the Double Cover of SO(3)
# 
# You've already built rotation matrices $R_x, R_y, R_z \in SO(3)$: real $3\times 3$ matrices that rotate vectors in ordinary 3D space. There is a second way to describe the *same* rotations, using $2\times 2$ **complex** matrices instead. This is the group $SU(2)$.
# 
# **Reminder: $R_z(\theta)$.** For reference, here again is the rotation-about-$z$ matrix you built in Activity X:
# 
# $$
# R_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}
# $$
# 
# ```python
# def Rz(theta):
#     c = np.cos(theta)
#     s = np.sin(theta)
#     return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
# ```
# 
# **Background (given, no derivation needed).** A rotation by angle $\theta$ about a unit-vector axis $n = [n_x, n_y, n_z]$ (given to you as a plain Python **list** of three numbers), viewed as an element of $SU(2)$, is given by:
# 
# $$
# U(\theta, n) =
# \begin{bmatrix}
# \cos\left(\dfrac{\theta}{2}\right) - i\,n_z \sin\left(\dfrac{\theta}{2}\right) & -(n_y + i\,n_x)\sin\left(\dfrac{\theta}{2}\right) \\[6pt]
# (n_y - i\,n_x)\sin\left(\dfrac{\theta}{2}\right) & \cos\left(\dfrac{\theta}{2}\right) + i\,n_z \sin\left(\dfrac{\theta}{2}\right)
# \end{bmatrix}
# $$
# 
# You are also given the three Pauli matrices. In math notation, they are:
# 
# $$
# \sigma_x = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \qquad
# \sigma_y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}, \qquad
# \sigma_z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}
# $$
# 
# and as NumPy arrays:
# 
# ```python
# sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
# sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
# sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
# paulis = [sigma_x, sigma_y, sigma_z]
# ```
# 
# Every $U \in SU(2)$ maps to an actual $3\times 3$ rotation matrix $R(U) \in SO(3)$ via the formula:
# 
# $$
# R(U)_{jk} = \frac{1}{2}\,\mathrm{tr}\big(\sigma_j\, U\, \sigma_k\, U^\dagger\big), \qquad j, k \in \{x, y, z\}
# $$
# 
# where $U^\dagger$ is the conjugate transpose of $U$ (`U.conj().T` in NumPy). Recall that the **trace** of a square matrix, written $\mathrm{tr}(\cdot)$, is just the sum of its diagonal entries; in NumPy you can compute it directly with `np.trace(A)` for any square array `A`, so you don't need to write a loop just to get the trace itself.
# 
# **(a) [15 pts]** Write a function `U(theta, n)` that takes an angle `theta` and an axis `n = [nx, ny, nz]` (a Python list), and returns the $2\times 2$ complex NumPy array given by the formula above. Write a function `su2_to_so3(M)` that builds the $3\times 3$ real matrix $R(M)$ using the second formula above (a double `for` loop over the `paulis` list is fine, using `np.trace` for the trace itself; take `.real` at the end, since the result should be real up to tiny numerical error). Using `n = [0, 0, 1]` (the $z$-axis) and an angle `theta` of your choice, confirm with `np.allclose` that `su2_to_so3(U(theta, n))` matches `Rz(theta)` (defined above).
# 
# **(b) [10 pts]** Here is a simpler way to see the double cover, using `Rz` and rotating **twice**. Here, $I$ denotes the identity matrix (in NumPy, `np.eye(n)` gives you the $n \times n$ identity). Let `n = [0, 0, 1]` and `theta = np.pi` (a half turn). Compute `U_half = U(theta, n)`, then "rotate twice" by composing this matrix with itself: `U_full = U_half @ U_half` (two half turns, applied one after another, make a full turn).
# 1. Use `np.allclose` to show that `U_full` equals `-np.eye(2)` (the *negative* identity), not the identity `np.eye(2)`, even though two half turns should bring you all the way back around.
# 2. Use `su2_to_so3` to show that `su2_to_so3(U_full)` matches `Rz(2 * np.pi)`, which should simply be the identity `3x3` matrix, since a full $2\pi$ rotation in ordinary 3D space does nothing at all.
# 3. Print a one or two sentence explanation of what this shows: two composed half turns return $SU(2)$ to $-I$ rather than back to $I$, yet the very same two half turns return $SO(3)$ to the identity, exactly as expected. Since two different $SU(2)$ matrices, $I$ and $-I$, both correspond to the very same $SO(3)$ rotation (doing nothing), $SU(2)$ is called a **double cover** of $SO(3)$.
# 

# %% [markdown]
# **Note: how $R_{jk}$ connects to $R_z(\theta)$.** The nine numbers $R_{jk}$ for $j,k \in \{x,y,z\}$ are just the nine entries of the $3\times3$ matrix, with $j$ giving the row and $k$ giving the column. So checking that `su2_to_so3(U(theta, n))` equals `Rz(theta)` just means all nine of these entries should match. When `n = [0, 0, 1]`, the formula for `U(theta, n)` becomes a diagonal matrix, so `U` commutes with `sigma_z`, giving `R_zz = 1` and `R_xz = R_yz = R_zx = R_zy = 0`. For the remaining entries, using `sigma_x` and `sigma_y` conjugated by `U` and the identity `tr(sigma_j sigma_k) = 2` if `j = k`, else `0`, gives `R_xx = R_yy = cos(theta)`, `R_yx = sin(theta)`, and `R_xy = -sin(theta)`. Arranging these nine values into the $3\times3$ grid reproduces exactly `Rz(theta)`. This is why the loop over `paulis` in `su2_to_so3` should reconstruct `Rz(theta)` when tested with `n = [0, 0, 1]`.
# 

# %%
# TODO: your code for Q4(a) here


# %%
# TODO: your code for Q4(b) here


# %% [markdown]
# ### Submission Instructions (5 points)
# 
# Submit this assignment in two parts:
# 
# 1. **CrowdMark:** Submit your completed notebook (or a PDF/printout of it, per your instructor's usual CrowdMark process) through CrowdMark as normal.
# 2. **GitHub (worth 5 points):** Push this completed notebook to a GitHub repository for Assignment II, and include the link to your GitHub repository as part of your CrowdMark submission (e.g. in a text box or as a comment on the first page).
#    - **Either** make the repository **public**, so the link alone is enough, **or**
#    - keep it **private** and add the instructor as a collaborator using the GitHub username `say-yas`.
# 3. Double check that the link you submit actually opens your repository (and that the notebook with your completed answers is visible in it) before submitting.
# 
# The 5 points here are awarded specifically for completing this GitHub step correctly (a working public link, or collaborator access granted on a private repo), and are counted toward the 100 point total alongside the base points from Questions 1 to 3 and the bonus points from Question 4.
# 


