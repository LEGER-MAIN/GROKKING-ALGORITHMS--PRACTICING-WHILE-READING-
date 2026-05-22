def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
    
print(fact(5))

# Notes

# EXERCISE
# 3.2 Suppose you accidentally write a recursive function that runs 
# forever. As you saw, your computer allocates memory on the 
# stack for each function call. What happens to the stack when your 
# recursive function runs forever?

"Eventually, the program runs out of stack memory, causing a stack overflow error."


# Recap
# • Recursion is when a function calls itself.
# • Every recursive function has two cases: the base case  
# and the recursive case.
# • A stack has two operations: push and pop.
# • All function calls go onto the call stack.
# • he call stack can get very large, which takes up a lot of memory.