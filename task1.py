# creating a list
my_list=[1,2,3,4,5]
# adding an element in the list
my_list.append(6)
#removing an element 
my_list.remove(3)
#modifying an element
my_list[0]=9

print("UPDATED LIST:",my_list)

#creating a dictionary
my_dict={'name':'john','age':26,'city':'delhi'}
#adding an element
my_dict['gender']='male'
#removing an element 
del my_dict['age']
#modifying the dictionary
my_dict['city']='mumbai'

print('UPDATED DICTIONARY:',my_dict)

#creating a set
my_set={1,2,3,4,5}
#adding an element
my_set.add(6)
#removing an element
my_set.remove(2)
##modifying the set
my_set.add(8)
my_set.discard(4)

print('UPDATED SET:',my_set)