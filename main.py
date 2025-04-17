from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from controller import validate_input
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for request body validation
class ContactForm(BaseModel):
    name: str
    email: str
    message: str

@app.post("/contact-form")
async def contact_form(data: ContactForm):
    try:
        response = validate_input(data.name, data.email, data.message)
        if response:
            return JSONResponse(
                content={
                    "message": "Form submitted successfully",
                    "response": response
                },
                status_code=200
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
