from flask import render_template, request, redirect,url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("task.html")


@app.route("/categories")
def categories():
    categories = Category.query.order_by(Categary.category_name).all()
    return render_template("categories.html",categories=catagories)
    

@app.route("/add_category", methods=["GET","POST"])
def add_category():
    if request.method == "POST":
        category = list(Category(category_name=request.form.get("category_name")))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")

