import os
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from ..infrastructure.dependencies.db import *
from .BaseController import BaseController  # Adjust the import path as necessary
from ..infrastructure.web.bind.decorator import *
from ..infrastructure.lang import *
from ..infrastructure.http import *

# Directory (relative to the app working directory) where uploaded txt files are stored.
TXT_UPLOAD_DIR = os.path.join("accountslogin", "src", "main", "resources", "uploads", "txt")

@RequestMapping("")
class IndexController(BaseController):
    def __init__(self):
        super().__init__()  # Call the super class initializer to ensure it's properly initialized
    
    
    @RequestMapping("", method = RequestMethod.GET, name="IndexController.default")
    @RequestMapping("/index/", method = RequestMethod.GET, name="IndexController.index")
    async def index(self, request: Request, db: AsyncSession = Depends(get_db)):
        request: WebRequest = WebRequest(request)
        self.logger.info("Entering index method in IndexController.")
        return self.render(request, "index.html", self.context)

    @RequestMapping("/index_content/", method = RequestMethod.GET, name="IndexController.index_content")
    async def indexcontent(self, request: Request, db: AsyncSession = Depends(get_db)):
        request: WebRequest = WebRequest(request)
        self.logger.info("Entering indexcontent method in IndexController.")
        return self.render(request, "index_content.html", self.context)

    @staticmethod
    def _safe_txt_name(filename: str) -> str:
        """Strip any directory components and enforce a .txt extension to avoid path traversal."""
        base = os.path.basename(filename or "").strip()
        if not base:
            raise HTTPException(status_code=400, detail="Missing file name.")
        name, ext = os.path.splitext(base)
        if ext.lower() != ".txt":
            raise HTTPException(status_code=400, detail="Only .txt files are allowed.")
        return base

    @RequestMapping("/index/upload_txt/", method = RequestMethod.POST, name="IndexController.upload_txt", response_class=JSONResponse)
    async def upload_txt(self, request: Request, file: UploadFile = File(...)):
        """Save an uploaded .txt file into uploads/txt/ and return its stored name."""
        self.logger.info("Entering upload_txt method in IndexController.")
        safe_name = self._safe_txt_name(file.filename)

        os.makedirs(TXT_UPLOAD_DIR, exist_ok=True)
        dest_path = os.path.join(TXT_UPLOAD_DIR, safe_name)

        content = await file.read()
        with open(dest_path, "wb") as out_file:
            out_file.write(content)

        return JSONResponse(content={"success": True, "filename": safe_name})

    @RequestMapping("/index/load_txt/", method = RequestMethod.GET, name="IndexController.load_txt", response_class=JSONResponse)
    async def load_txt(self, request: Request, name: str):
        """Read a previously uploaded .txt file from uploads/txt/ and return its content."""
        self.logger.info("Entering load_txt method in IndexController.")
        safe_name = self._safe_txt_name(name)
        file_path = os.path.join(TXT_UPLOAD_DIR, safe_name)

        if not os.path.isfile(file_path):
            raise HTTPException(status_code=404, detail="File not found.")

        with open(file_path, "r", encoding="utf-8", errors="replace") as in_file:
            content = in_file.read()

        return JSONResponse(content={"success": True, "filename": safe_name, "content": content})


# Register the routes from the Webpage class
RegisterRoutes.getInstance().RegisterRoutes(IndexController)