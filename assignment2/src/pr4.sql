.output '../output/keyword_search.txt'
select f1.docid, sum(f1.count * f2.count) as count from frequency f1,
(
    SELECT 'q' as docid, 'washington' as term, 1 as count 
    UNION
    SELECT 'q' as docid, 'taxes' as term, 1 as count
    UNION 
    SELECT 'q' as docid, 'treasury' as term, 1 as count
) as f2
where f1.term = f2.term
group by f1.docid = f2.docid
order by count desc
limit 1;

.output stdout
select "All done, results in ../output/keyword_search.txt";
