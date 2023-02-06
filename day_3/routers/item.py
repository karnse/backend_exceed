from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel

class ItemDetail(BaseModel):
    item_color:str
    item_detail:str

class Item(BaseModel):
    item_id:Union[int,str]=0
    item_name:str=' '
    item_bool:bool=False
    item_detail:ItemDetail
router = APIRouter(prefix='/items')


@router.post('/1/foo/true')
def show_item():
    return {"msg":"order"}
@router.post("",status_code=201)
def create_item():
    return {"massage":"created"}

@router.post('/{item_id}/{item_name}/{item_bool}')
def show_item(item_id:Union[int,str],item_name:str,item_bool:bool):
    return {"item_id": item_id,"item_name":item_name,"item_bool":item_bool}
@router.get("/")
def query_item(item_id:int=0,item_name:str= " ",item_bool:bool|None=None):
    if(item_bool==None):
        return {"item_id": item_id,"item_name":item_name}
    return {"item_id": item_id,"item_name":item_name,"item_bool":item_bool}

@router.get('/with_body')
def show_item_body(Item:Item, detail:ItemDetail):
    return {"item":Item,"Detail":detail}

@router.get('/with_body_with_params')
def show_item_body(Item:Item):
    return {"item":Item}

@router.get("/combine/{item_id}")
def combine_all_params(item_id:str,item_name:str,item_detail:ItemDetail):
    return {"item_id":item_id,"item_name":item_name,"item_detail":item_detail}