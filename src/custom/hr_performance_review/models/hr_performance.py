from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class HrPerfomanceReview(models.Model):

    _name = 'hr.performance.review'
    _description = 'Evaluación de Desempeño'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2one('hr.employee', string = 'Empleado Evaluado', required=True, tracking=True)
    review_date = fields.Date(string = 'Fecha de Evaluación', default = fields.Date.context_today, tracking = True)
    reviewer_id = fields.Many2one('res.users', string='Evaluador', required=True, default=lambda self: self.env.user, domain=lambda self: [('groups_id', 'in', [self.env.ref('hr.group_hr_user').id])], tracking=True)

    score = fields.Float(string = 'Calificación Numérica', tracking = True)
    comments = fields.Text(string = 'Observaciones cualitativas')
    goals_next_period = fields.Text(string = 'objetivos para el siguiente ciclo')
    strengths = fields.Text(string = 'Fortalezas')
    weaknesses = fields.Text(string = 'Debilidades')


    #Kanban
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('completed', 'Completado')
    ], string = 'Estado', default = 'pending', tracking = True)

    def action_complete(self):
        self.state = 'completed'

    #validacion
    @api.constrains('review_date')
    def _check_review_date(self):
        for record in self:
            if record.review_date > date.today():
                raise ValidationError('La fecha de evaluación no puede ser mayor a la fecha actual')

    @api.constrains('score')
    def _check_score(self):
        for record in self:
            if record.score < 0 or record.score > 10:
                raise ValidationError('La calificación debe estar entre 0 y 10')

    @api.constrains('employee_id', 'reviewer_id')
    def _check_reviewer_not_employee(self):
        for record in self:
            if record.employee_id.user_id == record.reviewer_id:
                raise ValidationError("Un empleado no puede ser su propio evaluador. Por favor, asigne a un supervisor o compañero diferente.")
                
    @api.constrains('reviewer_id')
    def _check_reviewer_is_hr(self):
        """Verifica que el evaluador pertenezca al grupo de Recursos Humanos"""
        hr_group = self.env.ref('hr.group_hr_user')
        for record in self:
            
            if record.reviewer_id and hr_group not in record.reviewer_id.groups_id:
                raise ValidationError("El evaluador seleccionado debe pertenecer al grupo de Recursos Humanos.")

    
    @api.constrains('employee_id', 'reviewer_id')
    def _check_reviewer_not_employee(self):
        """Evita que un empleado se evalúe a sí mismo"""
        for record in self:
            
            if record.employee_id.user_id == record.reviewer_id:
                raise ValidationError("Un empleado no puede ser su propio evaluador. Por favor, asigne a otra persona.")                        
                
    _sql_constraints = [
    ('performance_unique', 'unique(employee_id, review_date)', '¡Ya existe una evaluación para este empleado en esta fecha!')
    ]

