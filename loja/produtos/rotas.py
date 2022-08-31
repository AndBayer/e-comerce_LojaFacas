from flask import redirect, render_template, url_for, flash, request
from .forms import Addprodutos
from loja import db, app, photos
from .models import Marca, Categoria, Addproduto
import secrets


@app.route('/addmarca', methods=['GET','POST'])
def addmarca():
    if request.method == "POST":
        getmarca = request.form.get('marca')
        marca = Marca(name=getmarca)
        db.session.add(marca)
        flash(f'A marca {getmarca} foi cadastrada com sucesso','success')
        db.session.commit()
        return redirect(url_for('addmarca'))
    return render_template('/produtos/addmarca.html', marcas='marcas')


@app.route('/addcat', methods=['GET','POST'])
def addcat():
    if request.method == "POST":
        getmarca = request.form.get('categoria')
        cat = Categoria(name=getmarca)
        db.session.add(cat)
        flash(f'A categoria {getmarca} foi cadastrada com sucesso','success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('/produtos/addmarca.html')


@app.route('/addproduto', methods=['GET','POST'])
def addproduto():
    marcas = Marca.query.all()
    categorias = Categoria.query.all()
    form = Addprodutos(request.form)
    if request.method == "POST":

        name     = form.name.data
        price    = form.price.data
        discount = form.discount.data
        stock    = form.stock.data
        colors   = form.colors.data
        desc     = form.description.data
        marca    = request.form.get('marca')
        categoria= request.form.get('categoria')

        image_1 = photos.save(request.files.get('image_1'),name=secrets.token_hex(10)+".")
        image_2 = photos.save(request.files.get('image_2'),name=secrets.token_hex(10)+".")
        image_3 = photos.save(request.files.get('image_3'),name=secrets.token_hex(10)+".")

        addpro = Addproduto(name=name, price=price, discount=discount, stock=stock, colors=colors, desc=desc,
        marca_id=marca, categoria_id=categoria, image_1=image_1, image_2=image_2, image_3=image_3 )
        db.session.add(addpro)
        flash(f'Produto {name} foi cadastrado com sucesso','success')
        db.session.commit()
        return redirect(url_for("login"))
        
    return render_template('produtos/addproduto.html', title="Cadastrar Produtos", form=form, marcas=marcas,
    categorias=categorias)