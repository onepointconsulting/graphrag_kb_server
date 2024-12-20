from typing import Tuple
from pathlib import Path
import shutil

from graphrag_kb_server.config import cfg
from graphrag_kb_server.model.jwt_token import JWTToken
from graphrag_kb_server.model.error import Error, ErrorCode

TENNANT_JSON = "tennant.json"


def get_folder(jwt_token: JWTToken) -> Tuple[Path, str]:
    folder_name = jwt_token.folder_name
    return cfg.graphrag_root_dir_path / folder_name, folder_name


def create_tennant_folder(jwt_token: JWTToken) -> str | Error:
    folder_path, folder_name = get_folder(jwt_token)
    if not folder_path.exists():
        folder_path.mkdir()
        descriptor = folder_path / TENNANT_JSON
        descriptor.write_text(jwt_token.model_dump_json(), encoding="utf-8")
    else:
        return Error(
            error_code=ErrorCode.PROJECT_EXISTS,
            error="Folder exists",
            description=f"Folder {folder_name} already exists. Choose another one.",
        )
    return folder_name


def delete_tennant_folder(jwt_token: JWTToken) -> str | None:
    folder_path, folder_name = get_folder(jwt_token)
    if folder_path.exists():
        shutil.rmtree(folder_path)
        return folder_name
    return None