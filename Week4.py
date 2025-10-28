from sympy import symbols, Or, Not, Implies, Xor, satisfiable

# Define propositional symbols
Rain = symbols('Rain')
Harry_Visited_Hagrid = symbols('Harry_Visited_Hagrid')
Harry_Visited_Dumbledore = symbols('Harry_Visited_Dumbledore')

# Knowledge base statements
s1 = Implies(Not(Rain), Harry_Visited_Hagrid)        # If it didn't rain, Harry visited Hagrid
s2 = Xor(Harry_Visited_Hagrid, Harry_Visited_Dumbledore)  # Harry visited exactly one of them
s3 = Harry_Visited_Dumbledore                        # Harry visited Dumbledore

# Combine all statements
knowledge_base = s1 & s2 & s3

# Find all satisfying models
sol = satisfiable(knowledge_base, all_models=True)

# Print results
for model in sol:
    if model.get(Rain, False):
        print("It rained today.")
    else:
        print("There is no rain today.")

"""output::


