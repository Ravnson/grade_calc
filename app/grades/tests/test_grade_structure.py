from lib import grades
import pdb

g = grades.Grade('my_table')

m = grades.Grade('muendlich', 2)

s = grades.Grade('schriftlich', 3)

s.add_grade(grades.Grade('Klausur 1', 1))
s.add_grade(grades.Grade('Klausur 2', 1))
s.add_grade(grades.Grade('Klausur 3', 1))
s.add_grade(grades.Grade('Klausur 4', 1))

t = grades.Grade('test', 1)

s.add_grade(t)

m.add_grade(grades.Grade('Mdl 1', 1))
m.add_grade(grades.Grade('Mdl 2', 1))
m.add_grade(grades.Grade('Mdl 3', 1))

t.add_grade(grades.Grade('Test 1', 1))
t.add_grade(grades.Grade('Test 2', 1))
t.add_grade(grades.Grade('Test 3', 1))
t.add_grade(grades.Grade('Test 4', 1))



g = grades.Grade('my_table')

m = grades.Grade('muendlich', 1)

s = grades.Grade('schriftlich', 2)

s.add_grade(grades.Grade('Klausur 1', 1))
s.add_grade(grades.Grade('Klausur 2', 1))
s.add_grade(grades.Grade('Klausur 3', 1))
s.add_grade(grades.Grade('Klausur 3', 1))

m.add_grade(grades.Grade('Mdl 1', 2))
m.add_grade(grades.Grade('Mdl 2', 1))
m.add_grade(grades.Grade('Mdl 3', 4))

g.add_grade(s)
g.add_grade(m)
