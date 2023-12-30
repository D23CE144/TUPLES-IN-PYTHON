# Given tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a Nordic country
estonia_is_nordic = 'Estonia' in nordic_countries

# Check if 'Iceland' is a Nordic country
iceland_is_nordic = 'Iceland' in nordic_countries

# Display the results
print("Is Estonia a Nordic country?", estonia_is_nordic)
print("Is Iceland a Nordic country?", iceland_is_nordic)

#  the in operator is used to check whether 'Estonia' and 'Iceland' are in the nordic_countries tuple. 
# The results will be False for 'Estonia' and True for 'Iceland' since Iceland is indeed a Nordic country.