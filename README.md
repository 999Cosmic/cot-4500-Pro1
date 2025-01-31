This entire repository is designed to show four algorithms:

Algorithms:
1. Approximation Algorithm
2. The Bisection Method
3. The Fixed-Point Iteration
4. The Newton-Raphson Method

in regards to how they are supposed to respond given their Python implementation.

The best way to fully explore the project is by deploying this repo into Replit, link below for instructions:
https://docs.replit.com/cloud-services/deployments/deploying-a-github-repository#:~:text=Import%20a%20Repl%20from%20GitHub,top%20right%20of%20the%20modal.

Once done, you will see on the left the following project structure:

src/main/__init__.py 

src/main/assignment_1.py

src/test/__init__.py

src/test/test_assignment_1.py

requirements.txt 

README.md 

in which assignment_1.py in main is the Python code for all four algorithms that are tied with values to specific related problems, in which test_assignment_1.py tests to make sure the
algorithms when run with those values match the correct number of iterations and specific values.

To compile and be able to see all of it yourself, here are the steps:
1. Make sure shell is on the right side (not console)
2. Type in "pip install pytest" (you will see it install with plenty of text)
3. After that, type in "pip freeze > requirements.txt", this should output for you the third-party libraries in Python you have installed in Replit, the libraries can vary depending on if you installed libraries before but what is important is you having pytest and its associated version
4. Now, type in the console "pytest src/test/test_assignment_1.py", this should output in the shell the pytest session starting and showing green with all 4 test cases passed in an allocated timeframe

If you want, you can alter the algorithms values in assignment_1.py and do step 4 again and see that 
the test cases can also debug code for you to see what you got wrong and what needs fixing. 

Use the project to your heart's intent and hope you enjoy it!
