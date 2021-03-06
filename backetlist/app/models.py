from app import db

class Bucketlist(db.Model):
    """ Represents the bucketlist table"""
    
    __tablename__ = 'bucketlist'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestampt())
    
    def __init__(self, name):
        """ Initialize with name"""
        self.name = name
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get_all():
        return Bucketlist.query.all()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def __repr__(self):
        return "<Bucketlist: {}>".format(self.name)
        