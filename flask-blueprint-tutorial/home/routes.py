from flask import Blueprint
from flask import current_app as app


# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@home_bp.route('/', methods=['GET'])
def home():
    """ Homepage """
    products = fetch_products(app)
    return render_template(
        'index.html',
        title='Flask Blueprint',
        subtitle='Demonstration of Flask blueprints in action',
        template='home-template',
        products=products
    )

