from enum import Enum

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ParameterTypes(str, Enum):
    START = 'start'
    END = 'end'

class Processes1(Base):

    __tablename__ = 'processes1'
    PackageName = Column(String, primary_key=True, index=True)
    Uid = Column(Integer, index=True)
    Pids = Column(String, index=True)
    Metrics = Column(String)
    Bytesize = Column(String)
    
    
    def __init__(self, package_name, uid, metrics, parameters, bytesize, pids):
        super().__init__()
        self.PackageName = package_name
        self.Uid = uid
        self.Metrics = metrics
        self.Bytesize = bytesize
        self.Pids = pids
        
 