#CHALLENGE 1 => who are the top 3 most profiting authors by using sub queries

select AuthorID, sum(Advance + Aggregated_royalties) as Total_profit

from (
	select TitleID, AuthorID, sum(Advance) as Advance, round(sum(Sales_royalty),0) as Aggregated_royalties
	from (
		select ta.title_id as TitleID, ta.au_id as AuthorID, round(t.advance * ta.royaltyper / 100) as Advance, 		round(t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100,2) as Sales_royalty
		from titleauthor ta
		join titles t
		on ta.title_id = t.title_id
		join sales s
		on t.title_id = s.title_id
	) summary
	group by TitleID, AuthorID
) sub_summary
group by AuthorID
order by Total_profit DESC
limit 3;


#CHALLENGE 2 => who are the top 3 most profiting authors by using temporary tables

CREATE TEMPORARY TABLE publications.store_sales_summary_2
select ta.title_id as TitleID, ta.au_id as AuthorID, round(t.advance * ta.royaltyper / 100) as Advance, round(t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100,0) as Sales_Royalty
from titleauthor ta
join titles t
on ta.title_id = t.title_id
join sales s
on t.title_id = s.title_id;

Select * 
from publications.store_sales_summary_2;




CREATE TEMPORARY TABLE publications.store_sales_summary_middle
select TitleID, AuthorID, sum(Advance) as Advance, round(sum(Sales_Royalty),0) as Aggregated_royalties
from publications.store_sales_summary_2 summary
group by TitleID, AuthorID;

Select * 
from publications.store_sales_summary_middle;




select AuthorID, sum(Advance + Aggregated_royalties) as Total_profit
from publications.store_sales_summary_middle
group by AuthorID
order by Total_profit DESC
limit 3;




#CHALLENGE 3

CREATE TEMPORARY TABLE most_profiting_authors
select AuthorID, sum(Advance + Aggregated_royalties) as Total_profit
from publications.store_sales_summary_middle
group by AuthorID
order by Total_profit DESC
limit 3;

Select * 
from most_profiting_authors;



