from app import app, render_template, request


@app.get('/dashboard')
@app.get('/admin')
def dashboard():
    module = 'dashboard'
    return render_template('admin/dashboard.html', module=module)
