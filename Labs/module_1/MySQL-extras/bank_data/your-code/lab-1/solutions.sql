#Lab | SQL - Selection 

#1
select client_id 
from client
where district_id like 1
limit 5;

#2
select client_id
from client
where district_id like 72
order by client_id DESC
limit 1;

#3
select amount
from loan
order by amount ASC
limit 3;

#4
select DISTINCT status
from loan
order by status ASC;

#5
select loan_id
from loan
order by payments DESC
limit 1;

#6
select account_id, amount
from loan
order by account_id ASC
limit 5;

#7
select account_id
from loan
where duration like 60
order by amount ASC
limit 5;

#8
select distinct(k_symbol)
from `order`
order by k_symbol ASC;

#9
select order_id
from `order`
where account_id like 34;

#10
select distinct(account_id)
from `order`
where order_id > 29540
and order_id <= 29560;


#11
select amount
from `order`
where account_to like 30067122; 

#12
select trans_id, date, type, amount
from trans 
where account_id = 793
order by date DESC
limit 10;







