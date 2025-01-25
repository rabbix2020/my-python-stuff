from sys import argv

if len(argv) == 1:	exit('ERROR: lack of any arguments, please key "/?" to get information')

if argv[1] == "/?":
  print("This program calcultes xp and was written on Python by rabbix (a.k.a zero)")
  print("syntax:")
  print("	calculate_xp [level] [promotion]")
  print("	calculate_xp /? - prints information about program")
  exit()

if len(argv) == 2 or len(argv) > 3:	exit('ERROR: invalid count of arguments, please key "/?" to get information')

promotion_scalar = [1.0, 1.0, 1.0, 1.0, 2.0, 4.0, 6.0, 6.0]

level_calc = lambda x: 25 * (x**2 +39*x)

level = int(argv[1])
promotion = int(argv[2])

if level < 1:	exit("ERROR: miminum level is 1")
if level > 26:	exit("ERROR: maximum level is 26")

if promotion < 1:	exit("ERROR: miminum promotion is 1")
if promotion > 7:	exit("ERROR: maximum promotion is 7")

print(promotion_scalar[promotion] * level_calc(level) - promotion_scalar[promotion] * level_calc(level-1))