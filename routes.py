from fastapi import APIRouter

from fastapi.params import Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import Processes1, Processes2, Processes3


from utils.parse_metrics import parse_metrics

from fastapi.responses import JSONResponse

from schemas import ProcessSchema

from database.database import get_db

process_router = APIRouter(prefix="/process", tags=["process"])

@process_router.get("/processes", response_model=list[ProcessSchema])
async def get_processes(db: Session = Depends(get_db)):
    
    processes1 = db.query(Processes1).all()
    processes2 = db.query(Processes2).all()
    processes3 = db.query(Processes3).all()
    processes = processes1 + processes2 + processes3
    return [
        {
            "PackageName": process.PackageName,
            "Uid": process.Uid,
            "Metrics": parse_metrics(process.Metrics) or {
                "timestamp": 0,  # Valor padrão
                "usagetime": 0,  # Valor padrão
                "delta_cpu_time": 0,
                "cpu_usage": 0.0,
                "rx_data": 0,
                "tx_data": 0,
            }        
        }
        for process in processes
    ]