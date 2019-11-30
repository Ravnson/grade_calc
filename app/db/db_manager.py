import os
import json

path = 'app/grades/db/'

def get_classes():
    return get_resources(path + 'classes/')

def create_class(name):
    create_resource(path + 'classes', name)

def rem_class(name):
    rem_resource(path + 'classes', name)

def get_class(name):
    return get_resource(path + 'classes', name)

def save_class(name):
    save_resource(path + 'classes', name)

def get_layouts():
    return get_resource(path + 'layouts/')

def create_layout(name):
    create_resource(path + 'layouts', name)

def rem_layout(name):
    rem_resource(path + 'layouts', name)

def get_layout(name):
    return get_resource(path + 'layouts', name)

def save_layout(name):
    save_resource(path + 'layouts', name)

def get_resources(resource):
    res = os.listdir(resource)
    try:
        return list(map(lambda x : x[:-5], res))
    except FileNotFoundError:
        print('No ' + res + ' exists')

def create_resource(res, name):
    try:
        fname = res + '/' + name + '.json'
        nfile = open(fname, "w+")
        nfile.close()
    except FileExistsError:
        print('Course already exists')

def rem_resource(res, name):
    try:
        fname = res + '/' + name + '.json'
        os.remove(fname)
        print('Removed ' + fname)
    except FileNotFoundError:
        print('Course doesn\'t exist')

def get_resource(res, name):
    try:
        fname = res + '/' + name + '.json'
        with open(fname, 'r') as f:
            res = json.load(f)
            f.close()
            return res
    except FileNotFoundError:
        print('No such ' + res)
    except JSONDecoderError:
        print('Somthing went wrong with the parsing')

def save_resource(res, name, dic):
    try:
        fname = res + '/' + name + '.json'
        with open(fname, 'w') as f:
            f.write(json.dumps(dic, indent=2))
            f.close
            return
    except FileNotFoundError:
        print('No such ' + res)
