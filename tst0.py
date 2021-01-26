import pandas as pd


df=pd.read_csv('data_analytics.csv')
n=0
sub_id = dict() #
LTV = 0
count_subs = 0
for col in range(len(df)):
    id = df['Subscriber ID'][col]
    if sub_id.get(id) == None:
        sub_id[id] = {'Trial':0,'Sub':0}
    if df['Subscription Offer Type'][col] == 'Free Trial':
        sub_id[id]['Trial'] +=1
    else:
        sub_id[id]['Sub'] +=1
        count_subs+=1


LTV=6.99*count_subs

print(LTV)

input()
