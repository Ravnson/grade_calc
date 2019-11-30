import grades


def json_to_grades(name, gra):
    b = grades.Grade(name, gra['weight'])
    for n, g in gra['children'].items():
        if n is None: 
            continue
        b.add_grade(json_to_grades(n, g))
    return b

def grades_to_json(gra):
    graNam = gra.get_name()
    graWei = gra.get_weight()
    graChil = {}
    for g in gra.get_grades():
        graChil.update(grades_to_json(g))
    return  {graNam: {"weight": graWei, "children" : graChil}}
