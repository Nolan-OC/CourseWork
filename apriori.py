# remove pandas warning
import warnings
warnings.filterwarnings('ignore')
# -------------------------------
import mysql.connector
import pandas as pd
import functions as my_funcs
import time

conn = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="root",
  database="cs637_midterm"
)

transaction_list = []
t_2023 = pd.read_sql('SELECT * FROM transactions_2023', con=conn)
t_2022 = pd.read_sql('SELECT * FROM transactions_2022', con=conn)
t_2021 = pd.read_sql('SELECT * FROM transactions_2021', con=conn)
t_2020 = pd.read_sql('SELECT * FROM transactions_2020', con=conn)
t_2019 = pd.read_sql('SELECT * FROM transactions_2019', con=conn)

# TESTING SET ONLY
test = pd.read_sql('SELECT * FROM test', con=conn)
test_list = test.groupby('transaction_id')['item_id'].apply(list).tolist()

tlist_2023 = t_2023.groupby('transaction_id')['item_id'].apply(list).tolist()
tlist_2022 = t_2022.groupby('transaction_id')['item_id'].apply(list).tolist()
tlist_2021 = t_2021.groupby('transaction_id')['item_id'].apply(list).tolist()
tlist_2020 = t_2020.groupby('transaction_id')['item_id'].apply(list).tolist()
tlist_2019 = t_2019.groupby('transaction_id')['item_id'].apply(list).tolist()

conn.close()

#------------------
support_threshold = float(input("please enter the support threshold\n"))
confidence_threshold = float(input("please enter the confidence threshold\n"))
#------------------
data_point = int(input("which dataset would you like to run? Please input an integer for choice\n 1- Transactions2023\n "
                   "2- Transactions2022\n 3- Transactions2021\n 4- Transactions2020\n 5- Transactions2019\n"))
if data_point == 1:
  transaction_list = tlist_2023
elif data_point == 2:
  transaction_list = tlist_2022
elif data_point == 3:
  transaction_list = tlist_2021
elif data_point == 4:
  transaction_list = tlist_2020
elif data_point == 5:
  transaction_list = tlist_2019
else:
  print("Please restart and input a valid integer 1-5")

start_time = time.time()
# get unique single unique elements from dataset
unique_ints = sorted(set([i for sublist in transaction_list for i in sublist]))
unique_groups = my_funcs.unique_groupings(1, unique_ints)
print(unique_ints)
print(unique_groups)

i = 0
rules = []
while len(unique_groups) != 0:
  print(f"~~~~~We begin a new loop: {i+1} at {time.time()-start_time} seconds~~~~~")
  unique_ints = sorted(set([i for sublist in unique_groups for i in sublist]))
  if i != 0:
    unique_groups = my_funcs.unique_groupings(i + 1, unique_ints)
  print(f"The selected transaction list is {transaction_list}")
  print(f"The unique elements are {unique_groups}")

  # check the support of each unique grouping and then drop any below threshold
  supported_groups = my_funcs.calculate_support(unique_groups, transaction_list)
  unique_groups = my_funcs.drop_check(supported_groups, support_threshold, unique_groups)
  print(f"New working list: {unique_groups}")
  print(f"Transaction List: {transaction_list}")

  if(i != 0):
    # if confidence high enough add to list of rules
    supported_confidence = my_funcs.calculate_confidence(unique_groups, transaction_list)
    unique_groups = my_funcs.drop_check(supported_confidence, confidence_threshold, unique_groups)

    print(f"New working list: {unique_groups}")
    print(f"Transaction List: {transaction_list}")
    rules+=(my_funcs.new_rules(unique_groups, transaction_list))

  i+=1

print(f"\nThe program has completed running in {i} iterations.\nWe generated {len(rules)} new rules"
      f"that satisfy Support > {support_threshold} and Confidence > {confidence_threshold}")
print(f"The program took {time.time()-start_time} seconds to complete")
for rule in rules:
  print(rule)