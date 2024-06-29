from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hospital_endpoint = fields.Char(string='Endpoint del WebService', config_parameter='vertical_hospital.endpoint')