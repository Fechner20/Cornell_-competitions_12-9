wh=int(input("How many hours did Denise work today?: "))

if wh >= 24:
  print (f"Hours Slept: {wh-24}")
else:
  print (f"Hours Slept: {24-wh}")
