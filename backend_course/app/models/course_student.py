from sqlalchemy import Column, Integer, DateTime, ForeignKey
from db.database import Base
from datetime import datetime

class CourseStudent(Base):
    __tablename__ = "course_students"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    student_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)