# Example family_members tuple
family_members = ('Hirenkumar', 'Swatiben', 'Yasika', 'Himanshi', 'Hemansh', 'Ramesh', 'Jayesh')

# Unpack siblings and parents
father, mother, *siblings = family_members

# Display the result
print("Father:", father)
print("Mother:", mother)
print("Siblings:", siblings)
# father and mother are assigned the first two elements of the family_members tuple, 
# and the *siblings syntax is used to collect the remaining elements into a list assigned to the siblings variable