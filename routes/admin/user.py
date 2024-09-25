from app import app, render_template, request


@app.get('/admin/user')
def user():
    module = 'user'
    return render_template('admin/user.html', module=module)
