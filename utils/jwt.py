import os
from jose import jwt,JWTError
from datetime import datetime, timedelta

SECRET_KEY=os.getenv('SECRET_KEY'," your-super-secret-key-change-it")
ALGORITHM=os.getenv('ALGORITHM',"HS256")
EXPIRE_MINUTES=int(os.getenv('EXPIRE_MINUTES','30'))

def create(username: str) -> str:
    payload= {
        "sub":username,
        "exp":datetime.utcnow()+ timedelta(minutes=EXPIRE_MINUTES)
    }
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

def verify(token:str) -> str:
    payload= jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    username=payload.get("sub")
    if not username:
        raise JWTError("token has no subjetc")
    return username