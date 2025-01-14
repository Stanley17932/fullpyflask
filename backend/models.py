from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.String(50))
    message = db.Column(db.String(200))

    def __init__(self, first_name,last_name, email, phone, message):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.message = message

    def to_json(self):
        return {
            'id': self.id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'message': self.message
        }