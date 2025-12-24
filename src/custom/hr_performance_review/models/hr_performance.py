from odoo import models, fields, api

class HrPerfomanceReview(models.Model):

    _name = 'hr.performance.review'
    _description = 'Evaluación de Desempeño'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2one('hr.employee', string = 'Empleado Evaluado', required=True, tracking=True)
    review_date = fields.Date(string = 'Fecha de Evaluación', default = fields.Date.context_today, tracking = True)
    reviewer_id = fields.Many2one('res.users', string = 'Evaluador', required = True, default = lambda self: self.env.user)

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