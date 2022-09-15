# Importando o Blueprint, render_template
from flask import Blueprint, render_template

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
    ucs_query = Uc.query.all()
    return render_template('uc_list.html', ucs = ucs_query)