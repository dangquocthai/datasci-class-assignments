-- Solutions to problem 1, in assignment 2.

-- Set up modes.
.output stdout
.header off
-- Problem 1: (a): select: Write a query that is equivalent to the following relational algebra expression.

-- σ docid=10398_txt_earn(frequency)
-- Interpretation: Select from frequency table, where condition docid=10398_txt_earn is True.
.output '../output/select.txt'

-- Answer 1:
select
    count(1)
from
    Frequency
where
    docid='10398_txt_earn';

.output stdout
select "Wrote Answer 1(a) to ../output/select.txt";
-- End problem 1(a)

-- Problem 1: (b): select project: Write a SQL statement that is equivalent to the following relational algebra expression.

-- πterm( σdocid=10398_txt_earn and count=1(frequency))
-- Interpretation: select terms from from frequency where docid=10398_txt_earn and count=1
.output '../output/select_project.txt'

-- Answer 1(b)
select
    count(1)
from
    frequency
where
    docid='10398_txt_earn'
    and
    count=1;

.output stdout
select "Wrote Answer 1(b) to ../output/select_project.txt";
-- End 1(b)

-- Problem 1 : (c):  union: Write a SQL statement that is equivalent to the following relational algebra expression. (Hint: you can use the UNION keyword in SQL).

-- πterm( σdocid=10398_txt_earn and count=1(frequency)) 
-- U 
-- πterm( σdocid=925_txt_trade and count=1(frequency))
.output '../output/union.txt'

-- Answer 1(c)
select 
    count(term) 
from
(
    select term from frequency where docid='925_txt_trade' and count=1
    union
    select term from frequency where docid='10398_txt_earn' and count=1
);

.output stdout
select "Wrote Answer 1(c) to ../output/union.txt";
-- End 1(c)

-- Problem 1: (d): Write a SQL statement to count the number of documents containing the word “parliament”
.output '../output/count.txt'

-- Answer 1(d)
select count(*) from frequency where term='parliament';

.output stdout
select "Wrote Answer 1(d) to ../output/count.txt";
-- End 1(d)

-- Problem 1: (e): big documents Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms. (Hint: You can use the HAVING clause, or you can use a nested query. Another hint: Remember that the count column contains the term frequencies, and you want to consider duplicates.) (docid, term_count)
.output '../output/big_documents.txt'

-- Answer 1(e)
select count(1) from
(
select docid, sum(count) as t_ct from frequency group by docid having t_ct > 300
);

.output stdout
select "Wrote Answer 1(e) to ../output/big_documents.txt";
-- End 1(e)

-- Problem 1: (f):  two words: Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.
.output '../output/two_words.txt'

-- Answer 1(f)
select
    count(t.docid)
from
    frequency t
    , frequency w
where
    t.term = 'transactions'
    and
    w.term = 'world'
    and 
    t.docid = w.docid;
-- Another method
--select t.docid
--from frequency t
--inner join frequency w
--on t.docid = w.docid
--where t.term = 'transactions'
--and w.term = 'world'
  /
.output stdout
select "Wrote Answer 1(f) to ../output/two_words.txt";
-- End 1(f)
select "All done.";
