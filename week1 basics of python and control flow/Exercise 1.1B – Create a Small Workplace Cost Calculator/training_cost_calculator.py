
""" 
 collect number of learners, cost per learner and fixed room/platform cost; 
 calculate variable cost and total cost; display the result.
"""
try:
    no_of_learners = int(input("Enter no of learners"))
    cost_per_learner = float(input("Enter cost per learner "))
    fixed_cost = float(input("Enter fixed cost"))
    variable_learner_cost = no_of_learners* cost_per_learner
    final_cost = variable_learner_cost +fixed_cost
    print("------summary-------")
    print(f"no of learners {no_of_learners}")
    print(f"Cost per learner {variable_learner_cost}")
    print(f"Fixed cost {fixed_cost}")
    print(f"Final cost {final_cost}")
    # no_of_learners=5, variable_learner_cost=100, fixed_cost=20
    #result fixed_cost 20   final cost= 520
except:
    print("Invalid input")