from flask import redirect, render_template, url_for, flash, request, session
from .forms import Addprodutos
from loja import db, app, photos
from .models import Marca, Categoria, Addproduto
import secrets


@app.route('/addmarca', methods=['GET','POST'])
def addmarca():
    if 'email' not in session:
        flash('Favor efetuar login primeiro', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getmarca = request.form.get('marca')
        marca = Marca(name=getmarca)
        db.session.add(marca)
        flash(f'A marca {getmarca} foi cadastrada com sucesso','success')
        db.session.commit()
        return redirect(url_for('addmarca'))
    return render_template('/produtos/addmarca.html', marcas='marcas')

@app.route('/updatemarca/<int:id>', methods=['GET','POST'])
def updatemarca(id):
    if 'email' not in session:
        flash('Favor efetuar login primeiro', 'danger')
        return redirect(url_for('login'))

    updatemarca= Marca.query.get_or_404(id)
    marca = request.form.get('marca')
    if request.method == 'POST':
        updatemarca.name = marca
        flash(f'Sua marca foi atualizada com sucesso','success')
        db.session.commit()
        return redirect(url_for('marcas'))
    return render_template('/produtos/updatemarca.html', title='Atualizar Fabricantes', updatemarca=updatemarca)

@app.route('/updatecat/<int:id>', methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash('Favor efetuar login primeiro', 'danger')
        return redirect(url_for('login'))

    updatecat= Categoria.query.get_or_404(id)
    categoria = request.form.get('categoria')
    if request.method == 'POST':
        updatemarca.name = categoria
        flash(f'Sua categoria foi atualizada com sucesso','success')
        db.session.commit()
        return redirect(url_for('categoria'))
    return render_template('/produtos/updatemarca.html', title='Atualizar Fabricantes', updatecat=updatecat)


@app.route('/addcat', methods=['GET','POST'])
def addcat():
    if 'email' not in session:
        flash('Favor efetuar login primeiro', 'danger')
        return redirect(url_for('login'))
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
    if 'email' not in session:
        flash('Favor efetuar login primeiro', 'danger')
        return redirect(url_for('login'))
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