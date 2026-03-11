from sqlmodel import SQLModel, create_engine

sqlite_file_name = "library.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)