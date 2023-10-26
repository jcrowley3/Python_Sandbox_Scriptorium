# Small test scripts
# To RUn: Highlight and press-> ctrl+option+n

# if statement with multiple conditions
# WORKS!
values = [None, 'ASC', 'DESC', 'bang', 'DESCs', 'DESCS', 1]
for var in values:
	if var not in (None, 'ASC', 'DESC'):
		print(f'{var}: if')
	else:
		print(f'{var}: else')


# if statement multiple variable falsy check
# WORKS!
var1 = 'ASC'
var2 = {}
var3 = 'DESC'

if all((var1, var2, var3)):
	print('No None values')
else:
	print('I sense a None value!')
