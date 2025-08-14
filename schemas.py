from pydantic import BaseModel

class Metrics(BaseModel):
    timestamp: int
    usagetime: int
    delta_cpu_time: int
    cpu_usage: float
    

class ProcessSchema(BaseModel):
    PackageName: str
    Uid: int
    Metrics: Metrics
    
    class Config:
        from_atributes = True