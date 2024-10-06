from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Crear el motor SQLAlchemy y la sesión
DATABASE_URL = 'postgresql://postgres:postgres@localhost:15432/postgres'  # URL de conexión
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Crear todas las tablas definidas en los modelos (si aún no existen)
Base.metadata.create_all(engine)

# Función para obtener una nueva sesión
def get_session():
    return Session()

# Probar la conexión
session = get_session()

try:
    result = session.execute("SELECT 1")
    print(result.fetchone())
    print("¡Conexión exitosa!")
except Exception as e:
    print(f"Error al conectar: {e}")
finally:
    session.close()
