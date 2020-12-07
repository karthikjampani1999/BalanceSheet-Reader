
share_capital =int(input("share_capital :"))
longterm_liabilities = int(input("longterm_liabilities ? :"))
reserves_and_surplus = int(input(" reserves_and_surplus :"))
longterm_assets = int(input("longterm_assets :"))
current_liabilities = int(input("current_liabilities :"))
current_assets = int(input("current_assets :"))


LTS = share_capital + longterm_liabilities + reserves_and_surplus #LTS :: LONGTERM SUPPLIES
LTU = longterm_assets # LTU :: LONGTERM USES
STS = current_liabilities # STS :: SHORTTERM SUPPLIES
STU = current_assets # STU :: SHORTTERM USES

if LTS == LTU and STS == STU:
  print('average company :| ')
if LTS > LTU and STS < STU:
  print('good company bro :) ')
if LTS < LTU and STS > STU:
  print('poor health bro :(  ')
