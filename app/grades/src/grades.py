def fill_grade_tree(comp_key, grades):
    for g in comp_key._grade:
        if g.get_name() in grades:
            g.add_grade(grades[g.get_name()])
        if g.is_grade():
            return
        fill_grade_tree(g, grades)

def compute(comp_key, grades):
    fill_grade_tree(comp_key, grades)
    return comp_key.compute_grades()

class Grade:

    def __init__(self, name, weight=1, grade=-1):
        ''' Initialize Grade.

        Set name, weight with default weight 1.
        Set grade list as an empty list, if no grade
        given, else set it as list containing the grade'''
        self._name = name
        self._weight = weight
        if (grade == -1):
            self._grade = []
        else :
            self._grade = [grade]

    def get_name(self):
        return self._name

    def get_weight(self):
        return self._weight

    def get_grades(self):
        return self._grade

    def set_weight(self, weight):
        self._weight = weight

    def add_grade(self, grade):
        self._grade.append(grade)

    def remove_grade(self, name):
        ''' Tree-like removal

        Remove Grade by name reference'''
        for g in self._grade:
            if (type(g) == int):
                return
            if g._name == name:
                self._grade.remove(g)
            else:
                g.remove_grade(name)

    def is_grade(self):
        ''' Checks if grade is a grade or a grade container '''
        if self._grade == []:
            return True
        for g in self._grade:
            if type(g) == int:
                return True
        return False

    def get_table(self):
        ''' Returns a list containing all names of grade/grade container '''
        res = []
        for g in self._grade:
            if type(g) != int:
                res.append(g.get_name())
                if g.get_table() != []: 
                    res.append(g.get_table())
        return res
    
    def get_by_layer(self):
        queue = [self]
        res = [self._name]
        while queue:
            obs = queue.pop(0)

            

    def size(self):
        count = 0
        if self.is_grade():
            return len(self._grade)
        for g in self._grade:
            count += g.size()
        return count

    def compute_grades(self):
        count = 0
        weight = 0
        if self.is_grade():
            return 0 if self._grade == [] else self._grade[0]
        for g in self._grade:
            count += (g.compute_grades() * g.get_weight())
            weight += g.get_weight() 
        return (count / weight)
