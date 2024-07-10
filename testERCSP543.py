from myconstraint import *
import time


grid=[]
rows=14 #int(input('how many rows?'))
cols=9  #int(input('how many columns?'))
for i in range(1,rows+1):
    row=[]
    for j in range(1,cols+1):
        if len(str(i))<2:
            row.append('0'+str(i)+str(j))
        elif len(str(i))==2:
            row.append(str(i)+str(j))
    grid.append(row)
    
p = Problem(OptimizedBacktrackingSolver())

'''grid = [['011','012','013','014','015','016','017','018','019'],['021','022','023','024','025','026','027','028','029'],['031','032','033','034','035','036','037','038','039'],
        ['041','042','043','044','045','046','047','048','049'],['051','052','053','054','055','056','057','058','059'],['061','062','063','064','065','066','067','068','069'],
        ['071','072','073','074','075','076','077','078','079'],['081','082','083','084','085','086','087','088','089'],['091','092','093','094','095','096','097','098','099'],
        ['101','102','103','104','105','106','107','108','109'],['111','112','113','114','115','116','117','118','119'],['121','122','123','124','125','126','127','128','129'],
        ['131','132','133','134','135','136','137','138','139'],['141','142','143','144','145','146','147','148','149']]
'''
for row in grid:
    p.addVariables(row,range(cols,0,-1))
    p.addConstraint(AllDifferentConstraint(),row)

green=[['104','129'],['093','118'],['053','081'],['108','135'],['069','147'],
       ['109','111'],['048','149'],['025','141'],['061','081'],['024','108'],
       ['107','144'],['028','121'],['016','072'],['035','144'],['075','114'],
       ['097','144'],['019','114'],['076','137'],['013','144'],['044','113'],
       ['082','099'],['116','134'],['047','135'],['054','114'],['032','143'],
       ['017','122'],['094','148'],['059','136'],['059','073'],['049','107'],
       ['117','126'],['063','146'],['114','128'],['118','127'],['071','135'],
       ['022','123'],['089','105'],['067','112'],['034','136'],['083','108'],
       ['056','137'],['031','135'],['062','145'],['083','127'],['102','145'],
       ['123','145'],['101','113'],['089','092'],['049','058'],['021','113'],
       ['079','148'],['125','138'],['134','145'],['011','123'],['046','079']]

'''green=[]
while True:
  gcell=input('enter green clue')
  if gcell=='.':
    break
  if (len(str(rows))+1)*2==len(gcell):
      green.append([gcell[0:int(len(gcell)/2)],gcell[int(len(gcell)/2):]])
  else:
    continue'''

for clue in green:
  p.addConstraint(AllEqualConstraint(),clue)

red=  [['086','129'],['077','115'],['086','103'],['072','146'],['052','116'],
       ['036','086'],['066','117'],['106','139'],['112','136'],['096','101'],
       ['064','135'],['096','139'],['072','138'],['099','141'],['128','149'],
       ['045','052'],['078','138'],['097','125'],['106','112'],['051','145'],
       ['086','122'],['088','113'],['036','121'],['027','096'],['043','075'],
       ['112','149'],['076','143'],['052','093'],['121','133'],['057','134'],
       ['073','142'],['037','106'],['072','112'],['084','141'],['064','144'],
       ['043','146'],['112','129'],['061','148'],['075','106'],['027','119'],
       ['078','145'],['036','103'],['019','041'],['103','128'],['128','133'],
       ['026','129'],['045','054'],['103','122'],['082','136'],['014','108'],
       ['087','095'],['097','121'],['131','143'],['014','129'],['012','066'],
       ['036','123'],['068','144'],['067','138'],['039','134'],['119','125'],
       ['112','121'],['135','146'],['012','124'],['112','144'],['099','115'],
       ['101','146'],['088','137'],['037','111'],['033','145'],['014','103'],
       ['098','103'],['084','101'],['029','143'],['089','146'],['105','139'],
       ['088','146'],['095','122'],['085','137'],['056','096'],['052','094'],
       ['136','146'],['037','145'],['094','124'],['014','135'],['053','131'],
       ['029','138'],['029','119'],['088','148'],['039','096'],['079','106'],
       ['111','148'],['045','141'],['079','131'],['015','137'],['068','132'],
       ['051','118'],['068','093']]
'''red=[]
while True:
  rcell=input('enter green clue')
  if rcell=='.':
    break
  if (len(str(rows))+1)*2==len(rcell):
      red.append([gcell[0:int(len(gcell)/2)],gcell[int(len(gcell)/2):]])
  else:
    continue'''

for clue in red:
  p.addConstraint(AllDifferentConstraint(),clue)

# get solution
start=time.time()
sol = p.getSolution()
end=time.time()

# print the answers
Ogrid=[]
for Orow in range(1,len(grid)+1):
  if len(str(Orow))<2:
    Ogrid.append([('L0'+str(Orow)) if i == 0 else ''  for i in range(cols+1)])
  elif len(str(Orow))==2:
    Ogrid.append([('L'+str(Orow)) if i == 0 else ''  for i in range(cols+1)])

for rownum,row in enumerate(grid):
  for cell in row:
    Ogrid[rownum][sol[cell]]=cell


# put the answers in the correct order of solution
print('\n\n', 'The calculated solution:', '\n')

for r in Ogrid:  
  print(f'{r[0]:>5s}: ', end='')
  for i in range(1, cols+1):
    print(f'{r[i]:>5s}',end='')
  print()
print()

print('time elapsed: ' , end-start)