class socio(user, db.model):
    __tablename__ = 'socio'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    dni = db.Column(db.String(80), nullable=False)
    telefono = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    direccion = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, nombre, apellido, dni, telefono, email, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
