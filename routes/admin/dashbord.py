from app import app, render_template, request


@app.get('/dashboard')
@app.get('/admin')
def dashboard():
    return render_template('admin/layout.html')
