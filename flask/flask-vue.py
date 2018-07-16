from views import app
from views.vue_test import HelloWorld, GetProxy
from flask_restful import  Api


api = Api(app)
api.add_resource(GetProxy, '/')

if __name__ == '__main__':
    app.run(debug=True)
