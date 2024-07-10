this is an optimized version of the "python-constraint2 2.0.0b5" which can be found in the following link: "https://pypi.org/project/python-constraint2/", or it can be found in the releases page of the repo: "https://github.com/python-constraint/python-constraint/releases".

i have been trying to solve a particular CSP problem using the OptimizedBacktrackingSolver, but when the solver ran for 8 days strait without giving me an answer I decided to optimize it more for my application.

assuming that the OptimizedBacktrackingSolver would at least take 691200 seconds (8days*24hours*60minutes*60seconds), and the solver would take only 8 seconds after optimization, the result is a speedup of >86,400X of computation time. the below picture is a proof that my code actually computed the solution in <8 seconds, you're most welcomed to try it yourself

![image](https://github.com/bmkaat/erbfs/assets/109302756/843ffd36-f27c-4d85-b77a-9926cfde45d4)

to run this library yourself, you need to install it manually, here's the steps i followed:
1- install the original library using "pip install python-constraint2"
2- downlaod this library.
3- cut and paste the library in the same folder as the original library is installed in.
feel free to suggest a better way for installation.

and here's the list of optimizations:
1- rewritten the constraint checking part of the "myconstraint.solvers.OptimizedBacktrackingSolver.getSolutionIter()" to check all the variables when an assignment is made and not only the assigned variables and their related constraints.
2- rewritten the "myconstraint.solvers.OptimizedBacktrackingSolver.getSortedVariables()" to sort by row first then by cell, since the constraints of each row are mutually exclusive. (i think a generalized form of this code can be implemented)
3- added some code to "myconstraint.Problem.AllDifferentConstraint()" to be able to check unassigned variables.
4- added some code to "myconstraint.Problem.AllEqualConstraint()" to be able to check unassigned variables.
