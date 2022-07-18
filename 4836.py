def firstRule(dance):
  error = []
  for i in range(len(dance)):
    if dance[i] == 'dip':
      if i >= 2 and (dance[i - 2] == 'jiggle' or dance[i - 1] == 'jiggle'):
        continue
      if i >= 1 and dance[i - 1] == 'jiggle':
        continue
      if i + 1 < len(dance) and dance[i + 1] == 'twirl':
        continue
      error.append(i)
  if len(error) > 0:
    return error
  return True

def secondRule(dance):
  if len(dance) < 3:
    return False
  if " ".join(dance[-3:]) == 'clap stomp clap':
    return True
  return False

def thirdRule(dance):
  if 'twirl' in dance:
    if 'hop' in dance:
      return True
    return False
  return True
  
def fourthRule(dance):
  if dance[0] == 'jiggle':
    return False
  return True

def fifthRule(dance):
  if 'dip' in dance or 'DIP' in dance:
    return True
  return False

rule_fn = [firstRule, secondRule, thirdRule, fourthRule, fifthRule]
dance = input().split()
error_index = []

for i in range(len(rule_fn)):
  if rule_fn[i](dance) != True:
    error_index.append(i+1)
    if i == 0: 
      for error_step in rule_fn[0](dance):
        dance[error_step] = 'DIP'

if len(error_index) == 0:
  print(f'form ok: {" ".join(dance)}')
elif len(error_index) == 1:
  print(f'form error {error_index[0]}: {" ".join(dance)}')
elif len(error_index) == 2:
  print(f'form errors {error_index[0]} and {error_index[1]}: {" ".join(dance)}')
else:
  print('form errors ',end='')
  for i in range(len(error_index)):
    print(f'{error_index[i]}',end='')
    if i < len(error_index) - 2:
      print(', ',end='')
    if i == len(error_index) - 2:
      print(' and ',end='')
  print(f': {" ".join(dance)}')