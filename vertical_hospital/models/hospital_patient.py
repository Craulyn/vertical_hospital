from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Paciente'
    

    name = fields.Char(string='Secuencia', readonly=True, copy=False, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('hospital.patient'))
    first_name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellido', required=True)
    rnc = fields.Char(string='RNC')
    treatment_ids = fields.Many2many('hospital.treatment', string='Tratamientos realizados')
    admission_date = fields.Datetime(string='Fecha de alta', default=fields.Datetime.now)
    update_date = fields.Datetime(string='Fecha de actualización', default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('alta', 'Alta'),
        ('baja', 'Baja')
    ], string='Estado', default='draft')

    @api.onchange('rnc')
    def _onchange_rnc(self):
        if self.rnc and not self.rnc.isdigit():
            raise ValidationError('El RNC solo puede contener números.')

    def write(self, vals):
        if 'rnc' in vals:
            self.message_post(body='Se ha modificado el RNC del paciente.')
        elif 'state' in vals:
            self.message_post(body='Se ha modificado el estado del paciente.')
        return super(HospitalPatient, self).write(vals)