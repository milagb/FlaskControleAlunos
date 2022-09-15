# Importando o Blueprint
from flask import Blueprint

#adicionar
from ..extensions import db
from ..models.uc import Uc

#Instanciar o blueprint
ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/uc')
def uc_list():
    # return "Teste"

#adicionar para poder criar a estrutura da tabela
    # db.create_all() --------> comentar para nao criar a tabela novamente
