# Importando o Blueprint
from flask import Blueprint

#Instanciar o blueprint
ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/uc')
def uc_list():
    return "Teste"