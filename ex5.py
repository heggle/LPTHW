#This exercise is to become more familiar with variables
#	and printing in python 

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie 
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'


#Insert a string variable into a string 
print "Let's talk about %s." % my_name

#Insert an integer variable into a string 
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight

print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are ususally %s depending on the coffee." % my_teeth

#This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)

# See rest of python formatters by googling "python format characters"
# "%r" is a very useful formatter because it will print anything

print "\nExample of the formatter 'r':"
print "He has %r teeth and weighs %r pounds!" %(my_teeth,my_weight)
print "However, '%r' does put strings in quotes, as demonstrated above!"