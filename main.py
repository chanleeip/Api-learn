'''
This is a sample fastapi application
'''

from typing import Annotated
from fastapi import FastAPI, Query,Path



app=FastAPI()

@app.get("/")
def read_root():
    '''
    This return the home page
    '''
    return "Hello,world"

@app.get("/item/{path}")
def read_item(path:Annotated[int | None,Path(...)]):
    '''this return norhing'''
    return f"the path is {path}"


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[str, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results