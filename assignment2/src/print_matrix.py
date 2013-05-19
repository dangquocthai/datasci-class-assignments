import sys
import sqlite3 as sq

vals = {}

def main():
  table_name = sys.argv[1]
  con = sq.connect('../matrix.db')

  with con:
    cur = con.cursor()
    cur.execute("select * from " + table_name)
    rows = cur.fetchall()

  for row in rows:
    r,c,v = row
    vals[(r,c)] = v

  with con:
    cur = con.cursor()
    cur.execute('select max(row_num), max(col_num) from ' + table_name)
    result = cur.fetchone()
    max_row, max_col = result
    print "Max row = ", max_row , "; Max col = ", max_col

  for row in range(max_row):
    for col in range(max_col):
      element = vals.get((row, col), 0)
      print element , "\t" ,
    print "\n"

  print "----------Transpose matrix----------"
  for row in range(max_row):
    for col in range(max_col):
      element = vals.get((col, row), 0)
      print element , "\t" ,
    print "\n"

if __name__ == "__main__":
  main()
