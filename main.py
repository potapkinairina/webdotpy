import web

from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

db = web.database(dbn = 'sqlite', db = 'irina.db')
render = web.template.render('templates/')

urls = ('/(.*)', 'index')

app = web.application(urls, globals())

def selectCat():
    return db.select('categories')


def selectGoods(cat):
    catwhere = "category=%s" % (cat)
    return db.select('goods', where=catwhere)


def selectProducts(id):
    goodwhere = "id=%s" % (id)
    return db.select('goods', where=goodwhere)


class index:
    def GET(self, name):
        goods = db.select('goods')
        products = selectProducts(-1)
        categories = selectCat()
        carts = db.query("SELECT cart.id, goods.name, cart.count, goods.price FROM cart JOIN goods WHERE cart.good = goods.id")
        form = web.input(cat = None, good = None)

        if name == "view" and form.cat and not form.good:
            goods = selectGoods(form.cat)
            products = selectProducts(-1)
            return render.index3(categories, goods, products, carts)


        if name == "view" and form.cat and form.good:
            goods = selectGoods(form.cat)
            products = selectProducts(form.good)
            return render.index3(categories, goods, products, carts)


        if name == "newcart":
            db.insert('cart', good = form.good, count = 1)
            raise web.seeother('/')            

        
        if name == "del":
            cartwhere = "id=%s" % (form.cart)
            db.delete('cart', where=cartwhere)
            raise web.seeother('/')            


        return render.index3(categories, goods, products, carts)


if __name__ == "__main__":
    app.run()