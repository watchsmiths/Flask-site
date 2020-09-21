from app import app, db
from app.models import Brands, Products

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'Brands':Brands, 'Products':Products}

if __name__ == "__main__":
    app.run(debug=True)