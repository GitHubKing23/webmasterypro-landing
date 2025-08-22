from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="WebMasteryPro Landing API")

class PageRequest(BaseModel):
    brand: str
    business: str
    audience: str
    location: str
    tone: str

@app.post("/generate")
def generate_page(data: PageRequest):
    title = f"{data.business} in {data.location} | {data.brand}"
    meta = f"{data.brand} offers {data.business.lower()} for {data.audience} in {data.location}."
    html = f"<html><head><title>{title}</title><meta name='description' content='{meta}'/></head><body><h1>{title}</h1><p>{meta}</p></body></html>"
    return {"title": title, "meta": meta, "html": html}
