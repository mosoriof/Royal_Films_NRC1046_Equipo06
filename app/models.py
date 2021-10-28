from app import db


class User(db.Model):
    __tablename__ = 'user';
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    celNum = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.email
    
    
class Movie(db.Model):
    __tablename__ = 'movie'
    movie_id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(255), unique=True)
    poster_file = db.Column(db.String(255), nullable=False)  
    trailer_url = db.Column(db.String(255), nullable=False)  
    synopsis = db.Column(db.Text, nullable=False) 
    length = db.Column(db.String(100), nullable=False) 
    format = db.Column(db.String(50), nullable=False)
    genre= db.Column(db.String(50), nullable=False)
    rating = db.Column(db.String(50), nullable=False)
    cast = db.Column(db.String(255), nullable=False)  
    release = db.Column(db.String(50), nullable=False)  
    status = db.Column(db.String(50), nullable=False)
    

    def __repr__(self):
        return '<Movie %r>' % self.title


class Review(db.Model):
    __tablename__ = 'review'
    comment_id = db.Column(db.Integer, primary_key=True) 
    comment = db.Column(db.String(255))
    rating = db.Column(db.String(50), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id')) 
    

    def __repr__(self):
        return '<Review %r>' % self.comment_id
    
    
class Screening(db.Model):
    __tablename__ = 'screening'
    screening_id = db.Column(db.Integer, primary_key=True) 
    date = db.Column(db.String(50))  
    time = db.Column(db.String(50))  
    number_seats = db.Column(db.String(50))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'))

    def __repr__(self):
        return '<Screening %r>' % self.screening_id
    

class Booking(db.Model):
    __tablename__ = 'booking'
    booking_id = db.Column(db.Integer, primary_key=True) 
    date = db.Column(db.String(50))  
    time = db.Column(db.String(50))  
    number_tickets = db.Column(db.String(50))
    seats = db.Column(db.String(50))
    payment = db.Column(db.String(50))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id')) 
    screening_id = db.Column(db.Integer, db.ForeignKey('screening.screening_id'))     

    def __repr__(self):
        return '<Booking %r>' % self.booking_id