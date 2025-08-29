from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Conexiune MySQL
engine = create_engine("mysql+mysqldb://snake:adidas88_AS@localhost/BalabacDB", echo=False)
#engine = create_engine("mysql+pymysql://snake:adidas88_AS@localhost/BalabacDB", echo=False)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Modele
class Department(Base):

    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    employees = relationship("Employee", back_populates="department")

class Employee(Base):

    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship("Department", back_populates="employees")

# Creăm tabelele
Base.metadata.create_all(engine)

# Inserăm date
#departments = [Department(name=f"Department {i}") for i in range(1, 11)]
#session.add_all(departments)
#session.commit()

employees = [
    Employee(name="Alice", department_id=1),
    Employee(name="Bob", department_id=2),
    Employee(name="Charlie", department_id=1),
    Employee(name="Diana", department_id=4),
    Employee(name="Ethan", department_id=1),
    Employee(name="Fiona", department_id=5),
    Employee(name="George", department_id=1),
    Employee(name="Hannah", department_id=5),
    Employee(name="Ian", department_id=None),
    Employee(name="Julia", department_id=None)
]
session.add_all(employees)
session.commit()

# LEFT JOIN + GROUP BY
results = (
    session.query(
        Department.name,
        func.count(Employee.id).label("employee_count")
    )
    .outerjoin(Employee, Department.id == Employee.department_id)
    .group_by(Department.id)
    .all()
)

# Afișare rezultate
print("\n📊 Număr de angajați per departament:")
for dept_name, count in results:
    print(f"{dept_name}: {count} angajați")
