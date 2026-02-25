from odoo import fields, models

class Student(models.Model):
    _name = 'student.student'
    description = 'Student info'

    name = fields.Char('Student Name')
    student_id = fields.Char('Student ID')
    image = fields.Char('Student Image')
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
