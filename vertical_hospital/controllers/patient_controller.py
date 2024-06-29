from odoo import http
from odoo.http import request
import json

class PacienteController(http.Controller):
    @http.route('/pacientes/consulta/<string:seq>', auth='public', type='http', methods=['GET'], csrf=False)
    def consulta_paciente(self, seq):
        paciente = request.env['hospital.patient'].search([('name', '=', seq)], limit=1)
        if paciente:
            data = {
                'seq': paciente.name,
                'name': f"{paciente.first_name} {paciente.last_name}",
                'rnc': paciente.rnc,
                'state': paciente.state,
            }
            return request.make_response(json.dumps(data), headers=[('Content-Type', 'application/json')])
        else:
            return request.not_found()
        
