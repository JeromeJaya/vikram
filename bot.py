# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import litellm
import uvicorn

# Setting the Gemini API key
os.environ["GEMINI_API_KEY"] = "AIzaSyAFwiGw-g89uKy3Sgy7v5S8rklApFDL9Oc"

# Create the FastAPI app
app = FastAPI()

# Define the input schema using Pydantic
class RequirementInput(BaseModel):
    requirements: str

# API endpoint to handle requirements and interact with Gemini API
@app.post("/generate_code/")
async def generate_code(input_data: RequirementInput):
    try:
        # Interacting with Gemini API
        response = litellm.completion(
            model="gemini/gemini-1.5-flash",
            messages=[{"role": "user", "content": f"write a code for the given requirements: {input_data.requirements}"}]
        )
        
        # Extracting the generated code
        generated_code = response.choices[0].message.json()

        return {"code": generated_code, "message": "Code generated and requirements.txt created successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")


# Main block to run the app on port 6012
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6012)
