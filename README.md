# CMPS 2200  Recitation 02

**Name (Team Member 1):**____Kayla Willis_____________________  
**Name (Team Member 2):**_____Cameron McLaren____________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of W(n) using f(n) = 1, f(n) = log n and f(n) = n. Then, generate actual values for W(n) for your code and confirm that the trends match your derivations.

**TODO: 
f(n) = 1: root is 1, level 1 is 1 * 2 (2 nodes) so it is leaf dominated, n leaves * 1 (constant) per leaf. for ours this gives us O(n)

f(n) = log(n): root is logn, level 1 is log(n/2) and log(n/2) meaning its root dominated because the leafs are smaller. for ours this gives us O(log^2n)

f(n) = n: root is n, level 1 is n/2 and n/2 added equals n, meaning it is balanced and the max cost per level is n*levels. for ours this gives us O(nlogn)
**

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of W(n), we can look at the relationship between a, b, and f(n). Suppose that f(n) = n^c. What is the asypmptotic behavior of W(n) if c < log_b a? What about c > log_b a? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

**
"if the c power is less than log base b of a" and if a=b=2 then logb(a) is 1
if c < log_b(a):
work is O(n) because if we plug in the numbers so that c is smaller than 1: W(n)=2*W(n/2)+n^log_2(1) which simplifies to 2*W(n/2)+1 (because n^0=1). Thus, root=1 and leaf level 1 = 2*1 like above so it is leaf dominated.
if c > log_b(a):
Work is O(n^2) because: W(n) = 2W(n/2) + n^log2(4) as 4>2 which simplifies to W(n) = 2W(n/2) + n^2. Root is n^2 and following leaf level is (n/2)^2 making it root dominated.
if c = log_b(a):
work is O(nlogn) because: W(n)=2*W(n/2)+n^log_2(2) which simplifies to 2W(n/2) + n. Thus, root is n and leaf level 1 is n/2 and n/2 which adds up to n, confirming its balanced and the work is n * log n

Both of our replits were not working so this was completed in visual studios where neither of us could get tabulate or pytests to work properly
**

- [ ] 6. (3 points) W(n) is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**
f(n) = 1
S(n) is O(logn). root = 1, leaf 1 is 1. since the tree is balanced, we also know the height is logn which is our span.
f(n) = log n
S(n) is O(log^2n). root=logn, level 1 leaf is log(n/2) being leaf dominated. 
f(n) = n
S(n) is O(n). root=n, level 1 leaf=n/2 being root dominated. 
**
