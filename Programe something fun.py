from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>', name=name)


#ajax('aaa.txt?t=' + new Date().getTime(), function(str){}, fucntion{})

