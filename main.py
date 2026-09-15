from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

posts: list[dict]  = [
    {
        "id": 1,
        "author": "John Doe",
        "title": "My First Post",
        "content": "This is the content of my first post.",
        "date_posted": "2023-01-01"
    }, 
    {
        "id": 2,
        "author": "Jane Smith",
        "title": "My Second Post",
        "content": "This is the content of my second post.",
        "date_posted": "2023-01-02"
    },
    {
        "id": 3,
        "author": "Alice Johnson",
        "title": "My Third Post",
        "content": "This is the content of my third post.",
        "date_posted": "2023-01-03"
    }
]


@app.get("/", include_in_schema=False, name="home")
def get_home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})

@app.get("/api/posts")
def get_posts():
    return posts

@app.get("api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    return {"error": "post not found"}