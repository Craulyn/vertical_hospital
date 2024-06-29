from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalTreatment(models.Model):
    _name = 'hospital.treatment'
    _description = 'Tratamiento'
    _rec_name = 'display_name'

    code = fields.Char(string='Código de tratamiento')
    name = fields.Char(string='Nombre del tratamiento')
    treating_physician = fields.Char(string='Médico tratante')
    display_name = fields.Char(compute='_compute_display_name', store=True, index=True)

    def name_get(self):
        result = []
        for rec in self:
            name = f"{rec.code} - {rec.name}"
            result.append((rec.id, name))
        return result

    @api.depends('code', 'name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.code} - {rec.name}"
            
    @api.constrains('code')
    def check_code(self):
        for record in self:
            if '026' in record.code:
                raise ValidationError("El codigo no puede contener la secuencia '026'")