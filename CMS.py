from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Card Management System")


# -------------------------------
# Pydantic Model
# -------------------------------
class Details(BaseModel):
    name: str
    age: int
    aadhar: str
    legacy_id: int
    card_type: str
    status: str


# -------------------------------
# In-Memory Database
# -------------------------------
details_db: List[Details] = [
    Details(
        name="Ramesh Kumar",
        age=32,
        aadhar="1234-5678-9012",
        legacy_id=101,
        card_type="Debit",
        status="Active"
    ),
    Details(
        name="Sita Sharma",
        age=28,
        aadhar="2345-6789-0123",
        legacy_id=102,
        card_type="Credit",
        status="Inactive"
    ),
    Details(
        name="Amit Verma",
        age=40,
        aadhar="3456-7890-1234",
        legacy_id=103,
        card_type="Prepaid",
        status="Active"
    ),
]


# -------------------------------
# Routes
# -------------------------------

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Card Management System"}


@app.get("/details", response_model=List[Details])
def get_all_details():
    return details_db


@app.post("/details", response_model=Details)
def add_details(details: Details):
    details_db.append(details)
    return details


@app.put("/details/{id}", response_model=Details)
def update_details(id: int, updated_details: Details):
    for index, record in enumerate(details_db):
        if record.legacy_id == id:
            details_db[index] = updated_details
            return updated_details
    raise HTTPException(status_code=404, detail="Record not found")


@app.delete("/details/{id}")
def delete_details(id: int):
    for index, record in enumerate(details_db):
        if record.legacy_id == id:
            details_db.pop(index)
            return {"message": "Record deleted successfully"}
    raise HTTPException(status_code=404, detail="Record not found")
