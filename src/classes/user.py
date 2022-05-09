from msilib.schema import Class

class user(db.model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    #foreign key for socio
    socio_id = db.Column(db.Integer, db.ForeignKey('socio.id'), nullable=False)
    

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    is_deleted = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    is_locked = db.Column(db.Boolean, default=False)
    is_logged_in = db.Column(db.Boolean, default=False)
    is_online = db.Column(db.Boolean, default=False)
    is_blocked = db.Column(db.Boolean, default=False)
    is_verified = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False) 
    is_user = db.Column(db.Boolean, default=False)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
