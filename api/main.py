import strawberry
import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from strawberry.fastapi import GraphQLRouter

"""
Example query:
{
  ping(message: "Ciao")
  allFilms {
    films {
      id
      title
      director
    }
  },
}
"""

@strawberry.type
class Film:
    id: str
    title: str
    director: str

@strawberry.type
class FilmList:
    films: list[Film]

@strawberry.type
class MyAPIQuery:
    @strawberry.field
    def allFilms(self) -> FilmList:
        return FilmList(films=[
            Film(id="1", title="The Empire Strikes Back", director="Irvin Kershner"),
            Film(id="2", title="A New Hope", director="George Lucas"),
            Film(id="3", title="Return of the Jedi", director="Richard Marquand"),
            Film(id="4", title="The Phantom Menace", director="George Lucas"),
            Film(id="5", title="Attack of the Clones", director="George Lucas"),
            Film(id="6", title="Revenge of the Sith", director="George Lucas"),
            Film(id="7", title="The Force Awakens", director="J.J. Abrams"),
            Film(id="8", title="The Last Jedi", director="Rian Johnson"),
            Film(id="9", title="The Rise of Skywalker", director="J.J. Abrams"),
            Film(id="10", title="Rogue One", director="Gareth Edwards"),
            Film(id="11", title="Solo", director="Ron Howard")
        ])

    @strawberry.field
    def ping(self, message: str) -> str:
        return f"Ack: {message}"



schema = strawberry.Schema(MyAPIQuery)

graphql_app = GraphQLRouter(schema)

app = FastAPI()

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://localhost:\d+",  # 允许localhost任何端口
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有请求头
)

# 构建前端路径
frontend_dist_path = Path(__file__).parent.parent / "frontend" / "dist"

# 如果前端已构建，则服务静态文件
if frontend_dist_path.exists():
    # 服务静态文件（JS, CSS, 图片等）
    app.mount("/assets", StaticFiles(directory=frontend_dist_path / "assets"), name="assets")
    
    # 服务根路径下的静态文件
    app.mount("/static", StaticFiles(directory=frontend_dist_path), name="static")
    
    # 处理所有其他路由，返回index.html（用于React Router）
    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        # 检查文件是否存在
        file_path = frontend_dist_path / full_path
        if file_path.exists() and file_path.is_file():
            return FileResponse(file_path)
        
        # 否则返回index.html（用于SPA路由）
        return FileResponse(frontend_dist_path / "index.html")
else:
    # 如果前端未构建，提供提示信息
    @app.get("/")
    async def root():
        return {
            "message": "Backend API is running. Please build the frontend first with 'npm run build' in the frontend directory.",
            "graphql_endpoint": "/graphql"
        }

# 最后添加GraphQL路由，确保它不会被通配符路由拦截
app.include_router(graphql_app, prefix="/graphql")