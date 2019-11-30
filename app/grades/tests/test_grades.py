from lib import grades
import pdb

g = grades.Grade('my_table')

m = grades.Grade('muendlich', 1)

s = grades.Grade('schriftlich', 2)

s.add_grade(grades.Grade('Klausur 1', 1, 3))
s.add_grade(grades.Grade('Klausur 2', 1, 1))
s.add_grade(grades.Grade('Klausur 3', 1, 2))
s.add_grade(grades.Grade('Klausur 3', 1, 4))

m.add_grade(grades.Grade('Mdl 1', 2, 5))
m.add_grade(grades.Grade('Mdl 2', 1, 2))
m.add_grade(grades.Grade('Mdl 3', 4, 1))

g.add_grade(s)
g.add_grade(m)

assert g.size() == 7 
assert g.compute_grades() == 2.4285714285714284

