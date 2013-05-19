-- In matix mulplication, C[row_num, col_num] = sum(A.col_num * B.row_num).
-- So,
-- select a.row_num, a.col_num, b.row_num, b.col_num, a.value, b.value, (a.value * b.value) as val from a, b where a.col_num = b.row_num order by a.row_num, b.col_num;
-- given row, col, and values of multiplications of the index will go.
-- To sum them up,
-- select a.row_num, b.col_num, (a.value * b.value) from a, b where a.col_num = b.row_num;
-- Now col 1 and col 2, are the indexes, but there will be duplicates in combination of col1 and col2, these should be added up, so:
-- select a.row_num r, b.col_num c, sum(a.value * b.value) from a, b where a.col_num = b.row_num group by r,c;
-- is the final answer.

.output '../output/multiply.txt'
select val from
(
select a.row_num r, b.col_num c, sum(a.value * b.value) as val from a, b where a.col_num = b.row_num group by r,c having r=2 and c=3
);

.output stdout
select "All done, result in ../outout/multiply.txt";
