import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Tracks(Base):
    __tablename__ = 'tracks'
    TrackId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Name = db.Column(db.String(200), nullable=False)
    AlbumId = db.Column(db.Integer, db.ForeignKey('albums.AlbumId'))
    MediaTypeId = db.Column(
        db.Integer,
        db.ForeignKey('media_types.MediaId'),
        nullable=False,
    )
    GenreId = db.Column(db.Integer, db.ForeignKey('genres.GenreId'))
    Composer = db.Column(db.String(220))
    Milliseconds = db.Column(db.Integer, nullable=False)
    Bytes = db.Column(db.Integer)
    UnitPrice = db.Column(db.Numeric(10, 2))


class MediaTypes(Base):
    __tablename__ = 'media_types'
    MediaTypeId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Name = db.Column(db.String(120))


class Playlists(Base):
    __tablename__ = 'playlists'
    PlaylistId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Name = db.Column(db.String(120))


class Genres(Base):
    __tablename__ = 'genres'
    GenreId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Name = db.Column(db.String(120))


class Artists(Base):
    __tablename__ = 'artists'
    ArtistId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Name = db.Column(db.String(120))


class Albums(Base):
    __tablename__ = 'albums'
    AlbumId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Title = db.Column(db.String(160), nullable=False)
    ArtistId = db.Column(db.Integer, db.ForeignKey('artists.ArtistId'), nullable=False)


class Customers(Base):
    __tablename__ = 'customers'
    CustomerId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    FirstName = db.Column(db.String(40), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    Company = db.Column(db.String(80))
    Address = db.Column(db.String(70))
    City = db.Column(db.String(40))
    State = db.Column(db.String(40))
    Country = db.Column(db.String(40))
    PostalCode = db.Column(db.String(10))
    Phone = db.Column(db.String(24))
    Fax = db.Column(db.String(24))
    Email = db.Column(db.String(60), nullable=False)
    SupportRepId = db.Column(db.Integer, db.ForeignKey('employees.EmployeeId'), nullable=False)


class Employees(Base):
    __tablename__ = 'employees'
    EmployeeId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    FirstName = db.Column(db.String(20), nullable=False)
    Title = db.Column(db.String(30))
    ReportsTo = db.Column(db.Integer, db.ForeignKey('employees.EmployeeId'), nullable=False)
    BirthDate = db.Column(db.DateTime)
    HireDate = db.Column(db.DateTime)
    Address = db.Column(db.String(70))
    City = db.Column(db.String(40))
    State = db.Column(db.String(40))
    Country = db.Column(db.String(40))
    PostalCode = db.Column(db.String(10))
    Phone = db.Column(db.String(24))
    Fax = db.Column(db.String(24))
    Email = db.Column(db.String(60))


class InvoiceItem(Base):
    __tablename__ = 'invoice_items'
    InvoiceLineId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    InvoiceId = db.Column(db.Integer, db.ForeignKey('invoices.InvoiceId'), nullable=False)
    TrackId = db.Column(db.Integer, db.ForeignKey('tracks.TrackId'), nullable=False)
    UnitPrice = db.Column(db.Numeric(10, 2), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)


class Invoice(Base):
    __tablename__ = 'invoices'
    InvoiceId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    CustomerId = db.Column(db.Integer, db.ForeignKey('customers.CustomerId'), nullable=False)
    InvoiceDate = db.Column(db.DateTime, nullable=False)
    BillingAddress = db.Column(db.String(70))
    BillingCity = db.Column(db.String(40))
    BillingState = db.Column(db.String(40))
    BillingCountry = db.Column(db.String(40))
    BillingPostalCode = db.Column(db.String(10))
    Total = db.Column(db.Numeric(10, 2), nullable=False)
