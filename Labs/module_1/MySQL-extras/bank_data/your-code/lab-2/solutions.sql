#Challenge 2

#1
select DISTINCT(district_id), count(client_id)
from client
where district_id < 10
group by district_id
order by district_id ASC;

#2
select type, count(type) as 'Total'
from card
group by type;

#3
select account_id, sum(amount)
from loan
group by account_id
order by sum(amount) DESC
limit 10;

#4
select date, count(loan_id)
from loan
where date < 930907
group by date
order by date DESC

#5
select date, duration, count(loan_id)
from loan
where date like '9712%'
group by date, duration
order by date ASC;

#6
select account_id, type, sum(amount) as total_amount
from trans
where account_id = 396
group by type
order by type ASC;

#7
UPDATE trans
SET type = 'Incoming'
where type = 'PRIJEM';

UPDATE trans
SET type = 'Outgoing'
where type = 'VYDAJ';

select account_id, type as transaction_type, round(sum(amount),0) as total_amount
from trans
where account_id = 396
group by type
order by type ASC;


#8
CREATE TEMPORARY TABLE incoming_result
select account_id, type as transaction_type, round(sum(amount),0) as total_amount
from trans
where account_id = 396
and type = 'Incoming'
group by type
order by type ASC;

CREATE TEMPORARY TABLE outgoing_result
select account_id, type as transaction_type, round(sum(amount),0) as total_amount
from trans
where account_id = 396
and type = 'Outgoing'
group by type
order by type ASC;

Select i_r.account_id, i_r.total_amount, o_r.total_amount, i_r.total_amount-o_r.total_amount as Difference
from incoming_result i_r
join outgoing_result o_r
on i_r.account_id = o_r.account_id;



#9
CREATE TEMPORARY TABLE incoming_result_3
select account_id, type as transaction_type, round(sum(amount),0) as total_amount
from trans
where type = 'Incoming'
group by account_id
order by type ASC;

CREATE TEMPORARY TABLE outgoing_result_3
select account_id, type as transaction_type, round(sum(amount),0) as total_amount
from trans
where type = 'Outgoing'
group by account_id
order by type ASC;


Select i_r.account_id, i_r.total_amount-o_r.total_amount as Difference
from incoming_result_3 i_r
join outgoing_result_3 o_r
on i_r.account_id = o_r.account_id
order by Difference DESC
limit 10;























