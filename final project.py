#CONNECTING MYSQL 
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="tiger")
cur=mycon.cursor()

#CREATING DATABASES

cur.execute("create database if not exists pnl")
cur.execute("use pnl")

# CREATING TABLES

cur.execute("create table if not exists supply (medi_name varchar(50),company varchar(50),quantity integer,b_tax integer,s_tax integer,b_cost integer,profit integer,selling_cost integer,rate integer)")
cur.execute("create table if not exists customer (name_cust varchar(50),date date,medi_name varchar(50),company varchar(50),quantity  integer,tax integer,rate integer,selling_cost integer)")
mycon.commit()
print("                             ***********************WELCOME TO PROFIT AND LOSS AYALYSIS SYSTEM************************                              ")
print("")
print("\npress 1 to enter stock ")
print("press 2 to buy a medicine")
print("press 3 to show sellout details")
print("press 4 to show customer")
print("press 5 to show stock")
print("press 6 to check sale of one medicine")
print("press 7 to check sale of all medicine ")
print("press 8 to check earn from one medicine")
print("press 9 to check earn from all medicine")
print("press 10 to check profit from one medicine")
print("press 11 to check profit from all medicine ")
print("press 12 to see monthly report")
print("press 13 to see target")
print("press 14 to see profit")
print("press 15 to see net profit or loss")
print('press 16 to logout')

while True:

 ch=int(input("\nEnter your choice:"))

# TO INPUT STOCK IN SUPPLY

 if ch==1:
  name=input("mediname")
  comp=input("company")
  quantity=input('quantity')
  btax=input("btax")
  stax=input("stax")
  rate=input("rate")
  bcost=input("bcost")      
  profit=input("profit")
  sellingcost=input("selling_cost")
  st="insert into supply (medi_name,company,quantity,b_tax,s_tax,b_cost,profit,selling_cost,rate) values('{}','{}',{},{},{},{},{},{},{})".format(name,comp,quantity,btax,stax,bcost,profit,sellingcost,rate)
  cur.execute(st)
  cur.execute("select * from supply")
  print("TABLE:STOCK(SUPPLY)")
  print("\nmedi_name,company,quantity,b_tax,s_tax,b_cost,profit,selling_cost,rate")
  for i in cur:
    print(i)
  mycon.commit()

# TO BUY MEDICINE

 if ch==2:   
  name=input('name of customer')
  date=input('date')
  mediname=input('name of medicine')
  qua=int(input('quantity'))
  sp=input('selling price')
  quan=int(input("Enter initial quantity from stock"))
  rate=input('rate')
  st="insert into customer (name_cust,date,medi_name,quantity,rate,selling_cost) values('{}','{}','{}',{},{},{})".format(name,date,mediname,qua,rate,sp)
  cur.execute(st)
  st2="update supply set quantity={} where medi_name='{}'".format(quan-qua,mediname)
  cur.execute(st2)
  cur.execute("select * from customer")
  print("CUSTOMERS")
     
  print("\nname_cust,date,medi_name,quantity,selling_cost")
  for i in cur:
            print(i)
  mycon.commit()

# TO GET SLIP

 if ch==3:
    print("\nTABLE TO ALL DETAILS OF  MEDICINE PURSHASED")
    print("\nDATE,NAME OF CUSTOMER,MEDICINE,QUANTITY,SELLING-COST,B-TAX,S-TAX,B-COST,REMAINING STOCK")
    cur.execute("select customer.date,customer.name_cust,customer.medi_name,customer.quantity as quantity_ofproduct,customer.selling_cost,supply.b_tax,supply.s_tax,b_cost,supply.quantity as remaining_stock from supply inner join customer on supply.medi_name =customer.medi_name")
    for i in cur:
      print(i)
    mycon.commit()

# TO SHOW CUSTOMERS

 if ch==4:
  print("\nCUSTOMERS DETAILS")
  print("\nname of customer,date,medicine,quantity,selling cost")
  cur.execute('select name_cust,date,medi_name,quantity,selling_cost from customer ')
  for i in cur :
      print(i)
  mycon.commit()
    
# TO SHOW STOCK(SUPPLY)

 if ch==5:
     print("\nSTOCK")
     print("\nmedi_name,company,quantity,b_tax,s_tax,b_cost,profit,selling_cost,rate")
     cur.execute("select*from supply")
     
     for i in cur :
       print(i)
     mycon.commit()
     
#TOTAL MEDICINE SELL OF ONE TYPE
     
 if ch==6:
     cur.execute("select customer.date,customer.medi_name,customer.quantity as sellout,supply.rate,supply.selling_cost from supply inner join customer on supply.selling_cost=customer.selling_cost")
     cur.fetchall()
     medi_name=input("medi_name")

     print("\nTOTAL MEDICINE SELL OF MEDICINE NAME:",medi_name)
     print("\nname of medicine,quantity sellout")
     st="select medi_name,SUM(quantity)'sellout' from customer where medi_name='{}'".format(medi_name)
     cur.execute(st)
     for i in cur:
         print(i)
     mycon.commit()
 
# TOTAL QUANTITY OF ALL MEDICINE SELL

 if ch==7:
     print("TOTAL QUANTITY OF ALL MEDICINE SELL")
     print("\nname of medicine,quantity sellout")
     cur.execute("select medi_name,SUM( quantity)'sellout quantitiy' from customer group by medi_name")
     for i in cur:
         print(i)
     mycon.commit()
     
# COST GAIN FROM ONE MEDICINE

 if ch==8:
     name=input("\nmedi_name:")
     cur.execute("select SUM( quantity)'sellout quantity',medi_name from customer group by medi_name")
     cur.fetchall()
     print("\nCOST GAIN FROM MEDICINE:",name)
     print("\nmedicine,cost gained")
     st="select medi_name,SUM( quantity)*selling_cost as cost_gain from customer where medi_name='{}'".format(name)
     cur.execute(st)
     for i in cur:
         print(i)
     mycon.commit()
     
# COST GAIN FROM ALL MEDICINES

 if ch==9:
     print("\nCOST GAIN ALL MEDICINE")
     print("\nmedicine,cost gained")
     cur.execute("select medi_name,sum(quantity)*selling_cost as cost_gain from customer group by medi_name")
     for i in cur:
         print(i)
     mycon.commit()
     
# PURE PROFIT FROM ONE MEDICINE

 if ch==10:
    name=input("enter medi_name")
    print("\nPURE PROFIT FROM  MEDICINE:",name)
    print("\nname of medicine,profit gained")
    st="select medi_name,(SUM( quantity)*selling_cost)-(rate*SUM( quantity)) from customer where medi_name='{}'".format(name)
    cur.execute(st)
    for i in cur:
         print(i)
    mycon.commit()
    
#PURE PROFIT FROM ALL MEDICINES
    
 if ch==11:
     print("\nPURE PROFIT FROM ALL MEDICINES")
     print("\nname of medicine,profit gained")
     cur.execute("select medi_name,(SUM( quantity)*selling_cost)-(rate*SUM( quantity)) from customer group by medi_name")
     for i in cur:
         print(i)
         
#MONTHLY REPORT

 if ch==12:
     a=input("from date")
     b=input("to date")
     print("\nMONTHLY REPORT")
     print("\nmedicine,    sellout,          profit,        rate,selling cost")
     st="select medi_name,(sum((quantity*selling_cost)-(rate*quantity))/(selling_cost-rate)) as sellout_stock,(SUM( quantity)*selling_cost)-(rate*sum(quantity)) as profit,rate,selling_cost from customer where date between '{}' and '{}' group by medi_name".format(a,b)
     cur.execute (st)
     for i in cur:
         print(i)
     mycon.commit()
     
# TARGET

 if ch==13:
     print("\nTARGET")
     print("\nmedicine,quantity to sale,cost to gain,cost to gain with profit")
     cur.execute("select medi_name,quantity as quantity_tosale,(quantity*rate) as to_gain,(quantity*selling_cost)as to_gainwithprofit from supply group by medi_name")
     for i in cur:
         print(i)
     mycon.commit()
     
# PROFIT OR LOSS

 if ch==14:
     print("\nPROFIT OR LOSS FROM ALL MEDICINE")
     print("\nmedi_name,(sum(customer.quantity)),selling_cost,rate,stock,b_cost,profitorloss,% profitloss")
     st="select customer.medi_name,(sum(customer.quantity)),customer.selling_cost,customer.rate,supply.quantity as stock,supply.b_cost,(sum(customer.quantity)*supply.rate-b_cost)as profitorloss,(sum(customer.quantity)*supply.rate-b_cost)/100  as '% profitloss' from supply inner join  customer on supply.rate=customer.rate group by medi_name"
     cur.execute(st)
     for i in cur:
         print(i)
     mycon.commit()
     
#NET PROFIT OR LOSS
     
 if ch==15:
     print("\nNET PROFIT OR LOSS IN BUSINESS")
     print("\nnet profit or loss,stock")
     st="select (sum(customer.quantity))-(sum(supply.b_cost)) as netprofitloss,(sum(supply.quantity)) as stock from supply inner join customer on supply.rate=customer.rate"
     cur.execute(st)
     for i in cur:
         print(i)
     mycon.commit()

# TO LOGOUT

 if ch==16:
     print("THANK YOU TO VISIT \nYOU LOGOUT FROM CODE")
     break





     
