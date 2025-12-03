from fastapi import FastAPI, HTTPException
import json
from pathlib import Path
 
app = FastAPI(title="EMIS API")
 
REGISTRATIONS_FILE = Path("registrations.json")
 
 
def load_registrations():
    if not REGISTRATIONS_FILE.exists():
        return []
    with open(REGISTRATIONS_FILE, "r") as f:
        return json.load(f)
 
def save_registrations(registrations):
    with open(REGISTRATIONS_FILE, "w") as f:
        json.dump(registrations, f, indent=4)
 
 
@app.get("/")
def root():
    return {"message": "Welcome to the EMIS API!"}
 
 
# ---------------------------
# READ – Get a single registration
# ---------------------------
@app.get("/registrations/{registration_id}")
def get_registration(registration_id: int):
    registrations = load_registrations()
 
    for registration in registrations:
        if registration["RegistrationID"] == registration_id:
            return registration
 
    raise HTTPException(status_code=404, detail="Registration not found")
 
 
# ---------------------------
# READ – Get all registrations
# ---------------------------
@app.get("/registrations")
def list_registrations():
    return load_registrations()
