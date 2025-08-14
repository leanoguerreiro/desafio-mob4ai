from fastapi import APIRouter

from fastapi.params import Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import Processes1

from utils.parse_metrics import parse_metrics

from fastapi.responses import JSONResponse

from schemas import ProcessSchema

from database.database import get_db

process_router = APIRouter(prefix="/process", tags=["process"])

@process_router.get("/processes", response_model=list[ProcessSchema])
async def get_processes(db: Session = Depends(get_db)):
    processes = db.query(Processes1).all()
    return [
        {
            "PackageName": process.PackageName,
            "Uid": process.Uid,
            "Metrics": parse_metrics(process.Metrics)  # Converte a string para um dicionário
        }
        for process in processes
    ]