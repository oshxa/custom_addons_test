from odoo import fields, models, api
from odoo.http import request
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = 'student.student'
    description = 'Student info'

    name = fields.Char('Student Name')
    student_id = fields.Char('Student ID', required=True)
    image = fields.Binary('Student Image')
    dob = fields.Date('Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ],string='Gender')
    email = fields.Char('Email Address')
    phone = fields.Char('Phone Number')
    address = fields.Char('Address')
    guardian_name = fields.Char('Guardian Name')

    guardian_phone = fields.Char('Guardian Phone')
    admission_date = fields.Date('Admission Date')

    def print_something(self):
        print(self.name,'the button get clicked')

    @api.model
    def create(self,vals):
        existing_student =  request.env['student.student'].search([])
        for student in existing_student:
            if student.student_id == vals.get('student_id'):
                raise ValidationError('Student ID is already in use')
        return super().create(vals)

    def write(self,vals):
        existing_student = request.env['student.student'].search([])
        for student in existing_student:
            if student.student_id == vals.get('student_id'):
                raise ValidationError('Student ID is already in use')
        return super().write(vals)