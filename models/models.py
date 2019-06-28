# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openerp.exceptions import ValidationError

# class rut_module(models.Model):
#     _name = 'rut_module.rut_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class RutValidator:

    def check_digit(self, rut):
        multipliers = '32765432'
        if len(rut) == 8:
            multipliers = '2765432'
        value = 11 - sum([ int(a)*int(b)  for a,b in zip(str(rut).zfill(len(rut)), multipliers)])%11
        return {10: 'k', 11: '0'}.get(value, str(value))
    

    def valid_rut(self, rut):
        rut_text = rut.replace('.', '')
        rut_text = rut_text.replace('-', '')
        return rut_text[-1].lower() == self.check_digit(rut_text)

    def format_rut(self, rut):
        rut_text = rut.replace('.', '')
        rut_text = rut_text.replace('-', '')
        dv = rut[-1].lower()
        return "{:,}".format(int(rut_text[:-1])).replace(',','.') + '-' + dv

class RutFIeld(models.Model):
    _inherit = 'res.partner'

    x_rut = fields.Char(required=True, string = 'RUT')

    @api.constrains('x_rut')
    def check_rut(self):
        rut_validator = RutValidator()
        for record in self:
            if not rut_validator.valid_rut(record.x_rut):
                raise ValidationError('EL rut ingresado no es valido')
    
    @api.onchange('x_rut')
    def show_message(self):
        if (self.x_rut):
            rut_validator = RutValidator()
            self.x_rut = rut_validator.format_rut(self.x_rut)

class EmployeeRutFIeld(models.Model):
    _inherit = 'hr.employee'

    x_rut = fields.Char(required=True, string = 'RUT')

    @api.constrains('x_rut')
    def check_rut(self):
        rut_validator = RutValidator()
        for record in self:
            if not rut_validator.valid_rut(record.x_rut):
                raise ValidationError('EL rut ingresado no es valido')
    
    @api.onchange('x_rut')
    def show_message(self):
        if (self.x_rut):
            rut_validator = RutValidator()
            self.x_rut = rut_validator.format_rut(self.x_rut)


    