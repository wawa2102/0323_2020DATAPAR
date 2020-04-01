#LAB | SQL | Extra

#Challenge 1

select max(price), min(price)
from order_items;


#Challenge 2

select min(shipping_limit_date), max(shipping_limit_date)
from order_items;


#Challenge 3

select count(customer_id), customer_state
from customers 
group by customer_state
order by count(customer_id) desc;


#Challenge 4

select count(customer_id), customer_city, customer_state
from customers 
where customer_state like 'SP'
group by customer_city, customer_state 
order by count(customer_id) desc;


#Challenge 5 

select count(distinct(business_segment))
from closed_deals;

#Challenge 6

select business_segment, sum(declared_monthly_revenue)
from closed_deals
group by business_segment
order by sum(declared_monthly_revenue) desc
limit 3;

#Challenge 7

select count(distinct(review_score))
from order_reviews;


#Challenge 8

#Didn't understand the question what is number category ?


#Challenge 9

select review_score, count(review_score)
from order_reviews
group by review_score
order by count(review_score) DESC
limit 1;




















